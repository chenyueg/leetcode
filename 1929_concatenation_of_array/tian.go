func getConcatenation(nums []int) []int {
	n := len(nums)
	result := make([]int, n*2)
	i := 0
	for i < n*2 {
		for _, num := range nums {
			if i >= n*2 {
				break
			}
			result[i] = num
			i++
		}
	}
	return result
}
