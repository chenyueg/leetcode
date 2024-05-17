func findPermutationDifference(s string, t string) int {
	hash := map[byte]int{}
	for i := 0; i < len(s); i++ {
		hash[s[i]] = i
	}
	result := 0
	for i := 0; i < len(t); i++ {
		char := t[i]
		index := hash[char]
		result += abs(i - index)
	}
	return result
}

func abs(a int) int {
	if a < 0 {
		return 0 - a
	}
	return a
}

