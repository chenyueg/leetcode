import "strings"

func truncateSentence(s string, k int) string {
	words := strings.Split(s, " ")
	return strings.Join(words[0:k], " ")
}

