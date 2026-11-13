## 建立环境

先把项目放在 `C:\work\mytool`，让 `main.py` 留在项目根目录。虚拟环境默认隔离第三方包，并基于创建它的 Python；本龙先替你把不同工具的依赖分开，免得装一个包，隔壁项目也跟着受影响。[1] 在 Windows CMD 逐行输入：

```bat
cd /d C:\work\mytool
python --version
python -m venv .venv
.venv\Scriptsctivate.bat
python -c "import sys; print(sys.executable)"
```

创建前先看版本是否符合项目需要；激活后应看到指向项目内 `.venv\Scripts\python.exe` 的路径，再继续安装。提示符有变化还不够，解释器路径才是我们要认的证据。源码别塞进环境里，否则日后重建环境，连自己的代码也要陪着折腾。

## 安装依赖

确认解释器后，再装示例依赖并运行入口：

```bat
python -m pip install requests
python main.py
```

我让你用解释器调用安装器，是为了让安装目标跟刚才确认的环境对应起来。标准库不需额外安装，别见到一个导入名称就急着找包。（安装器没有报错，也不代表工具已经能用了。）接着看入口能否完成你预期的操作；若程序还需要数据或配置，先补齐再判断。环境隔离的是包，不能替你准备业务所需的一切。

## 记录依赖

工具在这套环境里运行正常后，导出当前包清单：

```bat
python -m pip freeze > requirements.txt
```

注意，这条命令会覆盖文件；已有清单时先检查是否需要保留原内容。它记录已安装的包，不会扫描源码找出真正用到哪些，也不生成完整锁文件。[2] 所以本龙会先确认这里没混进其他项目的试验包，再把清单交给下一台电脑；清单再长，也不等于准备得更周全。

默认还会省略部分引导工具，Python 3.12 之后默认省略 pip；确实要包含全部时才加 `--all`。另外在 README 记下 Python 版本、入口、数据配置和外部程序。包清单负责包，剩下这些条件得另外交代，免得未来的你只能靠猜。

## 换电脑

先拿到源码、清单和说明，核对新电脑的 Python 主次版本与架构。别先复制旧环境碰运气：环境里的脚本可能含绝对路径，它本来就不适合直接搬家。[1] 在新电脑的项目目录中重新建立环境：

```bat
cd /d C:\work\mytool
python --version
python -m venv .venv
.venv\Scriptsctivate.bat
python -c "import sys; print(sys.executable)"
python -m pip install -r requirements.txt
python main.py
```

路径确认正确后才安装，再按说明补数据配置与外部程序，实际运行验收。即使包都装好了，也不能保证跨平台完全复现；我会把运行结果当完成标志，不拿安装成功替整件事盖章。

## Git

在项目根目录的 `.gitignore` 写入：

```gitignore
.venv/
```

环境可以重建，又带有本机路径，不上传它能避免把机器相关的目录当成项目源码保存。[1] 应保留的是源码、依赖清单与恢复说明。这里有个容易踩的边界：已经被 Git 跟踪的环境，仅加忽略规则不会取消跟踪。先看它是否仍在跟踪范围内；写进忽略文件，不等于过去的记录自动失忆。

## 排错

找不到 `python` 时，先确认命令是否可用；若 `py` 可用，可改用 `py -m venv .venv` 创建，随后激活并核对解释器路径。

装完仍缺包，我先查当前终端和编辑器分别用了哪个解释器，两边都应指向项目环境。别一上来反复安装，装进另一处，再勤快也救不了当前这一处。

新终端需重新激活，因为激活只改变当前终端的查找路径；不想激活，也能直接调用环境解释器：[1]

```bat
.venv\Scripts\python.exe main.py
```

遇到版本不兼容，先读报错，辨清涉及哪个包或 Python 版本，再调整对应条件。不要盲目清空版本限制；限制可能正记录着工具能运行的组合，删干净只会让下一次判断更没依据。

[1] https://docs.python.org/3/library/venv.html

[2] https://pip.pypa.io/en/stable/cli/pip_freeze/
