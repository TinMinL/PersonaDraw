你这个自用小工具，本小姐会选 **`venv + pip + requirements.txt`**：步骤少，换电脑时也有据可循。查过 Python 官方文档及 PyPA 文档后，下面按 Windows 的 PowerShell 来教；命令供你执行，我没有改动项目。

**先给工具一个独立环境。** 虚拟环境把这个项目的第三方包与其他项目分开，免得一次升级牵连另一份脚本。只有自己用，也值得留这点余地。先打开 PowerShell，进入项目目录，再创建环境：genui{"citation":{"ref":"turn5view1"}}

```powershell
cd C:\work\mytool
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

把路径换成你的实际目录。最后一行应显示项目内 `.venv\Scripts\python.exe`。若使用 CMD，激活命令改为 `.venv\Scripts\activate.bat`；不要把两种终端的写法混着用。激活只对当前终端生效，新开窗口要重新激活，退出用 `deactivate`。代码请放在项目目录，别放进 `.venv`。genui{"citation":{"ref":"turn4view0"}}

**再安装实际用到的包。** 下面用 `requests` 示范，换成你的依赖名称；若只用了 `json`、`pathlib` 等标准库，就不必为它们安装包。

```powershell
python -m pip install requests
python -m pip list
python main.py
```

我偏爱 `python -m pip` 这个写法：让当前 Python 执行 pip，少一层“包装进了另一套 Python”的疑惑。把 `main.py` 换成入口文件，确认工具能运行后再记录依赖，这个顺序才妥当，desuwa。genui{"citation":{"ref":"turn4view1"}}

**记录能工作的版本。** 在已激活的项目环境中执行：

```powershell
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
python --version
```

这里明确写 UTF-8，避开不同 PowerShell 版本的重定向编码差异。`freeze` 会记录已安装包，包括间接依赖，常见形式是 `包名==版本`。它不会分析源码来挑必需品，所以别在这个环境里随手安装无关包。（清单干净，未来的你才不必猜。）它也不是完整锁文件，不记录 Python 本体，不能保证跨平台原样复现；默认还会省略部分安装工具。把 Python 版本另写进 README，依赖变更且运行正常后重新导出清单。genui{"citation":{"ref":"turn5view0"}}

**换电脑时重建。** 先安装与原机相同主、次版本的 Python，尽量保持相同架构，再取回源码与清单。在项目目录执行，先核对版本：

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

安装成功后还要实际运行工具，别把“下载完了”当作验收。多个 Python 并存时，要用目标解释器创建环境；例如原来是 3.13，可用 `py -3.13 -m venv .venv`。genui{"citation":{"refs":["turn4view1","turn5view1"]}}

**GitHub 留源码和清单就好。** `.venv` 包含解释器相关文件、安装包以及与本机路径有关的内容，官方明确把它视为可重建、通常不可搬移的目录。上传既增加体积，也不能可靠解决迁移；换了目录都可能需要重建。本小姐要的是下次能恢复，存上一大箱机器相关文件可不算周到。项目根目录的 `.gitignore` 加入：genui{"citation":{"ref":"turn4view0"}}

```gitignore
.venv/
__pycache__/
*.pyc
```

源码、`requirements.txt`、README 和 `.gitignore` 则提交保存。

常见卡点先这样排：

- **`py` 找不到：** 若 `python --version` 正常，用 `python -m venv .venv`；两者都不可用，先检查 Python 安装。
- **禁止运行激活脚本：** 不必急着改系统策略，直接用 `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`，运行工具也用这个解释器。激活并非必要条件。genui{"citation":{"ref":"turn4view0"}}
- **装了仍提示缺包：** 再查 `sys.executable`，并让编辑器选中同一个环境解释器。
- **新机安装失败：** 先读报错，核对 Python 版本、架构及清单里的本地路径；不要一上来把全部依赖升级，免得原先可用的版本依据也丢了。
