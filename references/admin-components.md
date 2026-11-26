# 清爽蓝白后台：组件、按钮与全部状态

配合 [设计基线](admin-design.md)、[页面组合](admin-pages.md) 和 [动效规范](admin-motion.md) 使用。此文件把原先的尺寸范围收敛为同风格的实现档位：已有明确参考值沿用；参考未精确规定的控件采用下方统一默认值，这些是落地约定而非逐像素原稿测量。用户的可访问性、明确风格或现有设计系统要求优先。

页内配置目录／子导航与记录范围／状态分段筛选，额外读取 [页内彩色菜单与分段筛选](admin-navigation.md)，其中有逐项配色、完整CSS、键盘算法和真实筛选约束。主侧栏仍按本文件的精确组色实现，不把两种选中态混用。

## 组件实现合同

同一职责在全项目只使用一套外观与状态规则。先建立目标项目里的PageHeader、Panel、Button、IconButton、SearchField、FormField、Segmented、StatusBadge、SummaryCard、ResourceCard、DataTable等共享实现或封装，再用数据组合页面。名字可跟随目标仓库，视觉职责不能随页面散开。不要只给组件库设置primary颜色便认为其余尺寸、浮层和状态已自动匹配。

**控件通用提示词：**

```text
为当前页面列出实际用到的组件及其variant、size、状态与动作，按本文件复用
同一实现。每个可操作组件都处理default、hover、active、focus-visible、
disabled；异步动作再处理loading、success、error。只有适用的状态才实现，
不要给静态装饰增加点击。状态改变不改宽度、字号、边距或图标基线；禁用
保留可读性，不触发hover动画和业务动作。视觉样式写入目标项目，说明文档
与截图只做参照；不要把演示页面、node_modules或测试构建放入skill。
```

## 尺寸、排版与密度档位

| 职责 | 固定基线 | 圆角／字号／图标 | 使用位置 |
|---|---|---|---|
| 紧凑文字按钮 | 高34，左右13，gap7 | 圆角8；12px／500；图标16 | 表格工具、普通卡片次操作 |
| 页头／表单操作 | 高38，左右14，gap8 | 圆角10；12px／500；图标16 | 页面右上、设置保存、表单动作 |
| 登录提交 | 高44、容器100%宽、左右17 | 圆角10；13px／600；图标16 | 登录卡，不能给所有后台按钮套44高 |
| 专用箭头按钮 | 最低38，左padding56、右15 | 圆角11；12px／500；箭头14 | 页面上下文入口，详细CSS见动效规范 |
| 顶栏图标按钮 | 36×36，无文字padding | 圆角10；图标16–18 | 菜单、主题、刷新；触摸命中区可扩到44 |
| 表格行图标动作 | 32×32基线，目标已有36则全表统一36 | 圆角8；图标16 | 详情、复制、更多；≤600可用44命中区 |
| 普通输入／Select | 高38，左右12；多行字段自适应 | 圆角10；正文13；前后图标16 | 表单、搜索、筛选；标签13、帮助12 |
| 登录大输入 | 高42，左右12 | 圆角10；14px；图标16 | 登录用户名与密码 |
| 分段选择 | 容器高38起，padding4 | 外圆角11、内7；11–12px／500 | 2–5个短选项；长标签不硬套等分 |
| 状态徽标 | min-height24、padding3 8、gap5 | 圆角999；11px／500／1.4；图标12 | 行状态、连接、产品状态，不能当主按钮 |
| 面板与子面 | 主面16圆角、padding20；子面12圆角、padding12–14 | panel白、line-soft边、低阴影 | 产品卡18、侧栏20、KPI24是有意例外，不全局设24 |

所有尺寸按border-box计算，包括边框和padding；普通38高输入不能因库默认line-height和内padding变成46。组件库大号默认、浏览器默认按钮、第三方弹层都需要落实对应档位。触屏变大命中区不代表桌面所有可见控件必须变大。

排版采用以下层级：页面26／650（概览30）、分区18／600、面板标题16／600、普通业务内容13–14／400、标签13／500、说明12／400、辅助ID11–12等宽；数值用tabular-nums。正文line-height1.5–1.7；表单标签与小胶囊不使用超大字距或全大写装饰。文档正文与登录大标题是专用排版，不影响后台控件。

<a id="clean-admin-sidebar"></a>

## 侧栏：分组竖线、彩色图标与菜单状态

以概览参考图中的完整侧栏为准。组标题文字使用text-soft，彩色短竖线位于文字前；不是把整段标题染色，也不是选中菜单左侧另加一条长线。未选菜单保留分组对应的彩色线框图标和浅色底座，选中菜单才统一蓝色渐变、白字白图标。分组颜色通过稳定的group tone绑定，不能用nth-child决定颜色而在隐藏菜单或调整顺序后串色。

| 分组示例／tone | 组标题短竖线（opacity .6） | 未选图标线条 | 24×24图标底座 |
|---|---|---|---|
| 工作台／blue | var(--accent)，浅色为#2478ff | var(--accent-link)，浅色为#175dc8 | var(--tint-blue)，浅色#edf4ff |
| 业务运营／violet | #b46bdd | #9860c1 | var(--tint-purple)，浅色#f4f0fa |
| 开发者工具／coral | #e99579 | #bd7351 | var(--tint-amber)，浅色#fff7e9 |
| 系统设置／cyan | #2db8d3 | #2192a7 | var(--tint-cyan)，浅色#edf8fa |

上表是四类参考组色，不强制只有四个业务分组；分组数量和名称来自目标产品。更多职责可按页内菜单规范的mint／rose等色扩展并固定映射，不能因插入新组让旧组换色。

组标题11px／700、line-height1.5、padding6 10 8、文字与竖线gap7；竖线4×10、圆角2，不是页面标题的4×12标记。组内gap5、组底margin19，导航区距搜索16。菜单min-height42、padding8 10、gap10、圆角11、1px透明边；图标底座24×24／圆角7，内部SVG17×17、线框且display:block。菜单文字12px／550、默认text-soft；图标有独立色值，不能被color:inherit变成全灰。

状态：default无整行底色；hover未选行变tint-blue，图标保留本组颜色；当前路由行使用180deg #3589ff→#1669f3、#267aff边、白字、内白25%高光与轻阴影，图标底座白18%、图标白色，计数白20%底／白字。focus-visible保留2px可见焦点环；hover不能盖掉active背景，active仅由真实路由／视图驱动。未选计数一律蓝字浅蓝底，不随组变紫／橙；未知不显示，真实0不误隐藏。

下面是单个分组的结构，目标项目按实际菜单复制数据；每组标题ID必须唯一，图标按业务换为同体系SVG，href映射真实页面。已有可靠菜单组件时保留其导航与焦点行为，仅映射这些样式。

```html
<nav class="admin-nav" aria-label="主导航">
  <section class="admin-nav__group" data-nav-tone="violet" aria-labelledby="nav-business">
    <h2 class="admin-nav__label" id="nav-business">业务运营</h2>
    <a class="admin-nav__item" href="/products" aria-label="产品目录">
      <span class="admin-nav__icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
          <path d="M5 8h14v13H5zM4 8l3-5h10l3 5M9 3v10h6V3" />
        </svg>
      </span>
      <span class="admin-nav__copy">产品目录</span><span class="admin-nav__count">3</span>
    </a>
  </section>
</nav>
```

```css
.admin-nav { margin-block-start:16px; }
.admin-nav__group { --nav-mark:var(--accent); --nav-ink:var(--accent-link); --nav-tint:var(--tint-blue);
  display:grid; gap:5px; margin-block-end:19px; }
.admin-nav__group[data-nav-tone="violet"] { --nav-mark:#b46bdd; --nav-ink:#9860c1; --nav-tint:var(--tint-purple); }
.admin-nav__group[data-nav-tone="coral"] { --nav-mark:#e99579; --nav-ink:#bd7351; --nav-tint:var(--tint-amber); }
.admin-nav__group[data-nav-tone="cyan"] { --nav-mark:#2db8d3; --nav-ink:#2192a7; --nav-tint:var(--tint-cyan); }
.admin-nav__label { display:flex; align-items:center; gap:7px; margin:0; padding:6px 10px 8px;
  color:var(--text-soft); font:700 11px/1.5 var(--sans); letter-spacing:.035em; }
.admin-nav__label::before { content:""; flex:0 0 4px; block-size:10px; border-radius:2px;
  background:var(--nav-mark); opacity:.6; }
.admin-nav__item { display:flex; align-items:center; gap:10px; min-inline-size:0; min-block-size:42px;
  padding:8px 10px; border:1px solid transparent; border-radius:11px; text-decoration:none;
  background:transparent; color:var(--text-soft); text-align:start;
  transition:color 120ms ease,background-color 120ms ease,box-shadow 160ms ease; }
.admin-nav__icon { display:grid; place-items:center; flex:0 0 24px; inline-size:24px; block-size:24px;
  border-radius:7px; background:var(--nav-tint); color:var(--nav-ink); }
.admin-nav__icon svg { display:block; inline-size:17px; block-size:17px; }
.admin-nav__copy { min-inline-size:0; font:550 12px/1.5 var(--sans); }
.admin-nav__count { margin-inline-start:auto; padding:1px 5px; border-radius:4px;
  color:var(--accent-link); background:var(--tint-blue); font:400 10px/1.5 var(--sans); }
.admin-nav__item:hover:not([aria-current="page"]) { background:var(--tint-blue); }
.admin-nav__item[aria-current="page"] { background:linear-gradient(180deg,#3589ff,#1669f3);
  color:#fff; border-color:#267aff; box-shadow:inset 0 1px 0 rgb(255 255 255 / .25),0 1px 2px rgb(15 70 170 / .2); }
.admin-nav__item[aria-current="page"] .admin-nav__icon { color:#fff; background:rgb(255 255 255 / .18); }
.admin-nav__item[aria-current="page"] .admin-nav__count { color:#fff; background:rgb(255 255 255 / .2); }
.admin-nav__item:focus-visible { outline:2px solid var(--accent-link); outline-offset:2px; }
@media(min-width:961px) {
  .app-shell[data-sidebar-collapsed="true"] .sidebar .admin-nav__label,
  .app-shell[data-sidebar-collapsed="true"] .sidebar .admin-nav__copy,
  .app-shell[data-sidebar-collapsed="true"] .sidebar .admin-nav__count { display:none; }
  .app-shell[data-sidebar-collapsed="true"] .sidebar .admin-nav__item { justify-content:center; padding-inline:0; }
}
@media(prefers-reduced-motion:reduce) { .admin-nav__item { transition:none; } }
```

桌面折叠为64px实际侧栏时，保留24px彩色底座和当前蓝色菜单；隐藏标签／计数前给每个入口设置完整aria-label，并提供聚焦可见的名称提示。手机抽屉显示完整标题、竖线、菜单文字与计数，不沿用折叠隐藏规则。深色底座引用相应tint主题，彩色竖线和图标不能丢失；按实际对比度需要适配色值时保留组间区别并注明调整。

**侧栏纠偏提示词：**

```text
按admin-components的侧栏合同修正共享导航。四组使用blue/violet/coral/cyan
稳定映射，组标题前4×10短竖线分别蓝/紫/珊瑚/青、.6透明度，标题仍text-soft。
每个未选菜单有24×24浅色底座、7圆角和17px彩色线框图标，文字12/550。
hover浅蓝整行且保留分组图标色；当前路由才是蓝色渐变整行、白字白图标、
白18%图标底座与白20%计数底。active不被hover覆盖，不出现全灰菜单或长竖线。
折叠仍保留彩色图标与名称入口，手机完整展示分组；不复制业务菜单或假计数。
```

## 按钮：样式、位置与状态矩阵

### Primary 主操作

- 默认：180deg渐变`#3589ff → #1669f3`、1px `#2478f8`边、白字；高光`inset 0 1px 0 rgba(255,255,255,.25)`，外阴影`0 1px 2px rgba(15,70,170,.18)`。图标在文字前，文字不使用全粗700；内容区单一主动作通常只出现一处。
- 悬停：渐变`#237bfa → #0f5ce6`、边框`#1669f3`，阴影增至`0 2px 5px rgba(15,70,170,.2)`；不突然发光或出现大面积blur。
- 按下：scale(.975)，120ms恢复；不要同时translateY和scale而造成按钮跳离基线。
- 聚焦：2px accent outline、offset3；颜色外观与hover可接近，但焦点环不能省略。
- 禁用：opacity .5、去外阴影、cursor not-allowed，保留宽高和文案；不能执行、不能press缩放。
- 加载：原图标位换16px旋转图标、文案“保存中…”等，按钮宽度至少维持进入loading前宽度，aria-busy；业务不允许时阻止重复提交，不锁住其他无关输入。
- 成功：需按钮内反馈时短时green表面、Check与结果文字；否则保留按钮并用合适Toast。失败恢复可再次执行且错误就地显示；不能一直停在loading。
- 深色：主操作仍保留蓝色渐变和白字；不要无条件套accent-ink导致暗字压在深蓝按钮上。专用箭头组件使用自身主题token，是不同variant。

**提示词：**

```text
所有保存、新建、确认主操作使用共享Primary Button：38px页头档或34px紧凑档、
指定蓝色渐变、白字、细高光和轻阴影，图标16px。逐个实现hover、scale(.975)
按压、2px键盘焦点、.5禁用与稳定宽度loading。不要用纯蓝平面矩形或第三方
默认大按钮替代。分区主动作之间有层级，不把导出、刷新和取消也涂成主蓝。
```

### Secondary／Outline／Text／Danger

| 类型 | 默认 | hover／active／focus | 禁用与业务 |
|---|---|---|---|
| 白色次按钮 | panel面、line细边、text-soft、shadow-sm | hover浅蓝4%混色、边线更清楚；press .975；focus2px | .5透明、无阴影；用于取消、编辑、辅助导航 |
| 弹窗页脚次按钮 | accent7%混panel，accent22%混line，text-soft | hover背景12%、边42%，focus2px | 不能在白弹窗里透明到看不到；取消在主按钮左侧 |
| 线框按钮 | 透明／panel、accent-link字、蓝色细边 | hover蓝色6–9%面；按压与focus同基础 | 只用于需要强调的次动作，不替代所有次按钮 |
| 文字按钮 | 无底无边，accent-link，最小可操作高度34 | hover accent-strong，focus环；不加整行跳动 | 适合查看、重置、复制；不可作为重要提交的唯一弱入口 |
| 危险次动作 | red文字与图标，淡红边或无边，背景低调 | hover red9%面、red30%边；可见focus | 删除确认内可用实心red主动作；默认页头不用巨大红色按钮 |
| IconButton | 图标16–18，顶栏浅蓝36面或行内透明32面 | hover面／边／颜色反馈，行内press下移1或统一缩放 | aria-label来自动作名；未禁用时Tooltip解释动作，禁用原因可放可聚焦wrapper |
| More／Split | More是32图标按钮，Split共38高，主动作与箭头区有细分界 | 每区独立hover、focus；菜单保持触发按钮名称 | 菜单为动作，Select为值；关闭菜单后焦点返回触发器 |

### Arrow Reveal 箭头展开按钮

使用 [动效规范的完整片段](admin-motion.md)，不能自行简化成hover变蓝。外层白面、11圆角、38高、稳定宽度；内部left4／top4／bottom4、28宽蓝块、7圆角、14箭头。hover和focus-visible时内部宽到`100%−8px`，300ms指定curve；三个2px圆点以5px间隔、180ms淡至.7；文字180ms转accent-ink；离开收回。文字不移动，小点不弹跳，箭头不挤压，禁用不展开。长标签留足前部箭头／三点固定区域，不能被装饰遮住。

## 输入、搜索与字段容器

| 组件 | 默认结构／视觉 | 交互和状态细节 |
|---|---|---|
| FormField | 可见label13在上，距输入8；必填红星在标签前；字段下help12／1.5，距6 | label关联input，错误文字替换或接在help下，保留布局空间；aria-describedby指向有效说明 |
| TextInput | panel、1px line、38高、10圆角，文字13、padding12，placeholder faint | hover边更清楚；focus accent边+3px淡蓝环；error红边+错误句；disabled panel-muted、muted；readonly保持可选择复制 |
| SearchField | 16放大镜+输入+有值时清空；38高，padding12；工具栏320–460宽 | 文案说明搜什么；清空恢复焦点；Enter查询或输入查询沿用产品模式；异步防竞态；不能只画一个看似可输入div |
| Password | 与输入同尺寸，左Lock，右显隐按钮，密码文字预留后缀区域 | 切type不清值、不自动提交；眼睛有“显示／隐藏密码”名称；正确autocomplete；禁用仍对齐 |
| Textarea | 最低96高、padding10 12、13px／1.6、10圆角；垂直扩展 | 长文本换行；高度由任务决定，错误不截断；无理由不禁止resize；禁用／只读与输入一致 |
| InputNumber | 38高、右侧两个step按钮或目标库一致结构；数字区与箭头区细分隔 | min/max及单位跟真实数据；非法值有提示；不会变NaN；键盘可调；禁用箭头不误触提交 |
| UnitField | 数字+单位Select，gap6；合计最大264宽，单位82宽为默认 | 标签描述整体概念；单位变化的数值换算／范围按业务；同组高度一致，不用文字后缀假装Select |
| Select | 字段显示当前值，右16px箭头，clear与arrow各有空间 | 单选已选项打勾，多选checkbox+field chips；下拉搜索与无结果；disabled与loading可区分；不能把动作塞进值列表 |
| Date／Range | 同38高，日期图标与范围分隔可读；文字不超过输入宽度 | 弹层同主题，已选范围有首尾与轻底；键盘与格式按库；手机有足够操作空间，不凭视觉修改时区／业务日期 |
| Upload | 小型边框区域、图标+动作+文件限制说明；已上传文件行 | 文件名可读、上传百分比真实、失败单项重试、移除明确；缩略图等比，不能先假成功再发请求 |
| Color／Avatar | 色块输入与34px头像预览+等宽色值成组 | 修改色值同步头像，合法色值校验，不能仅颜色表达账号身份；状态颜色不跟用户头像色任意改变 |

输入前缀／后缀SVG为block且flex-shrink0，gap6–8；文字行中图标不能上浮半个字。输入的边框与焦点建议通过同一层shadow／border绘制，避免同时两层库边框叠粗。全局主题需覆盖append-to-body的选择面板，不能只在页面容器设变量。

**表单提示词：**

```text
统一38px普通字段和42px登录字段，10px圆角，白面细灰边，标签13、正文13、
帮助12。前后缀16px并预留空间；focus用accent边与淡环，错误用红边和字段下
说明，disabled只读和loading各有真实区别。双列表单每列min-width:0、gap20，
手机单列；不要用placeholder代替标签或让红色校验文字遮住下一个字段。
```

## Switch、Checkbox、Radio与Segmented

| 控件 | 本风格默认 | 语义与状态 |
|---|---|---|
| Switch | 40×20左右胶囊起点，thumb16、两侧2；开accent、关中性灰，必要时短“开／关”文字 | 保留项目库可访问实现；指示位置+名称表达值；saving时pending、失败回滚；表单保存型不伪称即时生效 |
| Checkbox | 可见框16，圆角4，选中accent白Check，框与标签gap8 | unchecked／checked／indeterminate／disabled／focus俱全；大命中区wrapper；半选不是另一项真实值 |
| Radio | 圆16，外边line、选中accent外环和中心圆点，标签gap8 | 单组选一，方向键；选中后不直接清空，允许无选择时提供明确选项；Select单选内部不用Radio圈 |
| Segmented | 高38、padding4、外11内7圆角，共享蓝渐变indicator，单项字11–12 | 同组等分短文案，默认值有效；键盘可达；280ms移动；不要三项分别淡入背景假装滑块 |
| Toggle／Chip | 28–32高紧凑标签、左右8–10、圆角7，未选浅面／选中浅蓝蓝字 | 多选和单选通过实际语义表达；删除chip有独立按钮名称，不因hover才让触屏用户看到删除 |

长说明选项使用纵向Radio或选择卡，每项边框面与标题说明成组，间距10–12、padding12，不强塞窄分段控件。选择卡属于同风格扩展，不使用四色统计卡表达选项状态。

## 面板、摘要卡、资源卡与图表

### 业务 Panel

主面panel、line-soft 1px边、圆角16、workspace-card-shadow；header左右20、上下18–20，标题16／600，右侧小计或次动作。body通常20，header/body分隔只在需要独立工具区时出现。嵌套信息用圆角12浅蓝／淡紫子面，不再包一张同样阴影的主卡；最多让业务层级清楚，避免“卡片套卡片套卡片”。

### 大KPI与普通摘要

- 大KPI：四色115deg精确渐变、192高起、24圆角、padding24 24 18；label15、value38／650、单位12；右圆入口32、图标15。底部hint深色32%透明面、白字12、padding4 9、7圆角、5px白点。
- 装饰：主线框图标约118–135，右下超出画框，白30%透明、转角约−24deg；左下150px环、20px描边、13%白，再一圈7%白；右上星芒24、60%白与小空心点。装饰置于背景层、pointer-events:none、aria-hidden；不能用emoji或实心大图标替代。
- 普通摘要：142高、20圆角、padding20 22、标签12、数字32、单位11；小版装饰85px线框，不加大KPIhint和圆入口。它与大KPI是两个固定variant，不能随机混合；概览中需要跳转的指标采用大KPI，不能以“精简摘要”为由省掉右上入口。
- hover大KPI上移3、普通摘要上移2，阴影按tone，数字保持真实值；按动效规范处理入场占用transform的问题。
- 三指标设置摘要使用紫／珊瑚／青，130高、21px状态值。业务不足四项时减少数量，不创造“好看”的虚构指标；颜色不承担成功失败语义。

<a id="clean-admin-metric-contract"></a>

#### 大KPI的颜色与导航合同

| 顺序／tone | 使用的唯一渐变token | 115deg起点 → 终点 | 同色阴影 |
|---|---|---|---|
| 1／violet | --summary-violet | #923cd1 → #ba68df | rgba(147,60,209,.17) |
| 2／coral | --summary-coral | #db6a58 → #efa28a | rgba(219,106,88,.18) |
| 3／rose | --summary-rose | #d84f81 → #ed8ba5 | rgba(216,79,129,.17) |
| 4／cyan | --summary-cyan | #149dcc → #59c4e3 | rgba(20,157,204,.19) |

CSS定义复用admin-design的token，表中端点用于核对，不能再选“接近的紫／红／青”。不要对整卡使用filter:brightness、opacity、黑色蒙层、multiply混合，或用主题深色变量替代这些渐变；黑色半透明面仅用于局部hint与圆按钮。实测computed background-image，排查旧类名、组件库variant、行内样式与dark规则覆盖；不能只看到变量定义正确就认定最终卡面正确。tone用上述视觉名称，不用success／warning等业务状态推断颜色，也不沿用其他组件里含义不同的旧tone别名。

每张可导航的大KPI都有**始终可见**的右上圆入口，标题与入口在同一header行，不能换成标题左侧的图标方块。圆按钮桌面32×32、1px白28%边、黑15%面、白色15px箭头；与顶部和右边均隔24px。默认右向SVG旋转−40deg；仅入口hover／focus-visible时旋回0deg、面变白24%；离开或失焦反向恢复。圆入口旋转200ms ease，卡片hover上移3px／180ms ease，二者独立，不移动数字与hint。≤600时圆入口40×40、header内margin-block:-6px，为触屏保留入口。

这是**导航链接**：接入目标页面的真实href或路由Link，保留键盘Enter、可访问名称与当前产品的导航机制；原项目使用视图切换时接同等动作。点击直接进入该指标对应的列表／详情，不弹提示、不打开菜单、不仅播放动画。各卡可以指向同页不同筛选；目标从业务对象与现有路由确定，不能照抄参考品牌或假造href="#"。只有箭头负责跳转，不把整卡包进链接或给外层添加与内部交互冲突的click。没有目标的纯统计采用明确的普通摘要variant，不生成看似可点却无行为的箭头。

每张卡的背景画元素是固定组成，不是可有可无的示意装饰。背景层由右下线框大图标、左下双层越界环、星芒、小空心点组成；前景层由标题、圆入口、数字单位和hint组成。右下图标按各卡业务分别选用同一图标体系，不把四卡全换成同一个大环或同一个图标；没有精确图标时用同含义线框图标适配，不能用品牌图片或emoji代替。

| tone | 右下线框图标（CSS px） | 星芒 | 其他固定装饰 |
|---|---|---|---|
| violet | 118×118、right−8、bottom4、旋转−24deg | right83、top27、24px、白60% | 左下环150、left−65、bottom−100、20px白13%边及20px白7%外环；小点right44、top65、10×10、3px白18%边 |
| coral | 135×135、right−15、bottom−5、旋转16deg | 同violet | 同violet，图标轮廓随业务变化 |
| rose | 135×135、right−11、bottom−9、旋转−20deg | 同位置、色#ffdf91 | 同violet |
| cyan | 同violet | right100、top34，其余同violet | 同violet |

图标为白30%透明线条，无实心底座；越界部分只在背景层裁切，避免装饰压住圆入口或hint。窄屏按片段缩小装饰与移动星芒、小点，仍保留这四种元素。下方图标是一个可替换的线框示例，其他tone的图标语义仍需按业务分别配置。

下面是目标项目的单卡结构示例，href、标题、数值、hint和右下线框图标按真实业务替换；其余卡切换tone、图标与数据。读取基础token后使用，不另建演示工程。

```html
<article class="admin-kpi" data-tone="violet">
  <div class="admin-kpi__art" aria-hidden="true">
    <i class="admin-kpi__ring"></i><span class="admin-kpi__star">✦</span><i class="admin-kpi__dot"></i>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
      <path d="M4 5h16v12H4zM9 21h6m-3-4v4" />
    </svg>
  </div>
  <header class="admin-kpi__header">
    <span>任务总量</span>
    <a class="admin-kpi__open" href="/tasks" aria-label="查看任务明细">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
        <path d="M5 12h14m-6-6 6 6-6 6" />
      </svg>
    </a>
  </header>
  <div class="admin-kpi__value"><strong>360</strong><small>项</small></div>
  <footer class="admin-kpi__hint"><i aria-hidden="true"></i><span>108项待处理</span></footer>
</article>
```

```css
.admin-kpi { --kpi-surface:var(--summary-violet); --kpi-shadow:rgba(147,60,209,.17);
  position:relative; isolation:isolate; min-inline-size:0; min-block-size:192px;
  padding:24px 24px 18px; border:0; border-radius:24px; overflow:hidden;
  color:#fff; background:var(--kpi-surface);
  box-shadow:0 4px 12px var(--kpi-shadow),inset 0 1px 0 rgb(255 255 255 / .25);
  transition:transform 180ms ease,box-shadow 180ms ease; }
.admin-kpi[data-tone="coral"] { --kpi-surface:var(--summary-coral); --kpi-shadow:rgba(219,106,88,.18); }
.admin-kpi[data-tone="rose"] { --kpi-surface:var(--summary-rose); --kpi-shadow:rgba(216,79,129,.17); }
.admin-kpi[data-tone="cyan"] { --kpi-surface:var(--summary-cyan); --kpi-shadow:rgba(20,157,204,.19); }
.admin-kpi:is(:hover,:focus-within) { transform:translateY(-3px); box-shadow:0 10px 24px var(--kpi-shadow); }
.admin-kpi__header,.admin-kpi__value,.admin-kpi__hint { position:relative; z-index:1; }
.admin-kpi__header { display:flex; align-items:center; justify-content:space-between; gap:6px; font:500 15px var(--sans); }
.admin-kpi__open { display:grid; place-items:center; flex:0 0 32px; inline-size:32px; block-size:32px;
  padding:0; border:1px solid rgb(255 255 255 / .28); border-radius:50%;
  background:rgb(0 0 0 / .15); color:#fff; text-decoration:none; }
.admin-kpi__open svg { display:block; inline-size:15px; block-size:15px;
  transform:rotate(-40deg); transition:transform 200ms ease; }
.admin-kpi__open:is(:hover,:focus-visible) { background:rgb(255 255 255 / .24); }
.admin-kpi__open:is(:hover,:focus-visible) svg { transform:rotate(0deg); }
.admin-kpi__open:focus-visible { outline:2px solid #fff; outline-offset:3px; }
.admin-kpi__value { display:flex; align-items:baseline; gap:4px; min-block-size:75px; padding-block-start:31px; }
.admin-kpi__value strong { margin:0; font:650 38px/1.2 var(--sans); font-variant-numeric:tabular-nums; letter-spacing:-.03em; }
.admin-kpi__value small { font-size:12px; color:rgb(255 255 255 / .95); }
.admin-kpi__hint { display:flex; align-items:center; gap:5px; inline-size:fit-content; max-inline-size:100%;
  margin-block-start:10px; padding:4px 9px; border:1px solid rgb(255 255 255 / .19);
  border-radius:7px; background:rgb(0 0 0 / .32); font:400 12px/1.5 var(--sans); }
.admin-kpi__hint i { flex:0 0 5px; block-size:5px; border-radius:50%; background:#fff; }
.admin-kpi__art { position:absolute; inset:0; z-index:0; overflow:hidden; pointer-events:none; }
.admin-kpi__art > svg { position:absolute; right:-8px; bottom:4px; inline-size:118px; block-size:118px;
  transform:rotate(-24deg); color:rgb(255 255 255 / .3); }
.admin-kpi[data-tone="coral"] .admin-kpi__art > svg { inline-size:135px; block-size:135px;
  right:-15px; bottom:-5px; transform:rotate(16deg); }
.admin-kpi[data-tone="rose"] .admin-kpi__art > svg { inline-size:135px; block-size:135px;
  right:-11px; bottom:-9px; transform:rotate(-20deg); }
.admin-kpi__ring { position:absolute; left:-65px; bottom:-100px; inline-size:150px; block-size:150px;
  border:20px solid rgb(255 255 255 / .13); border-radius:50%; box-shadow:0 0 0 20px rgb(255 255 255 / .07); }
.admin-kpi__star { position:absolute; right:83px; top:27px; color:rgb(255 255 255 / .6); font:24px/1 var(--sans); }
.admin-kpi[data-tone="rose"] .admin-kpi__star { color:#ffdf91; }
.admin-kpi[data-tone="cyan"] .admin-kpi__star { right:100px; top:34px; }
.admin-kpi__dot { position:absolute; right:44px; top:65px; inline-size:10px; block-size:10px;
  border:3px solid rgb(255 255 255 / .18); border-radius:50%; }
@media(max-width:1280px) {
  .admin-kpi { min-block-size:185px; padding:20px 18px 16px; border-radius:20px; }
  .admin-kpi__header { font-size:13px; } .admin-kpi__value strong { font-size:34px; }
  .admin-kpi[data-tone] .admin-kpi__art > svg { inline-size:90px; block-size:90px; bottom:12px; opacity:.75; }
}
@media(max-width:960px) {
  .admin-kpi { min-block-size:190px; }
  .admin-kpi__header { font-size:15px; } .admin-kpi__value strong { font-size:38px; }
  .admin-kpi[data-tone] .admin-kpi__art > svg { inline-size:120px; block-size:120px; }
}
@media(max-width:600px) {
  .admin-kpi { min-block-size:164px; padding:16px 14px 12px; border-radius:18px; }
  .admin-kpi__header { font-size:12px; }
  .admin-kpi__open { flex-basis:40px; inline-size:40px; block-size:40px; margin-block:-6px; }
  .admin-kpi__value { min-block-size:57px; padding-block-start:22px; }
  .admin-kpi__value strong { font-size:30px; }
  .admin-kpi__hint { margin-block-start:8px; padding:4px 6px; }
  .admin-kpi[data-tone] .admin-kpi__art > svg { inline-size:82px; block-size:82px; right:-18px; bottom:10px; }
  .admin-kpi[data-tone] .admin-kpi__star { right:30px; top:45px; font-size:17px; }
  .admin-kpi[data-tone="cyan"] .admin-kpi__star { right:35px; }
  .admin-kpi__dot { right:15px; top:26px; }
}
@media(prefers-reduced-motion:reduce) {
  .admin-kpi,.admin-kpi__open svg { transition:none; }
  .admin-kpi:is(:hover,:focus-within) { transform:none; }
}
```

overflow仅裁切有意越界的装饰，不用于掩盖文本；长标题允许换行，数值、单位和hint自然增高。不得让全局header/footer/article样式改掉这些命名类的最终结果。

**指标卡纠偏提示词：**

```text
当前概览卡颜色过深且缺少跳转入口。按admin-components的大KPI合同和参考图
修正共享组件：四卡依次使用115deg的summary-violet/coral/rose/cyan精确渐变，
检查最终computed background和祖先filter/opacity，去掉整卡变暗覆盖。
保留24圆角、192起高、38数值；每卡均有不同业务的右下半透明线框图标、左下
双层环、星芒、小空心点与左下hint，按tone配置位置，不只画统一大圆环。
背景aria-hidden且不接收点击，前景内容不被盖住，不改成普通142摘要。
每张卡右上始终显示32px圆形链接，白15px箭头默认-40deg，hover/focus-visible
200ms转到0deg并亮面；离开复原，卡片独立180ms上移3px。点击链接直接跳到
该指标的真实页面或带对应筛选的列表，保留键盘操作；不要换成三点菜单、
左侧图标块、蓝底铺满按钮或仅Toast。记录每张卡的目标路由并实际点击验证。
```

### ResourceCard

18圆角、padding22、白面细边。内部按 [目录页面](admin-pages.md) 的固定顺序；顶部短色条3×44，不延伸到整卡外缘；图标底座40／12圆角、主题色7%混panel与15%边，状态贴图标右、更多靠最右。ID11、标题18、说明12／1.7。能力面蓝、数量面紫、内圆角12；页脚有细线、34次按钮与11状态。整卡hover上移3，但只有实际入口负责导航，不能把菜单点击冒泡成整卡跳转。

### Badge／Avatar／Count

- StatusBadge：min-height24、padding3 8、gap5、11字，color按success／warning／danger／info／neutral；边为tone24%混透明，面为tone7%混panel，图标12；文本不换行，长状态考虑完整可访问名与更合适区域，不能把整行撑高。
- Count：数字tabular-nums，浅蓝小底、圆角4、padding1 5，导航选中时白字20%白底；未知数量不显示0。
- Avatar：侧栏30、顶栏26、列表32、身份hero66–72四档；小头像圆角8–10，大头像圆形。图片object-fit:cover且预留尺寸，缺图用姓名首字；不使用第三方真实头像作素材。

### 图表／进度

工作台里的两排图表、比例环、图标快捷卡和最近活动，按 [完整工作台规范](admin-workbench.md) 实现；本节只提供共享组件基线，不将下面几句概述当成全部图表要求。

图表背景透明；主要系列蓝，辅助青／薄荷／橙／紫等与真实legend一致；网格line-soft、虚线约5，轴文字10–12；标题14，图例10–12，小点8，坐标保持同口径。避免图表自带大toolbar、厚阴影、深灰默认绘图区与全蓝坐标轴。长标签可合理截断并提供完整值，不把所有类别缩成不可识别前缀。

环形图与进度环分开：生命周期环显示真实分项分布，中心29–30数值与12说明；细进度环r51、线6、圆端，value/total为真实比例。线性进度高5、圆角999、浅蓝轨道、accent填充。零总量用“暂无数据”，不能用100%让卡片显得完成。

## 表格、工具栏与分页

| 元素 | 视觉要求 | 交互要求 |
|---|---|---|
| 工具栏 | panel面，padding12 20，gap10；搜索／筛选同38高，右轻操作 | 查询和重置保留焦点，加载不清旧值；条件多时换行或展开 |
| 表头／行 | header44、单行56、双信息64；cell水平12；底线line-soft，无粗竖线 | 排序符号、选择框、动作可键盘；不能为视觉顺序破坏DOM顺序 |
| 单元格 | 名称13、说明12灰、ID11–12等宽，数字右对齐，单位同列规则 | 长值可读或展开，复制真实完整内容，不能只复制截断文本 |
| hover／选中 | hover蓝3%混panel，selected蓝6%；选中保留checkbox | 行hover不代表可点击整行；状态按钮不冒泡触发详情 |
| 状态／行操作 | badge与IconButton使用固定档位，actions列96–144 | 操作少时展示文字，多时More；危险动作确认，禁用有说明 |
| 分页 | 上细线，padding16–20，左计数右页码；数字32px命中起点 | active浅蓝蓝字或项目统一蓝面；禁用prev/next清楚；手机换行不能挤掉总量 |
| 选择操作栏 | 深色紧凑底、白字11–12、圆角12、动作34；浮动在内容区下方 | 仅选中显示，留安全间距；取消选择可键盘；进出按动效规范 |

**表格提示词：**

```text
请逐项实现表格头、每列密度、编号复制、数值对齐、状态、选择框、行hover、
选中面、更多菜单、空结果、失败重试与分页。使用本文件固定行高与字体，
让业务主字段容易扫读；不要通过大行距和超大圆角制造空旷感。表格横向
滚动只发生在table容器；批量操作栏不遮挡最后一条记录或分页。
```

## Dialog、Drawer、Dropdown、Tooltip与反馈

| 组件 | 几何／材质 | 内容与状态 |
|---|---|---|
| 普通表单Dialog | 默认520宽、最大calc(100vw−32px)、16圆角、panel面；头20 24、体20 24、脚16 24 | 标题18、说明13，关闭32；字段38；页脚取消在左、主操作在右、gap8；长内容体滚动，头脚不被裁掉 |
| 危险确认 | 默认440宽、20圆角；小图标底座36、标题16、正文13 | 说清对象／数量／后果；取消次按钮+red确认；点遮罩不可执行确认；不要输入不存在的恢复承诺 |
| 详情Drawer | 默认520、最大100vw、左侧圆角16；body浅底padding20、子面14圆角 | header标题20，独立关闭；内容分组小蓝条，ID／状态／事实项有层级；手机全宽可用 |
| Dropdown Menu | panel面、细边、10圆角、padding6、item32高、左右10、图标16／文字12–13 | hover浅蓝，危险red，disabled muted；键盘上下／Esc，触发器保持名字；大段输入不放菜单 |
| Tooltip | panel混2%蓝、20%蓝边、圆角8、padding6 10、12字、max360宽 | show180／hide100／offset8，hover及focus；无交互简短解释，箭头同色；触屏入口不能依赖hover |
| Popover | 12圆角、padding16、标题14、正文13、细边轻阴影 | 有交互则能移入与聚焦；依据职责关闭，不从timer误关内部焦点 |
| Toast | 自适应宽、max360、圆角10、padding12 16、图标16与13文字、轻阴影 | 成功短时反馈，失败持久行内为主，不堆重复通知；文案变长可换行；不固定显示截图里的偶然Toast |
| Inline Alert | 浅语义色面、细边、10–12圆角、padding12 16，图标20 | 标题13／600、说明12–13、有效重试；局部出错只影响对应区域 |
| Empty State | 正文区域居中，图标32–48、标题16、说明13、距操作16 | 真空、无结果、无权限与失败分别描述；没有恢复能力不画假按钮；不替换整套后台壳层 |
| Skeleton | 与最终卡／表格同列数、同外框、低对比块 | 未到数据不显示全0；默认静态、无shimmer，刷新失败可保留旧数据 |

弹层、Switch、Select、Checkbox等优先使用目标项目已有库的语义和焦点实现，再统一视觉。上表宽度／密度是本风格默认约定，不是要求重写库或新增依赖。库portal也读取主题，浮层方向箭头颜色一致；Dialog和Drawer只有一个层负责进出动画，遮罩不要变成夸张深黑或多重毛玻璃。

## 逐组件验收与反例

逐个打开该页面用到的组件，依次核对默认、hover、press、键盘focus、disabled；异步组件再看loading、success、error。状态之间bounding box尺寸保持稳定；必需的文本换行属于自然增高，不能为了截图一致裁掉错误。

以下情况属于样式偏离，需在目标项目修正：主按钮没有渐变／高光；所有圆角都变24；表单全部48–56高；导航选中只有一条蓝线而没有蓝色渐变面；图标变成emoji／实心杂色图；普通摘要错误采用大KPI结构；所有字段无标签；文字与图标基线不齐；select展开为另一套深色主题；loading改变按钮宽度；箭头按钮只变背景却不铺底；不同页相同状态色和字号不一致。

长表单、长名称、空数据与窄屏要处理真实内容压力；从同一组件与token调整，不能为通过一张静态图而硬编码文本、绝对定位所有字段或禁用浏览器缩放。
