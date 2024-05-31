func createTargetArray(nums []int, index []int) []int {
	result := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		idx := index[i]
		move(result, idx)
		result[idx] = num
	}
	return result
}

func move(nums []int, start int) {
	for i := len(nums) - 1; i > start; i-- {
		nums[i] = nums[i-1]
	}
}

