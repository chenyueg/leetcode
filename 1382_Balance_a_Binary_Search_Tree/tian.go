/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func balanceBST(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	values := []int{}
	stack := []*TreeNode{}
	node := root
	for node != nil || len(stack) != 0 {
		for node != nil {

			stack = append(stack, node)
			node = node.Left
		}
		if len(stack) != 0 {
			node = stack[len(stack)-1]
			values = append(values, node.Val)
			stack = stack[:len(stack)-1]
			node = node.Right
		}
	}
	//fmt.Println("values: ", values)
	root = generateTree(values, 0, len(values)-1)
	return root
}

func generateTree(values []int, left, right int) *TreeNode {
	if left > right {
		return nil
	}
	mid := (right + left) / 2
	root := &TreeNode{
		Val: values[mid],
	}
	root.Left = generateTree(values, left, mid-1)
	root.Right = generateTree(values, mid+1, right)
	return root
}
