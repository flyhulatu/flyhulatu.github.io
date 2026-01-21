---
title: "关于"
layout: "about"
url: "/about/"
summary: about
slug: "about"
showToc: false
# 隐藏页面元数据（发布日期、作者、阅读时间等），这对于 About 页很重要
hidemeta: true
# 禁用评论（可选，通常 About 页不需要评论）
comments: false
disableShare: true
# 如果你想让这个页面不出现在首页列表中
disableHLJS: true
---
<style>
  /* About 页局部：更像 Bear（纯文本、无组件感） */
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
  <h1>胡志朋 <span class="muted">（笔名：胡拉图）</span></h1>

  <p class="muted">一名不谈专业、只聊生活、热爱折腾的研究生。</p>

  <hr>
  
  <h2>关于</h2>
  <p>泥嚎！欢迎来到我的世界。</p>
  <p>目前在<strong>郑州</strong>上学。平时喜欢搞鼓 <strong>Mac、GitHub、写作</strong> 和各类生产力工具。</p>
  <p>这个博客用来记录学习和生活随想，希望你喜欢。</p>


  <h2>联系</h2>
  <p class="links">
    <a href="https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/qq.webp">QQ</a><span class="dot">·</span>
    <a href="https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/wechat.webp">WeChat</a><span class="dot">·</span>
    <a href="mailto:flyhulatu@gmail.com">Gmail</a><span class="dot">·</span>
    <a href="mailto:2983685624@qq.com">QQ Mail</a>
  </p>

  <h2>订阅</h2>
  <p class="links">
    <a href="/feed">Feed</a><span class="dot">·</span>
    <a href="/atom.xml">Atom</a><span class="dot">·</span>
    <a href="/rss.xml">RSS 2.0</a><span class="dot">·</span>
    <a href="/rss1.xml">RSS 1.0</a>
  </p>

  <h2>平台</h2>
  <p class="links">
    <a href="https://sspai.com/u/hulatu/updates">少数派</a><span class="dot">·</span>
    <a href="https://www.xiaohongshu.com/user/profile/68a9d4e5000000001a00fcf9">小红书</a><span class="dot">·</span>
    <a href="https://cdn.jsdelivr.net/gh/flyhulatu/img@main/uPic/gzh.webp">公众号</a>
  </p>
</div>
