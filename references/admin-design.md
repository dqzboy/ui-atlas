# 清爽蓝白后台：布局、主题和组件规范

本规范用于创建具有相同视觉语言的后台。与 [完整配方](recipes/clean-admin.md) 和 [动效说明](admin-motion.md) 配套；只将相关代码片段移植到目标项目，不需要在 skill 中附带前端工程。

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
:root[data-theme="light"] {
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
  --workspace-card-shadow:0 3px 18px rgba(0,0,0,.08);
}
```

字体使用系统回退，不下载商业字体；不同操作系统的字形和占宽会有差异。字体基准为正文 14px、标签 13px、说明 12px；此套紧凑控件有 10–12px 辅助信息，不把小号辅助字当作所有正文的尺寸。大标题一般 26px／1.3、650，概览标题 30px；KPI 38px／1.2、650，tabular-nums；标题字距约 -.035em 到 -.04em。

## 壳层的几何

| 区域 | 桌面规则 | 窄屏规则 |
|---|---|---|
| 外层 | Grid：256px + minmax(0,1fr)，最小高度 100dvh | ≤960px 改单列，导航改抽屉 |
| 侧栏 | fixed，距左／上／下 12px；宽 232px；内边距 12px；圆角 20px；蓝色细边 | 展开宽 min(280px,视口−32px)，背景不可交互；关闭后恢复焦点 |
| 折叠侧栏 | 外层第一列 88px，实际侧栏宽 64px；标签／计数隐藏，保留可访问名称 | 抽屉始终显示完整标签，不沿用图标折叠态 |
| 侧栏品牌 | 68px 起始区域，下边距与分隔线；标记 34px，标题 20px | 品牌可替换，不复制原用户标记 |
| 菜单项 | 最小高 42px，内边距 8px 10px，间距 10px，圆角 11px；图标底座 24px／7px | 命中区须能触摸操作，图标有文字或 aria-label |
| 顶栏 | 独立白色面板；margin 12px 28px 0 16px；圆角18px；内容高68px；横向内边距18px | ≤960px 横向20px；≤600px margin 8px 12px、圆角14px、内容高60px |
| 顶栏控件 | 图标按钮36px／10px；搜索宽clamp(170px,20vw,260px)、高36px；头像26px／8px | 手机搜索缩为36px图标按钮，隐藏搜索文案、连接状态与用户名，保留入口 |
| 正文 | max-width 1620px；padding 26px 28px 48px 16px；子项min-width:0 | ≤1280px 24px 24px 40px 16px；≤960px 24px 20px 32px；≤600px 20px 12px 28px |
| 页标题 | 分组标记 + h1 + 说明 + 右侧主次操作；min-height约94px，底部14px与细线，之后24px | 手机上下排列，操作区可占整行 |
| 面板 | 白色、边界line-soft、圆角16px、workspace-card-shadow；面板间20px | 在容器内重排，不能靠隐藏溢出解决碰撞 |

顶栏在普通文档流中，不默认 sticky；长内容收起时，固定顶栏与浏览器滚动锚定混用可能造成“顶栏突然掉下来”。侧栏导航区域独立滚动，品牌、搜索、底部帮助与用户区不随菜单滚走。

```css
.app-shell { display:grid; grid-template-columns:256px minmax(0,1fr); min-height:100dvh; }
.workspace,.content,.panel { min-inline-size:0; }
.sidebar { position:fixed; inset:12px auto 12px 12px; inline-size:232px;
  display:flex; flex-direction:column; padding:12px; border:1px solid var(--workspace-blue-line);
  border-radius:20px; background:var(--panel); }
.sidebar nav { flex:1; min-block-size:0; overflow-y:auto; overscroll-behavior:contain; }
.console-masthead { margin:12px 28px 0 16px; border:1px solid var(--workspace-blue-line);
  border-radius:18px; background:var(--panel); }
.topbar { display:flex; align-items:center; gap:16px; block-size:68px; padding-inline:18px; }
.content { inline-size:100%; max-inline-size:1620px; margin-inline:auto; padding:26px 28px 48px 16px; }
@media(max-width:960px) { .app-shell { grid-template-columns:minmax(0,1fr); } }
```

## 按钮、输入、浮层

- 主按钮：180deg，`#3589ff → #1669f3`；边框 `#2478f8`，白字；高光 `inset 0 1px 0 rgba(255,255,255,.25)` 与轻微外阴影。hover 改 `#237bfa → #0f5ce6`。普通按钮高34px、左右13px、12px／500；页标题主次操作高38px、圆角约10–11px。
- 次按钮：panel 或透明表面、text-soft、细边；弹窗页脚改为7%蓝色混入panel与22%蓝色边框，hover增到12%／42%，避免白面板上消失。危险操作用red，不能只用红色无动作文字。
- 图标与文字：inline-flex居中，间距6–9px；按钮图标16px、独立图标按钮约36px；SVG display:block、flex-shrink:0，不用字体基线硬推 margin-top。触屏可扩大实际命中区到44px。
- 纯箭头按钮是特殊组件，不能用普通主按钮替换；蓝块、三点和文字覆盖关系见动效说明。
- 表单：可见标签、输入高度约38–42px、圆角8–10px；白色输入面、line边框、focus accent边与轻微环；输入前后图标对齐。数量+单位并排分配，禁用时仍可读。
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

真实依赖库的 Success/Warning/Danger、禁用态和全部主色层级同样要映射；上面只列相关起点，不将复制片段当作库完整主题文件。

## 页面结构

| 页面 | 结构与参数 | 必须保留的关系 |
|---|---|---|
| 登录 | 桌面双栏minmax(0,1.2fr) + minmax(430px,.8fr)；左品牌／大标题／说明／三块功能，右440px登录卡；卡padding 24–36px、圆角16px，主题切换右上 | 标签、用户名、密码显隐、可选验证码、错误信息、忙碌主操作；手机改单栏且表单不被遮挡 |
| 登录验证 | 居中352px面板、圆角20px、6px背景模糊；场景320:180，圆角11px；轨道50px、滑块48px、胶囊圆角 | 拼图实际尺寸由挑战返回；图像ready、失败、刷新、拖动、验证、错误、通过分别呈现；键盘可调 |
| 概览 | 四列KPI、18px左右间距；下方36px进度条；主图表区1.55:1双列；白色图表与快捷入口 | 数字、单位、比例、图例口径一致，空数据不画假趋势；≤1280px主图改单列，≤960pxKPI两列 |
| 摘要卡 | 115deg四色渐变；大KPI min-height192px、24px圆角、padding24px 24px 18px；普通摘要142px高、20px圆角 | 右下大线框图标、左下半透明环、星芒是装饰；标签和数值在前层，hint为小深色面 |
| 产品目录 | 四摘要→目录标题→搜索／分段筛选→类别标题／折叠→三列卡片；产品卡圆角18px | 3px顶部短色条、图标与状态、稳定ID、标题说明、浅蓝能力面、淡紫数量面、页脚动作；筛选状态真实 |
| 业务列表 | 头部摘要、工具栏、白色表格、底部计数与分页；hover轻蓝，选中行更深 | 横向滚动局限于表格区域；数字对齐、状态徽标、代码复制、行操作、选择操作栏不能遮挡记录 |
| 文档中心 | 操作面板→文档说明→横向特征条→左目录与正文；圆角16px白色面，浅蓝引用与元信息 | 搜索仅筛目录，标题滚动与当前项同步；复制／下载同一内容，长代码和表格独立滚动 |
| 用户中心 | 左身份栏约228–250px、紫色210px hero与头像，状态／子导航；右区表单+250px事实栏 | 表单按登录身份、联系外观分区，动作底栏；只替换展示数据，业务更改语义仍由目标项目决定 |
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
