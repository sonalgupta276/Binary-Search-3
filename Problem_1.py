class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.00
        result = self.myPow(x, int(n/2))
        if n % 2 == 0:
            return result * result
        else:
            if n < 0:
                return result * result * (1/x)
            else:
                return result * result * x

# Time Complexity: log(n)
# Space Complexity: log(n) due to recursive stack being used.


