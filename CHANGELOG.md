# PersonaDraw 更新日志

版本按新到旧排列。检查更新时，读取 [main 分支插件清单](plugins/persona-draw/plugin.json) 的 `version`，与已安装清单中的语义版本比较。个人导入的副本、手动复制的 skill 需要单独更新；单文件安装若未记录版本，可直接比较技能正文。

## 0.3.0 · 2026-11-07

- 亮签新增「角色形象」入口，可选每个对话、偶尔或不生成。首次未设置时询问，用户忽略也能继续聊天；同一聊天反复亮签只做一次自动出图决定。
- 四位角色各有社区同人视觉参考；脾气影响表情和姿态。没有生图工具的客户端仍可使用文本菜单。
- 新增本日志和 README 检查更新入口。[下载 v0.3.0](dist/persona-draw-0.3.0.zip)

## 0.2.2 · 2026-11-07

指定后当轮接话；区分局部正式输出、整场暂停、戏内调侃和真实身份问题。亮签时注明补抽。[提交](https://github.com/TinMinL/PersonaDraw/commit/08a9b39b1d33fd04582cda3d63e9286ca4971cff)

## 0.2.1 · 2026-11-07

亮签菜单支持宿主提供的点选控件和编号回退，补充 Hermes Agent 与 DeepSeek Harness 安装说明。[提交](https://github.com/TinMinL/PersonaDraw/commit/87209f746c7bbd124a822f52fa29f713d953bd81)

## 0.2.0 · 2026-11-07

新增 Gemini 和 12 种脾气，可独立调整工作回复的分隔提示及括号旁评。[提交](https://github.com/TinMinL/PersonaDraw/commit/bc7eb114c4b41fce838615bd91762df1efaf4358)

## 0.1.5 · 2026-11-07

技术工作中的交流沿用本场人设，可为注释单独选择文风。[提交](https://github.com/TinMinL/PersonaDraw/commit/b329672b88925706eca04d41e5650de560fb9861)

## 0.1.4 · 2026-11-07

首次上传 GitHub 安装包，附个人安装、默认暗抽与项目交付物的文风说明。[提交](https://github.com/TinMinL/PersonaDraw/commit/2cda86c62dce34a8851c53dd0f595a0ec4504ad1)
