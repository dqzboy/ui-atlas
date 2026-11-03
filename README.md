# UI Atlas

包含 GIF 动图、六帧对照图、原尺寸静态设计图和 AI 技能的可视化 UI 参考库。把“加一个发光效果”“保存后给个提示”等需求，转换成明确的组件名称、触发方式和状态变化，帮助 AI 在现有项目中选型、实现和核对界面。

参考库包含 **209 个组件／效果／页面条目 + 19 个选型／纠错片段**，共 **228 条参考**，覆盖 **18 个分类**。动画参考提供 170 组 GIF 和六帧图；静态设计参考提供 58 组图集、119 张原尺寸单图和 58 张总览。所有条目均有中文说明、英文名称和指令例句。

仓库与技能统一使用名称 **`ui-atlas`**，在支持技能的 AI 工具中可通过 `$ui-atlas` 调用。技能执行流程见 [SKILL.md](SKILL.md)，浏览资料可直接从 [参考总索引](references/index.md) 开始。

## 能用它做什么

- **按行为选组件**：区分 Tooltip、Popover、Toast、Modal，以及 Switch、Checkbox、Radio 等容易混用的组件。
- **按名称指定效果**：区分沿边框移动的 Border Beam、扫过表面的 Shimmer、跟随指针的 Spotlight。
- **给 AI 提供视觉证据**：先筛选相关条目，涉及视觉判断时查看六帧图，连续运动再查看 GIF；同轮复用已确认的参考，按触发、方向、层次、节奏和状态实现。
- **选择页面布局与联动**：覆盖移动端滚动、整页布局、Web 微交互、Dashboard 导航与多区域数据同步。
- **按业务选整页参考**：查看物流、招聘、MES、企业门户、移动服务首页，以及工业／能源／建筑数字孪生；静态稿用于判断视觉结构，交互需在实际项目中设计和验证。
- **精修材质和排版**：查看玻璃层次、背景选型、等宽数字、同心圆角与平衡换行。
- **核对实际交互**：检查初始、触发、进行、完成与恢复状态，异步操作同时检查失败与回滚。

这里提供视觉与交互参考。具体实现沿用目标项目的技术栈、组件库和设计系统。静态总览只用于筛选；看文字、图表和材质细节时打开条目中的单图链接，有独立设计稿时优先查看独立稿。海报本身已缩小的界面，其细节仍受源图限制。

执行中按需查看参考，最终汇报以项目实际修改与验证结果为主；需要配图时优先展示项目实际效果。选型或效果对比时再展示参考图，并明确区分参考与实现。

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
| [移动端滚动](references/mobile-scroll.md) | 6 | 0 | 视差头图与下拉拉伸、吸顶分类与滚动联动、封面收进导航栏 |
| [Web 微交互](references/web-interactions.md) | 10 | 0 | 钉住主图的产品叙事、情境光标、磁吸主操作按钮 |
| [移动端交互](references/mobile-interactions.md) | 10 | 0 | 触点扩散主题切换、拖拽排序与弹性让位、批量勾选的顺序反馈 |
| [移动端页面布局](references/mobile-layouts.md) | 6 | 0 | 宽体标题与大图列表、大图头块叠信息、黑白分层主次布局 |
| [Dashboard 与后台导航](references/dashboard-navigation.md) | 6 | 0 | 图文侧栏与内容同步、内容分组导航、顶部胶囊菜单 |
| [玻璃材质与背景](references/glass-materials.md) | 1 | 4 | 磨砂玻璃的基本层次、增色与透明叠白、亮边与边缘折射 |
| [界面排版与细节](references/interface-details.md) | 0 | 5 | 等宽数字防跳动、嵌套容器同心圆角、内容分组错峰入场 |
| [Dashboard 布局与联动](references/dashboard-layouts.md) | 6 | 0 | 多彩错列主次网格、工业分区与固定操作区、中轴观测与时间轴联动 |
| [企业工作台与业务后台](references/enterprise-workbenches.md) | 27 | 0 | 物流配载、企业门户、AI 助手、招聘、MES 与项目任务 |
| [数据可视化与数字孪生](references/data-visualization.md) | 24 | 0 | 工业／能源／建筑孪生、地图、健康与安全态势 |
| [移动端工作台与服务门户](references/mobile-workbenches.md) | 8 | 0 | CRM、寄件、校园、文旅与企业服务首页 |
| **合计** | **209** | **19** | **170 组 GIF + 六帧图；58 组图集／119 张单图** |

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

```text
使用 $ui-atlas，参考 dashboard-layouts/inventory-action-workbench，
让库存表的当前商品与右侧操作卡同步，加入清单后更新数量，失败可恢复。
```

建议说明：**目标组件、触发条件、状态变化、作用范围、关键视觉特征**。例如“只在推荐套餐卡片边框循环移动光点”，比“给页面加点动效”更容易得到准确实现。

```text
使用 $ui-atlas，参考 enterprise-workbenches/recruitment-candidate-workbench，
先查看候选人工作台的原尺寸单图，再按现有招聘流程实现指标、筛选和列表，验证空结果与失败恢复。
```
