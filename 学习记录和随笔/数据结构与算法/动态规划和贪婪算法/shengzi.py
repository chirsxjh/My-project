def solve(n):
    result=[0 for i in range(n)]
    result[0]=1
    result[1]=2
    result[2]=3
    result[3]=4
    other=[0,1,2,4]
    if n<5:   #直接给答案
        return other[n-1]
    for i in range(4,n):  #从绳子长度5开始计算
        max_val=0
        for j in range(int(i/2)):   #从已有数组计算最优解，需循环
            if result[j]*result[i-1-j]>max_val:
                max_val=result[j]*result[i-1-j]
        result[i]=max_val
    return result[n-1]


ss=solve(10)
print(ss)

