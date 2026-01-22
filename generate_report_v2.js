const fs = require('fs');

// Use a fixed date for the report to match previous context or use current date
const now = new Date();
const year = now.getFullYear();
const month = String(now.getMonth() + 1).padStart(2, '0');
const day = String(now.getDate()).padStart(2, '0');
const dateStr = `${year}/${month}/${day}`;
const dateStrCompact = `${year}${month}${day}`;

const outputFile = `weibo_analysis_report_${dateStrCompact}.html`;

// The content is hardcoded based on the agent's analysis of the provided JSON data.
const reportData = {
    date: dateStr,
    reportTitle: "微博热搜深度分析",
    subtitle: "深度挖掘社交媒体趋势 · 洞察算法挑战权威 · 重塑底层生存逻辑",
    topics: [
        {
            title: "# 医生给1岁娃开小众药被AI提醒慎用",
            heat: "778,179",
            categoryColor: "#4facfe", // Tech Blue
            categoryBg: "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
            background: "<strong>信任危机：</strong> 一位母亲带1岁孩子看病，医生开具“人干扰素”雾化药。母亲不放心，咨询AI助手（蚂蚁阿福），AI提示该药在儿童群体临床数据有限，建议慎用。这引发了全网关于“听医生还是听AI”的激烈讨论。这也折射出患者利用AI填补医疗信息差的新常态。",
            analysis: [
                {
                    title: "权威的去中心化与算法挑战",
                    desc: "医疗、法律等传统高壁垒行业的“知识霸权”正在被AI瓦解。患者不再盲目迷信白大褂，而是手持算法工具进行“实时审计”。这种“人机对峙”将倒逼专业服务向更高透明度、更强解释性的方向进化。"
                },
                {
                    title: "第二诊疗意见的平权化",
                    desc: "过去“寻求第二诊疗意见”是中产以上阶层的特权，现在AI将其普及为一种零成本的基础权利。这种“防御性就医”心理的蔓延，标志着医患关系已从单纯的“托付”转向“博弈与合作”。"
                }
            ],
            ideas: [
                {
                    tag: "C端工具",
                    title: "处方审计师 (RxAuditor)",
                    desc: "一款面向患者的“用药安全卫士”App。拍照扫描处方，AI 实时比对 FDA/NMPA 数据库及最新临床文献，针对儿童、孕妇等特殊人群发出风险红绿灯预警，并翻译晦涩的药理机制为大白话。",
                    stack: "OCR + Medical Knowledge Graph + RAG"
                },
                {
                    tag: "医患沟通",
                    title: "医患对齐助手 (MediBridge)",
                    desc: "嵌入医生工作台的辅助工具。当医生开具“非共识”或“超说明书”用药时，系统自动生成“为何这样开”的循证医学解释话术，主动预判并化解患者（及其AI助手）的潜在质疑。",
                    stack: "Clinical Decision Support System (CDSS) + NLP"
                }
            ]
        },
        {
            title: "# 儿子回应怒吼癌症妈妈碰瓷爆火",
            heat: "1,076,529",
            categoryColor: "#FF4757", // Social Red
            categoryBg: "linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%)",
            background: "<strong>生存困境：</strong> 64岁患癌母亲为减轻儿子负担，瞒着家人碰瓷大货车讹钱。儿子赶到医院得知真相后，既心疼又愤怒地怒吼母亲“不要祸害别人”。事后儿子坚持退回部分捐款，维护了最后的尊严。该事件刺痛了无数网友关于底层大病家庭生存现状的神经。",
            analysis: [
                {
                    title: "道德与生存的极限拉扯",
                    desc: "母亲的“恶”（碰瓷）源于对儿子的“爱”（减负），儿子的“怒”（斥责）源于对“善”（底线）的坚守。这一悖论展示了极端经济压力通过扭曲人性来制造社会冲突的残酷机制，也揭示了“因病致贫”依然是社会最大的痛点。",

                },
                {
                    "title": "贫穷的尊严感",
                    "desc": "儿子拒绝过度捐款的行为，打破了传统“卖惨求助”的叙事逻辑。这说明即便是从困境中走出的人群，也依然渴望被平等看待而非单纯的怜悯。这种“有尊严的受助”是未来公益设计必须考虑的核心心理需求。"
                }
            ],
            ideas: [
                {
                    tag: "互助金融",
                    title: "尊严互助池 (DignityPool)",
                    desc: "基于区块链的去中心化互助保险平台。专注于“灾难性医疗支出”，采用“直接赔付给医院”模式，受助者无需公开隐私卖惨即可获得资金支持，保护受助人尊严，利用Smart Contract确保资金专款专用。",
                    stack: "Blockchain (DAO) + Smart Contracts"
                },
                {
                    tag: "公益科技",
                    title: "医疗众筹风控雷达 (CharityShield)",
                    desc: "针对大病众筹平台的反欺诈/反碰瓷系统。接入医院HIS系统与社保数据，自动核验病情真实性与家庭资产状况，为每一笔求助打上“信用分”，让真正的善意不被滥用，重建社会信任。",
                    stack: "Big Data Risk Control + Privacy Computing"
                }
            ]
        },
        {
            title: "# 用大寒节气打开冬日中国之美",
            heat: "598,206",
            categoryColor: "#a29bfe", // Culture Purple
            categoryBg: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            background: "<strong>文化回归：</strong> 大寒作为二十四节气之尾，成为冬日旅游和文化消费的新节点。从东北的冰雪温泉到南方的围炉煮茶，年轻人开始热衷于按照“节气”来规划生活仪式感。这不仅是旅游，更是一种对“顺时而动”的东方生活哲学的回归。",
            analysis: [
                {
                    title: "时间颗粒度重塑生活方式",
                    desc: "在原子化的工业时间（996/24h）压迫下，年轻人试图通过回归农业文明的“节气时间”（15天一轮）来寻找掌控感与喘息空间。节气不再是日历上的符号，而是具体的“生活指南”和“消费借口”。"
                },
                {
                    title: "极致寒冷的美学经济",
                    desc: "从哈尔滨的火爆到大寒温泉热，体现了后疫情时代人们对“强感官体验”的追求。越是极端（极冷/极热），越能带来脱离日常的疏离感及社交货币价值，催生了“苦寒美学”的商业化。",

                }
            ],
            ideas: [
                {
                    tag: "生活方式",
                    title: "时令生活家 (SeasonFlow)",
                    desc: "一款极简的“节气生活OS”。根据用户地理位置，精准推送当前节气（大寒）的“宜与忌”：宜喝什么汤、听什么曲、去哪里发呆。将宏大的节气文化拆解为每日可执行的微行动（Micro-Habits）。",
                    stack: "LBS + GenAI Content Generation"
                },
                {
                    tag: "新零售",
                    title: "二十四味快闪店 (24-Tastes)",
                    desc: "一个永远只卖“当季”商品的电商平台。每15天全站换品，大寒只卖糯米饭、消寒糕与暖手炉。过期即下架。利用“限时”的紧迫感与“顺时”的正当性，打造极致的垂直转化率。",
                    stack: "Niche E-commerce + Supply Chain Management"
                }
            ]
        }
    ]
};

let htmlTemplate = `<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${reportData.reportTitle} - ${reportData.date}</title>
    <link
        href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Noto+Sans+SC:wght@300;400;700&display=swap"
        rel="stylesheet">
    <style>
        :root {
            --primary: #FF4757;
            --secondary: #2F3542;
            --accent: #FFA502;
            --bg-dark: #0A0F1E;
            --card-bg: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(255, 255, 255, 0.1);
            --text-glow: rgba(255, 71, 87, 0.4);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', 'Noto Sans SC', sans-serif;
            background: var(--bg-dark);
            color: #E2E8F0;
            line-height: 1.6;
            overflow-x: hidden;
            background-image:
                radial-gradient(circle at 0% 0%, rgba(255, 71, 87, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 100% 100%, rgba(79, 172, 254, 0.08) 0%, transparent 50%);
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 60px 20px;
        }

        /* --- Header --- */
        header {
            text-align: center;
            margin-bottom: 80px;
            animation: fadeInDown 1s ease-out;
        }

        .date-chip {
            display: inline-block;
            background: rgba(255, 71, 87, 0.15);
            color: var(--primary);
            padding: 8px 24px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.9rem;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 71, 87, 0.3);
            letter-spacing: 2px;
        }

        h1 {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(to right, #FFF, #94A3B8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
            letter-spacing: -1px;
        }

        .subtitle {
            font-size: 1.1rem;
            color: #94A3B8;
            max-width: 600px;
            margin: 0 auto;
        }

        /* --- Topic Card --- */
        .topic-card {
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 32px;
            margin-bottom: 50px;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            animation: fadeInUp 0.8s ease-out both;
        }

        .topic-card:hover {
            transform: translateY(-8px);
            border-color: rgba(255, 255, 255, 0.2);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
        }

        .card-header {
            padding: 30px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--glass-border);
        }

        .topic-identity {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .category-tag {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            box-shadow: 0 0 10px currentColor;
        }

        .topic-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: #FFF;
        }

        .heat-score {
            font-family: 'Outfit';
            font-weight: 800;
            font-size: 1.2rem;
            color: var(--primary);
            text-shadow: 0 0 15px var(--text-glow);
        }

        .card-body {
            padding: 40px;
        }

        .section-label {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--accent);
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .section-label::after {
            content: '';
            height: 1px;
            flex-grow: 1;
            background: linear-gradient(to right, rgba(255, 165, 2, 0.3), transparent);
        }

        .content-block {
            margin-bottom: 40px;
        }

        .background-prose {
            color: #CBD5E1;
            font-size: 1rem;
            line-height: 1.8;
        }

        .analysis-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 20px;
        }

        .analysis-item {
            background: rgba(255, 255, 255, 0.02);
            padding: 20px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .analysis-item h4 {
            color: #FFF;
            margin-bottom: 10px;
            font-size: 1.1rem;
        }

        .analysis-item p {
            font-size: 0.9rem;
            color: #94A3B8;
        }

        /* --- Ideation Grid --- */
        .ideation-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }

        .idea-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.01) 100%);
            padding: 25px;
            border-radius: 20px;
            border: 1px solid var(--glass-border);
            position: relative;
            transition: 0.3s;
        }

        .idea-card:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: var(--primary);
        }

        .idea-card h5 {
            color: var(--primary);
            font-size: 1.2rem;
            margin-bottom: 12px;
        }

        .idea-tag {
            font-size: 0.7rem;
            background: rgba(255, 71, 87, 0.1);
            color: var(--primary);
            padding: 3px 10px;
            border-radius: 6px;
            margin-bottom: 15px;
            display: inline-block;
        }

        .idea-desc {
            font-size: 0.9rem;
            color: #E2E8F0;
            margin-bottom: 15px;
        }

        .tech-stack {
            font-size: 0.75rem;
            color: #64748B;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            padding-top: 12px;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        /* --- Footer --- */
        footer {
            text-align: center;
            padding-top: 100px;
            padding-bottom: 50px;
            color: #475569;
            font-size: 0.9rem;
        }

        /* --- Animations --- */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(40px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-40px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* --- Responsive --- */
        @media (max-width: 768px) {
            .analysis-grid {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 2.2rem;
            }

            .card-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 10px;
            }
        }
    </style>
</head>

<body>
    <div class="container">
        <header>
            <div class="date-chip">REPORT · ${reportData.date}</div>
            <h1>${reportData.reportTitle}</h1>
            <p class="subtitle">${reportData.subtitle}</p>
        </header>
`;

reportData.topics.forEach(topic => {
    htmlTemplate += `
        <!-- Topic -->
        <div class="topic-card">
            <div class="card-header">
                <div class="topic-identity">
                    <div class="category-tag" style="color: ${topic.categoryColor}; background: ${topic.categoryBg};"></div>
                    <span class="topic-title">${topic.title}</span>
                </div>
                <div class="heat-score">${topic.heat}</div>
            </div>
            <div class="card-body">
                <div class="content-block">
                    <div class="section-label">背景来龙去脉</div>
                    <div class="background-prose">
                        <p>${topic.background}</p>
                    </div>
                </div>

                <div class="content-block">
                    <div class="section-label">深度分析</div>
                    <div class="analysis-grid">
                        <div class="analysis-item">
                            <h4>${topic.analysis[0].title}</h4>
                            <p>${topic.analysis[0].desc}</p>
                        </div>
                        <div class="analysis-item">
                            <h4>${topic.analysis[1].title}</h4>
                            <p>${topic.analysis[1].desc}</p>
                        </div>
                    </div>
                </div>

                <div class="content-block">
                    <div class="section-label">软件产品创意</div>
                    <div class="ideation-grid">
                        <div class="idea-card">
                            <span class="idea-tag">${topic.ideas[0].tag}</span>
                            <h5>${topic.ideas[0].title}</h5>
                            <p class="idea-desc">${topic.ideas[0].desc}</p>
                            <div class="tech-stack">${topic.ideas[0].stack}</div>
                        </div>
                        <div class="idea-card">
                            <span class="idea-tag">${topic.ideas[1].tag}</span>
                            <h5>${topic.ideas[1].title}</h5>
                            <p class="idea-desc">${topic.ideas[1].desc}</p>
                            <div class="tech-stack">${topic.ideas[1].stack}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
});

htmlTemplate += `
        <!-- Social Sentiment Section -->
        <div class="topic-card"
            style="background: linear-gradient(135deg, rgba(255, 71, 87, 0.1) 0%, rgba(79, 172, 254, 0.1) 100%);">
            <div class="card-body">
                <div class="section-label">今日社会情绪综述</div>
                <div class="background-prose" style="font-size: 1.2rem; text-align: center; padding: 20px 0;">
                    <p>今日舆论场呈现出<strong>“权威祛魅、底层挣扎、文化避世”</strong>的混合光谱。</p>
                    <p style="font-size: 1rem; color: #94A3B8; margin-top: 15px;">
                        公众既在技术理性（AI问诊）中寻求对传统权威的反制，又在社会新闻（癌症母亲）的残酷中窥见生存的底色；最终，在传统节气（大寒）的仪式感中，寻找片刻的心灵宁静。</p>
                </div>
            </div>
        </div>

        <footer>
            <p>© 2026 微博热搜分析实验室 · 由 Antigravity 极致驱动</p>
            <p style="margin-top: 5px;">基于 ${new Date().toLocaleString()} 实时动态生成</p>
        </footer>
    </div>
</body>

</html>
`;

fs.writeFileSync(outputFile, htmlTemplate, 'utf8');
console.log(`Report generated: ${outputFile}`);
