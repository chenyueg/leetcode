func reversePrefix(word string, ch byte) string {
	arr := []byte(word)
	right := 0
	for right < len(word) && word[right] != ch {
		right++
	}
	if right >= len(word) {
		return word
	}
	left := 0
	for left < right {
		tmp := arr[left]
		arr[left] = arr[right]
		arr[right] = tmp
		left++
		right--
	}
	return string(arr)
}
