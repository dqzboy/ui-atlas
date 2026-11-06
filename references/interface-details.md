# 界面排版与细节

用于精修已有界面的数字、圆角、标题、入场和阴影。保留任务所需的输入边界、焦点与真实状态，避免把局部技巧推广为整站硬规则。

参考图用于核对构图与可见状态；连续动作在实际项目中验证。像素值、技术栈与缓动由当前项目决定。

结构、等高、图标库、图标底座和纹理的完整说明见 [卡片质感指南](card-craft.md)。

## 目录

- [递进圆角与连续曲率](#continuous-corners)
- [中英文排版与稳定数字](#cjk-latin-typesetting)
- [发光分割线](#glowing-divider)
- [卡片内高光](#inner-highlight)
- [卡片质感与结构选型](#card-craft)

<a id="continuous-corners"></a>
## 递进圆角与连续曲率 / Nested Radii and Continuous Corners

- 标识：`interface-details/continuous-corners`；类型：选型／纠错。
- 效果要点：等距嵌套采用内圆角 = 外圆角 − 内缩距离，再以 corner-shape: superellipse(1.25) 渐进增强，胶囊与圆保持全圆。
- 实现关注：从弹窗或卡片向内协调面板、输入、按钮与标签；示例外圆角 32、内缩 16，则内层 16。优先改现有 radius token；4px 网格与最小 4px 是本配方的风格起点，产品已有尺度优先。只在目标容器内应用 @supports 增强，普通 border-radius 始终保留。连续曲率和非等距内缩需检查视觉边距，不假定减法产生严格几何等距线。
- 验证重点：检查各层四角、边框与 clip-path 对齐；胶囊和圆不变形；目标浏览器不支持时仍有正常圆角。
- 指令例句：参考 interface-details/continuous-corners，等距嵌套采用内圆角 = 外圆角 − 内缩距离，再以 corner-shape: superellipse(1.25) 渐进增强，胶囊与圆保持全圆。
- [完整配方与效果参考](recipes/continuous-corners.md) · [效果图](../assets/recipes/continuous-corners.jpg)。
- 媒体取舍：重点是嵌套间距、曲率和圆角连接，高清示意图及状态对照足够；讲解镜头不需保留 GIF。

<a id="cjk-latin-typesetting"></a>
## 中英文排版与稳定数字 / CJK Latin Typesetting

- 标识：`interface-details/cjk-latin-typesetting`；类型：选型／纠错。
- 效果要点：标题 balance、正文 pretty、动态数字 tabular-nums、flex 文本 min-width:0；中文按 lang 处理自动间距、标点避头尾及分词断行。
- 实现关注：短标题平衡行长，正文减少末行孤词；数字与单位等不可分割组合用不换行空格。按钮不换行；flex 项 min-width:0 后再做 ellipsis，并为真实截断提供完整文本入口。中文正文两端对齐限于足够宽的文字列，窄列不强制；text-autospace 与 text-spacing-trim 渐进增强。中文标题采用分词断点后才用 keep-all；避免 line-break:anywhere 破坏标点禁则。
- 验证重点：检查长短标题、窄屏、长英文、混合数字单位、字体加载前后、价格计时器位数变化、截断文本的键盘与触摸入口；不支持的新 CSS 自然回退。
- 指令例句：参考 interface-details/cjk-latin-typesetting，标题 balance、正文 pretty、动态数字 tabular-nums、flex 文本 min-width:0；中文按 lang 处理自动间距、标点避头尾及分词断行。
- [完整配方与效果参考](recipes/cjk-latin-typesetting.md) · [效果图](../assets/recipes/cjk-latin-typesetting.jpg)。
- 媒体取舍：重点是换行、字距、标点与文本边界，清晰的中英文排版状态图足够。

<a id="glowing-divider"></a>
## 发光分割线 / Glowing Divider

- 标识：`interface-details/glowing-divider`；类型：组件／效果。
- 效果要点：分割线上中心略亮、两端渐隐，让价格与权益区自然分离。
- 实现提示词：将目标卡片内分割线改为中间微亮、两侧渐隐的细线，保持上下间距与文字层级。
- 核对要点：这是卡片内部细线局部参考；不把分割线扩大成霓虹外框，普通分区仍应可辨。
- 媒体取舍：仅保留一张无讲解文字的效果参考；该图展示局部细节。触发、时序、运动路径与减弱动态需在项目中验证。

<!-- ui-atlas:details interface-details/glowing-divider -->
- 原尺寸图片：[01 · 450×75](../assets/details/interface-details/glowing-divider-effect.webp)。
- 清晰度边界：1440×2560 视频在播放器接近原尺寸呈现后，仅裁出 UI 效果区域；WebP 质量 98，未放大、未锐化、未涂抹。原画中的材质模糊和光晕属于效果；静态图只核对可见状态，连续运动在项目中验证。

![发光分割线：原尺寸独立参考](../assets/details/interface-details/glowing-divider-effect.webp)
<!-- /ui-atlas:details -->

<a id="inner-highlight"></a>
## 卡片内高光 / Inner Highlight

- 标识：`interface-details/inner-highlight`；类型：选型／实现规则。
- 效果要点：沿上缘和内侧保留细微亮边，配合轻阴影形成卡片厚度。
- 实现提示词：给当前卡片增加克制的内高光，统一光源方向、阴影和圆角，保留文字、线性图标与按钮的清晰轮廓。
- 核对要点：高光使用独立装饰层或 inset 阴影，不给正文加滤镜；在深浅主题与窄屏分别检查。
- 媒体取舍：仅保留一张无讲解文字的效果参考；触发、时序、运动路径与减弱动态需在项目中验证。

<!-- ui-atlas:details interface-details/inner-highlight -->
- 原尺寸图片：[01 · 1250×645](../assets/details/interface-details/inner-highlight-effect.webp)。
- 清晰度边界：1440×2560 视频在播放器接近原尺寸呈现后，仅裁出 UI 效果区域；WebP 质量 98，未放大、未锐化、未涂抹。原画中的材质模糊和光晕属于效果；静态图只核对可见状态，连续运动在项目中验证。

![卡片内高光：原尺寸独立参考](../assets/details/interface-details/inner-highlight-effect.webp)
<!-- /ui-atlas:details -->

<a id="card-craft"></a>
## 卡片质感与结构选型 / Card Craft and Structure

- 标识：`interface-details/card-craft`；类型：选型／实现规则。
- 效果要点：23 项卡片技巧：按需求选择玻璃、全息、金属、边框与光效，再统一结构、等高、图标、底座、渐变、纹理与圆角。
- 实现提示词：先读取 references/card-craft.md 中 23 项选型与组合提示词，选择一种主材质和少量重点效果；保留现有内容、组件接口与操作，再核对真实项目。
- 完整指南：[23 项技巧与组合提示词](card-craft.md)。
- 媒体取舍：复用已完成的卡片布局，展示结构、线性图标、底座、同色渐变与浅纹理；其他材质和交互以指南文字为准，该图不证明它们的外观或连续行为。

<!-- ui-atlas:details interface-details/card-craft -->
- 原尺寸图片：[01 · 1250×645](../assets/details/interface-details/inner-highlight-effect.webp)。
- 清晰度边界：1440×2560 视频在播放器接近原尺寸呈现后，仅裁出 UI 效果区域；WebP 质量 98，未放大、未锐化、未涂抹。原画中的材质模糊和光晕属于效果；静态图只核对可见状态，连续运动在项目中验证。

![卡片质感与结构选型：原尺寸独立参考](../assets/details/interface-details/inner-highlight-effect.webp)
<!-- /ui-atlas:details -->
