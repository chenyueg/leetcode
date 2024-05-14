/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func averageOfSubtree(root *TreeNode) int {
	result := 0
	walk(root, &result)
	return result
}

func walk(root *TreeNode, result *int) (int, int) {
	if root == nil {
		return 0, 0
	}
	if root.Left == nil && root.Right == nil {
		*result += 1
		return root.Val, 1
	}
	leftSum, leftCount := walk(root.Left, result)
	rightSum, rightCount := walk(root.Right, result)

	ave := (leftSum + rightSum + root.Val) / (leftCount + rightCount + 1)

	if ave == root.Val {
		*result += 1
	}
	return leftSum + rightSum + root.Val, leftCount + rightCount + 1
}

