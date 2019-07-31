#!/usr/bin/python

import sys

if len(sys.argv) == 1:
	str1 = raw_input("Please enter a string: ")
else:
	str1 = sys.argv[1]

checkTime = str1 * 1000000

def r1(s):
	rstr = s[::-1]

	return rstr

def r2(s):
	rstr = ""
	size = len(s) - 1
	while size >= 0:
		rstr += s[size]
		size -= 1

	return rstr

def r3(s):
	rstr = ""
	strStack = []
	size = len(s)

	for i in range(size):
		strStack.append(s[i])

	for i in range(size):
		rstr += strStack.pop()

	return rstr

print(r1((str1)))
print(r2((str1)))
print(r3((str1)))
r1(checkTime)
print(1)
r2(checkTime)
print(2)
r3(checkTime)
print(3)