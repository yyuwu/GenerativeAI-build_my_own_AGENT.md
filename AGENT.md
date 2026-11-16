# AGENT.md - 哲學邏輯課堂與習題 Wiki 維護規範

> 本文件是本知識庫（Logic Wiki）的核心規則手冊（Schema）。它規範了 AI Agent 如何維護、擴充、驗證本「邏輯學（Logic）」課程知識庫。
> 核心架構啟發自 Andrej Karpathy 的 **LLM Wiki Pattern**：使用者負責蒐集原始資料（講義、作業、考題）與提問探索；Agent 負責建立雙向鏈結、提煉概念、維護一致性、詳解習題，打造持續積累與進化的持久性知識庫。

---

## 1. 角色定位與核心哲學 (Philosophy & Role)

- **IDE 與程式設計師的比喻**：
  - **Obsidian** 是使用者瀏覽與檢視關聯的 IDE。
  - **Agent** 是編寫、重構與維護筆記的工程師。
  - **Wiki 庫** 是一套持續演化的軟體程式碼庫。
- **持續累積而非單次生成**：
  - 傳統 RAG 每次查詢都從碎片拼湊，無法累積體系。
  - 本 Wiki 將每一次的「講義研讀」、「習題解析」、「論證辯析」編譯並沉澱為互相鏈結的 Markdown 筆記。
- **單一真理來源 (Single Source of Truth)**：
  - 原始講義與題目放在 `raw/`，永不被 Agent 修改。
  - `wiki/` 則是由 Agent 全權編寫、持續維護與交織鏈結的精華層。

---

## 2. 知識庫架構 (Three-Layer Architecture)

```
邏輯_Logic/
├── AGENT.md                    # 本維護手冊 (Schema & Conventions)
├── index.md                    # 內容總目錄與概念索引 (Content Index)
├── log.md                      # 時間軸變更紀錄 (Append-only Chronological Log)
│
├── raw/                        # 【第一層：原始來源層 (唯讀)】
│   ├── lectures/               # 課堂投影片、教師講義、課堂筆記、錄音逐字稿
│   ├── readings/               # 教科書章節、哲學經典選讀
│   ├── problem_sets/           # 原始作業卷、期中期末歷屆試題
│   └── assets/                 # 原始圖片、真值表截圖、范恩圖
│
└── wiki/                       # 【第二層：知識沉澱層 (Agent 全權維護)】
    ├── concepts/               # 核心概念（有效性、健全性、語義學、語法學等）
    ├── rules/                  # 推論規則與等值規則（MP, MT, De Morgan, UI, EI 等）
    ├── methods/                # 證明與決策程序（真值表法、自然演繹法、真值樹法等）
    ├── fallacies/              # 形式與非形式謬誤（稻草人、假二分、肯定後項等）
    ├── exercises/              # 習題詳解庫、易錯陷阱、解題策略與技巧
    └── overviews/              # 單元綜述、邏輯體系地圖、期中/期末複習綱要
```

---

## 3. 符號與排版規範 (Notation & Formatting)

邏輯學高度依賴精確的符號與推導格式。所有 Wiki 頁面必須嚴格遵守以下格式：

### 3.1 邏輯運算子 (LaTeX 語法)

| 邏輯運算 / 概念                        | 標準 LaTeX 符號                          | 備註說明                         |
| :------------------------------- | :----------------------------------- | :--------------------------- |
| **否定 (Negation)**                | $\neg P$ 或 $\sim P$                  | 建議全庫統一優先使用 $\sim$            |
| **連言 (Conjunction)**             | $P \land Q$ 或 $P \ ∙ \ Q$            | 建議優先使用 $P \ ∙ \ Q$           |
| **選言 (Disjunction)**             | $P \lor Q$                           | 包含性選言 (Inclusive OR)         |
| **條件句 / 實質蘊涵 (Conditional)**     | $P \rightarrow Q$ 或 $P \supset Q$    | 建議優先使用$P \supset Q$          |
| **雙條件句 / 實質等值 (Biconditional)**  | $P \leftrightarrow Q$ 或 $P \equiv Q$ | 若且唯若 (iff)建議優先使用$P \equiv Q$ |
| **全稱量詞 (Universal)**             | $\forall x \, P(x)$                  | 對於所有 $x$                     |
| **存在量詞 (Existential)**           | $\exists x \, P(x)$                  | 存在至少一個 $x$                   |
| **邏輯推導 (Turnstile / Syntactic)** | $P \vdash Q$                         | 句法推論（可推導出）                   |
| **語意蘊涵 (Semantic Entailment)**   | $P \vDash Q$                         | 語意推論（模型滿足）                   |
| **矛盾符號 (Contradiction)**         | $\bot$ 或 $\times$                    | 歸謬法或真值樹封閉                    |

### 3.2 雙向鏈結 (Obsidian Wikilinks)
- 提及任何已存在或重要的核心術語時，**務必使用雙向鏈結**，例如：`[[有效性與健全性]]`、`[[假言推理_Modus_Ponens]]`、`[[自然演繹法_Natural_Deduction]]`。
- 建立新頁面時，若檔名包含英文學名，建議採用 `概念名_英文名` 命名（如 `選言三段論_Disjunctive_Syllogism.md`），以兼顧繁中閱讀與學術檢索。

### 3.3 自然演繹法排版模板
在記錄習題證明或規則範例時，統一採用標準行號排版：

```markdown
證明目標：$P \rightarrow R$
前提：
1. $P \rightarrow Q$                     (前提)
2. $Q \rightarrow R$                     (前提)

證明步驟：
3. | $P$                                (假設，用於條件證明 CP)
4. | $Q$                                (1, 3 假言推理 MP)
5. | $R$                                (2, 4 假言推理 MP)
6. $P \rightarrow R$                     (3-5 條件證明 CP)
Q.E.D.
```

### 3.4 頁面 Frontmatter 元數據 (YAML)
每個 `wiki/` 頁面頂部均應包含 YAML 元數據：
```yaml
---
title: 概念或題目名稱
aliases: [別名1, English Name]
category: concepts | rules | methods | fallacies | exercises | overviews
tags:
  - 命題邏輯
  - 自然演繹法
updated: YYYY-MM-DD
sources:
  - "[[raw/lectures/lecture_03.pdf]]"
---
```

---

## 4. 四大標準作業流程 (Agent Workflows)

### 4.1 Ingest（攝取原始教材 / 講義）
當使用者上傳或放入新講義至 `raw/` 並發出指令時：
1. **閱讀並解析**：細讀 raw 檔案，識別出：
   - 核心定義 (Definitions)
   - 推論規則 (Inference Rules)
   - 經典例題與論證 (Example Arguments)
2. **建構與更新頁面**：
   - 若為全新概念：於 `wiki/concepts/` 或 `wiki/rules/` 建立新頁面。
   - 若為既有概念：打開舊頁面，擴充細節，若有定義差異或更深入的說明，進行整合；若與過去筆記有衝突，加註思辨與比對說明。
3. **建立網絡交叉鏈結**：確保新頁面鏈結回舊頁面，且舊頁面反向鏈結至新概念。
4. **維護索引與紀錄**：
   - 在 `index.md` 對應分類中加入項目與一句話說明。
   - 在 `log.md` 結尾新增一筆記錄：`## [YYYY-MM-DD] ingest | 講義標題`。

### 4.2 Solve & Learn（習題推導與錯題沉澱）
當使用者要求解題或上傳作業題庫時：
1. **符號化 (Symbolization)**：
   - 定義命題常元/述詞符號（如 $P$:「蘇格拉底是人」）。
   - 標明論證的前提 (Premises) 與結論 (Conclusion)。
2. **完整推導證明 (Step-by-step Proof)**：
   - 標註每一步採用的規則（附上該規則的 Wiki 鏈結，如 `[[假言推理_Modus_Ponens]]`）。
   - 若題目有多種解法（例如真值表法 vs 歸謬法 vs 自然演繹法），提供最簡潔解法與替代解法。
3. **易錯分析 (Pitfalls & Key Insights)**：
   - 說明此題容易犯的謬誤或盲點（例如誤將肯定後項當作 MP，或在量詞推導時違反 UG 的限制條件）。
4. **沉澱歸檔**：
   - 將題目與詳解存入 `wiki/exercises/`，檔名格式例如 `ex_2026_HW2_Q4_條件證明.md`。
   - 更新 `index.md` 與 `log.md`。

### 4.3 Query & Synthesis（概念查詢與綜述生成）
當使用者提問（例如：「解釋條件證明 (CP) 與歸謬法 (IP) 的差異與使用時機」）：
1. **檢索 Wiki 庫**：先檢視 `index.md` 與相關 concept/rule 頁面。
2. **綜合回答**：提供清楚嚴謹的哲學邏輯說明，附帶具體公式與例題，並精確引用既有筆記的鏈結。
3. **回饋成新綜述 (Compounding)**：
   - 若該提問具有高度複習價值或跨單元綜合性質，詢問或主動將其提煉為新頁面（如 `wiki/overviews/CP與IP方法比較.md`）。
   - 確保好答案不只留在對話歷史中，而是沉澱回知識庫。

### 4.4 Lint & Refactor（健康檢查與知識除錯）
定期執行知識庫盤點：
- **孤島檢測 (Orphan Pages)**：找出沒有任何入向鏈結的 Wiki 頁面，為其在 index 或相關概念頁補上鏈結。
- **缺失概念標記 (Wanted Pages)**：檢查筆記中被頻繁提及但尚未有獨立頁面的核心主題（例如提到了「選言三段論」但尚無該頁面），主動提示使用者建立。
- **一致性校驗 (Consistency Check)**：符號用法是否統一？規則引用是否準確？

---

## 5. `index.md` 與 `log.md` 維護約定

- **`index.md` 規則**：
  - 依照分類列出所有 wiki 頁面。
  - 格式範例：`- [[有效性與健全性]] — 論證形式評估的兩大核心標準（有效：前提真則結論必真；健全：形式有效且前提均為真）。`
  - 保持精簡，作為 Agent 尋找筆記的第一站地圖。
- **`log.md` 規則**：
  - 嚴格採用 Append-only（僅在末尾追加）。
  - 格式標準：
    ```markdown
    ## [YYYY-MM-DD] <操作類型> | <目標名稱>
    - **摘要**：簡述變動內容與主要涉及概念。
    - **新增/更新頁面**：
      - `[[wiki/.../xxx.md]]`
    ```
  - 操作類型限定為：`ingest`、`solve`、`query`、`lint`、`refactor`。

---

## 6. 給 Agent 的行為準則 (Agent Commandments)

1. **講求邏輯嚴謹性**：邏輯學容不得模糊，每一條推論都必須有合法的規則依據。
2. **繁體中文為主要輸出**：專有名詞保留中英對照（如：健全性 Soundness、析取/選言 Disjunction）。
3. **保持連結網絡緊密**：絕不建立互不相連的孤島筆記。
4. **守護 raw 目錄**：嚴禁修改或刪除 `raw/` 下的使用者原始檔案。
5. **杜絕遞迴嵌套**：簡報組件嚴禁包含回跳父頁面之鏈結，保持單向展示邊界。
6. **堅持設計系統一致性**：所有頁面與簡報必須嚴格繼承亮橘細線、磨砂玻璃與藍紫重點之設計標記（Design Tokens）。

---

## 7. 專題研究與簡報自動化生產管線 (Topic & Presentation Pipeline)

本章節規範如何將靜態 Wiki 知識庫快速提煉為高品質「主題研究筆記」與「互動式 HTML 簡報」，並實現零手動修改程式碼的一鍵自動編譯。

### 7.1 五步標準生產管線 (5-Step Production SOP)

```
[Wiki 知識庫] 
      │
      ▼ (Step 1: 嚴格本庫立論 + 外部 SEP 建議)
[notes/<主題名稱>.md] (Frontmatter 包含 presentation 宣告)
      │
      ▼ (Step 2: 黃金 9 頁論證拆解)
[slides/<主題名稱>.md] (每頁論點、公式、日常例證、鳥獸戲畫對應)
      │
      ▼ (Step 3: 基於模版派生)
[presentation/<主題名稱>/index.html] (套用 Design Tokens 與貼圖)
      │
      ▼ (Step 4: 一鍵編譯)
`python scripts/generate_html_wiki.py` (自動掃描 notes/，自動掛載側邊欄與內嵌 iframe)
      │
      ▼ (Step 5: 驗證無窮嵌套與孤島)
[更新完成之 logic_wiki.html]
```

### 7.2 黃金 9 頁哲學論證骨架 (The Golden 9-Slide Schema)

所有主題研究簡報統一遵循此 9 頁節奏，兼具形式邏輯嚴密性與自然語言批判性：

| 頁碼 | 類型標籤 (Kicker) | 核心任務 | 鳥獸戲畫貼圖配置推薦 |
| :---: | :--- | :--- | :--- |
| **Slide 1** | `COVER` | 專題題目、副標題、研究團隊標註 | **引路/講師動物**（如 `choju109_0011_3.png` 手持指揮棒迎賓） |
| **Slide 2** | `THE CLASH OF INTUITIONS` | 形式規定 vs. 日常直覺的強烈衝突點 | **震驚/恐慌動物**（如 `choju112_0017_4.png` 雙手大開張口驚呼） |
| **Slide 3** | `SYSTEM JUSTIFICATION` | 形式體系為何不能退讓的三大理由（真值函應、保真性、規則保全） | **防護/捍衛動物**（如 `choju97_0024_5.png` 撐開結界守護自洽邊界） |
| **Slide 4** | `CLASSICAL PARADOXES` | 形式規定引發的經典哲學悖論（如假前項、真後項） | **重擊/破壞動物**（如 `choju108_0007_1.png` 扛巨槌破壞常理） |
| **Slide 5** | `PROOF & THEOREMS` | 支撐該特性的演繹定理或推導法（如演繹定理 DT、條件證法 CP） | **典雅推理動物**（如 `choju68_0023_1.png` 持荷葉傘漫步呼應雨天條件句） |
| **Slide 6** | `NATURAL RESISTANCE` | 自然語言在深層語境下的抗拒（如充要混淆、反事實條件句崩塌） | **抱頭/頭痛動物**（如 `choju95_0039_3.png` 冒汗抱頭陷入語意崩潰） |
| **Slide 7** | `PHILOSOPHICAL REMEDIES` | 哲學家提出的修補進路（語用學格萊斯、模態邏輯劉易斯等） | **深思動物**（如 `choju93_0012_3.png` 托腮陷入沉思） |
| **Slide 8** | `SYNTHESIS & INSIGHTS` | 符號系統的工具邊界與終極省思（符號演算 vs 鮮活思維） | **凌空/昇華動物**（如 `choju111_0006_2.png` 展臂凌空飛越形式束縛） |
| **Slide 9** | `REFERENCES & EXPANSION` | 權威文獻回顧（SEP）與未來 Wiki 待擴充概念詞條 | **回眸/致意動物**（如 `chojuother2nd0014_10.png` 搖扇含笑致意收尾） |

### 7.3 資料驅動 Frontmatter 宣告規範

在 `notes/<主題名稱>.md` 頂部的 YAML 元數據中，以宣告式結構控制簡報內嵌：

```yaml
---
title: 主題研究標題
category: projects
tags: [主題研究, 專案簡報]
created: YYYY-MM-DD
wiki_sources:
  - "[[wiki/concepts/...]]"
presentation:
  enabled: true
  path: "presentation/index.html"    # 簡報 HTML 之相對路徑
  height: "660px"                   # 內嵌 iframe 高度
  title: "主題研究互動式簡報"
---
```

---

## 8. 全端視覺設計系統規範 (Design Tokens & UI Schema)

本 Wiki 與專題簡報嚴格遵守統一的現代極簡美學（Neo-Brutalist & Minimalist Glassmorphism）。

### 8.1 核心色彩標記 (Color Tokens)

```css
:root {
    /* 1. 主色系：亮橘細線與微光 (System Actions, Hairlines & Accents) */
    --accent-orange: #ff7300;
    --accent-orange-deep: #e65c00;
    --line-orange: #ff7300;
    --line-orange-soft: rgba(255, 115, 0, 0.28);
    --line-orange-glow: rgba(255, 115, 0, 0.12);

    /* 2. 重點色系：藍紫色 (Wikilinks, Highlighting & Selection) */
    --accent-purple: #5c56d6;
    --accent-purple-deep: #4338ca;
    --line-purple-soft: rgba(92, 86, 214, 0.38);
    --bg-purple-highlight: rgba(92, 86, 214, 0.12);
    --selection-purple: rgba(92, 86, 214, 0.22);

    /* 3. 中性文字與底色 */
    --bg-page: #ffffff;
    --text-main: #171717;
    --text-secondary: #525252;
    --text-muted: #8c8c8c;
    --line-border: #e5e5e5;
}
```

- **規範規則**：橘色（Orange）專門用於「系統操作」、「主視覺外框」與「狀態光暈」；藍紫色（Blue-Purple）專門用於「維基雙向鏈結」、「內文反白」與「名詞醒目標示」，兩者職責分明，嚴禁混淆。

### 8.2 半透明磨砂玻璃卡片規範 (Glassmorphism Cards)

投影片卡片與目錄浮動面板統一採用如下樣式：
```css
.card-surface {
    background: rgba(255, 255, 255, 0.82);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid var(--line-orange);
    border-radius: 4px;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.04), 0 1px 8px var(--line-orange-glow);
}
```

### 8.3 日本鳥獸戲畫貼圖美學規範 (Chōjū-giga Sticker Guidelines)

- **一頁一圖原則**：每張投影片卡片僅配置一張鳥獸戲畫貼圖，維持高雅留白與視覺專注。
- **安全距離容器**：標題區必須包覆於 `.slide-title-wrap` 中，並設定 `padding-right: 150px;`，確保貼圖置於右上側時絕不與文字產生任何遮疊。
- **微互動微動效應**：
  ```css
  .slide-sticker {
      position: absolute;
      pointer-events: none;
      filter: drop-shadow(0 6px 14px rgba(0, 0, 0, 0.08));
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), filter 0.28s ease;
  }
  .slide-card:hover .slide-sticker {
      transform: scale(1.04) rotate(-1.5deg);
      filter: drop-shadow(0 8px 18px rgba(255, 115, 0, 0.18));
  }
  ```

---

## 9. 防呆機制與架構純淨準則 (Safety Checks & Quality Assurance)

1. **嚴禁 iframe 遞迴嵌套**：
   - 簡報 HTML（`presentation/.../index.html`）作為嵌入元件，**內部絕對禁止出現任何連回主 Wiki 首頁或文章之連結與按鈕**，以防止在 iframe 內再次載入全站網頁造成無窮遞迴。
2. **目錄層級控制單一化**：
   - 「展開全部 / 收起全部」功能僅允許存在於右側目錄側邊欄搜尋框正下方（`.sidebar-quick-tools`），隨目錄收合自動隱藏；頂部 Header 一律保持極簡純淨，僅保留首頁標誌與當前路徑。
3. **無邊框無干擾內嵌**：
   - 簡報內嵌於文章頂端時，外層 iframe 必須維持 `border: none;`，不可再額外套用裝飾性外框或宣傳字樣，使簡報自然融為文章的一部分。
