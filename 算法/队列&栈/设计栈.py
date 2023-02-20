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

"""
通过两个队列，模拟栈的实现
1, 2, 3, 4, 5 依次进入q1队列
q1 = [5,4,3,2,1]
q2 = []

q1 = [5] 弹出此值 --> []
q2 = [4, 3, 2, 1]

来回导， q1 变 q2. q2变q1
[4, 3, 2, 1]
[]
周而复始， 依次弹出5, 4, 3 ,2, 1
"""


"""
通过两个栈，模拟队列的实现
1,2,3,4,5 依次进s1的栈
push_stack = [1,2,3,4,5]       (左为底部  右边为顶部)
pop_stack = []

每次当pop_stack为空时，才能 导腾 数据，将 push_stack的数据依次导入到pop_stack中
"""