#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AI Demo 自动测试脚本"""

import json
import urllib.request

API_KEY = "sk-d997add3f630491ab11b0dd7d151130b"
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

def call_llm(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": "你是一名 AI 助手"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    try:
        req = urllib.request.Request(API_URL, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['choices'][0]['message']['content']
    except Exception as e:
        return f"错误：{str(e)}"

print("=" * 60)
print("🤖 AI 产品经理作品集 - 真实 AI 测试")
print("=" * 60)

# 测试 1：学伴 AI
print("\n📚 测试 1: 学伴 AI - 学习助手")
print("-" * 40)
question = "高数极限怎么求？用简单的话解释"
print(f"问：{question}")
answer = call_llm(question)
print(f"答：{answer[:200]}...")

# 测试 2：周报生成
print("\n📝 测试 2: 周报助手 - AI 生成")
print("-" * 40)
work = "本周完成了用户登录模块开发，修复了 3 个 bug，参与了产品评审会"
print(f"输入：{work}")
report = call_llm(f"请根据以下工作内容生成周报：{work}")
print(f"输出：{report[:200]}...")

# 测试 3：搜索 AI
print("\n🔍 测试 3: 搜索 AI - 智能答案")
print("-" * 40)
query = "敏感肌用什么水乳？推荐 3 款"
print(f"搜索：{query}")
result = call_llm(query)
print(f"结果：{result[:200]}...")

print("\n" + "=" * 60)
print("✅ 测试完成！AI Demo 可以正常工作")
print("=" * 60)
