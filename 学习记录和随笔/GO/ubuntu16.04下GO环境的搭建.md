# ubuntu16.04 GO环境的搭建

### 安装

使用命令 ```sudo apt-get install golang-go``进行安装，大概需要三分钟左右

![](/home/xiang/mygit/学习记录和随笔/图片/9.4.1.PNG)

查看GO的版本

![](/home/xiang/mygit/学习记录和随笔/图片/9.4.2.PNG)

### 配置环境变量

首先创建一个go工作区的文件夹

```mkdir ~/GO```(文件夹名字随意)

其次Go和其他语言不同的特殊之处在于需要保存在工作区中，所以我们需要自己建一个工作文件夹，我们建立在~/Go中，之后我们需要在环境变量中增加GOPATH指向该目录即可，采用如下代码即可完成。

```
mkdir ~/workspace
echo 'export GOPATH="$HOME/Go"' >> ~/.bashrc
source ~/.bashrc
```

![](/home/xiang/mygit/学习记录和随笔/图片/9.4.3.PNG)

![](/home/xiang/mygit/学习记录和随笔/图片/9.4.4.PNG)



### 运行一个小DEMO

编写hello.go

```
// hello.go
package main
import (
   "fmt"
   "os"
   "strings"
)
  
func main() {
   who := "World!"
   if len(os.Args) > 1 {
       who = strings.Join(os.Args[1: ], " ")
   }
   fmt.Println("Hello", who)
}

```



然后cd到GO目录下使用命令```go build```再l``ls```会出现GO 和 hello.go

最后使用```go run xxx.go``运行代码

效果如图：

![](/home/xiang/mygit/学习记录和随笔/图片/9.4.5.PNG)

