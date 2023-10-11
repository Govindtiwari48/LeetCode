class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=x
        x=str(x)
        rev=str(x)
        rev=rev[::-1]
        print(rev)
        print(x)
        if(rev==x):
            return True
        else:
            return False