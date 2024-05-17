func largestLocal(grid [][]int) [][]int {
	n := len(grid)

	result := [][]int{}
	for i := 1; i < n-1; i++ {
		tmp := []int{}
		for j := 1; j < n-1; j++ {
			maxNum := grid[i][j]
			for a := i - 1; a <= i+1; a++ {
				for b := j - 1; b <= j+1; b++ {
					maxNum = max(maxNum, grid[a][b])
				}
			}
			tmp = append(tmp, maxNum)
		}
		result = append(result, tmp)
	}
	return result
}


