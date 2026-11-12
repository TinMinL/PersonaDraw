你这个规模，用 **`venv`＋`pip`＋`requirements.txt`** 就够了。本龙查过 Python 和 pip 官方文档：虚拟环境让每个项目单独放依赖，免得你升级另一个工具，顺手把这个也弄坏。下面按 Windows PowerShell 写，路径和包名换成自己的；项目本身我没有改动。genui{"citation":{"ref":"turn53search0"}}

**先建立环境，把解释器认准。**

在项目文件夹打开 PowerShell，依次运行：

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

最后输出应指向当前项目的 `.venv\Scripts\python.exe`。本龙会看这个路径，不只看提示符有没有多出 `(.venv)`。源代码放在项目目录，别塞进 `.venv`，它是可以重建的耗材。激活只影响当前终端，关掉后下次重新激活即可；退出用 `deactivate`。genui{"citation":{"refs":["turn52view0","turn53search0"]}}

**接着装依赖，别装到隔壁去。**

假设工具需要 `requests`，激活后运行：

```powershell
python -m pip install requests
python -m pip --version
python main.py
```

把 `main.py` 换成你的入口文件。`python -m pip` 让安装动作跟着当前解释器走，第二条输出里的 pip 路径也应在 `.venv` 内。只装项目真正需要的第三方包，`json`、`pathlib` 这类标准库不用另装。（包不是收藏品，本龙不主张看见名字就收。）genui{"citation":{"ref":"turn53search1"}}

**跑通以后，再记录依赖。**

```powershell
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
python --version
```

第一条会覆盖清单，记录当前环境已装的包及版本，包括间接依赖；PowerShell 这里明确指定 UTF-8，省得编码添乱。第二条的版本请写进 README，并注明 Windows、启动命令和必要配置。以后增删或升级依赖，确认工具还能用，再更新清单。genui{"citation":{"ref":"turn52view1"}}

别把 `freeze` 当成它自动读懂了你的代码：实验时随手装进去的包也会被记下。它输出的是安装现状，并不是完整锁文件，更不会记录 Python 本身、系统组件或你的数据文件。小工具用它很实用，但本龙不会替它保证跨电脑百分之百复刻。genui{"citation":{"ref":"turn52view2"}}

**换电脑时，带清单过去重新建。**

先安装相同 Python 大小版本，尽量保持架构一致，再取回代码、清单及所需数据。在项目目录运行：

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

先核对第一条版本，再继续；装完要实际跑一遍常用功能，安装成功还不等于工具恢复成功。清单恢复安装是官方支持的用法，但环境差异仍可能影响结果。genui{"citation":{"ref":"turn52view1"}}

**为什么不把 `.venv` 上传 GitHub？**

官方明确把它视为应重建、不应纳入 Git 的目录：里面可能包含绝对路径，又依赖本机 Python 与平台，复制过去未必可用。把整箱环境搬走，看着踏实，结果可能连门都打不开。项目根目录的 `.gitignore` 加上：

```gitignore
.venv/
__pycache__/
```

提交代码、`requirements.txt`、README 和 `.gitignore` 就好；密码、令牌别一起提交。genui{"citation":{"ref":"turn52view0"}}

**遇到问题，先查这几处。**

- **`py` 找不到：**先试 `python --version`，能确认是所需版本，就用 `python -m venv .venv`；两者都不行，再检查 Python 安装。
- **PowerShell 拦截激活脚本：**别急着改系统策略。直接用 `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`，运行时也用该解释器接 `main.py`，无需激活。genui{"citation":{"ref":"turn52view0"}}
- **装过包仍报找不到模块：**先重跑上面的解释器路径检查；编辑器运行按钮也应选这一份 Python。本龙先查你用了谁，再考虑重装，免得忙半天只给另一份环境添了包。
