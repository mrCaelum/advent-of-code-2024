#!/usr/bin/env python3

import sys

# Parse input into two lists
def parse_input():
	count = 0
	list_1 = []
	list_2 = []
	for line in sys.stdin:
		tmp = line.split()
		list_1.append(int(tmp[0]))
		list_2.append(int(tmp[1]))
		count += 1
	return list_1, list_2, count

if __name__ == "__main__":
	similarity_score = 0
	input_list_1, input_list_2, count = parse_input()
	for value in input_list_1:
		similarity_score += value * input_list_2.count(value)
	print(similarity_score)
