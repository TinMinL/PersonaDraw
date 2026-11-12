你这个自用小工具，用 **`venv`＋`pip`＋`requirements.txt`** 就够。本龙先替你压住配置欲：每个项目一个环境，把能恢复的步骤记下来，比把整台电脑搬上 GitHub 实在。下面以 **PowerShell** 为主，命令供你操作，我没有改动项目。

**1．先建立环境，再安装依赖**

打开项目目录的终端，把示例路径换成自己的：

```powershell
cd "C:\Projects\mytool"
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

最后一行应指向当前项目的 `.venv\Scripts\python.exe`。先认准这条路径；提示符多个括号很热闹，却不如解释器位置可靠。虚拟环境默认隔离其他环境的第三方包，源码仍放项目目录，别塞进 `.venv`。genui{"citation":{"ref":"turn55view0"}}

若用的是 CMD，激活命令换成：

```bat
.venv\Scripts\activate.bat
```

**2．只装工具实际需要的包**

假设程序需要 `requests`，在已激活的终端执行：

```powershell
python -m pip install requests
python -m pip show requests
python main.py
```

把包名、入口文件换成实际名称。这里本龙坚持写 `python -m pip`，让安装器跟着当前解释器走，免得包装在甲处、程序跑在乙处。`json`、`pathlib` 这些标准库无需安装；只有第三方依赖才交给 pip。官方教程也采用这种安装方式。genui{"citation":{"ref":"turn55search0"}}

**3．跑通以后，记录依赖**

```powershell
python -m pip freeze | Set-Content -Encoding utf8 requirements.txt
python --version
```

第一条是 PowerShell 写法，明确使用 UTF-8；第二条的结果另记进 README，再写上启动命令。`freeze` 记录环境中已安装的包及版本，也包括间接依赖，所以别在这个环境里顺手试装一堆无关工具。（它会记账，但不会替你判断哪些购物是冲动消费。）依赖增删或升级后，确认程序可用，再更新清单。genui{"citation":{"refs":["turn55search1","turn55search5"]}}

**4．换电脑时，重建环境**

先安装与原机相同大、小版本的 Python，尽量保持系统与架构一致；下载或克隆源码，在项目目录执行：

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

先核对版本再创建，别让新电脑默认选中的 Python 偷偷替你做决定。恢复还需要程序用到的数据、配置和外部软件；清单不负责这些。`freeze` 也不是完整锁文件，换平台或 Python 版本仍可能遇到兼容问题，恢复后必须实际运行。genui{"citation":{"refs":["turn55search0","turn55view1"]}}

**5．为什么不上传 `.venv`**

它含解释器、安装包和与本机有关的路径，通常不能直接搬到另一台电脑；官方明确把它视为可删除重建、无需提交 Git 的目录。本龙要你保存的是源码和重建依据，上传一大堆本机文件，并不会自动获得可移植性。genui{"citation":{"ref":"turn55view0"}}

在项目根目录的 `.gitignore` 中加入：

```gitignore
.venv/
__pycache__/
*.pyc
```

提交源码、`requirements.txt`、README 和 `.gitignore`。如果 `.venv` 已经被 Git 跟踪，单加忽略规则不够，还要取消跟踪；先别以为写进去就算清干净了。

**常见卡点，按症状查**

- **找不到 `py`**：试 `python --version`；能用就以 `python -m venv .venv` 创建。两者都不行，先检查 Python 安装与命令路径，重开终端再试。
- **PowerShell 禁止激活脚本**：不用急着改执行策略。直接执行 `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`，运行也用这个解释器；激活并非必需。genui{"citation":{"ref":"turn54search2"}}
- **装了仍报找不到模块**：重查 `sys.executable`，编辑器也选择项目的 `.venv` 解释器。先把安装和运行对齐，重装十遍并不能修正跑错地方。
- **新终端又失效**：重新激活即可；结束时输入 `deactivate`，这只退出环境，不会删除依赖。
