# 微博热搜分析工具启动器
Write-Host "================================" -ForegroundColor Cyan
Write-Host "微博热搜分析工具启动器" -ForegroundColor Yellow
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# 检查Python是否安装
try {
    $pythonVersion = python --version 2>$null
    if ($pythonVersion) {
        Write-Host "✅ Python环境检测成功: $pythonVersion" -ForegroundColor Green
        Write-Host ""
        Write-Host "🚀 启动微博热搜分析..." -ForegroundColor Yellow
        Write-Host ""

        python weibo_analysis_command.py

        Write-Host ""
        Write-Host "================================" -        Write-Host "分析完成！" -ForegroundColor Cyan
ForegroundColor Yellow
        Write-Host "================================" -ForegroundColor Cyan
    } else {
        throw "Python not found"
    }
} catch {
    Write-Host "❌ 错误：未找到Python，请先安装Python 3.x" -ForegroundColor Red
    Write-Host ""
    Read-Host "按Enter键退出"
}

Read-Host "按Enter键退出"