#!/usr/bin/python3
"""
Python script that sends in a URL, and displays the value of the X-Request-Id header.
"""

import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
	request_id = response.getheader("X-Request-Id")
            if request_id:
                print(request_id)
    except Exception as e:
        sys.stderr.write("Error: {}\n".format(str(e)))
        sys.exit(1)
