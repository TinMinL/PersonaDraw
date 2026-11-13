你这个规模，用 Python 自带的 `venv` 加 `pip` 就够了。本龙先替你省掉一套工具链：只有自己用，也值得隔离依赖，免得另一个脚本升级包，顺手把这个小工具送走。

我查了 Python 官方教程、`venv` 文档及 PyPA 文档。下面以 **PowerShell、项目根目录** 为准，只给操作说明，没有改动你的项目。

**先建立环境。** 假设项目放在 `C:\work\mytool`，把路径换成你的：

```powershell
cd C:\work\mytool
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip --version
```

`venv` 使用执行创建命令的那个 Python；`.venv` 放解释器及第三方包，自己的 `.py` 文件放在它外面。最后一条输出中的路径应包含当前项目的 `.venv`。若你习惯用 CMD，激活命令换成 `.venv\Scripts\activate.bat`。genui{"citation":{"ref":"turn8view0"}}

**接着装依赖，再运行。** 以下假设需要 `requests`，入口叫 `main.py`；按实际名称替换，没用到的包别顺手装进去。

```powershell
python -m pip install requests
python main.py
```

我建议一直写 `python -m pip`：让当前 Python 调用自己的 pip，省得两个解释器各干各的，还都声称安装成功。安装时会一并处理该包的依赖。新开终端后，需要重新激活已有环境，无须重新创建；结束时运行 `deactivate` 即可。genui{"citation":{"ref":"turn9view0"}}

**确认工具能跑后，记录依赖。** 在已激活的环境中执行：

```powershell
python -m pip freeze > requirements.txt
python --version
```

第一条把已安装包及其版本写进文件，包含间接依赖；第二条的版本号手动记进 README，并写清启动命令。以后增删、升级依赖，验证运行正常后再导出，注意它会覆盖旧文件。Python 官方教程支持将这个依赖文件提交到版本控制。genui{"citation":{"ref":"turn8view1"}}

这里我得挑一句：`freeze` 不会读你的代码、替你筛掉闲置包，也不是完整锁文件。所以专用环境越干净，清单越可信；它也不记录 Python 本身。看到本机路径或本地包条目，要另行安排来源，别指望新电脑认识旧电脑的盘符。genui{"citation":{"ref":"turn8view2"}}

**换电脑时，重新搭环境。** 先安装相同 Python 主、次版本，尽量保持系统及架构一致；拿到源码和 `requirements.txt` 后，在项目目录执行：

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

安装需要可访问依赖来源。版本清单能减少漂移，不能保证跨系统、跨 Python 版本无条件复现；恢复后仍要实际运行工具。先让原来的组合跑通，再考虑升级，我不建议把搬家和装修安排在同一天。genui{"citation":{"refs":["turn8view1","turn8view2"]}}

**GitHub 保存重建材料。** 提交源码、README、`requirements.txt` 和 `.gitignore`，在项目根目录的 `.gitignore` 中加入：

```gitignore
.venv/
```

`.venv` 不是可搬走的独立安装包：它关联本机 Python，部分脚本含绝对路径，换位置可能失效。官方明确把它视为可丢弃、可重建、不应纳入 Git 的目录。（整个搬上去，看着齐全，实际上连旧地址也打包了。）genui{"citation":{"ref":"turn8view0"}}

**遇到问题，先查这三项：**

- **PowerShell 禁止运行激活脚本：** 无须急着改策略，直接用 ` .\.venv\Scripts\python.exe -m pip install -r requirements.txt` 安装，再用 `.\.venv\Scripts\python.exe main.py` 运行；激活不是必需步骤。genui{"citation":{"ref":"turn8view0"}}
- **装了包仍提示找不到：** 检查 `python -m pip --version` 的路径；编辑器也要选当前 `.venv` 的解释器。先核对环境，再重复安装，省得给错误的位置继续添库存。
- **找不到 `python`：** 若 `py --version` 可用，创建环境时改用 `py -m venv .venv`；否则先安装并确认 Python 命令可用，再继续。genui{"citation":{"ref":"turn9view0"}}

还有两处容易混淆，我给你拎出来。虚拟环境解决的是“这个项目用哪些包”，不会替你保存输入文件、配置或业务数据；搬电脑时，这些材料也要按实际用途带走。源码目录和依赖目录分开，才方便判断哪些东西丢了能重建，哪些东西必须备份。

如果你的工具只用 `pathlib`、`json` 这类标准库，就不必为了填满清单安装第三方包；空的依赖文件也不丢人。真正该记的是 Python 版本、入口和运行所需文件。本龙看重能复原，不看重目录里住了多少包。

若安装失败，先保留完整报错，核对包名、要求的版本和 Python 版本。别一上来删除版本限制：那可能只是把“装不上”换成“装上了却不能跑”。每次有意升级后，跑一次你常用的输入，再更新清单，留住上次可用的记录。
