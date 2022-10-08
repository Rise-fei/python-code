# 售价 5元，   5,10,20找零
l = [5,10,5,10,5,5,5,20,20]

five = 0
ten = 0
for i in l:
    if i == 5:
        five += 1
    elif i == 10:
        if five > 0:
            five -= 1
            ten += 1
        else:
            print('NO')
            break
    else:
        if five > 0 and ten > 0:
            five -= 1
            ten -= 1
        elif five >= 3:
            five -= 3
        else:
            print('NO')
            break
