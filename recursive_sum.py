#/usr/bin/env python3

'''
Given an array compute sum of numbers recursively.
'''

def compute_sum_recursively(numbers, summ):
	if len(numbers) == 0:
		return summ
	return compute_sum_recursively(numbers, summ+numbers.pop())

if __name__ == "__main__":
	numbers = [2,3,7,9,10,11,15,20,30]
	summ = compute_sum_recursively(numbers, summ=0)
	print(summ)