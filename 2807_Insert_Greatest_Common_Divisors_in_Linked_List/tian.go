/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	dummy := &ListNode{Next: head}
	node := head
	for node.Next != nil {
		next := node.Next
		gcd := getGCD(node.Val, next.Val)
		curr := &ListNode{Val: gcd}
		node.Next = curr
		curr.Next = next
		node = next
	}
	return dummy.Next
}

func getGCD(a, b int) int {
	if b == 0 {
		return a
	}
	return getGCD(b, a%b)
}
