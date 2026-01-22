@echo off
echo ================================
echo 微博热搜分析工具启动器
echo ================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误：未找到Python，请先安装Python 3.x
    echo.
    pause
    exit /b 1
)

echo ✅ Python环境检测成功
echo.
echo 🚀 启动微博热搜分析...
echo.
python weibo_analysis_command.py

echo.
echo ================================
echo 分析完成！
echo ================================
echo.
pause