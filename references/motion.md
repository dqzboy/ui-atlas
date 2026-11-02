# 常见动效

来源：`16种常见动画效果.mp4`。时间为原片绝对时间，片段按原速播放。

GIF 看连续运动，六帧图看状态变化。参考视频包含讲解者的鼠标、选框和字幕；这些演示标注不属于待实现产品。

## 目录

- [边缘流光 / Border Beam](#border-beam)
- [聚光 / Spotlight](#spotlight)
- [3D 倾斜 / Tilt](#tilt)
- [滚动叙事 / Scroll Storytelling](#scroll-storytelling)
- [乱码解码 / Scramble Text](#scramble-text)
- [视差滚动 / Parallax](#parallax)
- [磁吸 / Magnetic](#magnetic)
- [打字机 / Typewriter](#typewriter)
- [跑马灯 / Marquee](#marquee)
- [流光 / Shimmer](#shimmer)
- [数字滚动 / Count Up](#count-up)
- [滚动出现 / Scroll Reveal](#scroll-reveal)
- [弹性 / Spring](#spring)
- [错峰 / Stagger](#stagger)
- [悬停上浮 / Hover Lift](#hover-lift)
- [缓动 / Easing](#easing)
- [动效时长、性能与减弱动态 / Motion rules](#motion-rules)

<a id="border-beam"></a>
## 边缘流光 / Border Beam

- 标识：`motion/border-beam`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，00:04.3–00:14.7。
- 视频要点：光沿卡片边框循环移动，用于突出推荐套餐或新功能；运动路径在边缘，不是扫过整个表面。
- 指令例句：只给推荐套餐卡片加沿边框环绕的 Border Beam。
- 参考：[GIF 动图](../assets/gifs/motion/border-beam.gif) · [六帧对照图](../assets/filmstrips/motion/border-beam.jpg)。

![边缘流光：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/border-beam.jpg)

<a id="spotlight"></a>
## 聚光 / Spotlight

- 标识：`motion/spotlight`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，00:16.3–00:22.5。
- 视频要点：卡片上有跟随鼠标的局部光斑，同时照亮表面和边框。
- 指令例句：卡片内部添加跟随鼠标位置的 Spotlight。
- 参考：[GIF 动图](../assets/gifs/motion/spotlight.gif) · [六帧对照图](../assets/filmstrips/motion/spotlight.jpg)。

![聚光：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/spotlight.jpg)

<a id="tilt"></a>
## 3D 倾斜 / Tilt

- 标识：`motion/tilt`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，00:24.1–00:31.5。
- 视频要点：卡片随鼠标位置向不同方向轻微倾斜，体现拿在手里的空间感；用于产品卡或会员卡。
- 指令例句：会员卡随鼠标微微 3D 倾斜，移开后恢复。
- 参考：[GIF 动图](../assets/gifs/motion/tilt.gif) · [六帧对照图](../assets/filmstrips/motion/tilt.jpg)。

![3D 倾斜：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/tilt.jpg)

<a id="scroll-storytelling"></a>
## 滚动叙事 / Scroll Storytelling

- 标识：`motion/scroll-storytelling`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，00:32.3–00:45.3。
- 视频要点：滚动时叙事区域保持固定，内部内容按进度逐步改变；示例指令是左侧文字切换、右侧图片同步变化。
- 指令例句：这一段固定展示，随滚动切换左侧文字与右侧图片。
- 参考：[GIF 动图](../assets/gifs/motion/scroll-storytelling.gif) · [六帧对照图](../assets/filmstrips/motion/scroll-storytelling.jpg)。

![滚动叙事：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/scroll-storytelling.jpg)

<a id="scramble-text"></a>
## 乱码解码 / Scramble Text

- 标识：`motion/scramble-text`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，00:47.1–00:52.6。
- 视频要点：文字先以随机字符跳动，再逐字符稳定成目标文本；适合科技感标题和数字。
- 指令例句：标题先短暂乱码扰动，再逐字符恢复为正确文字。
- 参考：[GIF 动图](../assets/gifs/motion/scramble-text.gif) · [六帧对照图](../assets/filmstrips/motion/scramble-text.jpg)。

![乱码解码：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/scramble-text.jpg)

<a id="parallax"></a>
## 视差滚动 / Parallax

- 标识：`motion/parallax`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，00:54.1–00:59.4。
- 视频要点：滚动时背景比前景移动更慢，产生纵深；区别于固定区域内切换内容的滚动叙事。
- 指令例句：让背景以比前景更慢的速度移动，产生轻微视差。
- 参考：[GIF 动图](../assets/gifs/motion/parallax.gif) · [六帧对照图](../assets/filmstrips/motion/parallax.jpg)。

![视差滚动：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/parallax.jpg)

<a id="magnetic"></a>
## 磁吸 / Magnetic

- 标识：`motion/magnetic`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，01:01.1–01:06.4。
- 视频要点：指针靠近按钮时，按钮向指针方向偏移一点；适用于重点 CTA。
- 指令例句：主 CTA 在指针靠近时小幅偏移产生磁吸，离开恢复。
- 参考：[GIF 动图](../assets/gifs/motion/magnetic.gif) · [六帧对照图](../assets/filmstrips/motion/magnetic.jpg)。

![磁吸：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/magnetic.jpg)

<a id="typewriter"></a>
## 打字机 / Typewriter

- 标识：`motion/typewriter`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，01:08.1–01:13.5。
- 视频要点：文字逐字出现，后面有闪烁光标；用于首页标题和 AI 回复表现。
- 指令例句：标题逐字出现并跟随光标，完成后可稳定阅读。
- 参考：[GIF 动图](../assets/gifs/motion/typewriter.gif) · [六帧对照图](../assets/filmstrips/motion/typewriter.jpg)。

![打字机：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/typewriter.jpg)

<a id="marquee"></a>
## 跑马灯 / Marquee

- 标识：`motion/marquee`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，01:15.1–01:24.4。
- 视频要点：内容从右向左无限循环，常用于 Logo 或评价；这类运动应匀速，悬停最好暂停。
- 指令例句：合作伙伴 Logo 用匀速无缝跑马灯，悬停时暂停。
- 参考：[GIF 动图](../assets/gifs/motion/marquee.gif) · [六帧对照图](../assets/filmstrips/motion/marquee.jpg)。

![跑马灯：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/marquee.jpg)

<a id="shimmer"></a>
## 流光 / Shimmer

- 标识：`motion/shimmer`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，01:26.1–01:32.4。
- 视频要点：一道光扫过物体表面；用于骨架屏加载提示或按钮强调，区别于沿边框绕行的 Border Beam。
- 指令例句：给加载骨架屏加入表面扫光 Shimmer。
- 参考：[GIF 动图](../assets/gifs/motion/shimmer.gif) · [六帧对照图](../assets/filmstrips/motion/shimmer.jpg)。

![流光：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/shimmer.jpg)

<a id="count-up"></a>
## 数字滚动 / Count Up

- 标识：`motion/count-up`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，01:33.3–01:39.7。
- 视频要点：数字从零快速递增到目标值，突出统计数字。
- 指令例句：统计数字进入视口后从零递增到真实目标值。
- 参考：[GIF 动图](../assets/gifs/motion/count-up.gif) · [六帧对照图](../assets/filmstrips/motion/count-up.jpg)。

![数字滚动：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/count-up.jpg)

<a id="scroll-reveal"></a>
## 滚动出现 / Scroll Reveal

- 标识：`motion/scroll-reveal`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，01:41.1–01:47.8。
- 视频要点：内容进入视口时淡入或滑入；适合长页面阅读节奏，非整页打开时同时播放。
- 指令例句：内容进入视口时轻微淡入上移。
- 参考：[GIF 动图](../assets/gifs/motion/scroll-reveal.gif) · [六帧对照图](../assets/filmstrips/motion/scroll-reveal.jpg)。

![滚动出现：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/scroll-reveal.jpg)

<a id="spring"></a>
## 弹性 / Spring

- 标识：`motion/spring`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，01:49.1–02:01.3。
- 视频要点：到终点后略微越过再回弹；用于少量趣味交互；视频建议弹窗从约 95% 到原尺寸，不从零缩放。
- 指令例句：弹窗从 0.95 倍到 1 倍轻微回弹，避免大幅晃动。
- 参考：[GIF 动图](../assets/gifs/motion/spring.gif) · [六帧对照图](../assets/filmstrips/motion/spring.jpg)。

![弹性：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/spring.jpg)

<a id="stagger"></a>
## 错峰 / Stagger

- 标识：`motion/stagger`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，02:02.3–02:14.1。
- 视频要点：一组元素按顺序依次出现，视频示例为每项间隔 0.05 秒。
- 指令例句：列表项依次出现，相邻开始时间间隔 0.05 秒。
- 参考：[GIF 动图](../assets/gifs/motion/stagger.gif) · [六帧对照图](../assets/filmstrips/motion/stagger.jpg)。

![错峰：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/stagger.jpg)

<a id="hover-lift"></a>
## 悬停上浮 / Hover Lift

- 标识：`motion/hover-lift`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，02:15.3–02:21.2。
- 视频要点：指针进入卡片时略微上浮并增强阴影，传达可点击性。
- 指令例句：可点击卡片悬停时轻微上浮并加深阴影。
- 参考：[GIF 动图](../assets/gifs/motion/hover-lift.gif) · [六帧对照图](../assets/filmstrips/motion/hover-lift.jpg)。

![悬停上浮：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/hover-lift.jpg)

<a id="easing"></a>
## 缓动 / Easing

- 标识：`motion/easing`；类型：组件／效果。
- 原视频：`16种常见动画效果.mp4`，02:22.3–02:42.4。
- 视频要点：速度变化决定运动观感；视频建议进场使用先快后慢的 ease-out，离场比进场更快更轻，协同元素节奏一致；跑马灯另用匀速。
- 指令例句：进场采用 ease-out，离场更快更轻，相关元素保持一致节奏。
- 参考：[GIF 动图](../assets/gifs/motion/easing.gif) · [六帧对照图](../assets/filmstrips/motion/easing.jpg)。

![缓动：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/easing.jpg)

<a id="motion-rules"></a>
## 动效时长、性能与减弱动态 / Motion rules

- 标识：`motion/motion-rules`；类型：选型／纠错讲解。
- 画面处理：已裁去顶部系列标识区，保留 UI 示例与规则字幕。
- 原视频：`16种常见动画效果.mp4`，02:44.2–02:54.7。
- 视频要点：视频总结：小动作约 0.1–0.2 秒，弹窗与抽屉约 0.2–0.3 秒；尽量动画化位置、大小和透明度；尊重减弱动态效果设置。
- 指令例句：按交互尺度设置时长，优先 transform 和 opacity，开启减弱动态时关闭非必要动画。
- 参考：[GIF 动图](../assets/gifs/motion/motion-rules.gif) · [六帧对照图](../assets/filmstrips/motion/motion-rules.jpg)。

![动效时长、性能与减弱动态：按时间从左到右、从上到下阅读](../assets/filmstrips/motion/motion-rules.jpg)
