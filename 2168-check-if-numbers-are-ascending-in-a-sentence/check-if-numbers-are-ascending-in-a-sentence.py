class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        maxi = 0

        for val in s.split():
            if val.isdigit() and int(val) <= maxi:
                return False
            elif val.isdigit():
                maxi = int(val)
        
        return True
        