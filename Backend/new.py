def longestSubstring(s):
    charSet = set()
    left = 0
    right = 0
    ans = 0
    while right < len(s):
        if s[right] not in charSet:
            charSet.add(s[right])
            right += 1
            ans = max(ans, right - left)
        else:
            charSet.remove(s[left])
            left += 1
    return ans

print(longestSubstring("abcabcbbc"))