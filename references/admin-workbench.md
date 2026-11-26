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

交付前核对：两排图表及最近活动是否因只看首屏被漏掉；趋势／状态分布／三个比例／分类对比是否各自使用正确数据；汇总能否核对；0与未知是否区分；图例形状、系列颜色、快捷入口图标和有效动作是否齐全；390宽度、深色、空／错／刷新及reduced-motion是否可用。没有运行图表时注明未验证，不用静态SVG预览冒充真实数据联动验证。

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
处理非零尺寸挂载、主题/resize/数据更新、失败保留旧图与路由清理。
实际截图与操作检查完整页面、图表值、空错态和手机布局，报告未验证部分。
```
