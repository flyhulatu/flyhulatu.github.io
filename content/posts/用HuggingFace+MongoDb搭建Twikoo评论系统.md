---
title: 用HuggingFace+MongoDb搭建Twikoo评论系统
date: 2026-01-19T21:19:41+08:00  
slug: ""  
summary: ""  
draft: true  
hidemeta: false  
comments: true   
---                           
如果你想有一个个人网站，市面上有很多搭建教程，我就先不写了，基于 **Hexo、Hugo、WordPress、VuePress……**这些平台都可以，挑选一款喜欢的主题，比如我的主题是 PaperMod，就可以开始搭建了，把网站放在 GitHub 的仓库里。

这时候，很多人会想要一个评论系统，giscus 搭建起来是最简单的，因为开源、免费、无广告，而且和 GitHub 的互联很好，有个缺点——就是浏览者想要评论必须要有个 GitHub 账号，这个其实有点门槛。

后来，我还是换成了 Twikoo，任何人都可以评论，大大的增加了个人博客的温度。

我使用的工具是 **HuggingFace+MongoDb**，下面我给大家分享一下，搭建的过程。

[MongoDb][1]

[HuggingFace][2]

第一步，这两个网站的账号，你得先注册，有一个自己的账号。

![新建][image-1]

![任意填一个名称][image-2]

![下一步][image-3]

![新建][image-4]

![必须要和我选择一样][image-5]

![调整ip][image-6]

![必须出现0.0.0.0/0][image-7]

![等状态称为 Active][image-8]

![点 connect][image-9]

![点 drivers][image-10]

![复制密钥][image-11]

记得把方框框起来的部分，换成你

获取这串密钥，打开下面的链接：

https://huggingface.co/spaces/imaegoo/twikoo?duplicate=true

![粘贴密钥][image-12]

把刚才复制的那一串密钥，粘贴进来，进行下一步。

![点击这里][image-13]


![复制这串地址][image-14]

在把刚才复制的链接，放在以下这段代码里。

在你的博客根目录下找到 layouts/partials/ 文件夹（如果没有就新建一个），创建一个文件叫 comments.html。填入以下代码：

```html
<div id="tcomment"></div>
<script src="https://registry.npmmirror.com/twikoo/1.6.44/files/dist/twikoo.min.js"></script>
<script>
twikoo.init({
  envId: '你的后端URL',    // 在单引号里填入获取的链接
  el: '#tcomment',
})
</script>
```

在 envId: 后填入我们刚复制的那个地址，那就是你的后端 URL。

最后，找到主题中显示文章内容的模板（通常在 themes/你的主题/layouts/\_default/single.html）。不要直接改主题文件，建议将其**复制**到根目录下的 layouts/\_default/single.html 中。
在合适的位置（通常是 {{ .Content }} 之后）添加：

```html
{{ partial "comments.html" . }}
```

然后去预览一下你的博客，开启了评论的文章，都可以显示评论系统了。

[1]:	https://cloud.mongodb.com/
[2]:	https://cloud.mongodb.com/

[image-1]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/SIRfV5.png
[image-2]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/YLgggx.png
[image-3]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/Ci9ypb.png
[image-4]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/u37BWm.png
[image-5]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/r9T5OZ.png
[image-6]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/EovxB1.png
[image-7]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/716if0.png
[image-8]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/07LZHu.png
[image-9]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/kDV9Tg.png
[image-10]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/G0PSLh.png
[image-11]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/2g6ttJ.png
[image-12]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/ygNW6U.png
[image-13]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/ileofb.png
[image-14]:	https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/968KMk.png