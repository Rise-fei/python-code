l = [1,2,3,2,3,6,5,6,7,8]

def solu(l):
    max_val = 0
    cur_len = 1
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            cur_len += 1
        else:
            cur_len = 1
        max_val = max(cur_len, max_val)
    return max_val

print(solu(l))