# UI 参考索引

参考库包含 150 个组件／效果条目、19 个选型／纠错片段，配有 169 组 GIF 和六帧对照图。

先查名称与意图，再只读相关分类中的匹配条目，按任务需要查看媒体。每个条目均包含效果说明、指令例句、GIF 和六帧对照图。

| 分类 | 组件／效果 | 选型／纠错 | 参考文件 |
|---|---:|---:|---|
| 弹窗与浮层 | 10 | 5 | [overlays.md](overlays.md) |
| 加载与错误页 | 13 | 0 | [loading-errors.md](loading-errors.md) |
| 背景特效 | 13 | 0 | [backgrounds.md](backgrounds.md) |
| 卡片与表格 | 14 | 0 | [cards-tables.md](cards-tables.md) |
| 表单 | 14 | 0 | [forms.md](forms.md) |
| 常见动效 | 16 | 1 | [motion.md](motion.md) |
| 按钮、状态与选项 | 25 | 4 | [buttons-controls.md](buttons-controls.md) |
| 移动端滚动 | 6 | 0 | [mobile-scroll.md](mobile-scroll.md) |
| Web 微交互 | 10 | 0 | [web-interactions.md](web-interactions.md) |
| 移动端交互 | 10 | 0 | [mobile-interactions.md](mobile-interactions.md) |
| 移动端页面布局 | 6 | 0 | [mobile-layouts.md](mobile-layouts.md) |
| Dashboard 与后台导航 | 6 | 0 | [dashboard-navigation.md](dashboard-navigation.md) |
| 玻璃材质与背景 | 1 | 4 | [glass-materials.md](glass-materials.md) |
| 界面排版与细节 | 0 | 5 | [interface-details.md](interface-details.md) |
| Dashboard 布局与联动 | 6 | 0 | [dashboard-layouts.md](dashboard-layouts.md) |
| **合计** | **150** | **19** | **169 组 GIF + 六帧图** |

## 按名称查找

```bash
python3 scripts/find_reference.py "边缘流光"
python3 scripts/find_reference.py "表单"
python3 scripts/find_reference.py --id motion/border-beam
python3 scripts/find_reference.py "仪表盘"
python3 scripts/find_reference.py --category dashboard-layouts
python3 scripts/find_reference.py "等宽数字"
```

路径相对于 skill 根目录。脚本只使用 Python 标准库。完整机器索引：[catalog.json](catalog.json)。

## 使用要点

- 参考库提供视觉与交互目标，具体实现沿用当前项目的技术栈、组件库和设计系统。
- 媒体读取、同轮复用与结果展示遵循 [技能使用方式](../SKILL.md#使用方式) 和 [沟通与结果展示](../SKILL.md#沟通与结果展示)，只查看当前任务所需的参考。
- GIF 看连续运动，六帧图看主要状态；短暂的按压或转场可能未出现在六帧图中，需要时从 GIF 额外抽帧。
- GIF 中的演示停顿与循环跳变不属于产品动画要求。
- 组件选型优先遵从用户要求及现有产品语义，参考中的通用经验可按实际场景调整。
- Ghost、Snackbar、Toggle Group 等名称在库间可能不同。按行为和视觉匹配；分段控制器在本例为单选，不可假定所有 Toggle Group 都只能单选。
- Shader 是一类实现技术的关键词，不代表这些背景必须使用某个特定框架。参考未指定的强度、尺寸、时长等参数，要标明为实现选择。

## 相近效果的选型入口

- 通用视差、磁吸、错峰等原子效果保留在 [常见动效](motion.md)；整段产品叙事和工具栏响应见 [Web 微交互](web-interactions.md)。
- 头部和页内分类随滚动变化见 [移动端滚动](mobile-scroll.md)；卡片层叠和触控反馈见 [移动端交互](mobile-interactions.md)。
- 选择整页结构见 [移动端页面布局](mobile-layouts.md) 或 [Dashboard 布局与联动](dashboard-layouts.md)；仅修改后台菜单见 [Dashboard 与后台导航](dashboard-navigation.md)。
- 材质和文字细修分别见 [玻璃材质与背景](glass-materials.md)、[界面排版与细节](interface-details.md)。
