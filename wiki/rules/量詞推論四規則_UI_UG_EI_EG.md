---
title: 量詞推論四規則 (UI, UG, EI, EG)
aliases: [量詞四規則, UI, UG, EI, EG, 量詞五大限制, 量詞規則形式定義]
category: rules
tags:
  - 述詞邏輯
  - 推論規則
  - 準變元
  - 演繹證明
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch09_述詞邏輯的證明.md]]"
  - "[[raw/assets/rules_for_predicate_logic_sheet.md]]"
---

# 量詞推論四規則 (UI, UG, EI, EG) 與 五大限制

在述詞邏輯中，要將語句邏輯的推論規則（如 MP, HS, MT）套用到量化語句上，必須先透過「量詞推論四規則」合法地消去或添加量詞。

---

## 1. 四大規則精確句法定義 (Official Specifications)

### 1.1 全稱引例 (Rule UI: Universal Instantiation)
$$(u)(\dots u \dots) \vdash (\dots w \dots)$$
- **Provided (限制條件)**：
  1. $(\dots w \dots)$ 是將 $(\dots u \dots)$ 中自由出現的 $u$ 全數代換為 $w$ 所得的結果；
  2. $w$ 可以是**常元 (Constant)**，也可以是**在 $(\dots w \dots)$ 中自由出現的變元 (Variable)**（不做其他變更）。

### 1.2 存在引例 (Rule EI: Existential Instantiation)
$$(\exists u)(\dots u \dots) \vdash (\dots w \dots)$$
- **Provided (限制條件)**：
  1. **$w$ 絕不能是個體常元 (Constant)**！
  2. **$w$ 絕不能是證明先前步驟中已經自由出現過的變元**（必須是全新的準變元）！
  3. $(\dots w \dots)$ 是將自由出現的 $u$ 全數代換為自由變元 $w$ 所得之結果。

### 1.3 全稱一般化 (Rule UG: Universal Generalization)
$$(\dots u \dots) \vdash (w)(\dots w \dots)$$
- **Provided (限制條件)**：
  1. **$u$ 絕不能是個體常元 (Constant)**！
  2. **$u$ 絕不能在先前由 EI 所得的步驟中自由出現過**！
  3. **$u$ 絕不能在尚未被消去的假設前提 (AP) 中自由出現過**！
  4. $(\dots w \dots)$ 是將自由出現的 $u$ 全數代換為自由變元 $w$ 所得之結果，且 $(\dots u \dots)$ 中原本未含有額外自由出現的 $w$。

### 1.4 存在一般化 (Rule EG: Existential Generalization)
$$(\dots u \dots) \vdash (\exists w)(\dots w \dots)$$
- **Provided (限制條件)**：
  1. $(\dots w \dots)$ 是將 $(\dots u \dots)$ 中出現的 $u$（常元或自由變元）**至少一處**代換為自由變元 $w$ 所得之結果，且 $(\dots u \dots)$ 中原本未含有額外自由出現的 $w$。

---

## 2. 五大主要限制 (The Five Major Restrictions)

為了嚴格防止從真前提推導出假結論（維持系統 Soundness），規則設有 5 項不可逾越的鐵律：

### (A) 針對存在引例 (EI) 的兩大限制
1. **限制 1：EI 絕不能引進個體常元**（不能從「有人是兇手」直接推得「張三是兇手」）。
2. **限制 2：EI 引進的準變元必須是「全新的」，絕不能是先前已使用過的符號**：
   - **實戰黃金法則**：**「先做 EI，再做 UI！」**（先讓 EI 佔用新變元，UI 再配合選擇相同變元以利後續推導）。

### (B) 針對全稱一般化 (UG) 的三大限制
3. **限制 3：UG 絕不能對「個體常元」做一般化**（不能因為阿圖笨就推導出全人類都是笨蛋）。
4. **限制 4：UG 絕不能對「由 EI 引進的準變元」做一般化**（凡在 EI 列自由出現過的變元皆失去任意性）。
5. **限制 5：UG 絕不能對「尚未消去的假設前提 (AP)」中自由出現的變元做一般化**（必須等 CP/IP 將該假設消去後，變元才能在作用域外重獲任意性）。

---

## 3. 相關鏈結

- 等值置換規則：[[量詞否定規則_QN]]、[[量詞前綴移入移出定理_Q17_Q18]]
- 55 條定理總覽：[[述詞邏輯55條定理總覽與分類]]
- 證明實戰指南：[[述詞邏輯演繹證明法]]
- 知識地圖：[[邏輯學知識體系地圖]]
