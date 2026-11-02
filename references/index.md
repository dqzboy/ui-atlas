# 原视频 UI 参考索引

参考库包含 105 个组件／效果条目、10 个选型／纠错片段，配有 115 组 GIF 和六帧对照图。摘要是按参考画面和嵌入字幕整理的改写，非逐字转录。GIF 为原速、循环、无声格式，保留区域比例、鼠标、UI 标题与讲解字幕；素材处理说明见 [来源与制作范围](sources.md)。

先查名称与意图，再只读相关分类。每个条目均包含原视频时间、效果说明、指令例句、GIF 和 6 帧对照图。例句是整理后的建议表达，不代表视频逐字原话。

| 分类 | 组件／效果 | 选型／纠错 | 参考文件 |
|---|---:|---:|---|
| 弹窗与浮层 | 10 | 5 | [overlays.md](overlays.md) |
| 加载与错误页 | 13 | 0 | [loading-errors.md](loading-errors.md) |
| 背景特效 | 13 | 0 | [backgrounds.md](backgrounds.md) |
| 卡片与表格 | 14 | 0 | [cards-tables.md](cards-tables.md) |
| 表单 | 14 | 0 | [forms.md](forms.md) |
| 常见动效 | 16 | 1 | [motion.md](motion.md) |
| 按钮、状态与选项 | 25 | 4 | [buttons-controls.md](buttons-controls.md) |

## 按名称查找

```bash
python3 scripts/find_reference.py "边缘流光"
python3 scripts/find_reference.py "表单"
python3 scripts/find_reference.py --id motion/border-beam
```

路径相对于 skill 根目录。脚本只使用 Python 标准库，不需要原视频。完整机器索引：[catalog.json](catalog.json)。

## 证据与实现边界

- 此资料包提供可观察到的视觉／交互目标。源视频没有交付网页源码，不能据此断言具体库、着色器实现、CSS 参数或精确缓动曲线。
- GIF 保留讲解时间，有些时段鼠标没有移动，循环结尾会跳回片段起点；这不是要求产品加上对应停顿或重播跳变。
- 6 帧图按整段均匀抽样，能显示主要状态，但可能漏掉一次非常短的按下或转场。需要时用 GIF 抽帧，或按时间回看原视频。
- 视频中的“小于 5 项”“一块区域一个主按钮”“一页一种背景”等是该系列的设计经验。优先遵从用户的具体要求及现有产品语义。
- Ghost、Snackbar、Toggle Group 等名称在库间可能不同。按行为和视觉匹配；分段控制器在本例为单选，不可假定所有 Toggle Group 都只能单选。
- Shader 是一类实现技术的关键词，不代表这些背景必须使用某个特定框架。视频没有给出的强度、尺寸、时长等参数，要标明为实现选择。

来源与裁剪处理详见 [sources.md](sources.md)。
