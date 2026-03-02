#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 产品经理作品集 - 真实 AI Demo
运行：python3 app.py
访问：http://localhost:7860
"""

import json
import urllib.request
import urllib.parse

# 配置你的 DashScope API Key
API_KEY = "sk-d997add3f630491ab11b0dd7d151130b"  # DashScope API Key
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

def call_llm(prompt, system_prompt="你是一名 AI 助手"):
    """调用通义千问大模型"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        req = urllib.request.Request(
            API_URL,
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['choices'][0]['message']['content']
    except Exception as e:
        return f"调用失败：{str(e)}"

def main():
    print("=" * 60)
    print("🤖 AI 产品经理作品集 - 真实 AI Demo")
    print("=" * 60)
    print("\n请选择 Demo 类型：")
    print("1. 学伴 AI - 学习助手（答题答疑）")
    print("2. 周报助手 - AI 生成周报")
    print("3. 搜索 AI - 智能答案生成")
    print("0. 退出")
    print()
    
    while True:
        choice = input("请输入选项 (0-3): ").strip()
        
        if choice == '0':
            print("再见！👋")
            break
        
        elif choice == '1':
            print("\n📚 学伴 AI - 学习助手")
            print("输入你的学习问题，AI 会帮你解答（输入 'q' 返回）")
            while True:
                question = input("\n你的问题：").strip()
                if question.lower() == 'q':
                    break
                if not question:
                    continue
                
                system_prompt = """你是一名专业的 AI 学习助手，帮助大学生解答课程问题。
要求：
1. 回答准确、清晰、有条理
2. 使用 Markdown 格式，重点内容加粗
3. 适当举例说明
4. 如果问题不完整，主动追问"""
                
                print("\n🤖 思考中...")
                answer = call_llm(question, system_prompt)
                print(f"\n{answer}")
        
        elif choice == '2':
            print("\n📝 周报助手 - AI 生成周报")
            print("输入本周工作内容，AI 会帮你生成周报（输入 'q' 返回）")
            while True:
                work = input("\n本周工作内容：").strip()
                if work.lower() == 'q':
                    break
                if not work:
                    continue
                
                system_prompt = """你是一名专业的职场写作助手，擅长撰写高质量周报。
根据用户输入的工作内容，生成结构化周报。
格式要求：
## 本周工作总结
- 完成事项 1（数据/成果）
- 完成事项 2（数据/成果）

## 遇到的问题与解决方案
- 问题 → 解决方案

## 下周工作计划
- 计划 1（预期成果）
- 计划 2（预期成果）

语言简洁专业，突出工作价值。"""
                
                print("\n🤖 生成中...")
                report = call_llm(f"请根据以下工作内容生成周报：\n{work}", system_prompt)
                print(f"\n{report}")
        
        elif choice == '3':
            print("\n🔍 搜索 AI - 智能答案生成")
            print("输入搜索词，AI 会生成结构化答案（输入 'q' 返回）")
            while True:
                query = input("\n搜索：").strip()
                if query.lower() == 'q':
                    break
                if not query:
                    continue
                
                system_prompt = """你是一名智能搜索助手，根据用户搜索词生成结构化答案。
要求：
1. 综合多方面信息，给出全面答案
2. 使用 Markdown 格式，结构清晰
3. 列出关键点和建议
4. 如果有争议，说明不同观点"""
                
                print("\n🤖 搜索中...")
                answer = call_llm(f"请详细解答：{query}", system_prompt)
                print(f"\n{answer}")
        
        else:
            print("无效选项，请重新输入")

if __name__ == "__main__":
    main()
