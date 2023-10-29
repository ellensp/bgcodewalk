#!/usr/bin/env python
#
#    bgcodewalk.py - Display structure of a binary gcode file
#
#    As ducumented https://github.com/prusa3d/libbgcode/blob/main/doc/specifications.md

import sys, struct, os

checksum_types          = ["none", "CRC32"]
block_types             = ["File Metadata Block", "GCode Block", "Slicer Metadata Block", "Printer Metadata Block", "Print Metadata Block", "Thumbnail Block"]
compression_types       = ["No compression","Deflate algorithm","Heatshrink algorithm with window size 11 and lookahead size 4","Heatshrink algorithm with window size 12 and lookahead size 4"]
gcode_encoding_types    = ["No encoding", "MeatPack algorithm", "MeatPack algorithm modified to keep comment lines"]
metadata_encoding_types = ["INI"]
format_types            = ["PNG","JPG",'QOI']

def error(descr):
    # print error and exit
    sys.exit(f"Error: {descr}.")

def getbytes(handle, length):
    # read bytes from file
    assert isinstance(length, int)
    data = handle.read(length)
    if len(data) < length:
        sys.exit("end of file")
    return data

def printval(descr, value):
    # print a value with description
    assert isinstance(value, int) or isinstance(value, str) \
    or isinstance(value, bytes)
    if isinstance(value, bool):
       value = ("no", "yes")[value]
    elif isinstance(value, bytes):
        value = value.decode("ascii", errors="backslashreplace")
    print(4 * " " + f"{descr}: {value}")

def printvalanddecode(descr, value, table):
    # print a value with description and decode value
    print(4 * " " + f"{descr}: {value} [{table[value]}]")

def read_header(handle):
    # read Header from current file position; return file version and checksum type
    (id_, version, checksum) = struct.unpack("4sIH", getbytes(handle, 10))
    if id_ != b"GCDE":
        error("not a bgcode file")
    return version, checksum

def read_block_header(handle):
    # read Block Header from current file position; return type, compression, uncompressed_size
    (type, compression, uncompressed_size) = struct.unpack("HHI", getbytes(handle,8))
    return type, compression, uncompressed_size

def read_block_header_end(handle):
    # read Block Header from current file position; return compressed_size
    compressed_size = struct.unpack("I", getbytes(handle, 4))
    return compressed_size[0]

def read_file_metadata(handle, length):
    (data) = struct.unpack("1s", getbytes(handle, 1))
    return data

def decode_metadata_block(handle,data_size,checksum,compression):
    (encoding) = struct.unpack("H", getbytes(handle,2))
    print("Block:")
    printvalanddecode("encoding",encoding[0],metadata_encoding_types)
    if compression == 0:
       bytes = getbytes(handle, data_size)
       printval("data",bytes.decode("utf-8").rstrip().replace('\n', '\n          '))
    else:
       printval("data", "Binary data skipped")
       handle.seek(handle.tell()+data_size)
    if checksum > 0:
       (checksum) = struct.unpack("I", getbytes(handle,4))
       printval("checksum",checksum[0])

def decode_gcode_block(handle,data_size,checksum,compression):
    (encoding) = struct.unpack("H", getbytes(handle,2))
    print("Block:")
    printvalanddecode("encoding",encoding[0],gcode_encoding_types)
    if compression == 0 and encoding[0] == 0:
       bytes = getbytes(handle, data_size)
       printval("data",bytes.decode("utf-8").rstrip().replace('\n', '\n          '))
    else:
       printval("data", "Binary data skipped")
       handle.seek(handle.tell()+data_size)
    if checksum > 0:
       (checksum) = struct.unpack("I",getbytes(handle,4))
       printval("checksum",checksum[0])

def decode_Thumbnail_block(handle,data_size,checksum):
    (format, width, height) = struct.unpack("HHH", getbytes(handle,6))
    print("Block:")
    printvalanddecode("format",format,format_types)
    printval("width", width)
    printval("height", height)
    printval("data", "Binary data skipped")
    handle.seek(handle.tell()+data_size)
    if checksum > 0:
       (checksum) = struct.unpack("I", getbytes(handle,4))
       printval("checksum",checksum[0])

def read_file(handle):
    handle.seek(0)

    version,checksum = read_header(handle)
    print("Header:")
    printval("Magic Number", "GCDE")
    printval("version", version)
    printvalanddecode("checksum", checksum,checksum_types)

    if version != 1:
        error("Unknown version")

    while(1):
        type, compression, uncompressed_size = read_block_header(handle)
        print("Block Header:")
        printvalanddecode("type",type,block_types)
        printvalanddecode("compression",compression,compression_types)

        printval("uncompressed_size", uncompressed_size)
        if compression != 0:
            compressed_size = read_block_header_end(handle)
            printval("compressed_size", compressed_size)
            data_size = compressed_size
        else:
            data_size = uncompressed_size

        if type == 0:  #"File Metadata Block"
            decode_metadata_block(handle,data_size,checksum,compression)
        if type == 1:  #"GCode Block"
            decode_gcode_block(handle,data_size,checksum,compression)
        if type == 2:  #"Slicer Metadata Block"
            decode_metadata_block(handle,data_size,checksum,compression)
        if type == 3:  #"Printer Metadata Block"
            decode_metadata_block(handle,data_size,checksum,compression)
        if type == 4:  #"Print Metadata Block"
            decode_metadata_block(handle,data_size,checksum,compression)
        if type == 5:  #"Thumbnail Block"
            decode_Thumbnail_block(handle,data_size,checksum)

def main(argv):
    # parse command line argument
    if len(sys.argv) != 2:
        sys.exit(
            "Print the high-level structure of a bgcode file. Argument: file to read."
        )
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        error("input file not found")

    try:
        with open(filename, "rb") as handle:
            read_file(handle)
    except OSError:
        error("could not read input file")

if __name__ == '__main__':
    sys.exit(main(sys.argv))