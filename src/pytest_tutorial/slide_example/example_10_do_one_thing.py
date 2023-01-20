import math
from typing import List


class PrimeGenerator:
    def generate_primes(self, n: int) -> List[int]:
        """List all prime number < n."""
        prime_so_far = []
        for i in range(n):
            for p in prime_so_far: # check if it's prime using previous prime
                if i % p == 0:
                    break
                if p > math.sqrt(i): #
                    prime_so_far.append(i)
                    break
        return prime_so_far

class CleanerPrimeGenerator:
    def _is_divisible_by_any_less_than_sqrt(self, x: int, divisors: List[int]) -> bool:
        """ Check if x is divisible by any number in divisors that is less than sqrt(x).

        Args:
            x (int): number to check.
            divisors (List[int]): divisor to check against. Assume sorted

        Returns:
            Ture if divisible by any in divisor less than sqrt.
        """
        for d in divisors:
            if x % d == 0:
                return True
            elif d > math.sqrt(x):  #
                return False
        return False


    def generate_prime(self, n: int) -> List[int]:
        """List all prime number < n."""
        prime_so_far = []
        for i in range(n):
            if self._is_divisible_by_any_less_than_sqrt(i, prime_so_far):
                prime_so_far.append(i)

        return prime_so_far
