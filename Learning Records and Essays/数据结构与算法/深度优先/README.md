### 题目：二叉搜索树
Input:二叉树 

Output:boolean值  

Conditions:检验一个二叉树是不是有效的二叉搜索树  

题目思路:

注意到，每层的最大最小约束都是不一样的，所以采用dfs的思想，不断更新最大最小值。在python中，数字可以取很大，要设大一点

我出现错误的思路：  
想的是直接和左右值比较，看是否符合对顶，但是忽略了隔层之间可能存在不符合规定的可能性，所以代码是错的

