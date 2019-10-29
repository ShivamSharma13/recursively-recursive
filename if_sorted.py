#/usr/bin/env python3

'''
Suppose you have an array of integers. Write a recursive function that
returns true if the array is sorted from smallest to largest, and false
otherwise.
'''

def is_list_sorted(list_1):
	if len(list_1) == 1:
		return True
	else:
		if list_1.pop() > list_1[-1]:
			return is_list_sorted(list_1)
		else:
			return False

if __name__ == "__main__":
	list_1 = [1,2,3,4,5,6,7,8,10,20,55,77,99]
	list_2 = [1,20,3,4,5,9,7,8,10,2,55,7,99]
	print(is_list_sorted(list_2))