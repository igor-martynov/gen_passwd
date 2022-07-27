#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.4.0"
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
	print(f"Usage: {os.path.abspath(__file__)} [-c count of password lines] [-l lenght of password] [options]")
	print(f"Alt usage: {os.path.abspath(__file__)} [count of password lines] [lenght of password] [options]")
	print("		options:")
	print("		--only-digits: use only digits in passwd")
	print("		--help | -h: print this help ")
	print()
	print(f"Example: {os.path.abspath(__file__)} -c 10 -l 12 		- will generate 10 passwords, 12 chars each")
	print(f"Example: {os.path.abspath(__file__)} 5 15		 	- will generate 5 passwords, 15 chars each")
	print(f"Example: {os.path.abspath(__file__)} -l 20		 	- will generate 10 passwords, 20 chars each")
	print(f"Example: {os.path.abspath(__file__)} 100 -l 20		 	- will generate 100 passwords, 20 chars each")
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
	if "-l" in args:
		try:
			LENGTH = int(args[args.index("-l") + 1])
		except Exception as e:
			print(f"ERROR: got error while parsing password length: {e}")
			print_help()
			sys.exit(1)
	if "-c" in args:
		try:
			LINE_COUNT = int(args[args.index("-c") + 1])
		except Exception as e:
			print(f"ERROR: got error while parsing password line count: {e}")
			print_help()
			sys.exit(1)
	if len(args) > 0 and args[0].isdigit():
		LINE_COUNT = int(args[0])
	if len(args) > 1 and  args[0].isdigit() and args[1].isdigit():
		LINE_COUNT = int(args[0])
		LENGTH = int(args[1])
	if "--only-digits" in args:
		CHOOSE_FROM = string.digits
	else:
		CHOOSE_FROM = string.ascii_uppercase + string.ascii_lowercase + string.digits
	
	# generating passwords here
	if PRINT_EXTRA_SPACES: print()
	for i in range(LINE_COUNT):
		print(gen_random_str(LENGTH, choose_from = CHOOSE_FROM))
	if PRINT_EXTRA_SPACES: print()
