可以，本龙带你从两个文件开始，把正常结果、边界和异常都照顾到。`unittest` 属于标准库，不用另装依赖；代价是类和断言写起来稍多。小项目先用它很省心，大量参数组合或复杂夹具再评估其他方案，别一上来就把工具箱塞满。

**先把文件摆好。** 在一个空目录放下面两个文件。业务与测试分开，改实现时更容易看清要求有没有被偷偷改掉；代价是多维护一个文件。这个平铺结构适合起步，项目长大后再建 `tests/`，届时要一并处理包与导入路径。

`calculator.py`：

```python
def divide(a, b):
    if b == 0:
        raise ValueError("divisor must not be zero")
    return a / b
```

`test_calculator.py`：

```python
import unittest
from calculator import divide


class TestDivide(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(divide(6, 3), 2)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 3), 0)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            divide(6, 0)


if __name__ == "__main__":
    unittest.main()
```

盯住三个约定：文件以 `test_` 开头、类继承 `TestCase`、方法以 `test_` 开头，这样发现机制才能接住它们。末尾入口让文件能直接执行；只用模块命令运行时可以省略。这里把零除定义为 `ValueError` 是示例的接口选择；你的项目若约定 `ZeroDivisionError`，就按它来，本龙可不会为了测试好看擅改契约。genui{"citation":{"ref":"turn43view0"}}

**断言要挑剔一点。** `assertEqual` 检查具体结果，比只检查“结果为真”更能抓错；`assertTrue` 适合明确的真假条件，却抓不住“返回了另一个非零数”。`assertRaises` 验证预期异常，里面只放目标调用，免得其他操作碰巧报错也算过关。别写成宽泛的 `Exception`，那会放走错误类型。genui{"citation":{"ref":"turn43view0"}}

本龙特意选了能精确表示的结果，让你先看懂流程。一般浮点运算可能存在舍入误差，应按业务容差比较；容差太松会漏错，金额要求精确时也不该靠放宽误差蒙混过关。genui{"citation":{"ref":"turn44view0"}}（放心，我会催你跑起来，也会拦着你把绿灯当护身符。）

**现在运行。** 在这两个文件所在目录执行，`python` 应指向你的 Python 3 环境；系统用 `python3` 时替换命令前缀。

```bash
python -m unittest discover -v
```

预期看到 `Ran 3 tests` 和 `OK`。发现模式会按默认 `test*.py` 找文件，适合日常全量检查；`-v` 显示每个测试名，排错舒服，测试多时日志也更长。只调一个问题就缩小范围：

```bash
python -m unittest -v test_calculator.TestDivide.test_zero_divisor
```

这会更快，但改完还得跑全套，漏掉的关联行为不会自己来提醒你。genui{"citation":{"ref":"turn43view0"}}

**报错时跟我看这几处。**

- `Ran 0 tests`：先查目录、文件名、方法名和继承；零个测试的 `OK` 可不够让本龙点头。
- `FAIL`：通常是断言不满足。核对需求、实际值和预期值，别急着把预期改成实际。
- `ERROR`：出现了未预期异常；如 `ModuleNotFoundError`，先查运行目录、解释器和模块命名，避免把文件命名为 `unittest.py`。genui{"citation":{"ref":"turn43view0"}}

读 traceback 先看末行异常类型，再沿文件与行号找自己的代码；语法错误的箭头是发现问题的位置，真正漏掉的冒号可能在前面。genui{"citation":{"ref":"turn44view1"}}

这个例子没有共享资源，我就不塞 `setUp()` 了；以后多个测试都要准备对象时再加，代价是每次准备的开销。自动测试会自动判断结果；要每次提交自动运行，还需让 CI 执行同一条命令。先把本地三项跑通，再接这一层，进度稳稳握在你手里。
