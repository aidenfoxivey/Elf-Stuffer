#!/bin/env python3
# -*-coding: utf-8 -*-


from construct import (
    ConstructError,
)
import sys
import elfformat


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [a.out]")
        exit(1)

    with open(sys.argv[1], "rb") as f:
        bytes = f.read()

        data = try_parse(elfformat.elf, bytes)

        print(data)


def hexdump(b: bytes) -> None:
    import binascii

    i = 0
    while i < len(b):
        for _ in range(4):
            block = b[i : i + 8]
            if block:
                print(binascii.hexlify(block), end=" ")
            i += 8
            print()


def try_parse(format, bytes):
    try:
        data = format.parse(bytes)
    except ConstructError as e:
        print(e)
        exit(1)
    return data


if __name__ == "__main__":
    main()
