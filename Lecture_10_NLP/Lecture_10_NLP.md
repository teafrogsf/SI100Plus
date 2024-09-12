---
title: Lecture_10_NLP
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css: assets/custom.css
autoFragment: true
autoTitlePage: true
makeTitle:
    lecture: SI100+ 2024 Lecture 10
    title: 用文字回应你的期待——自然语言处理
    detail: SI100+ 2024 Staff | 2024-09-13
revealOptions:
    transition: 'slide'
    transitionSpeed: fast
    center: false
    slideNumber: "c/t"
    width: 1000
    pdfSeparateFragments: false
---

# Intro: ChatGPT 的诞生

<!--v-->

## ChatGPT

- ChatGPT: Chat Generative Pre-trained Transformer
- 2022 年 11 月 30 日，ChatGPT 横空出世，短短5天，注册用户数就超过100万。
- 2023 年一月末，ChatGPT的月活用户已突破1亿，成为史上增长最快的消费者应用。
- 笔者当时拿它做疫情期间的英语试卷，比我分还高 /TwT/
- 引发了一火车 **新闻学乱象**
    - ![img|123](image.png)

<!--s-->

# AI 的两大流派 - NLP VS CV

<!--v-->

## 自然语言处理（NLP, Natural Language Processing）

- 自然语言处理
    - 顾名思义：关注如何让计算机理解、解释和生成人类语言。
- 特点：
    - 离散（Discrete）： 处理的文本数据是离散的字符和词汇。
    - 长上下文依赖（Long Context Dependency）： 理解和生成文本需要长距离的上下文信息。
    - 线性结构（Linear）： 语言数据可以看作是线性序列，如语句中的单词顺序。
- 主要任务：
    - 语言模型（Language Modeling）： 预测下一个词汇。
    - 机器翻译（Machine Translation）： 将一种自然语言翻译成另一种。
    - 情感分析（Sentiment Analysis）： 分析文本中的情感倾向。
    - 文本生成（Text Generation）： 生成有意义的文本段落。

<!--v-->

## 计算机视觉（CV, Computer Vision）


- 让计算机能够像人类一样理解和解析视觉世界。
- 特点
    - 连续（Continuous）： 处理的图像和视频数据是连续的。
    - 局部性（Locality）： 图像中每个像素的位置和邻域关系非常重要。
- 主要任务
    - 图像分类（Image Classification）： 识别图像所属的类别。
    - 目标检测（Object Detection）： 找出图像中的目标及其位置。
    - 语义分割（Semantic Segmentation）： 将图像划分为具有不同语义的区域。
    - 人脸识别（Face Recognition）： 识别并确认图像或视频中的人脸。

<!--v-->

## 其他流派

- 语音识别: 将口语转换为书面文本
    - 任务: 语音转文本、语音分析、语音生成
    - 应用: 语音助手、自动翻译电话、无障碍沟通技术
- 强化学习: 关注如何通过奖励和惩罚机制指导代理（agent）学习策略。
    - 任务: 策略优化、环境交互、奖励机制设计
    - 应用: 游戏AI、机器人控制、自动化交易系统
- 生成对抗网络（Generative Adversarial Networks, GANs）: 由生成器和判别器组成的模型框架，用于生成接近真实数据的假数据。
    - 任务： 图像生成、图像超分辨率、数据增强。
    - 应用： 图像合成、虚拟现实、艺术创作。

<!--v-->

## CV 与 NLP 的早期发展

- 计算机视觉的发展在深度学习时代率先取得了显著突破，其关键事件是上节课说的 AlexNet。
    - AlexNet 使用 CNN 取得了远超传统方法的准确率，激发了研究热潮。
    - 随后几年，计算机视觉领域涌现出一系列创新，包括VGGNet、GoogLeNet、ResNet等，更深更复杂的网络模型不断刷新图像识别的性能记录。
- 与此同时，自然语言处理（NLP）主要依赖于循环神经网络（RNN）及其变种，如LSTM和GRU，来处理序列数据。
    - 然而，RNN结构在处理长距离依赖和并行计算方面存在固有的局限性。
    - 2017年，Vaswani等人在论文 [**《Attention is All You Need》**](https://arxiv.org/abs/1706.03762) 中提出了Transformer模型，彻底改变了NLP领域。
        - 之前了解过 AI 的同学对这个文章名应该不陌生 ~~Money is All You Need~~
    - Transformer摒弃了RNN结构，采用了自注意力机制（self-attention mechanism），极大地改善了处理长距离依赖和并行计算的能力。

<!--v-->

## NLP 的异军突起

<div style="column-count: 2">

- 基于Transformer的 **语言模型** 如BERT、GPT系列、T5等，迅速成为NLP的主流技术。
- 这些模型大幅提升了各类NLP任务的表现，从文本分类、机器翻译，到问答系统和文本生成。
- 更可怕的是……
- Transformer不止局限于NLP，也开始在**计算机视觉、语音处理等**领域展现出强大的通用性和适用性。

<!-- <img src="./image-1.png" width="500"/> -->
![蛙蛙抱怨|380](image-1.png) <!-- .element: class="fragment" -->
</div>
