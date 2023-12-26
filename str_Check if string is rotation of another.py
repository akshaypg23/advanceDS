class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        l1= len(str1)
        l2= len(str2)
        if l1!=l2:
            return False
        else:
            temp=str1+str1
            if str2 in temp:
                return True
            else:
                return False
