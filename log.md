# 維護與變更日誌 (Wiki Activity Log)

本紀錄檔採 Append-only 方式維護，忠實記錄 Wiki 知識庫的演進歷程。

---

## [2026-11-17] init | 邏輯學課堂 Wiki 知識庫初始化
- **摘要**：參考 Karpathy LLM Wiki 規範完成知識庫骨架搭建，建立 AGENT.md 繁中指引與標準三層架構，並導入第一批核心邏輯概念與範例頁面。
- **新增/更新頁面**：
  - `[[AGENT.md]]`
  - `[[index.md]]`
  - `[[raw/README.md]]`
  - `[[wiki/overviews/邏輯學知識體系地圖.md]]`
  - `[[wiki/concepts/有效性與健全性.md]]`
  - `[[wiki/rules/假言推理_Modus_Ponens.md]]`
  - `[[wiki/rules/否定後項_Modus_Tollens.md]]`
  - `[[wiki/methods/自然演繹法_Natural_Deduction.md]]`
  - `[[wiki/fallacies/肯定後項的謬誤.md]]`
  - `[[wiki/exercises/ex_001_基本演繹推導與有效性判定.md]]`

## [2026-11-17] ingest | 第一章 導論 (Ch. 1 Introduction)
- **摘要**：完成第一章課堂講義全文字攝取（Ingest）。將原始講義完整歸檔至 `raw/lectures/ch01_導論.md`，並提煉出 4 個全新核心概念頁面、1 個推論規則頁面，深度充實了「有效性與健全性」的真假值組合分析與「肯定後項謬誤」的反例剖析，全面更新了知識地圖與總索引。
- **新增檔案**：
  - `[[raw/lectures/ch01_導論.md]]`
  - `[[wiki/concepts/論證與陳述句.md]]`
  - `[[wiki/concepts/演繹與歸納.md]]`
  - `[[wiki/concepts/一致性與有效性檢測.md]]`
  - `[[wiki/concepts/發現脈絡與證成脈絡.md]]`
  - `[[wiki/rules/選言三段論_Disjunctive_Syllogism.md]]`
- **更新頁面**：
  - `[[wiki/concepts/有效性與健全性.md]]`（增補講義經典真值與有效性 4 象限組合矩陣及柯林頓/鴨嘴獸等案例）
  - `[[wiki/fallacies/肯定後項的謬誤.md]]`（增補講義羅德島、閱讀/睡覺等無效性證偽範例）
  - `[[wiki/overviews/邏輯學知識體系地圖.md]]`（掛載新概念與論證基礎章節）
  - `[[index.md]]`（新增各概念頁面連結與一句話摘要）

## [2026-11-17] ingest | 第二章至第五章 語句邏輯、真值表與演繹證明全體系
- **摘要**：完成 Ch. 2 符號化、Ch. 3 真值表、Ch. 4 自然演繹法 18 條規則、Ch. 5 條件證法/間接證法與後設邏輯的巨量講義攝取。將原始講義拆分並完整保存在 `raw/lectures/`，並提煉出 6 個核心概念頁面、4 個證明方法頁面、8 個推論與等值規則頁面，全面更新知識地圖與總索引。
- **新增檔案**：
  - `[[raw/lectures/ch02_語句邏輯裡的符號化.md]]`
  - `[[raw/lectures/ch03_真值表.md]]`
  - `[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]`
  - `[[raw/lectures/ch05_條件證法與間接證法及後設邏輯.md]]`
  - `[[wiki/concepts/真值函應與邏輯連接詞.md]]`
  - `[[wiki/concepts/語句形式與取代實例.md]]`
  - `[[wiki/concepts/自然語言翻譯與充要條件.md]]`
  - `[[wiki/concepts/恆真句_矛盾句與適真句.md]]`
  - `[[wiki/concepts/使用與提及_Use_and_Mention.md]]`
  - `[[wiki/concepts/後設邏輯_健全性與完備性.md]]`
  - `[[wiki/methods/真值表判定法.md]]`
  - `[[wiki/methods/條件證明法_Conditional_Proof.md]]`
  - `[[wiki/methods/間接證明法_Indirect_Proof.md]]`
  - `[[wiki/methods/引進與消去規則系統.md]]`
  - `[[wiki/rules/假言三段論_Hypothetical_Syllogism.md]]`
  - `[[wiki/rules/簡化律與連言律_Simp_and_Conj.md]]`
  - `[[wiki/rules/附加律與兩難推論_Add_and_CD.md]]`
  - `[[wiki/rules/笛摩根定律_DeMorgans_Laws.md]]`
  - `[[wiki/rules/實質蘊涵律與異質換位_Impl_and_Contra.md]]`
  - `[[wiki/rules/分配律與結合律_Dist_and_Assoc.md]]`
  - `[[wiki/rules/輸出入律與重言律_Exp_and_Taut.md]]`
  - `[[wiki/rules/實質等值律_Material_Equivalence.md]]`
- **更新頁面**：
  - `[[wiki/methods/自然演繹法_Natural_Deduction.md]]`（增補 18 條規則單雙向權限對照表、6 大戰略心法）
  - `[[wiki/overviews/邏輯學知識體系地圖.md]]`（擴充語句邏輯語法、語意、證明與後設邏輯完整架構）
  - `[[index.md]]`（全面更新所有新增條目之導航連結與一句話摘要）

## [2026-11-17] ingest | 第七章至第十一章 一階述詞邏輯、語意學、量詞演繹證明與等同理論
- **摘要**：完成 Ch. 7 述詞符號化、Ch. 8 述詞語意學與反例、Ch. 9 四大量詞推論規則與 QN、Ch. 11 等同邏輯與確定描述詞的全面講義攝取。將原始講義歸檔至 `raw/lectures/`，並提煉出 5 個核心概念頁面、3 個推論規則頁面、1 個演繹方法頁面、1 個進階實戰習題頁面，全面升級知識地圖與總索引。
- **新增檔案**：
  - `[[raw/lectures/ch07_述詞邏輯的符號化.md]]`
  - `[[raw/lectures/ch08_述詞邏輯的語意學.md]]`
  - `[[raw/lectures/ch09_述詞邏輯的證明.md]]`
  - `[[raw/lectures/ch11_等同與確定描述詞.md]]`
  - `[[wiki/concepts/個體_述詞與量詞.md]]`
  - `[[wiki/concepts/對當方陣與範恩圖.md]]`
  - `[[wiki/concepts/展開式與有數量化.md]]`
  - `[[wiki/concepts/等同與確定描述詞.md]]`
  - `[[wiki/concepts/述詞邏輯語意學與無效性證明.md]]`
  - `[[wiki/rules/量詞推論四規則_UI_UG_EI_EG.md]]`
  - `[[wiki/rules/量詞否定規則_QN.md]]`
  - `[[wiki/rules/等同規則與反身律_ID_and_IR.md]]`
  - `[[wiki/methods/述詞邏輯演繹證明法.md]]`
  - `[[wiki/exercises/ex_002_述詞邏輯演繹推導與量詞規則限制.md]]`
- **更新頁面**：
  - `[[wiki/overviews/邏輯學知識體系地圖.md]]`（新增完整的「一階述詞邏輯與等同」完整章節，鏈結語法、語意、演繹與哲學問題）
  - `[[index.md]]`（全庫納入述詞邏輯與量詞規則條目，保持單一知識地圖索引）

## [2026-11-17] ingest | 第一章至第五章課堂作業習題與官方解答全面沉澱
- **摘要**：完成 Ch. 1 至 Ch. 5 所有指定習題與官方解答的全面攝取（Ex 1-3, 2-7, 2-10, 3-1~3-13, 4-1~4-14, 5-1~5-8）。將原始作業卷與詳解依章節完整歸檔於 `raw/problem_sets/`，並提煉出 5 個專題習題解析頁面，涵蓋概念辨析、短真值表反例技巧、18 條規則解題心法、表達完備性 (DNF) 證明、IP vs. 直接證法效率對比與零前提定理推導。
- **新增檔案**：
  - `[[raw/problem_sets/exercises_ch01_導論.md]]`
  - `[[raw/problem_sets/exercises_ch02_符號化.md]]`
  - `[[raw/problem_sets/exercises_ch03_真值表.md]]`
  - `[[raw/problem_sets/exercises_ch04_自然演繹證明.md]]`
  - `[[raw/problem_sets/exercises_ch05_條件與間接證法.md]]`
  - `[[wiki/exercises/ex_ch01_有效性與健全性觀念辨析.md]]`
  - `[[wiki/exercises/ex_ch02_語句符號化與真值函應判準.md]]`
  - `[[wiki/exercises/ex_ch03_真值表與短真值表反例技巧.md]]`
  - `[[wiki/exercises/ex_ch04_自然演繹法18條規則經典推導.md]]`
  - `[[wiki/exercises/ex_ch05_條件證法與間接證法進階演練.md]]`
- **更新頁面**：
  - `[[index.md]]`（增列完整的習題解析專區與單行指引）

## [2026-11-17] ingest | 碎片講義、期中考解答、課本進階章節與參考卡全面歸檔
- **摘要**：完成使用者提供的碎片講義與考卷全面歸納與吸收：
  1. 將「115上 邏輯期中考解答」保存至 `raw/problem_sets/`，並提煉成專門的應試與避坑頁面。
  2. 將課本 pp. 63-65 一對一邏輯形式 (One-one form) 與真值表建構五步法、pp. 44-45 符號化與 Exercise 2-6、實質條件句哲學證成講義、Q17/Q18 量詞移位定理歸納入知識庫。
  3. 將官方 18 條規則＋CP/IP 參考卡存入 `raw/assets/`。
- **新增檔案**：
  - `[[raw/lectures/supplement_實質條件句的哲學證成.md]]`
  - `[[raw/lectures/supplement_一對一形式與真值表建構.md]]`
  - `[[raw/lectures/supplement_自然語言翻譯技巧與Ex2-6.md]]`
  - `[[raw/lectures/supplement_述詞量化定理與Q17應用.md]]`
  - `[[raw/problem_sets/exam_115上_邏輯期中考解答.md]]`
  - `[[raw/assets/valid_forms_reference_sheet.md]]`
  - `[[wiki/concepts/實質條件句的哲學爭論與證成.md]]`
  - `[[wiki/rules/量詞前綴移入移出定理_Q17_Q18.md]]`
  - `[[wiki/exercises/exam_期中考精華詳解與觀念避坑.md]]`
  - `[[wiki/exercises/ex_ch02_自然語言符號化Ex2-6實戰.md]]`
- **更新頁面**：
  - `[[wiki/concepts/語句形式與取代實例.md]]`（深入定義一對一邏輯形式及其判定定理）
  - `[[wiki/methods/真值表判定法.md]]`（增補五步 $2^n$ 交替建構算法）
  - `[[wiki/overviews/邏輯學知識體系地圖.md]]`（納入新定理、概念與期中考專案）
  - `[[index.md]]`（同步更新全庫索引）

## [2026-11-17] ingest | 語句邏輯小考 (1) 至 (7) 官方解答全面吸納與考點梳理
- **摘要**：檢索並提取使用者指定的 `語句邏輯小考解答-20261116` 資料夾中全部 7 份 docx 檔案。將原始試卷依序完整轉存至 `raw/problem_sets/`，並提煉產出綜合性的大師複習手冊 `wiki/exercises/quiz_語句邏輯小考精華與考點全解.md`，涵蓋是非題、五大符號化句型、短真值表、18 條規則一題多解、CP/IP 定理推導與單選核心避坑指南。
- **新增檔案**：
  - `[[raw/problem_sets/quiz_01_論證有效性與一致性是非題.md]]`
  - `[[raw/problem_sets/quiz_02_語句邏輯符號化.md]]`
  - `[[raw/problem_sets/quiz_03_真值表檢驗有效性與一致性.md]]`
  - `[[raw/problem_sets/quiz_04_自然演繹法18條規則推導.md]]`
  - `[[raw/problem_sets/quiz_05_自然演繹法多重證法演練.md]]`
  - `[[raw/problem_sets/quiz_06_推論規則證明定理_CP_IP.md]]`
  - `[[raw/problem_sets/quiz_07_語句邏輯綜合觀念選擇題.md]]`
  - `[[wiki/exercises/quiz_語句邏輯小考精華與考點全解.md]]`
- **更新頁面**：
  - `[[index.md]]`（增列小考全解條目與各分項導航）

## [2026-11-17] ingest | 述詞邏輯課後作業 (Ch 7~10) 與期末小考全面歸檔
- **摘要**：完成使用者提供的 Chapter 7、8、9、10 課後作業解答及 `期末/述詞邏輯小考解答-20261116`（小考 5、6、7）的全面吸納與知識庫沉澱。將原始試卷與作業依章節保存於 `raw/problem_sets/`，並提煉出 4 個高階述詞解析頁面（量詞符號化陷阱、數學反例模型構造、一元述詞演繹證明與易錯限制、關係述詞多重量詞推導與 Q17 定理證明）。
- **新增檔案**：
  - `[[raw/problem_sets/exercises_ch07_述詞符號化.md]]`
  - `[[raw/problem_sets/exercises_ch08_述詞語意學與反例.md]]`
  - `[[raw/problem_sets/exercises_ch09_一元述詞演繹證明.md]]`
  - `[[raw/problem_sets/exercises_ch10_關係述詞與多重量詞證明.md]]`
  - `[[raw/problem_sets/quiz_述詞邏輯小考_05_06_07.md]]`
  - `[[wiki/exercises/ex_ch07_述詞邏輯符號化與量詞陷阱.md]]`
  - `[[wiki/exercises/ex_ch08_述詞邏輯語意學與反例模型構造.md]]`
  - `[[wiki/exercises/ex_ch09_一元述詞演繹證明與易錯限制.md]]`
  - `[[wiki/exercises/ex_ch10_關係述詞多重量詞推導與定理證明.md]]`
- **更新頁面**：
  - `[[index.md]]`（增設「一階述詞邏輯習題解析單元」與單行索引）


## [2026-11-17] ingest | 附錄二述詞邏輯55條定理、推論規則手冊與自然語言否定補充講義
- **摘要**：完成使用者提供的《附錄二：述詞邏輯定理》(Q1~Q55)、《述詞邏輯推論規則》官方掃描參考卡、以及《補充一：部分否定與全部否定》與《補充二：部分否定、全部否定和雙重否定的翻譯》等碎片講義的全面歸檔與知識轉化。
  1. 將 55 條定理結構化歸入 `raw/lectures/supplement_述詞邏輯55條重要定理集.md`，並提煉出專門綜述頁面 `wiki/overviews/述詞邏輯55條定理總覽與分類.md`，詳解 Q38 不對稱推導與五大結構定理族。
  2. 將雙面量詞推論規則及等同公理手冊轉存為 `raw/assets/rules_for_predicate_logic_sheet.md`，對照更新推論規則庫。
  3. 將部分否定 (Not all / Both not)、全部否定 (None / Neither / Nor) 與雙重否定 (Double Negation) 深度語義比較與中英對照指南轉存至 `raw/lectures/supplement_英語與漢語否定句翻譯指南.md`，並提煉產出核心概念頁面 `wiki/concepts/自然語言否定深層語意_部分否定與雙重否定.md`。
- **新增檔案**：
  - `[[raw/lectures/supplement_述詞邏輯55條重要定理集.md]]`
  - `[[raw/lectures/supplement_英語與漢語否定句翻譯指南.md]]`
  - `[[raw/assets/rules_for_predicate_logic_sheet.md]]`
  - `[[wiki/overviews/述詞邏輯55條定理總覽與分類.md]]`
  - `[[wiki/concepts/自然語言否定深層語意_部分否定與雙重否定.md]]`
- **更新頁面**：
  - `[[index.md]]`（增列述詞邏輯 55 條定理總覽與自然語言否定深層語意條目）
  - `[[wiki/overviews/邏輯學知識體系地圖.md]]`（鏈結述詞邏輯定理全集與否定翻譯語意學）


## [2026-11-17] refactor | 離線單一檔案 HTML 網頁應用生成 (logic_wiki.html)
- **摘要**：響應使用者延伸應用需求，將全庫 56 篇 Markdown 筆記、對照表與雙向連結打包為離線自包含單一 HTML 網頁 (`logic_wiki.html`)。
  1. **排版風格全面精煉**：去除所有 Emoji 表情符號，側邊欄取消深色底色改採無底色純白極簡風格；字體全面改採纖細高雅字重（Font-weight 350 / 500）；全站以 1px 極細微細線（Hairline border）作為格線與結構分割。
  2. **側邊欄自律收納機制**：左側欄劃分「講義」、「習題」與「專案」三大部分，各章節支援雙層折疊收納；側邊欄本身支援全域一鍵收納與展開，收起後主文章自適應展開至全寬。
  3. **離線預先編譯數學公式**：LaTeX 邏輯運算子與自然演繹法格式在 Python 預編譯為語意化標籤，完全不仰賴外部 CDN。
- **新增檔案**：
  - `[[scripts/build_title_anchor_map.py]]`
  - `[[scripts/title_anchor_map.json]]`
  - `[[scripts/title_anchor_map.md]]`
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`
- **更新頁面**：
  - `[[wiki/overviews/邏輯學知識體系地圖.md]]`（增補別名）
  - `[[wiki/concepts/後設邏輯_健全性與完備性.md]]`（增補別名）


## [2026-11-17] fix | 側邊欄左上角三槓按鈕與雙向連結點擊導航修復
- **摘要**：針對使用者反饋進行兩項關鍵修復：
  1. **左上角常駐細線三槓 (Hamburger) 按鈕**：在頂部工具列最左端與側邊欄標題旁加入無表情符號之 1.2px 極細線條三槓開關，側邊欄收起後仍常駐於螢幕左上角，點擊可自由切換展開與收納。
  2. **正文雙向連結（底線文字）點擊跳轉修復**：分析發現原本透過非同步 `hashchange` 監聽在本地 `file:///` 環境下易被瀏覽器安全沙盒阻擋或因 Hash 未變而不觸發。全面改為在生成 HTML 時直接於 `<a>` 標籤注入 `onclick="navigateTo('file_id', 'sub_id'); return false;"`，並搭配全域點擊事件直調，實現點擊底線文字 100% 零延遲瞬間切換文章與滾動定位。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] refactor | 側邊欄調整至右側 (Right-Sidebar Layout)
- **摘要**：應使用者要求，將目錄導航側邊欄改置於畫面右側（Right-Sidebar）：
  1. **右側收納動畫**：左側作為主要閱讀與推導正文區，右側為講義/習題/專案目錄；收起時平滑向右滑出，正文自適應擴充至全寬。
  2. **常駐右上角三槓按鈕**：頂部導航列最右側固定設置極簡三槓按鈕，無論側欄收起或展開，該按鈕皆永久停駐於螢幕右上角，點擊可自由切換開關，徹底解決收納後按鈕消失的問題。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] fix | 右側欄排版偏移與按鈕跳躍問題徹底解決
- **摘要**：深度分析使用者指出的「排版一起往右移、按鈕消失」現象，發現原先負 margin 與 flex 自適應寬度造成點擊瞬間按鈕與導航列向右暴衝 320px，導致按鈕跳出游標點擊範圍。
  1. **右上角視窗級絕對固定按鈕 (`position: fixed`)**：將三槓按鈕改以 `position: fixed` 固定釘在螢幕右上角 (`top: 10px; right: 18px; z-index: 1000;`)，完全脫離 flex 文件流，位置永遠保持在同一個像素座標，游標原地再點一次即可無痛開關。
  2. **純寬度收斂動畫 (width: 0)**：徹底拔除 `margin-right: -320px` 負邊距，側欄收折改為平滑寬度歸零，主畫面不再發生跳動或向右拉扯偏移。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] refactor | 亮橘色細線邊框與毛玻璃磨砂質感視覺改版
- **摘要**：針對使用者指定的視覺風格進行專屬調校：
  1. **亮橘色細線條視覺語彙**：全目錄主邊界、搜尋外框、折疊分割線、右上角固定開關按鈕採用高辨識度亮橘色細線 (`#ff7300` / `rgba(255, 115, 0, 0.28)`)，營造俐落科技工藝感。
  2. **毛玻璃透明質感 + 磨砂效果 (Frosted Glass & Matte Texture)**：目錄底色改採 `rgba(255, 255, 255, 0.78)` 搭配 `backdrop-filter: blur(20px) saturate(180%)` 高透光毛玻璃，並疊加純 CSS 3px 微米級磨砂顆粒噪點遮罩 (`radial-gradient`)，兼具物理磨砂玻璃觸感與文字高清晰度。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] feat | 設計感主頁 (Home View) 與統一風格標誌導航
- **摘要**：應使用者要求，為 Wiki 網頁增設專屬設計感主頁與頂部品牌連動：
  1. **主頁中央「邏輯」巨幅視覺字樣**：字體採用極簡纖細字重（Font-weight 300，4.6rem），搭配上方 `PHILOSOPHY & FORMAL REASONING` 與下方 `SYMBOLIC LOGIC // KNOWLEDGE BASE` 等寬英文字樣，展現高雅哲學工藝感。
  2. **懸浮中央搜尋列與即時檢索下拉選單**：搜尋框支援全庫 56 篇文獻即時模糊檢索，輸入時即時浮現毛玻璃卡片式結果列表，點擊即跳轉目標文章。
  3. **快速導航標籤與數據橫條**：配置「知識地圖、18條規則、真值表法、55條定理、小考全解、期中解答」等 6 大捷徑，並列出全庫 56 篇核心指標。
  4. **頂部標誌風格統一與一鍵返家**：左上角 LOGIC WIKI 改為同款「邏輯 LOGIC // WIKI」精緻標籤，點擊立即一鍵滑順切換回主頁。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] fix | 展開全部與收起全部功能僅在目錄開啟時顯示
- **摘要**：針對使用者要求「展開全部跟收起全部的功能應該在目錄開啟時才出現」進行優化：
  1. **頂部操作列連動隱藏**：在 CSS 中綁定 `body.sidebar-collapsed .nav-right`，當目錄側欄處於收起狀態時，頂部的「展開全部」與「收起全部」按鈕平滑淡出並完全隱藏 (`opacity: 0; visibility: hidden; pointer-events: none;`)，避免在無目錄時出現無關操作干擾正文閱讀；目錄開啟時則自動平滑顯現於目錄左側。
  2. **目錄搜尋列內嵌快速控制工具**：在毛玻璃側邊欄搜尋框下方新增「架構層級」極細線工具列（`[展開全部] / [收起全部]`），使目錄結構控制與側欄本體緊密聚合，自然在目錄開啟時呈現。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] style | 展開/收起按鈕亮橘細線光暈美化與主頁數據條移除
- **摘要**：應使用者指示進行細部視覺優化：
  1. **展開/收起按鈕風格一致化**：「展開全部」與「收起全部」按鈕套用與右上角固定三槓開關完全一致的亮橘色細邊框 (`1px solid #ff7300`)、柔和橘光外發光 (`box-shadow: 0 1px 6px rgba(255, 115, 0, 0.12)`)、毛玻璃底色以及 Hover 時的高亮擴散光暈 (`0 0 10px rgba(255, 115, 0, 0.28)`)。
  2. **主頁純粹化留白調整**：移除主頁下方之「56 篇文獻 · 11 個章節 · 18 條演繹規則 · 55 條述詞定理 · 100% 離線可用」數據橫條，聚焦中央巨幅「邏輯」字樣、懸浮檢索框與快速入口，使主頁視覺更加極簡沉浸。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] style | 雙向連結底線字樣反白色彩調整為藍紫色
- **摘要**：針對正文中雙向連結（底線字樣）之互動與反白色彩進行調校：
  1. **移除橘色反白**：將 `a.wikilink` 懸停時的背景反白、文字變色與底線顏色，由原先的亮橘色系全面調整為高雅沉穩的藍紫色系（Indigo / Blue-Purple）。
  2. **藍紫色系視覺規格**：
     - 底線預設：`text-decoration-color: rgba(92, 86, 214, 0.38)` 柔和藍紫細線。
     - 懸停反白（Hover Highlight）：文字轉為深藍紫 `#4338ca`、底線轉為鮮明藍紫 `#5c56d6`、背景反白轉為清透藍紫微光 `rgba(92, 86, 214, 0.12)`。
     - 游標選取反白（Selection）：文字選取時背景同步轉為藍紫色 `rgba(92, 86, 214, 0.22)`。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] feat | 實質條件句主題研究全套產出：筆記、逐頁簡報與離線 HTML 投影
- **摘要**：響應使用者主題研究需求，完成方向一「實質條件句的哲學悖論與自然語言的語意鴻溝」之三階產出與全站整合：
  1. **完整研究筆記（純 Wiki 來源保證）**：於 `notes/` 目錄建立 `實質條件句的哲學悖論與自然語言的語意鴻溝.md`，正文百分之百取材自 Wiki 既有文獻，系統論證真值函應之最小語意、三大系統性證成（真值函應、MP保全、CP演繹定理）、兩大經典悖論、充要混淆與反事實崩塌、以及格萊斯語用學與劉易斯模態嚴格條件句。檢索史丹佛哲學百科（SEP）前沿文獻（Grice 1989, Lewis 1912, Ramsey 1929, Adams 1975, Edgington 1995），乾淨隔離於文末「附錄」作為未來 Wiki 擴充指引。
  2. **逐頁簡報腳本設計**：於 `slides/` 目錄建立 `slide_content.md`，架構包含 9 頁精煉投影片，涵蓋封面、衝突起源、系統證成、經典悖論、演繹定理、自然語言反抗、哲學救援、結論省思與文獻展望。
  3. **獨立互動式 HTML 簡報**：於 `presentation/` 目錄建立 `index.html`，具備鍵盤導航（左右方向鍵、Space、F全螢幕）、進度條指示、頁碼計數與 100% 離線預渲染排版，延續亮橘細線（#ff7300）、毛玻璃與藍紫色重點色風格。
  4. **無縫整合至主網頁 (`logic_wiki.html`)**：在側邊欄「專案 (PROJECTS)」新增「主題研究與專題簡報」分組，主畫面內嵌 9 頁簡報之即時互動視窗與全螢幕播放按鈕，並於專案總覽中心掛載已上線卡片。
- **新增檔案**：
  - `[[notes/實質條件句的哲學悖論與自然語言的語意鴻溝.md]]`
  - `[[slides/slide_content.md]]`
  - `[[presentation/index.html]]`
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] refactor | 移除專案總覽中心並消除簡報遞迴嵌套連結
- **摘要**：應使用者指示進行架構純化與防呆修復：
  1. **移除專案總覽與擴充中心**：徹底從側欄與全站結構中移除 `project_hub`（專案總覽與擴充中心），側邊欄「專案 (PROJECTS)」直接聚焦於具體落地的「主題研究與專題簡報」。
  2. **消除簡報遞迴嵌套漏洞**：移除 `presentation/index.html` 頂部「邏輯 LOGIC // SLIDES」之超連結以及「返回 Wiki」按鈕，使其成為純粹專注展示的簡報投影片，徹底杜絕 iframe 內嵌時因點擊返回而引發「網頁嵌套網頁」的遞迴無窮問題。
- **更新檔案**：
  - `[[presentation/index.html]]`
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`


## [2026-11-17] style | 簡報內嵌介面純淨化：移除外框與多餘介紹文案
- **摘要**：針對主頁面中「實質條件句」文章上方內嵌之簡報介面進行視覺純淨化：
  1. **移除冗餘介紹外框**：徹底拔除原先包裹 iframe 之橘色大外框容器（`project-presentation-banner`）及其多層巢狀邊界，消除「框中有框」的冗贅感。
  2. **移除介紹標題與文字**：刪除「INTERACTIVE SLIDE DECK // 專案簡報成果」與「本研究已製作為 9 頁高質感互動式 HTML 簡報」等介紹性文案，使 9 頁簡報播放器直接無邊框（`border: none`）自然嵌入文章頂部，維持純粹優雅的極簡版面。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`
  - `[[presentation/index.html]]`


## [2026-11-17] feat | 簡報融合日本鳥獸戲畫貼圖美學（assets）
- **摘要**：檢視並整合 `assets/` 目錄中 10 款鳥獸戲畫（鳥獣戯画）傳統水墨典雅貼圖，依據每頁簡報之哲學主題精準對應並配置至 9 頁投影片中：
  1. **貼圖內容檢視與主題對應佈局**：
     - **Slide 1 [封面]**：`choju109_0011_3.png`（持指揮棒引導之青蛙講師），右下角典雅迎賓宣告主題。
     - **Slide 2 [起源與衝突]**：`choju112_0017_4.png`（雙手大開、張口驚駭青蛙），生動呈現日常常識面對「前假則真」的荒謬震撼感。
     - **Slide 3 [形式系統證成]**：`choju97_0024_5.png`（高舉雙手撐開防護結界之學士貓），象徵嚴格形式系統捍衛假言推理（Modus Ponens）之自洽邊界。
     - **Slide 4 [經典悖論展示]**：`choju108_0007_1.png`（扛著巨大重槌之青蛙），象徵假前項悖論 *Ex falso quodlibet*「偽妄之中，可推導出一切事物」的毀滅性衝擊。
     - **Slide 5 [演繹定理雙刃劍]**：`choju68_0023_1.png`（頂戴學帽、手持碩大荷葉傘漫步之學者貓），以經典的「若下雨則帶傘」日常條件句意象呼應條件證明法（CP）。
     - **Slide 6 [自然語言反抗]**：`choju95_0039_3.png`（抱頭冒汗、極度崩潰痛苦之貓咪），生動反映自然語言遇到反事實條件句與充要條件混淆時的認知崩塌。
     - **Slide 7 [哲學家修補]**：`choju93_0012_3.png`（單爪托腮、陷入深沉哲學沉思之學士貓），展現羅丹「沉思者」風範，對應格萊斯與劉易斯為悖論開出的深刻修補處方。
     - **Slide 8 [形式邊界啟示]**：`choju111_0006_2.png`（凌空騰躍、展翅飛翔之青蛙），寓意人類理性超越機械外延邊界、回歸心靈鮮活洞察的高遠境界。
     - **Slide 9 [文獻與未來展望]**：`chojuother2nd0014_10.png`（手搖摺扇、回眸含笑致意之優雅學士貓），為專案研究作收尾並展望後續 Wiki 詞條擴充。
  2. **樣式與動態美學**：
     - 加入 `.slide-title-wrap` 與 `.slide-sticker` 響應式佈局，預留右上角視覺空間，避免與標題文字疊合。
     - 貼圖具備細緻陰影（`drop-shadow`）與滑鼠懸停微動效果（`scale(1.04) rotate(-1.5deg)`），結合現代磨砂玻璃與古雅水墨浮世繪，營造獨特且專業之哲學簡報質感。
- **更新檔案**：
  - `[[presentation/index.html]]`
  - `[[log.md]]`


## [2026-11-17] refactor | 收攏展開與收起按鈕：僅保留目錄導航內部之快捷控制
- **摘要**：應使用者指示純化版面操作層次：
  1. **移除頂部導航列按鈕**：徹底移除頂部導覽列（`top-navbar`）右側之「展開全部」與「收起全部」按鈕（`.nav-right` 與 `.action-btn`）。
  2. **專注目錄內部快捷控制**：全站僅保留目錄側邊欄（`wiki-sidebar`）搜尋列下方、具備亮橘細線磨砂光暈質感的「架構層級」展開／收起按鈕組（`.sidebar-quick-tools`），使版面視覺更為簡潔清爽，操作邏輯高度收斂於目錄本身。
- **更新檔案**：
  - `[[scripts/generate_html_wiki.py]]`
  - `[[logic_wiki.html]]`
  - `[[log.md]]`


## [2026-11-17] refactor | 系統規則升級：建立可持續擴充的專題與簡報自動化生產產線
- **摘要**：應使用者對超越單次 Vibe Coding、建立長期標準生產機制的願景，完成全系統規範重構與自動化引擎解耦：
  1. **升級核心手冊規約（AGENT.md）**：
     - 新增「第 7 章：專題研究與簡報自動化生產管線（5 步標準產線 SOP、黃金 9 頁哲學論證骨架、宣告式 Frontmatter Schema）」。
     - 新增「第 8 章：全端視覺設計系統規範（亮橘細線 `#ff7300`、藍紫維基鏈結 `#5c56d6`、磨砂壓克力玻璃、鳥獸戲畫貼圖美學）」。
     - 新增「第 9 章：防呆機制與架構純淨準則（杜絕 iframe 遞迴嵌套、目錄快捷控制單一化）」。
  2. **編譯器動態資料驅動改造（scripts/generate_html_wiki.py）**：
     - 徹底廢除 Python 腳本中寫死的單一專案判斷（`if doc_id == "project_material_implication"`），改為動態掃描 `notes/*.md`。
     - 支援通用宣告式 Frontmatter 元數據 `presentation: { enabled: true, path: ..., height: ... }`，自動掛載專案側邊欄與內嵌無邊框簡報。
  3. **固化通用簡報骨架模板（presentation/template.html）**：
     - 將全套響應式磨砂卡片、進度條、鍵盤換頁監聽（←/→/Space/F）、全螢幕及鳥獸戲畫貼圖容器抽成通用模板，未來幾秒鐘內即可派生全新主題簡報。
  4. **同步更新索引與全站編譯**：
     - `index.md` 增設「主題研究與專題簡報」區塊。
     - `logic_wiki.html` 重新編譯通過，驗證零孤島與零語法錯誤。
- **新增檔案**：
  - `[[presentation/template.html]]`
- **更新檔案**：
  - `[[AGENT.md]]`
  - `[[index.md]]`
  - `[[scripts/generate_html_wiki.py]]`
  - `[[notes/實質條件句的哲學悖論與自然語言的語意鴻溝.md]]`
  - `[[logic_wiki.html]]`
  - `[[log.md]]`
