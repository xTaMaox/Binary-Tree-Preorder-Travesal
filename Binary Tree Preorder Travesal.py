class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:

        return [] if not root else   ([root.val]+
                self.preorderTraversal(root.left)+
                self.preorderTraversal(root.right))