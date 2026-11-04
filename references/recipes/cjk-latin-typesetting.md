# 中英文排版与稳定数字 / CJK Latin Typesetting

这是实现配方，未附视觉媒体；参数是可调起点，不代表已验证的动画或浏览器能力。

## 适用与边界

标题 balance、正文 pretty、动态数字 tabular-nums、flex 文本 min-width:0；中文按 lang 处理自动间距、标点避头尾及分词断行。

短标题平衡行长，正文减少末行孤词；数字与单位等不可分割组合用不换行空格。按钮不换行；flex 项 min-width:0 后再做 ellipsis，并为真实截断提供完整文本入口。中文正文两端对齐限于足够宽的文字列，窄列不强制；text-autospace 与 text-spacing-trim 渐进增强。中文标题采用分词断点后才用 keep-all；避免 line-break:anywhere 破坏标点禁则。

做 i18n 时同时检查译文长度、词边界与当前布局的匹配程度；仅在用户允许调整文案时改写译文，不用强行断词或大量空隙掩盖布局问题。

## 核对

检查长短标题、窄屏、长英文、混合数字单位、字体加载前后、价格计时器位数变化、截断文本的键盘与触摸入口；不支持的新 CSS 自然回退。

## 实现提示词

将下方配方应用于用户指定的组件或页面；其中 product、global、every 等范围以用户本次授权为界，不自动扩大到整站。已有设计系统和提交语义优先，新增设置面板、全局扫描和演示风格仅在任务需要时采用。

```text
Polish the typography in my product with a set of CSS switches. Change only how text wraps, spaces, aligns and truncates. No copy, font, colour or layout changes beyond what each rule says.

0. Start from what exists
- Put the rules in the global text styles (base CSS, typography tokens, Tailwind config or shared text components) so every page inherits them. Add per-component rules only where a component overrides the base.
- Every rule below is progressive enhancement: browsers that don't know a property ignore it. Add no polyfills.
- Scope the Chinese rules with :lang(zh), and make sure the lang attribute is set on the html element or on the element itself, so English text keeps its own rules.

1. Headings break into even lines
- On h1 to h3, card titles and hero lines: text-wrap: balance;
- Lines come out about the same length, so a heading never ends on one lonely word. Use it on short text; test the target browser's balancing limits.

2. No lone word at the end of a paragraph
- On paragraphs, descriptions and list items: text-wrap: pretty;
- Also join pairs that must not split with a non-breaking space (U+00A0): an em dash and the name after it, a number and its unit.

3. Numbers that change keep their width
- On anything that updates in place or sits in a column (counters, prices, timers, stats, table cells): font-variant-numeric: tabular-nums;
- The font must have tabular figures (the tnum feature); check that the width actually stops changing. Leave running text proportional.

4. Button labels stay on one line
- On buttons and other labels in flex rows: white-space: nowrap; (flex-shrink: 0 works too)
- A crowded row must not squeeze a label onto two lines.

5. Long text truncates instead of spilling out
- A flex item won't shrink below its content, so text inside it can't truncate. On the flex item: min-width: 0;
- On the text itself: overflow: hidden; white-space: nowrap; text-overflow: ellipsis;
- When the text really is cut (scrollWidth > clientWidth), show the full text in a tooltip on hover.

6. Chinese body text: justified, on a whole number of characters
- On Chinese paragraphs only: text-align: justify;
- Set the measure to a whole number of characters (for example max-width: 26em at the paragraph's font size), so a justified line only stretches to absorb Latin words and squeezed punctuation.
- Not for narrow columns (under about 15 characters), short text, captions, buttons or mostly-English text: the gaps get uneven.

7. Space between Chinese and Latin text or numbers
- On Chinese text: text-autospace: normal;
- The browser adds a thin gap between Han characters and Latin letters or digits. Don't also hand-type spaces in copy or translation files. Skip code, inputs and monospaced text.

8. No half-width gap before an opening bracket at a line start
- On Chinese UI text without a first-line indent: text-spacing-trim: trim-start;
- An opening 「 “ （ at the start of a line drops its blank half and lines up with the text above. Long-form text with a two-character indent should use space-first instead. Keep the browser fallback and test the target engines.

9. Chinese headings break between words
- Chinese has no spaces, so a heading can split a word across lines. Mark the break points between words with BudouX (its Simplified or Traditional Chinese model), inserting a wbr element at each one, at build time for static copy or at render time for dynamic copy. Then: word-break: keep-all; overflow-wrap: anywhere; text-wrap: balance;
- Never use keep-all on Chinese without break points: the heading becomes one unbreakable word. Don't use Intl.Segmenter for this (it splits common words wrongly), and don't apply it to body text.

10. Line-start and line-end rules (避头尾)
- Browsers already keep punctuation off the start of a line and squeeze line-end punctuation. Don't rebuild this.
- Find and remove any line-break: anywhere used to stop overflow: it turns these rules off. Use overflow-wrap: anywhere instead.
- Text drawn on canvas or SVG, or wrapped by hand in JS, gets none of this: apply the rules there yourself.

11. When done
- List every file and selector you changed.
- List every line-break: anywhere and word-break: break-all you removed or kept, and why.
- Show before and after on my own pages: a wrapped heading, a paragraph ending, a changing number, a truncated label and a mixed Chinese-English paragraph.
```
