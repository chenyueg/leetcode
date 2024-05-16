import "strings"

func mostWordsFound(sentences []string) int {
	result := 0
	for _, item := range sentences {
		result = max(result, len(strings.Split(item, " ")))
	}
	return result
}
