# 参考媒体取舍

媒体判断按条目进行，不按分类名称整批保留或删除。先用静态图片选型，只有需要观察连续变化或重要短暂状态时再获取 GIF。

同一效果只留一张代表图，连续变化由 GIF 展示；不同页面、布局或必要状态可保留多图，不固定导出六张独立帧。已有独立稿时，移除重复包含相同页面的组合图。

小字、边框、圆角、阴影和材质需查看独立原尺寸图片；不要放大总览的小格判断。可选 PNG 细节与大尺寸 GIF 的读取方式、来源和实际分辨率限制见 [查看清晰参考](media-quality.md)。

## 判断依据

- 保留 GIF：运动路径、速度变化、回弹、错峰、拖拽、滚动关联、光线移动，或稀疏状态图漏掉的重要反馈。保留对应 JPG 作为轻量预览。
- 仅保留静态图片：布局、形状、颜色、层级、纹理、普通控件的状态和语义对照；旁白讲解、镜头缩放与标注不构成需要复刻的产品动效。
- 静态状态图可指导实现，但不能证明真实点击、网络请求、防连点、键盘焦点管理或数据正确性。
- 原有 GIF 为 10 fps，配方 GIF 为 10–15 fps，只能辅助判断观感和先后，不用于测定精确毫秒、弹簧参数或缓动曲线。演示停顿、剪辑与循环重置不成为产品要求。

## 本次检查

逐项核对原有 157 个 GIF 条目的说明及六帧图片，并解析全部 GIF 的帧数与时长；对 27 个容易误判的条目额外检查更密的时间序列，其中 Pressed 检查全部 41 帧。另有 58 组静态图集保留原尺寸 JPG 与 PNG。10 份实现配方的新增演示媒体见下节。

结果：**78 条保留 GIF＋图片，79 条移除 GIF、仅保留静态图片**。58 组静态图集不变，原媒体部分为 78 条动态参考和 137 条纯图片参考，另有 10 份实现配方。

原有远程媒体清单包含 334 张 JPG（95.96 MiB）与 78 个 GIF（199.74 MiB）；这一部分的离线下载为 295.70 MiB，较去重后全部保留 GIF 减少 178.38 MiB。原有远程 GIF 不随默认安装下载；普通预览只获取 JPG。

特别注意：Pressed 的下压仅在 GIF 尾帧短暂出现，现有六帧图漏掉了它；这个 GIF 也不能证明松开恢复。乐观更新的短暂失败回滚需看 GIF。普通 Modal 主要是静态讲解，Toast 现有素材未完整演示自动消失；两者保留图片和规则，实际开闭及计时仍需项目验证。移动服务首页的镜头转场不属于页面内交互，已改为图片参考。

## 配方效果参考

10 份配方各附一张高清效果 JPG，随技能提供。005、006、008、009、010 另附精选 GIF；001、002、003、004、007 使用高清图片。按名称进入 [配方索引](craft-recipes.md) 查看具体画面和媒体取舍。

配方 GIF 以 10–15 fps 导出，选取与目标行为相关的未遮挡原始片段；帧率记录在 `gif_fps` 中。它们不完整覆盖原演示中的全部行为，具体范围在各配方中说明。媒体清单以 `bundled: true` 标记这些本地文件；不会为尚未发布的新文件生成不可用的远程地址。

## 分类结果

| 分类 | 保留 GIF＋图片 | 原 GIF 改为仅图片 | 原静态图集 | 实现配方 |
|---|---:|---:|---:|---:|
| 弹窗与浮层 | 2 | 10 | 0 | 2 |
| 加载与错误页 | 7 | 6 | 0 | 0 |
| 背景特效 | 10 | 2 | 0 | 1 |
| 卡片与表格 | 3 | 11 | 0 | 1 |
| 表单 | 2 | 12 | 0 | 0 |
| 常见动效 | 16 | 1 | 0 | 0 |
| 按钮、状态与选项 | 3 | 26 | 0 | 1 |
| 移动端滚动 | 6 | 0 | 0 | 0 |
| Web 微交互 | 10 | 0 | 0 | 0 |
| 移动端交互 | 9 | 0 | 0 | 1 |
| 移动端页面布局 | 2 | 4 | 0 | 0 |
| Dashboard 与后台导航 | 1 | 5 | 0 | 0 |
| 玻璃材质与背景 | 0 | 0 | 0 | 1 |
| 界面排版与细节 | 1 | 1 | 0 | 2 |
| Dashboard 布局与联动 | 6 | 0 | 0 | 0 |
| 企业工作台与业务后台 | 0 | 0 | 27 | 0 |
| 数据可视化与数字孪生 | 0 | 0 | 24 | 0 |
| 移动端工作台与服务门户 | 0 | 1 | 7 | 0 |
| 文档与帮助中心布局 | 0 | 0 | 0 | 1 |

## 原 GIF 逐条处理

下表只列原有 GIF 的 157 条。理由同时写入机器索引 `media_reason`，检索时可直接查看；静态图集没有 GIF 可删。

### 弹窗与浮层

| 条目 | 处理 | 理由 |
|---|---|---|
| [弹窗](overlays.md#modal) · `overlays/modal` | 仅图片 | 重点是中央面板、遮罩和关闭入口；现有 GIF 主要停留讲解，没有值得单独保留的开闭运动。 |
| [确认弹窗](overlays.md#alert-dialog) · `overlays/alert-dialog` | 仅图片 | 重点是确认语义、按钮与遮罩规则，图片加文字足够；行为仍需项目验证。 |
| [抽屉](overlays.md#drawer) · `overlays/drawer` | GIF＋图片 | 需看面板从侧边滑入的方向与遮罩配合，开闭截图不能表达滑入过程。 |
| [底部弹层](overlays.md#bottom-sheet) · `overlays/bottom-sheet` | GIF＋图片 | 需看底部面板向上滑出的过程及其与遮罩的关系。 |
| [轻提示](overlays.md#toast) · `overlays/toast` | 仅图片 | 位置、文案和撤销样式由图片表达；现有 GIF 未完整演示自动消失，不作为计时证据。 |
| [通知](overlays.md#notification) · `overlays/notification` | 仅图片 | 标题、正文、关闭入口和位置是重点，普通出现过程没有独立参考价值。 |
| [轻提示与通知选型](overlays.md#toast-vs-notification) · `overlays/toast-vs-notification` | 仅图片 | 属于消息语义与样式对比，图片和选型说明足够。 |
| [保存成功提示纠正](overlays.md#success-toast-correction) · `overlays/success-toast-correction` | 仅图片 | 属于弹窗改轻提示的前后方案对比，无需保留讲解过程。 |
| [气泡提示](overlays.md#tooltip) · `overlays/tooltip` | 仅图片 | 锚点位置与简短解释由图片表达，悬停与离开规则由文字描述。 |
| [气泡卡片](overlays.md#popover) · `overlays/popover` | 仅图片 | 重点是锚定位置、内容与操作构成，图片加触发规则足够。 |
| [气泡确认框](overlays.md#popconfirm) · `overlays/popconfirm` | 仅图片 | 重点是就地确认的位置与按钮，图片加确认规则足够。 |
| [下拉菜单](overlays.md#dropdown-menu) · `overlays/dropdown-menu` | 仅图片 | 重点是操作列表及触发入口，普通展开无需单独保留 GIF。 |

### 加载与错误页

| 条目 | 处理 | 理由 |
|---|---|---|
| [骨架屏](loading-errors.md#skeleton) · `loading-errors/skeleton` | GIF＋图片 | 需看扫光循环和骨架被真实内容原位替换的过程。 |
| [模糊渐显](loading-errors.md#blur-up) · `loading-errors/blur-up` | GIF＋图片 | 模糊到清晰的连续变化是目标，静态前后对比会丢失过渡观感。 |
| [乐观更新](loading-errors.md#optimistic-ui) · `loading-errors/optimistic-ui` | GIF＋图片 | 需看立即反馈、请求结果与失败回滚的先后；现有六帧未完整覆盖短暂失败提示。 |
| [下拉刷新](loading-errors.md#pull-to-refresh) · `loading-errors/pull-to-refresh` | GIF＋图片 | 需看下拉、松手、刷新指示和复位的连续关系。 |
| [进度条](loading-errors.md#progress-bar) · `loading-errors/progress-bar` | 仅图片 | 重点是比例、已完成量和时间信息的呈现，多个进度状态加文字足够。 |
| [按钮加载状态](loading-errors.md#loading-button) · `loading-errors/loading-button` | GIF＋图片 | 需看提交后转圈到完成的反馈顺序；防重复提交仍须操作实际项目验证。 |
| [空状态](loading-errors.md#empty-state) · `loading-errors/empty-state` | 仅图片 | 插图、原因与下一步入口属于静态结构。 |
| [404 页面](loading-errors.md#not-found) · `loading-errors/not-found` | 仅图片 | 错误说明、回首页和搜索入口属于页面布局参考。 |
| [错误页](loading-errors.md#error-page) · `loading-errors/error-page` | 仅图片 | 原因文案与重试入口属于静态内容结构。 |
| [断网提示](loading-errors.md#offline) · `loading-errors/offline` | GIF＋图片 | 需看断网横幅进入、恢复连接换色和最终收起的过程。 |
| [没有权限](loading-errors.md#no-permission) · `loading-errors/no-permission` | 仅图片 | 无权限说明与申请入口属于静态内容结构。 |
| [结果页](loading-errors.md#result) · `loading-errors/result` | 仅图片 | 成功、失败与下一步的对照图足够，不保留装饰性庆祝过程。 |
| [加载动画](loading-errors.md#spinner) · `loading-errors/spinner` | GIF＋图片 | 旋转、跳点与条形起伏依赖循环和节奏，单图不能表达。 |

### 背景特效

| 条目 | 处理 | 理由 |
|---|---|---|
| [极光](backgrounds.md#aurora) · `backgrounds/aurora` | GIF＋图片 | 光团漂移与融合是效果主体，需保留连续变化。 |
| [流动渐变](backgrounds.md#mesh-gradient) · `backgrounds/mesh-gradient` | GIF＋图片 | 色块缓慢流动与混合是效果主体，区别于静态渐变。 |
| [粒子波浪](backgrounds.md#particle-wave) · `backgrounds/particle-wave` | GIF＋图片 | 需看粒子网面的起伏及指针附近的避让过程。 |
| [点阵地球](backgrounds.md#dotted-globe) · `backgrounds/dotted-globe` | GIF＋图片 | 需看地球旋转与城市连线变化，图片只显示某一角度。 |
| [流体](backgrounds.md#fluid) · `backgrounds/fluid` | GIF＋图片 | 需看指针搅动后烟雾生成、扩散与消散的过程。 |
| [光束](backgrounds.md#beams) · `backgrounds/beams` | GIF＋图片 | 光束扫动的方向、轨迹与循环是参考重点。 |
| [字符雨](backgrounds.md#matrix-rain) · `backgrounds/matrix-rain` | GIF＋图片 | 字符按竖列下落的方向与节奏依赖连续画面。 |
| [点阵背景](backgrounds.md#dot-grid) · `backgrounds/dot-grid` | GIF＋图片 | 需看局部提亮和放大如何跟随指针移动。 |
| [透视网格](backgrounds.md#retro-grid) · `backgrounds/retro-grid` | GIF＋图片 | 需保留透视网格的流动观感；只参考网格构图时查看 JPG 即可。 |
| [星空穿梭](backgrounds.md#starfield) · `backgrounds/starfield` | GIF＋图片 | 星点迎面运动与透视速度差不能由单图表达。 |
| [噪点颗粒](backgrounds.md#grain) · `backgrounds/grain` | 仅图片 | 重点是颗粒纹理的强弱与质感，图片足够，不要求动态噪点。 |
| [渐变背景](backgrounds.md#gradient) · `backgrounds/gradient` | 仅图片 | 基础静态渐变只需颜色与构图参考，不引入持续流动。 |

### 卡片与表格

| 条目 | 处理 | 理由 |
|---|---|---|
| [轮播](cards-tables.md#carousel) · `cards-tables/carousel` | GIF＋图片 | 需看横向切换、过渡方向与连续轮播的衔接。 |
| [瀑布流](cards-tables.md#masonry) · `cards-tables/masonry` | 仅图片 | 重点是等宽不等高的紧凑排布，不把讲解中的逐张出现当作布局要求。 |
| [翻转卡片](cards-tables.md#flip-card) · `cards-tables/flip-card` | GIF＋图片 | 需看正面经过侧面转到背面的空间路径，不能只比对两面。 |
| [统计卡片](cards-tables.md#stat-card) · `cards-tables/stat-card` | 仅图片 | 数字、趋势和比较口径的层级可由图片表达，计数动效另见 count-up。 |
| [时间线](cards-tables.md#timeline) · `cards-tables/timeline` | 仅图片 | 事件、竖线与节点的结构可由图片表达，不要求依次绘制。 |
| [头像组](cards-tables.md#avatar-group) · `cards-tables/avatar-group` | 仅图片 | 重叠、间距与超出数量可由图片表达。 |
| [徽标](cards-tables.md#badge) · `cards-tables/badge` | 仅图片 | 红点、数量与上限样式可由状态图片表达。 |
| [标签](cards-tables.md#tag) · `cards-tables/tag` | 仅图片 | 状态文字、颜色与密度可由图片表达。 |
| [折叠面板](cards-tables.md#accordion) · `cards-tables/accordion` | 仅图片 | 普通折叠与展开的两种结构由状态图表达；连续高度动效另见 animated-text-expand。 |
| [固定表头](cards-tables.md#fixed-header) · `cards-tables/fixed-header` | GIF＋图片 | 需对照正文滚动与表头、首列保持固定的相对运动。 |
| [排序和筛选](cards-tables.md#sort-filter) · `cards-tables/sort-filter` | 仅图片 | 排序箭头、条件与结果列表可由状态图表达，数据正确性仍需项目验证。 |
| [行内操作](cards-tables.md#row-actions) · `cards-tables/row-actions` | 仅图片 | 默认与显露操作的状态图足够，触摸和键盘入口依照文字规则实现。 |
| [斑马纹](cards-tables.md#zebra-stripes) · `cards-tables/zebra-stripes` | 仅图片 | 交替行底色和数字对齐是静态阅读细节。 |
| [卡片和列表](cards-tables.md#card-list) · `cards-tables/card-list` | 仅图片 | 卡片与列表的结构对照即可，不要求附加动效。 |

### 表单

| 条目 | 处理 | 理由 |
|---|---|---|
| [浮动标签](forms.md#floating-label) · `forms/floating-label` | GIF＋图片 | 需看聚焦后标签缩小上移并持续保留的过渡。 |
| [验证码输入框](forms.md#otp-input) · `forms/otp-input` | GIF＋图片 | 需看输入自动前进、删除退格和整串填入的焦点顺序。 |
| [拖拽上传](forms.md#dropzone) · `forms/dropzone` | 仅图片 | 区域、限制、进度、成功与失败状态均可由图片配合文字表达。 |
| [日期选择器](forms.md#date-picker) · `forms/date-picker` | 仅图片 | 单日、范围与直接输入的结构和状态由图片表达。 |
| [滑块](forms.md#slider) · `forms/slider` | 仅图片 | 单点、双端和精确输入的状态图足够；惯性、吸附另有动态条目。 |
| [自动补全](forms.md#autocomplete) · `forms/autocomplete` | 仅图片 | 输入、候选和选中状态图足够，不把普通输入过程单独作为动效参考。 |
| [级联选择](forms.md#cascader) · `forms/cascader` | 仅图片 | 层级结构与逐级选择规则由状态图和文字表达。 |
| [标签输入](forms.md#tag-input) · `forms/tag-input` | 仅图片 | 输入、成标签与移除的状态图足够，无独立运动要求。 |
| [密码强度](forms.md#password-strength) · `forms/password-strength` | 仅图片 | 强度分级、说明和明文开关由状态图片表达。 |
| [下拉选择](forms.md#select) · `forms/select` | 仅图片 | 选项展开和选中结果由图片表达，重点是控件选型。 |
| [校验报错](forms.md#validation) · `forms/validation` | 仅图片 | 正常与报错状态由图片表达，失焦时机和校验结果仍需项目验证。 |
| [帮助文字](forms.md#helper-text) · `forms/helper-text` | 仅图片 | 持续可见的帮助文字是静态排版参考。 |
| [必填星号](forms.md#required) · `forms/required` | 仅图片 | 必填与选填标记是静态信息表达。 |
| [输入框和提交按钮](forms.md#input-submit) · `forms/input-submit` | 仅图片 | 基础输入框和提交按钮的结构即可，不要求额外效果。 |

### 常见动效

| 条目 | 处理 | 理由 |
|---|---|---|
| [边缘流光](motion.md#border-beam) · `motion/border-beam` | GIF＋图片 | 需确认光沿边框绕行而非扫过表面，路径与循环是主体。 |
| [聚光](motion.md#spotlight) · `motion/spotlight` | GIF＋图片 | 需看局部光斑如何跟随指针以及表面、边框的同步变化。 |
| [3D 倾斜](motion.md#tilt) · `motion/tilt` | GIF＋图片 | 需看倾斜方向随指针改变以及离开后的复位。 |
| [滚动叙事](motion.md#scroll-storytelling) · `motion/scroll-storytelling` | GIF＋图片 | 需看固定叙事区内文字与图片随滚动进度切换的关系。 |
| [乱码解码](motion.md#scramble-text) · `motion/scramble-text` | GIF＋图片 | 随机字符逐步稳定的先后与节奏是主体。 |
| [视差滚动](motion.md#parallax) · `motion/parallax` | GIF＋图片 | 需看前后层在同一滚动中的速度差。 |
| [磁吸](motion.md#magnetic) · `motion/magnetic` | GIF＋图片 | 需看靠近时偏移和离开后复位的连续响应。 |
| [打字机](motion.md#typewriter) · `motion/typewriter` | GIF＋图片 | 需看文字逐字出现和光标跟随的先后。 |
| [跑马灯](motion.md#marquee) · `motion/marquee` | GIF＋图片 | 需看匀速移动、首尾衔接和暂停；单图无法判断无缝循环。 |
| [流光](motion.md#shimmer) · `motion/shimmer` | GIF＋图片 | 需看亮带扫过表面的方向与循环，区别于边框绕行。 |
| [数字滚动](motion.md#count-up) · `motion/count-up` | GIF＋图片 | 需看数字递增到目标值的过程与稳定终态。 |
| [滚动出现](motion.md#scroll-reveal) · `motion/scroll-reveal` | GIF＋图片 | 需看内容与视口边界的关系及入屏时的淡入位移。 |
| [弹性](motion.md#spring) · `motion/spring` | GIF＋图片 | 越过终点再回弹的过程是主体，终态截图无法表达。 |
| [错峰](motion.md#stagger) · `motion/stagger` | GIF＋图片 | 需看多个元素先后入场的相对节奏。 |
| [悬停上浮](motion.md#hover-lift) · `motion/hover-lift` | GIF＋图片 | 需看上浮、阴影变化和离开复位的配合。 |
| [缓动](motion.md#easing) · `motion/easing` | GIF＋图片 | 需比较同一路径的速度变化；GIF 仅作观感参考，不能反推出精确曲线。 |
| [动效时长、性能与减弱动态](motion.md#motion-rules) · `motion/motion-rules` | 仅图片 | 这是时长、性能与减弱动态的文字规则，拼图讲解无须保留 GIF。 |

### 按钮、状态与选项

| 条目 | 处理 | 理由 |
|---|---|---|
| [按钮层级总览](buttons-controls.md#button-hierarchy) · `buttons-controls/button-hierarchy` | 仅图片 | 主次视觉权重与层级对照由图片表达。 |
| [主按钮](buttons-controls.md#primary-button) · `buttons-controls/primary-button` | 仅图片 | 重点是主操作的视觉权重与位置，图片足够。 |
| [次按钮](buttons-controls.md#secondary-button) · `buttons-controls/secondary-button` | 仅图片 | 重点是次操作的视觉权重，图片足够。 |
| [线框按钮](buttons-controls.md#outline-button) · `buttons-controls/outline-button` | 仅图片 | 边框与无填充形态属于静态样式。 |
| [文字按钮](buttons-controls.md#text-button) · `buttons-controls/text-button` | 仅图片 | 文字入口的视觉层级属于静态样式。 |
| [危险按钮](buttons-controls.md#danger-button) · `buttons-controls/danger-button` | 仅图片 | 危险色与动作文字属于静态语义表达。 |
| [幽灵按钮](buttons-controls.md#ghost-button) · `buttons-controls/ghost-button` | 仅图片 | 默认与悬停外观对照足够，没有必须观察的独特轨迹。 |
| [图标按钮](buttons-controls.md#icon-button) · `buttons-controls/icon-button` | 仅图片 | 图标含义、尺寸和文字辅助属于静态可辨识性参考。 |
| [胶囊按钮](buttons-controls.md#pill-button) · `buttons-controls/pill-button` | 仅图片 | 胶囊是形状，图片足够，不要求额外运动。 |
| [按钮组](buttons-controls.md#button-group) · `buttons-controls/button-group` | 仅图片 | 分组排布与独立选中态由图片表达。 |
| [分割按钮](buttons-controls.md#split-button) · `buttons-controls/split-button` | 仅图片 | 主动作和菜单入口的分工由状态图表达。 |
| [悬浮按钮](buttons-controls.md#fab) · `buttons-controls/fab` | 仅图片 | 固定位置、尺寸与安全区由图片和文字表达，运行时仍需滚动核对。 |
| [按钮主次纠正](buttons-controls.md#hierarchy-correction) · `buttons-controls/hierarchy-correction` | 仅图片 | 提交、取消和删除的前后层级对照由图片表达。 |
| [悬停](buttons-controls.md#hover) · `buttons-controls/hover` | 仅图片 | 默认与提亮后的状态图足够；若需要上浮过程，选 hover-lift。 |
| [按下](buttons-controls.md#pressed) · `buttons-controls/pressed` | GIF＋图片 | 下压仅在 GIF 尾帧短暂出现，现有六帧图漏掉；保留 GIF，松开恢复仍需在项目中验证。 |
| [焦点](buttons-controls.md#focus) · `buttons-controls/focus` | 仅图片 | 焦点环外观由图片表达，Tab 顺序需在实际项目验证。 |
| [加载中](buttons-controls.md#loading) · `buttons-controls/loading` | GIF＋图片 | 旋转指示持续运动，需看加载期间的动态反馈。 |
| [成功](buttons-controls.md#success) · `buttons-controls/success` | 仅图片 | 加载与成功对勾两种状态足够，没有独立的变形动画要求。 |
| [禁用](buttons-controls.md#disabled) · `buttons-controls/disabled` | 仅图片 | 禁用外观及原因说明由图片和文字表达。 |
| [按钮反馈补全](buttons-controls.md#state-correction) · `buttons-controls/state-correction` | 仅图片 | 补全反馈的规则与前后对照由图片表达，按压和旋转分别路由至动态条目。 |
| [开关](buttons-controls.md#switch) · `buttons-controls/switch` | 仅图片 | 核心是即时应用的开闭语义，状态图足够；特殊涟漪另见 switch-group-ripple。 |
| [复选框](buttons-controls.md#checkbox) · `buttons-controls/checkbox` | 仅图片 | 多选与统一保存的语义由状态图和文字表达。 |
| [半选](buttons-controls.md#indeterminate) · `buttons-controls/indeterminate` | 仅图片 | 全选、半选和全不选可由状态图片表达。 |
| [单选框](buttons-controls.md#radio) · `buttons-controls/radio` | 仅图片 | 互斥选择关系可由状态图和文字表达。 |
| [分段控制器](buttons-controls.md#segmented-control) · `buttons-controls/segmented-control` | GIF＋图片 | 需看选中底块滑向另一项，而非只更换选中颜色。 |
| [切换按钮](buttons-controls.md#toggle-button) · `buttons-controls/toggle-button` | 仅图片 | 选中和取消的外观对照足够，无特殊运动要求。 |
| [可选标签](buttons-controls.md#chip) · `buttons-controls/chip` | 仅图片 | 选中与未选中的筛选样式可由图片表达。 |
| [计数器](buttons-controls.md#stepper) · `buttons-controls/stepper` | 仅图片 | 加减入口、当前值和边界规则可由图片加文字表达。 |
| [开关和选项选型](buttons-controls.md#control-selection) · `buttons-controls/control-selection` | 仅图片 | 属于开关、多选和单选的语义选型，图片和规则足够。 |

### 移动端滚动

| 条目 | 处理 | 理由 |
|---|---|---|
| [视差头图与下拉拉伸](mobile-scroll.md#elastic-parallax-hero) · `mobile-scroll/elastic-parallax-hero` | GIF＋图片 | 需看头图与正文的速度差、下拉放大和松手回弹。 |
| [吸顶分类与滚动联动](mobile-scroll.md#sticky-category-tabs) · `mobile-scroll/sticky-category-tabs` | GIF＋图片 | 需看滚动到阈值时吸顶及分类与正文的同步变化。 |
| [封面收进导航栏](mobile-scroll.md#collapsing-cover-navbar) · `mobile-scroll/collapsing-cover-navbar` | GIF＋图片 | 需看封面收缩、头像移动与导航背景变化如何随进度协同。 |
| [图文分层滚动渐显](mobile-scroll.md#editorial-scroll-reveal) · `mobile-scroll/editorial-scroll-reveal` | GIF＋图片 | 图文错时入场和图片逐渐清晰依赖连续过程。 |
| [下拉刷新场景反馈](mobile-scroll.md#pull-to-refresh-scene) · `mobile-scroll/pull-to-refresh-scene` | GIF＋图片 | 场景随下拉距离变化，达到阈值后松手刷新，需保留手势过程。 |
| [进入视口的数据生长](mobile-scroll.md#viewport-chart-growth) · `mobile-scroll/viewport-chart-growth` | GIF＋图片 | 需看入屏触发柱高增长与数值同步变化。 |

### Web 微交互

| 条目 | 处理 | 理由 |
|---|---|---|
| [钉住主图的产品叙事](web-interactions.md#sticky-product-story) · `web-interactions/sticky-product-story` | GIF＋图片 | 需看固定主图、滚动讲解和部位强调之间的同步关系。 |
| [情境光标](web-interactions.md#contextual-cursor) · `web-interactions/contextual-cursor` | GIF＋图片 | 需看指针进入、形态变化、移动跟随与离开恢复。 |
| [磁吸主操作按钮](web-interactions.md#magnetic-cta) · `web-interactions/magnetic-cta` | GIF＋图片 | 需看靠近偏移、离开弹性复位及指针与按钮的相对运动。 |
| [图标按钮展开标签](web-interactions.md#expanding-icon-label) · `web-interactions/expanding-icon-label` | GIF＋图片 | 需看图标按钮宽度展开、文字出现与收回的协同。 |
| [导航底色跟随](web-interactions.md#sliding-nav-highlight) · `web-interactions/sliding-nav-highlight` | GIF＋图片 | 需看底色平滑移动并适配文字宽度的过程。 |
| [角落扩散填色](web-interactions.md#corner-fill-hover) · `web-interactions/corner-fill-hover` | GIF＋图片 | 需看主题色从角落扩散及图标、文字同步换色的过程。 |
| [分档吸附拖动条](web-interactions.md#snapping-level-slider) · `web-interactions/snapping-level-slider` | GIF＋图片 | 需看跨档反馈和释放后吸附刻度的行为。 |
| [柱状图跟手读数](web-interactions.md#scrubbing-bar-chart) · `web-interactions/scrubbing-bar-chart` | GIF＋图片 | 需看指针、读数、标记与明暗范围的实时跟随。 |
| [列表悬停预览图](web-interactions.md#hover-image-preview) · `web-interactions/hover-image-preview` | GIF＋图片 | 需看指针切换条目时图片预览的位置、显隐与跟随。 |
| [圆形扩散换肤](web-interactions.md#circular-theme-reveal) · `web-interactions/circular-theme-reveal` | GIF＋图片 | 需看圆形遮罩从触发位置扩散，静态主题对比不足以表达。 |

### 移动端交互

| 条目 | 处理 | 理由 |
|---|---|---|
| [触点扩散主题切换](mobile-interactions.md#touch-origin-theme) · `mobile-interactions/touch-origin-theme` | GIF＋图片 | 需看主题从实际触点扩散且文字布局不被拉伸的过程。 |
| [批量勾选的顺序反馈](mobile-interactions.md#staggered-batch-check) · `mobile-interactions/staggered-batch-check` | GIF＋图片 | 依次勾选的节奏与局部弹性反馈是主体。 |
| [滑杆惯性与回吸](mobile-interactions.md#inertial-slider-snap) · `mobile-interactions/inertial-slider-snap` | GIF＋图片 | 松手后惯性滑行再吸附是主体，终态截图不能表达。 |
| [文本展开与箭头同步](mobile-interactions.md#animated-text-expand) · `mobile-interactions/animated-text-expand` | GIF＋图片 | 需看容器高度连续变化与箭头旋转的同步关系。 |
| [步骤进度的轻微回弹](mobile-interactions.md#step-progress-settle) · `mobile-interactions/step-progress-settle` | GIF＋图片 | 需看进度线推进、轻微越过与归位的过程。 |
| [开关组涟漪反馈](mobile-interactions.md#switch-group-ripple) · `mobile-interactions/switch-group-ripple` | GIF＋图片 | 需看相邻项反馈的传播顺序，并在项目中确认其值未被改变。 |
| [卡片沿轨迹离场](mobile-interactions.md#card-delete-trajectory) · `mobile-interactions/card-delete-trajectory` | GIF＋图片 | 删除后的曲线路径、缩放、旋转与淡出是主体。 |
| [滚动吸顶压缩卡片栈](mobile-interactions.md#sticky-compressing-stack) · `mobile-interactions/sticky-compressing-stack` | GIF＋图片 | 需看卡片吸顶、缩小后退和后续卡片补位的连续层次。 |
| [选中标签放大并让位](mobile-interactions.md#reflowing-choice-tabs) · `mobile-interactions/reflowing-choice-tabs` | GIF＋图片 | 需看选中放大时其余标签如何让位和重新排布。 |

### 移动端页面布局

| 条目 | 处理 | 理由 |
|---|---|---|
| [宽体标题与大图列表](mobile-layouts.md#wide-title-image-list) · `mobile-layouts/wide-title-image-list` | 仅图片 | 重点是标题、筛选、宽图和参数的静态布局，讲解遮罩无需保留。 |
| [大图头块叠信息](mobile-layouts.md#hero-information-overlay) · `mobile-layouts/hero-information-overlay` | 仅图片 | 重点是大图上的信息叠放与下方信息区布局。 |
| [黑白分层主次布局](mobile-layouts.md#monochrome-priority) · `mobile-layouts/monochrome-priority` | 仅图片 | 重点是黑白卡片的主次权重，图片足够。 |
| [大色块与小格网格](mobile-layouts.md#color-block-bento) · `mobile-layouts/color-block-bento` | 仅图片 | 重点是大小色块和数据层级，讲解中的强调不是产品动效。 |
| [海报大字与半圆转盘](mobile-layouts.md#poster-semicircle-dial) · `mobile-layouts/poster-semicircle-dial` | GIF＋图片 | 布局示例中包含真实转盘选择，需看转动与固定指针的关系。 |
| [叠放卡片翻阅布局](mobile-layouts.md#swipe-deck-layout) · `mobile-layouts/swipe-deck-layout` | GIF＋图片 | 布局示例中包含前卡拖离、后卡补位与页码切换的连续行为。 |

### Dashboard 与后台导航

| 条目 | 处理 | 理由 |
|---|---|---|
| [图文侧栏与内容同步](dashboard-navigation.md#icon-text-sidebar) · `dashboard-navigation/icon-text-sidebar` | 仅图片 | 图标、文字、分区与选中态由图片表达，普通路由切换无需 GIF。 |
| [内容分组导航](dashboard-navigation.md#grouped-content-sidebar) · `dashboard-navigation/grouped-content-sidebar` | 仅图片 | 分组结构、侧栏层级与选中样式由状态图表达。 |
| [顶部胶囊菜单](dashboard-navigation.md#top-pill-navigation) · `dashboard-navigation/top-pill-navigation` | 仅图片 | 顶部容器、入口密度与选中样式由图片表达。 |
| [极简图标侧栏](dashboard-navigation.md#compact-icon-rail) · `dashboard-navigation/compact-icon-rail` | 仅图片 | 窄轨尺寸、图标分区及底部账户区属于静态布局。 |
| [品牌色高亮侧栏](dashboard-navigation.md#brand-accent-sidebar) · `dashboard-navigation/brand-accent-sidebar` | 仅图片 | 品牌色、当前入口和上下分区属于静态视觉层级。 |
| [分组标签与数据联动](dashboard-navigation.md#context-data-tabs) · `dashboard-navigation/context-data-tabs` | GIF＋图片 | 需看对象标签切换后多处指标、曲线和列表的联动顺序。 |

### 界面排版与细节

| 条目 | 处理 | 理由 |
|---|---|---|
| [内容分组错峰入场](interface-details.md#section-stagger) · `interface-details/section-stagger` | GIF＋图片 | 标题、主图、数字与操作分组入场的先后是主体。 |
| [柔和多层阴影](interface-details.md#layered-soft-shadow) · `interface-details/layered-soft-shadow` | 仅图片 | 近细远柔的投影层次及前后对照由图片表达。 |

### Dashboard 布局与联动

| 条目 | 处理 | 理由 |
|---|---|---|
| [多彩错列主次网格](dashboard-layouts.md#asymmetric-color-grid) · `dashboard-layouts/asymmetric-color-grid` | GIF＋图片 | 需看日期选择如何带动柱形、标签与容量读数同步变化。 |
| [工业分区与固定操作区](dashboard-layouts.md#inventory-action-workbench) · `dashboard-layouts/inventory-action-workbench` | GIF＋图片 | 需看筛选、选中商品、右侧操作卡切换和加入清单的连续关系。 |
| [中轴观测与时间轴联动](dashboard-layouts.md#central-observation-timeline) · `dashboard-layouts/central-observation-timeline` | GIF＋图片 | 需看拖动时间轴如何驱动中央视图与读数同步变化。 |
| [玻璃点阵与月份指标](dashboard-layouts.md#glass-matrix-metrics) · `dashboard-layouts/glass-matrix-metrics` | GIF＋图片 | 需看月份与指标切换如何更新点阵读数和趋势，材质本身看 JPG 即可。 |
| [暖色三栏控制台](dashboard-layouts.md#warm-three-column-console) · `dashboard-layouts/warm-three-column-console` | GIF＋图片 | 需看房间、模式、数值与单位的协调切换；三栏构图只需 JPG。 |
| [暗色增长与图表递进入场](dashboard-layouts.md#dark-growth-dashboard) · `dashboard-layouts/dark-growth-dashboard` | GIF＋图片 | 需看数字、曲线、面积与环图按顺序进入的节奏。 |

### 移动端工作台与服务门户

| 条目 | 处理 | 理由 |
|---|---|---|
| [CRM、寄件与生活服务首页](mobile-workbenches.md#sales-crm-parcel-homes) · `mobile-workbenches/sales-crm-parcel-homes` | 仅图片 | 原 GIF 展示多张静态页面与镜头转场，没有页面内交互；仅保留页面组合图片。 |
