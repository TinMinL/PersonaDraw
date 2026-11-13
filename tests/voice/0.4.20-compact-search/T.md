自己用的小工具，先用 **`venv`＋`pip`＋`requirements.txt`** 就够了。本龙先替你省掉一套工具选型：你要解决的是下次还能跑，不是把安装步骤发展成第二个项目。下面以 Windows 的 **命令提示符（cmd）** 为主；命令请在终端输入，别放进 Python 的 `>>>`。

先进入存放代码的目录，把示例路径换成自己的：

```bat
cd /d D:\projects\mytool
python --version
python -m venv .venv
.venv\Scripts\activate.bat
python -c "import sys; print(sys.executable)"
```

最后一行应指向项目下的 `.venv\Scripts\python.exe`。我更看重这个路径，提示符多了个 `(.venv)` 只是辅助证据。`venv` 使用创建它的 Python 版本，默认隔离其他环境的第三方包；代码放在项目目录，别塞进 `.venv`，以后重建时还得抢救自己的源码。genui{"citation":{"ref":"turn7view0"}}

接着安装工具真正用到的包。假设代码需要 `requests`：

```bat
python -m pip install requests
python -m pip show requests
python main.py
```

把 `requests` 和 `main.py` 换成实际包名、入口文件名。标准库如 `json`、`pathlib` 无需另装。我这里坚持写 `python -m pip`，是为了让安装器跟着当前 Python 走，免得包装完了，程序却站在另一个环境里喊找不到。`show` 输出里的 `Location` 也应落在这个项目的 `.venv` 中。genui{"citation":{"ref":"turn7view1"}}

确认工具正常运行后，在同一个已激活的 cmd 窗口记录依赖：

```bat
python -m pip freeze > requirements.txt
python --version
```

把第二条输出的 Python 版本写进 README，再注明运行命令。`freeze` 会记录环境里已安装的包及版本，包括间接依赖；它不读你的源码，也不会替你挑出哪些包真的用到了。因此本龙让你从干净环境开始，免得试装过的东西一起搭便车。以后增删、升级依赖并验证成功后，再更新这份清单。它是安装快照，不是完整锁文件，更不会打包 Python 本身。genui{"citation":{"ref":"turn7view2"}}

换电脑时，先安装与记录一致的 Python 版本，取回代码和 `requirements.txt`，进入项目目录，再运行：

```bat
python --version
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python main.py
```

先核对版本，再创建环境；别把旧 `.venv` 复制过来碰运气。安装完成后，实际跑一次常用功能，才能确认恢复成功。依赖清单不会替你恢复数据文件、配置或外部程序，这些若有，也要另行备份和记录。跨 Python 版本或系统恢复可能遇到兼容问题，版本号相同并不等于所有运行条件都相同。genui{"citation":{"refs":["turn7view0","turn7view1"]}}

至于 GitHub，上传代码、README 和依赖清单，在项目根目录的 `.gitignore` 加一行：

```gitignore
.venv/
```

官方明确把虚拟环境视为可删除重建、不要纳入 Git 的目录。它包含解释器、安装包及指向本机位置的路径，通常不能直接搬家。把整箱本机零件传上去，不会自动变成便携版。（这点本龙可不替复制粘贴担保。）genui{"citation":{"ref":"turn7view0"}}

遇到问题，先查这几处：

- **`python` 找不到**：若 `py --version` 可用，创建环境时改用 `py -m venv .venv`；否则先检查 Python 安装及终端命令配置，重开终端再试。
- **用的是 PowerShell**：激活命令换成 `.\.venv\Scripts\Activate.ps1`。如果脚本被执行策略拦住，我会直接用下面的路径调用，省得为了激活先改策略。

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

- **安装后仍找不到模块**：再查 `sys.executable`；编辑器的解释器也要选这个 `.venv`。包名与导入名还可能不同，别见到 `import` 就原样拿去安装。
- **关闭终端后“失效”**：环境还在，新终端需要重新激活；退出用 `deactivate`。激活只是调整当前终端的查找路径，并非使用环境的必要条件。genui{"citation":{"ref":"turn7view0"}}
