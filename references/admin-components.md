# 清爽蓝白后台：组件、按钮与全部状态

配合 [设计基线](admin-design.md)、[页面组合](admin-pages.md) 和 [动效规范](admin-motion.md) 使用。此文件把原先的尺寸范围收敛为同风格的实现档位：已有明确参考值沿用；参考未精确规定的控件采用下方统一默认值，这些是落地约定而非逐像素原稿测量。用户的可访问性、明确风格或现有设计系统要求优先。

后台顶部栏的窄屏导航入口、搜索／快捷键、状态徽标、主题／刷新与头像账户组合，必读 [完整顶部栏](admin-topbar.md)，使用其中的结构、准确SVG和共享状态。页内配置目录／子导航与记录范围／状态分段筛选，额外读取 [页内彩色菜单与分段筛选](admin-navigation.md)，其中有逐项配色、完整CSS、键盘算法和真实筛选约束。主侧栏仍按本文件的精确组色实现，不把两种选中态混用。

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

<a id="clean-admin-information-layout"></a>

## 信息排版：键值、数字、长内容与卡片操作

| 场景 | 必须落实的结构与状态 | 验收边界 |
|---|---|---|
| 详情键值（Key-Value Alignment） | 同一分组用稳定标签列＋可收缩值列，标签12–13／muted、值13／text；列宽按本组标签和现有页面结构统一，说明跟随对应值。使用语义明确的详情列表等结构，不用空格或连续冒号拼齐。值、复制动作分别占位 | 各行值从同一位置开始，长值换行且不把下一行挤错列；窄屏放不下时转为标签在上／值在下。复制取得完整原值 |
| 数字与单位（Baseline Alignment） | 同一读数的数字、货币／数量／百分比／耗时单位共用文字基线；数值采用等宽数字，负号、小数、分隔符与单位有稳定间距。KPI等组件已有尺寸继续沿用 | 位数和单位长短变化不让单位上下漂移、不遮挡操作；仅同一读数用基线对齐，顶栏图标按钮和输入图标仍按容器中心对齐 |
| 文件／路径／标识（Middle Truncation） | 首尾都有识别意义时中间省略，保留名称前部及扩展名、版本或标识后缀；原始完整值单独保存，复制／下载／跳转均用完整值。普通标题仍按阅读任务换行或尾省略，不一律从中间裁 | 如design…dark.css与design…light.css仍可区别；完整查看入口支持键盘和触摸，不只依赖鼠标Tooltip。菜单动作、错误恢复说明、关键数值不为排齐强行截断 |
| 标题和说明换行（Text Balance／Line Clamp） | 短标题可采用平衡换行；中文、英文与数字单位按[界面排版](interface-details.md#cjk-latin-typesetting)处理。卡片摘要确需限行时提供完整内容入口，不对表单标签、校验错误和详情原文统一限行 | 长标题与390宽时不留单字孤行、不裁掉关键动作；不用手写固定换行适配某一句文案，不靠缩小全局字号或整页缩放通过 |
| 同排卡片底部操作（Bottom-Aligned CTA） | 同一排同类资源／项目卡共享外部高度，内部正文自然增高，操作区由弹性剩余空间推至底部；说明为空时也遵守同一操作区职责，不塞不可见假文字 | 对照1行／多行／空说明，操作基线一致且不覆盖正文；不能固定正文高度裁字、绝对定位压住内容或使用负margin。换列后按各行对齐，不强迫不同职责卡片同高 |

上述排版在目标项目共享详情行、数值块、文件名和卡片页脚组件中实现。已有可靠组件先映射其结构，不为这些规则新增运行时依赖或在skill创建演示工程。

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

**切换时文字不闪动：**当前项的渐变背景与标签、图标、计数的前景色在同一次状态更新中切换，不对这些文字或图标的color／opacity做补间。渐变background-image在这份实现中直接切换；若文字仍单独做120ms过渡，旧项移除蓝底后会短暂白字配浅底，新项也会短暂深字配蓝底，产生闪淡。悬停背景与阴影可继续轻过渡。标签使用同一个稳定DOM节点，路由切换不重挂载整个侧栏，不给标签按当前路由设key或套out-in／淡入淡出；选中态按真实路由在同一提交中替换，不先清空全部选中再用定时器或下一帧补回。库自带的label／icon／count过渡也需要在当前导航组件内映射或取消，不能只修改外层。

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
  transition:background-color 120ms ease,box-shadow 160ms ease; }
.admin-nav__icon { display:grid; place-items:center; flex:0 0 24px; inline-size:24px; block-size:24px;
  border-radius:7px; background:var(--nav-tint); color:var(--nav-ink); transition:none; }
.admin-nav__icon svg { display:block; inline-size:17px; block-size:17px; }
.admin-nav__copy { min-inline-size:0; color:inherit; font:550 12px/1.5 var(--sans); transition:none; }
.admin-nav__count { margin-inline-start:auto; padding:1px 5px; border-radius:4px;
  color:var(--accent-link); background:var(--tint-blue); font:400 10px/1.5 var(--sans); transition:none; }
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

验收连续来回点击同组与跨组菜单、快速点击尚在悬停中的旧项，并用键盘导航／浏览器返回重复切换；在浅深主题下逐帧核对新旧两项标签、图标和计数。旧项离开蓝底时立即恢复未选前景，新项进入蓝底时立即白字；不出现白字配浅底、深字配蓝底、文字消失再出现或字重／宽度跳变。侧栏节点与导航滚动位置保持稳定，主题和正文入场不影响菜单文字。正文另按页面规则更新，不为消除菜单闪动而关闭所有组件动画。

桌面折叠为64px实际侧栏时，保留24px彩色底座和当前蓝色菜单；隐藏标签／计数前给每个入口设置完整aria-label，并提供聚焦可见的名称提示。手机抽屉显示完整标题、竖线、菜单文字与计数，不沿用折叠隐藏规则。深色底座引用相应tint主题，彩色竖线和图标不能丢失；按实际对比度需要适配色值时保留组间区别并注明调整。

### 品牌居中与侧栏内部折叠控制

品牌区内Logo和文字横向排列，Logo与“标题＋副标题”这一整体垂直居中；整组按实际内容宽度在侧栏内水平居中。不能只让标题文字居中却把Logo留在左边，也不能用justify-content:space-between把两者拉开；标题与副标题在文字列内左对齐。图标34×34、gap11、名称20／700、副标题10；副标题可选，只有标题时仍居中。品牌外区min-height68、左右沿用侧栏12px内边距；在100%缩放下，整组包围盒中心与侧栏内容区中心误差不超过1px。长名在可用宽度内截断并提供完整名称，不靠放大侧栏或任意缩小字号补救。Logo等比contain；素材本身有透明留白时检查可见图形的光学中心，不能靠不对称padding把整组推偏。

桌面折叠／展开按钮放在侧栏内部：默认位于滚动导航之后、帮助和账户区域之前的固定控制行，36高、图标16，浅蓝面与侧栏协调。它不随菜单长列表滚走，不占品牌区宽度，也不悬浮到正文或卡片上。展开时显示图标＋“收起侧栏”；折叠到64px后保持36×36的“展开侧栏”图标按钮可见、居中、可聚焦，不能把唯一展开入口一起隐藏。aria-label、aria-expanded、图标方向与实际折叠状态在同一次更新中同步；aria-controls指向实际侧栏，点击不触发路由或清空表单。≤960px隐藏桌面折叠控制，由顶栏入口打开完整模态导航；抽屉内部有独立关闭按钮，不沿用窄栏状态。

```html
<!-- 品牌区在侧栏顶部；菜单nav由同一个侧栏实例提供。 -->
<div class="admin-sidebar-brandbar">
  <a class="admin-sidebar-brand" href="/" aria-label="示例管理平台首页">
    <svg class="admin-sidebar-brand__logo" viewBox="0 0 34 34" aria-hidden="true">
      <rect x="2" y="2" width="30" height="30" rx="9" fill="currentColor" />
      <path d="M11 11h12v12H11z" fill="var(--panel)" />
    </svg>
    <span class="admin-sidebar-brand__copy"><strong>示例管理平台</strong><small>MANAGEMENT CONSOLE</small></span>
  </a>
</div>
<!-- 放在nav之后、帮助和账号区之前；控制实际.app-shell状态。 -->
<div class="admin-sidebar-control">
  <button class="admin-sidebar-toggle" type="button" aria-label="收起侧栏"
    aria-controls="console-sidebar" aria-expanded="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m14 6-6 6 6 6" /></svg>
    <span>收起侧栏</span>
  </button>
</div>
```

```css
.admin-sidebar-brandbar { display:flex; align-items:center; justify-content:center; flex:0 0 auto;
  min-block-size:68px; min-inline-size:0; padding-block:12px; border-block-end:1px solid var(--line-soft); }
.admin-sidebar-brand { display:flex; align-items:center; gap:11px; inline-size:max-content; max-inline-size:100%;
  min-inline-size:0; margin-inline:auto; color:var(--text); text-decoration:none; }
.admin-sidebar-brand__logo { display:block; flex:0 0 34px; inline-size:34px; block-size:34px;
  color:var(--accent-link); object-fit:contain; }
.admin-sidebar-brand__copy { display:flex; flex-direction:column; min-inline-size:0; gap:3px; text-align:start; }
.admin-sidebar-brand__copy strong { display:block; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;
  font:700 20px/1.3 var(--sans); }
.admin-sidebar-brand__copy small { display:block; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;
  color:var(--muted); font:400 10px/1.4 var(--sans); }
.admin-sidebar-control { flex:0 0 auto; padding-block:8px; }
.admin-sidebar-toggle { display:flex; align-items:center; justify-content:center; gap:8px; inline-size:100%;
  min-block-size:36px; padding:6px; border:1px solid var(--line-soft); border-radius:10px;
  background:var(--tint-blue); color:var(--accent-link); font:500 12px/1.5 var(--sans); cursor:pointer; }
.admin-sidebar-toggle svg { display:block; flex:0 0 16px; inline-size:16px; block-size:16px; }
.admin-sidebar-toggle:hover { background:var(--panel-strong); }
.admin-sidebar-brand:focus-visible,.admin-sidebar-toggle:focus-visible { outline:2px solid var(--accent-link); outline-offset:2px; }
@media(min-width:961px) {
  .app-shell[data-sidebar-collapsed="true"] .admin-sidebar-brand__copy,
  .app-shell[data-sidebar-collapsed="true"] .admin-sidebar-toggle > span { display:none; }
  .app-shell[data-sidebar-collapsed="true"] .admin-sidebar-brand { gap:0; }
  .app-shell[data-sidebar-collapsed="true"] .admin-sidebar-toggle { inline-size:36px; margin-inline:auto; }
  .app-shell[data-sidebar-collapsed="true"] .admin-sidebar-toggle svg { transform:rotate(180deg); }
}
@media(max-width:960px) { .admin-sidebar-control { display:none; } }
```

真实事件由项目组件接入：用同一布尔状态更新app-shell、按钮label与expanded，品牌／菜单的显隐使用该状态；不通过点击后重建侧栏实现折叠。检查展开、折叠、快速反向、键盘、长品牌、无副标题、短屏和跨960px断点；折叠前后品牌的可见Logo保持居中，帮助／账户缩成可用入口且不撑出64px。宽度／容器变化后图表与正文重新适配，顶部栏桌面不能残留第二个折叠按钮。旧参考图若仍显示顶栏折叠位置，按本节最新归属要求实现，参考素材不因本次规则调整而重制。

**侧栏纠偏提示词：**

```text
按admin-components的侧栏合同修正共享导航。四组使用blue/violet/coral/cyan
稳定映射，组标题前4×10短竖线分别蓝/紫/珊瑚/青、.6透明度，标题仍text-soft。
每个未选菜单有24×24浅色底座、7圆角和17px彩色线框图标，文字12/550。
hover浅蓝整行且保留分组图标色；当前路由才是蓝色渐变整行、白字白图标、
白18%图标底座与白20%计数底。active不被hover覆盖，不出现全灰菜单或长竖线。
来回切换时选中背景与标签/图标/计数同步换色，取消前景color/opacity补间，
保留悬停背景和阴影反馈；菜单节点稳定，不随路由重挂载或让文字淡出再淡入。
折叠仍保留彩色图标与名称入口，手机完整展示分组；不复制业务菜单或假计数。
品牌Logo与双行标题横排垂直居中，整组水平居中；桌面折叠按钮在侧栏内部底部
固定控制行，收起后保留展开入口，窄屏才在顶栏显示模态导航入口。
```

## 按钮：样式、位置与状态矩阵

同一操作组通常只有一个主动作，取消／导出／刷新等按职责降为次操作；不同独立分区可以各有主动作，不把“一处主操作”误解成全页只能有一个按钮。loading保留原按钮占位及相邻控件位置，忙碌文案仍说明正在执行什么，不强制把所有按钮都变成无文字转圈。禁用保留可读名称，必要时提供键盘可达的原因说明；disabled不承担loading或无权限解释的全部语义。触屏沿用既有至少44px命中区约定，不改变桌面可见档位，扩大点击范围时不能与相邻按钮重叠。

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
| TextInput | panel、1px line、38高、10圆角，文字13、padding12，placeholder faint | hover边更清楚；focus同一外壳边界加深并向内强调，不叠第二框；error红边+错误句；disabled panel-muted、muted；readonly保持可选择复制 |
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

<a id="clean-admin-input-surface"></a>

### 一体式输入面：前后缀不能出现灰色拼接块

普通输入、搜索、密码、日期与可输入Select的内部图标区，应与文字区使用连续的一张表面。浅色是统一panel面，深色引用深色panel；外壳统一负责背景、1px边框、10px圆角和焦点强调，内部input、prefix、suffix、清除／显隐按钮的常态背景透明，无第二层边框、内阴影或独立胶囊。不能出现“灰色搜索图标底＋白色输入区＋灰色右端”、双圆角白色小内胆或两端月牙状色块；图标用muted／text-soft，不加独立浅灰方形底座。

接入组件库时检查实际wrapper、inner input、prefix／suffix容器、clear按钮以及::before／::after的background、border和box-shadow，修正当前字段组件的主题映射与规则优先级。不要只把input涂白，留下外壳两端原有灰底；不要靠overflow:hidden裁掉内层或全局input／button重置掩盖问题。搜索为空时不显示占位灰块，有值时清除按钮仍与输入面融合；内侧左右留白统一12px，图标16px、间距6–8，长文本可编辑且不盖住后缀。

**填写内容不改变字段底色。**手动输入、粘贴、浏览器自动填充、密码管理器回填、失焦再聚焦后，浅色可编辑字段始终是连续白面，深色始终是连续深色panel；不得按非空值、:valid、:placeholder-shown或库的filled状态给文字区增加灰蓝色背景。hover、focus、error、readonly也不另铺文字区色块。搜索左右的wrapper、prefix、suffix和清空按钮在这些状态下都必须与文字区连成一面，不能仅默认空值截图正常。

自动填充需单独适配：保留正确autocomplete，不用关闭自动填充、数小时background过渡或定时重置value绕开浏览器。浏览器可能用UA重要规则绘制底色，单写background:transparent不够；在字段内部用不透明panel色的inset填充覆盖该底色，显式同步文字与caret颜色。该填充只负责表面，唯一焦点边界仍由外壳绘制。保留可访问的回填状态，例如字段下固定说明位显示“已自动填充，可直接修改”，不要用对比突兀的蓝底表达。强制颜色模式撤销自定义覆盖并交回系统；未支持的回填选择器保留原生行为，不添加JS填色补丁。

**再次点击不能闪蓝底：瞬态与终态同样验收。**登录账号／密码和页面内输入、搜索在pointerdown、active、focus／focus-visible、失焦再进入、自动填充候选预览／确认／取消及回填后编辑时，文字区与整框都不能先闪蓝／灰蓝再恢复。字段外壳仅允许原边界的颜色变化，背景不补间；内部input的背景、background-image、填色用box-shadow及文字颜色不参与transition／animation，不用transition:all。特别排查库的is-focus／filled／active类、全局input:focus和自动填充阴影重置，避免遮盖层从none插值到不透明，或聚焦那一帧被移除。下方最小实现将同主题的不透明内填充在普通及回填状态持续保留，且不做过渡；prefix／suffix仍透明，不因修复重现两端拼接块。

点击只放置光标，不由业务脚本额外执行select()／setSelectionRange全选来制造整块蓝底。用户主动拖选、双击、键盘选择／全选时，正常文本选区高亮必须保留；不能用透明::selection、user-select:none、隐藏caret或强制blur消掉表面问题。原生密码管理器候选面板与页面输入底色是两回事：保留候选和正确autocomplete，不伪造／隐藏系统候选，不以禁用粘贴、回填或替换密码管理器解决闪色。仅凭录屏不能断定具体规则，修目标项目时需结合实际DOM／样式与浏览器回填检查。

**文字字重也必须稳定。**普通输入、已填写值、聚焦、自动填充、候选确认／取消、密码显隐和失焦再进入均沿用正文输入字重（默认400）与同一字体、字号、行高、字间距；不能因为非空／filled／focus／autofill给文字加粗、套系统粗体或改变字宽。需要强调字段状态时只改外壳边界，不改输入文字。真实产品若业务明确要求粗体，必须由该字段的设计合同单独说明，不能由浏览器或组件库状态隐式触发。

**聚焦也只能有一圈完整字段边界。**有包装层的输入由包装层统一绘制边框，内部input在focus／focus-visible时不另绘border、outline、焦点box-shadow或圆角框；同色内填充阴影持续保留；包装层聚焦只把原边界变为accent-link，并在同一边界向内增加1px强调，不加有间隙的外圈、3px扩散环或第二个套框。独立input没有包装层时由input自己承担这唯一边界；不能外壳和input同时画。保留清晰键盘焦点，不用全局outline:none取消其他组件焦点；清除／显隐等独立按钮聚焦时允许其自身的小范围标识，但不能产生覆盖文字区的第二个大矩形。库wrapper的is-focus、内部input:focus和全局input规则、浏览器默认搜索框样式都要实际检查，并在字段作用域解决冲突。

下方为无组件库时的最小表面实现；已有可靠库时映射到其结构，保留输入、搜索和清除行为。不额外创建前端工程。

```css
.admin-input { display:flex; align-items:center; gap:8px; min-inline-size:0;
  --input-focus:var(--accent-link); --input-surface:var(--panel);
  min-block-size:38px; padding:0 12px; border:1px solid var(--line); border-radius:10px;
  background:var(--input-surface); color:var(--text); transition:border-color 160ms ease; }
.admin-input > input { flex:1; min-inline-size:0; inline-size:100%; min-block-size:36px;
  margin:0; padding:0; border:0; border-radius:0; background:transparent;
  box-shadow:inset 0 0 0 100vmax var(--input-surface); transition:none; animation:none;
  color:inherit; caret-color:var(--text); font:400 13px/1.5 var(--sans);
  font-weight:400; font-synthesis:none; font-variation-settings:normal; letter-spacing:normal; }
.admin-input > input::placeholder { color:var(--faint); opacity:1; }
.admin-input > :is(.admin-input__prefix,.admin-input__suffix) {
  display:inline-flex; align-items:center; flex:0 0 auto; color:var(--muted);
  background:transparent; border:0; box-shadow:none; }
.admin-input svg { display:block; inline-size:16px; block-size:16px; flex-shrink:0; }
.admin-input .admin-input__action { display:grid; place-items:center; inline-size:24px; block-size:24px;
  padding:0; border:0; border-radius:5px; background:transparent; color:var(--muted); box-shadow:none; }
.admin-input .admin-input__action:hover:not(:disabled) { background:transparent; color:var(--accent-link); }
.admin-input:hover:not(:has(input:disabled)) { border-color:var(--text-soft); }
.admin-input:focus-within { border-color:var(--input-focus); box-shadow:inset 0 0 0 1px var(--input-focus); }
.admin-input > input:is(:hover,:active,:focus,:focus-visible) {
  background:transparent; background-image:none;
  box-shadow:inset 0 0 0 100vmax var(--input-surface); transition:none; animation:none;
  font-weight:400; font-synthesis:none; font-variation-settings:normal; letter-spacing:normal;
}
.admin-input > input:focus { border:0; outline:none; } /* 外壳提供唯一可见焦点，内填充不移除 */
.admin-input > input:is(:autofill, :-webkit-autofill) {
  box-shadow:inset 0 0 0 100vmax var(--input-surface); transition:none; animation:none;
  -webkit-text-fill-color:var(--text); caret-color:var(--text); font-weight:400;
  font-synthesis:none; font-variation-settings:normal; letter-spacing:normal;
} /* 回填与非回填同一不透明填充，无进入／离开补间；panel必须为纯色 */
.admin-input:has(input:disabled) > input:is(:autofill, :-webkit-autofill) {
  box-shadow:inset 0 0 0 100vmax var(--input-surface);
  -webkit-text-fill-color:var(--muted);
}
.admin-input .admin-input__action:focus-visible { outline:2px solid var(--accent-link); outline-offset:1px; }
.admin-input:has(input[aria-invalid="true"]) { --input-focus:var(--red); border-color:var(--red); }
.admin-input:has(input:disabled) { --input-surface:var(--panel-muted); color:var(--muted); cursor:not-allowed; }
.admin-input > input:disabled { color:inherit; opacity:1; cursor:not-allowed; }
@media(pointer:coarse) {
  .admin-input { min-block-size:44px; }
  .admin-input > input { min-block-size:42px; font-size:16px; }
  .admin-input .admin-input__action { inline-size:44px; block-size:44px; }
}
@media(forced-colors:active) {
  .admin-input { border-color:CanvasText; }
  .admin-input:focus-within { outline:2px solid Highlight; outline-offset:-2px; }
  .admin-input > input,.admin-input > input:is(:hover,:active,:focus,:focus-visible) {
    box-shadow:none; caret-color:auto;
  }
  .admin-input > input:is(:autofill, :-webkit-autofill) {
    box-shadow:none; -webkit-text-fill-color:FieldText; caret-color:auto;
  }
  .admin-input:has(input:disabled) > input:is(:autofill, :-webkit-autofill) {
    box-shadow:none; -webkit-text-fill-color:GrayText;
  }
}
```

disabled可让**整框**使用panel-muted，不能只让两端变灰；同时禁用清除／显隐按钮。readonly仍可聚焦、选择和复制；error保留真实错误说明，不只改红边。loading只替换后缀图标，不另加灰底、不改变高度。上述CSS面向直接子input，组件库嵌套结构必须映射到真实节点，不能假定选择器已命中。单位Select、步进器、明确的prepend／append操作属于有意分区，沿用对应组件合同，不强行移除必要边界。

最小实现中内部input的inset只负责持续遮盖UA填色，不是第二层焦点阴影；与外壳共用同一个input-surface，正常、聚焦、回填／退出回填均不可被库shadow重置清空。已有库使用其对应主题／样式入口，在该字段作用域检查最终优先级，不靠延时追加样式让首帧先露出蓝底。强制颜色模式交回系统绘制，不能为了截图强制抹除用户系统颜色。

验收时在浅色／深色下实际查看空值、有值、长值、hover、输入聚焦、清除按钮聚焦、清空、disabled、readonly、error和loading。登录账号与密码分别验证手动输入、粘贴、浏览器自动填充及回填后编辑；搜索验证空值／有值／聚焦／失焦时两端。分别检查左图标区、文字区、右后缀区及四个圆角的实际绘制；不能仅检查input的computed background，自动填充需看实际绘制与caret。确认全框底色连续、聚焦前后都只有一圈完整字段边界、焦点清楚、无灰蓝文字底／灰色端盖／双圆角／内外套框／裁切，清除后焦点仍在输入，禁用动作不执行，390宽与浏览器缩放不挤出边界。伪状态强制只能验证CSS，不能冒充实际密码管理器回填测试；未运行状态须说明。

再执行“已有值→点空白失焦→再次点击账号→切密码→重复点击／Tab切换”，包括候选列表出现、选择、取消、回填后增删一字、密码显隐；录屏逐帧核对pointerdown起的首帧及随后约300ms，而非只截稳定后的画面。无主动选区时，文字之外的整块字段面在各帧持续保持当前主题底色；正常拖选、全选、caret、输入值与密码管理器仍可用。对比填写前、聚焦、候选打开、回填后和再次点击时的computed font-family／font-size／font-weight／line-height／letter-spacing，字重必须保持400且不能被filled／autofill规则改粗。浏览器可强制伪状态验证CSS覆盖，但真实候选预览与系统密码管理器必须单独实测并记录，不能据此承诺所有浏览器都已验证。

**表单提示词：**

```text
统一38px普通字段和42px登录字段，10px圆角，白面细灰边，标签13、正文13、
帮助12。前后缀16px并预留空间；focus在同一外边界用accent色向内强调，不叠外框，错误用红边和字段下
说明，disabled只读和loading各有真实区别。双列表单每列min-width:0、gap20，
手机单列；不要用placeholder代替标签或让红色校验文字遮住下一个字段。
普通输入和搜索按一体式输入面合同：外壳统一底色/边框/圆角/单层焦点强调，内部input、
图标前后缀及清除按钮透明，不出现两端灰色块或白色内胆；禁用整框统一变色。
填写、粘贴、自动填充、readonly及重新聚焦不改变文字区底色；按本节覆盖UA
自动填充底色并同步文字/caret，保留autocomplete、可访问回填说明和单层焦点。
再次点击、切换账号/密码及候选预览/取消时也不能先闪蓝再恢复；外壳只过渡边框，
内部填色不补间且不因focus被移除，不用transition:all或延时重置样式。逐帧检查
点击首帧到稳定态；输入字重保持400，不因filled/autofill/focus加粗；正常文本选区高亮、caret、密码管理器和粘贴保留。
```

## Switch、Checkbox、Radio与Segmented

| 控件 | 本风格默认 | 语义与状态 |
|---|---|---|
| Switch | 40×20左右胶囊起点，thumb16、两侧2；开accent、关中性灰，必要时短“开／关”文字 | 保留项目库可访问实现；指示位置+名称表达值；saving时pending、失败回滚；表单保存型不伪称即时生效 |
| Checkbox | 可见框16，圆角4，选中accent白Check，框与标签gap8 | unchecked／checked／indeterminate／disabled／focus俱全；大命中区wrapper；半选不是另一项真实值 |
| Radio | 圆16，外边line、选中accent外环和中心圆点，标签gap8 | 单组选一，方向键；选中后不直接清空，允许无选择时提供明确选项；Select单选内部不用Radio圈 |
| Segmented | 高38、padding4、外11内7圆角，共享蓝渐变indicator，单项字11–12 | 同组等分短文案，默认值有效；选中标签／图标／计数在hover、按下和focus-visible时仍为白色，蓝底不能被白色hover面覆盖，按钮保持透明；未选蓝字；键盘可达；280ms移动；完整状态CSS见admin-navigation |
| Toggle／Chip | 28–32高紧凑标签、左右8–10、圆角7，未选浅面／选中浅蓝蓝字 | 多选和单选通过实际语义表达；删除chip有独立按钮名称，不因hover才让触屏用户看到删除 |

长说明选项使用纵向Radio或选择卡，每项边框面与标题说明成组，间距10–12、padding12，不强塞窄分段控件。选择卡属于同风格扩展，不使用四色统计卡表达选项状态。

## 面板、摘要卡、资源卡与图表

### 业务 Panel

主面panel、line-soft 1px边、圆角16、workspace-card-shadow；header左右20、上下18–20，标题16／600，右侧小计或次动作。body通常20，header/body分隔只在需要独立工具区时出现。嵌套信息用圆角12浅蓝／淡紫子面，不再包一张同样阴影的主卡；最多让业务层级清楚，避免“卡片套卡片套卡片”。

同排同类卡片的操作区按[信息排版合同](#clean-admin-information-layout)对齐；内部说明用间距和必要细线分组，保留资源卡已有蓝／紫子面的业务层级，不为扁平化删除有效内容。

### 独立面板之间保留区块间距

有各自背景、边框或圆角的相邻区块，按独立面板排列，外边界之间必须有清楚的间距；面板内部padding不能代替面板之间的gap。普通页面卡片默认20px，元信息／说明面等同属一组的紧凑区块16px；≤600px分别14px和12px。例如文档顶部“适用范围／接入标识／服务地址”信息面板与下面“API基地址／版本”条是两个面板，使用紧凑16px间距，不把下方条贴在上方圆角或边框上。

同一父布局使用Grid／Flex的gap统一管理，不逐项叠加margin；不使用负margin、绝对定位或translateY消掉间隙，也不要全局给所有带border的元素加margin。一个面板内部的标题／正文／页脚可以共用边界、用细线分隔；有意的按钮组、输入组合不按独立面板处理。

```css
.admin-panel-stack { display:grid; min-inline-size:0; gap:20px; }
.admin-panel-stack--compact { gap:16px; }
@media(max-width:600px) {
  .admin-panel-stack { gap:14px; }
  .admin-panel-stack--compact { gap:12px; }
}
```

实际测量相邻面板的border box距离，而非只检查gap声明：排除子项margin、负偏移或transform使可见边框仍接触。检查长内容换行、展开收起、窄屏改列、错误说明增高和主题切换，边框／圆角始终分离，阴影低调、不因间距叠加形成大空洞；内容自然增高不覆盖下一面板。

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

每张可导航的大KPI都有**始终可见**的右上圆入口，标题与入口在同一header行，不能换成标题左侧的图标方块。圆按钮桌面32×32、1px白28%边、黑15%面；与顶部和右边均隔24px。内部15×15图标是**无箭杆的细右尖括号形chevron**，使用下方基准SVG路径：未旋转时只有构成右尖括号的两条细边，默认旋转−40deg后呈右上折角。不能用完整的ArrowUpRight／带箭杆Right、外链图标、字符↗或加粗箭头替代，不能给基准填充路径额外描边。

四卡共用同一基准图标，不按业务更换右上入口形状；按业务变化的是右下背景图标。基准viewBox为0 0 1024 1024，fill=currentColor、stroke=none，不把1024坐标路径塞进24的viewBox，也不加stroke-width来模拟粗细。仅入口hover／focus-visible时旋回0deg，终态是细右尖括号，面变白24%；离开或失焦反向恢复。圆入口旋转200ms ease，卡片hover上移3px／180ms ease，二者独立，不移动数字与hint。≤600时圆入口40×40，内部图标仍为15×15，header内margin-block:-6px，为触屏保留入口。

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
      <svg viewBox="0 0 1024 1024" fill="currentColor" stroke="none" aria-hidden="true" focusable="false">
        <path d="M340.864 149.312a30.59 30.59 0 0 0 0 42.752L652.736 512 340.864 831.872a30.59 30.59 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z" />
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
  fill:currentColor; stroke:none; transform-origin:50% 50%;
  transform:rotate(-40deg); transition:transform 200ms ease; }
.admin-kpi__open svg path { fill:currentColor; stroke:none; }
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
每张卡右上始终显示32px圆形链接，内部15px的无箭杆细chevron用本节基准SVG，
不是完整↗、ArrowUpRight或加粗箭头。默认-40deg，hover/focus-visible时200ms
转到0deg成为细右尖括号并亮面；离开复原，卡片独立180ms上移3px。点击直接跳到
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
表格的横向滚动局限于table容器；竖向默认随页面增高，明确需要固定高度时才启用表内竖滚。按[滚动条与容器规范](admin-design.md#clean-admin-scrollbars)统一细度、主题和边界，滚动体留在圆角面板内；批量操作栏不遮挡最后一条记录或分页。
```

## Dialog、Drawer、Dropdown、Tooltip与反馈

| 组件 | 几何／材质 | 内容与状态 |
|---|---|---|
| 普通表单Dialog | 默认520宽、最大calc(100vw−32px)、16圆角、panel面；头20 24、体20 24、脚16 24 | 标题18、说明13，关闭32；字段38；页脚取消在左、主操作在右、gap8；长内容体滚动，头脚不被裁掉 |
| 危险确认 | 默认440宽、20圆角；小图标底座36、标题16、正文13 | 说清对象／数量／后果；取消次按钮+red确认；点遮罩不可执行确认；不要输入不存在的恢复承诺 |
| 详情Drawer | 默认520、最大100vw、左侧圆角16；body浅底padding20、子面14圆角 | header标题20，独立关闭；内容分组小蓝条，ID／状态／事实项有层级；手机全宽可用 |
| Dropdown Menu | panel面、细边、10圆角、padding6、item32高、左右10、图标16／文字12–13 | hover浅蓝，危险red，disabled muted；键盘上下／Esc，触发器保持名字；主题／账户入口菜单优先按[顶部栏紧凑菜单](admin-topbar.md)的4px外壳padding、8px行padding及max-content收宽，不继承入口宽度；大段输入不放菜单 |
| Tooltip | panel混2%蓝、20%蓝边、圆角8、padding6 10、12字、max360宽 | 使用下方自定义气泡合同，禁止title触发浏览器默认提示；show180／hide100／offset8，hover及focus；无交互简短解释，箭头同色；触屏入口不能依赖hover |
| Popover | 12圆角、padding16、标题14、正文13、细边轻阴影 | 有交互则能移入与聚焦；依据职责关闭，不从timer误关内部焦点 |
| Toast | 自适应宽、max360、圆角10、padding12 16、图标16与13文字、轻阴影 | 成功短时反馈，失败持久行内为主，不堆重复通知；文案变长可换行；不固定显示截图里的偶然Toast |
| Inline Alert | 浅语义色面、细边、10–12圆角、padding12 16，图标20 | 标题13／600、说明12–13、有效重试；局部出错只影响对应区域 |
| Empty State | 正文区域居中，图标32–48、标题16、说明13、距操作16 | 真空、无结果、无权限与失败分别描述；没有恢复能力不画假按钮；不替换整套后台壳层 |
| Skeleton | 与最终卡／表格同列数、同外框、低对比块 | 未到数据不显示全0；默认静态、无shimmer，刷新失败可保留旧数据 |

弹层、Switch、Select、Checkbox等优先使用目标项目已有库的语义和焦点实现，再统一视觉。上表宽度／密度是本风格默认约定，不是要求重写库或新增依赖。库portal也读取主题，浮层方向箭头颜色一致；Dialog和Drawer只有一个层负责进出动画，遮罩不要变成夸张深黑或多重毛玻璃。

<a id="clean-admin-custom-tooltips"></a>

### 悬停气泡统一设计，不使用浏览器默认title提示

日期时间、截断名称／ID、版本、侧栏折叠项、图标按钮及帮助说明等后台自有提示，统一使用共享Tooltip组件；不能把完整内容只写入HTML的title／框架:title绑定，留给浏览器绘制灰色系统提示。沿用已有组件库可靠的Tooltip并映射本节主题，不要求从零重写；原生Popover可以承载自定义气泡，但必须自行落实外观与交互，不能保留UA默认外框。图表数值提示继续按[图表专节](admin-workbench.md#clean-admin-chart-tooltips)处理，不混用其6px数据锚点规则与本节普通标签offset8。

**外观合同：**浅色气泡采用panel混2%accent的近白面、accent20%混line-soft的1px细边；深色读取相同语义token得到协调的深面。正文text、12px／1.5、padding6px 10px、8px圆角，宽度按内容自然收紧，最大min(360px,视口−24px)，无固定最小宽或大面积空白。短日期时间保持一行，长文件名／解释可断行，不强制截成第二个省略文本。轻阴影沿用浮层token，无重灰渐变、系统黑框、厚阴影或毛玻璃。箭头12×7px，与气泡同色、根部无穿线／白缝，四向外轮廓连续；复用图表专节已验证的无接缝做法并映射气泡的背景／边框token，不能固定白色遮盖深色箭头。

**迁移title时保留语义：**检查实际触发节点、嵌套子节点、父级继承title，以及表格overflow-tooltip、日期格式化组件、图标组件自动透传的title。移除当前自定义提示重复的原生title来源，必要时在局部阻断继承；不要在应用挂载后全局遍历删除所有title。SVG的title可能承担可访问名称，先以正确aria-label／aria-labelledby等保留名称，再处理重复的浏览器提示；页面文档title、表单label、img alt和其他无关原生行为不删除。日期弹出完整时间，沿用产品既有时区和格式，不把演示日期硬编码；复制仍用完整原值。

**交互与可访问性：**

- 指针初次停留180ms打开，最后离开触发器与气泡的联合区域100ms后关闭；仅采用库的一套延时。移入气泡正文继续可读，不能pointer-events:none导致一进入就消失；仍无按钮、链接或输入，有交互则按Popover处理。详细意图判断另按[悬停配方](recipes/hover-intent.md)，不叠两组timer。
- 键盘聚焦有意义的触发器可立即显示，不移走焦点；气泡role=tooltip、有唯一ID，额外说明通过aria-describedby关联。图标按钮始终有独立可访问名称，气泡若只重复该名称不再重复描述；不设aria-live、不对纯提示添加aria-haspopup或假展开状态，不覆盖已有描述。静态日期／文本不一律加Tab停靠点：完整值已可见时不必重复提示，截断或补充信息有需要才提供合适焦点／查看入口。
- Escape可在不移动鼠标／焦点时关闭并取消待打开任务；同一停留或聚焦周期内抑制自动重开，离开后重新进入才恢复。无自动几秒消失；指针或焦点仍在有效阅读区域时保持，离开、内容失效、路由卸载后清理。触摸提供可见完整文本、详情或有名称的信息按钮，不吞掉链接／按钮首次点击来展示提示，不依赖长按作为唯一入口。
- 优先上方或按组件职责放置，与实际触发器相邻且不遮挡触发器／焦点；边缘翻转后箭头同步回指，滚动／resize更新或关闭，不留悬空旧气泡。沿用已有portal与定位库，不被表格overflow裁切，也不滚动页面来迁就气泡。单一提示作用域最多显示一个气泡；自定义层与原生title不得同时出现。

若独立使用interestfor／popover=hint等平台能力，实施前按目标浏览器做功能检测与必要回退；已有库无需改为该API。缺少hint支持时不能把永不轻关闭的manual当完整回退，缺少anchor定位时由可靠定位回退保持贴近触发器，不能放到屏幕中央。不要为替换title新增依赖或用纯CSS伪元素代替完整语义和关闭逻辑。

验收鼠标移入后完全静止、快速掠过、显示后再停留至少3秒（检查无原生title叠层）、跨入气泡、离开、Escape原地关闭及重新进入；再查键盘聚焦、触屏等价入口、长文本、浅深主题、表格滚动和边缘翻转。检查目标及祖先／子节点是否仍透传title，确认只有一份设计后的气泡。实际业务项目未操作验证时标明未验证，不以静态截图证明悬停时序。

## 按业务启用的编辑、敏感字段与恢复反馈

仅当目标产品已包含或用户要求相应能力时使用下表，不据此自动创建业务页或增加审批步骤。

| 模式 | 适用边界与实现要求 |
|---|---|
| 敏感字段（Secret Field） | 密钥／令牌默认遮蔽；显示、隐藏、复制分别有明确名称和权限，显示后保持单一输入面、等宽字符与稳定占位。没有权限不把完整值先送到前端再遮住；已遮蔽响应不假装能还原，不能复制一串占位符并宣称成功。可查看何种前后缀按产品策略，不统一硬编码 |
| 行内编辑（Inline Edit） | 适合名称／备注等简短值；提供可发现且键盘可用的编辑入口，编辑时使用现有字段焦点规则。保存／取消语义明确，组合输入期间Enter不误提交，取消恢复原值，保存失败保留草稿和错误；复杂字段继续用正式表单，失焦不悄悄丢失内容 |
| 撤销反馈（Undo Toast） | 仅对后端确实支持恢复的归档／移除等动作提供撤销；撤销接真实逆操作、显示执行状态与失败原因，键盘与触摸可执行。不把不可逆删除改成先删后假撤销；时限按业务并让用户能读到和完成操作，重要结果不能只靠短暂Toast |
| 差异查看（Diff View） | 配置发布／版本比较／内容审核确有需要时显示前后差异，增删除颜色外保留标记／文字；接受／拒绝或保存接真实数据。若含凭据继续遵守遮蔽和权限，不能为了比较回显秘密 |
| AI输出与工具状态 | 只有包含AI业务时才添加流式输出、引用、工具状态或审批卡；状态来自真实执行，来源可追溯。不显示虚构推理或工具进度，不把通用后台操作都加审批。需要审批时按既有产品权限与明确业务规则展示影响范围和确认／取消 |

## 逐组件验收与反例

逐个打开该页面用到的组件，依次核对默认、hover、press、键盘focus、disabled；异步组件再看loading、success、error。状态之间bounding box尺寸保持稳定；必需的文本换行属于自然增高，不能为了截图一致裁掉错误。

以下情况属于样式偏离，需在目标项目修正：主按钮没有渐变／高光；所有圆角都变24；表单全部48–56高；导航选中只有一条蓝线而没有蓝色渐变面；图标变成emoji／实心杂色图；普通摘要错误采用大KPI结构；所有字段无标签；文字与图标基线不齐；select展开为另一套深色主题；loading改变按钮宽度；箭头按钮只变背景却不铺底；不同页相同状态色和字号不一致。

长表单、长名称、空数据与窄屏要处理真实内容压力；从同一组件与token调整，不能为通过一张静态图而硬编码文本、绝对定位所有字段或禁用浏览器缩放。
