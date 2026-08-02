class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}
        for element in s1:
            hashMap1[element] = 1 + hashMap1.get(element,0) 

        L = 0
        for R in range(len(s2)):
            while R - L + 1 > len(s1):
                if s2[L] in hashMap2:
                    hashMap2[s2[L]]-= 1
                L+=1
            hashMap2[s2[R]] = 1 + hashMap2.get(s2[R],0)
            print(f"This is hashMap2: {hashMap2} and hashMap1: {hashMap1}") 

            if hashMap1.items() <= hashMap2.items():
                print(f"hashMap1: {hashMap1} and hashMap2: {hashMap2}") 
                return True

        return False

            


