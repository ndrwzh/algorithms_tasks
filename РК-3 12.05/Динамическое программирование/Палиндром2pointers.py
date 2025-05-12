def longestPalindrome(s):

    if not s:
        return ""

    n = len(s)
    max_left = 0
    max_right = 0

    def expandAroundCenter(left, right):
        nonlocal max_left, max_right
        while left >= 0 and right < n and s[left] == s[right]:
            if (right - left) > (max_right - max_left):
                max_right = right
                max_left = left
            left -= 1
            right += 1

    for i in range(n):
        expandAroundCenter(i, i)  # Нечетная длина палиндрома
        expandAroundCenter(i, i + 1)  # Четная длина палиндрома

    return s[max_left : max_right + 1]