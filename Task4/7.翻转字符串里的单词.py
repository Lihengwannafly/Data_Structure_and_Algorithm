class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "":
            return ""

        s = s.split()[::-1]
        return " ".join(s)