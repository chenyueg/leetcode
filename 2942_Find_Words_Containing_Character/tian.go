import "strings"

func findWordsContaining(words []string, x byte) []int {
	result := []int{}
	for i, w := range words {
		if strings.ContainsRune(w, rune(x)) {
			result = append(result, i)
		}
	}
	return result
}
