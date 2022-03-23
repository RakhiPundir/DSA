class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = []
        for i in range(1, rowIndex+2):
            l = []
            if(i == 1):
                l.append(1)
                pascal.append(l)
            elif(i == 2):
                l.append(1)
                l.append(1)
                pascal.append(l)
            else:
                l.append(1)
                for j in range(i-2):
                    x = pascal[i-2][j] + pascal[i-2][j+1]
                    l.append(x)
                l.append(1)
                pascal.append(l)
                
        print(pascal)
        return pascal[rowIndex]
