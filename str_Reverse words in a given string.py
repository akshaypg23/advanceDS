class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        ans=[]
        word=[]
        for x in S:
            if x !='.':
                word.append(x)
            else:
                ans.insert(0,"".join(word))
                word=[]
        ans.insert(0,"".join(word))
        return ".".join(ans)
