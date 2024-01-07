#!/usr/bin/python3
"""This is a module that sends a request to a url
and managing errors
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    url = argv[1]

    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
