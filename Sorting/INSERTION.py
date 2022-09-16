# INSERTION SORT

def insertion_sort(arr):
	for i in range(1, len(arr)):
		anchor = arr[i]
		j = i-1
		while j >= 0 and arr[j] > anchor:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = anchor
