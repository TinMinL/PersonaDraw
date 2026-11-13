# 任务

我在 Windows 上写了个 Python 自用小工具。请按以下固定资料教我建立虚拟环境、安装依赖、记录依赖、换电脑恢复，以及不上传 .venv 的原因和常见排错。使用 Windows CMD；入口 main.py，示例依赖 requests，示例目录 C:\work\mytool。只提供教程，不实际执行命令或改项目。正文 1000—1200 个汉字（不计代码、英文、标点），分为六节：建立环境、安装依赖、记录依赖、换电脑、Git、排错。各节都要解释原因与接下来的判断，不以重复内容凑长度。只使用下面资料，不另行搜索；引文可用 [1]/[2]，正文末列URL。

# 固定资料

资料由主任务于2026-11-13查阅；此题检验读完相同资料后的讲解，不检验独立搜索能力。

[1] https://docs.python.org/3/library/venv.html
venv 默认隔离第三方包，基于创建它的 Python。Windows 环境包含 Scripts/python.exe。CMD 激活用 .venv\Scripts\activate.bat；激活只影响当前终端的查找路径，新终端需重做。也可以直接运行环境解释器，不必激活。环境可以重建，不宜纳入 Git 或当作可搬运目录；脚本可能包含绝对路径。源码放在环境之外。

[2] https://pip.pypa.io/en/stable/cli/pip_freeze/
freeze 输出已安装包的 requirements 格式清单，不扫描源码，不生成完整锁文件。默认省略部分引导工具；Python 3.12 之后默认省略 pip。需要全部时用 --all。用 python -m pip freeze > requirements.txt 导出，用 python -m pip install -r requirements.txt 恢复。

# 题设约定与要求

已安装 Python，创建前检查 python --version；激活后用 python -c "import sys; print(sys.executable)" 确认解释器路径。使用 python -m pip install requests 安装，python main.py 验收。标准库不需额外安装。导出会覆盖文件。README 另记Python版本、入口、数据配置及外部程序；换电脑先核对Python主次版本与架构，重建后实际运行，不保证跨平台完全复现。项目根 .gitignore 写 .venv/；已跟踪的目录仅加忽略规则不会取消跟踪。本题仅说明该边界，不提供删除命令。排错覆盖找不到python（py可用时可用py创建）、安装后缺包（核对终端与编辑器解释器）、新终端需激活、版本不兼容时先读报错不要盲目清空版本限制。不可声称已实际执行。
