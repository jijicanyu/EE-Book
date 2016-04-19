# EE-Book

[中文](./README_cn.md) | [English](./README.md)

*Note*: Due to personal reason, there will be no big changes in the next two months, Only a few small patches.   --2016.04.19  

[EE-Book](https://github.com/knarfeh/EE-Book) is a command-line utility to downlaod text from the Web, and make it a e-book. GUI is under developing.

## Supported Sites (UPDATING!)

* [https://www.zhihu.com/](https://www.zhihu.com/)
* [https://www.jianshu.com/](https://www.jianshu.com/)
* [http://blog.sina.com.cn/](http://blog.sina.com.cn/)
* [http://blog.csdn.net/](http://blog.csdn.net/)

## Usage

get help info:  

```shell
python ee-book -h
```

for example:  

```shell
python ee-book -u http://www.jianshu.com/users/b1dd2b2c87a8/latest_articles
```

after a while, you will get the e-book:   

![yinwang](http://7xi5vu.com1.z0.glb.clouddn.com/2016-03-09jianshu_yinwang.png)

## Contributing

...would be awesome! 

### requirements

 * [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/)
 * [lxml](http://lxml.de/)
 * [PyQt4](https://www.riverbankcomputing.com/software/pyqt/download)

### Setting up a development environment for EE-Book 

```shell
$ sudo pip install -r requirements.txt
```

[install pyqt4](https://riverbankcomputing.com/software/pyqt/download/)


### [TODO List](./doc/TODOlist.md)

## Relevant Infomation

* previous [README](https://github.com/knarfeh/EE-Book/blob/c4d870ff8cca6bbac97f04c9da727397cee8d519/README.md)

* An [article](http://knarfeh.github.io/2016/03/17/EE-Book/) posted on [v2ex](https://v2ex.com/)

## License

EE-Book is licensed under the terms of [MIT license](./LICENSE).

