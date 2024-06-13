func garbageCollection(garbage []string, travel []int) int {
	preSum := make([]int, len(travel)+1)
	for i := 1; i < len(preSum); i++ {
		preSum[i] = preSum[i-1] + travel[i-1]
	}
	lastP := 0
	lastG := 0
	lastM := 0
	result := 0
	for i := 0; i < len(garbage); i++ {
		for j := 0; j < len(garbage[i]); j++ {
			if garbage[i][j] == 'G' {
				lastG = i
				result++
			} else if garbage[i][j] == 'M' {
				lastM = i
				result++
			} else {
				lastP = i
				result++
			}
		}
	}
	result += preSum[lastP] + preSum[lastG] + preSum[lastM]
	return result
}

