func countTriplets(arr []int) int {
	result := 0
	for i, val := range arr {
		for k := i + 1; k < len(arr); k++ {
			val ^= arr[k]
			if val == 0 {
				result += k - i
			}
		}
	}
	return result
}
