class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        i = 0
        li = []

        a_index = 1
        b_index = 1

        while i < n:
            aa = a * a_index
            bb = b * b_index
            if aa < bb:
                li.append(aa)
                a_index += 1
            elif aa > bb:
                li.append(bb)
                b_index += 1
            else:
                li.append(aa)
                a_index += 1
                b_index += 1

            i += 1
        return li[-1] % (10 ** 9 + 7)


s = Solution()
ret = s.nthMagicalNumber(1000000000, 40000,  40000)
print(ret)
