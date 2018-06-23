## scrapy简介
----
## Scrapy
该框架是Python开发的一个快速、高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。  
**各功能组件流程图**  
![png](https://upload-images.jianshu.io/upload_images/8332299-e0b022368b063020.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)  
**Scrapy Engine**  
引擎负责控制数据流在系统中所有组件中流动，并在相应动作发生时触发事件。 详细内容查看下面的数据流(Data Flow)部分  
**调度器(Scheduler)**  
调度器从引擎接受request并将他们入队，以便之后引擎请求他们时提供给引擎  
**下载器(Downloader)**  
下载器负责获取页面数据并提供给引擎，而后提供给spider  
**Spiders**  
Spider是Scrapy用户编写用于分析response并提取item(即获取到的item)或额外跟进的URL的类。 每 个spider负责处理一个特定(或一些)网站  
**Item Pipeline**  
Item Pipeline负责处理被spider提取出来的item。典型的处理有清理、 验证及持久化(例如存取到数 据库中)  
**下载器中间件(Downloader middlewares)**  
下载器中间件是在引擎及下载器之间的特定钩子(specific hook)，处理Downloader传递给引擎的 response。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能  
**Spider中间件(Spider middlewares)**  
Spider中间件是在引擎及Spider之间的特定钩子(specific hook)，处理spider的输入(response)和输出 (items及requests)。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能  
**数据流(Data flow)**  
### Scrapy中的数据流由执行引擎控制，其过程如下:  
引擎打开一个网站(open a domain)，找到处理该网站的Spider并向该spider请求第一个要爬取的 URL(s)。  
引擎从Spider中获取到第一个要爬取的URL并在调度器(Scheduler)以Request调度。  
引擎向调度器请求下一个要爬取的URL。  
调度器返回下一个要爬取的URL给引擎，引擎将URL通过下载中间件(请求(request)方向)转发给下载 器(Downloader)。  
一旦页面下载完毕，下载器生成一个该页面的Response，并将其通过下载中间件(返回(response)方 向)发送给引擎。  
引擎从下载器中接收到Response并通过Spider中间件(输入方向)发送给Spider处理  。
Spider处理Response并返回爬取到的Item及(跟进的)新的Request给引擎。  
引擎将(Spider返回的)爬取到的Item给Item Pipeline，将(Spider返回的)Request给调度器。  
(从第二步)重复直到调度器中没有更多地request，引擎关闭该网站.  
### scrapy的流程如图，并且可归纳如下:
* 首先下载器下载request回执的html等的response
* 然后下载器传给爬虫解析
* 接着爬虫解析后交给调度器过滤，查重等等
* 最后交给管道，进行爬取数据的处理





