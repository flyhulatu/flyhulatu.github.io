---
title: "关于"
layout: "page"
url: "/about/"
summary: about
slug: about
hidden: true
comments: false
disableShare: true
disableHLJS: true
---
<style>
  .post-header { display: none; }

  .about{
    max-width: var(--measure);
    margin: 0 auto;
  }
  .about h1{
    font-size: 1.9rem;
    line-height: 1.15;
    margin: 0.2rem 0 1rem;
  }
  .about p{
    margin: 0.85rem 0;
  }
  .about .muted{
    color: var(--muted);
  }

  /* 让链接像“正文的一部分” */
  .about a{
    color: var(--text);
    text-decoration: underline;
    text-underline-offset: 3px;
    text-decoration-color: var(--faint);
  }
  .about a:hover{
    text-decoration-color: var(--text);
  }

  /* 行内链接列表（QQ · WeChat · ...） */
  .about .links{
    margin: 0.6rem 0 1.1rem;
    display: inline;
  }
  .about .links a{
    font-weight: 600;
  }
  .about .dot{
    color: var(--muted);
    padding: 0 0.45rem;
  }

  /* 小标题更克制 */
  .about h2{
    font-size: 1.05rem;
    font-weight: 700;
    margin: 1.6rem 0 0.45rem;
  }

  /* 小分隔（可删） */
  .about hr{
    border: 0;
    border-top: 1px solid var(--faint);
    margin: 1.4rem 0;
  }
</style>

<div class="about">
  <h1>朋朋 <span class="muted">（笔名：胡拉图）</span></h1>
  <p class="muted">一名不谈专业、只聊生活、热爱折腾的研究生。</p>
  <hr>
  <h2>关于</h2>
  <p>泥嚎！欢迎来到我的世界。</p>
  <p>目前在郑州上学。平时喜欢搞鼓 Mac、写作和各类生产力工具。</p>
  <p>这个博客用来记录学习和生活，希望你喜欢。</p>
  <p>
  博客搭建基于 Hugo 框架、PaperMod 主题；
  
  参考 [Solazy](https://blog.solazy.me/) 的博客，简化成了 BearBlog 风格。
  </p>

  
  <h2>订阅</h2>
  <p class="links">
    <a href="/atom.xml">Atom</a><span class="dot">·</span>
    <a href="/rss.xml">RSS</a><span class="dot">·</span>
  </p>
  
  <h2>平台</h2>
  <p class="links">
    <a href="https://sspai.com/u/hulatu/updates">少数派</a><span class="dot">·</span>
    <a href="https://www.xiaohongshu.com/user/profile/68a9d4e5000000001a00fcf9">小红书</a><span class="dot">·</span>
    <a href="https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/m1g8nr.webp">公众号</a><span class="dot">·</span>
  </p>


  <h2>交流</h2>
  <p class="links">
    <a href="https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/46bLCd.webp">QQ</a><span class="dot">·</span>
    <a href="https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/XbfMd9.webp">WeChat</a><span class="dot">·</span>
    <a href="mailto:flyhulatu@gmail.com">Gmail</a><span class="dot">·</span>
    <a href="mailto:2983685624@qq.com">QQ Mail</a><span class="dot">·</span>
  </p>
</div>
