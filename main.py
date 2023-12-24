#!/bin/env python3

from enum import Enum
import sys

class Elf:
    pass


class Class(Enum):
    ThirtyTwo = 1
    SixtyFour = 2


class Endian(Enum):
    Little = 1
    Big = 2


class Version(Enum):
    One = 1


class OSABI(Enum):
    SysV = 0


class Type(Enum):
    NONE = 0
    REL = 1
    EXEC = 2
    DYN = 3
    CORE = 4


class Machine(Enum):
    X86 = 1
    X86_64 = 2


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [a.out]")
        exit(1)

    with open(sys.argv[1], "rb") as f:
        bytes = f.read()
        magic = bytes[0:4]

        if magic != b'\x7fELF':
            print("Not an ELF file!")
            exit(1)

        class_ = int(bytes[4])
        endian = int(bytes[5])
        version = int(bytes[6])
        os_abi = int(bytes[7])
        type = int.from_bytes(bytes[16:18], byteorder="little")
        machine = bytes[18:20]
        entry_point = int.from_bytes(bytes[24:32], byteorder="little")
        tbl_offset_prg = int.from_bytes(bytes[32:40], byteorder="little")
        tbl_offset_sec = int.from_bytes(bytes[40:48], byteorder="little")

        print(f"{magic} {class_} {endian} {version} {os_abi}")
        print(f"{type} {machine} {entry_point} {tbl_offset_prg} {tbl_offset_sec}")


if __name__ == "__main__":
    main()
