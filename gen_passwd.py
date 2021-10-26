#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2021-10-26

__version__ = "0.1.1"
__author__ = "Igor Martynov (phx.planewalker@gmail.com)"


"""Generate random passwords the simple way.
Python3 required.

See print_help() for usage info"""

# basic imports
import os
import datetime
import sys
import traceback
import random
import string


def gen_random_str(length):
	return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(length))


def print_help():
	print()
	print(f"Usage: {os.path.abspath(__file__)} [-C number of password lines] [-L lenght of password]")
	print(f"Example: {os.path.abspath(__file__)} -C 10 -L 12 		- will generate 10 passwords, 12 chars each")
	print()


if __name__ == "__main__":
	# defaults
	LENGTH = 10
	LINE_COUNT = 10
	PRINT_EXTRA_SPACES = True
	
	# CLI arguments
	args = sys.argv[1:]
	
	if "--help" in args or "-h" in args:
		print_help()
		sys.exit(0)
	if "-L" in args:
		try:
			LENGTH = int(args[args.index("-L") + 1])
		except Exception as e:
			print(f"ERROR: got error while parsing password length: {e}")
			print_help()
			sys.exit(1)
	if "-C" in args:
		try:
			LINE_COUNT = int(args[args.index("-C") + 1])
		except Exception as e:
			print(f"ERROR: got error while parsing password line count: {e}")
			print_help()
			sys.exit(1)
	
	# generating here
	if PRINT_EXTRA_SPACES: print()
	for i in range(LINE_COUNT):
		print(gen_random_str(LENGTH))
	if PRINT_EXTRA_SPACES: print()
