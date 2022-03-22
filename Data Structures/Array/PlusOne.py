class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits[-1] != 9):
            digits[-1] = digits[-1] + 1
            return digits
        else:
            i = -1
            digits[i] = digits[i] + 1
            if(len(digits) == 1):
                digits[0] = 0
                digits.insert(0, 1)
            else:
                for i in range(-1, -(len(digits)), -1):
                    if(digits[i] == 10):
                        digits[i] = 0
                        digits[i-1] = digits[i-1] + 1 
                    
            if(digits[0] == 10):
                digits[0] = 0
                digits.insert(0, 1)
            return digits
