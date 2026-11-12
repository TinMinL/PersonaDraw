你这个自用小工具，用 Python 自带的 `venv` 加 `pip` 就够了。本龙会把依赖单独圈在项目里：以后别的小工具升级库，不至于顺手把它撞坏。下面按 Windows PowerShell 写，只给操作说明，没有改动你的项目。

**先建环境，再安装依赖。** 打开项目目录的终端，先确认 Python 能运行：

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

最后一行应指向当前项目的 `.venv\Scripts\python.exe`。本龙更看重这个路径，提示符多出一个 `(.venv)` 只是辅助线索。若 `python` 不可用但 `py --version` 正常，把前两条里的 `python` 换成 `py`；激活后仍用 `python`。虚拟环境沿用创建它的 Python 版本，不会自行替你挑版本。genui{"citation":{"ref":"turn51view0"}}

假设工具需要 `requests`，这样安装、查看并运行；包名和入口文件换成你的实际名称：

```powershell
python -m pip install requests
python -m pip list
python main.py
```

我让你写 `python -m pip`，是为了让安装器跟着当前解释器走。机器上 Python 一多，单独一个 `pip` 很容易让人查错地方。（包装好了，程序却说没有，通常就从这里查。）标准库如 `json`、`pathlib` 不需要另外安装。安装完成后，先实际跑通工具，再记录依赖。genui{"citation":{"ref":"turn51view0"}}

**把能运行的依赖记下来。** 在已激活的环境里执行：

```powershell
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
python --version
```

这里显式写 UTF-8，省得不同 PowerShell 版本的默认编码添乱。把第二条输出记进 README，再写上启动命令。`freeze` 会记录已安装的包，通常包括间接依赖和具体版本；它不会扫描代码，只留下“真正用到”的库。所以这个环境尽量只装本项目需要的东西，别把试验用包全塞进去。它也不是完整锁文件，不能保证换系统、换 Python 版本后原样成功。genui{"citation":{"ref":"turn51search2"}}

**GitHub 留源码和清单，`.venv` 在本机重建。** 在项目根目录的 `.gitignore` 中加入：

```gitignore
.venv/
__pycache__/
*.pyc
```

把源码、`requirements.txt`、README 和 `.gitignore` 一起提交。`.venv` 含解释器相关文件、安装包和指向本机位置的路径；搬到另一台电脑或改个目录，都可能失效。Python 官方明确把它视为可丢弃、应重建且不应纳入 Git 的目录。本龙要保住的是重建办法，整箱搬走也不等于能用；你的源码当然也别放进 `.venv`。genui{"citation":{"ref":"turn51search0"}}

换电脑时，先安装 README 记录的 Python 版本，尽量保持相同主次版本和架构；下载或克隆项目后，进入项目目录：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

安装成功后还要跑一次实际功能；配置、密钥、数据和外部程序不在这张包清单里，得另外准备。依赖有变化时，跑通后重新导出清单。genui{"citation":{"ref":"turn51search4"}}

**碰到问题，先对症查。**

- PowerShell 禁止运行激活脚本？先不用改执行策略，直接指定解释器：` .\.venv\Scripts\python.exe -m pip install -r requirements.txt`，运行时同样用它接 `main.py`。激活只是方便，并非必需。genui{"citation":{"ref":"turn50search7"}}
- 安装过却提示缺模块？再查 `sys.executable`，编辑器也选项目里的解释器。别急着重复安装，本龙先确认它们是不是同一套环境。
- 新电脑提示没有匹配版本？先对照 Python 版本、系统架构和报错包的支持范围，别一上来删掉所有版本号。
- 新开终端需要重新激活；结束后输入 `deactivate` 即可。它只退出当前终端的环境，不会删除依赖。genui{"citation":{"ref":"turn51view0"}}
