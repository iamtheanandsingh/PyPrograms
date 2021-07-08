def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:
		mid = (high + low) // 2
		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1
		else:
			return mid
	return -1


arr = []

y = int(input("Enter Range Of Array : "))

for i in range(0,y):
    z = int(input())
    arr.append(z)

x = print("Enter Search Element : ")

result = binary_search(arr, x)

if result != -1:
	print("Element Is Present At Index", str(result))
else:
	print("Element Is Not Present In Array")