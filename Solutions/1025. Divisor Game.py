'''
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
• Choosing any x with 0 < x < n and n % x == 0.
• Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.


Constraints:
• 1 <= n <= 1000


Example 1:
Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:
Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
'''


class Solution:
    memo = {}

    def divisorGame(self, n: int) -> bool:
        if n in self.memo:
            return self.memo[n]

        if n == 1:
            return False

        for x in range(1, n):
            if n % x == 0:
                if not self.divisorGame(n - x):
                    self.memo[n] = True
                    return True

        self.memo[n] = False
        return False