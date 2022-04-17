#!/usr/bin/env python3

import sys
import os
from app.application import *

commands = sys.argv[1:]

def check_commands(commands):
	count = 0
	for command in commands:
		count += 1
		if command == "-n":
			name(commands[count])
		elif command == "-l":
			license(commands[count])
		elif command == "-d":
			project_name = commands[count]
			desc = commands[count+1:]
			description(project_name,desc)
		else:
			pass

check_commands(commands)