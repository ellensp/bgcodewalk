# bgcodewalk

    Prusa recently published the documentation for a binary encoded gcode file
    here https://github.com/prusa3d/libbgcode/blob/main/doc/specifications.md

    I wanted a way to view alot more of the structure of this file.

    bgcodewalk does this

### Example 

In https://github.com/prusa3d/libbgcode/tree/main/tests/data is an example file mini_cube_b.bgcode

You can now decode this file,

### Example output
```
Header:
    Magic Number: GCDE
    version: 1
    checksum: 1 [CRC32]
Block Header:
    type: 0 [File Metadata Block]
    compression: 0 [No compression]
    uncompressed_size: 27
Block:
    encoding: 0 [INI]
    data: Producer=PrusaSlicer 2.6.0
    checksum: 1107857561
Block Header:
    type: 3 [Printer Metadata Block]
    compression: 0 [No compression]
    uncompressed_size: 345
Block:
    encoding: 0 [INI]
    data: printer_model=MINI
          filament_type=PETG
          nozzle_diameter=0.4
          bed_temperature=90
          brim_width=0
          fill_density=15%
          layer_height=0.15
          temperature=240
          ironing=0
          support_material=0
          max_layer_z=18.05
          extruder_colour=""
          filament used [mm]=986.61
          filament used [cm3]=2.37
          filament used [g]=3.01
          filament cost=0.08
          estimated printing time (normal mode)=32m 6s
    checksum: 1322088737
Block Header:
    type: 5 [Thumbnail Block]
    compression: 0 [No compression]
    uncompressed_size: 461
Block:
    format: 0 [PNG]
    width: 16
    height: 16
    data: Binary data skipped
    checksum: 857325959
Block Header:
    type: 5 [Thumbnail Block]
    compression: 0 [No compression]
    uncompressed_size: 4836
Block:
    format: 0 [PNG]
    width: 220
    height: 124
    data: Binary data skipped
    checksum: 1248255378
Block Header:
    type: 4 [Print Metadata Block]
    compression: 0 [No compression]
    uncompressed_size: 248
Block:
    encoding: 0 [INI]
    data: filament used [mm]=986.61
          filament used [cm3]=2.37
          filament used [g]=3.01
          filament cost=0.08
          total filament used [g]=3.01
          total filament cost=0.08
          estimated printing time (normal mode)=32m 6s
          estimated first layer printing time (normal mode)=1m 8s
    checksum: 3874661661
Block Header:
    type: 2 [Slicer Metadata Block]
    compression: 1 [Deflate algorithm]
    uncompressed_size: 9745
    compressed_size: 3383
Block:
    encoding: 0 [INI]
    data: Binary data skipped
    checksum: 798982874
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 37969
    compressed_size: 14537
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 275413227
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 37022
    compressed_size: 14920
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 3841336050
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 37048
    compressed_size: 14467
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 3571696445
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 37123
    compressed_size: 14582
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 2540499508
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 37127
    compressed_size: 14454
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 2693658072
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 36902
    compressed_size: 15137
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 3637508086
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 37154
    compressed_size: 14504
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 3661250819
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 36921
    compressed_size: 15205
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 4109584004
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 37123
    compressed_size: 14516
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 424206192
Block Header:
    type: 1 [GCode Block]
    compression: 3 [Heatshrink algorithm with window size 12 and lookahead size 4]
    uncompressed_size: 19618
    compressed_size: 7350
Block:
    encoding: 2 [MeatPack algorithm modified to keep comment lines]
    data: Binary data skipped
    checksum: 3686292011
end of file
```