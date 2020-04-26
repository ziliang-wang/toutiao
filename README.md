# splash+lua+scrapy抓取今日头条热点新闻前n笔
splash+lua+scrapy抓取异步数据(今日头条热点新闻前n笔)
##### 1，抓包截图
###### 默认12笔，每次拉到最底端会再加载12笔，以此不断的循环，经观察，每一次加载出来的Request URL都是经过加密且都是异步请求，selenium不适用此场景
![img1](https://github.com/ziliang-wang/toutiao/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200426094344.png)
##### 2，关键代码-splash无头浏览器内的lua脚本
###### splash透过lua脚本来控制浏览器的操作，红框处是lua代码段，定义了2个js代码，由splash:runjs()方法运行脚本，js1是首次进入首页时，滚轴拉到当前页面的一半(scrollHeight/2)，js2是直拉到页面底部的动作代码，再透过for循环，重复运行7次，本项目是7次，若想获取更多数据，加大循环次数即可，但很可能会被封！
![img2](https://github.com/ziliang-wang/toutiao/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200426092936.png)
##### 3，spider爬虫的解析代码
###### 此部份很简单，不多做说明，红框处则是SplashRequest请求内的参数，必传参数有url和args以endpoing，args传入一个字典，lua_source字段指定lua脚本的来源，这里是lua_code变量，wait字段为等待时间，images字段决定了是否在加载时加载图片，0为不加载，参数endcoding指定了splash服务器的接口，因为要在python代码里运行lua脚本，所以必须指定execute做为接口，相当于在localhost:8050/execute这个url传参
![img3](https://github.com/ziliang-wang/toutiao/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200426093621.png)

