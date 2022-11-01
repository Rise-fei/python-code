import heapq

li = [1, 5, 4, 2, 45, 3, 42, 34]
# 建立堆,默认小根堆
heapq.heapify(li)
print(li)
for i in range(len(li)):
    s = heapq.heappop(li)  # 弹出堆中最小的值
    print(s)
