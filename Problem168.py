# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 



def convertToTitle(self, n):
    output = []
    s = ""
    while n != 0:
        output.append((n-1)%26 + 65)
        n = (n - 1) // 26
    for i in output:
        s=chr(i)+s
    return s

#        ### recursion solution
#        if n > 26:
#            return (self.convertToTitle((n - 1) // 26) + self.convertToTitle(n%26))        
#        else:
#            return (chr((n-1)%26 + 65))   
