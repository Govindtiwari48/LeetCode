class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        start=0
        end=len(pref)-1
        res=[pref[0]]
        while(start<end):
            res.append(pref[start]^pref[start+1])
            start+=1
        return res


        