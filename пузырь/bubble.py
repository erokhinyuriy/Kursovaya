
>>> def bubble (arr,dim):
	alg_count = [0,0]
	for i in range (0, dim - 1):
		for j in range (len(arr) - 1, i, -1):
			alg_count[0] += 1
			if arr[j] < arr [j - 1]:
				alg_count[1] += 1
				arr[j - 1], arr[j] = arr[j], arr[j - 1]
	returnalg_count
