#!/bin/bash

# 微博热搜产品创意分析工具 - 快速开始脚本

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║        微博热搜产品创意分析工具 - 快速开始                        ║"
echo "║        Weibo Hot Search Product Analysis Tool                  ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "📌 请选择操作："
echo ""
echo "  1. 预览API数据 (preview)"
echo "  2. 分析前5个话题 (analyze)"
echo "  3. 运行完整分析并生成HTML报告 (full)"
echo "  4. 查看README文档 (readme)"
echo "  5. 退出 (quit)"
echo ""
read -p "请输入选项 (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🔍 正在预览API数据..."
        python3 test_with_real_api.py preview
        ;;
    2)
        echo ""
        echo "🎯 正在分析前5个话题..."
        python3 test_with_real_api.py analyze
        ;;
    3)
        echo ""
        echo "🚀 正在运行完整分析..."
        python3 test_with_real_api.py full
        ;;
    4)
        echo ""
        echo "📖 正在打开README文档..."
        if command -v less &> /dev/null; then
            less README.md
        elif command -v cat &> /dev/null; then
            cat README.md
        else
            echo "请手动打开 README.md 文件"
        fi
        ;;
    5)
        echo ""
        echo "👋 感谢使用！"
        echo ""
        exit 0
        ;;
    *)
        echo "无效选项！"
        ;;
esac

echo ""
read -p "按 Enter 键继续..."
echo ""
bash "$0"
