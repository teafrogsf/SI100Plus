---
title: Lecture_PY_02_Var_Operator_Expr
theme: simple
highlightTheme: css/github.css
css: css/custom.css
revealOptions:
    transition: 'slide'
    transitionSpeed: fast
    center: false
    slideNumber: "c/t"
---


<div style="display: flex; justify-content: center; align-items: center; height: 700px;">
  <div style="text-align: center; padding: 40px; background-color: white; border: 2px solid rgb(0, 63, 163); border-radius: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.1);">
    <h1 style="font-size: 48px; font-weight: bold; margin-bottom: 20px; color: #333;">SI100+ 2024 Python Lecture 3</h1>
    <p style="font-size: 24px; color: #666;">函数</p>
    <p style="font-size: 16px; color: #999; margin-top: 20px;">SI100+ 2024  Staff | 2024-08-26</p>
  </div>
</div>

---

# 00. 在开始之前

--

## 如何查询已有函数的用法

- 我们已经学会了调用 `print`, `input` 来完成一些基本操作
- 但是 Python 还有很多函数，即使是 `print`, `input` 也有很多用法
- 如何查询？

--

## `help()`

**这是什么**

- `help()` 可以查看某函数或对象的帮助
- 在交互式命令行中
	- 输入 `help()` 并按下回车，可以进入交互式 `help` 环境（不太常用）
	- 输入 `help(x)` 并按下回车，可以看到关于 `x` 的帮助（`less` 模式）
		- 如果 `x` 是函数那么则是对于这个函数的帮助
		- 如果 `x` 是某个类型的字面值 / 变量，那么则是对于这个类型的帮助
- 在其他情况下，`help()` 就相当于 "`print(帮助内容)` "

--

在交互式控制台（打开 Anaconda Prompt / Terminal，输入 Python 并回车后）

```py
>>> help(print)
Help on built-in function print in module builtins:
# 上面告诉了你 `print` 是一个内置函数，在模块 `builtins` 里（之后会讲）
print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
# 上面两行分别是 `print` 的用法（也就是定义）和作用描述
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
# 下面是在解释在用法出现的“参数”含义（还记得 end 吗？）
~
(END)
```

+ ***怎么退出啊啊啊啊啊啊！！！**

--

## \[番外\] `less` ：只是为了看长长的报错

- Python 的控制台中的 `help` 使借用 `less` 命令输出的，在 `linux` 下，它是用来“展示”输出的（否则内容过多就会溢出屏幕而丢失）
- 在很久以前，计算机里只有 `vi` 编辑器，它规定的 `:q` 退出， `J/K` 用来上下翻页，`Ctrl+U/D` 快速上下翻页。而这成为了当时的习惯，被沿用下来。
- 当时 `less` 的作者 Mark Nudelman 只是想“方便的翻阅长长的报错”
	- 他当时用的 `vi` 版本不能打开这么大的日志文件
	- 另一个叫 `more` 的工具虽然能打开，但是不能向回翻<small>（现在似乎有了）</small>
- `less` = `vi` 的操作模式 + `more` 的文件支持 的“查看器” （文件分页器）

<split even>

- 极客的浪漫莫过于此
- 编程：重复事情上制胜的法宝

![GRT|300](https://www.globalnerdy.com/wp-content/uploads/2012/04/geeks-and-repetitive-tasks.jpg)

</split>

--

## 代码提示：VSCode 为什么比记事本好

- 将鼠标悬浮在 `print` 上，会弹出来一个小提示，会简单告诉你用法

```py
(function) # 告诉我们 `print` 是一个函数
def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None: ...
# 课后查阅资料：为什么会有两个 `print`？？？
def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: _SupportsWriteAndFlush[str] | None = None,
    flush: bool
) -> None: ...
```

--

## 代码提示 (cont' d)

- 除了鼠标悬浮，在你一边输入 `print(...)` 的时候，代码提示也会出现
- 并且会用醒目的标识来指示你正在输入哪个参数

```py
# 尝试在 VSCode 中缓慢打出
print("Hello", end="!")
```

--

## IPython 的小问号 `?`

- 在 Jupyter Notebook / IPython 里，我们可以直接用 `?` 接在函数名字的末尾

```py
In [1]: print?
Signature: print(*args, sep=' ', end='\n', file=None, flush=False)
# 上面告诉了我们用法格式/定义，下面这一串是 docstring (函数自身携带的文档的内容)
Docstring:
Prints the values to a stream, or to sys.stdout by default.

sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush
  whether to forcibly flush the stream.
# 最后告诉我们这是一个“内置函数或方法”
Type:      builtin_function_or_method
```

--

## 内置函数(?)初探

- `len(str)`: `str` 的长度
- `max(a, b)`: `a` 与 `b` 中最大值
- `min(a, b)`: `a` 与 `b` 中最小值
- `abs(x)`: `x` 的绝对值
- `str.upper()` 全大写的 `str`
- `str.lower()` 全小写的 `str`
- `str.capitalize()` 首字母大写的 `str`
- `str.replace(str1, str2)` 将 `str` 中的所有 `str1` 替换成 `str2`
- `str.replace(str1, str2, N)` 同上，但最多只替换 `N` 次
- `str.isupper()` `str` 是否全是大写字母（布尔类型）
- `str.isdigit()` `str` 是否全是数字（布尔类型）
- `str.isalpha()` `str` 是否全是字母（布尔类型）
- `str.isalnum()` `str` 是否全是数字或字母（布尔类型）

--

**演示** `"ABC123".isupper()"`

+ 为什么是 False?
+ `help("ABC123".isupper)` 一下？

--

> [!warning]
> 
> 尽管我们用简短的文字介绍了他们，但是还有很多细节是我们忽略了的
> 
> 使用函数的时候切记不可以 **望文生义**，遇到行为奇怪的函数，应该查文档和它的 Docstring

---

# 01. 函数与方法

--

## 函数 (function)

- 为什么要有函数？
	- 数学中，“令 $f(x) = x^{2}+2x+1$” 可以让我们过程更简洁
	- 编程中，定义一个函数可以**防止重复的代码**（代码复用）
- 函数是什么？
	- 独立的代码块，通过名称调用
	- 通俗理解，函数就是大段代码的“替身”

--

## 方法 (method)

- 什么是方法？我怎么从来没听说过？
	- 还记得我们之前的疑问吗？
	- 为什么有些“函数”是可以直接用的 (`print`)
	- 有些“函数”要用一个 `.` 连接才能使用？(`isdigit`)

**演示** 方法的“依赖性”

```py
print("123".isdigit())
print(123.isdigit())
```

--

## 方法 (method) (cont'd)

- 方法区别于函数，它不是 **随处可用** 的，而是 **依赖** 某个特定的字面值/变量
	- 例如，上述例子中，只有 `str` 类型的字面值/变量才能够使用 `.isdigit()`
	- P.S. 在 `IPython` / `Notebook` 中，也必须用 `类型名.方法名?` 来获取帮助
		- 但可以直接 `help(变量/字面值.方法名)` 和悬浮
- 我们并不会在这次课程中涉及到怎么写 **方法**，因为还需要很多面向对象的前置知识，在 SI 100B 正课里面（也许会）涉及

--

## Re: 内置函数和方法初探

- `len(str)`: `str` 的长度
- `max(a, b)`: `a` 与 `b` 中最大值
- `min(a, b)`: `a` 与 `b` 中最小值
- `abs(x)`: `x` 的绝对值
- `str.upper()` 全大写的 `str`
- `str.lower()` 全小写的 `str`
- `str.capitalize()` 首字母大写的 `str`
- `str.replace(str1, str2)` 将 `str` 中的所有 `str1` 替换成 `str2`
- `str.replace(str1, str2, N)` 同上，但最多只替换 `N` 次
- `str.isupper()` `str` 是否全是大写字母（布尔类型）
- `str.isdigit()` `str` 是否全是数字（布尔类型）
- `str.isalpha()` `str` 是否全是字母（布尔类型）
- `str.isalnum()` `str` 是否全是数字或字母（布尔类型）

--

# 太酷了，还有更多吗

--

## 引入库 (Import Packages)

- Python 自带了很多库，相当于有很多“工具箱”
- 我们可以使用 `import` 语句导入库，从而使用工具箱里的工具

```py
import math # 导入数学库

print(math.sqrt(16)) # 使用数学库里的平方根函数

import random # 导入随机数库

print(random.randint(1,100)) # 输出在 [a,b] 中的的随机整数
print(random.random()) # 输出在 0.0 <= x < 1.0 之间的随机小数
```

- 也有些强大的库需要额外安装，这些将会在之后涉及

---

# 02. 定义函数、调用函数

--

## 先尝试自己理解

下面是对 $f(x) = x^{2}+2x+1$ 的简单实现

```py []
def f(x):
	ans = x ** 2 + 2 * x + 1
	return ans
```

- 尝试运行
+ **无事发生。。。**

--

## 先尝试自己理解 (cont'd)

哦哦哦！！单纯的写函数而不调用，就像单纯 令 $f(x)=...$ 而不计算一样  
**是没有效果的！**

下面是对 $f(x) = x^{2}+2x+1$ 的简单实现（附**调用**）

```py []
def f(x):
	ans = x ** 2 + 2 * x + 1
	return ans

print(f(2))
```


**Magic!**

--

## `def` - 定义函数

```py [1]
def f(x):
	ans = x ** 2 + 2 * x + 1
	return ans
```

- 要定义一个函数，我们会用关键字 `def` 开头，后接函数名称和一对圆括号
- 圆括号里面的“变量”叫做**参数** (Parameter)，可以有多个，用逗号分隔
- 圆括号里写下的变量可以直接在函数里面使用，实际的值将由调用时 **真正的参数** 决定
	- 例如 `f(2)` 会自动将 `x` 赋值为 `2`，这样才计算得出了正确的结果
- **一定不要忘记那个冒号！**
	- 冒号相当于告诉 Python 我们的函数到底有“多长”
	- 具体多长那就是靠**缩进**解决，冒号后面跟的是有 4 个空格的代码，那下面紧挨着的所有 4 个空格开始的代码都是函数“内容”~
- **定义不一定会被执行**（目前理解为不会执行就好）

--

**函数定义的格式**

```py []
def 函数名(参数, 参数, ...):
    函
    数
    体
```

**演示** 谁在内部

```py [0|5|6|1,2,3|2|3|1,2,3,6|7|0]
def fun(): # 定义一个不需要参数的函数，定义不会执行
	print("我在函数内部！")
	print("我也在函数内部！")

print("我不在函数内部！")
fun()
print("我当然也不在函数内部")
```

--

那如果我们换一个顺序呢？

**演示** 函数调用顺序

```py []
g("初音未来")

def g(chara):
	print("我去,", chara, "!")
```

- 居然报错了？
  
```py
NameError                      Traceback (most recent call last)
Cell In[?], line 1
----> 1 g("初音未来")
      3 def g(chara):
      4 	print("我去,", chara, "!")

NameError: name 'g' is not defined
```

- 换回来呢

--

## 为什么动漫里要先喊技能名

- 函数必须先声明才能调用
	- 什么是声明？就是从 `def` 一直到代码块结束！

![declaration|400](../res/Pasted image 20240825112850.png)

--

## `return` 函数终结者

```py[3]
def f(x):
	ans = x ** 2 + 2 * x + 1
	return ans
```

- 函数存在的意义是什么？复用代码，从而更方便地
	- 执行某些代码
	- 计算某些值
- `return` 就是用来 **返回** 这个计算的值，倘若一个函数始终没有 `return` 执行完成后相当于返回了一个 `None` (代表什么都没有)
- 倘若计算完成，那使命也就完成了！也就没有继续运行的意义了！

--

**演示** 有返回值和无返回值

```py []
def calc1(x):
	ans = x ** 2

def calc2(x):
	ans = x ** 2
	return ans

def calc3(x):
	return x ** 2 # return 也可以直接返回

print(calc1(2), calc2(2), calc3(2))
```

--

**演示** `return` 之后不会继续运行函数

```py [8|2|3|4|5|1-5,8]
def ChuanShanJia():
	print("Gui Ye 先生")
	print("Tian Huang 陛...下")
	print("我滴任务完成辣")
	return "拉开了手榴弹，并没有爆炸"
	print("啊哈哈哈哈哈哈哈哈") # 笑不出来

print(ChuanShanJia())
```

- `return` 可以提前结束函数，通常会在以后的以下情况遇到
	- 某些情况输入就是错的，执行函数没有意义或者会导致崩溃
	- 某些情况是特定的，需要返回特定的值
	- 某些情况是更简单地，可以用更简单的方法计算并返回
- 以上的 **某些情况** 都代表了一种“只有特定条件才会触发”的含义，我们会在下一节课（控制流）中学会它！

---

# 03. 参数

--

## 参数：函数沟通的桥梁

- 刚才的例子中我们探索了如何传递参数，现在我们来看看参数到底是什么
- 参数分为形式参数和实际参数
	- 形式参数：就是写在定义处的参数 `def f(x1, x2):...`
		- 除了会作为变量使用之外，还能规定函数的形式（长什么样）
	- 实际参数：就是调用处的参数 `f(1, 2)`
		- 这里的参数具有实际意义，是真实拿来运算的值