/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeNodes(head *ListNode) *ListNode {
	dummy := head
	node := head
	fast := head
	for fast != nil {
		for fast != nil && fast.Val == 0 {
			fast = fast.Next
		}
		sum := 0
		for fast != nil && fast.Val != 0 {
			sum += fast.Val
			fast = fast.Next
		}
		if sum == 0 {
			break
		}
		node.Next = &ListNode{Val: sum}
		node = node.Next

	}
	return dummy.Next
}
