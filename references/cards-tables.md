# 卡片与表格

GIF 看连续运动，六帧图看状态变化。按当前项目需求实现目标组件的交互与动效。

## 目录

- [轮播 / Carousel](#carousel)
- [瀑布流 / Masonry](#masonry)
- [翻转卡片 / Flip Card](#flip-card)
- [统计卡片 / Stat Card](#stat-card)
- [时间线 / Timeline](#timeline)
- [头像组 / Avatar Group](#avatar-group)
- [徽标 / Badge](#badge)
- [标签 / Tag](#tag)
- [折叠面板 / Accordion](#accordion)
- [固定表头 / Fixed Header](#fixed-header)
- [排序和筛选 / Sort & Filter](#sort-filter)
- [行内操作 / Row Actions](#row-actions)
- [斑马纹 / Zebra Stripes](#zebra-stripes)
- [卡片和列表 / Card & List](#card-list)

<a id="carousel"></a>
## 轮播 / Carousel

- 标识：`cards-tables/carousel`；类型：组件／效果。
- 效果要点：多张图或卡片左右切换；自动切换不宜过快，悬停暂停，保留左右箭头和指示圆点供手动切换。
- 指令例句：轮播支持手动箭头和圆点，自动播放克制，悬停暂停。
- 参考：[GIF 动图](../assets/gifs/cards-tables/carousel.gif) · [六帧对照图](../assets/filmstrips/cards-tables/carousel.jpg)。

![轮播：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/carousel.jpg)

<a id="masonry"></a>
## 瀑布流 / Masonry

- 标识：`cards-tables/masonry`；类型：组件／效果。
- 效果要点：卡片等宽而高度不同，按列紧凑排列；适合尺寸不一的大量图片，减少空白。
- 指令例句：图片集合使用等宽、不等高的 Masonry 瀑布流。
- 参考：[GIF 动图](../assets/gifs/cards-tables/masonry.gif) · [六帧对照图](../assets/filmstrips/cards-tables/masonry.jpg)。

![瀑布流：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/masonry.jpg)

<a id="flip-card"></a>
## 翻转卡片 / Flip Card

- 标识：`cards-tables/flip-card`；类型：组件／效果。
- 效果要点：鼠标进入时卡片像翻牌一样转到背面，展示更多说明；适合正面图片、背面权益说明。
- 指令例句：会员卡正面展示图片，交互后翻到背面展示权益说明。
- 参考：[GIF 动图](../assets/gifs/cards-tables/flip-card.gif) · [六帧对照图](../assets/filmstrips/cards-tables/flip-card.jpg)。

![翻转卡片：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/flip-card.jpg)

<a id="stat-card"></a>
## 统计卡片 / Stat Card

- 标识：`cards-tables/stat-card`；类型：组件／效果。
- 效果要点：一张卡片突出一个大数字，并用趋势箭头表现涨跌；常用于后台首页订单和销售指标。
- 指令例句：每张统计卡突出一个核心数字，附清楚的趋势和比较口径。
- 参考：[GIF 动图](../assets/gifs/cards-tables/stat-card.gif) · [六帧对照图](../assets/filmstrips/cards-tables/stat-card.jpg)。

![统计卡片：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/stat-card.jpg)

<a id="timeline"></a>
## 时间线 / Timeline

- 标识：`cards-tables/timeline`；类型：组件／效果。
- 效果要点：竖线与圆点按时间串联事件；用于物流、订单记录和公司历程。
- 指令例句：物流记录按时间线排列，圆点对应事件。
- 参考：[GIF 动图](../assets/gifs/cards-tables/timeline.gif) · [六帧对照图](../assets/filmstrips/cards-tables/timeline.jpg)。

![时间线：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/timeline.jpg)

<a id="avatar-group"></a>
## 头像组 / Avatar Group

- 标识：`cards-tables/avatar-group`；类型：组件／效果。
- 效果要点：多个圆形头像重叠，末尾用 +N 表示未展示人数；用于参与者和协作者。
- 指令例句：参与者用重叠头像组显示，超出部分显示 +N。
- 参考：[GIF 动图](../assets/gifs/cards-tables/avatar-group.gif) · [六帧对照图](../assets/filmstrips/cards-tables/avatar-group.jpg)。

![头像组：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/avatar-group.jpg)

<a id="badge"></a>
## 徽标 / Badge

- 标识：`cards-tables/badge`；类型：组件／效果。
- 效果要点：图标角落显示小红点或计数；较大数量显示 99+，避免数字撑大组件。
- 指令例句：未读消息使用小徽标，超过上限显示 99+。
- 参考：[GIF 动图](../assets/gifs/cards-tables/badge.gif) · [六帧对照图](../assets/filmstrips/cards-tables/badge.jpg)。

![徽标：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/badge.jpg)

<a id="tag"></a>
## 标签 / Tag

- 标识：`cards-tables/tag`；类型：组件／效果。
- 效果要点：小圆角色块表达已付款、待发货等状态；建议控制颜色种类，避免过于杂乱。
- 指令例句：订单状态用统一含义的标签表达，颜色克制且带文字。
- 参考：[GIF 动图](../assets/gifs/cards-tables/tag.gif) · [六帧对照图](../assets/filmstrips/cards-tables/tag.jpg)。

![标签：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/tag.jpg)

<a id="accordion"></a>
## 折叠面板 / Accordion

- 标识：`cards-tables/accordion`；类型：组件／效果。
- 效果要点：点击标题展开内容，再点收起；适合 FAQ、设置和手机上的较长内容。
- 指令例句：常见问题使用 Accordion，点击问题展开或收起答案。
- 参考：[GIF 动图](../assets/gifs/cards-tables/accordion.gif) · [六帧对照图](../assets/filmstrips/cards-tables/accordion.jpg)。

![折叠面板：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/accordion.jpg)

<a id="fixed-header"></a>
## 固定表头 / Fixed Header

- 标识：`cards-tables/fixed-header`；类型：组件／效果。
- 效果要点：滚动表格时表头保留；列较多时也可固定首列，以便持续辨认含义。
- 指令例句：表格滚动时固定表头，需要横向滚动时固定标识列。
- 参考：[GIF 动图](../assets/gifs/cards-tables/fixed-header.gif) · [六帧对照图](../assets/filmstrips/cards-tables/fixed-header.jpg)。

![固定表头：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/fixed-header.jpg)

<a id="sort-filter"></a>
## 排序和筛选 / Sort & Filter

- 标识：`cards-tables/sort-filter`；类型：组件／效果。
- 效果要点：列标题箭头改变排序，小漏斗按条件过滤行；示例只看待发货订单。
- 指令例句：列标题支持排序，并允许按订单状态筛选。
- 参考：[GIF 动图](../assets/gifs/cards-tables/sort-filter.gif) · [六帧对照图](../assets/filmstrips/cards-tables/sort-filter.jpg)。

![排序和筛选：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/sort-filter.jpg)

<a id="row-actions"></a>
## 行内操作 / Row Actions

- 标识：`cards-tables/row-actions`；类型：组件／效果。
- 效果要点：悬停某一行时，在行尾出现编辑和删除操作，默认隐藏以减少视觉负担。
- 指令例句：行尾操作在悬停和键盘聚焦时显示，触摸端提供可见操作入口。
- 参考：[GIF 动图](../assets/gifs/cards-tables/row-actions.gif) · [六帧对照图](../assets/filmstrips/cards-tables/row-actions.jpg)。

![行内操作：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/row-actions.jpg)

<a id="zebra-stripes"></a>
## 斑马纹 / Zebra Stripes

- 标识：`cards-tables/zebra-stripes`；类型：组件／效果。
- 效果要点：行背景深浅交替，帮助阅读长列表；同时应注意金额等数字右对齐便于比较。
- 指令例句：长表格使用轻微斑马纹，金额列右对齐。
- 参考：[GIF 动图](../assets/gifs/cards-tables/zebra-stripes.gif) · [六帧对照图](../assets/filmstrips/cards-tables/zebra-stripes.jpg)。

![斑马纹：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/zebra-stripes.jpg)

<a id="card-list"></a>
## 卡片和列表 / Card & List

- 标识：`cards-tables/card-list`；类型：组件／效果。
- 效果要点：基础卡片和列表作为对照；不要求额外的特殊动画。
- 指令例句：按内容结构使用基础卡片或列表，不附加未指定效果。
- 参考：[GIF 动图](../assets/gifs/cards-tables/card-list.gif) · [六帧对照图](../assets/filmstrips/cards-tables/card-list.jpg)。

![卡片和列表：按时间从左到右、从上到下阅读](../assets/filmstrips/cards-tables/card-list.jpg)
