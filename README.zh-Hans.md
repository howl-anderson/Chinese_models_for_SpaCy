[README written in English](README.md)
------------------------------

# SpaCy 中文模型

为 SpaCy 提供的中文数据模型. 这些模型目前比较实现的比较粗糙并且还在开发状态. 但毕竟“有总比没有的好”。

## 开始使用

模型用二进制文件的形式进行分发, 用户应该具备基础的 SpaCy （version > 2) 的基础知识.

### 系统要求

Python 3 (也许支持 python2, 但未经过良好测试)

### 安装

从 `releases` 页面下载模型.

```
wget -c XXX.tar.gz
```

然后安装模型

```
pip install XXX.tar.gz
```


## 运行 Demo 代码

Demo 代码位于 `test.py`. 在安装好模型后，可以直接执行

```bash
python3 ./test.py
```

打开地址 `http://127.0.0.1:5000`, 将看到如下：

![Dependency of doc](.images/dependency_of_doc.png)


## Built With

* TODO

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the `tags` on this repository.

## Authors

* **Xiaoquan Kong** - *Initial work* - [howl-anderson](https://github.com/howl-anderson)

See also the list of `contributors` who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* TODO
