
"""
通过两个队列，模拟栈的实现

q1 =  5 4 3 2 1
q2 =  None

pop()
q1 = 5
q2 = 4 3 2 1
弹出q1


两个队列来回导， 每次留1个数弹出，其他的倒走
"""


"""
链表构建栈：
push   不断的加头结点
pop    去除头结点，设置2结点为新头

数组构建栈：
push  index++  li[index] = new_val
pop   index--

extra： 额外设计栈，需要维护 每次得到栈中最小值为O（1）
    解法1：
    设计两个栈，第一个为data栈， 第二个为 min栈【每次data新进的数据跟min的栈顶做判断，谁小加谁到min中】

    data = [3,4,2,2,7]
    min = [3,3,2,2,2]

    pop的时候，需要两个栈同时pop
    min中的栈顶就是 实时的data栈最小值

    优化2：
    min栈中，每次data新的数据跟min栈顶做判断，如果>min-top,不动，否则，加入min栈中
    data = [3,4,2,2,7]
    min = [3,2,2]

    pop的时候，需要额外判断，如果data > min 则只pop data  否则 pop- data   && pop - min
"""
