#!/usr/bin/env python3
"""
测试微博热搜分析斜杠命令
直接运行此脚本测试命令功能

使用方法:
python test_weibo_command.py
"""

import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from weibo_analysis_command import main

if __name__ == "__main__":
    print("🚀 启动微博热搜分析斜杠命令测试")
    print("=" * 70)
    main()