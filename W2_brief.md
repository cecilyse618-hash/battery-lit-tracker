# W2 任务单：battery-lit-tracker（电池文献 arXiv 追踪 CLI）

> Phase 1A 第一个构建物 ｜ 周期：2026-10-28 ~ 2026-11-08（两周，约 20h）
> 目标能力：A1 前置基础（API 调用、JSON 解析）+ B6（交付文档）+ 工程习惯（Git、测试、venv）
> 领域资产：产出从第一天起就带电池方向属性，为 Phase 1B 的电池文献 RAG 和旗舰项目铺路

---

## 一、做什么

一个命令行小工具：查询 arXiv 公开 API，按关键词（如 "lithium electrolyte"）抓取最新论文，
输出标题/作者/日期/链接，可保存为 CSV，支持按日期范围和结果数量过滤。

**为什么选这个题**：arXiv API 免费、无需注册、返回结构化数据（XML/JSON）——
"调公开 API 并处理结果"的所有基本功一次练齐，同时工具本身对课题组有真实用处（W20+ 旗舰项目的雏形）。

替代选题（不喜欢可做）：天气聚合 CLI / 汇率转换 CLI——技术要求相同，领域资产为零。

## 二、验收标准（证据门槛，缺一不可）

1. `git clone` 后按 README 安装、运行成功（导师或同学实测更佳）。
2. 至少 10 个有意义的 Git commit，历史呈现渐进式开发（不是一次性提交）。
3. 英文 README 包含：功能说明、安装步骤、使用示例、设计取舍（至少 2 条：如为什么选 argparse 而不用 sys.argv）。
4. 至少 5 个 pytest 测试（参数解析、API 响应解析、错误路径）。
5. 每周决策记录：周报里至少写 1 条"面对什么选择 → 选了什么 → 为什么"。

## 三、独立性规矩（本项目起生效）

| ✅ 允许 | ❌ 禁止 |
|---|---|
| 问 AI "这个报错是什么意思" | "帮我写 xxx 功能的代码" |
| 问 "argparse 和 click 有什么区别" | 让 AI 生成整段代码后照抄 |
| 让 AI 解释一段官方文档看不懂的部分 | 直接粘贴 AI 输出到项目里 |
| 请 AI review 你已写好的代码并给建议 | 让 AI 直接改写你的代码文件 |

判断标准一句话：**产出必须能经得住面试逐行讲解释**——每个函数你都能说出它做什么、为什么这么写。

## 四、两周日程（约 20h）

| 日 | 小时 | 任务 | 边做边补的知识点 |
|---|---|---|---|
| D1 | 2 | 环境：装 Python 3.11+、创建 venv、git init、建 GitHub 仓库 | venv/pip 原理、git 基础（add/commit/push） |
| D2 | 3 | CLI 骨架：argparse 接收关键词、数量、日期参数，打印 help | argparse 用法、if __name__ == "__main__" |
| D3 | 3 | 调 arXiv API：requests 发请求、拿到原始响应 | HTTP 基础（GET/状态码）、requests、urllib.parse 编码 |
| D4 | 3 | 解析响应：从 XML/JSON 提取标题/作者/日期/链接，处理无结果和错误响应 | XML/JSON 结构、异常处理 try/except、API 速率限制 |
| D5 | 2 | 输出：格式化打印 + 写 CSV 文件 | csv 模块、字符串格式化、文件写入 |
| D6 | 3 | 测试 + README：pytest 写 5 个测试；英文 README 完稿 | pytest 基础、断言、README 写法 |
| D7 | 2 | 复盘：跑通全流程、请别人按 README 试装、写英文技术笔记（第一篇博客） | — |
| D8–D14 | 2 | 弹性/加深：1 个自选扩展（见下）+ 周报 ×2 | — |

**自选扩展（完成验收标准后挑一个）**：config 文件支持多关键词批量查询 / 结果去重与本地历史 / 简单的结果排序选项。

## 五、README 结构模板（D6 用）

```
# battery-lit-tracker

One-line description.

## What it does
（2-3 句，给谁用、解决什么）

## Install
（venv 创建、pip install、依赖列表——用 requirements.txt）

## Usage
（命令行示例 + 预期输出截图或文本）

## Design decisions
（≥2 条取舍：为什么 argparse？为什么 XML 解析选 ElementTree？）

## Tests
（怎么跑 pytest，覆盖什么）

## Limitations / next steps
（诚实写局限：如 arXiv 速率限制、无增量更新）
```

## 六、与路线图的对账

- 完成后 A1 未直接得分（A1 需 LLM API 经验），但 Phase 1B W7 的 LLM 应用会把本项目复用为数据层。
- B6 从 0 → 有望 2 分（证据 = 本仓库 README + 实测记录）。
- 第一篇英文技术笔记（D7）计入 30 天计划的"英文技术笔记篇数"指标。
