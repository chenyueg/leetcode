func finalValueAfterOperations(operations []string) int {
	inc := 0
	dec := 0
	for _, item := range operations {
		if item == "--X" || item == "X--" {
			dec++
		}
		if item == "++X" || item == "X++" {
			inc++
		}
	}
	return inc - dec
}
