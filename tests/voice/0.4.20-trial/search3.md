你这个自用小工具，先用 Python 自带的 `venv` 加 `pip` 就够了。本龙会把力气留给工具本身，暂时不替它置办一整套发布流水线。下面按 **Windows PowerShell** 写，路径、包名和入口文件换成你的；这里只给操作说明，不改项目。

**先建立环境，再安装依赖。** 在项目目录打开终端：

```powershell
cd C:\projects\mytool
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

最后应输出项目下 `.venv\Scripts\python.exe` 的完整路径。先认准这一条，别只看提示符多了个括号就放心。虚拟环境让这个项目的第三方包独立存放，免得另一个小脚本升级依赖，顺手把它弄坏。若 `python` 无法识别，先确认已安装 Python；有 `py` 命令时，也可用 `py -m venv .venv` 创建。激活后继续用 `python`。genui{"citation":{"ref":"turn49view1"}}

假设工具需要 `requests`：

```powershell
python -m pip install requests
python -m pip show requests
python main.py
```

包名只是示例，按实际需要安装；`json`、`pathlib` 这类标准库不用装。本龙这里坚持写 `python -m pip`，是为了让安装器跟着当前解释器走。电脑上有几份 Python 并不稀奇，装得很成功、运行时却找不到包，也就跟着不稀奇了。装完跑一次实际功能，才知道工具是否正常。genui{"citation":{"ref":"turn48view0"}}

**能跑之后，记录依赖。** 在这个已激活的环境里执行：

```powershell
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
python --version
```

第一行会覆盖依赖清单，显式用 UTF-8，省去不同 PowerShell 版本默认编码的麻烦。把第二行显示的 Python 版本记进 README，连同运行命令保存。每次增删或升级依赖，确认程序还能跑，再更新清单。

注意，`freeze` 记录的是环境里已经安装的包，包括间接依赖；它不会读懂你的代码，也不生成严格的锁文件。因此别在一个塞满杂包的公共环境里导出，否则只是把杂物清单写得很整齐。它也不记录 Python 本身；我会把版本另外记下来，避免换电脑时靠回忆。genui{"citation":{"ref":"turn49view0"}}

**GitHub 保存重建材料，别上传 `.venv`。** 在项目根目录的 `.gitignore` 加上：

```gitignore
.venv/
__pycache__/
*.pyc
```

提交源码、`requirements.txt`、README 和 `.gitignore`。Python 官方明确把虚拟环境视为可删除重建、不应纳入版本控制的目录；里面的配置及脚本会关联本机路径，整体搬过去不保证能用。文件多只是附带麻烦，真正的问题是它并非便携安装包。源码也别放进去，免得重建环境时一起丢掉。genui{"citation":{"ref":"turn48view1"}}

**换电脑时重新建。** 先装好记录的 Python 版本，取得源码和依赖清单，在项目目录执行：

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

先核对版本，再安装；不要把恢复和升级同时做，本龙不想让你排错时还得猜是哪一步变了。依赖清单也不是整机备份：工具需要的数据、配置和外部程序要另行准备。genui{"citation":{"ref":"turn48view0"}}

**几个常见卡点，按症状处理。**

- PowerShell 禁止执行激活脚本：可以直接跳过激活，使用下面两条命令；不必为了跑个工具先修改执行策略。
- 提示 `ModuleNotFoundError`：再查 `sys.executable`，编辑器也要选同一份 `.venv\Scripts\python.exe`，别给错误的解释器反复装包。
- 新终端没有环境：激活只影响当前终端，重新激活即可；结束时输入 `deactivate`。

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

直接指定解释器是官方支持的用法，激活只是省掉路径。若使用 CMD，激活命令改为 `.venv\Scripts\activate.bat`；两种终端的脚本别混着用。genui{"citation":{"ref":"turn48view1"}}
