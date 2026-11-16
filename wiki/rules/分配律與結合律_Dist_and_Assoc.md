---
title: 分配律、結合律與交換律 (Dist, Assoc & Comm)
aliases: [Dist, Assoc, Comm, 分配律, 結合律, 交換律]
category: rules
tags:
  - 等值規則
  - 代數性質
  - 自然演繹法
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]"
---

# 分配律 (Dist)、結合律 (Assoc) 與 交換律 (Comm)

這三組規則奠定了語句邏輯運算子的代數結構，賦予我們重構命題括弧、次序與結合方式的完全自由。

---

## 1. 交換律 (Commutation, Comm)

- **形式**：
  $$\begin{aligned}
  p \lor q &:: q \lor p \\
  p \land q &:: q \land p
  \end{aligned}$$
- **注意禁忌**：**條件句不具交換律**（$p \rightarrow q$ 絕不等於 $q \rightarrow p$）！

---

## 2. 結合律 (Association, Assoc)

- **形式**：
  $$\begin{aligned}
  p \lor (q \lor r) &:: (p \lor q) \lor r \\
  p \land (q \land r) &:: (p \land q) \land r
  \end{aligned}$$
- **限制**：只有在**連詞完全相同**（全為選言，或全為連言）時才能移動括弧。不可從 $A \lor (B \land C)$ 移動括弧為 $(A \lor B) \land C$！

---

## 3. 分配律 (Distribution, Dist)

- **形式**：
  $$\begin{aligned}
  p \land (q \lor r) &:: (p \land q) \lor (p \land r) \\
  p \lor (q \land r) &:: (p \lor q) \land (p \lor r)
  \end{aligned}$$
- **解題核心價值**：
  - **割離不要項**：在推導中，若語句中混雜著不需要的中間變元，透過 Dist 可以把原句拆開，再用 Simp 將不要的項徹底分離剔除！

---

## 4. 相關鏈結

- 證明體系：[[自然演繹法_Natural_Deduction]]
- 搭配規則：[[簡化律與連言律_Simp_and_Conj]]、[[笛摩根定律_DeMorgans_Laws]]
