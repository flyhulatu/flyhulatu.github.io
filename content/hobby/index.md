---
title: "我的书影音"
date: 2026-01-10T13:50:29+08:00
lastmod: 2026-01-10T13:50:29+08:00
draft: false
# 描述：用于 SEO 和列表页显示的摘要，不填默认截取文章前几行
description: "" 

# 分类与标签
categories: [] 
tags: [] 

# 作者 (如果你想覆盖配置文件里的默认作者)
author: "图图"

# PaperMod 主题特定配置
# 是否在首页隐藏元数据（日期、作者等）
hidemeta: false
# 是否开启目录
showToc: true
# 是否开启评论 (如果你后续接了 Twikoo)
comments: true
layout: "hobby" 
ShowShareButtons: false
menu:
  main:
    name: "书影音"
    weight: 3

# 封面图设置 (PaperMod 核心功能)
cover:
    image: "" # 图片链接，本地图片建议放 static/images 下，填 images/xxx.png
    alt: ""
    caption: ""
    relative: false # 是否使用相对路径

# 这是一个非常重要的字段，特别是对中文标题
slug: "" 
---

## 🍿 最近看过的电影 

{{< douban type="movie" limit="12" >}} 

---

## 📚 最近读过的书

{{< douban type="book" limit="12" >}}