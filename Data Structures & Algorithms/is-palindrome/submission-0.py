class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        print(newS)
        for i in range(len(newS)//2):
            if(newS[i]!=newS[-1-i]):
                return False
        return True
        