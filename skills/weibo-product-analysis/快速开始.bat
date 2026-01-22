@echo off
chcp 65001 >nul
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║        微博热搜产品创意分析工具 - 快速开始                        ║
echo ║        Weibo Hot Search Product Analysis Tool                  ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo 📌 请选择操作：
echo.
echo   1. 预览API数据 (preview)
echo   2. 分析前5个话题 (analyze)
echo   3. 运行完整分析并生成HTML报告 (full)
echo   4. 查看README文档 (readme)
echo   5. 退出 (quit)
echo.
set /p choice=请输入选项 (1-5):

if "%choice%"=="1" goto preview
if "%choice%"=="2" goto analyze
if "%choice%"=="3" goto full
if "%choice%"=="4" goto readme
if "%choice%"=="5" goto quit
echo 无效选项！
pause
goto start

:preview
echo.
echo 🔍 正在预览API数据...
python test_with_real_api.py preview
pause
goto start

:analyze
echo.
echo 🎯 正在分析前5个话题...
python test_with_real_api.py analyze
pause
goto start

:full
echo.
echo 🚀 正在运行完整分析...
python test_with_real_api.py full
pause
goto start

:readme
echo.
echo 📖 正在打开README文档...
start README.md
goto start

:quit
echo.
echo 👋 感谢使用！
echo.
exit

:start
cls
goto :eof
