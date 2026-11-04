# 玻璃材质与背景

按背景、主题与前景可读性调整液态玻璃；折射是需要实测的渐进增强。当前条目提供实现配方、状态对照图和精简动态演示。

## 目录

- [自适应液态玻璃材质 / Adaptive Liquid Glass](#liquid-glass)

<a id="liquid-glass"></a>
## 自适应液态玻璃材质 / Adaptive Liquid Glass

- 标识：`glass-materials/liquid-glass`；类型：组件／效果。
- 效果要点：将投影、背景模糊与提亮、边缘折射和色散、着色、边缘光与前景着色组合成共享 token，并按背景亮度与深浅主题适配。
- 实现关注：浅色起点：白色着色 6–22%、blur 2px、saturate 180%、brightness 1.06；深色：rgb(20 20 24) 16–38%、2px、160%、0.8。边缘宽度 min(44px,短边/3.5)，偏移 1.1 × rim × (1-d/rim)^2.6，色散 ±15%；中间保持平整。5×3 采样丢弃最亮暗各两点，平均亮度 0.5 阈值与 ±0.05 滞回切换前景。同排面板共享决策；采样不可读时跟随主题并提高着色密度。
- 验证重点：检查忙碌／明暗背景、文字实际对比、圆角与位移贴图边缘、主题切换、逐主题着色设置。SVG backdrop 折射必须实测，解析支持不等于绘制可用；失败用纯 CSS 玻璃，小尺寸或不稳定合成层跳过折射，减少透明或强制颜色时回退实心。
- 指令例句：参考 glass-materials/liquid-glass，将投影、背景模糊与提亮、边缘折射和色散、着色、边缘光与前景着色组合成共享 token，并按背景亮度与深浅主题适配。
- [完整配方与效果参考](recipes/liquid-glass.md) · [效果图](../assets/recipes/liquid-glass.jpg) · [交互片段](../assets/recipes/liquid-glass.gif)。
- 媒体取舍：需看背景变化与主题切换时玻璃的透射、折射和前景对比，保留播放器主体的连续片段。

<!-- ui-atlas:details glass-materials/liquid-glass -->
- 连续效果：[GIF · 1080×926](../assets/details/glass-materials/liquid-glass.gif)。
- 清晰度边界：从 2160×2880 原片重新导出，使用已确认的精选片段和裁切；GIF 仍受 256 色限制，静态细节查看随包 JPG。
<!-- /ui-atlas:details -->
