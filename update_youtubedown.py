#!/usr/bin/env python3

# update_youtubedown

# This program looks if there is a new version of youtubedown.
# The original lives at https://www.jwz.org/hacks/youtubedown

import sys
import requests

path_to_file: str = "/Users/vincentzee/bin/youtubedown"

url: str = "https://jwz.org/hacks/youtubedown"


def get_local_version(path_to_file: str) -> str:
    """Returns the version number of the local version as a string."""
    try:
        f = open(path_to_file, "rt")
    except FileNotFoundError as e:
        print(e)
        sys.exit()

    for line in f:
        if "$Revision" in line:
            l = line.split(" ")
    f.close()
    return l[4]


def get_remote_version(url: str) -> str:
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


def get_version_number(long_string: str) -> str:
    """Extracts the version number from string and returns it."""
    lines = long_string.splitlines()
    for line in lines:
        if "$Revision" in line:
            l = line.split(" ")
    return l[4]


def compare_versions(localv: str, remotev: str) -> None:
    if float(localv) < float(remotev):
        print(f"local version {localv} is older than remote version {remotev}")


def main() -> None:
    compare_versions(get_local_version(path_to_file), get_remote_version(url))


if __name__ == "__main__":
    main()
