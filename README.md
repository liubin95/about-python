# about python

## 基础依赖

### [pipenv](https://pipenv.pypa.io/en/latest/)

虚拟环境和依赖管理工具

> Pipenv 是一个 Python virtualenv 管理工具，支持多种系统并很好地弥合了系统之间的差距
> pip、python（使用系统 python、pyenv 或 asdf）和 virtualenv。 Linux、macOS 和 Windows 都是一等公民
> 在 Pipenv 中。

#### 安装

```shell
pip install  pipenv
# 设置清华源
# https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
pipenv config set global.pypi-mirror https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 使用

- `Pipfile`：Pipenv 的配置文件，类似于 `package.json`。
- `Pipfile.lock`：Pipenv 的锁文件，类似于 `package-lock.json`。
- `Pipfile` 和 `Pipfile.lock` 用于替代 `requirements.txt`。
- `Pipfile.lock` 需要提交，禁止手动修改。

##### 环境

```shell
# 创建虚拟环境
# --python 指定python版本
pipenv --python 3.8
# 进入虚拟环境
pipenv shell
# 运行脚本
python main.py
# 直接运行脚本
pipenv run python main.py
# 退出虚拟环境
exit
```

##### 依赖

```shell
# 安装 black 依赖
pipenv install black --dev
# 安装 black[jupyter] 依赖
pipenv install black[jupyter] --dev
# 安装指定版本的依赖
pipenv install black==19.10b0 --dev
# 卸载依赖
pipenv uninstall black
# 升级依赖
pipenv update black
```

```shell
# 安装全部依赖
pipenv install
# 安装全部依赖(包括开发依赖)
pipenv install --dev
# 查看依赖
pipenv graph
# 生成requirements.txt
pipenv requirements --dev --hash > requirements.txt
```

### [pyenv](https://github.com/pyenv/pyenv)

> pyenv 可让您轻松地在多个 Python 版本之间切换。
> 它简单、不引人注目，并且遵循 UNIX 单一用途工具只做好一件事的传统。
> 该项目是从rbenv和 ruby​​-build分叉出来的，并针对 Python 进行了修改。

### [pylint](https://pypi.org/project/pylint/)

静态代码检查工具

> Pylint是Python 2或3的静态代码分析器。最新版本支持Python 3.8.0及以上版本。皮林特
> 分析您的代码而不实际运行它。它检查错误，执行编码标准，查找代码异味，
> 并可以就如何重构代码提出建议。

#### 全局安装

```shell
brew install pylint
```

#### 项目安装

```shell
pipenv install pylint --dev
```

### [black](https://pypi.org/project/black/)

代码格式化

> Black 是不妥协的 Python 代码格式化程序。通过使用它，您同意放弃对细节细节的控制
> 手动格式化。作为回报，Black 为您提供速度、确定性和免于 pycodestyle 对格式的烦扰。
> 您将为更重要的事情节省时间和精力。

#### 全局安装

无法安装`black[jupyter]`,如果需要格式化`jupyter`文件,需要在项目中安装

```shell
brew install black
```

#### 项目安装

```shell
pipenv install black --dev
# pycharm 配置
# black 选择 打包
```

## jupyter
