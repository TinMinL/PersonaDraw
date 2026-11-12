你这类自用小工具，用 Python 自带的 `venv` 加 `pip` 就够了。本龙先把流程压实：每个项目建自己的环境，依赖装进去，把清单留给未来的自己。只有自己用，也挡不住半年后忘记装过什么。

下面按 **Windows PowerShell** 写，假设入口是 `main.py`；路径、入口和示例包名请换成你的实际值。

**1．先建环境，再装依赖**

在项目目录运行：

```powershell
cd C:\work\mytool
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

最后一行应指向当前项目的 `.venv\Scripts\python.exe`。本龙更认这个路径，提示符多了个 `(.venv)` 只能算辅助证据。虚拟环境默认隔离其他环境的第三方包，创建时也会安装 pip；你的源码放项目目录，别塞进 `.venv`。genui{"citation":{"ref":"turn46search1"}}

接着装工具真正用到的包，例如：

```powershell
python -m pip install requests
python main.py
```

我这里坚持写 `python -m pip`，让安装依赖的 pip 跟着当前 Python 走。电脑里装了几份 Python 时，裸写 `pip` 很容易各忙各的。`requests` 只是示例；`json`、`pathlib` 这类标准库不必另装。官方安装说明也使用这种模块调用方式。genui{"citation":{"ref":"turn46search7"}}

**2．跑通之后，记录依赖**

先确认当前环境干净、程序能跑，再导出：

```powershell
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
```

这会记录已安装包及版本，连带依赖也会列入；以后增删或升级包，测试通过后再更新它。PowerShell 这里显式写 UTF-8，省得旧版本重定向的编码来添乱。官方教程支持把这份清单纳入版本控制，并用 `install -r` 恢复。genui{"citation":{"ref":"turn46search2"}}

另外在 README 记下 `python --version` 的结果和启动命令。我可不把依赖清单当整台电脑的复印件：Python 本身、外部程序、配置和数据，都得另记、另备份。（密码别顺手记进公开仓库。）

**3．换电脑时重建**

新电脑先装与原来相同主次版本、尽量同补丁版本及架构的 Python，取得源码和 `requirements.txt`，进入项目目录后运行：

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

本龙要你最后实际跑一次工具：安装成功只说明包进去了，文件路径、配置缺失仍可能让程序停住。版本清单能提高恢复的一致性，却不能保证不同操作系统或 Python 版本都兼容。

**4．为什么不上传 `.venv`**

它包含环境路径、解释器相关文件和已安装包；环境中的脚本可能绑定绝对路径，因此通常不能靠复制搬家。官方明确把它视作可删除重建、不应纳入 Git 的目录。上传一大堆文件，换机器仍得重建，这份勤快实在不划算。genui{"citation":{"ref":"turn46search0"}}

在项目根目录的 `.gitignore` 加入：

```gitignore
.venv/
__pycache__/
*.pyc
```

提交源码、`requirements.txt` 和说明即可。若 `.venv` 已被 Git 跟踪，新增忽略规则不会自动撤回；可用 `git rm -r --cached .venv` 取消跟踪，再提交变更，本地文件会保留。

**常见卡点**

- **找不到 `python`**：先试 `py --version`；可用时以 `py -m venv .venv` 创建。两者都找不到，先检查 Python 安装与 PATH，别急着重装依赖。
- **禁止运行激活脚本**：无需先改执行策略，直接用 `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`，运行程序也用这个解释器路径。激活只是方便切换 PATH，并非必须。genui{"citation":{"ref":"turn46search1"}}
- **安装了仍报缺包**：再查 `sys.executable`，编辑器也选 `.venv\Scripts\python.exe`。先查是不是同一份 Python，这比反复安装有用。
- **退出与重新打开**：输入 `deactivate` 退出；新开终端后重新激活即可，不用重建环境。
