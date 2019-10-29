#/usr/bin/env python3

def recursive_binary_search(numbers, search_number, start, stop, mid):
	print("start: {}, stop: {}, mid: {}".format(start, stop, mid))
	if search_number == numbers[mid]:
		return mid

	if search_number < numbers[mid]:
		mid = recursive_binary_search(numbers, search_number, start, stop=mid, mid=(start+mid)//2)

	if search_number > numbers[mid]:
		mid = recursive_binary_search(numbers, search_number, start=mid, stop=stop, mid=(stop+mid)//2+1)

	return mid

if __name__ == "__main__":
	numbers = [2,3,7,9,10,11,15,20,30]
	search_number = 15
	mid = recursive_binary_search(numbers, search_number, start=0, stop=len(numbers)-1, mid=len(numbers)//2)
	print(mid)