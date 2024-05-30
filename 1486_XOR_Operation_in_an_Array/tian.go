func xorOperation(n int, start int) int {
	result := 0
	curr := start
	i := 1
	for n > 0 {
		result ^= curr
		curr = curr + i*2
		n--
	}
	return result
}
