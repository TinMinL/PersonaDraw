你这个规模，Python 自带的 `venv` 加 `pip` 就够了，本龙先把工具链的膨胀欲按住。只有自己用也值得隔离依赖：以后另一个脚本升级某个包，不必顺便把这个工具弄坏。下面按 Windows PowerShell 来，命令由你执行，我没有改动项目。

**先在项目目录建立环境。** 假设代码放在 `C:\work\mytool`，入口叫 `main.py`，请替换成实际路径和文件名：

```powershell
cd C:\work\mytool
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

最后应显示项目内 `.venv\Scripts\python.exe`。`venv` 使用运行它的那个 Python 版本，默认隔离全局第三方包；激活只是让当前终端优先找到环境里的 Python。新开终端要重新激活，退出用 `deactivate`。代码放项目目录，别塞进 `.venv`，那是可以重建的耗材区。[官方说明](https://docs.python.org/3/library/venv.html)

**再安装实际需要的包。** 以 `requests` 为例，不需要它就换成你的依赖；`json`、`pathlib` 等标准库不用安装。

```powershell
python -m pip install requests
python main.py
```

我建议一直写 `python -m pip`，明确让当前解释器负责安装。电脑里 Python 多了，单独一个 `pip` 很容易把包装给隔壁。（安装成功，运行却找不到，往往就是这出。）

工具跑通后，记录环境里的依赖：

```powershell
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
python --version
```

把显示的 Python 版本记进 README，也写明启动命令。这里用显式 UTF-8 输出，避开旧版 Windows PowerShell 重定向的编码差异。`freeze` 会记录已安装包及版本，通常也包含间接依赖；以后增删或升级包、确认运行正常后，再更新文件。[官方教程](https://docs.python.org/3/tutorial/venv.html)

注意，它不是读你的源码来猜依赖，也不保证跨平台完全复现。别在这个环境顺手试装十几个无关包，再指望它替你辨认真爱。`freeze` 是安装状态清单，不是完整锁文件。[pip 官方说明](https://pip.pypa.io/en/stable/cli/pip_freeze/)

**换电脑时，拿清单重建。** 先安装相同 Python 主次版本，尽量保持相同架构；下载或克隆项目，进入目录后执行：

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

若装了多个 Python，可用对应版本创建，例如原来是 3.13，就用 `py -3.13 -m venv .venv`。恢复后实际运行一次；依赖清单不包含你的数据、私密配置或外部程序，这些需要另行迁移。

**GitHub 保存源码和配方，不搬整个环境。** 将源码、README、`requirements.txt` 和 `.gitignore` 提交；在项目根目录的 `.gitignore` 加上：

```gitignore
.venv/
__pycache__/
```

官方明确说虚拟环境不应纳入 Git，也不应直接复制搬家。它包含机器相关路径，已安装脚本可能引用解释器的绝对路径，还可能有平台相关二进制包；上传一大堆文件并不能让它变得便携。本龙宁可保留能重建的步骤，也不收藏一箱换电脑就认生的零件。[官方依据](https://docs.python.org/3/library/venv.html)

**卡住时先查这几项：**

- `py` 找不到：若 `python --version` 正常，创建时改用 `python -m venv .venv`；两者都不行，先检查 Python 安装。
- PowerShell 禁止激活：不必急着改执行策略，直接调用环境解释器即可，下面两条都无需激活。

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

- CMD 的激活命令是 `.venv\Scripts\activate.bat`，别混用终端语法。
- 安装后仍提示缺包：检查 `sys.executable`，编辑器也应选择 `.venv\Scripts\python.exe`。
- 恢复时报版本不兼容：先核对 Python 版本和架构，再看具体包的报错；别直接删掉所有版本号碰运气。
