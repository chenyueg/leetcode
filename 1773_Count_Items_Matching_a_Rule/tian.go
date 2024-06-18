func countMatches(items [][]string, ruleKey string, ruleValue string) int {
	result := 0
	for _, item := range items {
		if ruleKey == "type" {
			if item[0] == ruleValue {
				result++
			}
		}
		if ruleKey == "color" {
			if item[1] == ruleValue {
				result++
			}
		}
		if ruleKey == "name" {
			if item[2] == ruleValue {
				result++
			}
		}
	}
	return result
}
