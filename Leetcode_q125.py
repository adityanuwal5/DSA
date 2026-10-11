class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        arr = []
        for i in range(len(s)):
            if s[i].isalnum():
                arr.append(s[i])

        for i in range(len(arr) // 2):
            if arr[i] != arr[len(arr) - 1 - i]:
                return False
        return True