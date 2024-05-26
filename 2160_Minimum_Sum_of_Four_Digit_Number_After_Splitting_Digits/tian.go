import "sort"

func minimumSum(num int) int {
	nums := []int{}
	for num > 0 {
		nums = append(nums, num%10)
		num /= 10
	}
	sort.Ints(nums)
	return nums[0]*10 + nums[2] + nums[1]*10 + nums[3]
}
