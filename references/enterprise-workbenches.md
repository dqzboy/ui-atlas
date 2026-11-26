# 企业工作台与业务后台

新建后台未指定视觉风格时，默认使用 [清爽蓝白后台](recipes/clean-admin.md)；明确指定其他风格或沿用已有设计系统时遵从用户要求。

按实际业务对象选择结构：物流配载、企业门户、AI 工具、招聘、生产任务和统计列表的任务目标各不相同。先看条目摘要和静态总览，再查看相关单图细节；不要只因都采用蓝色就互换工作流。

## 证据与实现边界

- 静态总览按图片编号从左到右、从上到下阅读；编号代表独立图片，不代表时间或交互状态。单图链接保留裁切后的完整分辨率。
- “画面要点”描述已查看的素材；“实现补充”和“验证重点”是落地建议，不能当作原稿已具备的功能。
- 图中的品牌、示例数字、人物和业务文案只用于理解层级，不自动成为需求。按用户的产品对象、技术栈和设计系统改写。
- 只读本次相关图片；静态稿未呈现的联动、筛选、点击结果、权限和响应式行为需在实际项目中确认。

## 目录

- [清爽蓝白后台、登录与组件动效](#clean-admin)
- [物流配载与车辆工作台](#logistics-loading-workbench)
- [AI 助手与效率工具工作台](#ai-assistant-productivity-hub)
- [暖橙欢迎区与管理首页](#warm-orange-management-home)
- [MES 生产状态与任务列表](#mes-production-task-management)

<a id="logistics-loading-workbench"></a>
## 物流配载与车辆工作台 / Logistics Loading Workbench

- 标识：`enterprise-workbenches/logistics-loading-workbench`；类型：组件／效果。
- 画面要点：车厢货位模型占据主区，司机、容量和活动日志列于侧边；另一页以车辆选择、装载状态和货物表组织配送任务。
- 指令例句：参考 enterprise-workbenches/logistics-loading-workbench，把货位、负载和清单保持在同一业务上下文；空货位、已装载和不可用应有可区分状态。
- 实现补充：把货位、负载和清单保持在同一业务上下文；空货位、已装载和不可用应有可区分状态。
- 验证重点：摘要与列表的业务口径一致；筛选、排序、分页和空／错／加载状态在项目中实际验证。

<!-- ui-atlas:details enterprise-workbenches/logistics-loading-workbench -->
- 原尺寸图片：[01 · 1920×2110](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/logistics-loading-workbench-01.png) · [02 · 1920×2110](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/logistics-loading-workbench-02.png)。
- 多图用途：不同页面或布局方案各自保留，不按连续抽帧处理。
- 清晰度边界：保留原尺寸与既有裁切，以无损 PNG 避免再次 JPEG 压缩；不能恢复源图已丢失的细节。

![物流配载与车辆工作台：原尺寸独立参考](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/logistics-loading-workbench-01.png)
<!-- /ui-atlas:details -->

<a id="ai-assistant-productivity-hub"></a>
## AI 助手与效率工具工作台 / AI Assistant Productivity Hub

- 标识：`enterprise-workbenches/ai-assistant-productivity-hub`；类型：组件／效果。
- 画面要点：工具卡、文档快捷创建和对话入口构成效率工作台；图集同时提供整页组合与独立设计稿。
- 指令例句：参考 enterprise-workbenches/ai-assistant-productivity-hub，区分新建文档、调用工具和开始对话，输入区的示例问题应能帮助用户发起具体任务。
- 实现补充：区分新建文档、调用工具和开始对话，输入区的示例问题应能帮助用户发起具体任务。
- 验证重点：摘要与列表的业务口径一致；筛选、排序、分页和空／错／加载状态在项目中实际验证。

<!-- ui-atlas:details enterprise-workbenches/ai-assistant-productivity-hub -->
- 原尺寸图片：[01 · 1672×942](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/ai-assistant-productivity-hub-01.png) · [02 · 1920×1080](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/ai-assistant-productivity-hub-02.png) · [03 · 1920×1080](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/ai-assistant-productivity-hub-03.png)。
- 多图用途：保留不同页面的独立稿，移除重复包含这些页面的组合图。
- 清晰度边界：保留原尺寸与既有裁切，以无损 PNG 避免再次 JPEG 压缩；不能恢复源图已丢失的细节。

![AI 助手与效率工具工作台：原尺寸独立参考](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/ai-assistant-productivity-hub-01.png)
<!-- /ui-atlas:details -->

<a id="warm-orange-management-home"></a>
## 暖橙欢迎区与管理首页 / Warm Orange Management Home

- 标识：`enterprise-workbenches/warm-orange-management-home`；类型：组件／效果。
- 画面要点：暖橙欢迎区搭配摘要指标、管理表和任务区域，图集包含整页和独立高清视图。
- 指令例句：参考 enterprise-workbenches/warm-orange-management-home，暖色集中在欢迎与重点数据，表格保持稳定对比和可扫描的行列节奏。
- 实现补充：暖色集中在欢迎与重点数据，表格保持稳定对比和可扫描的行列节奏。
- 验证重点：摘要与列表的业务口径一致；筛选、排序、分页和空／错／加载状态在项目中实际验证。

<!-- ui-atlas:details enterprise-workbenches/warm-orange-management-home -->
- 原尺寸图片：[01 · 1780×974](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/warm-orange-management-home-01.png) · [02 · 1984×1182](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/warm-orange-management-home-02.png)。
- 多图用途：保留不同页面的独立稿，移除重复包含这些页面的组合图。
- 清晰度边界：保留原尺寸与既有裁切，以无损 PNG 避免再次 JPEG 压缩；不能恢复源图已丢失的细节。

![暖橙欢迎区与管理首页：原尺寸独立参考](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/warm-orange-management-home-01.png)
<!-- /ui-atlas:details -->

<a id="mes-production-task-management"></a>
## MES 生产状态与任务列表 / Mes Production Task Management

- 标识：`enterprise-workbenches/mes-production-task-management`；类型：组件／效果。
- 画面要点：浅色生产后台以状态摘要、进度条、业务表和通知组合生产管理视图。
- 指令例句：参考 enterprise-workbenches/mes-production-task-management，生产任务进度要有清楚完成标准，异常和通知区分优先级，并能定位具体记录。
- 实现补充：生产任务进度要有清楚完成标准，异常和通知区分优先级，并能定位具体记录。
- 验证重点：摘要与列表的业务口径一致；筛选、排序、分页和空／错／加载状态在项目中实际验证。

<!-- ui-atlas:details enterprise-workbenches/mes-production-task-management -->
- 原尺寸图片：[01 · 1920×2110](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/mes-production-task-management.png)。
- 清晰度边界：保留原尺寸与既有裁切，以无损 PNG 避免再次 JPEG 压缩；不能恢复源图已丢失的细节。

![MES 生产状态与任务列表：原尺寸独立参考](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/enterprise-workbenches/mes-production-task-management.png)
<!-- /ui-atlas:details -->

<a id="clean-admin"></a>
## 清爽蓝白后台、登录与组件动效 / Clean Blue Admin Design System and Motion

- 标识：`enterprise-workbenches/clean-admin`；类型：后台风格／组件实现配方。
- 适用场景：创建新后台、既有管理系统换肤，以及登录页、概览、目录、列表、文档、资料与配置页面。
- 画面要点：浅蓝背景，独立圆角侧栏和顶栏，蓝色渐变主按钮，紫／珊瑚／玫红／青色摘要卡与白色业务面板。
- 实现提示词：读取 [完整配方](recipes/clean-admin.md)、[布局与主题](admin-design.md)、[逐页提示词](admin-pages.md)、[组件与按钮状态](admin-components.md)、[组件动效](admin-motion.md)，把规范落到目标项目的现有技术栈与组件；品牌和业务数据按目标替换。
- 动效范围：箭头蓝底展开、三点与文字变色、按压、导航折叠、分段滑块、页签标记、数字滚动、徽标、卡片悬停、连续展开、刷新、进度环、弹窗抽屉、登录验证、保存和任务反馈；参数与状态规则见动效文档。
- 核对要点：浅深主题、390／768／1280／1920宽度、键盘与焦点、快速反向、减弱动态、真实加载与失败；原业务与安全策略不作为新项目需求。
- 媒体取舍：只保留虚构数据重新渲染的独立页面和关键两态；不把完整前端工程、原账号截图或大体积动画放进skill。

<!-- ui-atlas:details enterprise-workbenches/clean-admin -->
- 原尺寸图片：[01 · 3840×2160](../assets/details/enterprise-workbenches/clean-admin-login.webp) · [02 · 704×652](../assets/details/enterprise-workbenches/clean-admin-login-puzzle.webp) · [03 · 3840×2160](../assets/details/enterprise-workbenches/clean-admin-overview.webp) · [04 · 3840×2160](../assets/details/enterprise-workbenches/clean-admin-overview-dark.webp) · [05 · 3840×2160](../assets/details/enterprise-workbenches/clean-admin-products.webp) · [06 · 3840×2160](../assets/details/enterprise-workbenches/clean-admin-docs.webp) · [07 · 3840×2160](../assets/details/enterprise-workbenches/clean-admin-account.webp) · [08 · 3840×2160](../assets/details/enterprise-workbenches/clean-admin-settings.webp) · [09 · 3840×2160](../assets/details/enterprise-workbenches/clean-admin-components.webp) · [10 · 290×78](../assets/details/enterprise-workbenches/clean-admin-arrow-default.webp) · [11 · 290×78](../assets/details/enterprise-workbenches/clean-admin-arrow-expanded.webp)。
- 清晰度边界：不同页面与状态的静态参考，不是整段动画记录；字体来自截图系统，业务流程、账号验证与图表数据为虚构。箭头两态不单独证明运动时序；动画在目标项目运行验证。

![清爽蓝白后台、登录与组件动效：原尺寸独立参考](../assets/details/enterprise-workbenches/clean-admin-overview.webp)
<!-- /ui-atlas:details -->
