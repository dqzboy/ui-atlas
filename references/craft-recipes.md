# 产品质感技巧配方

本组包含 20 份实现配方，配有随技能提供、可离线查看的参考图。011 复用已有缓动参考，包含两段连续使用的提示词；012 提供六种消息气泡材质参考；冲击波提供深、浅主题两张效果局部；014 提供四种卡片删除效果；015 提供八类状态连续模式和三张清晰完成态参考；016 提供三类 Toast、通知与行内反馈选型、完整提示词及两张效果参考；017 提供等待状态选型、完整提示词与四种不同用途的效果局部；018 提供六种镭射卡片材质、倾斜与可选厚度翻面、完整提示词及六张清晰正面参考；019 提供五种可逆卡片滚动模式、完整提示词、设备适配和五张清晰局部；Bento 展示另附可编辑 HTML 与渲染脚本。按所需行为选用，再读取对应的完整参数和实现提示词。

| 编号 | 技巧 | 检索 ID | 完整配方 | 效果参考 |
|---|---|---|---|---|
| 001 | 有点击手感的拟物按钮 | `buttons-controls/tactile-button` | [配方](recipes/tactile-button.md) | [JPG](../assets/recipes/tactile-button.jpg) |
| 002 | 带安全三角区的级联菜单 | `overlays/safe-cascade-menu` | [配方](recipes/safe-cascade-menu.md) | [JPG](../assets/recipes/safe-cascade-menu.jpg) |
| 003 | 可调 ASCII 与有序抖色 | `backgrounds/ascii-dither` | [配方](recipes/ascii-dither.md) | [JPG](../assets/recipes/ascii-dither.jpg) |
| 004 | 递进圆角与连续曲率 | `interface-details/continuous-corners` | [配方](recipes/continuous-corners.md) | [JPG](../assets/recipes/continuous-corners.jpg) |
| 005 | 拖拽插入线与递减让位 | `mobile-interactions/ripple-reorder` | [配方](recipes/ripple-reorder.md) | [JPG](../assets/recipes/ripple-reorder.jpg) |
| 006 | 像书一样翻开的卡片 | `cards-tables/book-open-card` | [配方](recipes/book-open-card.md) | [JPG](../assets/recipes/book-open-card.jpg) |
| 007 | 中英文排版与稳定数字 | `interface-details/cjk-latin-typesetting` | [配方](recipes/cjk-latin-typesetting.md) | [JPG](../assets/recipes/cjk-latin-typesetting.jpg) |
| 008 | Wiki 与帮助中心响应式框架 | `documentation-layouts/wiki-layout` | [配方](recipes/wiki-layout.md) | [JPG](../assets/recipes/wiki-layout.jpg) |
| 009 | 提示、跟随气泡与浮层决策 | `overlays/overlay-decision` | [配方](recipes/overlay-decision.md) | [JPG](../assets/recipes/overlay-decision.jpg) |
| 010 | 自适应液态玻璃材质 | `glass-materials/liquid-glass` | [配方](recipes/liquid-glass.md) | [JPG](../assets/recipes/liquid-glass.jpg) |
| 011 | 如何选择更合适的动画节奏？ | `motion/easing` | [配方（两段提示词）](recipes/easing.md) | [WebP](../assets/details/motion/easing-hd-01.webp) |
| 012 | 消息气泡的材质与动效（探索版） | `glass-materials/message-bubble-materials` | [配方](recipes/message-bubble-materials.md) | [六种材质](glass-materials.md#message-bubble-materials) |
| — | 有物理质感的冲击波（含扭曲与通道分离） | `motion/shockwave-halo` | [配方](recipes/shockwave-halo.md) | [深浅主题](motion.md#shockwave-halo) |
| 014 | 四种卡片删除效果：燃烧、柔焰、碎块和撕贴纸 | `motion/card-delete-effects` | [配方（完整提示词）](recipes/card-delete-effects.md) | [四种效果](motion.md#card-delete-effects) |
| 015 | 用好连续性，让产品更丝滑 | `motion/continuous-transitions` | [配方（完整提示词）](recipes/continuous-transitions.md) | [三类完成态](motion.md#continuous-transitions) |
| 016 | Toast 和 Notification 怎么选？ | `overlays/toast-vs-notification` | [配方（完整提示词）](recipes/toast-vs-notification.md) | [两类反馈](overlays.md#toast-vs-notification) |
| 017 | 巧用等待状态，让产品响应更丝滑 | `loading-errors/loading-states` | [配方（完整提示词）](recipes/loading-states.md) | [四种等待反馈](loading-errors.md#loading-states) |
| 018 | 会倾斜、能翻转的 3D 镭射卡片 | `cards-tables/holographic-card` | [配方（完整提示词）](recipes/holographic-card.md) | [六种材质](cards-tables.md#holographic-card) |
| 019 | 五种经典的卡片滚动交互 | `motion/scroll-card-interactions` | [配方（完整提示词）](recipes/scroll-card-interactions.md) | [五种模式](motion.md#scroll-card-interactions) |
| — | Bento 组件网格与独立动效 | `design-composition/bento-motion-grid` | [配方与模板](recipes/bento-motion-grid.md) | [完整网格](design-composition.md#bento-motion-grid) |

参数是实现起点，按现有组件、主题、字号与设备调整。浮层选型先遵循产品的真实可逆性和保存语义；玻璃与连续圆角在目标浏览器中验证并保留回退。所有效果都需在项目实际状态中核对。
