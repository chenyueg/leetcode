func pivotArray(nums []int, pivot int) []int {
	left := []int{}
	right := []int{}
	pivots := []int{}
	for _, n := range nums {
		if n < pivot {
			left = append(left, n)
		} else if n > pivot {
			right = append(right, n)
		} else {
			pivots = append(pivots, n)
		}
	}
	left = append(left, pivots...)
	left = append(left, right...)
	return left
}

