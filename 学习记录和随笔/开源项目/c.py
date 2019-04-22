    #print 'a'
#_*_ coding:utf-8 _*_
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key = lambda x:x[0])
print intervals
res = [intervals[0]]
print res[-1]
'''
adic = {1:98,2:12,3:78}

alist= []
for i in adic.items():
    alist.append(i)

print alist
alist.sort(key=lambda x: x[1])
print alist

l = ['鹅鹅鹅', '曲项向天歌', '锄禾日当午', '春种一粒粟']
for i, v in enumerate(l):
    print( v)


d = dict()
dict[2] = 0
print (d)
'''