import (
	"math"
	"sort"
)

func maxWidthOfVerticalArea(points [][]int) int {
	sort.Slice(points, func(a, b int) bool {
		return points[a][0] < points[b][0]
	})
	result := math.MinInt64
	for i := 1; i < len(points); i++ {
		result = max(result, points[i][0]-points[i-1][0])
	}
	return result
}
