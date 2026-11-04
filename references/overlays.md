# 弹窗与浮层

静态图用于查看构图与可见状态，连续运动和短暂状态需在实际项目验证。按当前项目需求实现目标组件的交互与动效。

## 目录

- [弹窗](#modal)
- [确认弹窗](#alert-dialog)
- [抽屉](#drawer)
- [底部弹层](#bottom-sheet)
- [轻提示](#toast)
- [通知](#notification)
- [轻提示与通知选型](#toast-vs-notification)
- [保存成功提示纠正](#success-toast-correction)
- [气泡提示](#tooltip)
- [气泡卡片](#popover)
- [气泡确认框](#popconfirm)
- [下拉菜单](#dropdown-menu)
- [带安全三角区的级联菜单](#safe-cascade-menu)
- [提示、跟随气泡与浮层决策](#overlay-decision)

<a id="modal"></a>
## 弹窗 / Modal

- 标识：`overlays/modal`；类型：组件／效果。
- 效果要点：屏幕中央弹出内容；背后有半透明遮罩 Overlay；示例支持右上角关闭和 Esc 关闭。用于当前需要集中处理的任务。
- 指令例句：为这个任务使用 Modal，保留遮罩、关闭按钮和 Esc 关闭。
- 媒体取舍：重点是中央面板、遮罩和关闭入口；现有素材主要停留讲解，没有值得单独保留的开闭运动。

<!-- ui-atlas:details overlays/modal -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/modal-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![弹窗：原尺寸独立参考](../assets/details/overlays/modal-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="alert-dialog"></a>
## 确认弹窗 / Alert Dialog

- 标识：`overlays/alert-dialog`；类型：组件／效果。
- 效果要点：删除等操作前询问是否确定；与普通弹窗区别是必须明确作出选择，点击空白遮罩不直接关闭。
- 指令例句：删除前显示确认弹窗，明确提供取消和删除，点击遮罩不确认也不关闭。
- 媒体取舍：重点是确认语义、按钮与遮罩规则，图片加文字足够；行为仍需项目验证。

<!-- ui-atlas:details overlays/alert-dialog -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/alert-dialog-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![确认弹窗：原尺寸独立参考](../assets/details/overlays/alert-dialog-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="drawer"></a>
## 抽屉 / Drawer

- 标识：`overlays/drawer`；类型：组件／效果。
- 效果要点：从屏幕侧边滑出整块面板；适合内容较多、仍需对照原页面的筛选和详情。
- 指令例句：把筛选条件放入侧边抽屉，保留对主页面的上下文。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details overlays/drawer -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/drawer-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![抽屉：原尺寸独立参考](../assets/details/overlays/drawer-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="bottom-sheet"></a>
## 底部弹层 / Bottom Sheet

- 标识：`overlays/bottom-sheet`；类型：组件／效果。
- 效果要点：从屏幕底部向上滑出，便于手机拇指操作；移动端承载弹出内容时可考虑使用。
- 指令例句：移动端使用从底部滑出的 Bottom Sheet 呈现这些选项。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details overlays/bottom-sheet -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/bottom-sheet-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![底部弹层：原尺寸独立参考](../assets/details/overlays/bottom-sheet-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="toast"></a>
## 轻提示 / Toast / Snackbar

- 标识：`overlays/toast`；类型：组件／效果。
- 效果要点：保存成功等简短反馈在上方或下方出现，几秒后自动消失；部分组件库称 Snackbar，可带撤销。
- 指令例句：保存成功后使用 Toast，3 秒后自动消失，无需用户再点确定。
- 媒体取舍：位置、文案和撤销样式由图片表达；现有素材未完整演示自动消失，不作为计时证据。

<!-- ui-atlas:details overlays/toast -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/toast-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![轻提示：原尺寸独立参考](../assets/details/overlays/toast-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="notification"></a>
## 通知 / Notification

- 标识：`overlays/notification`；类型：组件／效果。
- 效果要点：通常出现在右上角，比 Toast 大，有标题和正文；停留更久，通常带关闭按钮，如新订单提醒。
- 指令例句：用有标题、正文和关闭按钮的通知显示新订单，停留时间长于普通轻提示。
- 媒体取舍：标题、正文、关闭入口和位置是重点，普通出现过程没有独立参考价值。

<!-- ui-atlas:details overlays/notification -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/notification-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![通知：原尺寸独立参考](../assets/details/overlays/notification-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="toast-vs-notification"></a>
## 轻提示与通知选型 / Toast vs Notification

- 标识：`overlays/toast-vs-notification`；类型：选型／纠错。
- 效果要点：只需看一眼的反馈用轻提示；希望用户注意并可持续查看的消息用通知。
- 指令例句：将简短成功反馈与可持续查看的通知分开处理。
- 媒体取舍：属于消息语义与样式对比，图片和选型说明足够。

<!-- ui-atlas:details overlays/toast-vs-notification -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/toast-hd-01.webp) · [02 · 2880×1770](../assets/details/overlays/notification-hd-01.webp)。
- 多图用途：属于消息语义与样式对比，图片和选型说明足够。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![轻提示与通知选型：原尺寸独立参考](../assets/details/overlays/toast-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="success-toast-correction"></a>
## 保存成功提示纠正 / Success feedback correction

- 标识：`overlays/success-toast-correction`；类型：选型／纠错。
- 效果要点：将强制点确定的保存成功弹窗改为轻提示；建议 3 秒后自动消失。
- 指令例句：把保存成功弹窗改成 Toast，3 秒后自动消失。
- 媒体取舍：属于弹窗改轻提示的前后方案对比，无需保留讲解过程。

<!-- ui-atlas:details overlays/success-toast-correction -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/success-toast-correction-hd-01.webp) · [02 · 2880×1770](../assets/details/overlays/success-toast-correction-hd-02.webp)。
- 多图用途：属于弹窗改轻提示的前后方案对比，无需保留讲解过程。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![保存成功提示纠正：原尺寸独立参考](../assets/details/overlays/success-toast-correction-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="tooltip"></a>
## 气泡提示 / Tooltip

- 标识：`overlays/tooltip`；类型：组件／效果。
- 效果要点：悬停时出现一句解释，移开消失，如导出图标说明；手机没有鼠标悬停，重要信息不能仅藏在这里。
- 指令例句：给导出图标添加 Tooltip；关键说明同时保留可见或触摸可访问入口。
- 媒体取舍：锚点位置与简短解释由图片表达，悬停与离开规则由文字描述。

<!-- ui-atlas:details overlays/tooltip -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/tooltip-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![气泡提示：原尺寸独立参考](../assets/details/overlays/tooltip-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="popover"></a>
## 气泡卡片 / Popover

- 标识：`overlays/popover`；类型：组件／效果。
- 效果要点：点击触发，在锚点附近展示较丰富的内容甚至操作按钮；例子为点击头像展示客户信息。
- 指令例句：点击客户头像打开带详情和操作的 Popover。
- 媒体取舍：重点是锚定位置、内容与操作构成，图片加触发规则足够。

<!-- ui-atlas:details overlays/popover -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/popover-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![气泡卡片：原尺寸独立参考](../assets/details/overlays/popover-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="popconfirm"></a>
## 气泡确认框 / Popconfirm

- 标识：`overlays/popconfirm`；类型：组件／效果。
- 效果要点：在删除按钮旁用小气泡询问是否确定，视觉负担低于整页确认弹窗。
- 指令例句：在这一行删除按钮旁显示 Popconfirm，提供取消和确认删除。
- 媒体取舍：重点是就地确认的位置与按钮，图片加确认规则足够。

<!-- ui-atlas:details overlays/popconfirm -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/popconfirm-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![气泡确认框：原尺寸独立参考](../assets/details/overlays/popconfirm-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="dropdown-menu"></a>
## 下拉菜单 / Dropdown Menu

- 标识：`overlays/dropdown-menu`；类型：组件／效果。
- 效果要点：点击后向下展开一串操作选项，如头像菜单中的设置、退出登录。
- 指令例句：点击头像展开 Dropdown Menu，包含设置和退出登录。
- 媒体取舍：重点是操作列表及触发入口，普通展开无需单独保留 GIF。

<!-- ui-atlas:details overlays/dropdown-menu -->
- 原尺寸图片：[01 · 2880×1770](../assets/details/overlays/dropdown-menu-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![下拉菜单：原尺寸独立参考](../assets/details/overlays/dropdown-menu-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="safe-cascade-menu"></a>
## 带安全三角区的级联菜单 / Safe Triangle Cascading Menu

- 标识：`overlays/safe-cascade-menu`；类型：组件／效果。
- 效果要点：用上一指针位置和子菜单近侧两角构造安全三角区，保护斜向移动；220ms 打开、360ms 关闭、1200ms 保护上限。
- 实现关注：保存最近两个 pointermove 坐标，以较早坐标作三角顶点。指针向子菜单移动时忽略路过行的高亮与打开；每 80ms 重查，离开保护区或达到 1200ms 后切换。拖过文件夹时用 420ms 打开。右侧不足时左翻，三角区改接子菜单右边；离开再返回取消关闭计时。行高亮由状态驱动，不能依赖 CSS :hover。
- 验证重点：检查缓慢斜移、停在保护区、快速往返、左右翻转、独立滚动、触摸和方向键；Esc 关闭并归还焦点。
- 指令例句：参考 overlays/safe-cascade-menu，用上一指针位置和子菜单近侧两角构造安全三角区，保护斜向移动；220ms 打开、360ms 关闭、1200ms 保护上限。
- [完整配方与效果参考](recipes/safe-cascade-menu.md) · [效果图](../assets/recipes/safe-cascade-menu.jpg)。
- 媒体取舍：高清图片用于观察父子菜单的层级与间距；安全区的指针轨迹和延时仍需在项目中验证。

<a id="overlay-decision"></a>
## 提示、跟随气泡与浮层决策 / Floating UI Decision Guide

- 标识：`overlays/overlay-decision`；类型：选型／纠错。
- 效果要点：按解释对象、可逆性、影响范围、表单长度和是否需要对照页面，在 Tooltip、Cursor Tip、Popover、Popconfirm、Dialog、Drawer 与独立页之间选型。
- 实现关注：元素的简短解释用 Tooltip；区域内持续读数用跟随气泡；有可点击操作改为 Popover。可撤销操作在产品规则允许时执行并提供真实 Undo；单项不可逆操作可用就地确认，影响大、批量或需决策用 Dialog。短表单且无需参照页面用弹窗；长表单或需对照页面用抽屉；主要任务或需独立 URL 用页面。现有保存机制优先，不把所有抽屉表单改为即时保存。
- 验证重点：逐个记录触发、内容、当前与目标类型；检查确认前不执行、取消可恢复、未保存退出提示、焦点回归、视口避让，以及键盘与触摸入口。
- 指令例句：参考 overlays/overlay-decision，按解释对象、可逆性、影响范围、表单长度和是否需要对照页面，在 Tooltip、Cursor Tip、Popover、Popconfirm、Dialog、Drawer 与独立页之间选型。
- [完整配方与效果参考](recipes/overlay-decision.md) · [效果图](../assets/recipes/overlay-decision.jpg)。
- 媒体取舍：保留未遮挡抽屉主体的打开片段，用于观察覆盖层、侧向入场和表单的关系。

- 连续动效：[GIF 片段](../assets/recipes/overlay-decision.gif)。
