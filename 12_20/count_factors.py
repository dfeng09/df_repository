from collections import defaultdict
class Solution:
    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(2, n + 1) if is_prime[i]]
    def count_factors(n):
        primes = Solution.sieve_of_eratosthenes(int(n**0.5) + 1)
        factor_count = defaultdict(int)
        for p in primes:
            while n % p == 0:
                factor_count[p] += 1
                n //= p
        if n > 1:
            factor_count[n] += 1
        result = 1
        for v in factor_count.values():
            result *= (v + 1)
        return result

if __name__ == "__main__":
    max_count = 0
    max_num = 0
    for num in range(1, 10 ** 6 + 1):
        cur_count = Solution.count_factors(num)
        if cur_count > max_count:
            max_count = cur_count
            max_num = num
    print(max_num)