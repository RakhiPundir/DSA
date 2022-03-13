class Solution:
    def reverse(self, x: int) -> int:
        if(-2147483648 <= x and x <= 2147483648):
            y = str(x)
            z = list(y)
            if "-" in z:
                z.remove("-")
                y = "".join(z)
                x = -(int(y [::-1]))
                if(-2147483648 <= x and x <= 2147483648):
                    return(x)
                else:
                    return 0
            else:
                x = int(y [::-1])
                if(-2147483648 <= x and x <= 2147483648):
                    return(x)
                else:
                    return 0
        else:
            return 0
