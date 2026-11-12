你这个规模，用 **内置 `venv`＋`pip`＋`requirements.txt`** 就够了。本龙会把力气花在“换电脑还能跑”上，先不替一个自用工具配齐整套工程仪仗队。下面以 **PowerShell** 为主，命令在项目根目录执行；路径、依赖名和入口文件按实际替换。

**1．先建环境，再往里面装东西**

确认已经安装 Python，进入项目目录：

```powershell
cd C:\Projects\mytool
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

最后一条应指向项目里的 `.venv\Scripts\python.exe`。先看这个，本龙不只认提示符前多出的括号。虚拟环境默认隔离各项目的第三方包，能避免你给另一个工具升级依赖，顺手把这个工具拆了。若使用 CMD，激活命令换成 `.venv\Scripts\activate.bat`。genui{"citation":{"ref":"turn47view0"}}

**2．安装依赖，并试跑工具**

假设工具需要 `requests`，入口是 `main.py`：

```powershell
python -m pip install requests
python main.py
```

把 `requests` 换成你真正需要的包；只有标准库就不用装。这里坚持写 `python -m pip`，是让当前解释器调用自己的 pip，省得安装成功了，运行时却找不到包。（电脑里 Python 一多，这种错位还挺会装成程序问题。）官方教程也采用这个安装形式。genui{"citation":{"ref":"turn47view1"}}

**3．能跑之后，记录依赖**

```powershell
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
python --version
```

这条导出命令显式指定 UTF-8，免得不同版本 PowerShell 的重定向编码添乱。把 Python 版本记进 README，再写清启动命令和必要配置。

`freeze` 记录环境里已安装的包及版本，通常也包括间接依赖；它不会读你的代码判断哪些包用得上。所以别把试验田里的所有包一起打包成家传配方。日常只往这个环境装项目需要的东西，新增或升级后试跑，再更新清单。它也不是完整锁文件，不能保证跨平台、跨 Python 版本原样复现。genui{"citation":{"ref":"turn47view2"}}

**4．换电脑：重新建，不搬旧环境**

在新电脑安装与原项目相同主、次版本的 Python，并尽量保持相同架构；拿到代码和清单后，在项目根目录执行：

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

先核对版本，再安装。本龙不建议搬家当天顺手升级 Python，出问题会平白多一个嫌疑对象。清单只负责包，数据文件、环境变量和外部程序仍要另行准备；恢复后实际跑一次常用功能。官方教程明确支持把清单纳入版本控制，再用 `install -r` 重装。genui{"citation":{"ref":"turn47view1"}}

**5．为什么不上传 `.venv`？**

它包含生成的解释器、第三方包及与本机有关的路径，通常不可直接搬迁；上传后既堆大仓库，也不能替代恢复步骤。源码放在项目目录，别塞进 `.venv`。在根目录 `.gitignore` 加：

```gitignore
.venv/
```

提交源码、`requirements.txt`、README 和 `.gitignore`。Python 官方也明确把虚拟环境视为可删除重建、不应入 Git 的目录。genui{"citation":{"ref":"turn47view0"}}

**遇到问题，按这个顺序查**

- **激活被脚本策略阻止**：先不用改策略，直接调用环境解释器：

  ```powershell
  .\.venv\Scripts\python.exe -m pip install -r requirements.txt
  .\.venv\Scripts\python.exe main.py
  ```

  激活只是方便输入，官方确认它并非必需。genui{"citation":{"ref":"turn47view0"}}
- **装了仍报找不到模块**：重查 `sys.executable`；编辑器也选同一个环境。先查跑的是谁，别急着重复安装。
- **找不到 `python`**：先确认 Python 安装及命令可用，重新打开终端；环境还没创建时，后面的命令自然救不了场。
- **新开终端又失效**：重新激活，或继续用完整路径。用完输入 `deactivate` 即可退出；它不会删除环境。
