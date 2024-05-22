func countPoints(points [][]int, queries [][]int) []int {
	result := []int{}
	for _, q := range queries {
		curr := 0
		for _, p := range points {
			tmp := distance(p, q)
			if tmp <= q[2]*q[2] {
				curr++
			}
		}
		result = append(result, curr)
	}
	return result
}

func distance(a, b []int) int {
	return (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1])
}

