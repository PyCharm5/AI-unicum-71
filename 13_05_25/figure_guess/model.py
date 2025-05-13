import math
class CombinatorialCalculatorModel:
    @staticmethod
    def calculate_permutations(n):
        return math.factorial(n)

    @staticmethod
    def calculate_arrangements(n, k, with_repeat):
        if with_repeat:
            return n ** k
        else:
            return math.factorial(n) // math.factorial(n - k)

    @staticmethod
    def calculate_combinations(n, k, with_repeat):
        if with_repeat:
            return math.comb(n + k - 1, k)
        else:
            return math.comb(n, k)

    @staticmethod
    def get_formula(func_type, n, k, with_repeat, result):
        if func_type == "permutations":
            return f"P(n) = n! = {n}! = {result}"
        elif func_type == "arrangements":
            if with_repeat:
                return f"A(n,k) = n^k = {n}^{k} = {result}"
            else:
                return f"A(n,k) = n!/(n-k)! = {n}!/({n}-{k})! = {result}"
        elif func_type == "combinations":
            if with_repeat:
                return f"C(n,k) = (n+k-1)!/(k!(n-1)!) = ({n}+{k}-1)!/({k}!({n}-1)!) = {result}"
            else:
                return f"C(n,k) = n!/(k!(n-k)!) = {n}!/({k}!({n}-{k})!) = {result}"