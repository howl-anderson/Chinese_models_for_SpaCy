[README written in English](README.en-US.md)
------------------------------

# SpaCy 中文模型

为 SpaCy 提供的中文数据模型. 这些模型目前比较实现的比较粗糙并且还在 **开发状态**. 但毕竟“有总比没有的好”。

## 在线演示

基于 Jupyter notebook 的在线演示在 [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/howl-anderson/Chinese_models_for_SpaCy/master?filepath=notebooks%2Fdemo.ipynb)。

### 特性
部分 `王小明在北京的清华大学读书` 这个 `Doc` 对象的属性信息:

![attributes_of_doc](.images/attributes_of_doc.png)

### NER (**New!**)
部分 `王小明在北京的清华大学读书` 这个 `Doc` 对象的 NER 信息:

![ner_of_doc](.images/ner_of_doc.png)

## 开始使用

模型用二进制文件的形式进行分发, 用户应该具备基础的 SpaCy （version > 2) 的基础知识.

### 系统要求

Python 3 (也许支持 python2, 但未经过良好测试)

### 安装

从 `releases` 页面下载模型.

```
wget -c https://github.com/howl-anderson/Chinese_models_for_SpaCy/releases/download/v2.0.4/zh_core_web_sm-2.0.4.tar.gz
```

然后安装模型

```
pip install zh_core_web_sm-2.0.4.tar.gz
```


## 运行 Demo 代码

Demo 代码位于 `test.py`. 在安装好模型后，用户下载或者克隆本仓库的代码，然后可以直接执行

```bash
python3 ./test.py
```

打开地址 `http://127.0.0.1:5000`, 将看到如下：

![Dependency of doc](.images/dependency_of_doc.png)

## 如何从零构造这个模型

见 [workflow](workflow.md)

## TODO list

* 属性 `pos_` 不正确. 这个和 SpaCy 中中文语言 Class 相关。
* 属性 `shape_` and `is_alpha` 似乎对中文并无意义, 但需要权威信息确认一下.
* 属性 `is_stop` 不正确. 这个和 SpaCy 中中文语言 Class 相关。
* 属性 `vector` 似乎没有训练的很好。
* <s>属性 `is_oov` 完全错误. 第一优先级修复。</s>
* <s>NER 模型，因为缺少 LDC 语料库，目前不可用. 正在解决中正在训练中。</s> 
* 将训练中所用的中间结果 release 出来, 方便用户自行定制模型

## 使用的组件

* TODO

## 如何贡献

请阅读 [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) , 然后提交 pull requests 给我们.

## 版本化控制

我们使用 [SemVer](http://semver.org/) 做版本化的标准. 查看 `tags` 以了解所有的版本.

## 作者

* **Xiaoquan Kong** - *Initial work* - [howl-anderson](https://github.com/howl-anderson)

更多贡献者信息，请参考 `contributors`.

## 版权

MIT License - 详见 [LICENSE.md](LICENSE.md)

## 致谢

* TODO
