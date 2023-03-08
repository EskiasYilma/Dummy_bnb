#!/usr/bin/python3
"""
Console Module Docstring
"""

import cmd

class HBNBCommand(cmd.Cmd):
	"""
	TODO
	"""
	def do_quit(self, inp):
		"""Quit command to exit the program\n"""
		return True

	def do_EOF(self, inp):
		"""Quit command to exit the program\n"""
		return True

	def emptyline(self):
		pass		



if __name__ == '__main__':
    HBNBCommand().cmdloop()
