func findMatrix(nums []int) [][]int {
	hash := map[int]int{}
	biggest := 1
	for _, n := range nums {
		hash[n]++
		biggest = max(biggest, hash[n])
	}
	var result [][]int
	for i := biggest - 1; i >= 0; i-- {
		var tmp []int
		for k, v := range hash {
			if v == i+1 {
				tmp = append(tmp, k)
				hash[k]--
			}
		}
		result = append(result, tmp)
	}
	return result
}

