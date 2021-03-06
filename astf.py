#!/usr/bin/env python3

# astf --> Add Sizes To File

import os
import sys
from PIL import Image


def process(filename):
    im = Image.open(filename)
    x, y = im.size[0], im.size[1]
    parts = filename.rpartition(".")
    newFilename = f"{parts[0]}_{x}x{y}.{parts[2]}"
    answer = input(f"Does this look good y/[n]: {newFilename}\n")

    if answer == "y" or answer == "Y":
        os.rename(filename, newFilename)
    else:
        print("Aborting")


def main():
    if len(sys.argv) < 2:
        print("Expected one or more filenames as arguments")
        print("example: astf picture.jpg")
        print("or     : astf picture.jpg picture2.png")
        sys.exit()

    filenames = sys.argv[1:]

    for filename in filenames:
        process(filename)


if __name__=="__main__":
    main()
