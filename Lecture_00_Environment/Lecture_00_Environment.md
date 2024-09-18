---
title: Lecture_00_Environment
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css: assets/custom.css
autoTitlePage: true
makeTitle:
    lecture: SI100+ 2024 Lecture 0
    title: 环境配置
    detail: SI100+ 2024 Staff | 2024-08-20
makeThanks: true
---

# Part.1 配置开始前的说明

<!--v-->

## 我们将要配置什么？

在本教程中，我们将配置一套可以用于 SI100B 课程的环境： Anaconda + Jupyter Notebook + VS Code

</br>

- Anaconda：一个 Python 发行版，提供了**包管理、环境管理**等非常方便的功能
  - 这里我们并没有选取 `python.org` 的 Python 安装包，是因为 Anaconda 提供了更好的环境管理功能
- Jupyter Notebook：一个交互式笔记本，可以融合代码、文本、图像等多种元素
- VS Code：~~最好的~~代码编辑器，拥有丰富的插件生态，支持多种编程语言

<!--v-->

## ⚠️：不要安装多个 Python

<div style=" margin-top: 10px; margin-right: 10px;" markdown="1">
<img src="images/python_environment.png" width="55%" style="float: right;">

<br/>

- 不同的项目可能需要不同的 Python 版本
- 不同的 Python 版本又可能需要不同版本的库
- 有没有工具可以让我们在不同的 Python 环境之间自由切换？

</div>

<!--v-->

## 可能遇到的问题

- 检查你的用户名是否为英文，中文用户名可能导致安装软件时出现问题
  - 打开 PowerShell，输入 `whoami`, 输出中不应该包含中文字符
- 我们将在 Windows 11 操作系统下演示，如果你使用其他操作系统，可以询问使用对应操作系统的助教
- 如果你遇到任何问题，请在 Piazza 或 Office Hour 求助，助教们都乐意帮助你 🥰

<!--s-->

# Part.2 Anaconda

<!--v-->

## 安装 Anaconda

- 打开浏览器，访问 [Anaconda 官网下载页面](https://www.anaconda.com/download/success)，点击 Download 按钮开始下载
- 也可以选择国内镜像下载，如 [清华大学镜像站](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=D)

<img src="images/anaconda_download.png" width="80%" style="display: block; margin: 0 auto;">

<!--v-->

## 安装 Anaconda

- 下载完成后，运行安装程序
- 点击 Next/I Agree 几次后会出现如下图所示的，选择安装位置的界面，如果不确定要安装到哪个位置，直接点击 Next 即可

<img src="images/anaconda_install_location.png" width="50%" style="display: block; margin: 0 auto;">

- 接下来一路点 Next/Install 直到安装完成即可

<!--v-->

## 启动 Anaconda Powershell Prompt

- 在安装完成后，Anaconda Navigator 会自动打开，我们可以在这里找到 Anaconda Powershell Prompt
- 后面你也可以在开始菜单中找到 Anaconda Powershell Prompt 和 Anaconda Prompt

<img src="images/anaconda_navigator.png" width="65%" style="display: block; margin: 0 auto;">

<!--v-->

## 创建一个新的 Python 环境

- 在 Anaconda Navigator 中，点击左侧的 Environments `->` Create
- 输入环境的名字，比如 `si100`，然后点击 Create

<img src="images/anaconda_create_env.png" width="70%" style="display: block; margin: 0 auto;">

<!--v-->

## 创建一个新的 Python 环境

<img src="images/anaconda_name_env.png" width="70%" style="display: block; margin: 0 auto;">

<!--v-->

## 安装 Jupyter Notebook

- 创建环境后，我们可以通过在环境列表里面点击对应环境的方式来切换，切换到我们刚刚创建的环境
- 点击左侧的 Home，找到 Notebook，点击 Install

<img src="images/anaconda_install_notebook.png" width="70%" style="display: block; margin: 0 auto;">

<!--s-->

# Part.3 VS Code & 插件

<!--v-->

## 安装 VS Code

- 打开浏览器，访问 [VS Code 官网下载页面](https://code.visualstudio.com/Download)，选择对应你的操作系统的版本下载

<img src="images/vscode_download.png" width="80%" style="display: block; margin: 0 auto;">

<!--v-->

## 安装 VS Code

- 下载完成后，运行安装程序
- 点击同意协议

<img src="images/vscode_install_1.png" width="50%" style="display: block; margin: 0 auto;">

<!--v-->

## 安装 VS Code

- 选择安装位置
- 如果不确定要安装到哪个位置，就用默认的位置

<img src="images/vscode_install_2.png" width="50%" style="display: block; margin: 0 auto;">

<!--v-->

## 安装 VS Code

- 在选择附加任务的界面，将下图红框中的选项勾选上

<img src="images/vscode_install_3.png" width="50%" style="display: block; margin: 0 auto;">

- 继续一路点击，完成安装

<!--v-->

## 安装 VS Code 插件

- 打开 VS Code，点击左侧边栏的 Extensions 图标
- 我们需要安装 Python 和 Jupyter 这两个插件
- 如果侧边栏没有自动推荐这两个插件，可以在搜索框中搜索并安装

<img src="images/vscode_extensions.png" width="75%" style="display: block; margin: 0 auto;">

<!--s-->

# Part.4 在 VS Code 中使用 Jupyter Notebook

<!--v-->

## VS Code 打开文件夹

- 在桌面或者其他地方新建一个文件夹，命名为 `SI100+`
- 将 Piazza 上的本课的 Jupyter Notebook 文件（`.ipynb` 文件）移动到 `SI100+` 文件夹中
- 在 Anaconda Navigator 中找到 VS Code 点击 Launch，令 VS Code 可以找到 Anaconda 中的 Python 环境
- 在 VS Code 中点击顶部菜单栏的 File `->` Open Folder，打开刚刚新建的 `SI100+` 文件夹
- 点击左侧边栏的 `.ipynb` 文件，即可打开文件，跟随 Notebook 的内容继续学习

<div style="position: absolute; bottom: -20vh; text-align: center;">

### 到这里，我们的环境配置初步完成！🎉

</div>