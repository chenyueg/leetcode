func minimumOperations(nums []int) int {
	result := 0
	for _, n := range nums {
		if n%3 != 0 {
			result++
		}
	}
	return result
}

