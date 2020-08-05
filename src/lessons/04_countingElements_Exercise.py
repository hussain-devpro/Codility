# Problem: You are given an integer m (1 <= m <= 1,000,000) and two non-empty, zero-indexed
# arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 respectively (0 <= ai, bi <= m).
# The goal is to check whether there is a swap operation which can be performed on these
# arrays in such a way that the sum of elements in array A equals the sum of elements in
# array B after the swap. By swap operation we mean picking one element from array A and
# one element from array B and exchanging them.


def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for i in range(n):
        count[A[i]] += 1
    return count


# print(counting([1, 3, 4, 5, 2, 0, 3, 4, 5, 6, 4, 3, 2, 7], 7))


def solution(A, B, m):
    N = len(A)
    Asum = sum(A)
    Bsum = sum(B)
    diff = Asum - Bsum

    # if difference is odd number, arrays can't be normalized by swapping numbers
    if diff % 2 != 0:
        return False

    diff = diff // 2  # indicate the actual difference between sum of array. If diff was 2 then +1 in A and -1 in B

    A_count = counting(A, m)

    for i in range(N):
        print(B[i], diff, A_count[B[i] - diff])
        if 0 <= (B[i] - diff) < m and A_count[B[i] - diff] > 0:
            return True
    return False

    return Asum, Bsum, diff


print(solution([1, 2, 3, 4, 2, 3, 4, 4], [3, 2, 4, 2, 4, 5, 2, 3], 5))
