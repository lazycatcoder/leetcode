'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0.

Constraints:
• 1 <= stones.length <= 30
• 1 <= stones[i] <= 1000


Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1

Example 2:
Input: stones = [1]
Output: 1
'''


class Solution():
    def lastStoneWeight(self, stones):
        def __str__(self):
            return
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]
        else:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if x != y:
                stones.append(y-x)
            return self.lastStoneWeight(stones)