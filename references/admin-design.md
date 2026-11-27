# 清爽蓝白后台：布局、主题和组件规范

本规范用于创建具有相同视觉语言的后台。与 [完整配方](recipes/clean-admin.md)、[逐页提示词](admin-pages.md)、[组件与按钮状态](admin-components.md)、[完整顶部栏](admin-topbar.md) 和 [动效说明](admin-motion.md) 配套；只将相关代码片段移植到目标项目，不需要在 skill 中附带前端工程。

## 样式执行优先级与稳定项

选择本风格后，不能再把它视为“蓝白色灵感”。用户明确指定的设计与可访问性需求优先；除此之外依次采用本文件的token／壳层、组件规范的尺寸与状态、逐页规范的组合、参考图的可见细节。参数未覆盖的情况从同职责组件扩展，并明确是补充默认值，不伪装为原图测量值。

必须保持：浅蓝画布；独立悬浮白色侧栏与顶栏；蓝色渐变选中菜单和主按钮；明确的紧凑字号；四色摘要及其装饰；低阴影白色业务面板；浅蓝／淡紫信息子面；专用箭头展开按钮及动效。它们不能只保留一两项便称为相同风格。

允许调整：目标品牌、菜单名称、字段、数据、指标数量、业务动作、长内容自然高度及按职责扩展的页面。缺少某业务区块可以省略；保留区块的尺寸与层级不随意改。

基础尺寸单位为CSS px、border-box、浏览器100%缩放。图像DPR2只增加参考像素，不增加UI逻辑尺寸。不要使用zoom、整页transform scale或所有字号乘1.25来迎合参考图。不同字体存在字宽差异，允许自然换行与轻微光学调整，不能覆盖核心比例。

## 视觉基线与主题

保留浅蓝画布、细蓝边界、独立的圆角白色侧栏／顶栏、低阴影面板、蓝色渐变主操作，以及四色摘要卡。彩色集中于导航选中、摘要和操作；正文、表单、表格与阅读面保持安静。

以下是这套风格采用的语义值，组件引用变量，不能在每页重写同一颜色。Element Plus 或其他库的色彩与浮层也须映射到同一 token。

```css
:root {
  --sans: "Avenir Next", "PingFang SC", "Microsoft YaHei", sans-serif;
  --mono: "SFMono-Regular", "Cascadia Code", "Roboto Mono", monospace;
  --sidebar-width: 256px;
  --console-header-height: 68px;
  --motion-spring: cubic-bezier(.2,.75,.25,1);
  --summary-violet: linear-gradient(115deg,#923cd1,#ba68df);
  --summary-coral: linear-gradient(115deg,#db6a58,#efa28a);
  --summary-rose: linear-gradient(115deg,#d84f81,#ed8ba5);
  --summary-cyan: linear-gradient(115deg,#149dcc,#59c4e3);
  --workspace-card-shadow: 0 3px 18px rgba(57,106,188,.035);
  --shadow-sm: 0 1px 2px rgba(0,0,0,.04);
}
:root, :root[data-theme="light"] {
  color-scheme: light;
  --bg:#f3f7ff; --panel:#fff; --panel-muted:#f5f8ff; --panel-strong:#edf3ff;
  --text:#202020; --text-soft:#525252; --muted:#686868; --faint:#757575;
  --line:#dcdcdc; --line-soft:#eaf0f8;
  --accent:#2478ff; --accent-strong:#1761dc; --accent-link:#175dc8; --accent-ink:#fff;
  --green:#287553; --red:#c34b67; --amber:#95601b;
  --tint-blue:#edf4ff; --tint-purple:#f4f0fa; --tint-cyan:#edf8fa;
  --tint-green:#eff8f2; --tint-amber:#fff7e9;
  --workspace-blue-line:#dfeaff; --workspace-lilac-line:#e8dff9;
  --workspace-blue-surface:linear-gradient(125deg,#eef5ff,#f5f9ff);
  --workspace-lilac-surface:linear-gradient(125deg,#f3eeff,#f9f6ff);
  --chart-license:#1769ff; --chart-activation:#27c9d5;
  --chart-mint:#31cfa1; --chart-orange:#ff964b; --chart-purple:#ba68e3; --chart-pink:#f4789d;
}
:root[data-theme="dark"] {
  color-scheme:dark;
  --bg:#141414; --panel:#1c1c1c; --panel-muted:#181818; --panel-strong:#252525;
  --text:#f5f5f5; --text-soft:#d4d4d4; --muted:#aaa; --faint:#969696;
  --line:#424242; --line-soft:#303030;
  --accent:#6aa8ff; --accent-strong:#88baff; --accent-link:#88baff; --accent-ink:#181818;
  --green:#8cd6ac; --red:#f3a4b1; --amber:#e6bc7f;
  --tint-blue:#1c3150; --tint-purple:#31253b; --tint-cyan:#1d3237;
  --tint-green:#1d3027; --tint-amber:#362d20;
  --workspace-blue-line:#354663; --workspace-lilac-line:#443553;
  --workspace-blue-surface:linear-gradient(125deg,#1c293c,#202b3e);
  --workspace-lilac-surface:linear-gradient(125deg,#2b233c,#29263a);
  --chart-license:#70a3ff; --chart-activation:#53d7df;
  --chart-mint:#5bd8ac; --chart-orange:#ffb075; --chart-purple:#cf93f0; --chart-pink:#f6a2bb;
  --workspace-card-shadow:0 3px 18px rgba(0,0,0,.08);
}
```

字体使用系统回退，不下载商业字体；不同操作系统的字形和占宽会有差异。字体基准为正文 14px、标签 13px、说明 12px；此套紧凑控件有 10–12px 辅助信息，不把小号辅助字当作所有正文的尺寸。大标题一般 26px／1.3、650，概览标题 30px；KPI 38px／1.2、650，tabular-nums；标题字距约 -.035em 到 -.04em。

未设置data-theme时默认浅色；需要深色时在首屏绘制前按目标项目已有主题机制设置dark。四色摘要在两种主题下使用同一渐变，不因深色模式给整张卡叠黑色蒙层或降低brightness。普通主按钮继续用蓝色渐变白字，专用箭头展开按钮才使用自身accent／accent-ink，不将两种variant的前景色混用。

## 壳层的几何

| 区域 | 桌面规则 | 窄屏规则 |
|---|---|---|
| 外层 | Grid：256px + minmax(0,1fr)，最小高度 100dvh | ≤960px 改单列，导航改抽屉 |
| 侧栏 | fixed，距左／上／下 12px；宽 232px；内边距 12px；圆角 20px；蓝色细边 | 展开宽 min(280px,视口−32px)，背景不可交互；关闭后恢复焦点 |
| 折叠侧栏 | 外层第一列 88px，实际侧栏宽 64px；标签／计数隐藏，保留可访问名称 | 抽屉始终显示完整标签，不沿用图标折叠态 |
| 侧栏品牌 | min-height68，标记34px与双行标题横排、垂直居中；整组在侧栏可用宽度内水平居中，左右留白对称；标题20px | 长名可截断并提供完整可访问名；折叠只保留居中Logo；按组件规范品牌合同 |
| 菜单项 | 最小高42px，内边距8px 10px，图文gap10px，组内gap5px，圆角11px；彩色图标底座24px／7px、内部SVG17px；组前4×10px彩色短竖线 | 命中区须能触摸操作，图标有文字或aria-label；分组配色和状态见组件规范侧栏合同 |
| 顶栏 | 独立白色面板；margin 12px 28px 0 16px；圆角18px；内容高68px；横向内边距18px | ≤1280px右margin24px；≤960px margin 12px 20px 0、内边距20px；≤600px margin 8px 12px 0、圆角14px、内容高60px、内边距10px |
| 顶栏控件 | 图标按钮36px／10px；搜索宽clamp(170px,20vw,260px)、高36px；头像26px／8px | 手机搜索缩为36px图标按钮，隐藏搜索文案、连接状态与用户名，保留入口 |
| 正文 | max-width 1620px；padding 26px 28px 48px 16px；子项min-width:0 | ≤1280px 24px 24px 40px 16px；≤960px 24px 20px 32px；≤600px 20px 12px 28px |
| 页标题 | 分组标记 + h1 + 说明 + 右侧主次操作；min-height约94px，底部14px与细线，之后24px | 手机上下排列，操作区可占整行 |
| 面板 | 白色、边界line-soft、圆角16px、workspace-card-shadow；面板间20px | 在容器内重排，不能靠隐藏溢出解决碰撞 |

独立面板外边界间距默认20px，同组紧凑信息面板16px；≤600px分别14px／12px。容器统一用gap，不能让两张卡的圆角或边框贴在一起；详情见组件规范的面板间距合同。品牌与折叠按钮遵守组件规范的新归属：品牌整组居中，桌面控制在侧栏内，窄屏顶栏只负责打开完整导航。

顶栏在普通文档流中，不默认 sticky；长内容收起时，固定顶栏与浏览器滚动锚定混用可能造成“顶栏突然掉下来”。侧栏导航区域独立滚动，品牌、搜索、底部帮助与用户区不随菜单滚走。下方壳层CSS只提供几何，顶部栏内部必须按 [完整顶部栏规范](admin-topbar.md) 的结构、基准图标、底座、搜索胶囊、状态、主题、刷新及头像账户实现，不能把空白header当作已完成。

```css
/* 合并到目标项目的reset；结构为.app-shell > .sidebar + .workspace。 */
*, *::before, *::after { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--text); font:400 14px/1.5 var(--sans); }
.app-shell { --sidebar-panel-width:232px; display:grid;
  grid-template-columns:var(--sidebar-width) minmax(0,1fr); min-height:100dvh; }
.app-shell[data-sidebar-collapsed="true"] { --sidebar-width:88px; --sidebar-panel-width:64px; }
.workspace { grid-column:2; }
.workspace,.content,.panel { min-inline-size:0; }
.sidebar { position:fixed; inset:12px auto 12px 12px; inline-size:var(--sidebar-panel-width);
  display:flex; flex-direction:column; padding:12px; border:1px solid var(--workspace-blue-line);
  border-radius:20px; background:linear-gradient(180deg,color-mix(in srgb,var(--accent) 3%,var(--panel)),var(--panel) 42%);
  box-shadow:0 4px 20px rgba(57,106,188,.04); }
.sidebar nav { flex:1; min-block-size:0; overflow-y:auto; overscroll-behavior:contain; }
.console-masthead { margin:12px 28px 0 16px; border:1px solid var(--workspace-blue-line);
  border-radius:18px; background:var(--panel); box-shadow:0 4px 20px rgba(57,106,188,.04); }
.topbar { display:flex; align-items:center; gap:16px; block-size:68px; padding-inline:18px; }
.content { inline-size:100%; max-inline-size:1620px; margin-inline:auto; padding:26px 28px 48px 16px; }
@media(max-width:1280px) {
  .console-masthead { margin-inline-end:24px; }
  .content { padding:24px 24px 40px 16px; }
}
@media(max-width:960px) {
  .app-shell { grid-template-columns:minmax(0,1fr); }
  .workspace { grid-column:1; }
  .app-shell > .sidebar { display:none; }
  .console-masthead { margin:12px 20px 0; }
  .topbar { padding-inline:20px; }
  .content { padding:24px 20px 32px; }
}
@media(max-width:600px) {
  .console-masthead { margin:8px 12px 0; border-radius:14px; }
  .topbar { block-size:60px; padding-inline:10px; }
  .content { padding:20px 12px 28px; }
}
```

fixed侧栏不占Grid轨道，所以工作区必须显式放第二列；窄屏恢复第一列，否则仍可能生成额外隐式列。上例只定义壳层几何：≤960时隐藏的是桌面侧栏实例，顶栏菜单按钮必须打开目标项目的模态导航抽屉，复用同一份导航数据；不能只隐藏侧栏而丢掉导航。折叠属性只控制桌面宽度，标签显隐与可访问名称按组件状态一并处理。

<a id="clean-admin-scrollbars"></a>

### 滚动条与滚动容器

滚动条是页面视觉的一部分。侧栏、表格、代码区、长列表、Dialog／Drawer正文及页面主滚动采用同一套主题规则；必须作用于真正产生滚动的元素，不能只给外层卡片设颜色。优先保留原生滚动和项目已有可靠滚动组件，不为换色新增滚动库、模拟拖动条或全局劫持滚轮。

| 项目 | 本风格要求 |
|---|---|
| 粗细与形状 | 桌面原生scrollbar-width:thin，具体宽度与圆角由浏览器／系统决定；旧WebKit回退槽宽10px、两侧透明边2px形成约6px圆角滑块。不得把所有平台强制成同一像素宽；触摸、高对比度优先系统可操作尺寸 |
| 颜色 | 浅色滑块#d8d8d8、深色#777777，均为R=G=B的中性灰，不能带蓝色；轨道transparent，融入panel／页面背景。浅色默认保持浅灰的轻量外观，不改回深灰蓝长条；不画粗轨道、外框或发光阴影。该浅灰默认不声明达到3:1；有明确非文字对比需求时使用更清楚的中性灰#888888，并保留下方高对比／系统颜色适配 |
| 布局稳定 | 会动态增减内容且需要稳定列宽的侧栏／表格使用scrollbar-gutter:stable；不要给所有卡片强留槽或使用both-edges制造双侧空白，不强制overflow:scroll常驻空轨道 |
| 容器边界 | 侧栏导航位于品牌／搜索和底部帮助／账号之间，flex子项min-block-size:0；滚动条不得越过该区域、侧栏外边界或卡片圆角。卡片头、尾、分页留在滚动体之外；滚动体与卡片边缘通常保留8–12px，按原有padding合并，不能重复叠加 |
| 滚动职责 | 页面默认一个主竖向滚动；侧栏可独立滚动。普通表格随页面增高、仅必要时局部横滚；业务明确要求固定表高／虚拟列表时才限制高度并启用内部竖滚，避免父子容器争抢同一内容的竖向滚动 |
| 交互与可读性 | 不隐藏唯一滚动入口、不用scrollbar-width:none或负margin把条移出容器；滑块不压住文字、行操作和最后一列。无内部可聚焦元素的独立滚动区提供tabindex=0、region与名称；焦点环在可见范围内 |

标准属性优先；只有不支持scrollbar-color时启用旧WebKit伪元素，并把该分支的scrollbar-width重置auto，避免两套方案互相禁用。滚动条不使用transition:all，也不对scrollbar-color做动画或主题淡变，避免滚动时闪烁。尊重系统覆盖式滚动条的自动显隐；不把macOS不滚动时隐藏原生条误判为丢失。

给实际滚动视口添加admin-scroll类；页面根滚动需明确给html添加该类，组件库则把类／变量映射到其实际viewport。下面只设置样式与布局收缩能力，overflow和高度按用途单独配置，不让每个面板自动变成滚动盒。

```css
:root {
  --admin-scroll-thumb:#d8d8d8;
  --admin-scroll-track:transparent;
}
:root[data-theme="dark"] { --admin-scroll-thumb:#777777; }
.admin-scroll {
  min-inline-size:0; min-block-size:0;
  scrollbar-width:thin;
  scrollbar-color:var(--admin-scroll-thumb) var(--admin-scroll-track);
}
.admin-scroll--stable { scrollbar-gutter:stable; }
.sidebar nav.admin-scroll { overflow-y:auto; overscroll-behavior-y:contain; }
.admin-table-scroll { max-inline-size:100%; overflow:auto; }
.admin-scroll:focus-visible { outline:2px solid var(--accent-link); outline-offset:2px; }
@supports not (scrollbar-color:auto) {
  .admin-scroll { scrollbar-width:auto; }
  .admin-scroll::-webkit-scrollbar { width:10px; height:10px; }
  .admin-scroll::-webkit-scrollbar-thumb {
    background:var(--admin-scroll-thumb); background-clip:padding-box;
    border:2px solid transparent; border-radius:999px;
  }
  .admin-scroll::-webkit-scrollbar-track,
  .admin-scroll::-webkit-scrollbar-corner { background:var(--admin-scroll-track); }
}
@media(pointer:coarse) { .admin-scroll { scrollbar-width:auto; } }
@media(prefers-contrast:more) {
  .admin-scroll {
    --admin-scroll-thumb:CanvasText; --admin-scroll-track:Canvas;
    scrollbar-width:auto;
  }
}
@media(forced-colors:active) {
  .admin-scroll { scrollbar-color:auto; scrollbar-width:auto; }
}
```

滚动容器嵌入圆角卡片时，先用内边距和布局把viewport放在边界内；确需外壳裁切时只裁切该卡片的圆角装饰范围，并给内部可聚焦内容留至少4px安全空间。Select／Tooltip等浮层沿用可靠portal，不被overflow裁掉；不能在body或整页使用overflow:hidden掩盖越界。自定义滚动库若已有轨道和滑块，按相同token适配，并关闭重复的原生可见轨道，实际滚动仍只有一个viewport；不能给库的外壳再加overflow:auto生成第二根条。

验收侧栏长菜单、短屏、展开表格、长代码、Dialog／Drawer和横纵同时溢出场景：浅深主题、1920／1280／768／390宽、200%缩放、系统常驻／覆盖式滚动条分别核对；滚到首尾能访问全部内容，键盘与触摸可操作，滚动条始终位于所属容器内，圆角、最后一行／列、分页和焦点环不被覆盖。内容增减与展开收起不让整页横跳，无无溢出却常驻的空轨道、无意的整页横滚或重复竖条。检查实际系统绘制截图，不仅检查computed scrollbar-color；未运行的浏览器／系统状态明确记录未验证。

### 统一响应式断点

以下是本风格的默认视口断点，与逐页规范共用，等于断点时进入较窄档。卡片和表单在实际容器放不下时可以提前换列，保持字号与控件档位，不缩放整页；页面里的局部重排不能另改全局侧栏阈值。

| CSS视口宽度 | 壳层与正文 | 主要内容重排 |
|---|---|---|
| >1280 | 256／232侧栏、68顶栏、正文26 28 48 16 | 概览KPI四列、图表1.55:1，资源卡三列 |
| 961–1280 | 保留桌面侧栏；正文24 24 40 16 | 主图表单列、资源卡两列；事实／说明栏可下移 |
| 601–960 | 单列壳层＋模态导航；正文24 20 32 | KPI两列，登录与主要业务分栏改单列，文档目录可展开 |
| ≤600 | 顶栏60高；正文20 12 28 | 资源卡与表单单列；KPI优先两列、164起高、数值30，内容放不下可单列；保留右上跳转入口 |

## 按钮、输入、浮层

- 主按钮：180deg，`#3589ff → #1669f3`；边框 `#2478f8`，白字；高光 `inset 0 1px 0 rgba(255,255,255,.25)` 与轻微外阴影。hover 改 `#237bfa → #0f5ce6`。普通按钮高34px、左右13px、圆角8px、12px／500；页标题主次操作高38px、圆角10px，专用箭头按钮圆角11px。
- 次按钮：panel 或透明表面、text-soft、细边；弹窗页脚改为7%蓝色混入panel与22%蓝色边框，hover增到12%／42%，避免白面板上消失。危险操作用red，不能只用红色无动作文字。
- 图标与文字：inline-flex居中，紧凑按钮间距7px、页头按钮8px；按钮图标16px、顶栏独立图标按钮36px；SVG display:block、flex-shrink:0，不用字体基线硬推 margin-top。触屏可扩大实际命中区到44px。
- 纯箭头按钮是特殊组件，不能用普通主按钮替换；蓝块、三点和文字覆盖关系见动效说明。
- 表单：可见标签、普通输入高38px、登录输入42px、圆角10px；白色输入面、line边框、focus只在同一边界加深／向内强调，不加第二圈外框；输入前后图标对齐。数量+单位并排分配，禁用时仍可读。
- 普通输入与搜索保持一体式表面：背景、边框、圆角由外壳统一绘制，图标前后缀与文字区无灰色端盖、双圆角或异色拼接；禁用统一整框换色，详见[输入面合同](admin-components.md#clean-admin-input-surface)。
- 输入、Select、Dropdown、弹窗与Tooltip的背景／边框跟随全局主题。浮层小三角用与面板同色的双层填充，边框约1px，12×7px（左右方向7×12px），不能露出异色旋转方块。
- Tooltip保持窄小文本面，max-width:min(360px,100vw−24px)，可断长字。内容含交互时改用合适浮层并保留焦点语义。

```css
:root {
  --el-color-primary:var(--accent); --el-color-primary-dark-2:var(--accent-strong);
  --el-color-primary-light-3:color-mix(in srgb,var(--accent) 70%,var(--panel));
  --el-color-primary-light-5:color-mix(in srgb,var(--accent) 50%,var(--panel));
  --el-color-primary-light-9:color-mix(in srgb,var(--accent) 9%,var(--panel));
  --el-bg-color:var(--panel); --el-bg-color-overlay:var(--panel);
  --el-fill-color-blank:var(--panel); --el-fill-color-light:var(--panel-muted);
  --el-text-color-primary:var(--text); --el-text-color-regular:var(--text-soft);
  --el-text-color-secondary:var(--muted); --el-text-color-placeholder:var(--faint);
  --el-border-color:var(--line); --el-border-color-light:var(--line-soft);
}
```

各类按钮、表单和浮层的精确档位及状态按 [组件规范](admin-components.md) 执行；普通输入默认38、登录42，不在每页任选38–42。

真实依赖库的 Success/Warning/Danger、禁用态和全部主色层级同样要映射；上面只列相关起点，不将复制片段当作库完整主题文件。

## 页面结构

| 页面 | 结构与参数 | 必须保留的关系 |
|---|---|---|
| 登录 | 桌面双栏minmax(0,1.2fr) + minmax(430px,.8fr)；左品牌／大标题／说明／三块功能，右440px登录卡；卡padding 24–36px、圆角16px，主题切换右上 | 标签、用户名、密码显隐、可选验证码、错误信息、忙碌主操作；手机改单栏且表单不被遮挡 |
| 登录验证 | 居中352px面板、圆角20px、6px背景模糊；场景320:180，圆角11px；轨道50px、滑块48px、胶囊圆角 | 拼图实际尺寸由挑战返回；图像ready、失败、刷新、拖动、验证、错误、通过分别呈现；键盘可调 |
| 概览 | 四列KPI、18px间距；36px进度条；主图表1.55:1双列；下一排三进度环／对象对比1.3:1；图标快捷卡与最近活动 | 按工作台规范映射数据，不能因只看首屏而漏掉下方模块；≤1280px两排图表单列，≤960pxKPI两列 |
| 摘要卡 | 115deg四色渐变；大KPI min-height192px、24px圆角、padding24px 24px 18px；普通摘要142px高、20px圆角 | 右下大线框图标、左下半透明环、星芒是装饰；标签和数值在前层，hint为小深色面 |
| 产品目录 | 四摘要→目录标题→搜索／分段筛选→类别标题／折叠→三列卡片；产品卡圆角18px | 3px顶部短色条、图标与状态、稳定ID、标题说明、浅蓝能力面、淡紫数量面、页脚动作；筛选状态真实 |
| 业务列表 | 头部摘要、工具栏、白色表格、底部计数与分页；hover轻蓝，选中行更深 | 横向滚动局限于表格区域；数字对齐、状态徽标、代码复制、行操作、选择操作栏不能遮挡记录 |
| 文档中心 | 操作面板→文档说明→横向特征条→左目录与正文；圆角16px白色面，浅蓝引用与元信息 | 搜索仅筛目录，标题滚动与当前项同步；复制／下载同一内容，长代码和表格独立滚动 |
| 用户中心 | 左身份栏228px、紫色210px hero与头像，状态／子导航；右区表单+250px事实栏 | 表单按登录身份、联系外观分区，动作底栏；只替换展示数据，业务更改语义仍由目标项目决定 |
| 系统配置 | 命令栏→三色摘要→主设置区+约250px说明栏；设置组圆角16px，成对数值字段浅蓝背景 | 未改禁用保存、dirty提示、保存中、成功和失败可区分；不能把演示安全配置当成目标项目策略 |
| 备份／发布／排查等扩展页 | 沿用同壳层、分组列表、运行状态、说明栏和同套按钮／浮层 | 复用动作状态样式；不要复制原仓库地址、签名参数、凭据、运行日志或服务端实现 |

卡片四种颜色是位置与分类装饰，不代表成功／失败；业务状态继续使用语义色。深色模式继续使用四色摘要，但白字与装饰对比单独检查。

## 实施与核对

- 原参考以多层CSS覆盖构成。移植时合并为一套有顺序的token／壳层／组件／页面层，不直接拷贝旧重写链。页签背景动画和hover不能争夺同一个transform。
- 栅格使用minmax(0,1fr)，工具栏flex-wrap，长ID可折行或提供可访问的完整值；布局问题在尺寸与换行处解决，不能给body加overflow-x:hidden掩盖。
- 桌面折叠侧栏与手机模态导航是两种模式。手机开关的aria-expanded、背景inert、Escape、遮罩关闭、焦点进入和返回一起完成；复用已有合适库时保留它的焦点管理。
- 浅深模式同时更新页面、组件库、浮层、图表、图例和代码区。图表绘图区显式采用透明背景，防止库的深色默认灰底盖住面板。不要让portal到body的弹层漏掉主题。
- 登录界面只提供输入与反馈外观。真实验证结果、权限、会话、设备与安全策略由目标服务确定；不能把演示滑块、前端布尔值或路由作为认证。
- 参考图由虚构数据重新截取，字体跟随截图环境。实现后对照1920桌面、1280中等宽度、768平板、390手机检查，且允许用户浏览器缩放。

## 视觉核对流程与验收表

把规范真正用于实现，需要在目标项目运行后比较画面。至少先完成壳层+一个实际需要的代表页，直接核对并修正后再批量铺其他页面；这不是要求用户审批，也不阻断已授权任务。代码结构正确、测试通过或使用同色不能替代视觉一致性。

| 检查层 | 实际核对内容 | 偏离时先修什么 |
|---|---|---|
| 尺寸口径 | 1920×1080 CSS、100%缩放、DPR记录；图片以相同比例查看 | 先排除参考图像素当CSS、未设置border-box、重复容器padding；不要通过全页缩放补救 |
| 壳层 | 侧栏12外留白、232实宽、顶栏68高、正文1620上限与padding；短屏导航仍可达 | 全局布局与容器，不能每页单独偏移 |
| 顶部控件 | 桌面侧栏内折叠入口／窄屏顶栏导航入口、紧凑面包屑、搜索及快捷键、状态胶囊、主题／刷新、头像用户名的顺序、尺寸、间距和实际动作 | 按admin-topbar修共享结构，不能只保留白色容器、裸折叠图标与账号文本；数据状态不能被身份认证文案替代 |
| 页面结构 | 区块顺序、主次列比例、卡数与高度、标题／操作关系 | 先主布局与业务映射，别先纠结小图标阴影 |
| 密度 | 页面26／30、说明12、控件34／38／42档、表格44／56／64档 | 共享字级／尺寸，不能一页修一批随机数 |
| 品牌与导航控制 | Logo与标题横排垂直居中、品牌组左右留白对称；桌面折叠按钮在侧栏内且折叠后可展开 | 长名／无副标题／窄栏／断点都核对；桌面顶栏不重复放折叠按钮，窄屏保留导航入口 |
| 输入焦点与面板间距 | 输入聚焦只强化同一条字段边界；相邻独立卡片20／16间距、手机14／12 | 排除内外套框、双焦点环、负margin和相邻圆角贴边；保留可见键盘焦点 |
| 表面 | bg／panel／line、圆角按职责、轻阴影、主按钮渐变 | token与组件variant；不得加巨型hero、大片玻璃或高饱和蓝面替代 |
| 组件细节 | 侧栏各组彩色短竖线、彩色线框图标与浅色底座，分隔线、ID复制、徽标、字段标签／help／后缀、普通摘要与大KPI差别 | 当前共享组件，不给每实例写补丁；检查default／hover／active时分组色与白色选中态不混用 |
| 装饰 | KPI线框图标、背景环、星芒、短色条、浅蓝能力面／淡紫数量面 | 装饰层与前景层分开，装饰不盖字、不抢点击 |
| 指标卡颜色与入口 | 四色115deg的两端值及实际computed background；右上圆箭头默认、悬停、键盘与点击目标 | 排除旧主题覆盖、整卡黑蒙层／brightness与错用tone名称；恢复圆形跳转入口及200ms旋转，不能只画装饰箭头 |
| 状态 | hover／press／focus／disabled／busy／success／error、选中与只读 | 用同一动作实际操作，截必要状态，确认尺寸不跳动 |
| 动画 | 箭头铺底、三点、数字、共享滑块、折叠反向、循环停止、卸载清理 | 逐项按动效规范检查；不从单帧推断正确时序 |
| 内容压力 | 长菜单／字段／文件名、四位数、空数据、错误、超长帮助 | 换行、min-width、局部滚动与状态语义，不裁切关键字段 |
| 响应式 | 1280／768／390宽与短屏、浏览器缩放、浮层和手机导航 | 使用同套响应式规则，不能仅桌面截图“看起来对” |
| 滚动条 | 页面／侧栏／表格／浮层的粗细、配色、边界、横纵滚动与首尾可达性 | 按滚动条规范检查实际viewport，轨道融入表面、不越过圆角、不遮挡操作、不制造重复滚动；高对比度尊重系统 |
| 主题 | 深色页面、body portal浮层、图表、禁用字与焦点 | 所有库主题映射和实际对比，不只改body背景 |
| 图表提示 | 数据点／日期对应的数值提示框、系列标记、单位、边缘避让、键盘／触摸等价入口 | 同一数据源与图例／摘要同步；按admin-workbench实测箭头尖端到可见图形边缘默认6px、正常4–8px，不按容器边缘定位；翻转同步箭头；柱图／折线高低值切换时正文与箭头随当前数据x/y更新，禁止固定top或按全图最高值定位；提示不裁切、不跳布局、不只依赖颜色或鼠标 |

参考可见区块的高宽、边距和字号有明确值时按数值核对；长真实内容可以自然增高。字体抗锯齿与业务文案不同，不要求整屏像素哈希相同，也不能用“文案不同”掩盖固定控件尺寸、导航结构与背景材质变化。自动视觉差异只能辅助定位，仍要实际打开截图判断。

在任务结果里简要列出本次页面及状态，使用“匹配／有意调整／待修正／未验证”。有意调整写业务或设备原因；能修的偏差直接继续修，不把明显偏离留作建议。不能启动项目或没有拿到截图时，明确“规范已接入，实际画面未验证”；不得声称“完全复刻”。比较与调试图用外部临时目录，保留仅在用户需要交付时。

### 常见偏差与纠正提示词

```text
当前结果只匹配蓝白颜色，尚未匹配这套后台。先停止增加装饰或业务组件，
读取admin-design、当前admin-pages章节和admin-components，打开对应高清图。
检查是不是把DPR2当CSS尺寸、给正文重复加padding、套用组件库大号默认，
或把所有panel圆角都设24。按壳层→页面区块→密度→控件状态→装饰→动效
顺序修正目标项目的共享实现，再回到同视口截图比较。
保持真实业务内容与功能，不复制演示数字，不为匹配截图固定文本高度。
把每项剩余差异和证据说明清楚；没实际看过运行截图不能说已复刻。
```
