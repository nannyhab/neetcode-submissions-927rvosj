class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        for char in s1:
            hashMap1[char] = 1 + hashMap1.get(char,0)
        
        L = 0

        for R in range(len(s2)):
            hashMap2[s2[R]] = 1 + hashMap2.get(s2[R],0)
            print(f"this is hashMap2: {hashMap2}")

            while R - L + 1 > len(s1):
                print(f"this is s2[L]: {s2[L]}")
                
                hashMap2[s2[L]] -= 1
                L += 1
            
            if hashMap1.items() <= hashMap2.items():
                return True

        return False