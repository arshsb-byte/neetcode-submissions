class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both and they should be same 
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_s == sorted_t
        