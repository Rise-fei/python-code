def clear_list(l):
    print(id(l))
    l = []
    print(id(l))


ll = [1, 2]
print(id(ll))
clear_list(ll)
print(ll)



def fun(l=[1]):
    l.append(1)
    print(l)


fun()
fun()

