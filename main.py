import os

file = 'table.txt'

read_file = open(file, 'r', encoding="utf-8")

lines = read_file.readlines()
print(lines)
units = {}
