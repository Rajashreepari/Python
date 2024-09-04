#Selection sort
def selectionSort(array, size):
	for i in range(size):
		min_index = i
		for j in range(i + 1, size):
			if array[j] < array[min_index]:
				min_index = j
		(array[i], array[min_index]) = (array[min_index], array[i])
arr = list(map(int,input("enter the element with sepoarated space: ").split()))
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
