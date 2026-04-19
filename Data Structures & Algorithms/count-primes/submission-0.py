class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2:
            return 0

        primes = [True for _ in range(n)]
        primes[0] = False
        primes[1] = False
        
        for i in range(2, math.ceil(math.sqrt(n))):
            if primes[i]:
                for x in range(i*i, n, i):
                    primes[x] = False
        
        return sum(primes)
        
