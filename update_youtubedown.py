#!/usr/bin/env python3
# update_youtubedown
# This program looks if there is a new version of youtubedown.
# The original lives at https://www.jwz.org/hacks/youtubedown

import os.path
import sys
import requests

path_to_file: str = "/Users/vincentzee/bin/youtubedown"
install_dir: str = "/Users/vincentzee/bin"

url: str = "https://jwz.org/hacks/youtubedown"


def installed() -> bool:
    """Checks if there is a file called youtubedown."""
    if os.path.isfile(path_to_file):
        return True
    else:
        return False


def install_dir_exists() -> bool:
    """Checks if there is a path to the bin directory."""
    if os.path.isdir(install_dir):
        return True
    else:
        return False


def make_executable(path_to_file: str) -> None:
    """Make the file executable."""
    os.chmod(path_to_file, 0o755)


def install_it(new_version: str) -> None:
    """Writing the file."""
    f = open(path_to_file, "w")
    print("Writing file")
    f.write(new_version)
    f.close()


def get_local_version(path_to_file: str) -> str:
    """Returns the version number of the local version as a string."""
    try:
        f = open(path_to_file, "rt")
        for line in f:
            if "$Revision" in line:
                l = line.split(" ")
        f.close()
        return l[4]
    except FileNotFoundError as e:
        print(e)
        sys.exit()


def get_remote_version(url: str) -> str:
    """Gets the remote file and returns it as a long string."""
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


def is_newer_version(localv: str, remotev: str) -> bool:
    """Checks if there is a more current version."""
    if float(localv) < float(remotev):
        return True
    else:
        return False


def backup_old_version(localv: str) -> None:
    """Backup the old file with its version number attached."""
    new_path: str = path_to_file + "_" + localv
    print("Old version will be backed up to:")
    print(new_path)
    os.rename(path_to_file, new_path)


def main() -> None:
    """The main function."""
    new_version: str = get_remote_version(url)
    # check if youtubedown is installed
    if not installed():
        print("youtubedown doesn't seem to be installed!")
        answer = input("Do you want to install it? [y/n]\n")

        if answer == "y" or answer == "yes":
            if not install_dir_exists():
                os.mkdir(install_dir)
                install_it(new_version)
                make_executable(path_to_file)
            else:
                install_it(new_version)
                make_executable(path_to_file)
        else:
            print("Exititng")
            sys.exit()
    elif installed():
        # getting local and remote version strings
        localv: str = get_local_version(path_to_file)
        remotev: str = get_version_number(new_version)

        if is_newer_version(localv, remotev):
            print("There is a newer version available.")
            print(f"old version {localv}; new version {remotev}")
            answer = input("Do you want to install it? [y/n]\n")
            if answer == "y" or answer == "yes":
                backup_old_version(localv)
                install_it(new_version)
                make_executable(path_to_file)
            else:
                print("Exiting")
                sys.exit()
        else:
            print(f"You have the latest version {localv}.")
    else:
        print("Something unexpected happened!")


if __name__ == "__main__":
    main()
