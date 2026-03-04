class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))
            my_dict[sorted_str].append(s)
        
        return list(my_dict.values())
            
