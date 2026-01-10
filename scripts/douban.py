import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random
import re

# ================= 配置区域 =================
DOUBAN_ID = "230092146"  
TYPES = ["movie", "book"] 
DATA_DIR = "../data/douban"
# ===========================================

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Referer": "https://www.douban.com/"
}

def fetch_douban_data(media_type):
    data_list = []
    url = f"https://{media_type}.douban.com/people/{DOUBAN_ID}/collect"
    page_count = 1
    
    while url:
        print(f"正在抓取第 {page_count} 页: {url}")
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code != 200:
                print(f"⚠️ 状态码: {res.status_code}，停止抓取。")
                break

            soup = BeautifulSoup(res.text, "lxml")
            items = soup.find_all("div", class_="item")
            
            for item in items:
                try:
                    # 1. 获取标题
                    title_tag = item.find("li", class_="title").a
                    title = title_tag.text.strip()
                    link = title_tag['href']
                    
                    # 2. 获取封面图
                    img_tag = item.find("div", class_="pic").a.img
                    img_url = img_tag['src']
                    if "ipst" in img_url: img_url = img_url.replace("ipst", "spst")
                    elif "mpic" in img_url: img_url = img_url.replace("mpic", "lpic")

                    # 3. 【暴力核心】获取评分
                    # 直接把 item 这一大块 HTML 转成字符串，用正则搜 ratingX-t
                    # 豆瓣的类名通常是 "rating5-t", "rating4-t" 等
                    rating = 0
                    item_str = str(item)
                    match = re.search(r'rating(\d)-t', item_str)
                    if match:
                        rating = int(match.group(1))
                    
                    # 4. 获取短评
                    comment = ""
                    comment_tag = item.find("span", class_="comment")
                    if comment_tag:
                        comment = comment_tag.text.strip()
                    
                    # 调试输出：如果 title 是 "怦然心动"，打印一下它的评分，帮你确认
                    # if "怦然心动" in title:
                    #     print(f"   >>> 调试: 发现《{title}》，抓取到评分: {rating}")

                    data_list.append({
                        "title": title,
                        "link": link,
                        "cover": img_url,
                        "rating": rating,
                        "comment": comment
                    })
                except Exception as e:
                    print(f"解析出错: {e}")
                    continue

            next_span = soup.find("span", class_="next")
            if next_span and next_span.find("a"):
                next_link = next_span.find("a")['href']
                url = "https://" + media_type + ".douban.com" + next_link
                page_count += 1
                time.sleep(random.uniform(2, 4)) 
            else:
                url = None
                
        except Exception as e:
            print(f"❌ 错误: {e}")
            break
            
    return data_list

if __name__ == "__main__":
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    for t in TYPES:
        print(f"\n🚀 开始处理 {t}...")
        data = fetch_douban_data(t)
        if len(data) > 0:
            with open(f"{DATA_DIR}/{t}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"💾 {t} 已保存 {len(data)} 条。")
            
            # --- 自检报告 ---
            rated_count = sum(1 for x in data if x['rating'] > 0)
            print(f"📊 统计: 在这 {len(data)} 条记录中，有 {rated_count} 条是有评分的。")
            if rated_count == 0:
                print("⚠️ 警告: 所有记录评分都是 0。")
                print("👉 原因可能是：你只是点击了'看过'，但没有打星星（个人评分）。")