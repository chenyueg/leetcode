import "sort"

func sortTheStudents(score [][]int, k int) [][]int {
	hash := map[int][]int{}
	m := len(score)
	for i := 0; i < m; i++ {
		hash[score[i][k]] = score[i]
	}
	arr := []int{}
	for a, _ := range hash {
		arr = append(arr, a)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(arr)))
	result := [][]int{}
	for i := 0; i < len(arr); i++ {
		result = append(result, hash[arr[i]])
	}
	return result
}
