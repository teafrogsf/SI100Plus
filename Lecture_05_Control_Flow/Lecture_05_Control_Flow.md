---
title: Lecture_05_Control_Flow
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
    <h1 style="font-size: 48px; font-weight: bold; margin-bottom: 20px; color: #333;">SI100+ 2024 Python Lecture 5</h1>
    <p style="font-size: 24px; color: #666;">控制流</p>
    <p style="font-size: 16px; color: #999; margin-top: 20px;">SI100+ 2024  Staff | 2024-08-26</p>
  </div>
</div>

<!--s-->

# 00. 控制流

<!--v-->

## 控制流 (Control Flow) 到底是什么？

- 控制流是指在一个程序中，决定程序执行顺序的过程。

- 一般的程序都是从上到下逐行代码执行，这是顺序结构 (Sequential Flow)

- 通过使用**条件语句**（如 `if-else`）和**循环语句**（如`for`、`while`），我们可以实现 条件结构 (Conditional Flow) 和 循环结构 (Looping Flow)

- 我们之前学过函数的运行逻辑，也就是当你调用一个函数时，会从入口处“跳”到函数处，在执行完后再“跳”回来，这是 分支结构 (Branching Flow)

- 这节课我们将主要介绍 条件结构 和 循环结构

<!--s-->

# 01. 条件结构

<!--v-->

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

很显然，`if` 就相当于中文的 如果，`else` 相当于 否则，而冒号和我们之前在《函数》的课程中遇见的一样，是用来标识一个代码块的。

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

```py
x = 10
if x > 0:
    print("x is a positive number")
```

<img src="./images/if.png" width="50%" style="display: block; margin: 0 auto;"/>

<!--v-->

## `if-else` 语句

- `if-else` 语句的基本语法如下：

```python
if condition:
    statement1
else:
    statement2
```

- 如果 `condition` 为 `True`，那么执行 `statement1`，否则执行 `statement2`。
- 例如，下面这个例子，因为 `x`不大于 `0`，所以会打印出 `x is not a positive number`

```py [0|1|2|4|5]
x = -10
if x > 0:
    print("x is a positive number")
else:
    print("x is not a positive number")
```

<!--v-->

- 同样也可以用流程图表示

```py []
x = -10
if x > 0:
    print("x is a positive number")
else:
    print("x is not a positive number")
```

<img src="./images/if_else.png" width="80%" style="display: block; margin: 0 auto;"/>

<!--v-->

- 倘若别的情况需要考虑呢？畅想一下下列情况

```py
如果 学生卡有钱 那么
    自己去食堂吃饭
或者 虽然卡里没钱，但有现金
    去全家买个方便面
否则
    找个同学一起吃
```

我们同样可以写出这样的代码：

```py []
if 学生卡有钱:
    去食堂吃饭
elif 有现金:
    去全家买方便面
else:
    找个同学一起吃
```

可见，这个 `elif` 蕴含了一个 “如果上面的（都）不满足，但是满足紧挨着的这个条件” 的意思，那我们来介绍一下 `if-elif-else` 语句吧

<!--v-->

## `if-elif-else` 语句

- `if-elif-else` 语句的基本语法如下：

```py
if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
...
else:
    statementN
```

注意，**可以有多个 `elif` 部分，也可以不包含 `else` 部分**

每个 `elif` 后面都跟着一个条件和相应的语句。如果 `condition1` 为 `True`，执行 `statement1`；否则，检查 `condition2`，如果为 `True`，执行 `statement2`；同理，直到最后，如果所有的条件都不为 `True`，执行 `statementN`.

<!--v-->

- 举个例子

```py [0|1|2|4|6|7|0]
x = 0
if x > 0:
    print("x is a positive number")
elif x < 0:
    print("x is a negative number")
else:
    print("x is zero")
```

- 如果中间的条件被满足，则不会进行接下来的比较了（哪怕条件满足）

```py [0|1|2|4|5|0]
x = 0
if x > 1:
    print("x > 1")
elif x < 1:
    print("x < 1")
elif x == 0:
    print("x is zero")
```

- 是不是有点类似 布尔表达式 中的 短路？

<!--v-->

## Nested `if`-statements 嵌套

- `if`、`elif` 和 `else` 主体中的所有语句也可以是条件语句，他们可以层层叠加，组成非常复杂的 `if` 网络（但是千万不要在实践中这么做！！！）

<img src="./images/image.png" width="70%" style="display: block; margin: 0 auto;"/>

<!--v-->

- 下面来看一个简单的例子

<div style="column-count: 2">

```py [0|1|2|4|5|7|9|10|0]
x = 50
if x < 2:
    print('Small')
else:
    if x < 10:
        print('Medium')
    elif x < 20:
        print('Big')
    elif x < 100:
        print('Huge')
    else:
        print('Ginormous')
```


<img src="./images/image-4.png" width="100%" style="display: block; margin: 0 auto;"/>

</div>

<!--v-->

- 但是并不建议你这么写，我们完全可以让他变得更加简单 (`else + if => elif`)

<div style="display: flex; align-items: center; justify-content: center;margin: 2vh;">

```py [0|3-4]
if x < 2:
    print('Small')
else:
    if x < 10:
        print('Medium')
    elif x < 20:
        print('Big')
    elif x < 100:
        print('Huge')
    else:
        print('Ginormous')
``` 
<!-- .element: style="margin: 1vh" -->

```py [0|3]
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 100:
    print('Huge')
else:
    print('Ginormous')
```
<!-- .element: style="margin: 1vh" -->

</div>

<!--v-->

## Example:

- 【2024 四川内江高三一模】如图是一个电子元件在处理数据时的流程图：

<img src="./images/image-10.png" width="70%" style="display: block; margin: 0 auto;"/>

```py []
def f(x):
    if x >= 1:
        y1 = x + 2
        return y1 ** 2
    else: # 写成 elif x < 1: 也可以，但没必要
        y2 = x ** 2
        return y2 + 2

x = int(input("请输入 x"))
print(f(x))
```

<!--v-->

## Example: 登机判断

```py []
def fly():
    ticket = int(input("是否购买机票（0-未购买 1-购买）"))
    safety = int(input("是否通过安检（0-未通过 1-通过）"))
    
    if ticket == 1 and safety == 1:
        print("请登机")
    elif ticket == 1 and safety != 1:
        print("未通过安检，不能登机")
    else:
        print("没有机票不能登机")
```

<!--s-->

# 02. 更多类型！列表、元组与字典

<!--v-->

## 列表 (`list`)

- 创建列表
    - `empty_list = []`
    - `fruits = ['apple', 'banana', 'cherry']`
    - 元素用 `,` 分隔

- 访问列表中的元素
    - 列表中可能有多个元素，我们用 **下标/索引** (index) 来访问
    - `fruits[1] = ?`: 索引从 `0` 开始

- 修改特定元素
    - `fruits[1] = 'blueberry'`

- 追加元素
    - 在末尾添加：`fruits.append('date')`

<!--v-->
## 列表 (`list`) (cont'd)

- 删除元素
    - 删除指定元素 `fruits.remove('banana')`
    - 删除指定索引的元素 `del fruits[1]`
    - 移除（并返回）最后一个元素 `last_fruit = fruits.pop()`

- 切片 (slide)
    - `fruits[from:to:step]`

- 长度
    - 获取列表中元素个数 `length = len(fruits)`

* operator运算符

  * '+' 可以连接两个 list `fruits + ['apple', 'banana']`


<!--v-->


## List

### Nested list 嵌套列表

* 我们可以在 `list` 中嵌套其他 `list`

* `matrix = [[1, 2, 3], [4, 5, 6]]` (二维列表)

<!--v-->

## 元组 (`Tuple`)

* Python 的元组与列表类似，**不同之处在于元组的元素不能修改**。

* 元组使用小括号，列表使用方括号。

* 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

```python []
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = (50,) # 元组中只包含一个元素时，需要在元素后面添加逗号
```

* 访问方法和list相同，只是元组中的元素值是不允许修改的。

<!--v-->

## 集合 (`Set`)

* 集合是一个无序的不重复元素序列。

* 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作

* 可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 `set()` 函数创建集合

```python []
set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合
```

<!--v-->

## 区分python中的四种集合数据类型

### （列表，元组，集合，字典）

1. 列表（List）：有序，可更改，可以有重复的成员

2. 元组（tuple）：有序，不可更改，可以有重复的成员

3. 集合（set）：无序，无索引，没有重复的成员。

4. 字典 （Dictionary）：无序，可更改，有索引，没有重复的成员(见末尾)

<!--s-->

# 03.循环语句

<!--v-->

## 循环

- 简单来说，循环语句就是让代码 **反复执行** 某个操作， **直到** 满足某个条件为止。
- 在 Python 中，最常用的循环语句就是 `for` 和 `while`

<!--v-->

## `while` - 很内向，吃饱了也不说话 

```py []
hungry = 10 # 如饱
print("很内向，吃饱了也不说话，就一直", end="")

while hungry > 0:
    print("吃", end="")
    hungry = hungry - 1

print()
print("吃饱了")
```

<!--v-->

## `while` 循环

```python
while condition：
    statements
```

<div style="column-count:2">

- 判断条件 (`condition`) 可以是任何表达式
- 当判断条件为 `False` 时，循环结束，否则一直循环
- 为了保证不会进入死循环 (infinite loop)，我们需要在 **循环体** （也就是循环要做的事情）中对先前的判断条件 **有所改变**

<img src="./images/image-9.png" width="80%"/>

</div>

<!--v-->

## Example: 猜数字

```py []
ans = 25
guess = input("请猜测: ")

while(ans != guess):
    if(ans < guess):
        print("大了")
    else:
        print("小了")
    guess = input("请重猜: ")

print("猜对了")
```

<!--v-->

## `break`, `continue`

- `break` 用于立即终止循环。无论循环条件是否为真，执行到 `break` 语句时，循环都会 **立刻结束**，跳出循环。
- `continue` 用于跳过 **当前的迭代**，并立即进行下一次迭代。后面的语句会被跳过，并直接进入下一次循环的条件判断。

<div style="display: flex; align-items: center; justify-content: center;margin: 2vh;">

```py [0|5|6|8|0]
i = 0
while i < 5:
    i += 1 # i += 1 就是 i = i + 1
    print(i)
    if i == 3:
        break
    print(i)
print("end.")
# Output: 1 1 2 2 3 end.
```
<!-- .element: style="margin:1vh"-->

```py [0|5|6|2|0]
i = 0
while i < 5:
    i += 1
    print(i)
    if i == 3:
        continue
    print(i)
print("end.")
# Output: 1 1 2 2 3 4 4 5 5 end.
```
<!-- .element: style="margin:1vh"-->

</div>

<!--v-->

## Example: 进制转换 (HARD)

- 还记得我们在扫盲课中介绍的，如何将十进制整数转换为二进制整数吗？
- 短除法！**每次** 除以 `2`， **直到** 商为 `0`，把结果从下往上读

```txt
将 10 转换为二进制 => 1010
10/2=5  ......0
5/2=2   ......1
2/2=1   ......0
1/2=0   ......1
```
<!--v-->

## Example: 进制转换 (HARD)

- 还记得我们在扫盲课中介绍的，如何将十进制整数转换为二进制整数吗？
- 短除法！**每次** 除以 `2`， **直到** 商为 `0`，把结果从下往上读

```py []
def decimal_to_binary(n):  
    binary_num = ''  
    while n > 0:  
        remainder = n % 2  
        binary_num = str(remainder) + binary_num # 不能写成 +=, 顺序不对
        n //= 2 # n = n // 2
    return binary_num  

decimal_number = 10
binary_number = decimal_to_binary(decimal_number)  
print(decimal_number, "的二进制是", binary_number)
```

- 请注意：这里最后的**binary_num**事实上是**string**类型的

<!--v-->

## `for` - 让你练习时长两年半

```py []
skills = ['唱', '跳', 'rap', '篮球']

print("前面忘了，喜欢")

for skill in skills:
    print(skill, end=", ")

print("Music!")
```

<!--v-->

## `for ... in` - 遍历

- `for` 循环可以 **遍历** 任何序列的项目，如一个列表或者一个字符串

```py []
for char in "123456":
    print(char, end="!")
print()
print(char) # char 在循环后仍然可用！写代码的时候小心变量名重名带来隐晦的错误！
```

```txt
1!2!3!4!5!6!
6
```

```py []
for fruit in ["apple", "banana", "cherry"]:
    print(fruit, end=", ")
```

```txt
apple, banana, cherry, 
```

<!--v-->

## `for` 中的 `break`, `continue`

- 行为和 `while` 一样，你还记得吗？

```py []
for fruit in ["apple", "banana", "cherry"]:
    if fruit == "banana": # 当遇到 banana 时结束循环
        break
    print(fruit, end=", ")
print("end.")
```

```py []
for fruit in ["apple", "banana", "cherry"]:
    if fruit == "banana": # 当遇到 banana 时跳过本轮循环
        continue
    print(fruit, end=", ")
print("end.")
```

<!--v-->

## 提一嘴：字符串 VS 列表

- 列表可以靠 `list1[i]` 获取单个元素，通过 `list1[start:end:step]` 切片
- 字符串可以靠 `str1[i]` 获取单个字符，通过 `str1[start:end:step]` 切片

- - -

- 列表的下标从 `0` 开始
- 字符串的下标从 `0` 开始

- - -

- 列表可以靠 `list1.append(item)` 添加
- 字符串可以靠 `str1 = str1 + "..."` 添加

- - -

- 两个列表可以通过 `+` 有序连接
- 两个字符串可以通过 `+` 有序连接

<!--v-->

## 来看一个奇怪的例子

```py []
li = [1, 3, 5, 7, 9, 11]
for i in li: # 一边迭代一边修改很危险！
    if i == 5:
        li.remove(i)
    print(i, end=' ')
```

<!--v-->

## Nested `for` statement 循环嵌套

```python
for i in [1, 2, 3]:
    for j in [1, 2, 3]:
        print(i * j, end=' ')
    print()
print('Bingo')
```

输出如下：

```python
1 2 3
2 4 6
3 6 9
Bingo
```

<!--v-->

## 太小了，我要一个 100 的循环 - `range`

```py
range(stop), range(start, stop), range(start, stop, step)
```

- `range` 能生成从 `start` 到 `stop` **而不包含 `stop`** 的“一列数”

```py []
>>> type(range(0, 10))       # range's type is `range`
<class 'range'>              # but we can convert it to list
>>> list(range(4))
[0, 1, 2, 3]                 # range(m) range from zero to m-1
>>> list(range(3, 9))
[3, 4, 5, 6, 7, 8]           # range(x, y) range from x to y-1
>>> list(range(3, 9, 2))
[3, 5, 7]
>>> list(range(7, 2, -1))    # range(x,y,-1) range form x to y+1
[7, 6, 5, 4, 3]
# range(x, y, step_size)
>>> list(range(4, 1))
[]                           # if x>y, it will be an empty object
```

<!--v-->

## Example: 判断奇数、偶数

- 这里涉及到了一点关于 [格式化输出](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html) 的用法，RTFM

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(f'Num:{i:2}: even')
    else:
        print(f'Num:{i:2}: odd')
```

<!--v-->

## 刚刚提过的小问题

```py []
num = 2
print("num =", num)

for num in [1, 5, 10]: # num 将覆盖外层的变量
    print(num,end=' ')

print()
print("num =", num) # 循环用的变量会被遗留下来，即使 num 也是由循环创建的
```

```txt
num = 2
1 5 10 
num = 10
```

- 编程习惯很重要，干净和有区分度的命名会避免小 bug
- 循环中，旧时通常使用 `i`, `j`, `k` 作为循环变量

<!--v-->

## Example: 判断质数

```py []
def is_prime(num):
    # 思路：默认输入的是一个素数，除非我们找到了一个因子
    if num < 2:
        return False # 0 和 1 不是素数！可以提前结束！
    for i in range(2, num):
        if num % i == 0:
            return False # 找到了一个因子，不是素数，函数提前结束！
    return True # 没有找到因子，是素数！

input_num = int(input("Input a number:"))

print(is_prime(input_num))
```

<!--s-->

## Takeaway Message

- 控制流是什么？
    - 条件结构
        - `if` ——如果
        - `if-else` ——如果，否则
        - `if-elif-else` —— `elif = else + if`
        - Nested-`if` 及正确化简
    - 循环结构
        - `while` ——满足条件一直做！
        - `for` ——遍历！逐个访问！
        - `break`, `continue` ——停下还是跳过
        - `range`：`for`的好帮手
        - 循环的嵌套

<!--s-->

## Takeaway Message (cont'd)

- 新学到的类型
    - `list` ——无序、什么都装的下的列表
    - `tuple` ——无法改变的“列表”
    - `set` ——集合，永远没有重复！

<!--s-->

<div style="display: flex; justify-content: center; align-items: center; height: 700px;" id="canvas">
  <div style="text-align: center; padding: 40px; background-color: white; border-radius: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.1);">
    <div style="display: inline-block; padding: 20px 40px; border-radius: 10 px; margin-bottom: 20px;">
      <h1 style="font-size: 48px; font-weight: bold; margin: 0; color: rgb(16, 33, 89)">Thanks for Listening</h1>
    </div>
    <p style="font-size: 24px; color: #666; margin: 0;">Any questions?</p>
  </div>
</div>


<!--v-->

# ??. 附加部分

由于各种原因，不确定是否有充足的时间，这一部分不一定会在上课中讲到～

但是我们会在 Notebook 中正常提供，供大家自行阅读～

**如果大家对某个内容呼声很高，可以在 Piazza 上发帖，也可以拉朋友来给你点赞（点 Good Notes / Good Question）！我们会做更多 Notebook / 视频带大家了解！**

<!--s-->

## 字典 (Dict)

* 字典的每个键值 **`key:value`** 用冒号 `:` 分割，每个键值对之间用逗号 `,` 分割，整个字典包括在花括号 `{}` 中 ,格式如下所示：
* 就像我们查《新华字典》，字就是 `key`，字的释义就是 `value`

```python
d = { key1 : value1, key2 : value2 }
```

* 键一般是唯一的、不可变的，如果重复最后的一个键值对会替换前面的，值不需要唯一。

```python
my_info = { # 这里用了一个比较美观的换行写法，适用于长文本排版
    "course_name": "SI 100+",
    "semester": "2023 Summer", # 这个逗号可选
}
```

形如 `"name": "ZAMBAR"` 的我们称之为**键值对** (key-value pairs)

<!--v-->

## 字典 (Dict) (cont'd)

更多请看即将 Release 的 Python 进阶 课程！

<!--v-->

## 简单的调试：追踪你的代码运行

- 注意到资料的**猜数字**代码左侧有一个小红点了吗？这个点的名字叫断点 (breakpoint)
- 鼠标悬浮在当前行的最左侧，就可以启用/禁用该断点
- 使用**调试**模式启动（代码块旁边有一个 ▶️ 的下拉菜单里，有一个 调试该代码块）时
    - 代码会自动在此处停止
    - 上面会多出一个执行的小方框
        - 我们暂时只需要无脑点 步入 (Step into) 就可以一步一步执行了
        - 上面小方框里的 ▶️ 代表继续，继续执行到下一次遇见断点或结束
    - 左侧会切换到 运行与调试 的菜单
        - 最上面写了一些探测到的变量，你可以实时观察他们
        - 中间是 监视，点击 + 可以输入一个 **表达式** 进行观测，就像实时 `print` 一样，非常方便
        - **小任务: 尝试观察 guess, 和 guess + 1**
    - 代码会有一行亮着的行，代表 **下一步** 将执行的代码

<!--v-->

## 格式化输出：让输出更美，字符串不分家！

- **判断奇偶的代码**里涉及到了一点关于 [格式化输出](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html) 的用法，RTFM
    - 字符串前的 `f` 是什么意思？
    - 字符串里的 `{i:2}` 是什么意思？运行的时候被替换成了什么？
    - 如果去掉 `:2` 输出是什么？你能明白 `:2` 的意思了吗？
    - 输出的格式是否更美观了？字符串是否可以从分割的变成一个整体了？
    - 你能理解格式化输出的意义了吗？
- 其实观察就可以发现，就是“让数字占据两位，用空格补齐”，那如果数字有三位呢？修改代码，观察结果。