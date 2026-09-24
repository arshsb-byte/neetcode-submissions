class Solution:

    def encode(self, strs: List[str]) -> str: 
        ans = ""
        for s in strs:
            ans+=(str(len(s))+"*"+s)
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i<len(s):
            j=i
            while s[j]!="*":
                j+=1
            strLen = int(s[i:j])
            strs.append(s[j+1:j+1+strLen])
            i=j+strLen+1

        return strs


