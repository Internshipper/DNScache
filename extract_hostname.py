# -*- coding: utf-8 -*-
# extract hostname
# input from a file, which one line has a url

import argparse
import ipaddress
import sys
import urllib
from urllib.parse import urlparse

def extractor(urls: list):
    hostnames = set()
    for url in urls:
        urldict = urllib.parse.urlparse(url)
        if urldict.hostname and urldict.hostname != 'localhost':
            try:
                ipaddress.ip_address(urldict.hostname)
            except:
                hostnames.add(urldict.hostname)
    return hostnames

def main(args):
    if args.infile:
        sys.stdin = args.infile
    if args.outfile:
        sys.stdout = args.outfile
    urls = [line.strip() for line in sys.stdin.readlines()]
    hostnames = extractor(urls)
    print('\n'.join(list(hostnames)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract hostname from urls")
    parser.add_argument("-if", "--infile", action="store", nargs='?', default=None, type=argparse.FileType("r"), help="the file name stored urls")
    parser.add_argument("-of", "--outfile", action="store", nargs='?', default=None, type=argparse.FileType("w"), help="the file name save hostnames")
    args = parser.parse_args()
    main(args)