from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        
        dict = defaultdict(int)
        
        for letter in magazine:
            dict[letter] += 1
        
        for letter in ransomNote:
            dict[letter] -= 1
            
            if dict[letter] == -1:
                return False
        
        return True