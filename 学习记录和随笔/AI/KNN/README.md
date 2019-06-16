## KNN K-近邻算法
### KNN简介
k-近邻（kNN, k-NearestNeighbor）算法是一种基本分类与回归方法，k 近邻算法的输入为实例的特征向量，对应于特征空间的点；输出为实例的类别，可以取多类。k 近邻算法假设给定一个训练数据集，其中的实例类别已定。分类时，对新的实例，根据其 k 个最近邻的训练实例的类别，通过多数表决等方式进行预测。因此，k近邻算法不具有显式的学习过程。
  
k 近邻算法实际上利用训练数据集对特征向量空间进行划分，并作为其分类的“模型”。 k值的选择、距离度量以及分类决策规则是k近邻算法的三个基本要素。
![](https://pic4.zhimg.com/v2-64a4aa7703c118377aec1868a8edef0f_b.jpg)
![](https://pic2.zhimg.com/v2-c59415d2b783e8505c284f507cd318c5_b.jpg)
例子：
![](https://pic1.zhimg.com/v2-eea2fdf7d0008e024e62f35690e90a94_b.jpg)
图中绿色的点就是我们要预测的那个点，假设K=3。那么KNN算法就会找到与它距离最近的三个点（这里用圆圈把它圈起来了），看看哪种类别多一些，比如这个例子中是蓝色三角形多一些，新来的绿色点就归类到蓝三角了.
![](https://pic2.zhimg.com/v2-136a496fcd752d1b72ae7d958a256b41_b.jpg)
但是，当K=5的时候，判定就变成不一样了。这次变成红圆多一些，所以新来的绿点被归类成红圆。从这个例子中，我们就能看得出K的取值是很重要的。

明白了大概原理后，主要有两个，**K值的选取和点距离的计算**
### 距离计算
要度量空间中点距离的话，有好几种度量方式，比如常见的曼哈顿距离计算，欧式距离计算等等。不过通常KNN算法中使用的是欧式距离，这里只是简单说一下，拿二维平面为例，，二维空间两个点的欧式距离计算公式如下
![](https://pic3.zhimg.com/v2-df7d6da3877de383fd5bfb1b72eeb92e_b.jpg)
拓展到多维空间，则公式变成这样：
![](https://pic3.zhimg.com/v2-f7cee96fcd460737f383681ccaacc1a2_b.jpg)
KNN算法最简单粗暴的就是将预测点与所有点距离进行计算，然后保存并排序，选出前面K个值看看哪些类别比较多。但其实也可以通过一些数据结构来辅助，比如最大堆，这里就不多做介绍，有兴趣可以百度最大堆相关数据结构的知识
### K值选择
K的取值比较重要，那么该如何确定K取多少值好呢？答案是通过**交叉验证**（将样本数据按照一定比例，拆分出训练用的数据和验证用的数据，比如6：4拆分出部分训练数据和验证数据），从选取一个较小的K值开始，不断增加K的值，然后计算验证集合的方差，最终找到一个比较合适的K值。
![](https://pic2.zhimg.com/v2-3ad2d58fa60fa20bdf8e97b9d6bb6491_b.jpg)
增大k的时候，一般错误率会先降低，因为有周围更多的样本可以借鉴了，分类效果会变好。但注意，和K-means不一样，当K值更大的时候，错误率会更高。这也很好理解，比如说你一共就35个样本，当你K增大到30的时候，KNN基本上就没意义了。所以选择K点的时候可以选择一个较大的临界K点，当它继续增大或减小的时候，错误率都会上升，比如图中的K=10。具体如何得出K最佳值的代码.
### KNN特点
KNN是一种非参的，惰性的算法模型。非参，什么是惰性呢？  
* 非参的意思并不是说这个算法不需要参数，而是意味着这个模型不会对数据做出任何的假设，与之相对的是线性回归（我们总会假设线性回归是一条直线）。也就是说KNN建立的模型结构是根据数据来决定的，这也比较符合现实的情况，毕竟在现实中的情况往往与理论上的假设是不相符的。
* 惰性又是什么意思呢？想想看，同样是分类算法，逻辑回归需要先对数据进行大量训练（tranning），最后才会得到一个算法模型。而KNN算法却不需要，它没有明确的训练数据的过程，或者说这个过程很快。
### 优势和劣势
KNN算法的优势和劣势了解KNN算法的优势和劣势，KNN算法优点简单易用，相比其他算法，
KNN算是比较简洁明了的算法。即使没有很高的数学基础也能搞清楚它的原理。模型训练时间快，上面说到KNN算法是惰性的，这里也就不再过多讲述。预测效果好。对异常值不敏感KNN算法缺点对内存要求较高，因为该算法存储了所有训练数据预测阶段可能很慢对不相关的功能和数据规模敏感至于什么时候应该选择使用KNN算法。  

### 代码实现：
#### 导入大顶堆和KD-Tree 
```
from ..utils.kd_tree import KDTree
from ..utils.max_heap import MaxHeap
```
####  创建KNeighborsBase类
k_neighbors存储k值，tree用来存储kd_tree。class KNeighborsBase(object):
  
    def __init__(self):
        self.k_neighbors = None
        self.tree = None

#### 训练KNN模型
设定k值，并建立kd-Tree  

```
def fit(self, X, y, k_neighbors=3):
    self.k_neighbors = k_neighbors
    self.tree = KDTree()
    self.tree.build_tree(X, y)
```

#### 创建KDTree类
寻找Xi的k近邻，代码看不懂没关系。慢慢来，毕竟我自己回过头来看这段代码也是一言难尽。
1. 获取kd_Tree

2. 建立大顶堆

3. 建立队列

4. 外层循环更新大顶堆

5. 内层循环遍历kd_Tree

6. 满足堆顶是第k近邻时退出循环


```
作者：李小文
链接：https://zhuanlan.zhihu.com/p/53737727
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

def _knn_search(self, Xi):
    tree = self.tree
    heap = MaxHeap(self.k_neighbors, lambda x: x.dist)
    nd = tree._search(Xi, tree.root)
    que = [(tree.root, nd)]
    while que:
        nd_root, nd_cur = que.pop(0)
        nd_root.dist = tree._get_eu_dist(Xi, nd_root)
        heap.add(nd_root)
        while nd_cur is not nd_root:
            nd_cur.dist = tree._get_eu_dist(Xi, nd_cur)
            heap.add(nd_cur)
            if nd_cur.brother and \
                    (not heap or
                        heap.items[0].dist >
                        tree._get_hyper_plane_dist(Xi, nd_cur.father)):
                _nd = tree._search(Xi, nd_cur.brother)
                que.append((nd_cur.brother, _nd))
            nd_cur = nd_cur.father
    return heap
```
#### 分类问题的预测方法
找到k近邻，取众数便是预测值。这里的写法仅针对二分类问题  

    def _predict(self, Xi):
        heap = self._knn_search(Xi)
        n_pos = sum(nd.split[1] for nd in heap._items)
        return int(n_pos * 2 > self.k_neighbors)
#### 回归问题的预测方法
找到k近邻，取均值便是预测值  

```
def _predict(self, Xi):
    heap = self._knn_search(Xi)
    return sum(nd.split[1] for nd in heap._items) / self.k_neighbors
```

#### 多个样本预测
_predict只是对单个样本进行预测，所以还要写个predict方法。  

    def predict(self, X):
        return [self._predict(Xi) for Xi in X]


#### 效果评估
####  分类问题
使用著名的乳腺癌数据集，按照7:3的比例拆分为训练集和测试集，训练模型，并统计准确度。(注意要对数据进行归一化)  

   

```
@run_time
def main():
    print("Tesing the performance of KNN classifier...")
    X, y = load_breast_cancer()
    X = min_max_scale(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=20)
    clf = KNeighborsClassifier()
    clf.fit(X_train, y_train, k_neighbors=21)
    model_evaluation(clf, X_test, y_test)
        
```
#### 回归问题
使用著名的波士顿房价数据集，按照7:3的比例拆分为训练集和测试集，训练模型，并统计准确度。(注意要对数据进行归一化)  

```
@run_time
def main():
    print("Tesing the performance of KNN regressor...")
    X, y = load_boston_house_prices()
    X = min_max_scale(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=10)
    reg = KNeighborsRegressor()
    reg.fit(X=X_train, y=y_train, k_neighbors=3)
    get_r2(reg, X_test, y_test)
```
### 总结
KNN分类的原理：用KD-Tree和大顶堆寻找最k近邻
KNN分类的实现：队列加两层while循环