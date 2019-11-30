#!/usr/bin/env python3

# This program looks if there is a new version of youtubedown.
# The original lives at https://www.jwz.org/hacks/youtubedown

import requests

path_to_file: str = "/Users/vincentzee/bin/youtubedown"

url: str = "https://jwz.org/hacks/youtubedown"


def my_version(path_to_file: str) -> str:
    """Returns the version number of the local version as a string."""
    f = open(path_to_file, "rt")

    for line in f:
        if "$Revision" in line:
            l = line.split(" ")
    f.close()
    return l[4]


def new_version(url: str) -> str:
    """Returns the version number of the remote version as a string."""
    response = requests.get(url)
    if response:
        s = response.text
        lines = s.splitlines()
        for line in lines:
            if "$Revision" in line:
                l = line.split(" ")
        return l[4]
    else:
        return "Url Not Found."


def main():
    print(my_version(path_to_file))

    print(new_version(url))


if __name__ == "__main__":
    main()
