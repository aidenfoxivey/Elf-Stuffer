#!/bin/env python3


from construct import Struct, Const, Int8ul, Int16ul, Array, Byte, this, Padding, Int32ul, Int64ul
import sys


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [a.out]")
        exit(1)

    with open(sys.argv[1], "rb") as f:
        bytes = f.read()
        format = Struct(
            "signature" / Const(b"\x7fELF"),
            "class" / Int8ul,
            "endian" / Int8ul,
            "version" / Int8ul,
            "abi" / Int8ul,
            Padding(8),
            "type" / Int16ul,
            "machine" / Int16ul,
            "version" / Int32ul,
            "entry_point" / Int64ul,
            "program_header_offset" / Int64ul,
            "section_header_offset" / Int64ul,
            "flags" / Int32ul,
            "header_size" / Int16ul,
            "entry_size" / Int16ul,
            "entry_count" / Int16ul,
            "entry_index" / Int16ul,
            "section_size" / Int16ul,
            "section_count" / Int16ul,
            "section_index" / Int16ul,
        )
        data = format.parse(bytes)
        print(data)


if __name__ == "__main__":
    main()
