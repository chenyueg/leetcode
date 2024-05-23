func leftRightDifference(nums []int) []int {
	n := len(nums)
	prefix := make([]int, n)
	suffix := make([]int, n)
	for i := 1; i < n; i++ {
		prefix[i] = prefix[i-1] + nums[i-1]
	}
	for i := n - 2; i >= 0; i-- {
		suffix[i] = suffix[i+1] + nums[i+1]
	}
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = abs(prefix[i] - suffix[i])
	}
	return result
}

func abs(a int) int {
	if a < 0 {
		return 0 - a
	}
	return a
}
