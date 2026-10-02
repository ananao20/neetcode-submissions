class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        a = ""
        for i in range(0,len(strs)):
            a+=str(len(strs[i]))+"#"+strs[i]
        return a

    def decode(self, s: str) -> List[str]:
        l=[]
        if len(s) == 0: 
            return l
        i = 0
        while i < len(s):
            print(i)
            leng = 0
            while i<len(s) and s[i]!='#':
                leng = (ord(s[i]) - ord('0')) + leng*10
                i+=1
            l.append(s[i+1:leng+i+1])
            i=i+leng+1
        return l

            
