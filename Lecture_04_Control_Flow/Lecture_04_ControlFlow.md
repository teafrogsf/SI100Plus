---
title: Lecture_03_Function
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css: assets/custom.css
revealOptions:
    transition: 'slide'
    transitionSpeed: fast
    center: false
    slideNumber: "c/t"
    width: 1000
---


<div style="display: flex; justify-content: center; align-items: center; height: 700px;">
  <div style="text-align: center; padding: 40px; background-color: white; border: 2px solid rgb(0, 63, 163); border-radius: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.1);">
    <h1 style="font-size: 48px; font-weight: bold; margin-bottom: 20px; color: #333;">SI100+ 2024 Python Lecture 4</h1>
    <p style="font-size: 24px; color: #666;">控制流</p>
    <p style="font-size: 16px; color: #999; margin-top: 20px;">SI100+ 2024  Staff | 2024-08-26</p>
  </div>
</div>

<!--s-->

# 01. 控制流

<!--v-->

## 控制流 (Control Flow) 到底是什么？

- 控制流是指在一个程序中，决定程序执行顺序的过程。

- 控制流是通过使用**条件语句**（如 `if-else`）和**循环语句**（如`for`、`while`）来实现的。

<!--s-->

## 条件语句

- 假设你遇到了这样一个场景
    - 中午吃饭的时候，你会检查卡有没有钱
        - 如果有钱，你就自己去吃饭
        - 如果没钱了，你就会~~和朋友一起去吃饭~~

我们简化一下： 

```txt
如果 卡里有钱 那么 自己去吃饭
否则 和朋友一起去吃饭
``` 

<!--v-->

## 条件语句 (cont'd)

我们将简化的内容翻译成 Python “代码”

```txt
如果 卡里有钱 那么 自己去吃饭
否则 和朋友一起去吃饭
```

```py []
if 卡里有钱:
    自己去吃饭
else:
    和朋友一起去吃饭
```

很显然，`if` 就相当于中文的 如果，`else` 相当于 否则，而冒号和函数的定义时遇见的一样，是用来标识一个代码块的。

其实，上面的 “代码” 叫做 **伪代码 (Pseudocode)** ，由于正式编程时，其中的细节可能非常复杂，而我们有的时候只关心逻辑是否正确，伪代码就是一个 **梳理思路** 的好帮手

接下来我们来正式看看 Python 中条件语句的用法

<!--v-->

## if 语句

- `if` 语句的基本语法如下：

```python
if condition: 
    statements
    statements
    ...
```

- 这里的 `condition` 是一个 **布尔表达式**，显然，如果其值为 `True`，那么` statements` 就会被执行
- 举个例子，在这个例子中，如果 `x` 大于 `0`，那么就会打印出 `x is a positive number`

```py [0|1|2|3]
x = 10
if x > 0:
    print("x is a positive number")
```

<!--v-->

- 当然，我们也可以用程序流程图来表示

```py [0|1|2|3]
x = 10
if x > 0:
    print("x is a positive number")
```

<img src="./if.png" width="50%" style="display: block; margin: 0 auto;"/>