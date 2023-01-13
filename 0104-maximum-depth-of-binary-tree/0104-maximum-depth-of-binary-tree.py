# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: # 이게 뭔데?
            return 0
        queue = collections.deque([root]) # deque 자료구조
        depth = 0
    
        while queue:
            depth += 1
            # n 레벨의 모든 노드를 pop 하여 -> 인접노드(자식노드)들을 q에 넣는 과정
            for _ in range(len(queue)):
                cur_root = queue.popleft() # deque에서 popleft는 q상의 front를 추출
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 ==> 깊이
        return depth
        