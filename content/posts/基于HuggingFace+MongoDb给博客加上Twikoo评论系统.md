---
title: "基于HuggingFace+MongoDb给博客加上Twikoo评论系统" 
date: 2026-01-19T21:19:41+08:00 
                           
slug: ""                                                                  
summary: ""                              
categories:                                  
  - ""
tags:                                        
  - ""

draft: true
showToc: true                                
TocOpen: true                                
hidemeta: false                              
comments: true                              
disableShare: false                          
# canonicalURL: ""                           
---

如果你想有一个个人网站，市面上有很多搭建教程，我就先不写了，基于 **Hexo、Hugo、WordPress、VuePress……**这些平台都可以，挑选一款喜欢的主题，比如我的主题是 PaperMod，就可以开始搭建了，把网站放在 GitHub 的仓库里。

这时候，很多人会想要一个评论系统，giscus 搭建起来是最简单的，因为开源、免费、无广告，而且和 GitHub 的互联很好，有个缺点——就是浏览者想要评论必须要有个 GitHub 账号，这个其实有点门槛。

后来，我还是换成了 Twikoo，任何人都可以评论，大大的增加了个人博客的温度。

我使用的工具是 **HuggingFace+MongoDb**，下面我给大家分享一下，搭建的过程。

[MongoDb](https://cloud.mongodb.com/)

[HuggingFace](https://cloud.mongodb.com/)

第一步，这两个网站的账号，你得先注册，有一个自己的账号。

