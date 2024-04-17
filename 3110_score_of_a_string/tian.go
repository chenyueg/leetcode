func scoreOfString(s string) int {
	result := 0
	for i := 0; i+1 < len(s); i++ {
		result += abs(int(s[i]) - int(s[i+1]))
	}
	return result
}

func abs(a int) int {
	if a < 0 {
		return 0 - a
	}
	return a
}

