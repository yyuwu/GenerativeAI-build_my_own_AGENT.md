---
title: 笛摩根定律 (DeMorgan's Laws)
aliases: [DeMorgan, DeM, 笛摩根定律, 狄摩根定理]
category: rules
tags:
  - 等值規則
  - 命題邏輯
  - 自然演繹法
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]"
---

# 笛摩根定律 (DeMorgan's Laws, DeM)

**笛摩根定律 (DeM)** 是邏輯學與集合論中最核心的對偶等值規則，精準揭示了「否定」、「連言」與「選言」三者之間的轉化關係。

---

## 1. 形式定義 (雙向等值 $::$)

$$\begin{aligned}
\neg(p \land q) &:: \neg p \lor \neg q \\
\neg(p \lor q) &:: \neg p \land \neg q
\end{aligned}$$

- **規則 1**：「不會既 $p$ 又 $q$」邏輯等值於「要麼非 $p$，要麼非 $q$」。
- **規則 2**：「既不是 $p$ 也不是 $q$」邏輯等值於「非 $p$ 且 非 $q$」。

---

## 2. 局部替換特徵

作為 10 條等值置換規則之一，DeM **不僅能用於整列語句，更可直接應用於任何複雜句式的內部子成分**。例如：
$$[(A \land B) \rightarrow C] \iff [(\neg A \lor \neg B) \rightarrow C]$$

---

## 3. 解題戰略價值

- **拆解複合否定句**：當看到括弧前面帶有否定符號（如 $\neg(P \land Q)$ 或 $\neg(P \lor Q)$）時，通常應第一時間使用 DeM 將括弧打開，以便將長句化成短句進行 Simp 或 DS。

---

## 4. 相關鏈結

- 自然語言對應：[[自然語言翻譯與充要條件]]（Not both / Neither nor）
- 等值規則體系：[[自然演繹法_Natural_Deduction]]
- 搭配規則：[[選言三段論_Disjunctive_Syllogism]]、[[簡化律與連言律_Simp_and_Conj]]
