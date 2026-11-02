# UI Atlas

包含 GIF 动图、六帧对照图和 AI 技能的可视化 UI 参考库。把“加一个发光效果”“保存后给个提示”等需求，转换成明确的组件名称、触发方式和状态变化，帮助 AI 在现有项目中选型、实现和核对界面。

参考库包含 **105 个组件／效果条目 + 10 个选型／纠错片段**，每个条目都有中文说明、英文名称、指令例句、GIF 和六帧图。

仓库与技能统一使用名称 **`ui-atlas`**，在支持技能的 AI 工具中可通过 `$ui-atlas` 调用。技能执行流程见 [SKILL.md](SKILL.md)，浏览资料可直接从 [参考总索引](references/index.md) 开始。

## 能用它做什么

- **按行为选组件**：区分 Tooltip、Popover、Toast、Modal，以及 Switch、Checkbox、Radio 等容易混用的组件。
- **按名称指定效果**：区分沿边框移动的 Border Beam、扫过表面的 Shimmer、跟随指针的 Spotlight。
- **给 AI 提供视觉证据**：先查看六帧图，涉及连续运动时再查看 GIF，然后按触发、方向、层次、节奏和状态实现。
- **核对实际交互**：检查初始、触发、进行、完成与恢复状态，异步操作同时检查失败与回滚。

这里提供视觉与交互参考。具体实现沿用目标项目的技术栈、组件库和设计系统。

## 参考分类

| 分类 | 组件／效果 | 选型／纠错 | 示例 |
|---|---:|---:|---|
| [弹窗与浮层](references/overlays.md) | 10 | 5 | Modal、Drawer、Toast、Tooltip、Popover |
| [加载与错误页](references/loading-errors.md) | 13 | 0 | 骨架屏、模糊渐显、乐观更新、进度条、空状态 |
| [背景特效](references/backgrounds.md) | 13 | 0 | 极光、网格渐变、粒子波浪、点阵地球、字符雨 |
| [卡片与表格](references/cards-tables.md) | 14 | 0 | 轮播、瀑布流、翻转卡、统计卡、固定表头 |
| [表单](references/forms.md) | 14 | 0 | 浮动标签、验证码、上传、日期、密码强度、校验 |
| [常见动效](references/motion.md) | 16 | 1 | 边缘流光、聚光、视差、磁吸、打字机、错峰 |
| [按钮、状态与选项](references/buttons-controls.md) | 25 | 4 | 主次按钮、Hover、Pressed、Focus、Switch、Checkbox |
| **合计** | **105** | **10** | **115 组 GIF + 六帧图** |

## 安装使用

### 方式一：跟你的 agent 说（推荐）

```text
帮我安装 ui-atlas 这个 skill（github.com/dqzboy/ui-atlas），装好后跑一遍参考检索示例
```

### 方式二：一行命令

```bash
npx skills add dqzboy/ui-atlas
```

### 给 AI 的指令示例

```text
使用 $ui-atlas，为推荐套餐卡片添加 motion/border-beam。
先查看对应六帧图和 GIF，只让光点沿卡片边框循环移动。
```

```text
使用 $ui-atlas 检查保存成功的反馈方式，
参考 overlays/success-toast-correction，说明选型依据后修改并验证交互。
```

```text
参考 loading-errors/optimistic-ui，实现点赞后立即反馈，
请求失败时回滚，并提供可见的失败提示。
```

建议说明：**目标组件、触发条件、状态变化、作用范围、关键视觉特征**。例如“只在推荐套餐卡片边框循环移动光点”，比“给页面加点动效”更容易得到准确实现。
