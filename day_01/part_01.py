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

# Gets the next min value from the given list and removes it
def get_next_item(target_list):
	index, value = min(enumerate(target_list), key = lambda x: x[1] )
	del target_list[index]
	return value

if __name__ == "__main__":
	diff = 0
	input_list_1, input_list_2, count = parse_input()
	for i in range(count):
		diff += abs(get_next_item(input_list_1) - get_next_item(input_list_2))
	print(diff)
