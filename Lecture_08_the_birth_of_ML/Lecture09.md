## 感知机的缺陷

* 感知机的缺陷非常明显，因为它仅仅是一个线性模型

* 相信聪明的你已经想到了，如果是下图的点要分类，一个简单的感知机模型显然是是无法做到的

<div align=center>  
<img src="https://i-blog.csdnimg.cn/blog_migrate/987cd61a7402119b10826f1e4893348f.png#pic_center" width=400> 
<div align=left> 

---

## 感知机的缺陷

* 图中的○和△无法用一条直线分开，但是如果将“直线”这个限制条件去掉，就可以实现了。比如，我们可以像下图那样，作出分开○和△的空间

<div align=center>  
<img src="https://i-blog.csdnimg.cn/blog_migrate/488a74468ef07fe2e09c675840335418.png#pic_center" width=400> 
<div align=left> 

* 感知机的局限性就在于它只能表示由一条直线分割的空间。上图这样弯曲的曲线无法用感知机表示。另外，由上图这样的曲线（非线性函数）分割而成的空间称为**非线性空间**，由直线（线性函数）分割而成的空间称为**线性空间**

## 早期机器学习的典型——感知机（perceptron）

<div align=center>  
<img src="image-1.png" width=250> 
<div align=left> 

* 把上述内容用数学式来表示，就是下面这个式子

$$ y = \left\{\begin{matrix} 
  0  \left ( w_1 x_1 +w_2x_2 \le \theta \right ) \\  
  1  \left ( w_1 x_1 +w_2x_2 > \theta \right )
\end{matrix}\right. $$

* 感知机的多个输入信号都有各自固有的权重，这些权重发挥着控制各个信号的重要性的作用。也就是说，权重越大，对应该权重的信号的重要性就越高

---

## 早期机器学习的典型——感知机（perceptron）

* 现在我们取权重参数$(\theta, w1, w2) = (−0.5, 1.0, 1.0)$，并将其可视化

$$ y = \left\{\begin{matrix} 
  0  \left ( -0.5 + x_1 + x_2 \le 0 \right ) \\  
  1  \left ( -0.5 + x_1 + x_2 > 0 \right )
\end{matrix}\right. $$

<div align=center>  
<img src="https://i-blog.csdnimg.cn/blog_migrate/a6bcf4af2c4bc6418dfa4062c8ee4937.png#pic_center" width=400> 
<div align=left> 

* 感知机会生成由直线$−0.5 + x_1 + x_2 = 0$分割开的两个空间.很容易发现，如果我们将上侧空间的点坐标输入给感知机，那么将输出1，否则输出是0

* 这其实就是一个非常简单的**二分类线性模型**，我们可以通过这个模型将一些点分成两类
---

## 感知机的缺陷

* 感知机的缺陷非常明显，因为它仅仅是一个线性模型

* 相信聪明的你已经想到了，如果是下图的点要分类，一个简单的感知机模型显然是是无法做到的



## 为什么它叫感知机呢？

* 回想起我们高中生物学过的知识（相信大家已经忘光了）

> 神经细胞结构大致可分为：树突、突触、细胞体及轴突。单个神经细胞可被视为一种只有**两种状态的机器**——激动时为‘是’，而未激动时为‘否’。神经细胞的状态取决于从其它的神经细胞收到的输入信号量，及突触的强度（抑制或加强）。当信号量总和超过了某个阈值时，细胞体就会激动，产生电脉冲。电脉冲沿着轴突并通过突触传递到其它神经元。

<div align=center>  <img src="image.png" width=250> 

---

## 早期机器学习的典型——感知机（perceptron）

* 没错，感知机是生物神经细胞的简单抽象，和神经细胞一样，感知机接受多个输入，最终只有一个输出（一般是0或者1）

下图就是一个接收两个输入信号的感知机的例子

<div align=center>  
<img src="image-1.png" width=250> 

<div align=left> 

* x<sub>1</sub> 、 x<sub>2</sub> 是输入信号，y是输出信号， w<sub>1</sub>、 w<sub>2</sub>是权重(weight)。

* 图中的○称为“神经元”或者“节点”。输入信号被送往神经元时，会被分别乘以固定的权重（w<sub>1</sub> x<sub>1</sub> 、 w<sub>2 </sub> x<sub>2</sub>）。神经元会计算传送过来的信号的总和，只有当这个总和超过了某个界限值时，才会输出1。这也称为“神经元被激活” 。这里将这个界限值称为阈值，用符号``θ``表示。

*到这里需要说出来：这是一层，或者说这是一个模块*
*能不能把这个作为模块搭起来？*

## 多层感知机（MLP）

* 未解决非线性空间的问题，科学家们引入了多层感知机（MLP，Multilayer Perceptron），也叫做人工神经网络
<div align=center>  
<img src="https://i-blog.csdnimg.cn/blog_migrate/fdd829e9575ea0544bcc9c43a01fd488.png" width=400> 
<div align=left> 

* 多层感知机最底层是输入层，中间是隐藏层（由很多层组成），最后是输出层

* MLP在隐藏层中引入了**激活函数**来解决输入输出只能是线性的问题，在此不多赘述

*MLP是不是也可以视为一个模块？*
*能不能把MLP也作为模块搭起来？*


梯度下降的时候要提到感知机其实跟梯度下降算出来的一样！

### 回归算法（看看就好）

* 线性(最小二乘)回归（Linear Regression）

* 多项式回归（Polynomial Regression）
* 逐步回归（Stepwise Regression）
* 岭回归（Ridge Regression）
* 套索回归（Lasso Regression）
* 弹性网回归（ElasticNet Regression）Lasso和Ridge回归技术的混合体
* XGBoost回归
* 泊松回归（Poisson Regression）