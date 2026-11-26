# 清爽蓝白后台：顶部栏的结构、样式与行为

新建本风格的后台壳层时必读本文件。参考[概览高清图](../assets/details/enterprise-workbenches/clean-admin-overview.webp)顶部；布局与主题token沿用[设计基线](admin-design.md)，动效沿用[动效规范](admin-motion.md)。这是一条悬浮式应用工具栏，不把整个区域赋予role=menu／menubar；只有实际打开的动作菜单使用相应菜单语义。

## 固定组合与可替换内容

桌面从左到右依次为：**浅蓝方形折叠按钮 → 紧凑面包屑 → 弹性留白 → 搜索入口与快捷键胶囊 → 状态徽标 → 主题按钮 → 刷新按钮 → 头像与账户名**。控件顺序、浅蓝底座、密度与独立圆角面板是默认风格的一部分，不能只做一个左侧标题加右侧账号的白条。普通文档／帮助链接按业务放到已有帮助入口或明确的附加位置，不能拿它替代搜索、主题或刷新。

“工作空间／工作台”、面包屑层级、用户名、头像首字与状态文案来自目标项目。图中的“演示数据”只代表演示环境，线上真实就绪可写“数据已连接”；不能因为用户已登录就把同步状态写成“身份已验证”，二者职责不同。没有接口时呈现中性“未接入数据／等待同步”，不能伪造已连接。确实不具备某能力时明确说明取舍，不能留一个可点却无响应的按钮。

| 部位 | 几何、颜色与排版 | 状态与行为 |
|---|---|---|
| 悬浮外框 | 独立panel面、1px workspace-blue-line、18圆角、0 4px 20px rgba(57,106,188,.04)轻影；桌面margin12 28 0 16 | 跟随工作区宽度，不与侧栏或页面头合并；普通文档流，不默认sticky |
| 内部一行 | 内容高68、左右padding18、gap16、align-items:center；68不包含外框上下各1px边 | 每项保持垂直居中，不做第二个大页面标题；DOM顺序与视觉顺序相同 |
| 折叠入口 | 36×36、圆角10、1px line-soft边、tint-blue底、accent-link图标14 | 使用Fold／Expand对应的基准图形；桌面控制256／88壳层，手机打开完整导航抽屉；aria-controls／aria-expanded同步 |
| 面包屑 | 12px、muted文字、gap9、10px细chevron分隔；当前业务页text／650 | 概览可用“工作空间 › 工作台”两层，业务页按真实分组加当前页；祖先可导航，当前项aria-current=page；不加独立大号品牌图标 |
| 页面搜索入口 | 36高、宽clamp(170px,20vw,260px)、左右padding10、gap7、10圆角、workspace-blue-line边、workspace-blue-surface渐变 | 它是打开命令搜索的button，不是不能输入的假input；前11px搜索图标、中间11px提示、右侧快捷键；margin-inline-start:auto把整组推向右边 |
| 快捷键胶囊 | 9px文字、padding3 5、圆角5、panel面、workspace-blue-line细边、accent-link | 展示⌘ / Ctrl K或匹配平台的同等快捷键；点击搜索与快捷键打开同一个搜索界面 |
| 右侧操作组 | flex且不缩小、gap8，无额外粗分割线 | 依次状态、主题、刷新、账户；不能平均分布到整条顶栏 |
| 状态徽标 | min-height24、padding3 8、999圆角、11px／500、gap5、12px图标；语义色24%边、7%混panel底 | 绿色成功／蓝色同步中／琥珀失败／中性等待由真实数据驱动；使用带图标的完整胶囊，不只放裸绿点 |
| 主题入口 | 36×36、10圆角、tint-blue底、line-soft边、15px蓝色太阳／月亮 | 点击打开浅色／深色／跟随系统选择；图标反映最终主题，可访问名称说明当前偏好，不能只画静态太阳 |
| 刷新入口 | 36×36、10圆角、tint-blue底、line-soft边、14px蓝色顺时针刷新图标 | 实际刷新当前约定的数据范围；hover图标转35deg，busy旋转与波纹按动效规范；请求结束立即恢复，禁重复请求 |
| 账户入口 | 高36、padding4 10 4 4、gap9、10圆角、workspace-blue-surface、workspace-blue-line边；用户名11px、最大100宽 | 左侧26×26头像、圆角8、浅蓝底蓝字／真实头像；右侧用户名。不能只用盾牌或纯文本operator替代头像结构；点击打开实际账户菜单 |

图标统一使用下方基准SVG，按指定尺寸显示，fill=currentColor、stroke=none；不引入新的图标依赖，也不混用实心彩色图、emoji和不同笔画粗细。头像与账号文字可替换，按钮底座不随品牌变成黑色线框按钮。

## 可移植结构

以下是使用虚构账号和演示状态的视觉结构。复制到目标壳层后，绑定实际路由、导航开合、命令搜索、主题、刷新和账户菜单；示例中的aria-expanded初始值须按真实状态更新。SVG symbol只定义一次，每个壳层实例使用唯一ID前缀；重复渲染时沿用目标项目已有图标组件或调整前缀。

```html
<svg class="admin-topbar__symbols" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
  <defs>
    <symbol id="atlas-topbar-fold" viewBox="0 0 1024 1024"><path fill="currentColor" d="M896 192H128v128h768zm0 256H384v128h512zm0 256H128v128h768zM320 384 128 512l192 128z" /></symbol>
    <symbol id="atlas-topbar-expand" viewBox="0 0 1024 1024"><path fill="currentColor" d="M128 192h768v128H128zm0 256h512v128H128zm0 256h768v128H128zm576-352 192 160-192 128z" /></symbol>
    <symbol id="atlas-topbar-chevron" viewBox="0 0 1024 1024"><path fill="currentColor" d="M340.864 149.312a30.59 30.59 0 0 0 0 42.752L652.736 512 340.864 831.872a30.59 30.59 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z" /></symbol>
    <symbol id="atlas-topbar-search" viewBox="0 0 1024 1024"><path fill="currentColor" d="m795.904 750.72 124.992 124.928a32 32 0 0 1-45.248 45.248L750.656 795.904a416 416 0 1 1 45.248-45.248zM480 832a352 352 0 1 0 0-704 352 352 0 0 0 0 704" /></symbol>
    <symbol id="atlas-topbar-sun" viewBox="0 0 1024 1024"><path fill="currentColor" d="M512 704a192 192 0 1 0 0-384 192 192 0 0 0 0 384m0 64a256 256 0 1 1 0-512 256 256 0 0 1 0 512m0-704a32 32 0 0 1 32 32v64a32 32 0 0 1-64 0V96a32 32 0 0 1 32-32m0 768a32 32 0 0 1 32 32v64a32 32 0 1 1-64 0v-64a32 32 0 0 1 32-32M195.2 195.2a32 32 0 0 1 45.248 0l45.248 45.248a32 32 0 1 1-45.248 45.248L195.2 240.448a32 32 0 0 1 0-45.248m543.104 543.104a32 32 0 0 1 45.248 0l45.248 45.248a32 32 0 0 1-45.248 45.248l-45.248-45.248a32 32 0 0 1 0-45.248M64 512a32 32 0 0 1 32-32h64a32 32 0 0 1 0 64H96a32 32 0 0 1-32-32m768 0a32 32 0 0 1 32-32h64a32 32 0 1 1 0 64h-64a32 32 0 0 1-32-32M195.2 828.8a32 32 0 0 1 0-45.248l45.248-45.248a32 32 0 0 1 45.248 45.248L240.448 828.8a32 32 0 0 1-45.248 0m543.104-543.104a32 32 0 0 1 0-45.248l45.248-45.248a32 32 0 0 1 45.248 45.248l-45.248 45.248a32 32 0 0 1-45.248 0" /></symbol>
    <symbol id="atlas-topbar-moon" viewBox="0 0 1024 1024"><path fill="currentColor" d="M240.448 240.448a384 384 0 1 0 559.424 525.696 448 448 0 0 1-542.016-542.08 391 391 0 0 0-17.408 16.384m181.056 362.048a384 384 0 0 0 525.632 16.384A448 448 0 1 1 405.056 76.8a384 384 0 0 0 16.448 525.696" /></symbol>
    <symbol id="atlas-topbar-refresh" viewBox="0 0 1024 1024"><path fill="currentColor" d="M784.512 230.272v-50.56a32 32 0 1 1 64 0v149.056a32 32 0 0 1-32 32H667.52a32 32 0 1 1 0-64h92.992A320 320 0 1 0 524.8 833.152a320 320 0 0 0 320-320h64a384 384 0 0 1-384 384 384 384 0 0 1-384-384 384 384 0 0 1 643.712-282.88" /></symbol>
    <symbol id="atlas-topbar-check" viewBox="0 0 1024 1024"><path fill="currentColor" d="M512 896a384 384 0 1 0 0-768 384 384 0 0 0 0 768m0 64a448 448 0 1 1 0-896 448 448 0 0 1 0 896" /><path fill="currentColor" d="M745.344 361.344a32 32 0 0 1 45.312 45.312l-288 288a32 32 0 0 1-45.312 0l-160-160a32 32 0 1 1 45.312-45.312L480 626.752z" /></symbol>
    <symbol id="atlas-topbar-system" viewBox="0 0 1024 1024"><path fill="currentColor" d="M544 768v128h192a32 32 0 1 1 0 64H288a32 32 0 1 1 0-64h192V768H192A128 128 0 0 1 64 640V256a128 128 0 0 1 128-128h640a128 128 0 0 1 128 128v384a128 128 0 0 1-128 128zM192 192a64 64 0 0 0-64 64v384a64 64 0 0 0 64 64h640a64 64 0 0 0 64-64V256a64 64 0 0 0-64-64z" /></symbol>
  </defs>
</svg>
<div class="console-masthead">
  <header class="topbar admin-topbar">
    <button class="admin-topbar__icon admin-topbar__toggle" type="button"
      aria-label="折叠导航" aria-controls="console-sidebar" aria-expanded="true">
      <svg viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><use href="#atlas-topbar-fold" /></svg>
    </button>
    <nav class="admin-topbar__breadcrumb" aria-label="当前位置">
      <a href="/">工作空间</a>
      <svg viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><use href="#atlas-topbar-chevron" /></svg>
      <span aria-current="page">工作台</span>
    </nav>
    <button class="admin-topbar__search" type="button" aria-label="查找页面，快捷键Command或Ctrl加K">
      <svg viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><use href="#atlas-topbar-search" /></svg>
      <span>查找页面…</span><kbd>⌘ / Ctrl K</kbd>
    </button>
    <div class="admin-topbar__actions">
      <span class="admin-topbar__status" data-tone="success" role="status">
        <svg viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><use href="#atlas-topbar-check" /></svg>
        <span>演示数据</span>
      </span>
      <button class="admin-topbar__icon admin-topbar__theme" type="button"
        aria-label="当前主题：浅色模式" aria-haspopup="menu" aria-expanded="false">
        <svg viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><use href="#atlas-topbar-sun" /></svg>
      </button>
      <button class="admin-topbar__icon admin-topbar__refresh" type="button" aria-label="刷新数据" aria-busy="false">
        <svg viewBox="0 0 1024 1024" aria-hidden="true" focusable="false"><use href="#atlas-topbar-refresh" /></svg>
      </button>
      <button class="admin-topbar__profile" type="button" aria-label="打开demo.admin的账户菜单" aria-haspopup="menu" aria-expanded="false">
        <span class="admin-topbar__avatar" aria-hidden="true">演</span><span class="admin-topbar__username">demo.admin</span>
      </button>
    </div>
  </header>
</div>
```

```css
.console-masthead { container:ui-atlas-topbar / inline-size; }
.admin-topbar__symbols { position:absolute; inline-size:0; block-size:0; overflow:hidden; pointer-events:none; }
.console-masthead .admin-topbar { display:flex; align-items:center; gap:16px;
  block-size:68px; min-inline-size:0; padding-inline:18px; }
.admin-topbar button { font-family:var(--sans); cursor:pointer; }
.admin-topbar svg { display:block; flex-shrink:0; fill:currentColor; stroke:none; }
.admin-topbar__icon { display:grid; place-items:center; flex:0 0 auto; inline-size:36px; block-size:36px;
  padding:0; border:1px solid var(--line-soft); border-radius:10px; background:var(--tint-blue);
  color:var(--accent-link); box-shadow:none; transition:background-color 160ms ease,border-color 160ms ease,transform 120ms ease; }
.admin-topbar__icon > svg { inline-size:14px; block-size:14px; }
.admin-topbar__theme > svg { inline-size:15px; block-size:15px; }
.admin-topbar__breadcrumb { display:flex; align-items:center; gap:9px; min-inline-size:0;
  color:var(--muted); font:400 12px/1.5 var(--sans); white-space:nowrap; }
.admin-topbar__breadcrumb a { color:inherit; text-decoration:none; }
.admin-topbar__breadcrumb > :is(a,span,strong) { min-inline-size:0; overflow:hidden; text-overflow:ellipsis; }
.admin-topbar__breadcrumb > svg { inline-size:10px; block-size:10px; color:var(--faint); }
.admin-topbar__breadcrumb strong { color:var(--text); font-weight:650; }
.admin-topbar__search { display:flex; align-items:center; gap:7px; flex:0 0 auto;
  inline-size:clamp(170px,20vw,260px); block-size:36px; margin-inline-start:auto; padding:0 10px;
  border:1px solid var(--workspace-blue-line); border-radius:10px; background:var(--workspace-blue-surface);
  color:var(--muted); font:400 11px var(--sans); text-align:start; }
.admin-topbar__search > svg { inline-size:11px; block-size:11px; }
.admin-topbar__search kbd { margin-inline-start:auto; padding:3px 5px; border:1px solid var(--workspace-blue-line);
  border-radius:5px; background:var(--panel); color:var(--accent-link); font:400 9px var(--sans); white-space:nowrap; }
.admin-topbar__actions { display:flex; align-items:center; flex:0 0 auto; gap:8px; }
.admin-topbar__status { --status-color:var(--muted); display:inline-flex; align-items:center; gap:5px;
  min-block-size:24px; padding:3px 8px; border:1px solid color-mix(in srgb,var(--status-color) 24%,transparent);
  border-radius:999px; background:color-mix(in srgb,var(--status-color) 7%,var(--panel));
  color:var(--status-color); font:500 11px/1.4 var(--sans); white-space:nowrap; }
.admin-topbar__status[data-tone="success"] { --status-color:var(--green); }
.admin-topbar__status[data-tone="loading"] { --status-color:var(--accent-link); }
.admin-topbar__status[data-tone="warning"] { --status-color:var(--amber); }
.admin-topbar__status > svg { inline-size:12px; block-size:12px; }
.admin-topbar__profile { display:flex; align-items:center; flex:0 0 auto; gap:9px; block-size:36px;
  padding:4px 10px 4px 4px; border:1px solid var(--workspace-blue-line); border-radius:10px;
  background:var(--workspace-blue-surface); color:var(--text-soft); font:400 11px var(--sans); }
.admin-topbar__avatar { display:grid; place-items:center; flex:0 0 26px; inline-size:26px; block-size:26px;
  border-radius:8px; background:var(--tint-blue); color:var(--accent-link); font:650 12px var(--sans); }
.admin-topbar__avatar img { display:block; inline-size:100%; block-size:100%; border-radius:inherit; object-fit:cover; }
.admin-topbar__username { max-inline-size:100px; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; }
.admin-topbar__icon:hover:not(:disabled),.admin-topbar__profile:hover { border-color:var(--line); background:var(--panel-strong); }
.admin-topbar__search:hover { border-color:var(--accent); }
.admin-topbar button:focus-visible,.admin-topbar__breadcrumb a:focus-visible { outline:2px solid var(--accent); outline-offset:3px; }
.admin-topbar__icon:active:not(:disabled) { transform:scale(.975); }
.admin-topbar button:disabled { cursor:not-allowed; opacity:.5; }
.admin-topbar__refresh > svg { transition:transform 450ms cubic-bezier(.4,0,.2,1); }
.admin-topbar__refresh:hover:not(:disabled) > svg { transform:rotate(35deg); }
.admin-topbar__refresh[aria-busy="true"] > svg { animation:admin-topbar-spin 720ms linear infinite; }
@keyframes admin-topbar-spin { to { transform:rotate(360deg); } }
@container ui-atlas-topbar (max-width:640px) {
  .admin-topbar__status { display:none; }
  .admin-topbar__search { inline-size:170px; }
  .admin-topbar__username { max-inline-size:72px; }
}
@media(max-width:1280px) {
  .admin-topbar__search { inline-size:170px; }
  .admin-topbar__breadcrumb { gap:6px; font-size:11px; }
}
@media(min-width:961px) and (max-width:1100px) { .admin-topbar__status { display:none; } }
@media(max-width:960px) {
  .console-masthead .admin-topbar { padding-inline:20px; gap:12px; }
  .admin-topbar__breadcrumb { display:none; }
  .admin-topbar__search { inline-size:clamp(150px,26vw,200px); margin-inline-start:0; }
  .admin-topbar__actions { margin-inline-start:auto; }
}
@media(max-width:600px) {
  .console-masthead .admin-topbar { block-size:60px; padding-inline:10px; gap:8px; }
  .admin-topbar__search { inline-size:36px; padding:0; justify-content:center; background:var(--tint-blue); color:var(--accent-link); }
  .admin-topbar__search > span,.admin-topbar__search kbd,.admin-topbar__status,.admin-topbar__username { display:none; }
  .admin-topbar__actions { gap:6px; }
  .admin-topbar__profile { inline-size:36px; padding:4px; }
}
@media(prefers-reduced-motion:reduce) {
  .admin-topbar__icon,.admin-topbar__refresh > svg { transition:none; animation:none; }
  .admin-topbar__refresh[aria-busy="true"] > svg { animation:none; }
  .admin-topbar__refresh:hover:not(:disabled) > svg { transform:none; }
}
```

<a id="clean-admin-search-dialog"></a>

## 搜索命令面板：点击后打开的模态弹窗

顶部搜索入口、侧栏快捷搜索和 `⌘/Ctrl+K` 都打开同一个**居中的搜索命令面板**。它是可用的模态搜索弹窗，不是下拉菜单、不能输入的假输入框、顶栏下方的小浮层，也不是一张没有层级和结果密度控制的全屏白板。目标是让用户在当前后台中快速找到页面、设置区和可执行导航；搜索结果必须来自真实可访问页面或当前项目明确支持的命令。

| 区域 | 清爽蓝白后台的默认要求 | 错误表现 |
|---|---|---|
| 遮罩 | `rgba(25,42,70,.28–.38)`的柔和遮罩；必要时轻微背景模糊；不让后台消失或变成纯黑 | 没有遮罩、遮罩过黑、背景仍可点击／滚动 |
| 弹窗外框 | 桌面宽 `min(760px, calc(100vw - 48px))`，最大高 `min(680px, calc(100dvh - 48px))`；panel面、1px line-soft边、20px圆角、`0 18px 50px`轻阴影；垂直位置约视口上方12–16%，不要贴顶 | 宽度随内容无限增长、贴边、占满整屏、白色大空框或圆角与后台不一致 |
| 标题栏 | 高72左右、左右24；左侧44×44浅蓝图标底座与搜索图标，旁边18px标题“快捷搜索”，可有一行12px说明；右侧36×36关闭按钮 | 只放一个巨大搜索图标、标题与输入提示重复、关闭按钮漂在弹窗外 |
| 输入区 | 标题栏下方保持16–20间距；输入高48–52、圆角12、1px accent边或focus ring；placeholder只说明搜索范围，例如“输入页面名称、设置或命令…”；输入获得初始焦点 | 把“查找管理页面”当作重复的大标题和placeholder同时堆叠、输入框过高、文字过淡或没有焦点 |
| 结果区 | 与输入框保持12–16间距；结果列表在弹窗内部独立滚动，行高64–76、左右12–16、图标36×36、标题14–16／650、说明12–13、右侧细chevron；hover/focus使用浅蓝面，当前键盘项使用清晰蓝色强调面与白字 | 结果行过高导致只看到一两项、图标和标题不对齐、结果溢出弹窗、整行无键盘选中态 |
| 空／无结果 | 保留输入内容，居中显示线框搜索图标、短说明和清除／查看全部等真实操作；不能显示一大片空白或虚构结果 | 无结果时弹窗塌陷、显示“暂无数据”但没有原因或恢复动作 |
| 底部提示 | 可选一行12px键盘提示，使用小胶囊展示 `↑↓`、`Enter`、`Esc`；与结果区留12px间距 | 把快捷键说明做成大标题、重复顶栏胶囊或遮住最后一条结果 |

推荐结构如下，实际项目应绑定真实路由和页面描述；示例文案仅说明层级，不复制为业务数据：

```html
<dialog class="admin-search-dialog" aria-labelledby="admin-search-title">
  <div class="admin-search-dialog__panel">
    <header class="admin-search-dialog__header">
      <span class="admin-search-dialog__mark" aria-hidden="true">⌕</span>
      <div><h2 id="admin-search-title">快捷搜索</h2><p>查找页面、设置和可用操作</p></div>
      <button class="admin-search-dialog__close" type="button" aria-label="关闭搜索">×</button>
    </header>
    <label class="admin-search-dialog__field">
      <span class="sr-only">搜索后台页面</span>
      <input type="search" autocomplete="off" placeholder="输入页面名称、设置或命令…" />
    </label>
    <div class="admin-search-dialog__results" role="listbox" aria-label="搜索结果">
      <!-- 每项绑定真实 route、标题、说明与稳定 value；当前项同步 aria-selected -->
    </div>
    <footer class="admin-search-dialog__hint"><kbd>↑↓</kbd>选择 <kbd>Enter</kbd>打开 <kbd>Esc</kbd>关闭</footer>
  </div>
</dialog>
```

```css
.admin-search-dialog { inline-size:min(760px,calc(100vw - 48px)); max-block-size:min(680px,calc(100dvh - 48px));
  padding:0; border:0; background:transparent; color:var(--text); }
.admin-search-dialog::backdrop { background:rgb(25 42 70 / .32); backdrop-filter:blur(3px); }
.admin-search-dialog__panel { display:grid; grid-template-rows:auto auto minmax(0,1fr) auto; max-block-size:inherit;
  overflow:hidden; border:1px solid var(--line-soft); border-radius:20px; background:var(--panel);
  box-shadow:0 18px 50px rgb(27 62 116 / .18); }
.admin-search-dialog__header { display:grid; grid-template-columns:44px minmax(0,1fr) 36px; align-items:center; gap:12px;
  min-block-size:72px; padding:14px 20px 10px; }
.admin-search-dialog__mark { display:grid; place-items:center; inline-size:44px; block-size:44px; border-radius:14px;
  background:var(--tint-blue); color:var(--accent-link); font-size:30px; line-height:1; }
.admin-search-dialog__header h2 { margin:0; font:650 18px/1.3 var(--sans); }
.admin-search-dialog__header p { margin:3px 0 0; color:var(--muted); font:400 12px/1.4 var(--sans); }
.admin-search-dialog__close { display:grid; place-items:center; inline-size:36px; block-size:36px; border:0; border-radius:10px;
  background:transparent; color:var(--text-soft); font-size:28px; line-height:1; cursor:pointer; }
.admin-search-dialog__close:hover { background:var(--tint-blue); color:var(--accent-link); }
.admin-search-dialog__field { display:block; margin:0 20px 14px; }
.admin-search-dialog__field input { inline-size:100%; block-size:50px; padding:0 14px; border:1px solid var(--accent);
  border-radius:12px; background:var(--panel); color:var(--text); font:400 14px var(--sans); outline:0;
  box-shadow:0 0 0 3px color-mix(in srgb,var(--accent) 12%,transparent); }
.admin-search-dialog__results { min-block-size:0; overflow:auto; padding:0 12px 8px; }
.admin-search-dialog__hint { padding:10px 20px 14px; color:var(--muted); font:400 11px/1.4 var(--sans); }
.admin-search-dialog__hint kbd { padding:2px 5px; border:1px solid var(--line-soft); border-radius:5px; background:var(--panel-muted); color:var(--accent-link); }
@media(max-width:600px) {
  .admin-search-dialog { inline-size:calc(100vw - 24px); max-block-size:calc(100dvh - 24px); }
  .admin-search-dialog__panel { border-radius:16px; }
  .admin-search-dialog__header { padding-inline:14px; }
  .admin-search-dialog__field { margin-inline:14px; }
}
```

打开时把焦点放到搜索输入，输入变化只更新真实结果列表，不重建弹窗外框或清空正在编辑的查询。上下方向键移动唯一的 `aria-selected` 结果，Enter 导航到真实页面，Esc、关闭按钮和允许的遮罩点击关闭；关闭后焦点回到原搜索入口。模态打开期间底层页面不可点击，背景不滚动；弹窗结果区可以独立滚动且滚动到首尾不会把页面带动。优先使用目标项目已有可靠 Dialog 组件或原生 `<dialog>` 的模态能力，不能额外叠加手写焦点陷阱和第二套遮罩。主题、滚动条、空态和错误态都必须从同一套后台 token 读取。

验收浅色／深色、1920／1280／768／390宽、长页面名、长说明、无结果、结果很多、键盘快速切换和关闭后焦点返回。重点排除：标题与placeholder重复、弹窗过宽或过高、结果列表挤压、滚动条越界、浅色主题弹窗套深色默认样式、背景仍可滚动、选中结果没有明显对比度，以及搜索入口和快捷键打开了两套不同的搜索界面。

容器≤640px时先隐藏辅助状态并收紧搜索与用户名；这是组件自身的空间规则，不改变全局侧栏断点。≤960视口的搜索宽在150–200px间适配，≤600仍固定36px图标入口。若面包屑或账户名称增长造成真实碰撞，应先将中间面包屑收为有名称的上级入口、缩短搜索提示、按本文件切换搜索图标形态；保留当前页的可访问名称和关键控件。不用整页缩放、隐藏body横向溢出或挤小按钮。验收不仅检查body横向滚动，也检查最右按钮是否仍在顶栏的内容边界内；不能只因按钮没重叠就忽略它挤出面板留白。

## 必须绑定的交互与验收

- 折叠：桌面切换侧栏实宽与Grid轨道，aria-expanded及Fold／Expand同步；手机同一入口打开模态导航，Escape与焦点返回由已有组件处理，不能隐藏侧栏后没有入口。
- 搜索：按钮、侧栏搜索、⌘／Ctrl+K必须打开同一个居中的模态搜索弹窗，按本文件的标题栏、输入区、结果列表、空态和尺寸层级实现；不能改成下拉菜单、内嵌假输入或无层次的大白框。搜索真实可访问页面，空结果有说明；上下键选择、Enter真正导航，Esc／关闭按钮／允许的遮罩点击关闭，关闭后焦点回到触发入口。模态期间底层不可点击且不滚动，结果区可独立滚动；监听器只在应用挂载时注册并在卸载清理，不拦截普通输入与IME组合。
- 状态：真实请求驱动等待／同步／就绪／失败，图标和文案一起更新；详细错误就地保留或有恢复入口。状态变化可礼貌播报，不在每次轮询反复打断读屏。
- 主题：浅色／深色／跟随系统由目标项目的主题机制持久化，按钮图标反映解析后的主题；弹层、图表和所有body下浮层同步。沿用可靠菜单组件的焦点和关闭行为。
- 刷新：真实Promise驱动busy与禁重复，保留旧数据；结束或失败后停止旋转与波纹，显示实际反馈。波纹900ms等细节沿用动效规范，不叠加两套spinner。
- 账户：头像与用户名来自同一用户模型；打开真实账户菜单。菜单只包含实际支持的账户／退出等动作，不用点击账户图标直接退出；完整用户名可通过可访问名称或提示读取。
- 核对：1920／1280／768／390宽、长面包屑与长用户名、浅深主题、键盘Tab及菜单开关、刷新失败和减弱动态。桌面七个职责、控件顺序、浅蓝图标底座、搜索快捷键与头像结构逐项齐全；在运行截图中发现缺项先修共享顶栏，不逐页补丁。

上面的HTML／CSS负责视觉结构，动作必须在目标项目接入，不能把示例渲染成功称为数据刷新、登录状态或菜单交互已完成。示例与验证文件仅在项目外临时环境使用，skill不附带前端工程。

## 顶部栏纠偏提示词

```text
按ui-atlas的admin-topbar规范修正所有登录后页面共用的顶部栏，以概览参考图为准。
保留18圆角白色悬浮外框、细浅蓝边和轻影、68内容高/18横向padding/gap16。
左侧36×36浅蓝圆角Fold/Expand按钮，再接12px紧凑面包屑与10px细chevron。
右侧依次是36高浅蓝渐变搜索入口及9px快捷键胶囊、带图标的语义色状态胶囊、
36×36浅蓝太阳/月亮按钮、同尺寸顺时针刷新按钮、26头像+11px用户名的账户入口。
按本文件基准SVG与CSS实现，不能简化成裸黑色折叠图标、接入文档链接、一个
绿色裸点和盾牌账户名。状态文案映射真实数据，不把身份验证替代数据同步状态。
手机按规范收起面包屑、搜索文案、状态与用户名，保留折叠/搜索/主题/刷新/头像。
绑定真实导航开合、统一命令搜索与快捷键、搜索模态弹窗、主题菜单、请求刷新和账户菜单，
逐项验证键盘、busy、失败、焦点返回、长内容和浅深主题；不要只画一条白色容器。
```
