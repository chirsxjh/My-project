# session和cookie
----
1. session 在服务器端，cookie 在客户端（浏览器）
2. session 默认被存在在服务器的一个文件里（不是内存）
3. session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，同时 session 也会失效（但是可以通过其它方式实现，比如在 url 中传递 session_id）
4. session 可以放在 文件、数据库、或内存中都可以。
5. 用户验证这种场合一般会用 session 因此，维持一个会话的核心就是客户端的唯一标识，即 session id
### session和cookie有何区别？
**cookie保存在客户端，session保存在服务器端**  
**cookie目的可以跟踪会话，也可以保存用户喜好或者保存用户名密码**  
**session用来跟踪会话**  
当我们登录网站勾选保存用户名和密码的时候，一般保存的都是cookie，将用户名和密码的cookie保存到硬盘中，这样再次登录的时候浏览器直接将cookie发送到服务端验证，直接username和password保存到客户端，当然这样不安全，浏览器也可以加密解密这样做，每个浏览器都可以有自己的加密解密方式，这样方便了用户，再比如用户喜欢的网页背景色，比如QQ空间的背景，这些信息也是可以通cookie保存到客户端的，这样登录之后直接浏览器直接就可以拿到相应的偏好设置。  

②跟踪会话，比如某些网站中网页有不同的访问权限，有只能登录的用户访问的网页或者用户级别不同不能访问的，但是http请求是无状态的，每次访问服务端是不知道是否是登录用户，很自然的想到在http请求报文中加入登录标识就可以了，这个登录标识就可以是cookie，这样的cookie服务端要保存有所有登录用户的cookie，这样请求报文来了之后拿到登录标识cookie，在服务端进行比较久可以了。再比如购物网站，多次点击添加商品到购物车客户端很容易知道哪些物品在购物车中，但是服务端怎么知道每次添加的物品放到哪个登录用户的购物车中呢？也需要请求报文中带着cookie才行（在不登陆的情况下京东也是可以不断添加商品的，推测应该是登录的时候一并创建cookie并且发送物品信息），这些cookie都是为了跟踪会话用的，所以客户端有，服务端也有，并且服务端有全部的会话cookie。后面衍生出session技术,session技术是要使用到cookie的，之所以出现session技术，主要是为了安全。  

http是无状态的协议，客户每次读取web页面时，服务器都打开新的会话，而且服务器也不会自动维护客户的上下文信息，那么要怎么才能实现网上商店中的购物车呢，session就是一种保存上下文信息的机制，它是针对每一个用户的，变量的值保存在服务器端，通SessionID来区分不同的客户,session是以cookie或URL重写为基础的，默认使用cookie来实现，系统会创造一个名为JSESSIONID的输出cookie，我们叫做session cookie,以区别persistent cookies,也就是我们通常所说的cookie,注意session cookie是存储于浏览器内存中的，并不是写到硬盘上的，这也就是我们刚才看到的JSESSIONID，我们通常情是看不到JSESSIONID的，但是当我们把浏览器的cookie禁止后，web服务器会采用URL重写的方式传递Sessionid，我们就可以在地址栏看sessionid=KWJHUG6JJM65HS2K6之类的字符串。  
![png](https://pic4.zhimg.com/80/249c3f10f411af56640113b615c972be_hd.jpg)  
大家请看在HTTP请求报文头的最后一行有cookie，不过是JSessionID的cookie值Cookie: $Version=1;Skin=new;jsessionid=5F4771183629C9834F8382E23BE13C4C  比如前两个值，应该属于偏好设置之类的。服务端是怎么知道客户端的多个请求是隶属于一个Session呢？注意到后台的那个jsessionid=5F4771183629C9834F8382E23BE13C4C木有？原来就是通过HTTP请求报文头的Cookie属性的jsessionid的值关联起来的！（当然也可以通过重写URL的方式将会话ID附带在每个URL的后面哦）  

明白了原理，我们就可以很容易的分辨出persistent cookies和session cookie的区别了，网上那些关于两者安全性的讨论也就一目了然了，session cookie针对某一次会话而言，会话结束session cookie也就随着消失了，而persistent cookie只是存在于客户端硬盘上的一段文本（通常是加密的），而且可能会遭到cookie欺骗以及针对cookie的跨站脚本攻击，自然不如 session cookie安全了。  

通常session cookie是不能跨窗口使用的，当你新开了一个浏览器窗口进入相同页面时，系统会赋予你一个新的sessionid，这样我们信息共享的目的就达不到了，此时我们可以先把sessionid保存在persistent cookie中，然后在新窗口中读出来，就可以得到上一个窗口SessionID了，这样通过session cookie和persistent cookie的结合我们就实现了跨窗口的session tracking（会话跟踪）。  
在一些web开发的书中，往往只是简单的把Session和cookie作为两种并列的http传送信息的方式，session cookies位于服务器端，persistent cookie位于客户端，可是session又是以cookie为基础的，明白的两者之间的联系和区别，我们就不难选择合适的技术来开发web service了。

* 由于HTTP协议是无状态的协议，所以服务端需要记录用户的状态时，就需要用某种机制来识具体的用户，这个机制就是Session.典型的场景比如购物车，当你点击下单按钮时，由于HTTP协议无状态，所以并不知道是哪个用户操作的，所以服务端要为特定的用户创建了特定的Session，用用于标识这个用户，并且跟踪用户，这样才知道购物车里面有几本书。**这个Session是保存在服务端的，有一个唯一标识**。在服务端保存Session的方法很多，内存、数据库、文件都有。集群的时候也要考虑Session的转移，在大型的网站，一般会有专门的Session服务器集群，用来保存用户会话，这个时候 Session 信息都是放在内存的，使用一些缓存服务比如Memcached之类的来放 Session。  
* 思考一下服务端如何识别特定的客户？这个时候Cookie就登场了。每次HTTP请求的时候，客户端都会发送相应的Cookie信息到服务端。实际上大多数的应用都是用 Cookie 来实现Session跟踪的，第一次创建Session的时候，服务端会在HTTP协议中告诉客户端，需要在 Cookie 里面记录一个Session ID，以后每次请求把这个会话ID发送到服务器，我就知道你是谁了。有人问，如果客户端的浏览器禁用了 Cookie 怎么办？一般这种情况下，会使用一种叫做URL重写的技术来进行会话跟踪，即每次HTTP交互，URL后面都会被附加上一个诸如 sid=xxxxx 这样的参数，服务端据此来识别用户。  
* Cookie其实还可以用在一些方便用户的场景下，设想你某次登陆过一个网站，下次登录的时候不想再次输入账号了，怎么办？这个信息可以写到Cookie里面，访问网站的时候，网站页面的脚本可以读取这个信息，就自动帮你把用户名给填了，能够方便一下用户。这也是Cookie名称的由来，给用户的一点甜头。  
### 总结一下:    
Session是在服务端保存的一个数据结构，用来跟踪用户的状态，这个数据可以保存在集群、数据库、文件中；  
Cookie是客户端保存用户信息的一种机制，用来记录用户的一些信息，也是实现Session的一种方式。
