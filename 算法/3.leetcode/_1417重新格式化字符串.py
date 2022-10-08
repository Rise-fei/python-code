def solution(s):
    alpha_num = 0
    digit_num = 0
    alpha_list = []
    digit_list = []
    for i in s:
        if i.isalpha():
            alpha_num += 1
            alpha_list.append(i)
        else:
            digit_num += 1
            digit_list.append(i)
    if abs(alpha_num - digit_num) > 1:
        return ""
    ret = []
    if alpha_num > digit_num:
        i = 0
        while i < len(digit_list):
            ret.append(alpha_list[i])
            ret.append(digit_list[i])
            i += 1
        ret.append(alpha_list[-1])
    else:
        i = 0
        while i < len(alpha_list):
            ret.append(digit_list[i])
            ret.append(alpha_list[i])
            i += 1
        if i == len(digit_list) - 1:
            ret.append(digit_list[-1])
    return "".join(ret)

s = "ab123"
ret = solution(s)
print(ret)
