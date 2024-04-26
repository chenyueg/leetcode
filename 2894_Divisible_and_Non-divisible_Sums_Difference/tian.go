func differenceOfSums(n int, m int) int {
	sum := (1 + n) * n / 2
	countM := n / m
	lastM := (n / m) * m
	sumM := (m + lastM) * countM / 2

	return sum - sumM*2
}
