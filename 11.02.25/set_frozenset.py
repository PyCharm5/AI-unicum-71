import time

lst = list("AAB")

def time_measuring(func):
    def wrapper(lst):
        start_time = time.time()
        res = func(lst)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        return res
    return wrapper

@time_measuring
def narayana_permutations(arr):
    if len(arr) == 0:
        return [[]]

    result = []

    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i + 1:]

        for perm in narayana_permutations(remaining):
            result.append([current] + perm)

    return result

@time_measuring
def johnson_trotter(n):
    if n == 0:
        return []

    permutation = list(range(n))
    directions = [-1] * n
    result = [permutation.copy()]

    def find_mobile():
        max_mobile = -1
        index = -1
        for i in range(len(permutation)):
            direction = directions[i]
            if (direction == -1 and i > 0 and permutation[i] > permutation[i - 1]) or \
                    (direction == 1 and i < len(permutation) - 1 and permutation[i] > permutation[i + 1]):
                if permutation[i] > max_mobile:
                    max_mobile = permutation[i]
                    index = i
        return index if max_mobile != -1 else None

    while True:
        mobile_idx = find_mobile()
        if mobile_idx is None:
            break

        mobile = permutation[mobile_idx]
        move_to = mobile_idx + directions[mobile_idx]

        permutation[mobile_idx], permutation[move_to] = permutation[move_to], permutation[mobile_idx]
        directions[mobile_idx], directions[move_to] = directions[move_to], directions[mobile_idx]

        for i in range(len(permutation)):
            if permutation[i] > mobile:
                directions[i] *= -1

        permutations = []
        for i in permutation:
            permutations.append(lst[i])
        result.append(permutations)

    return result


permutations_jhonson = johnson_trotter(len(lst))

permutations_nara = narayana_permutations(lst)

print(permutations_jhonson)
print(permutations_nara)