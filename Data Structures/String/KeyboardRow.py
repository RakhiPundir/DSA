class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        op = []
        for i in words:
            if(i[0].lower() in r1):
                w = 0
                for j in i:
                    if j.lower() in r1:
                        w += 1
                if(len(i)==w):
                    op.append(i)
            elif(i[0].lower() in r2):
                w = 0
                for j in i:
                    if j.lower() in r2:
                        w += 1
                if(len(i)==w):
                    op.append(i)
            elif(i[0].lower() in r3):
                w = 0
                for j in i:
                    if j.lower() in r3:
                        w += 1
                if(len(i)==w):
                    op.append(i)
        return op
