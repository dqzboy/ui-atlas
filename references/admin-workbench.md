# 清爽蓝白后台：工作台图表与完整概览

用于包含“工作台／运营概览／Dashboard”的后台，配合[逐页规范](admin-pages.md)、[组件规范](admin-components.md)、[设计基线](admin-design.md)及[动效规范](admin-motion.md)。已有[概览高清图](../assets/details/enterprise-workbenches/clean-admin-overview.webp)用于核对卡片、主图表和快捷卡；本文件补齐下方的状态进度环、对象对比和活动模块。截图只覆盖可见区域，不能据此删掉完整工作台的其余模块。

## 工作台的组合与业务映射

用户要求带工作台的后台时，默认按下列顺序组织，不只生成四张统计卡和空白占位。先从真实业务映射“数量、期间变化、互斥状态、完成比例、对象规模、最近事件、快捷动作”；有对应数据就接入相应模块，不把原示例的授权、设备、产品或日志名称强加给新项目。没有相关业务时省略该模块并说明映射原因，不能无声漏掉已经存在的数据视图。接口尚未接入时明确展示未接入／加载／空态，不能冒充已有统计；独立预览可使用明确的演示数据。

| 顺序 | 模块 | 几何与关键细节 |
|---|---|---|
| 1 | 页面头、大KPI | 按组件规范保留四色、每卡背景画与右上跳转入口，不能改成普通摘要 |
| 2 | 覆盖率／完成率细条 | min-height36、圆角11、padding8 16；左蓝色线框图标与说明、加重百分比、中间约180×5真实进度、右侧业务入口与小箭头 |
| 3 | 期间趋势＋生命周期分布 | 桌面1.55fr:1fr、gap18；左趋势图含图例、期间汇总与同步状态，右环图含总量及两侧状态值 |
| 4 | 三个状态进度环＋对象规模对比 | 桌面1.3fr:1fr、gap18；左三个独立比例环，右同类别双系列分组柱图，不能重复放一张生命周期环图 |
| 5 | 四个快捷业务入口 | 四等列、gap12、低白卡、14圆角、padding14 16；同风格扩展默认min-height76，36px浅色图标座、标题／说明、右侧小圆箭头 |
| 6 | 最近活动 | 白色16圆角面板；上方标题及数量，下面左侧淡紫摘要、右侧事件列表；无活动时保留明确空态 |

所有业务面板使用panel、line-soft、16圆角和轻阴影；图表白面或深色panel，绘图区透明。区块间18，手机14。标题14／600、panel header min-height58、padding18 22 10；手机标题13、header min-height56、padding16 16 8。页面自然滚动，不为了塞入一屏缩小全部图表。

## 图表的职责与视觉参数

### 期间趋势：线／面积与真实日期

默认用于最近一段时间的两条事件量趋势。横轴是真实日期、纵轴从0起且单位明确；窗口按产品确定，不能把“近14天”与周／月数据混用。第一系列蓝色4px实线，可有由44%到2%淡出的浅面积；第二系列青色3px虚线、dash5、不填面积。深色首段面积透明度可降到38%。无须绘制全部常驻点；hover显对应日期、两个系列的值和单位，不能靠颜色识别系列。

<a id="clean-admin-chart-tooltips"></a>

### 图表数值提示框：悬停、聚焦与触摸都能读到

趋势图、柱图、环图和有明确数据点的面积图都必须提供对应的数值提示。鼠标移到数据点、柱体或同一日期的绘图区时，以最近的有效数据点／共享横轴索引为准，同时显示该日期或分类、所有可见系列的名称、颜色标记、数值和单位；不能只显示鼠标最近的一条线，也不能只靠图例和纵轴让用户自己估算。趋势图可显示一条与x索引对齐的细竖向引导线，并对当前点加小圆点或轻微高亮，不能改变数据本身。

提示框沿用页面面板主题：白色主题使用panel面、line-soft边、12px圆角和轻阴影；深色使用同一组件token映射到深色panel、line和text。标题日期14px／650，行高26左右；每行是7–8px系列色标、系列名12px和右对齐13px／650数值，单位跟在数值后且不依赖颜色。小三角指向当前真实数据锚点，提示框优先放在点的上方或侧上方；按下方尖端间距合同定位，不能按图表外壳或额外顶留白定位。靠近边缘时翻转或在可见边界内平移，箭头同步回指锚点；不能被panel的padding、圆角或页面边界裁切。提示框不参与图表布局，不造成页面跳动，不遮住当前点；interactive tooltip若包含链接才允许pointer-events:auto，否则保持none并由图表事件控制。

#### 箭头根部与正文无接缝

小三角与提示框必须是一整块气泡：同一panel底色连续相接，**根部不允许有提示框横向／纵向边框线穿过**，不出现三角形底边、白缝、双描边或独立贴上的小菱形。提示框外框与箭头两条外斜边可保留同色1px细轮廓；禁止的是箭头与正文之间的内部隔线，不是要求去掉整圈外轮廓。

下方示例用外层三角延续轮廓，内层三角向正文内重叠2px并保留一小段平直填充，覆盖穿过根部的那段正文边框；四个方向翻转时遮盖段也必须同步转向。不能只把三角放到框外相邻位置，不能靠移除整条底边／顶边掩盖，也不要用固定白色补丁盖深色气泡。已有组件库优先调整其arrow内层／伪元素和背景变量，不叠加第二个箭头。

浅深主题、上下左右方向、非整数位置、DPR1／2和浏览器缩放时实际放大核对连接处：内部底色连续，根部无穿线；外斜边自然接上正文边框，仍保持7px突出高度和到图形默认6px的间距。箭头无接缝与动态锚点、近图定位须同时满足。

#### 尖端与可见图形之间的距离

分布环图、细进度环、折线点和柱体提示均适用：**箭头尖端到实际可见图形边缘默认6px，正常允许4–8px**，单位为CSS px。不是提示框正文底边到图形6px，也不是箭头到整个SVG／canvas／卡片边缘6px；阴影不计入间距。不能让箭头与圆环之间出现数十像素空档，不能把面板padding、库内置offset和额外translateY重复相加。

- 环图／进度环的整体汇总放在上方时，锚点取可见圆环最上缘，即中心cy减实际外半径（SVG描边圆为r加stroke-width/2）；不取圆心、容器顶部或中心数字。扇区专属提示指向该扇区真实外弧锚点，随扇区方向选择侧边或上／下方，不为了统一居中而指向另一段弧；hover偏移和放大需计入实际外缘。
- 折线以当前点的可见标记边缘为准；柱图以当前柱顶／柱边为准。共享横轴提示保留同日期完整系列，其锚点与引导线及当前点一致，不锚到面板标题或图例。
- 提示内容更新后先测量实际宽高，再定位。上置正文top = 锚点y − 6 − 箭头突出高度 − 提示框实测高度；下置正文top = 锚点y + 6 + 箭头突出高度。本节三角突出高度为7px，不能又在CSS margin或库offset里再扣一次；库offset若从正文边界计算则传入13px，若从箭头尖端计算则传入6px，按该库实际定义核对。
- 统一坐标系：SVG数据点经getScreenCTM转为视口CSS坐标，canvas坐标按绘制区域与client rect比例转换；portal到body按视口／页面定位策略转换，局部absolute再减实际定位父级原点。DPR、页面滚动和缩放只换算一次，不把设备像素直接当CSS px。
- 上方放不下就翻到下方或侧边，不能把框留在原处、只移动箭头。左右平移避边时重新计算箭头位置，避开12px圆角并指向原锚点；四向placement与箭头方向同一状态驱动。沿用可靠图表／浮层库的offset、flip、shift、arrow能力，不叠第二套定位；CSS anchor的方向查询只在支持时使用，不支持时由宿主最终placement同步箭头，无法可靠回指时隐藏装饰箭头而保留可读提示。不得回退成居中悬空提示框。

#### 柱图与折线：位置随当前数据高度变化

**提示框的纵坐标必须由当前激活数据的实际绘制位置计算，不能固定在图表顶部。**仅随鼠标或分类索引改横坐标、仅替换内容但保留同一个top，都属于错误。鼠标悬停在矮柱、键盘移动到小值或触摸点按低值分类时，正文和箭头必须一起下移，保持上述6px尖端间距；不能让同一组提示全部停在最高柱对应的高度。这里跟随的是当前柱顶／数据点，不是整张图表的容器高度，也不是鼠标在柱子内部的任意y坐标。

| 图表／模式 | 动态锚点的计算口径 |
|---|---|
| 单系列竖柱 | 当前柱远离零基线的可见端点，x取柱中心；正值通常上置、负值通常下置。不要把负柱上方零基线误当数据末端 |
| 分组柱共享分类提示 | 内容列该分类所有可见系列；正值上置时取该组可见柱体中实际y最小的柱顶，x取产生该端点的柱中心。柱高相同则优先当前命中柱，键盘按稳定系列顺序；正文可向分类中心对齐，但箭头仍回指真实柱顶。不是取全图最大值，也不是取首个分类的高度 |
| 隐藏系列／混合正负 | 只用仍可见且有有效数据的图形计算锚点；改变图例可见性后重新定位。混合正负共享提示以实际激活柱端为准，其余系列只补充内容；没有明确激活柱时选最近的有效端点并高亮，不套全图最高处 |
| 堆叠／横向柱 | 堆叠单项取当前段暴露端，共享合计取当前分类的可见堆叠外缘；横柱按实际条末端和左右方向定位。取最终绘制几何，不用单段原始数值当堆叠总高度 |
| 折线／面积共享日期 | 锚到当前高亮点的实际像素位置，内容仍保留该日期所有可见系列；索引变化时x、y同时更新。切换到低点时随之下移，不能钉在整张图的顶部 |
| 0值／缺失值 | 真实0值可以锚到该分类的零基线并清楚显示0；缺失值不转换成0。当前分类完全无有效数据时呈现无数据反馈或隐藏数值提示，不复用上一个分类的锚点 |

优先使用现有图表库的激活元素、最终bar rect／point、scale映射和tooltip position回调；不要按截图比例、固定图表高度减常数或缓存上一次分类的y。独立实现时，先取当前索引对应的可见几何与坐标变换，更新文案并测量提示框，再按“锚点 − 间距 − 箭头高度 − 提示框高度”计算位置。每次hover分类／键盘索引／触摸选点、数据或过滤条件变化、图例隐藏／显示、坐标轴范围变化、resize及滚动后均重算；图形仍有入场动画时读取当帧几何，或等稳定后显示，不在动画起点冻结提示。快速移动取消旧定位任务，不能让迟到的回调把新分类提示拉回旧高度。

验收至少连续操作“高柱→中柱→接近零的矮柱→高柱”，确认内容、激活高亮、箭头和正文在同一更新中对应当前分类；切换后逐项实测尖端间距。再检查同组柱高不等、隐藏最高系列、0值、负值／堆叠（产品存在时）、调整图表高度与坐标轴范围；适用场景中不得保留固定top、首项高度或全图最大值高度。上述动态验收与下方通用间距验收同时执行。

实际渲染验收时测量**三角尖端到圆环／柱体／点标记可见边缘**，不能只检查offset配置。分布环和细环分别检查粗细、尺寸变化、非100%扇区、上／下／侧向避让、长内容、浅深主题、滚动、resize、390宽和200%缩放；定位后不遮挡当前数据和键盘焦点、不裁切，提示框不改变图表布局。只有截图和操作验证过的场景才标为已验证。

```html
<div class="admin-chart" data-chart-id="storage-publish-trend">
  <div class="admin-chart__plot" role="img"
    aria-label="内容保存与发布趋势，2026年11月27日草稿保存1次、内容发布1次">
    <!-- 图表库或SVG/canvas绘图区 -->
  </div>
  <div class="admin-chart-tooltip" role="status" aria-live="polite" hidden>
    <strong class="admin-chart-tooltip__title">2026-11-27</strong>
    <div class="admin-chart-tooltip__row"><i data-tone="blue"></i><span>草稿保存</span><b>1 <small>次</small></b></div>
    <div class="admin-chart-tooltip__row"><i data-tone="cyan"></i><span>内容发布</span><b>1 <small>次</small></b></div>
  </div>
</div>
```

```css
.admin-chart { position:relative; min-inline-size:0; }
.admin-chart__plot { position:relative; min-block-size:232px; }
.admin-chart-tooltip { position:absolute; z-index:3; inline-size:max-content; max-inline-size:min(240px,calc(100% - 16px));
  padding:10px 12px; border:1px solid var(--line-soft); border-radius:12px; background:var(--panel);
  color:var(--text); box-shadow:0 8px 24px rgb(38 73 126 / .14); pointer-events:none; }
.admin-chart-tooltip { --tooltip-gap:6px; --tooltip-arrow-height:7px; --tooltip-arrow-base:12px; }
.admin-chart-tooltip::before,.admin-chart-tooltip::after { content:""; position:absolute; pointer-events:none;
  inset-block-start:calc(100% + 1px); inset-inline-start:var(--tooltip-arrow,50%);
  inline-size:var(--tooltip-arrow-base); block-size:var(--tooltip-arrow-height);
  clip-path:polygon(0 0,100% 0,50% 100%); transform:translateX(-50%); background:var(--line-soft); }
.admin-chart-tooltip::after { inset-block-start:calc(100% - 1px);
  inline-size:calc(var(--tooltip-arrow-base) - 2px); block-size:calc(var(--tooltip-arrow-height) + 1px);
  clip-path:polygon(0 0,100% 0,100% 2px,50% 100%,0 2px); background:var(--panel); } /* 平直填充跨过1px边框，不留根部横线 */
.admin-chart-tooltip[data-placement="bottom"]::before,
.admin-chart-tooltip[data-placement="bottom"]::after { inset-block-start:auto; inset-block-end:calc(100% + 1px);
  clip-path:polygon(50% 0,100% 100%,0 100%); }
.admin-chart-tooltip[data-placement="bottom"]::after { inset-block-end:calc(100% - 1px);
  clip-path:polygon(50% 0,100% calc(100% - 2px),100% 100%,0 100%,0 calc(100% - 2px)); }
.admin-chart-tooltip:is([data-placement="left"],[data-placement="right"])::before,
.admin-chart-tooltip:is([data-placement="left"],[data-placement="right"])::after {
  inset-block-start:var(--tooltip-arrow-y,50%); inset-block-end:auto;
  inline-size:var(--tooltip-arrow-height); block-size:var(--tooltip-arrow-base); transform:translateY(-50%); }
.admin-chart-tooltip[data-placement="left"]::before,
.admin-chart-tooltip[data-placement="left"]::after { inset-inline-start:calc(100% + 1px); inset-inline-end:auto;
  clip-path:polygon(0 0,100% 50%,0 100%); }
.admin-chart-tooltip[data-placement="left"]::after { inset-inline-start:calc(100% - 1px);
  inline-size:calc(var(--tooltip-arrow-height) + 1px); block-size:calc(var(--tooltip-arrow-base) - 2px);
  clip-path:polygon(0 0,2px 0,100% 50%,2px 100%,0 100%); }
.admin-chart-tooltip[data-placement="right"]::before,
.admin-chart-tooltip[data-placement="right"]::after { inset-inline-start:auto; inset-inline-end:calc(100% + 1px);
  clip-path:polygon(100% 0,100% 100%,0 50%); }
.admin-chart-tooltip[data-placement="right"]::after { inset-inline-end:calc(100% - 1px);
  inline-size:calc(var(--tooltip-arrow-height) + 1px); block-size:calc(var(--tooltip-arrow-base) - 2px);
  clip-path:polygon(0 50%,calc(100% - 2px) 0,100% 0,100% 100%,calc(100% - 2px) 100%); }
.admin-chart-tooltip[data-arrow="hidden"]::before,
.admin-chart-tooltip[data-arrow="hidden"]::after { content:none; }
.admin-chart-tooltip__title { display:block; margin-block-end:4px; font:650 14px/1.35 var(--sans); font-variant-numeric:tabular-nums; }
.admin-chart-tooltip__row { display:grid; grid-template-columns:8px minmax(0,1fr) auto; align-items:center; gap:7px; min-block-size:26px;
  font:400 12px/1.4 var(--sans); }
.admin-chart-tooltip__row i { inline-size:7px; block-size:7px; border-radius:50%; background:var(--tooltip-tone,var(--accent)); }
.admin-chart-tooltip__row i[data-tone="blue"] { --tooltip-tone:var(--chart-license); }
.admin-chart-tooltip__row i[data-tone="cyan"] { --tooltip-tone:var(--chart-activation); border-radius:1px; }
.admin-chart-tooltip__row b { font:650 13px/1.4 var(--sans); font-variant-numeric:tabular-nums; white-space:nowrap; }
.admin-chart-tooltip__row small { color:var(--muted); font:400 11px/1.4 var(--sans); }
@media(prefers-reduced-motion:reduce) { .admin-chart-tooltip { transition:none; } }
```

提示框由真实图表状态驱动：进入数据点后立即更新内容，离开绘图区隐藏，快速移动时取消上一点的延迟／定位任务；不使用定时器伪造数值，不在数据尚未到达时显示0。图表库若提供axis／index tooltip，优先使用它并映射上述token，同时将位置绑定当前激活几何，不能沿用固定顶部position；自绘SVG或canvas需要维护x索引到日期和系列的稳定映射。提示框内容必须与图下摘要、图例和无障碍文本使用同一数据源，格式化后保留真实精度和单位。

键盘不能依赖鼠标：给图表提供可聚焦的数据点／日期列表、等价文本表格或图表库已有键盘导航；左右键切换日期并更新同一提示框，Home／End跳到首尾，Escape关闭。触摸设备第一次点按数据区域显示并锁定提示框，第二次点按其他点更新，点击空白处或关闭按钮收起；没有可操作点时至少提供“查看数据表”入口。提示框的`aria-live`不要在指针移动每一帧重复播报，键盘或锁定后的数据变化才礼貌更新；`role=img`的静态摘要仍需包含图表结论。

面板右上独立小图例：第一系列8px空心圆、第二系列8px空心圆角方块、文字10–12。绘图区桌面高246、左右18内边距，手机高232、左右6；日期文字10、最多约4档整数纵轴，避免密集交叉标签。趋势图可采用浅竖网格；柱图采用浅水平虚线网格，不把所有图强行设成同一网格。

底部min-height46、padding0 22 12：两个期间汇总，分别带蓝／青小标记、说明10与数值16／600；末尾有实际更新时间或同步状态。自动刷新间隔来自目标产品，不复制截图中的固定秒数；失败保留旧图、说明失败和更新时间。趋势为空时保留标题和底部真实汇总，用约28px线框图标、短标题、两行以内说明及38px有效下一步操作替换绘图区，不能凭空画平滑曲线。

已有参考图中的柱状展示说明卡片密度，不代表所有时间趋势都应转成分类柱图。时间趋势和对象规模对比分别映射真实数据语义。

### 生命周期环图：一个总量的互斥分布

左标签／中间环／右标签布局，桌面列为minmax(56px,1fr) minmax(140px,2.1fr) minmax(56px,1fr)，gap6、padding14 18 18、内容min-height287。环容器最大宽230、高240，数据环无3D／挤出／爆炸；中心总数29／600、说明12。两侧状态数值21／500、状态10、比例9、6px色点，不把小分类文字压到圆环上。

状态顺序与颜色通过稳定key映射，默认蓝、薄荷、橙、紫、玫粉；顺序变化不换色，真实业务语义优先。环内总量必须等于互斥分项之和，比例来自同一个分母。分类重叠时用条形等合适图，不硬做部分之和。0值状态可以在标签中显示0，不强加可见扇区；全部0时显示暂无数据，不画100%彩环。百分比四舍五入时允许显示和为99／101，不能改真实数值凑100。

≤1280改为独占一行，可用minmax(56px,1fr) minmax(180px,2fr) minmax(56px,1fr)，环最大260、高240，左右padding40。≤600环高210、中心数24，状态数19；长标签改为环下可换行图例，不缩小到不可读或裁掉状态。

### 状态速览：三个独立的细进度环

用于三个各有分母的比例，如任务完成、资源启用、版本发布；这些比例可以来自不同总量，不能误加成一个生命周期环图。三等列、gap18、padding30 24 22；环宽min(100%,148px)、1:1。SVG viewBox 0 0 120 120，圆心60／60、r51、线宽6，进度圆端，从12点方向开始；轨道使用该环颜色10%混panel。三个环默认蓝／薄荷／橙。

中心是**业务数量＋单位**，桌面28／500、单位10，下面12／500标签与8px空心色点，再下面10px“占比 · 总量”；不能只放一个大百分比而丢掉数量和统计口径。三个环下有12px线框说明图标及10px口径文字。ratio=clamp(value/total,0,1)，周长=2π×51，dashoffset=周长×(1−ratio)；total≤0时不除零、不显示完成，文本为暂无数据。value超出total时图形可钳制，但真实值保留并报告口径不一致。

```html
<!-- 示例45/60：数量、分母、文案与offset必须由同一真实数据计算。 -->
<div class="admin-status-ring" style="--ring-color:var(--chart-mint)">
  <div class="admin-status-ring__figure" role="img" aria-label="已完成任务45项，共60项，占75%">
    <svg viewBox="0 0 120 120" aria-hidden="true">
      <circle class="admin-status-ring__track" cx="60" cy="60" r="51" />
      <circle class="admin-status-ring__value" cx="60" cy="60" r="51"
        stroke-dasharray="320.44245" stroke-dashoffset="80.11061" />
    </svg>
    <div class="admin-status-ring__number"><span>45</span><small>项</small></div>
  </div>
  <b>已完成任务</b><span>占总量75% · 共60项</span>
</div>
```

```css
.admin-status-ring { display:flex; flex-direction:column; align-items:center; min-inline-size:0; text-align:center; }
.admin-status-ring__figure { position:relative; inline-size:min(100%,148px); aspect-ratio:1; }
.admin-status-ring svg { display:block; inline-size:100%; block-size:100%; transform:rotate(-90deg); }
.admin-status-ring circle { fill:none; stroke-width:6; }
.admin-status-ring__track { stroke:color-mix(in srgb,var(--ring-color) 10%,var(--panel)); }
.admin-status-ring__value { stroke:var(--ring-color); stroke-linecap:round;
  transition:stroke-dashoffset 400ms cubic-bezier(.2,.75,.25,1); }
.admin-status-ring__number { position:absolute; inset:0; display:flex; align-items:center; justify-content:center;
  gap:3px; color:var(--text); font:500 28px var(--sans); font-variant-numeric:tabular-nums; }
.admin-status-ring__number small { margin-block-start:5px; color:var(--muted); font-size:10px; }
.admin-status-ring > b { display:inline-flex; align-items:center; gap:6px; margin-block-start:12px;
  color:var(--text-soft); font:500 12px/1.5 var(--sans); }
.admin-status-ring > b::before { content:""; inline-size:8px; block-size:8px;
  border:2px solid var(--ring-color); border-radius:50%; }
.admin-status-ring > span { margin-block-start:8px; color:var(--muted); font:400 10px/1.6 var(--sans); }
@media(max-width:600px) {
  .admin-status-ring__number { font-size:23px; }
  .admin-status-ring > b { font-size:10px; } .admin-status-ring > span { font-size:9px; }
}
@media(prefers-reduced-motion:reduce) { .admin-status-ring__value { transition:none; } }
```

数值更新时沿用400ms dashoffset过渡，减少动态时直接更新；不每次轮询从0重放。静态环使用role=img与完整可访问名称，只有实际有导航任务时才增加独立链接，不把每个环都做成不可解释的可点区域。

### 对象规模对比：分组柱图

用于项目、产品、团队等同一分类下两个可比的计数系列，蓝＋薄荷并列，不堆叠，不用平滑面积替代。右上保留真实“管理对象”入口；图例是7×7小色块、10px文字、gap14，注明系列单位，显示TOP N时说明排序口径。类别名称可截断但需提供完整名称；横轴类别不能与趋势日期混用。纵轴从0、约4档、浅水平虚线；柱体清楚分组且保留组间空隙，局部圆角而非胶囊，不能放满整格。

图下10px汇总展示对象数及两系列总量，gap12、分隔小点；筛选、时间范围、单位和汇总口径一致。两个系列不同单位且量级不可直接比较时分图或明确双轴，不能为了复刻外观悄悄共用一个误导纵轴。复用目标项目已有图表库；本规范不要求安装特定库。

## 快捷卡、空态和活动里的小图标

快捷卡按产品／对象、创建／签发、核验／设备、发布／交付等真实职责分别选择同一套线框图标，不能四个都用相同箭头或emoji。36×36底座、圆角11、图标约18；四卡可用蓝／绿／青／棕弱色面区分。右侧小圆箭头与KPI右上入口是不同尺寸职责。hover图标rotate(−7deg) scale(1.08)、260ms spring，右箭头右移3px／220ms，卡片轻上移2px；键盘同样可进入动作，禁用不动且有原因。

空趋势用图表类线框图标，空分布用该业务对象图标，创建按钮内是16px加号；底部统计用蓝／青小点或菱形，同步信息用绿色小点，统计口径用12px说明／锁形图标。图例、图标和文字一起表达含义，不能把这些位置全部用普通圆点代替。

最近活动面板：左摘要与右列表列比minmax(220px,.75fr) minmax(0,2fr)，gap18、padding4 20 20。左面板淡紫渐变、lilac细边、圆角14、padding24，有蓝色小状态点、最近时间、简短业务说明及右下半透明越界环。右列表每行min-height47、列为28px minmax(0,1fr) auto、gap10、底细线；25px浅色事件图标底座，标题12／650、说明12、右侧9px等宽时间小胶囊，蓝字浅蓝底。成功、警告、失败分别使用匹配的事件图标和语义色，不能全部伪装为成功。

事件来自实际数据；默认最多6条，可连接日志／活动详情，长说明可查看完整内容。空列表显示图标、标题与短说明；未知数量不显示虚假0。小屏摘要上移、列表单列，时间可移到正文下方而保留信息。截图中的仓库地址、账号、任务名和运行细节不作为演示数据写入新项目。

## 响应式、数据更新与验收

≤1280两排主图均改为单列；≤960快捷卡两列、侧栏按全局抽屉规则；≤600区块gap14、三环gap8／padding18 12 14。三环标签放不下时先换行，再按容器改一列，不隐藏某个指标。活动列表与图例保留可读性，不给body设置overflow-x:hidden。

图表挂载前容器必须有非零宽高；主题、容器尺寸、筛选及数据更新后同步更新图表，路由离开销毁实例和观察器。首次运营数据优先直接展示，不补长时间绘制／轮播；刷新保留旧图而非闪空。提示框随主题，触屏和键盘能获得数值，另提供文本摘要或等价数据表。不要只保留canvas图形而丢掉统计值。

交付前核对：两排图表及最近活动是否因只看首屏被漏掉；趋势／状态分布／三个比例／分类对比是否各自使用正确数据；汇总能否核对；0与未知是否区分；鼠标悬停／键盘左右键／触摸点按是否显示同一日期或分类的完整数值提示，提示框是否避让边缘、随主题、无裁切、无布局跳动，分布环与细进度环箭头尖端到实际外缘是否为4–8px且默认6px、翻转后是否仍回指锚点，柱图／折线高低值切换时是否同步更新x与y而非固定top；图例形状、系列颜色、快捷入口图标和有效动作是否齐全；390宽度、深色、空／错／刷新及reduced-motion是否可用。没有运行图表时注明未验证，不用静态SVG预览冒充真实数据联动验证。

## 可直接执行的工作台提示词

```text
按ui-atlas清爽蓝白后台实现本项目工作台。先读admin-design、admin-components
的侧栏和大KPI合同，再执行本文件。除页面头、四色KPI及细覆盖率条外，还要
映射真实业务的期间趋势/生命周期分布、三个状态进度环/对象分组柱状对比、
四个带不同线框图标的快捷卡和最近活动。不要只看首屏图便省掉下方模块。
两排图表桌面分别1.55:1和1.3:1，白色16圆角面板、gap18；1280以下单列。
保留蓝/青双趋势及图例和底部汇总、中心总量及两侧状态的环图、蓝/薄荷/橙
三个细进度环的数量/单位/比例/总量、蓝/薄荷分组柱图的对象标签与真实入口。
趋势为空用线框图标/短说明/有效操作；数量未知不画0，分母为0不伪造100%。
快捷卡图标、空态图标、图例形状、同步小点、口径说明图标和活动语义图标
都按职责保留。最近活动使用淡紫摘要+真实事件列表，时间小胶囊浅蓝蓝字。
数据映射到我的业务，不复制参考的授权字段、个人信息、地址或日志。缺少
业务关系时说明取舍；有实际数据的模块不能无声删除。复用已有图表库，
处理非零尺寸挂载、主题/resize/数据更新、提示框定位与隐藏、失败保留旧图与路由清理；提示框不可被卡片或portal边界裁掉，数据点、图例、数据表与提示共用同一真实数据源。
提示箭头尖端到实际图形边缘默认6px、正常4–8px；分布环与细进度环锚定可见外缘，
不按容器顶边或圆心定位。正文定位计入7px箭头高度，offset不重复累加；空间不足
翻转并同步箭头，不能通过拉远提示框避让。箭头根部覆盖正文边框，内部无穿过的
横线/竖线、白缝或独立底边，外轮廓细边可保留；浅深主题都与正文同色连成一体。
实际测量尖端距离，核对滚动/resize/缩放。
柱图/折线提示同时跟随当前索引的x和y，正值分组柱按当前分类可见柱顶定位，
不按全图最高柱或固定top；高柱→矮柱切换时框与箭头同步下移。数据、图例、
轴范围、resize变化重新映射锚点，实际操作验证而非仅截图某一分类。
实际截图与操作检查完整页面、图表值、空错态和手机布局，报告未验证部分。
```
