#!/bin/bash

# 步骤 1：添加所有修改的文件到暂存区
echo "🔍 正在添加所有修改的文件到Git暂存区..."
git add .

# 步骤 2：提交更改，支持自定义提交信息（不传参则使用默认值）
commit_msg=${1:-"导入旧博客文章"}  # 自定义提交信息优先级高于默认值
echo "📝 正在提交更改，提交信息：$commit_msg"
git commit -m "$commit_msg"

# 步骤 3：推送到远程仓库的main分支
echo "🚀 正在推送到origin main分支..."
git push origin main

# 部署完成提示
echo "✅ 部署完成！"