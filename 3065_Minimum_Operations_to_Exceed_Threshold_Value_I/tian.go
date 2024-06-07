func minOperations(nums []int, k int) int {
	result := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] < k {
			result++
		}
	}
	return result
}
