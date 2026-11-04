# 常见动效

静态图用于查看构图与可见状态，连续运动和短暂状态需在实际项目验证。按当前项目需求实现目标组件的交互与动效。

## 目录

- [边缘流光](#border-beam)
- [聚光](#spotlight)
- [3D 倾斜](#tilt)
- [滚动叙事](#scroll-storytelling)
- [乱码解码](#scramble-text)
- [视差滚动](#parallax)
- [磁吸](#magnetic)
- [打字机](#typewriter)
- [跑马灯](#marquee)
- [流光](#shimmer)
- [数字滚动](#count-up)
- [滚动出现](#scroll-reveal)
- [弹性](#spring)
- [错峰](#stagger)
- [悬停上浮](#hover-lift)
- [缓动](#easing)
- [动效时长、性能与减弱动态](#motion-rules)

<a id="border-beam"></a>
## 边缘流光 / Border Beam

- 标识：`motion/border-beam`；类型：组件／效果。
- 效果要点：光沿卡片边框循环移动，用于突出推荐套餐或新功能；运动路径在边缘，不是扫过整个表面。
- 指令例句：只给推荐套餐卡片加沿边框环绕的 Border Beam。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/border-beam -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/border-beam-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![边缘流光：原尺寸独立参考](../assets/details/motion/border-beam-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="spotlight"></a>
## 聚光 / Spotlight

- 标识：`motion/spotlight`；类型：组件／效果。
- 效果要点：卡片上有跟随鼠标的局部光斑，同时照亮表面和边框。
- 指令例句：卡片内部添加跟随鼠标位置的 Spotlight。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/spotlight -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/spotlight-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![聚光：原尺寸独立参考](../assets/details/motion/spotlight-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="tilt"></a>
## 3D 倾斜 / Tilt

- 标识：`motion/tilt`；类型：组件／效果。
- 效果要点：卡片随鼠标位置向不同方向轻微倾斜，体现拿在手里的空间感；用于产品卡或会员卡。
- 指令例句：会员卡随鼠标微微 3D 倾斜，移开后恢复。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/tilt -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/tilt-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![3D 倾斜：原尺寸独立参考](../assets/details/motion/tilt-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="scroll-storytelling"></a>
## 滚动叙事 / Scroll Storytelling

- 标识：`motion/scroll-storytelling`；类型：组件／效果。
- 效果要点：滚动时叙事区域保持固定，内部内容按进度逐步改变；示例指令是左侧文字切换、右侧图片同步变化。
- 指令例句：这一段固定展示，随滚动切换左侧文字与右侧图片。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/scroll-storytelling -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/scroll-storytelling-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![滚动叙事：原尺寸独立参考](../assets/details/motion/scroll-storytelling-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="scramble-text"></a>
## 乱码解码 / Scramble Text

- 标识：`motion/scramble-text`；类型：组件／效果。
- 效果要点：文字先以随机字符跳动，再逐字符稳定成目标文本；适合科技感标题和数字。
- 指令例句：标题先短暂乱码扰动，再逐字符恢复为正确文字。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/scramble-text -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/scramble-text-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![乱码解码：原尺寸独立参考](../assets/details/motion/scramble-text-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="parallax"></a>
## 视差滚动 / Parallax

- 标识：`motion/parallax`；类型：组件／效果。
- 效果要点：滚动时背景比前景移动更慢，产生纵深；区别于固定区域内切换内容的滚动叙事。
- 指令例句：让背景以比前景更慢的速度移动，产生轻微视差。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/parallax -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/parallax-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![视差滚动：原尺寸独立参考](../assets/details/motion/parallax-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="magnetic"></a>
## 磁吸 / Magnetic

- 标识：`motion/magnetic`；类型：组件／效果。
- 效果要点：指针靠近按钮时，按钮向指针方向偏移一点；适用于重点 CTA。
- 指令例句：主 CTA 在指针靠近时小幅偏移产生磁吸，离开恢复。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/magnetic -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/magnetic-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![磁吸：原尺寸独立参考](../assets/details/motion/magnetic-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="typewriter"></a>
## 打字机 / Typewriter

- 标识：`motion/typewriter`；类型：组件／效果。
- 效果要点：文字逐字出现，后面有闪烁光标；用于首页标题和 AI 回复表现。
- 指令例句：标题逐字出现并跟随光标，完成后可稳定阅读。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/typewriter -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/typewriter-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![打字机：原尺寸独立参考](../assets/details/motion/typewriter-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="marquee"></a>
## 跑马灯 / Marquee

- 标识：`motion/marquee`；类型：组件／效果。
- 效果要点：内容从右向左无限循环，常用于 Logo 或评价；这类运动应匀速，悬停最好暂停。
- 指令例句：合作伙伴 Logo 用匀速无缝跑马灯，悬停时暂停。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/marquee -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/marquee-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![跑马灯：原尺寸独立参考](../assets/details/motion/marquee-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="shimmer"></a>
## 流光 / Shimmer

- 标识：`motion/shimmer`；类型：组件／效果。
- 效果要点：一道光扫过物体表面；用于骨架屏加载提示或按钮强调，区别于沿边框绕行的 Border Beam。
- 指令例句：给加载骨架屏加入表面扫光 Shimmer。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/shimmer -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/shimmer-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![流光：原尺寸独立参考](../assets/details/motion/shimmer-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="count-up"></a>
## 数字滚动 / Count Up

- 标识：`motion/count-up`；类型：组件／效果。
- 效果要点：数字从零快速递增到目标值，突出统计数字。
- 指令例句：统计数字进入视口后从零递增到真实目标值。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/count-up -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/count-up-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![数字滚动：原尺寸独立参考](../assets/details/motion/count-up-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="scroll-reveal"></a>
## 滚动出现 / Scroll Reveal

- 标识：`motion/scroll-reveal`；类型：组件／效果。
- 效果要点：内容进入视口时淡入或滑入；适合长页面阅读节奏，非整页打开时同时播放。
- 指令例句：内容进入视口时轻微淡入上移。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/scroll-reveal -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/scroll-reveal-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![滚动出现：原尺寸独立参考](../assets/details/motion/scroll-reveal-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="spring"></a>
## 弹性 / Spring

- 标识：`motion/spring`；类型：组件／效果。
- 效果要点：到终点后略微越过再回弹；用于少量趣味交互；建议弹窗从约 95% 到原尺寸，不从零缩放。
- 指令例句：弹窗从 0.95 倍到 1 倍轻微回弹，避免大幅晃动。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/spring -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/spring-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![弹性：原尺寸独立参考](../assets/details/motion/spring-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="stagger"></a>
## 错峰 / Stagger

- 标识：`motion/stagger`；类型：组件／效果。
- 效果要点：一组元素按顺序依次出现，示例为每项间隔 0.05 秒。
- 指令例句：列表项依次出现，相邻开始时间间隔 0.05 秒。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/stagger -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/stagger-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![错峰：原尺寸独立参考](../assets/details/motion/stagger-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="hover-lift"></a>
## 悬停上浮 / Hover Lift

- 标识：`motion/hover-lift`；类型：组件／效果。
- 效果要点：指针进入卡片时略微上浮并增强阴影，传达可点击性。
- 指令例句：可点击卡片悬停时轻微上浮并加深阴影。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/hover-lift -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/hover-lift-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![悬停上浮：原尺寸独立参考](../assets/details/motion/hover-lift-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="easing"></a>
## 缓动 / Easing

- 标识：`motion/easing`；类型：组件／效果。
- 效果要点：速度变化决定运动观感；建议进场使用先快后慢的 ease-out，离场比进场更快更轻，协同元素节奏一致；跑马灯另用匀速。
- 指令例句：进场采用 ease-out，离场更快更轻，相关元素保持一致节奏。
- 媒体取舍：保留静态效果图与实现说明；连续路径、触发顺序、节奏和短暂状态需在项目中实际验证。

<!-- ui-atlas:details motion/easing -->
- 原尺寸图片：[01 · 1440×1610](../assets/details/motion/easing-hd-01.webp)。
- 清晰度边界：从 2160 像素高的原片按原像素裁切，WebP 质量 95，不放大、不锐化、不涂抹；静态帧不能证明完整运动。

![缓动：原尺寸独立参考](../assets/details/motion/easing-hd-01.webp)
<!-- /ui-atlas:details -->

<a id="motion-rules"></a>
## 动效时长、性能与减弱动态 / Motion rules

- 标识：`motion/motion-rules`；类型：选型／纠错。
- 效果要点：常见节奏起点：小动作约 0.1–0.2 秒，弹窗与抽屉约 0.2–0.3 秒；尽量动画化位置、大小和透明度；尊重减弱动态效果设置。
- 指令例句：按交互尺度设置时长，优先 transform 和 opacity，开启减弱动态时关闭非必要动画。
- 媒体取舍：这是时长、性能与减弱动态的文字规则，拼图讲解静态图足够。

<!-- ui-atlas:details motion/motion-rules -->
- 原尺寸图片：[01 · 600×756](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/motion/motion-rules.png)。
- 清晰度边界：从历史素材提取原尺寸独立帧，避免总览缩图和再次 JPEG 压缩；源素材的分辨率与色彩限制仍在，图片不能证明连续运动。

![动效时长、性能与减弱动态：原尺寸独立参考](https://raw.githubusercontent.com/dqzboy/ui-atlas/4d61e1224c50685c02acae3ae67ebe9c217fa3b9/assets/details/motion/motion-rules.png)
<!-- /ui-atlas:details -->
