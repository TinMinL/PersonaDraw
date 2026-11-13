只有自己用，本小姐会给你挑最省心的一套：**每个项目一个 `.venv`，用 pip 装包，用 `requirements.txt` 记下依赖**。无需先摆出一整套发布工程，先让今天能跑的小工具，换台电脑也有章可循，desuwa。以下按 Windows PowerShell 写；项目目录和 `main.py` 请换成你的实际名称。

先打开终端，进入放着代码的目录，确认 Python 能运行，再建立环境：

```powershell
cd C:\work\mytool
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

最后一行应指向本项目的 `.venv\Scripts\python.exe`。我更看重这个路径，提示符里的 `(.venv)` 可以当辅助。`venv` 会使用创建它的那份 Python，并默认隔离其他环境的第三方包；你的代码仍放在项目目录，别塞进 `.venv`。如此以后别的工具升级依赖，也不至于顺手搅乱这里。genui{"citation":{"ref":"turn6view0"}}

环境就位后，再请项目真正需要的包进来。以 `requests` 为例，你不需要它就换成自己的依赖；`os`、`json` 这类标准库不必安装。

```powershell
python -m pip install requests
python -m pip list
python main.py
```

我这里特意写 `python -m pip`：让当前 Python 来调用 pip，解释器和安装目标才好对上。若需要指定版本，使用 `包名==版本号`；平时不要为了“保持最新”随手升级全部依赖，先让自己的工具稳定运行，更合本小姐的心意。安装与版本指定方法见 Python 官方教程。genui{"citation":{"ref":"turn6view1"}}

确认程序正常后，记录依赖。下面用 UTF-8 写文件，兼顾 Windows PowerShell 的编码差异：

```powershell
python -m pip freeze | Set-Content -Encoding utf8 requirements.txt
python --version
```

把第二行显示的 Python 版本另记进 README，也记下启动命令。`freeze` 会记录当前安装的包，包含间接依赖，并不是分析你的源码来挑必需品。因此这个环境只服务这一个项目，清单才不夹带别的工具。新增或升级依赖、试跑成功后，再重新导出。（收拾名单这一步，可别留给换电脑那天。）它也不是严格的锁文件，不能保证任意系统、任意 Python 版本都能重现。genui{"citation":{"ref":"turn6view2"}}

至于 GitHub，请提交源码、README、`requirements.txt`，并在项目根目录的 `.gitignore` 加一行：

```gitignore
.venv/
```

`.venv` 里装的是可重建的解释器和依赖，既有重复文件，也可能包含机器上的绝对路径。官方明确把它视为不该进入版本控制、通常不可搬运的目录；直接复制过去，路径或平台一变就可能失效。保留重建办法才体面，desuwa。若已经跟踪过它，仅加忽略规则不会取消跟踪，需要另行处理 Git 索引。genui{"citation":{"ref":"turn6view0"}}

换电脑时，先安装尽量相同版本、相同架构的 Python，下载或克隆项目，进入目录后重新建立：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

恢复依赖后还要实际运行工具，尤其留意配置文件、数据和系统外部软件；这些不会凭 `freeze` 自动搬家。官方教程给出的恢复方式就是按清单安装。genui{"citation":{"ref":"turn6view1"}}

最后几处常见小绊脚石，我替你提前点出来：

- **找不到 `python`**：先确认已安装 Python；若 `py --version` 可用，可用 `py -m venv .venv` 创建。
- **PowerShell 禁止激活脚本**：不必急着改系统设置。直接用下面两行，照样能安装和运行；激活本来就不是必需步骤。genui{"citation":{"ref":"turn6view0"}}

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

- **装了包却报 `ModuleNotFoundError`**：先查前面的解释器路径，编辑器也要选本项目那份 Python，别急着重复安装。
- **关掉终端再打开**：需要重新激活；用完输入 `deactivate` 即可退出，不会删除环境。若你用 CMD，激活命令则是 `.venv\Scripts\activate.bat`。genui{"citation":{"ref":"turn6view0"}}
