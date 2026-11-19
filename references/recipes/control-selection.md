# 020 · 选择控件选型 / Choice Controls

在现有产品中检查开关、复选框、单选框、分段控制器、下拉选择和操作菜单。先判断它设置什么或执行什么、选项数量、可选数量和生效时机，再判断控件是否合适；保留用户已保存的值、现有组件和依赖。

## 选型规则

| 判断维度 | 推荐起点 | 需要保留的语义 |
|---|---|---|
| 一个即时生效的二元设置 | Switch | 切换即应用；标签描述稳定的设置，不随开关状态改名 |
| 表单中的独立答案，提交后生效 | Checkbox | 可以勾选或取消；多个复选框彼此独立，统一提交时保留草稿 |
| 单选，2–5 个短标签 | 单选 Segmented Control | 设置一个值或同一内容的视图；选中状态明确，窄屏和长标签仍可读 |
| 单选，2–5 个需要说明的选项 | Radio 纵向组 | 同组最多选一个；若业务允许未决定，提供明确的“暂不选择”等选项 |
| 单选，约 6 个以上或标签动态增长 | Select | 字段保留当前值，展开项显示选中标记；宽度与换行受控 |
| 数百个选项 | 可搜索 Select／Combobox | 保留可选值约束、搜索与无匹配提示；不可擅自变为任意输入 |
| 多选 | Checkbox 组或多选 Select | 允许零项与否由业务校验决定；收起后仍能识别所选值 |
| 执行 Export、Duplicate、Delete 等动作 | Dropdown Menu | 选择后执行动作，触发按钮仍表示动作入口；不伪装成已选值 |
| 常用主动作及其相关动作 | Split Button | 主按钮与菜单分别可操作；菜单打开本身不执行主动作 |
| 切换内容面板或目的区域 | Tabs／已有导航 | 与设置数据值的控件区分；保留面板、路由和历史语义 |

数量是本配方的选型起点，需结合标签长度、比较需求、平台惯例与现有设计系统。一个设置的开／关不拆成 On／Off 两个单选；Light／Dark 两个独立命名模式则按互斥选择判断。

## 先诊断，再实施所选范围

盘点每个实际使用位置，包括共用组件在不同页面的不同用途；记录当前值、保存方式、选项来源与现有键盘行为。输出下表，正确项也标明“保持”，不为采用新样式而替换。

| 位置／组件 | 设置的值或执行的动作 | 选项数／可选数／生效时机 | 当前控件 | 建议控件或保持 | 一行理由 | 其他行为变化 |
|---|---|---|---|---|---|---|
| 按实际产品填写 | 字段、筛选或命令 | 即时／Save／Submit | 现有实现 | 基于语义判断 | 指明决定因素 | 保存按钮、空值、菜单位置等 |

仅请求审查时先给诊断并等待用户选择；已有明确选择和实施授权时沿用，不重复索要许可。生效时机、允许空值、清除、默认值、保存入口和动作位置的变化均需明确记录。复用项目组件，没有时使用平台原生控件，不新增依赖。

## 应用边界

下方完整提示词保留其选型简化，使用时按本节解释：

- **生效时机与选中模型分开判断**：即时开关与提交表单复选框是本配方推荐，不代表所有 Checkbox 都必须等待保存。已有即时筛选、表格行选择、全选与半选仍可使用复选框；不能为符合口诀自动新增 Save，也不能去掉原有提交步骤。单个独立表单答案仍可用复选框，不要求一定有多项。
- **值、动作与导航分开判断**：Select 保存值；操作菜单执行命令；Tabs 显示关联面板，导航链接前往目的地。分段外观不自动决定角色，需沿用真实单选、切换按钮或 Tabs 行为。已有动作菜单也可能包含可勾选命令，不因为有勾就一律改为 Select；表单附近的字段操作仍按动作处理。
- **空值与旧数据**：Radio 组可以初始未选，但选定后不能靠再点同项清除。仅在业务允许时增加明确的 none 选项，不静默映射为默认值；required、多选上限、禁用项和失效旧值分别处理。选项使用稳定 ID，标签变化不改已保存值，不因搜索过滤就清除已选项。
- **选择标记与辅助技术**：单选下拉用勾、多选用复选标记及 chips 是自定义外观建议，原生控件保留平台呈现；不强迫原生多选改成 chips。多选 listbox 中的勾选框可作为视觉标记，不在 option 中嵌套另一套可聚焦 checkbox；选中状态由相应控件语义表达。chips 删除入口具有名称，并有删除后的焦点去向。
- **异步与布局**：即时保存失败恢复一致状态并给出可见错误；快速连续切换时防止旧响应覆盖新值。搜索区分加载、无匹配和失败，支持清除搜索与保留选中值；Select 也需为长文、多语言、移动端和放大字号安排宽度、换行与可读的选项列表，不能承诺换成 Select 就永不移位。
- **键盘与读屏**：优先保留原生或现有可靠组件的标签、组名、值、选中／开闭／禁用状态。按控件模式检查 Tab、Space、方向键和 Escape，菜单关闭后焦点回到触发入口；不套用同一套按键给所有控件。检查键盘选中与焦点的区别，状态不能仅靠颜色识别。

## 已有参考

沿用现有条目与文件，不复制图片、不新增 GIF。按要修改的控件读取对应独立原尺寸 WebP：

- [Switch](../buttons-controls.md#switch)、[Checkbox](../buttons-controls.md#checkbox)、[半选](../buttons-controls.md#indeterminate)。
- [Radio](../buttons-controls.md#radio)、[Segmented Control](../buttons-controls.md#segmented-control)、[Split Button](../buttons-controls.md#split-button)。
- [Select](../forms.md#select)、[Dropdown Menu](../overlays.md#dropdown-menu)。

旧参考含控件名称、教学标注或指针时，仅识别控件外观，不将标注、指针或演示页面复制到产品；本配方不声称已获得新帖效果图。静态图不能证明保存时机、键盘、焦点、读屏或数据保持，这些按实际代码与操作验证。

## 完整实现提示词

```text
Review the choice controls in my product (switches, checkboxes, radio buttons, segmented controls, selects and dropdown menus) and decide for each one whether it is the right control. Diagnose first; change only what I approve, in my own code and components, without new dependencies.

1. Read the product
Find every place a person picks something, turns something on or off, or runs an action from a list. For each, note what it sets or does, how many options it has, how many can be picked, and whether it takes effect at once or on Save.

2. How to choose
a. Switch or checkbox: when it takes effect.
- Switch: takes effect the moment it is flipped (settings that save on their own, no Save button).
- Checkbox: one answer in a form, applied on Submit or Save.
- One thing on or off is one switch, never two radios (On / Off). If both sides have names of their own (Light / Dark), it is a choice of one: see (c).

b. Select or dropdown menu: a value or an action.
- Select: holds a value; after a pick the field shows it, and the picked option has a tick in the list.
- Dropdown menu: holds actions (Export, Duplicate, Delete). A pick runs it, the button keeps its name, and the result shows elsewhere. Menus go in page headers, toolbars and row ends, not among form fields. A split button pairs a main action with a menu of related ones (Send, with Send later and Save as draft beside it).
- Tabs switch to other content and set nothing; a segmented control sets a value or the view of the same content.

c. One of several: by the number of options.
- 2 to 5 short options: a segmented control.
- 2 to 5 that each need a line: radio buttons, stacked under the label.
- 6 or more, or labels that change or grow (names, dates, items people add): a select, so the layout never shifts.
- Hundreds (time zones, countries, people): a select with search, and a clear message when nothing matches.

d. Radio or checkbox: how many can be picked.
- Radio: exactly one, all options in view, as in a survey question. It can't be cleared once picked, so add a "none" option (Not sure yet) when that is a fair answer.
- Checkbox: any number, none included.
- Inside a select: a tick for one value, never radio circles; a checkbox before each option for several, with the picks shown as chips in the field.

3. Report before changing
Give me a table, one row per control: where, what it sets or does, the control now, the control it should be (or "right as it is"), why in one line, and anything else that changes (a Save button, a "none" option, an action moved out of a form). Flag every change in behaviour, ask about cases that could go either way, and wait for me to choose.

4. Change what I approve
Use my components, or the platform's own controls when I have none. Keep the values people already saved. Check that switches act at once and checkboxes on submit, selects show their value, menu buttons keep their name, and everything works by keyboard and screen reader.
```

## 实施后核对

- 只修改选中行，报告文件与行为差异；未选项和原本正确项保持原行为。
- 切换、选择、提交、取消与清除符合记录的生效方式；重新打开页面后已保存值一致。
- Select 显示当前值，菜单按钮保持入口名称，Split Button 主动作与次级菜单互不误触发。
- 验证未选、必填、零项、多项、禁用、失效旧值、长标签、无匹配、保存失败与连续操作。
- 手机、放大字号、键盘和读屏可识别名称、组、值与状态，浮层关闭与选项／chip 删除后焦点可预期。

关联配方：[009 浮层与确认选型](overlay-decision.md)、[016 消息反馈选型](toast-vs-notification.md)、[017 等待状态选型](loading-states.md)。
