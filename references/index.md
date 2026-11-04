# UI 参考索引

参考库共 **225 条参考、19 个分类**：213 个组件／效果／页面条目、12 个选型／纠错片段。包含 157 张六帧 JPG（其中 78 条另保留 GIF、79 条仅保留静态图片）、58 组静态图集（119 张单图）及 10 份附效果图的实现配方（10 张高清效果 JPG、5 段精简 GIF）。各条目已附精选原尺寸图片和可用 GIF；相同效果保留一张代表图，不同页面或关键状态才保留多图。完整版本可直接查看；精简版本按需获取原有媒体。

先查名称、意图与关键词，再只读匹配条目。文字配方提供实现参数与提示词；涉及视觉结论时仍须查看对应媒体或项目实际效果。

| 分类 | 组件／效果 | 选型／纠错 | 参考文件 |
|---|---:|---:|---|
| 弹窗与浮层 | 11 | 3 | [overlays.md](overlays.md) |
| 加载与错误页 | 13 | 0 | [loading-errors.md](loading-errors.md) |
| 背景特效 | 13 | 0 | [backgrounds.md](backgrounds.md) |
| 卡片与表格 | 15 | 0 | [cards-tables.md](cards-tables.md) |
| 表单 | 14 | 0 | [forms.md](forms.md) |
| 常见动效 | 16 | 1 | [motion.md](motion.md) |
| 按钮、状态与选项 | 26 | 4 | [buttons-controls.md](buttons-controls.md) |
| 移动端滚动 | 6 | 0 | [mobile-scroll.md](mobile-scroll.md) |
| Web 微交互 | 10 | 0 | [web-interactions.md](web-interactions.md) |
| 移动端交互 | 10 | 0 | [mobile-interactions.md](mobile-interactions.md) |
| 移动端页面布局 | 6 | 0 | [mobile-layouts.md](mobile-layouts.md) |
| Dashboard 与后台导航 | 6 | 0 | [dashboard-navigation.md](dashboard-navigation.md) |
| 玻璃材质与背景 | 1 | 0 | [glass-materials.md](glass-materials.md) |
| 界面排版与细节 | 0 | 4 | [interface-details.md](interface-details.md) |
| Dashboard 布局与联动 | 6 | 0 | [dashboard-layouts.md](dashboard-layouts.md) |
| 企业工作台与业务后台 | 27 | 0 | [enterprise-workbenches.md](enterprise-workbenches.md) |
| 数据可视化与数字孪生 | 24 | 0 | [data-visualization.md](data-visualization.md) |
| 移动端工作台与服务门户 | 8 | 0 | [mobile-workbenches.md](mobile-workbenches.md) |
| 文档与帮助中心布局 | 1 | 0 | [documentation-layouts.md](documentation-layouts.md) |
| **合计** | **213** | **12** | **225 条** |

## 按名称查找

```bash
python3 scripts/find_reference.py "边缘流光"
python3 scripts/find_reference.py "拟物"
python3 scripts/find_reference.py "安全三角区"
python3 scripts/find_reference.py "Dither"
python3 scripts/find_reference.py "等宽数字"
python3 scripts/find_reference.py "Wiki"
python3 scripts/find_reference.py "液态玻璃"
python3 scripts/find_reference.py --category documentation-layouts
```

十份质感技巧统一见 [配方索引](craft-recipes.md)，完整机器索引见 [catalog.json](catalog.json)。

## 证据与媒体

- `recipe` 提供实现配方、演示抽帧 JPG 与可选精选 GIF；配方参数和项目实现仍需验证。
- `animation` 先看条目的原尺寸图片，六帧 JPG 用于状态对照，任务依赖路径、节奏、跟随或短暂状态时再用 `--media gif` 补看；`filmstrip` 仅保留静态图片。每个条目的理由见 `media_reason` 和 [媒体取舍](media-policy.md)。
- 六帧图仅表示抽样状态，不能证明速度、缓动、连续轨迹及所有短暂反馈。小字、圆角和材质需用 `--media images` 读取独立图片；可选细节库的来源与限制见 [查看清晰参考](media-quality.md)。原有 GIF 为 10 fps，随包配方 GIF 为 10–15 fps，可选大尺寸配方 GIF 为 15 fps，均不能用于测定精确时长和曲线；结果仍需在项目中验证。
- 静态图集优先查看独立原尺寸图片；小字、图表和材质判断按需取原尺寸单图，编号不代表状态或时间。
- 下载脚本返回可打开的绝对缓存路径；仓库版和完整包的对应媒体均可本地读取，精简版的原有远程媒体来自固定版本。相同远程文件只下载一次。
- 静态参考不能证明点击、响应式和数据联动；这些行为需在项目实际实现中验证。
- 组件、参数和代码均服从用户目标、现有项目技术栈、设计系统与业务语义；不自动照搬演示背景、文案与配色。
- 具体读取、实现与核对步骤见 [SKILL.md](../SKILL.md)。

```bash
python3 scripts/fetch_media.py motion/border-beam
python3 scripts/fetch_media.py motion/border-beam --media gif
python3 scripts/fetch_media.py enterprise-workbenches/recruitment-candidate-workbench --media images
```
