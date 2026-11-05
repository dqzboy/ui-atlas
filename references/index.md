# UI 参考索引

共 **177 条参考、18 个分类**：155 组组件／状态／设计规则（缓动条目附 011 配方）、12 组精选页面图集，以及 10 组独立配方条目；共提供 11 份完整实现配方。相同效果只保留代表图，必要状态和不同页面才使用多图。

先按名称、意图与关键词筛选，再查看匹配条目的图片和说明。配方参数是实现起点，视觉参考不能替代实际操作验证。

| 分类 | 条目数 | 按需读取 |
|---|---:|---|
| 弹窗与浮层 | 14 | [overlays.md](overlays.md) |
| 加载与错误页 | 13 | [loading-errors.md](loading-errors.md) |
| 背景特效 | 13 | [backgrounds.md](backgrounds.md) |
| 卡片与表格 | 15 | [cards-tables.md](cards-tables.md) |
| 表单 | 14 | [forms.md](forms.md) |
| 常见动效 | 17 | [motion.md](motion.md) |
| 按钮、状态与选项 | 43 | [buttons-controls.md](buttons-controls.md) |
| Web 微交互 | 10 | [web-interactions.md](web-interactions.md) |
| 移动端交互 | 1 | [mobile-interactions.md](mobile-interactions.md) |
| Dashboard 与后台导航 | 4 | [dashboard-navigation.md](dashboard-navigation.md) |
| 玻璃材质与背景 | 1 | [glass-materials.md](glass-materials.md) |
| 界面排版与细节 | 2 | [interface-details.md](interface-details.md) |
| 企业工作台与业务后台 | 4 | [enterprise-workbenches.md](enterprise-workbenches.md) |
| 数据可视化与数字孪生 | 6 | [data-visualization.md](data-visualization.md) |
| 移动端工作台与服务门户 | 3 | [mobile-workbenches.md](mobile-workbenches.md) |
| 文档与帮助中心布局 | 1 | [documentation-layouts.md](documentation-layouts.md) |
| 文字特效 | 12 | [text-effects.md](text-effects.md) |
| 页面与演示设计 | 4 | [design-composition.md](design-composition.md) |

## 查找与查看

```bash
python3 scripts/find_reference.py "长按确认"
python3 scripts/find_reference.py "文字镂空"
python3 scripts/find_reference.py "PPT"
python3 scripts/find_reference.py "动画节奏"
python3 scripts/fetch_media.py text-effects/text-mask
python3 scripts/fetch_media.py loading-errors/loading-button --media images
```

- 组件与文字特效的原片截图随包提供，其他页面图片按需下载并校验 SHA-256，重复使用读取缓存。
- 静态图显示构图与状态；触发、路径、速度、焦点、请求和响应式行为在真实项目中验证。5 份配方另有精选连续片段。
- [11 份质感配方](craft-recipes.md) · [机器索引](catalog.json) · [图片清晰度](media-quality.md) · [技能说明](../SKILL.md)
