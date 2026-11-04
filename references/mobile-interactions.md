# 移动端交互

触控手势与真实状态分开验证。回弹、轨迹和错峰是视觉反馈，不能意外修改相邻设置、延迟真实选中或触发额外请求。

参考图用于核对构图与可见状态；连续动作在实际项目中验证。像素值、技术栈与缓动由当前项目决定。

## 目录

- [拖拽插入线与递减让位](#ripple-reorder)

<a id="ripple-reorder"></a>
## 拖拽插入线与递减让位 / Ripple Drag Reorder

- 标识：`mobile-interactions/ripple-reorder`；类型：组件／效果。
- 效果要点：横向或纵向拖拽时以插入线标明落点，两侧按距离递减位移并错峰让位；释放提交真实顺序，Esc 或落在外侧恢复。
- 实现关注：可拖目标悬停为 pointer、拖动为 grabbing。被拖项浮起并避开落点；插入线从中心展开，在自身原位置不显示。邻项 n 从 0 计，位移 A × 0.7ⁿ，延迟 24ms × n；图标 A≈10px、卡片≈8px，回弹约 250ms 收敛。视觉位移用 transform，拖拽结束才提交数据；取消恢复拖前快照。
- 验证重点：检查首尾与相邻换位、横竖布局、键盘重排、触摸滚动冲突、落在外部与 Esc 取消；保存失败回滚并显示原因；减弱动态时仅保留插入线。
- 指令例句：参考 mobile-interactions/ripple-reorder，横向或纵向拖拽时以插入线标明落点，两侧按距离递减位移并错峰让位；释放提交真实顺序，Esc 或落在外侧恢复。
- [完整配方与效果参考](recipes/ripple-reorder.md) · [效果图](../assets/recipes/ripple-reorder.jpg)。
- 媒体取舍：需看拖拽中的落点变化与邻项让位，保留未遮挡列表主体的连续片段。

- 连续动效：[GIF 片段](../assets/recipes/ripple-reorder.gif)。
