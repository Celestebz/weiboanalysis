import os
import glob
import shutil
from datetime import datetime, timedelta, timezone
import re

# ================= 配置区域 =================
# 本地报告目录 (会尝试自动识别)
POSSIBLE_REPORT_DIRS = ["weibo_products_report", "reports"]
OUTPUT_DIR = "public"
# ===========================================

def find_reports_dir():
    for d in POSSIBLE_REPORT_DIRS:
        if os.path.exists(d) and os.path.isdir(d):
            return d
    return None

def main():
    print("🚀 开始构建站点...")
    
    # 1. 准备目录
    reports_dir = find_reports_dir()
    if not reports_dir:
        print(f"❌ 未找到报告目录，请确认目录名为以下之一: {POSSIBLE_REPORT_DIRS}")
        return

    print(f"📂 报告源目录: {reports_dir}")
    
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    os.makedirs(os.path.join(OUTPUT_DIR, "reports"))

    # 2. 获取所有报告文件并排序
    all_reports = sorted(glob.glob(f"{reports_dir}/*.html"), key=os.path.getmtime, reverse=True)
    
    if not all_reports:
        print("❌ 目录中没有找到HTML报告文件")
        return

    latest_report_path = all_reports[0]
    print(f"✅ 最新报告: {os.path.basename(latest_report_path)}")

    # 3. 识别今天的报告 (用于下拉菜单)
    # 兼容两种时间格式: YYYYMMDD (20260101) 和 YYMMDD (260101)
    # 使用北京时间 (UTC+8)
    today = datetime.now(timezone.utc) + timedelta(hours=8)
    today_str_long = today.strftime("%Y%m%d")
    today_str_short = today.strftime("%y%m%d")
    
    todays_reports = []
    
    for r in all_reports:
        filename = os.path.basename(r)
        # 尝试提取日期
        match = re.search(r'(\d{6,8})', filename)
        if match:
            date_part = match.group(1)
            if date_part == today_str_long or date_part == today_str_short:
                todays_reports.append(r)

    # 4. 构建导航栏 HTML (包含最新的白底黑字按钮样式)
    dropdown_options = ""
    for r in todays_reports:
        fname = os.path.basename(r)
        # 解析时间显示
        time_label = "今日报告"
        # 尝试匹配 HHMM
        time_match = re.search(r'[-_](\d{4})\.html', fname)
        if time_match:
            hhmm = time_match.group(1)
            hour = int(hhmm[:2])
            min_str = hhmm[2:]
            period = "早报" if hour < 12 else "晚报"
            time_label = f"{hour}:{min_str} - {period}"
        
        dropdown_options += f'<option value="reports/{fname}">{time_label}</option>'

    navbar_html = f"""
    <style>
      #weibo-analysis-nav {{
          position: fixed; top: 0; left: 0; right: 0;
          height: 50px; 
          background: rgba(255, 255, 255, 0.95); 
          backdrop-filter: blur(12px);
          border-bottom: 1px solid rgba(0, 0, 0, 0.05);
          box-shadow: 0 2px 10px rgba(0,0,0,0.05);
          z-index: 9999; display: flex; align-items: center; justify-content: space-between;
          padding: 0 20px; font-family: 'Outfit', -apple-system, sans-serif;
      }}
      #weibo-analysis-nav .logo {{ font-weight: 700; font-size: 16px; color: #1e293b; display: flex; align-items: center; gap: 8px; }}
      #weibo-analysis-nav .actions {{ display: flex; align-items: center; gap: 15px; }}
      #weibo-analysis-nav select {{ 
          padding: 6px 16px; 
          border: 1px solid #e2e8f0; 
          border-radius: 20px; 
          font-size: 14px; 
          background: #f8fafc; 
          color: #334155;
          cursor: pointer;
          outline: none;
          transition: all 0.2s;
      }}
      #weibo-analysis-nav select:hover {{ border-color: #FF4757; background: #fff; }}
      
      #weibo-analysis-nav .archive-btn {{
          text-decoration: none; 
          color: #fff; 
          background: #1e293b;
          padding: 6px 20px; 
          border-radius: 20px; 
          font-size: 14px; 
          font-weight: 600;
          transition: all 0.2s;
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      }}
      #weibo-analysis-nav .archive-btn:hover {{ 
          transform: translateY(-1px); 
          background: #0f172a;
          box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
      }}
      body {{ padding-top: 80px !important; }}
    </style>
    <div id="weibo-analysis-nav">
        <div class="logo">
            <span>🔥</span> 微博热搜创意洞察
        </div>
        <div class="actions">
            <select onchange="if(this.value) location.href=this.value">
                <option value="" disabled selected>📅 切换分析报告...</option>
                {dropdown_options}
            </select>
            <a href="reports/index.html" class="archive-btn">📂 历史归档</a>
        </div>
    </div>
    """

    # 5. 生成 index.html (首页)
    try:
        with open(latest_report_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 注入导航栏
        if '<body' in content:
            content = re.sub(r'(<body[^>]*>)', r'\1' + navbar_html, content, count=1)
        else:
            content = navbar_html + content
            
        with open(os.path.join(OUTPUT_DIR, "index.html"), 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ 首页 index.html 生成完成")
    except Exception as e:
        print(f"⚠️ 生成首页失败: {e}")

    # 6. 复制文件并生成归档页
    archive_list_items = ""
    
    for r in all_reports:
        fname = os.path.basename(r)
        # 复制到 outputs/reports/
        shutil.copy(r, os.path.join(OUTPUT_DIR, "reports", fname))
        
        # 生成列表项
        date_display = fname
        match = re.search(r'(\d{6,8})', fname)
        if match:
            # 简单格式化日期
            d = match.group(1)
            if len(d) == 8: # 20260101
                date_display = f"{d[:4]}-{d[4:6]}-{d[6:]}"
            elif len(d) == 6: # 260101
                date_display = f"20{d[:2]}-{d[2:4]}-{d[4:]}"
                
            # 尝试提取时间
            t_match = re.search(r'[-_](\d{4})\.html', fname)
            if t_match:
                t = t_match.group(1)
                date_display += f" {t[:2]}:{t[2:]}"
        
        archive_list_items += f"""
        <li>
            <a href="{fname}">📄 {fname}</a>
            <span class="date">{date_display}</span>
        </li>
        """

    archive_html = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>历史归档 - 微博热搜创意洞察</title>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
        <style>
          :root {{
              --primary: #FF4757;
              --bg-dark: #0A0F1E;
              --card-bg: rgba(255, 255, 255, 0.03);
              --glass-border: rgba(255, 255, 255, 0.1);
              --text-main: #E2E8F0;
              --text-muted: #94A3B8;
          }}
          * {{ box-sizing: border-box; }}
          body {{ 
              font-family: 'Outfit', sans-serif; 
              background: var(--bg-dark); 
              color: var(--text-main);
              margin: 0; 
              padding: 40px 20px;
              min-height: 100vh;
              background-image:
                  radial-gradient(circle at 0% 0%, rgba(255, 71, 87, 0.08) 0%, transparent 50%),
                  radial-gradient(circle at 100% 100%, rgba(79, 172, 254, 0.08) 0%, transparent 50%);
          }}
          .container {{ 
              max-width: 800px; 
              margin: 0 auto; 
              background: var(--card-bg); 
              backdrop-filter: blur(20px);
              border: 1px solid var(--glass-border);
              border-radius: 24px; 
              overflow: hidden; 
              box-shadow: 0 20px 50px rgba(0,0,0,0.2);
              animation: fadeInUp 0.8s ease-out both;
          }}
          .header {{ 
              background: linear-gradient(135deg, rgba(255, 71, 87, 0.1) 0%, rgba(79, 172, 254, 0.1) 100%);
              padding: 40px; 
              text-align: center; 
              border-bottom: 1px solid var(--glass-border);
              position: relative;
          }}
          h1 {{ 
              margin: 0; 
              font-size: 2rem; 
              font-weight: 800;
              color: #FFF;
              text-shadow: 0 2px 10px rgba(0,0,0,0.2);
          }}
          ul {{ list-style: none; padding: 0; margin: 0; }}
          li {{ 
              padding: 20px 30px; 
              border-bottom: 1px solid var(--glass-border); 
              display: flex; 
              justify-content: space-between; 
              align-items: center;
              transition: all 0.2s;
          }}
          li:hover {{ background: rgba(255, 255, 255, 0.05); }}
          li a {{ 
              text-decoration: none; 
              color: var(--text-main); 
              font-weight: 500; 
              font-size: 1.1rem; 
              display: flex;
              align-items: center;
              gap: 10px;
          }}
          .date {{ color: var(--text-muted); font-size: 0.9rem; font-family: 'Outfit'; }}
          .back-btn {{ 
              display: block; 
              text-align: center; 
              padding: 25px; 
              color: var(--primary); 
              text-decoration: none; 
              font-weight: 600;
              border-top: 1px solid var(--glass-border);
              transition: background 0.3s;
          }}
          .back-btn:hover {{ background: rgba(255, 71, 87, 0.1); }}
          
          @keyframes fadeInUp {{
              from {{ opacity: 0; transform: translateY(20px); }}
              to {{ opacity: 1; transform: translateY(0); }}
          }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📂 历史报告归档</h1>
            </div>
            <ul>{archive_list_items}</ul>
            <a href="../" class="back-btn">← 返回最新报告</a>
        </div>
    </body>
    </html>
    """
    
    with open(os.path.join(OUTPUT_DIR, "reports", "index.html"), 'w', encoding='utf-8') as f:
        f.write(archive_html)
        
    print(f"✅ 归档页 reports/index.html 生成完成")
    print(f"\n🎉 站点已在 '{OUTPUT_DIR}' 目录生成，请双击打开 public/index.html 预览")

if __name__ == "__main__":
    main()
