#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.3.0"
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


def gen_random_str(length, choose_from = string.ascii_uppercase + string.ascii_lowercase + string.digits):
	return ''.join(random.choice(choose_from) for x in range(length))


def print_help():
	print()
	print(f"Usage: {os.path.abspath(__file__)} [-C count of password lines] [-L lenght of password] [options]")
	print("		options:")
	print("		--only-digits: use only digits in passwd")
	print("		--help | -h: print this help ")
	print()
	print(f"Example: {os.path.abspath(__file__)} -C 10 -L 12 		- will generate 10 passwords, 12 chars each")
	print()


if __name__ == "__main__":
	# CLI arguments
	args = sys.argv[1:]
	
	# defaults
	LENGTH = 10
	LINE_COUNT = 10
	PRINT_EXTRA_SPACES = True	

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
	if "--only-digits" in args:
		CHOOSE_FROM = string.digits
	else:
		CHOOSE_FROM = string.ascii_uppercase + string.ascii_lowercase + string.digits
	
	# generating passwords here
	if PRINT_EXTRA_SPACES: print()
	for i in range(LINE_COUNT):
		print(gen_random_str(LENGTH, choose_from = CHOOSE_FROM))
	if PRINT_EXTRA_SPACES: print()
