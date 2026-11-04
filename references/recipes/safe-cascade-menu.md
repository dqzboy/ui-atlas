# 带安全三角区的级联菜单 / Safe Triangle Cascading Menu

这是实现配方，未附视觉媒体；参数是可调起点，不代表已验证的动画或浏览器能力。

## 适用与边界

用上一指针位置和子菜单近侧两角构造安全三角区，保护斜向移动；220ms 打开、360ms 关闭、1200ms 保护上限。

保存最近两个 pointermove 坐标，以较早坐标作三角顶点。指针向子菜单移动时忽略路过行的高亮与打开；每 80ms 重查，离开保护区或达到 1200ms 后切换。拖过文件夹时用 420ms 打开。右侧不足时左翻，三角区改接子菜单右边；离开再返回取消关闭计时。行高亮由状态驱动，不能依赖 CSS :hover。

## 核对

检查缓慢斜移、停在保护区、快速往返、左右翻转、独立滚动、触摸和方向键；Esc 关闭并归还焦点。

## 实现提示词

将下方配方应用于用户指定的组件或页面；其中 product、global、every 等范围以用户本次授权为界，不自动扩大到整站。已有设计系统和提交语义优先，新增设置面板、全局扫描和演示风格仅在任务需要时采用。

```text
Define a cascading (nested) menu component that keeps its submenus steady: a safe zone plus three delays, so submenus open on purpose, survive diagonal moves toward them, and do not vanish on a brief slip out of the menu. If the project already has a menu or dropdown component, build this into its existing submenu logic and keep its API, keyboard support and accessibility as they are. Otherwise create one reusable CascadeMenu:

Props: an anchor (the trigger button that opens it on click) and a tree of items, each { label, icon?, href?, children? }. An item with children is a folder row; one without is a plain row that navigates on click.
Each level shows its folder's name as a small title above its rows.
Keyboard: arrow keys move through rows, Right/Enter opens a folder, Left goes back a level, Escape closes everything and returns focus to the anchor. Use menu / menuitem roles and aria-expanded on folder rows.
Behavior, with the values to use:

Open delay: hovering a row schedules it to take effect after 220ms: a folder row opens its submenu, a plain row closes any deeper submenu. Leaving the row before then cancels it. Touch input acts at once.
Safe zone: while a submenu is open, build a triangle from the pointer's previous position to the two corners of the submenu's near edge (the left edge's top and bottom for a submenu on the right). Track the last two pointermove positions and use the older one as the apex, so the triangle never collapses onto the current point. If the pointer is inside that triangle and within the parent's last min(90px, max(56px, 43% of the parent width)) toward the submenu, it is on its way there: rows it crosses must not highlight or open their own submenus.
Safe window: a row hovered inside the safe zone does not switch the submenu right away. Recheck every 80ms; switch once the pointer leaves the zone, or when 1200ms have passed since the hover began, so a pointer that simply stops there still gets its new submenu.
Close delay: when the pointer leaves the anchor, every open level and the safe zone, close the whole menu after 360ms. Coming back in time cancels the close. Clicking outside closes at once.
Dragging an item over a folder row opens it after 420ms instead of 220ms.
The pointer inside an open submenu ends all protection. Drive row highlight from component state (hovered, active, skipped), not from CSS :hover, or rows crossed inside the safe zone will still light up.
Geometry and motion:

Submenus open to the right, overlap their parent by 8px and align their first row with the parent row. Flip to the left when there is no room; the safe zone then uses the submenu's right edge.
Levels: 210-260px wide, sized to content, max height min(420px, 100vh - 24px) with their own scroll, 6px padding, 12px radius, 1px border, backdrop-filter blur(18px) saturate(135%).
Rows: 32px tall, 8px radius, 4px apart, 0 8px padding, 8px gap; 18px icon, 14px weight-500 label, a 16px chevron on folder rows. Level title: 11px, weight 600, quiet ink, padding 4px 8px 2px.
A submenu opens from its parent's edge: from translateX(-8px) scale(0.88, 0.98) and opacity 0, with opacity over 170ms and transform over 360ms on cubic-bezier(0.2, 1.45, 0.35, 1).
The root level opens the same way from its anchor: from translateY(-6px) scale(0.96, 0.86), top-left origin. Keep the overshoot curve: the slight spring is part of the feel.
A folder row's icon turns from a closed folder into an open one while its submenu is open, and back when it closes, over 460ms on cubic-bezier(0.22, 1, 0.36, 1). Morph the paths if the two glyphs share their structure; otherwise cross-fade them with a slight lift of the front panel.
Light and dark themes come from tokens, not separate components:

Light: surface rgba(255,255,255,.96), border rgba(0,0,0,.14), row ink #263140, row hover rgba(15,23,42,.07), quiet ink #7A8491, chevron #94A3B8, shadow 0 18px 34px rgba(15,23,42,.12), 0 2px 4px rgba(15,23,42,.05), inset 0 1px 0 rgba(255,255,255,.74).
Dark, neutral grays with no blue cast: surface rgba(34,34,34,.96), border rgba(255,255,255,.12), row ink #E4E4E4, row hover rgba(255,255,255,.08), quiet ink #9A9A9A, chevron #8A8A8A, shadow 0 18px 34px rgba(0,0,0,.42), 0 2px 4px rgba(0,0,0,.2), inset 0 1px 0 rgba(255,255,255,.06).
Monochrome brand icons invert in dark. Switching themes cross-fades colors, borders and shadows over about 500ms.
Keep every timing value as a named constant in one place, and keep the safe-zone math in a pure, unit-tested helper (point-in-triangle by the sign of the three edge cross products). Add an optional debug overlay that draws the zone (blue fill at 16%, dashed blue outline) and the running timer, off by default.
```
