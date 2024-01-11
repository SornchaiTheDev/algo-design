from collections import Counter


def longest_repeated_substring(s, k):

    if not s or k <= 0:
        return 0

    start, max_length = 0, 0
    char_count = Counter(s[:k])

    for end in range(k, len(s)):
        char_count[s[end]] += 1

        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage
s = "ababcaaadc"
k = 2
result = longest_repeated_substring(s, k)
print(result)  # Output: 4
