# UI 参考索引

参考库包含 105 个组件／效果条目、10 个选型／纠错片段，配有 115 组 GIF 和六帧对照图。

先查名称与意图，再只读相关分类。每个条目均包含效果说明、指令例句、GIF 和六帧对照图。

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

路径相对于 skill 根目录。脚本只使用 Python 标准库。完整机器索引：[catalog.json](catalog.json)。

## 使用要点

- 参考库提供视觉与交互目标，具体实现沿用当前项目的技术栈、组件库和设计系统。
- GIF 看连续运动，六帧图看主要状态；短暂的按压或转场可能未出现在六帧图中，需要时从 GIF 额外抽帧。
- GIF 中的演示停顿与循环跳变不属于产品动画要求。
- 组件选型优先遵从用户要求及现有产品语义，参考中的通用经验可按实际场景调整。
- Ghost、Snackbar、Toggle Group 等名称在库间可能不同。按行为和视觉匹配；分段控制器在本例为单选，不可假定所有 Toggle Group 都只能单选。
- Shader 是一类实现技术的关键词，不代表这些背景必须使用某个特定框架。参考未指定的强度、尺寸、时长等参数，要标明为实现选择。
