# SI 100+ 2024 Summer - Maze Game

## 简介

这是一个从上一届 SI 100B 的 Final Project 汲取灵感而~~偷~~来的小游戏。你将操控主角走完迷宫！

## 在开始之前

在开始之前，你需要在你的虚拟环境中装好 `pygame` 库，这是一个基于 Python 的游戏库，我们的 Maze Game 基于它编写，否则将会抛出如下错误。

```
ModuleNotFoundError: No module named 'pygame'
```

如果你还不知道什么是虚拟环境或想新建一个虚拟环境，可以参考 Lecture_00_Environment 中的配置，新建一个环境。  
如果你不知道如何通过 `conda` / `pip` 在某个虚拟环境中安装 `pygame` 库，可以参考 Lecture_06_How_To_Use_Python 来安装额外的库。

> 如果下载速度过慢，可以尝试**换源**，以清华大学镜像源为例，可以在 `pip install ...` / `conda install ...` 命令后加入 `-i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple`

```
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
Collecting pygame
  Downloading https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/8e/4b/8034e481b7f40026943947d8e81e39d335cea9c649770d309c657b700311/pygame-2.6.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (14.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.0/14.0 MB 1.7 MB/s eta 0:00:00
Installing collected packages: pygame
Successfully installed pygame-2.6.0
```

## Credits

美术素材：

[Sokoban Free Tileset - DANI MACCARI](https://dani-maccari.itch.io/sokoban-tileset)

[Small 8-direction Characters - AxulArt](https://axulart.itch.io/small-8-direction-characters)

字体：

[Caskaydia Cove Nerd Font - Nerd Fonts](https://www.nerdfonts.com/)
