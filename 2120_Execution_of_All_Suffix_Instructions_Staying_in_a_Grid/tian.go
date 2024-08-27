type Location struct {
	Row int
	Col int
}

func executeInstructions(n int, startPos []int, s string) []int {
	var result []int
	for i := 0; i < len(s); i++ {
		l := Location{Row: startPos[0], Col: startPos[1]}
		counter := 0
		for j := i; j < len(s); j++ {
			l.walk(s[j])
			if l.Row < 0 || l.Col < 0 || l.Row >= n || l.Col >= n {
				break
			}
			counter++
		}
		result = append(result, counter)
	}
	return result
}

func (l *Location) walk(b byte) {
	switch b {
	case 'L':
		l.Col--
	case 'R':
		l.Col++
	case 'U':
		l.Row--
	case 'D':
		l.Row++
	}
}
