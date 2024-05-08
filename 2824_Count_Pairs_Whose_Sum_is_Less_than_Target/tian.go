import "sort"

func countPairs(nums []int, target int) int {
	sort.Ints(nums)
	left := 0
	right := len(nums) - 1
	result := 0
	for left < right {
		sum := nums[left] + nums[right]
		if sum < target {
			result += right - left
			left++
		} else {
			right--
		}
	}
	return result
}
