import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        # print("")
        # print(s)
        # print(s[::-1])
        # print(s == s[::-1])

        return s == s[::-1] # 슬라이싱