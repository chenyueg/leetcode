func subsetXORSum(nums []int) int {
	result := []int{}
	for _, n := range nums {
		size := len(result)
		for i := 0; i < size; i++ {
			result = append(result, result[i]^n)
		}
		result = append(result, n)
	}
	sum := 0
	for _, n := range result {
		sum += n
	}
	return sum
}
