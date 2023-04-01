#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
