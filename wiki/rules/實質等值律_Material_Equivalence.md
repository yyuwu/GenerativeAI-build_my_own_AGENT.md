---
title: 實質等值律 (Material Equivalence)
aliases: [Equiv, 實質等值律, 等值規則]
category: rules
tags:
  - 等值規則
  - 雙條件句
  - 自然演繹法
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]"
---

# 實質等值律 (Material Equivalence, Equiv)

**實質等值律 (Equiv)** 是自然演繹法中解構雙條件句（$\leftrightarrow$ 或 $\equiv$）的核心雙向規則。

---

## 1. 形式定義

- **雙向條件式拆解**：
  $$p \leftrightarrow q :: (p \rightarrow q) \land (q \rightarrow p)$$
- **真值同況拆解**：
  $$p \leftrightarrow q :: (p \land q) \lor (\neg p \land \neg q)$$

---

## 2. 戰略價值

- **打破雙條件句**：在自然演繹中，原生的推論規則（如 MP, MT）無法直接作用於雙條件句。透過 Equiv，可將 $p \leftrightarrow q$ 化為 $(p \rightarrow q) \land (q \rightarrow p)$，再用 Simp 分離出單向條件句進行後續推導。
- **建構雙條件句結論**：若結論要求證明 $A \leftrightarrow B$，標準策略為分別證明 $A \rightarrow B$ 與 $B \rightarrow A$，利用 Conj 合併後，透過 Equiv 完成最後一步。

---

## 3. 相關鏈結

- 語意定義：[[真值函應與邏輯連接詞]]
- 證明體系：[[自然演繹法_Natural_Deduction]]
- 搭配方法：[[條件證明法_Conditional_Proof]]
