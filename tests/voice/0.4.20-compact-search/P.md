你这个规模，用 Python 自带的 `venv` 加 `pip` 就够。本龙先把工具箱收小一点：只有自己用，也值得隔离依赖，免得另一个脚本升级包，你的小工具跟着罢工。下面按 Windows **命令提示符（cmd）**讲，路径和包名换成你的；这里只给步骤，没有改动项目。genui{"citation":{"ref":"turn0view1"}}

**先建环境，再装东西。** 打开 cmd，进入存放代码的目录：

```bat
cd /d D:\projects\mytool
python --version
python -m venv .venv
.venv\Scripts\activate.bat
python -c "import sys; print(sys.executable)"
```

最后应输出项目内的 `.venv\Scripts\python.exe`。先看这条路径，别只被提示符里的 `(.venv)` 哄住。环境使用创建它的 Python 版本；代码放项目目录，别塞进 `.venv`。以后重新开终端，只需进入目录、激活，不必重新创建。genui{"citation":{"refs":["turn0view0","turn1search0"]}}

**安装依赖时，让解释器认领自己的 pip。** 假设工具用到 `requests`：

```bat
python -m pip install requests
python -m pip --version
python main.py
```

把 `requests` 换成实际需要的包，把 `main.py` 换成入口文件；标准库不用安装。我这里坚持写 `python -m pip`，是为了明确用当前 Python 的 pip，少给“装了却找不到”留下机会。检查 pip 输出路径也在 `.venv` 下，再运行工具确认正常。（装成功和程序能用，还是两件事。）genui{"citation":{"ref":"turn1search1"}}

**能跑以后，记录依赖。** 在刚才激活的 cmd 中执行：

```bat
python -m pip freeze > requirements.txt
python --version
```

第一条会覆盖文件，记录当前环境的包及版本，通常包括间接依赖。它不会替你扫描代码、挑出真正用到的包，所以别往这个环境里随手堆实验用品。以后增删或升级依赖，确认工具仍能运行，再重新导出。genui{"citation":{"ref":"turn0view2"}}

把第二条的版本结果记在 README，顺手写上启动命令。`freeze` 不记录 Python 本身，也不是完整锁文件；跨 Python 版本或操作系统恢复，并不保证照单全成。本龙宁可现在多记一行，也不想搬电脑时靠回忆破案。genui{"citation":{"ref":"turn0view2"}}

**换电脑时重建。** 先安装与旧机相同大、小版本的 Python，尽量保持同为 Windows、同一架构；拿到代码和 `requirements.txt`，进入项目目录：

```bat
python --version
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python main.py
```

先对照版本，再安装，最后实际跑一次。依赖清单负责重新安装包，你的数据、配置和系统外部程序仍要另行准备；清单没承诺替整台电脑搬家。genui{"citation":{"refs":["turn0view1","turn0view2"]}}

**GitHub 里保留重建材料。** 提交代码、README、`requirements.txt`，在项目根目录的 `.gitignore` 加一行：

```gitignore
.venv/
```

`.venv` 含解释器、第三方包及关联本机路径的文件，本来就不适合作为可搬运目录。官方明确把它视为可删除重建、不要纳入 Git 的内容。上传一大箱本机环境，也换不来可靠恢复。genui{"citation":{"ref":"turn0view0"}}

**卡住时，先查这几处：**

- `python` 找不到：先试 `py --version`；能用就以 `py -m venv .venv` 创建，再激活。两者都不可用，先安装或修复 Python。
- PowerShell 激活：用 `.\.venv\Scripts\Activate.ps1`。若被脚本策略拦住，本龙建议先省掉激活，直接运行 `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`；运行脚本也用这个解释器即可，激活并非必需。genui{"citation":{"ref":"turn0view0"}}
- `ModuleNotFoundError`：检查上面的解释器路径；编辑器也要选择该项目的解释器，别让终端和编辑器各过各的。
- 用完输入 `deactivate` 退出环境；这不会删除依赖，下次激活还能继续。genui{"citation":{"ref":"turn1search0"}}
