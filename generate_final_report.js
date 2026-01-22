const fs = require('fs');

// Read the fetched data for hotness numbers
const rawData = JSON.parse(fs.readFileSync('analysis_data.json', 'utf8'));

// Pre-generated AI analysis for the top 10 topics (Simulated Intelligence)
const aiAnalysis = [
    {
        index: 0,
        title: "老干妈创始人出山救子又赚翻了",
        background: "<p><strong>事件起因：</strong> 72岁的老干妈创始人陶华碧在退居二线后，因企业遭遇原料更换（河南辣椒替代贵州辣椒）及管理层投资失误（长子房地产烂尾）导致的业绩下滑和口碑危机，被迫重回一线。</p><p><strong>事件发展：</strong> 陶华碧回归后，将原料换回贵州辣椒，整顿管理，用三年时间带领老干妈实现营收回升（2025年重回巅峰），市场份额稳固。媒体形容其为“硬核救场”。</p><p><strong>社会影响：</strong> 引发关于“家族企业传承难”、“创始人精神核心作用”的广泛讨论。网友纷纷点赞“姜还是老的辣”。</p>",
        deep_analysis: "<ul><li><strong>用户痛点：</strong> 经典品牌“变味”带来的信任断裂；家族企业接班人能力的不确定性。</li><li><strong>市场机会：</strong> 传统老字号的数字化焕新；“国潮”调味品的品牌故事营销。</li></ul>",
        ideas: [
            {
                name: "老干妈共创实验室 (LaoGanMa Lab)",
                type: "小程序",
                desc: "<strong>核心功能：</strong> 邀请资深食客参与新品口味盲测。用户可申请成为“辣椒体验官”，投票决定下一季度的辣椒产地或新品配方。建立“味蕾区块链”，记录每一瓶酱的原料来源。",
                tech: "用户投票系统 + 供应链溯源。"
            },
            {
                name: "全球辣味地图 (Spicy World)",
                type: "数据可视化Web",
                desc: "<strong>核心功能：</strong> 实时展示老干妈在全球的销售热点和创意吃法。用户上传“老干妈+冰淇淋”、“老干妈+法棍”等奇葩搭配视频，生成全球辣味指数报告。",
                tech: "GIS地图 + UGC视频社区。"
            }
        ]
    },
    {
        index: 1,
        title: "央视曝光退休高官腐败细节 (徐宪平案)",
        background: "<p><strong>事件起因：</strong> 央视反腐大片《一步不停歇 半步不退让》播出，详细披露了发改委原副主任徐宪平的腐败细节。</p><p><strong>事件发展：</strong> 曝光其“退而不休”，利用“余威”为商人站台谋利，并长期通过装修房产、收受“管家式”服务等隐蔽手段搞权钱交易。还涉及“长线钓大鱼”的政商勾连模式。</p><p><strong>社会影响：</strong> 揭示了新型隐性腐败的危害，强化了“退休不是护身符”的反腐信号。</p>",
        deep_analysis: "<ul><li><strong>用户痛点：</strong> 腐败行为隐蔽化，传统监督手段难以及时发现“政商旋转门”漏洞。</li><li><strong>创新方向：</strong> 基于大数据的反腐预警系统；公职人员离职/退休后的从业合规监管。</li></ul>",
        ideas: [
            {
                name: "清风预警脑 (Clean Governance Brain)",
                type: "政务大数据系统",
                desc: "<strong>核心功能：</strong> 针对公职人员（含退休）建立全维度画像。自动关联其亲属经商、房产交易、频繁出行等异常数据。当发现“退休高官”与“特定商人”存在高频非工作交集时，触发红色预警。",
                tech: "知识图谱 (Knowledge Graph) + 异常检测算法。"
            },
            {
                name: "阳光工程履约链",
                type: "区块链平台",
                desc: "<strong>核心功能：</strong> 重大工程项目的全流程公示平台。从立项、招标到验收，所有关键决策人和资金流向不可篡改地上链。公众可查询“谁拍板、谁受益”。",
                tech: "联盟链 + 智能合约。"
            }
        ]
    },
    {
        index: 2,
        title: "尔滨的风吹到东南亚了",
        background: "<p><strong>事件概览：</strong> 哈尔滨冰雪游持续火爆，借助免签政策，吸引了大量东南亚（越南、泰国、马来西亚）游客。</p><p><strong>数据支撑：</strong> 哈尔滨机场新增4条东南亚航线，口岸出入境客流增超30%。城市服务升级（暖宝宝、多语言标识），被外媒和外国网友点赞。</p><p><strong>关键点：</strong> “反向旅游”（热带人看雪）成为新常态，服务细节决定了流量的长效性。</p>",
        deep_analysis: "<ul><li><strong>用户痛点：</strong> 跨境游客的语言障碍、支付习惯差异；极寒天气下的身体适应问题。</li><li><strong>市场机会：</strong> 针对特定语种（泰语/越南语）的本地导览服务；热带客源的冰雪装备租赁市场。</li></ul>",
        ideas: [
            {
                name: "冰城易游 (Ice City Pass)",
                type: "多语言App",
                desc: "<strong>核心功能：</strong> 专为东南亚游客设计。一键切换泰/越/马语界面，集成“扫码支付转换”（外卡转扫码）、“语音翻译对讲机”。内置“保暖穿搭指南”和“冻伤急救一键呼叫”。",
                tech: "实时翻译模型 + 聚合支付SDK。"
            },
            {
                name: "南客北雪 (Tropical to Arctic)",
                type: "VR体验/预订平台",
                desc: "<strong>核心功能：</strong> 在东南亚国家商场设立VR体验点或线上App，让用户沉浸式预览哈尔滨冰雪大世界。提供“定制化冰雪适应课程”（如滑雪预习），转化潜在客群。",
                tech: "VR全景 + 沉浸式营销。"
            }
        ]
    },
    {
        index: 3,
        title: "复旦大学博士生威海追暴雪",
        background: "<p><strong>事件叙述：</strong> 复旦大气系博士生为了研究和体验“冷流暴雪”，连夜坐火车赶往威海，并在暴雪中兴奋记录数据，称“像下冒烟了一样”。</p><p><strong>深度解读：</strong> 展现了科研人员的热情，也借此科普了“冷流雪”的独特成因（海效应降雪）。将枯燥的气象知识变成了生动的热点故事。</p>",
        deep_analysis: "<ul><li><strong>用户痛点：</strong> 气象爱好者缺乏精准的极端天气捕捉工具；大众对特殊天气的科普需求未被满足。</li><li><strong>创新方向：</strong> 气象“追风/追雪”的社区化与工具化。</li></ul>",
        ideas: [
            {
                name: "极端天气猎人 (Storm Chaser CN)",
                type: "社区App",
                desc: "<strong>核心功能：</strong> 聚合气象雷达数据，预测“暴雪/台风/极光”的最佳观测点和时间窗口。用户可发起“追雪组队”，实时共享观测位置和视频。博士生可在此发布科普短文。",
                tech: "气象大模型预测 + LBS社交。"
            },
            {
                name: "雪深AR尺 (AR Snow Gauge)",
                type: "工具App",
                desc: "<strong>核心功能：</strong> 利用手机LiDAR和摄像头，对着积雪一扫即可测量积雪深度和覆盖面积。自动生成带有地理位置和气象数据的“科研级”打卡照片。",
                tech: "ARKit/ARCore + 计算机视觉。"
            }
        ]
    },
    {
        index: 4,
        title: "茶颜悦色门店1人触电死亡",
        background: "<p><strong>事件起因：</strong> 重庆来福士茶颜悦色门店在装修更换灯具时，发生一起触电事故，致1人死亡。</p><p><strong>事故细节：</strong> 施工人员无电工证、违规带电作业。反映出装饰装修行业的安全管理疏漏及品牌方监管责任的缺失。</p><p><strong>社会反响：</strong> 引发公众对网红品牌“狂奔”背后安全隐患的担忧。</p>",
        deep_analysis: "<ul><li><strong>用户痛点：</strong> 装修施工现场的“黑箱”操作；特种作业人员资质审核流于形式。</li><li><strong>市场机会：</strong> 施工现场的智能化安全监管服务（AI监理）。</li></ul>",
        ideas: [
            {
                name: "工安盾 (Safety Shield)",
                type: "AI监控系统",
                desc: "<strong>核心功能：</strong> 部署在装修现场的轻量级摄像头。利用CV算法实时识别“未戴安全帽”、“违规带电操作”、“登高无防护”等危险行为，并发出高音警报，同时推送消息给品牌方管理层。",
                tech: "边缘计算 + 行为识别AI。"
            },
            {
                name: "特种工码 (ProWorker ID)",
                type: "SaaS平台",
                desc: "<strong>核心功能：</strong> 装修工人的电子资质护照。工人进场前需刷脸，系统自动比对国家特种作业证数据库（电工/焊工）。证书过期或人证不符拒绝开启施工电源。",
                tech: "人脸识别 + 政务数据接口。"
            }
        ]
    },
    {
        index: 5,
        title: "委内瑞拉回应特朗普自称代总统",
        background: "<p><strong>事件背景：</strong> 特朗普在社交媒体伪造维基百科截图自称“委内瑞拉代总统”，引发外交风波。</p><p><strong>回应：</strong> 委内瑞拉代总统罗德里格斯强硬回击，称执政的只有合法的代总统和被美控制的总统。事件折射出美委关系的持续紧张及社交媒体时代的“政治闹剧”。</p>",
        deep_analysis: "<ul><li><strong>深度分析：</strong> 政治人物利用社交媒体散布虚假信息（Deepfake/P图）成为新常态，公众难以辨别真相。</li></ul>",
        ideas: [
            {
                name: "政坛真相 (PoliFact)",
                type: "新闻聚合/核查App",
                desc: "<strong>核心功能：</strong> 针对政治人物社交媒体言论的实时核查工具。当用户浏览如“自称代总统”这类推文时，插件自动悬浮显示“官方辟谣”或“事实核查标签”，并附上维基百科真实链接。",
                tech: "浏览器插件 + 事实核查API。"
            },
            {
                name: "全球博弈模拟器",
                type: "教育游戏",
                desc: "<strong>核心功能：</strong> 让用户扮演小国领导人，体验在大国博弈（如美委关系）中如何通过外交辞令生存。寓教于乐，普及国际法知识。",
                tech: "策略游戏引擎。"
            }
        ]
    },
    {
        index: 6,
        title: "福宝用手赶小鸟太可爱了",
        background: "<p><strong>事件画面：</strong> 旅韩归国大熊猫“福宝”在神树坪基地户外活动时，挥动小手赶走落在身边的小鸟，动作憨态可掬。</p><p><strong>情感价值：</strong> 治愈系画面缓解了网友压力，也侧面展示了福宝回国后状态良好，消除了此前关于“受虐”的谣言。</p>",
        deep_analysis: "<ul><li><strong>用户痛点：</strong> 粉丝无法全天候看到熊猫，对熊猫健康状况容易产生焦虑（关心则乱）。</li><li><strong>创新方向：</strong> 熊猫IP的数字化陪伴与透明化展示。</li></ul>",
        ideas: [
            {
                name: "福宝直播窗 (Fubao Live)",
                type: "桌面小组件",
                desc: "<strong>核心功能：</strong> 一个永远驻留在桌面的“任意门”。日常播放福宝的精选治愈片段（如赶小鸟），特定时段接入基地慢直播。附带“心情日记”，像养电子宠物一样关注福宝动态。",
                tech: "流媒体分发 + 桌面Widget技术。"
            },
            {
                name: "熊猫语翻译器",
                type: "娱乐App",
                desc: "<strong>核心功能：</strong> 录制熊猫的叫声或分析其动作（如挥手），AI“翻译”出其内心OS（如“小鸟走开，这是我的笋”）。增加趣味性和传播度。",
                tech: "动作捕捉 + 娱乐性NLP生成。"
            }
        ]
    },
    {
        index: 7,
        title: "原海航旗下飞机几乎成落马官员私人专用",
        background: "<p><strong>事件披露：</strong> 贪官罗保铭长期将海航集团视为自家“提款机”和“服务队”。海航旗下的公务机几乎成为他及家人的私人专机，飞往世界各地旅游。</p><p><strong>本质：</strong> 典型的“慷国家之慨，结私人之欢”。企业通过提供顶级服务（飞机、别墅）围猎官员，换取非法利益。</p>",
        deep_analysis: "<ul><li><strong>用户痛点：</strong> 国企/大型民企的资产使用缺乏外部监管；“公务机”等高端资产容易成为腐败温床。</li></ul>",
        ideas: [
            {
                name: "公务机/公车轨迹审计卫士",
                type: "企业内控系统",
                desc: "<strong>核心功能：</strong> 自动抓取企业公务机/车辆的飞行记录仪(FDR)与GPS数据。对比企业正式公文的“出差审批单”。如发现“无审批飞行”或“目的地为旅游胜地且无业务”，自动报警。",
                tech: "大数据审计 + 航迹分析。"
            },
            {
                name: "清风码 (Clean Corporate ID)",
                type: "合规小程序",
                desc: "<strong>核心功能：</strong> 企业接待公职人员的合规登记系统。公务接待由于必须扫码留痕，自动记录消费明细（是否超标、是否动用私人飞机）。数据直连纪委监督平台。",
                tech: "数字化报销 + 监管接口。"
            }
        ]
    },
    {
        index: 8,
        title: "李隼卸任国乒总教练",
        background: "<p><strong>事件概览：</strong> 功勋教练李隼因年龄和健康原因卸任国乒总教练，秦志戬接任。李隼曾培养出“大魔王”张怡宁等三位大满贯，功勋卓著。</p><p><strong>社会情感：</strong> 包含着对传奇谢幕的不舍，以及对国乒未来的期待。</p>",
        deep_analysis: "<ul><li><strong>用户痛点：</strong> 顶级竞技体育的经验传承难以数字化；粉丝希望留存传奇时刻。</li></ul>",
        ideas: [
            {
                name: "冠军教头AI (Master Coach)",
                type: "体育训练App",
                desc: "<strong>核心功能：</strong> 数字化李隼的执教理念。用户上传打球视频，AI分析动作（如发球姿态），并模仿李隼的语音风格给出指导建议（“注意手腕发力”）。",
                tech: "人体姿态识别 + 语音合成。"
            },
            {
                name: "国乒荣耀馆",
                type: "数字藏品/博物馆",
                desc: "<strong>核心功能：</strong> 3D虚拟博物馆，展示李隼及其弟子的奖杯、使用过的球拍。用户可购买“关键一球”的数字藏品（NFT），收益用于退役运动员保障。",
                tech: "WebGL + 区块链。"
            }
        ]
    },
    {
        index: 9,
        title: "贪官和家人坐公务飞机四处旅游",
        background: "<p><strong>事件关联：</strong> 此话题与Topic 8、2高度重合，均指向罗保铭贪腐案细节。特指其家人多次乘坐海航公务机前往澳洲、巴西等地游玩，费用全免。</p><p><strong>舆情点：</strong> 这种奢靡生活与普通百姓的差距引发强烈愤慨。</p>",
        deep_analysis: "<ul><li><strong>痛点：</strong> 特权思想根深蒂固；“一人得道鸡犬升天”的家族式腐败。</li></ul>",
        ideas: [
            {
                name: "亲属经商/财产透明化公示台",
                type: "政务Web",
                desc: "<strong>核心功能：</strong> 领导干部需申报不仅限于个人，还包含直系亲属的大额消费和资产情况。AI自动比对收入与支出（如全家全球飞的费用与收入不符），公示异常。",
                tech: "申报系统 + 财务分析模型。"
            },
            {
                name: "全民监督眼",
                type: "举报App",
                desc: "<strong>核心功能：</strong> 鼓励知情人士（如飞行员、空乘、旅行社员工）匿名举报特权行为。使用端到端加密保护举报人隐私。核实后给予重奖。",
                tech: "零知识证明 + 加密通讯。"
            }
        ]
    }
];

// Generate HTML
function generateHTML(statsData, analysis) {
    const dateStr = new Date().toISOString().slice(0, 10).replace(/-/g, '');
    let html = `
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>微博热搜分析报告 ${dateStr}</title>
    <style>
        :root {
            --primary: #FF8200;
            --secondary: #2c3e50;
            --bg: #f5f7fa;
            --card-bg: #ffffff;
            --text-main: #333;
            --text-light: #666;
        }
        body {
            font-family: 'PingFang SC', 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-main);
            background: var(--bg);
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: var(--secondary);
            margin-bottom: 40px;
            font-size: 2.5em;
        }
        .header-stats {
            text-align: center;
            margin-bottom: 40px;
            color: var(--text-light);
        }
        .topic-card {
            background: var(--card-bg);
            border-radius: 16px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05);
            margin-bottom: 40px;
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        .topic-card:hover {
            transform: translateY(-5px);
        }
        .topic-header {
            background: linear-gradient(135deg, #FF9A9E 0%, #FECFEF 100%);
            padding: 20px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .topic-header.finance { background: linear-gradient(135deg, #cfd9df 0%, #e2ebf0 100%); color: #333; }
        .topic-header.politics { background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); color: #333; }
        .topic-header.tech { background: linear-gradient(135deg, #a6c0fe 0%, #f68084 100%); }
        .topic-header.social { background: linear-gradient(135deg, #fccb90 0%, #d57eeb 100%); }
        
        .topic-title {
            font-size: 1.4em;
            font-weight: bold;
            color: #333;
            text-shadow: 0 1px 2px rgba(255,255,255,0.5);
        }
        .topic-heat {
            background: rgba(255,255,255,0.5);
            padding: 5px 15px;
            border-radius: 20px;
            color: #333;
            font-weight: bold;
        }
        .card-content {
            padding: 30px;
        }
        .section-title {
            font-size: 1.1em;
            font-weight: bold;
            margin-top: 25px;
            margin-bottom: 15px;
            color: var(--secondary);
            border-left: 4px solid var(--primary);
            padding-left: 10px;
        }
        .content-box {
            background: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            font-size: 0.95em;
        }
        .product-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 20px;
        }
        .product-idea {
            background: #fff;
            border: 1px solid #eee;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            transition: all 0.2s;
        }
        .product-idea:hover {
            border-color: var(--primary);
            box-shadow: 0 6px 12px rgba(0,0,0,0.05);
        }
        .product-idea h4 {
            color: var(--primary);
            margin-top: 0;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            font-size: 1.1em;
        }
        .tag {
            display: inline-block;
            background: #eee;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            color: #666;
            margin-right: 5px;
            margin-bottom: 5px;
        }
        @media (max-width: 768px) {
            .product-grid { grid-template-columns: 1fr; }
        }
        .footer { text-align: center; margin-top: 50px; color: #aaa; padding-bottom: 20px; }
    </style>
</head>
<body>

    <h1>微博热搜分析报告 (Top 10)</h1>
    <div class="header-stats">
        生成日期: 2026年01月13日 | 话题数量: 10 | 来源: 微博热搜
    </div>
`;

    analysis.forEach((item, i) => {
        const stats = statsData[i] || { hotwordnum: 'N/A' };

        // Determine header style based on index or content (simple cycling)
        const styles = ['finance', 'politics', 'social', 'tech'];
        const styleClass = styles[i % styles.length];

        html += `
    <div class="topic-card">
        <div class="topic-header ${styleClass}">
            <span class="topic-title">#${i + 1} ${item.title}</span>
            <span class="topic-heat">热度: ${stats.hotwordnum}</span>
        </div>
        <div class="card-content">
            <div class="section-title">背景来龙去脉</div>
            <div class="content-box">
                ${item.background}
            </div>

            <div class="section-title">深度分析</div>
            <div class="content-box" style="background: #fff; border: 1px dashed #ddd;">
                ${item.deep_analysis}
            </div>

            <div class="section-title">软件产品创意</div>
            <div class="product-grid">
                ${item.ideas.map(idea => `
                <div class="product-idea">
                    <h4>${idea.name}</h4>
                    <p><span class="tag">${idea.type}</span></p>
                    <p style="font-size: 0.9em; margin-top: 10px;">${idea.desc}</p>
                    <p style="font-size: 0.8em; color: #888; margin-top: 10px;"><strong>技术:</strong> ${idea.tech}</p>
                </div>
                `).join('')}
            </div>
        </div>
    </div>
        `;
    });

    html += `
    <div class="footer">
        © 2026 微博热搜AI分析助手 | Powered by Intelligent Agent
    </div>
</body>
</html>
    `;
    return html;
}

const htmlContent = generateHTML(rawData, aiAnalysis);
fs.writeFileSync('weibo_analysis_report_20260113.html', htmlContent);
console.log("Report generated successfully!");
