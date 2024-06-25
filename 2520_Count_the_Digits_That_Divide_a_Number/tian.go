func countDigits(num int) int {
	result := 0
	n := num
	for n > 0 {
		d := n % 10
		if num%d == 0 {
			result += 1
		}
		n /= 10
	}
	return result
}
