#!/usr/bin/env python3

# update_youtubedown

# This program looks if there is a new version of youtubedown.
# The original lives at https://www.jwz.org/hacks/youtubedown

import sys
import requests

path_to_file: str = "/Users/vincentzee/bin/youtubedown"
install_dir: str = "/Users/vincentzee/bin"

url: str = "https://jwz.org/hacks/youtubedown"


def get_local_version(path_to_file: str) -> str:
    """Returns the version number of the local version as a string."""
    try:
        f = open(path_to_file, "rt")
    except FileNotFoundError as e:
        print("It seems that Youtubedown is not installed on your system.")
        result = input("Do you want to install it? [y/n] ")

        if result == "y" or result == "yes":
            print("Installing")
            s = get_remote_version(url)
            f = open(path_to_file, "w")
            print("Writing file")
            f.write(s)
            f.close()
            sys.exit()
        else:
            print("Exiting")
            sys.exit()

    for line in f:
        if "$Revision" in line:
            l = line.split(" ")
    f.close()
    return l[4]


def get_remote_version(url: str) -> str:
    """Gets the remote version and returns it as a long string."""
    response = requests.get(url)
    if response:
        print("Getting remote version")
        s = response.text
        return s
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
    """Compare the version numbers of the remote and local version."""
    if float(localv) < float(remotev):
        print(f"local version {localv} is older than remote version {remotev}")
    else:
        print(f"local version = {localv}; remote version = {remotev}")


def main() -> None:
    # Getting the local version number
    localv = get_local_version(path_to_file)

    remote_version = get_remote_version(url)

    # Getting the remote version number
    remotev = get_version_number(remote_version)

    # Comparing the two versions
    compare_versions(localv, remotev)


if __name__ == "__main__":
    main()
