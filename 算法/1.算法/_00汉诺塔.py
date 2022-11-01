'''
所有盘子  由 A 经过 C 移动 B         a,c,b
1.n-1个  由 a 经过 b 移动 到 c       a，b,c
2. 移动 a --- b
3. n - 1 个 由 c 经过a 移动到 b     c,a,b
'''

def hannuo(n,a,c,b):
    if n > 0:
        hannuo(n-1,a,b,c)
        print('move--',a,"-----",b)
        hannuo(n-1,c,a,b)

hannuo(3,'A','C','B')