# 清爽蓝白后台：页内彩色菜单与分段筛选

主侧栏的精确组色见[组件规范](admin-components.md#clean-admin-sidebar)。本文件用于设置目录、资料导航、页内模块菜单，以及记录范围／状态等分段筛选；按[基础设计](admin-design.md)的token与[动效规则](admin-motion.md)实现。页内菜单的逐项配色是本风格按需扩展的约定，不声称所有参考页面已有逐像素原稿。

<a id="clean-admin-page-menus"></a>

## 页内菜单必须保留分类色

彩色视觉延续到页面内部，不只停在主侧栏。配置目录、个人中心子导航、模块入口等带图标菜单，按实际职责配置稳定的item tone；默认状态有彩色线框图标与浅色底座，不能全设为muted灰色或默认蓝。相同业务项在不同页面复用相同tone；新增项从下表按职责分配，不按数组序号随机循环，重排与过滤后颜色不变。

| tone | 图标／强调色（浅色主题） | 浅色底座 | 可映射职责示例 |
|---|---|---|---|
| blue | #2478ff | #edf4ff | 基本信息、总览 |
| violet | #9860c1 | #f4f0fa | 资源、内容、分发 |
| cyan | #2192a7 | #edf8fa | 用户、接入、通信 |
| mint | #287553 | #eff8f2 | 数据、同步、保存策略 |
| amber | #bd7351 | #fff7e9 | 运营、任务、推广 |
| rose | #c34b67 | #fff0f5 | 安全、权限、需注意的策略 |

这是分类色，不表达成功／失败；破坏性动作仍遵守Danger语义。深色保留tone区别，底座映射tint主题，必要时将图标适配为blue #88baff、violet #cf93f0、cyan #8ed5df、mint #8cd6ac、amber #e6bc7f、rose #f3a4b1，再核对实际对比。不能使用低透明度整块菜单实现浅色，把文字也一起变淡。

目录组标题：11–12px、text-soft／muted，可在标题前复用4×10短竖线；用该组tone，不能每组全灰。普通带说明菜单行采用58px起高、padding10 12、列32px minmax(0,1fr) 12px、gap10、圆角10；图标底座32×32／圆角9、内部17px线框，标题13／550、说明12／1.5，末尾12px箭头。较宽设置目录可用36px底座、14px标题；同一目录使用同一档，长说明自然换行，不照着放大的截图把菜单行做成巨型卡。

默认无整行底色；hover浅蓝面，保留item图标色；当前项tint-blue底、accent-link标题、白／panel图标底座，图标仍保留该项tone；说明保持muted、右箭头accent-link。当前项还需aria-current或aria-selected与实际路由／面板同步，不能只换颜色而内容不切换。focus-visible为2px可见环；disabled不跳转、不hover、不只靠透明度说明原因。页内选中面是浅蓝，与主侧栏的蓝色渐变选中面区分。

切换独立页面用真实链接；同页切换面板使用具有正确键盘行为的Tabs／按钮导航；跳到设置分区则用真实锚点并处理当前分区。语义按任务确定，不因为都“长得像菜单”就全部套role=menu。保留表单草稿、焦点、滚动与实际保存语义；长配置表需要目录导航时才加入，不能给每张小表单再包一层左菜单。

```css
.admin-page-menu { --item-ink:#2478ff; --item-tint:var(--tint-blue); }
.admin-page-menu[data-item-tone="violet"] { --item-ink:#9860c1; --item-tint:var(--tint-purple); }
.admin-page-menu[data-item-tone="cyan"] { --item-ink:#2192a7; --item-tint:var(--tint-cyan); }
.admin-page-menu[data-item-tone="mint"] { --item-ink:var(--green); --item-tint:var(--tint-green); }
.admin-page-menu[data-item-tone="amber"] { --item-ink:#bd7351; --item-tint:var(--tint-amber); }
.admin-page-menu[data-item-tone="rose"] { --item-ink:var(--red); --item-tint:#fff0f5; }
.admin-page-menu { display:grid; grid-template-columns:32px minmax(0,1fr) 12px; align-items:center;
  gap:10px; min-block-size:58px; padding:10px 12px; border:0; border-radius:10px;
  background:transparent; color:var(--text-soft); text-align:start; text-decoration:none;
  transition:background-color 160ms ease,color 160ms ease; }
.admin-page-menu__icon { display:grid; place-items:center; inline-size:32px; block-size:32px;
  border-radius:9px; color:var(--item-ink); background:var(--item-tint); }
.admin-page-menu__icon svg { display:block; inline-size:17px; block-size:17px; }
.admin-page-menu__copy { min-inline-size:0; }
.admin-page-menu__copy b { display:block; font:550 13px/1.5 var(--sans); }
.admin-page-menu__copy small { display:block; margin-block-start:4px; color:var(--muted); font:400 12px/1.5 var(--sans); }
.admin-page-menu__arrow { inline-size:12px; block-size:12px; color:var(--faint); }
.admin-page-menu:hover:not(:disabled):not([aria-disabled="true"]) { background:var(--tint-blue); }
.admin-page-menu:is([aria-current="page"],[aria-selected="true"]) { background:var(--tint-blue); color:var(--accent-link); }
.admin-page-menu:is([aria-current="page"],[aria-selected="true"]) .admin-page-menu__icon { background:var(--panel); }
.admin-page-menu:is([aria-current="page"],[aria-selected="true"]) .admin-page-menu__arrow { color:var(--accent-link); }
.admin-page-menu:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.admin-page-menu:is(:disabled,[aria-disabled="true"]) { opacity:.5; cursor:not-allowed; }
:root[data-theme="dark"] .admin-page-menu { --item-ink:#88baff; }
:root[data-theme="dark"] .admin-page-menu[data-item-tone="violet"] { --item-ink:#cf93f0; }
:root[data-theme="dark"] .admin-page-menu[data-item-tone="cyan"] { --item-ink:#8ed5df; }
:root[data-theme="dark"] .admin-page-menu[data-item-tone="amber"] { --item-ink:var(--amber); }
:root[data-theme="dark"] .admin-page-menu[data-item-tone="rose"] { --item-ink:var(--red); --item-tint:color-mix(in srgb,var(--red) 10%,var(--panel)); }
:root[data-theme="dark"] .admin-page-menu[data-item-tone="mint"] { --item-ink:var(--green); }
@media(prefers-reduced-motion:reduce) { .admin-page-menu { transition:none; } }
```

结构为菜单入口下的`.admin-page-menu__icon`、`.admin-page-menu__copy`（含b与small）与`.admin-page-menu__arrow`。每个入口设置data-item-tone，图标与纯装饰箭头aria-hidden；链接禁用时仅aria-disabled不够，还须在目标项目阻止导航或呈现说明文字。小屏目录可变为上方可展开导航或可滚动列表，保留分类色、完整名称与当前项，不能挤压右侧表单。

<a id="clean-admin-segmented"></a>

## 分段筛选：浅蓝轨道与蓝色共享滑块

“日常记录／已归档／全部记录”“全部／有效／已撤销／已解除”等是一组选值，使用本节样式；它们是同一个内容区域的范围或状态筛选。每组可使用radiogroup＋radio语义；切换到另一独立内容面板才用Tabs，执行导出／删除才是Menu。分段组选中使用同一套蓝色，不把每个选项都做成四色指标卡。

| 部位 | 精确默认值与状态 |
|---|---|
| 外轨道 | inline Grid等宽N列、padding4、1px workspace-blue-line边、圆角11、min-height38、背景accent 7%混panel |
| 单项 | min-height28、左右padding12、gap6、无边无单独背景、圆角7、11px／500、未选accent-link；手机左右8 |
| 共享滑块 | 仅一个、left/top/bottom4、宽(轨道padding box−8)/N、圆角7、1px #2675ef边、180deg #3484ff→#1764e7；外影0 2 6 rgba(31,101,225,.2)、内白20%高光 |
| 选中 | 白字，hover仍白；滑块以自身宽度translateX(index×100%)，280ms cubic-bezier(.2,.75,.25,1)，文字160ms ease |
| 聚焦 | 当前选项2px accent outline、offset2；每组只有一项tabindex0，焦点与选中视觉是两个状态 |
| 计数 | 可选10px、padding1 4、圆角4；默认text6%混透明，选中白字／白18%底；未知不显示，0保留 |
| 不可用 | 该选项disabled、禁选、跳过键盘循环、.5透明度；整组不可用时没有假选中且显示原因 |
| 减弱动态 | 保留真实选中值，滑块和文字无过渡，点击不等待动画 |

筛选组在工具栏内与38px搜索、主次操作垂直居中、gap12–16。不同组可独立占一行；窄屏先让工具栏换行，单组仍放不下时在自己的横向滚动容器中滚动，不让radio在两行间换位而滑块仍按单行计算。不改变相邻搜索框高度，不能给每个选项都加独立蓝边或把默认项做成白底Tab。

```html
<div class="admin-segment-scroll">
  <div class="admin-segmented" role="radiogroup" aria-label="记录范围" style="--segment-count:3;--segment-index:0">
    <span class="admin-segmented__indicator" aria-hidden="true"></span>
    <button type="button" role="radio" aria-checked="true" tabindex="0" value="daily">日常记录</button>
    <button type="button" role="radio" aria-checked="false" tabindex="-1" value="archived">已归档</button>
    <button type="button" role="radio" aria-checked="false" tabindex="-1" value="all">全部记录</button>
  </div>
</div>
```

```css
.admin-segment-scroll { max-inline-size:100%; min-inline-size:0; overflow-x:auto; padding:4px; }
.admin-segmented { position:relative; isolation:isolate; display:inline-grid;
  grid-template-columns:repeat(var(--segment-count),minmax(0,1fr)); inline-size:max-content;
  min-block-size:38px; padding:4px; border:1px solid var(--workspace-blue-line); border-radius:11px;
  background:color-mix(in srgb,var(--accent) 7%,var(--panel)); }
.admin-segmented__indicator { position:absolute; z-index:-1; left:4px; top:4px; bottom:4px;
  inline-size:calc((100% - 8px) / var(--segment-count));
  transform:translateX(calc(var(--segment-index) * 100%)); border:1px solid #2675ef; border-radius:7px;
  background:linear-gradient(180deg,#3484ff,#1764e7);
  box-shadow:0 2px 6px rgb(31 101 225 / .2),inset 0 1px 0 rgb(255 255 255 / .2);
  transition:transform 280ms cubic-bezier(.2,.75,.25,1); pointer-events:none; }
.admin-segmented > button { display:inline-flex; align-items:center; justify-content:center; gap:6px;
  min-inline-size:0; min-block-size:28px; padding:0 12px; border:0; border-radius:7px;
  background:transparent; color:var(--accent-link); white-space:nowrap; font:500 11px var(--sans);
  transition:color 160ms ease; }
.admin-segmented > button:hover:not(:disabled) { color:var(--accent-strong); }
.admin-segmented > button[aria-checked="true"] { color:#fff; }
.admin-segmented > button:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.admin-segmented > button:disabled { opacity:.5; cursor:not-allowed; }
.admin-segmented small { padding:1px 4px; border-radius:4px; background:color-mix(in srgb,var(--text) 6%,transparent); font-size:10px; }
.admin-segmented [aria-checked="true"] small { color:#fff; background:rgb(255 255 255 / .18); }
@media(max-width:600px) { .admin-segmented > button { padding-inline:8px; } }
@media(prefers-reduced-motion:reduce) { .admin-segmented__indicator,.admin-segmented > button { transition:none; } }
```

在目标组件内绑定唯一value：click即时更新筛选值、aria-checked、roving tabindex与segment-index，再触发真实筛选；不能只移动蓝块。左右键循环跳过disabled，Home／End选首尾可用项，移动后焦点同步；从Tab进入当前项，再次Tab离开整组。初始值失效时选第一个有效项并同步实际model，不能只画首项蓝块；无可用项时隐藏indicator。options变动重新计算N和index，不复用旧索引。

已有框架组件可采用下列无依赖算法映射事件，不必另建前端文件：

```js
// options包含稳定value与disabled；调用方同步实际模型并触发筛选。
function resolveSegment(options, value, key, direction = 'ltr') {
  const enabled = options.filter(option => !option.disabled);
  if (!enabled.length) return null;
  let index = enabled.findIndex(option => option.value === value);
  if (index < 0) index = 0;
  if (key === 'Home') index = 0;
  else if (key === 'End') index = enabled.length - 1;
  else if (key === 'ArrowLeft' || key === 'ArrowRight') {
    const step = (key === 'ArrowRight' ? 1 : -1) * (direction === 'rtl' ? -1 : 1);
    index = (index + step + enabled.length) % enabled.length;
  }
  const selected = enabled[index];
  return { value: selected.value, index: options.findIndex(option => option.value === selected.value) };
}
```

方向键仅在上述键触发时preventDefault；未处理的键保持浏览器行为。焦点切到新radio后只滚动本组容器以露出目标，不拉动整个页面；RTL布局的indicator锚点与位移方向同时镜像，不能只反转键盘箭头。静态示例按LTR布局。

记录范围与状态是两个独立维度，保留两个真实筛选值，组合条件、计数、分页和URL按目标项目现有规则同步；筛选变化后按实际产品回到有效页，不把“归档”变成真正移动／删除记录的操作。请求异步时旧结果不能覆盖新选择，busy反馈局限当前数据区，不阻止用户改选。

## 可直接执行的菜单与筛选提示词

```text
本项目的页内配置目录、资料导航、模块菜单都沿用清爽蓝白风格的分类色。
为每个菜单项配置稳定tone，默认有彩色线框图标和浅色底座；分组标题前短
竖线有对应色，不能只给主侧栏上色、页内全部灰色。按本文件处理hover、
当前项、focus、禁用和小屏导航，保持真实页面／锚点／面板切换语义。
记录范围与状态筛选使用浅蓝圆角轨道+蓝色渐变共享滑块，38高/4padding/
11外圆角/7内圆角/11字，选中白字、未选蓝字，280ms指定曲线。不要用下划线
Tabs、每项独立蓝边或四个不同色块替代。完整实现点击、方向键/Home/End、
单Tab入口、禁用跳过、计数、无效初始值与动态选项，视觉和实际value一致。
筛选改变真实数据与分页；保持搜索、范围与状态的组合，不仅移动蓝色背景。
```
