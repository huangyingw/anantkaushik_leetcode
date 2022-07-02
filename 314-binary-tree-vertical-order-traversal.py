class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        self.d = {}
        self.bfs(root)
        res = []
        for x in sorted(self.d.keys()):
            res.append(self.d[x])
        return res

    def bfs(self, root):
        if not root:
            return
        stack = [[root, 0]]
        while stack:
            new_level = []
            temp = []
            for i in range(len(stack)):
                node, x = stack[i]
                if node.left:
                    new_level.append([node.left, x - 1])
                if node.right:
                    new_level.append([node.right, x + 1])
                if x in self.d:
                    self.d[x].append(node.val)
                else:
                    self.d[x] = [node.val]
            stack = new_level if new_level else None
