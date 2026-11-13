## 建立环境

先把项目目录准备好，再在 CMD 中依次输入下面的命令。本小姐先替你把边界划清：`main.py` 放在项目根目录，别塞进 `.venv`；环境日后可以重建，源码可不能跟着丢。[1]

```bat
cd /d C:\work\mytool
python --version
python -m venv .venv
.venv\Scripts\activate.bat
python -c "import sys; print(sys.executable)"
```

看到版本号后再创建；最后的路径应指向 `C:\work\mytool\.venv\Scripts\python.exe`。这一步确认的是正在用谁，单看提示符还不够呢。虚拟环境默认隔离第三方包，并基于创建它的 Python；确认路径正确，才轮到安装依赖。

## 安装依赖

请在刚确认过的终端中安装并运行：

```bat
python -m pip install requests
python main.py
```

我偏爱这种写法，因为安装器跟着当前解释器走，少一层装错位置的疑虑。标准库已经随 Python 提供，不需要额外安装；第三方包才按工具需要补。安装结束还不能宣布成功，入口实际跑通、功能结果符合预期，才算这一步过关，desuwa。

如果你不想激活，也可以直接指定环境解释器；我把完整写法放在这里，两种方式选一种便好。[1]

```bat
.venv\Scripts\python.exe -m pip install requests
.venv\Scripts\python.exe main.py
```

## 记录依赖

确认工具能运行后，再在项目根目录导出：

```bat
python -m pip freeze > requirements.txt
```

请先确认仍在目标环境中，而且旧文件里的内容允许被覆盖。`freeze` 记录已安装包，包含环境中已有的其他包；它不会阅读源码替你挑出真正用到的依赖，也不是完整锁文件。[2] 所以本小姐会先看看清单有没有无关包，再把它交给下一台电脑。（整洁环境在这里便显出好处了。）

默认清单会省略部分引导工具，Python 3.12 起默认省略 `pip`；确实要连这些也记录时才加 `--all`。[2] 另在 README 写下 Python 版本、入口、数据配置及外部程序，因为包清单不会替你记住这些运行条件。

## 换电脑

先带走源码、依赖清单、README 和所需数据配置，再核对新机 Python 主次版本与架构。我会先把这些条件对齐，免得装包时才发现差异。把项目放到示例目录后，在新机 CMD 中操作：

```bat
cd /d C:\work\mytool
python --version
python -m venv .venv
.venv\Scripts\activate.bat
python -c "import sys; print(sys.executable)"
python -m pip install -r requirements.txt
python main.py
```

路径核对正确再恢复依赖；最后还要按 README 补齐运行条件并检查实际功能。安装成功只能说明包安装了，不能保证跨平台完全复现。这份验收，本小姐可不会替尚未运行的程序提前签字。

## Git

在项目根目录的 `.gitignore` 写入：

```gitignore
.venv/
```

源码、依赖清单和 README 才是重建的依据。环境含有依赖本机位置的内容，脚本可能写入绝对路径，直接搬走未必能用，因此不宜上传 Git 或作为可搬运目录。[1] 让新机器重新建立，反而省心些。

还请留意：如果 `.venv` 已被 Git 跟踪，新增忽略规则不会取消跟踪。接下来要判断它是否已经进入版本记录，不能看到忽略文件便以为问题解决了。

## 排错

找不到 `python` 时，先检查命令是否可用；如果 `py` 可用，可以用下面的命令创建，再激活并核对路径：

```bat
py -m venv .venv
```

安装后仍缺包，我会先让你比较终端和编辑器使用的解释器，两边都应指向项目环境，再确认包安装到了那里，别急着反复安装。

新开 CMD 后需要重新激活，因为激活只改变当前终端的查找路径；也可沿用直接指定解释器的方式。[1] 遇到版本不兼容，请先读报错指出的是哪个包、哪项版本要求，再检查环境与清单。不要盲目清空版本限制；先查清冲突，改动才有依据，desuwa。

[1] https://docs.python.org/3/library/venv.html

[2] https://pip.pypa.io/en/stable/cli/pip_freeze/
