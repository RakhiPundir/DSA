class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        print(li)
        l = []
        for i in li:
            l.append(i[::-1])
        print(l)
        return ' '.join(l)
