class Solution:
    def keyOfAnagram(string:str)->str:
        return "".join(sorted(string))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            k = "".join(sorted(s)) 
            if k not in hashmap:
                hashmap[k] = []
            hashmap[k].append(s)
        
        ans = []
        for i in hashmap.values():
            ans.append(i)

        return ans