# 界面排版与细节

用于精修已有界面的数字、圆角、标题、入场和阴影。保留任务所需的输入边界、焦点与真实状态，避免把局部技巧推广为整站硬规则。

参考图用于核对构图与可见状态；连续动作在实际项目中验证。像素值、技术栈与缓动由当前项目决定。

## 目录

- [递进圆角与连续曲率](#continuous-corners)
- [中英文排版与稳定数字](#cjk-latin-typesetting)

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
