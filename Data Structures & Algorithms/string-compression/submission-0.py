class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 1
        L = 0

        for R in range(1,len(chars)+1):
            if R < len(chars) and chars[R] == chars[R-1]:
                counter += 1
            else:
                chars[L] = chars[R-1]
                L += 1
                if counter > 1:
                    for k in str(counter):
                        chars[L] = k 
                        L += 1
                counter = 1
        return L

