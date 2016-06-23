#!/usr/bin/python
# Title: print.py
# Description: Contains the gramma or value on the console
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-23
# Version: 0.1
# Usage: python print.py
# Notes: 
# python_version: 2.6.6
# License: Copyright 200X Sawan J. Kapai Harpalani 
# This file is part of MMOTracker. MMOTracker is free software: you can redistribute it  and/or modify 
# it under the terms of the GNU GeneralPublic License as published by the Free Software  Foundation, 
# either version 3 of the License,  or (at your option) any later version 
# MMOTracker is distributed in the hope that it willbe useful, but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESSFOR A PARTICULAR PURPOSE. See the GNU General 
# PubliLicense for more details.You should have received a copy of the GNU GeneralPublic License along with MMOTracker. 
# If not, seehttp://www.gnu.org/licenses/.
#==============================================================================

from pyparsing import *

from variable import *

# Rules
printReservedWord = Suppress(Literal("printConsole"))
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
number = Word(nums)
message = QuotedString('"')
variableID = identifier
plus = Suppress(Literal("+"))
printExpr = printReservedWord + leftBracket + (message.setResultsName("message", listAllMatches=True) | variableID.setResultsName("varID", listAllMatches=True)) + Optional(ZeroOrMore(plus + (message.setResultsName("message", listAllMatches=True) | variableID.setResultsName("varID", listAllMatches=True)))) + rightBracket

stack = []
v = assignment.parseString("a -> 2")
stack.append(v)
v = assignment.parseString("c -> 3")
stack.append(v)
x = printExpr.parseString("printConsole(a + \" sdwws \"+ c)")
print x.dump()

# Prints console parsed object
def printConsole(parsedObject, varStack):
	stringToPrint = ''
	for element in parsedObject:
		if element in parsedObject.varID.asList():
			for item in varStack:
				if element == item.varName:
					stringToPrint += item.varValue
		elif element in parsedObject.message.asList():
			stringToPrint += element

	print stringToPrint

printConsole(x, stack)