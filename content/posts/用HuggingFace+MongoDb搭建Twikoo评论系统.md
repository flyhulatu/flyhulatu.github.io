---
title: 用HuggingFace+MongoDb搭建Twikoo评论系统
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





https://huggingface.co/spaces/imaegoo/twikoo?duplicate=true

把刚才复制的那一串密钥，复制进来





在把刚才复制的链接，放在以下这段代码里。

在你的博客根目录下找到 layouts/partials/ 文件夹（如果没有就新建一个），创建一个文件叫 comments.html。填入以下代码：

```html
<div id="tcomment"></div>
<script src="https://registry.npmmirror.com/twikoo/1.6.44/files/dist/twikoo.min.js"></script>
<script>
twikoo.init({
  envId: '你的后端URL',         // 在单引号里填入获取的链接
  el: '#tcomment',
})
</script>
```

最后，找到主题中显示文章内容的模板（通常在 themes/你的主题/layouts/\_default/single.html）。不要直接改主题文件，建议将其**复制**到根目录下的 layouts/\_default/single.html 中。
在合适的位置（通常是 {{ .Content }} 之后）添加：

```html
{{ partial "comments.html" . }}
```

然后去预览一下你的博客，开启了评论的文章，都可以显示评论系统了。
