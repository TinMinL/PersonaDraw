## 一、建立环境

先把项目目录和环境分清，本小姐可不愿您重建环境时连源码也搭进去。把入口文件放在项目根目录，虚拟环境单独放进子目录。它基于创建时的解释器，默认隔离第三方包，让这个工具的依赖有自己的位置。[1]

在 Windows CMD 中依次输入：

```bat
cd /d C:\work\mytool
python --version
python -m venv .venv
.venv\Scripts\activate.bat
python -c "import sys; print(sys.executable)"
```

先确认版本命令正常，再创建环境。最后输出应指向下面的解释器；若不是，先处理路径问题，暂缓安装。激活只是调整当前终端的查找路径，并没有替换电脑上的其他解释器。[1]

```text
C:\work\mytool\.venv\Scripts\python.exe
```

## 二、安装依赖

确认解释器后再安装，顺序请别颠倒：通过解释器调用安装工具，才能明确包要装进哪里。

```bat
python -m pip install requests
python main.py
```

安装结束后实际运行入口，检查需要网络请求的功能是否正常。看到安装成功还不算验收完成，程序能用才值得喝茶庆祝，desuwa。标准库随解释器提供，不必把每个导入名称都拿去安装。若运行失败，先辨认是缺包还是程序自身的配置问题。

## 三、记录依赖

在刚才确认过的环境中导出：

```bat
python -m pip freeze > requirements.txt
```

这会覆盖同名文件，先确认旧清单没有需要保留的内容。导出结果记录当前已安装的包，不扫描源码，也不是完整锁文件；试装但没有使用的包也可能进入清单，所以我会先检查内容，再把它交给下一台电脑。[2]

默认会省略部分引导工具；从指定的较新版本起，默认省略的是安装工具本身。若确实需要列出全部已安装包，可以使用下面的命令，并留意它同样会覆盖文件。[2]

```bat
python -m pip freeze --all > requirements.txt
```

在 README 中另记 Python 版本、入口、数据与配置要求，以及依赖的外部程序。包清单管不到这些条件，少记一项，恢复时就要多猜一次。

## 四、换电脑

先核对新旧电脑的 Python 主次版本与架构，再复制源码、依赖清单及需要的数据配置。环境目录留在原处即可：其中脚本可能包含绝对路径，直接搬运并不可靠。[1]

在新电脑的项目目录重建：

```bat
cd /d C:\work\mytool
python --version
python -m venv .venv
.venv\Scripts\activate.bat
python -c "import sys; print(sys.executable)"
python -m pip install -r requirements.txt
python main.py
```

路径确认无误再继续安装。我会按说明补齐数据配置和外部程序，然后实际检查功能；即使包版本相同，也不保证跨平台完全复现，别让一份清单承担它做不到的承诺。

## 五、Git

在项目根目录的 .gitignore 中写入：

```gitignore
.venv/
```

提交源码、清单和说明即可，环境适合按记录重建，不宜纳入版本管理。[1] 这样换目录或换电脑时，也不会把旧路径当作可用配置沿用。若环境目录已经被跟踪，仅补忽略规则不会取消跟踪；请先检查跟踪状态，再判断是否还有后续处理，别看到规则写好了便认定已经生效。

## 六、排错

找不到解释器时，先确认安装和命令是否可用；若启动器可用，可以改用它创建环境：

```bat
py -m venv .venv
```

安装后仍缺包，请再次打印解释器路径，并核对编辑器选择的解释器是否与终端一致。本小姐会先查包究竟装给了谁，重复安装未必能解决错位。

新终端需要重新激活；也可以直接指定环境解释器，不依赖激活状态：[1]

```bat
.venv\Scripts\python.exe main.py
```

遇到版本不兼容，先读报错，核对它指向的解释器或依赖版本条件，再决定调整哪项；不要盲目清空版本限制，那只会把明确的问题换成更难判断的组合。

[1] https://docs.python.org/3/library/venv.html

[2] https://pip.pypa.io/en/stable/cli/pip_freeze/
