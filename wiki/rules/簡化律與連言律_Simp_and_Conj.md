---
title: 簡化律與連言律 (Simplification & Conjunction)
aliases: [Simp, Conj, 簡化規則, 連言規則]
category: rules
tags:
  - 推論規則
  - 命題邏輯
  - 自然演繹法
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]"
---

# 簡化律 (Simp) 與 連言律 (Conj)

**簡化律 (Simp)** 與 **連言律 (Conj)** 是[[自然演繹法_Natural_Deduction]]中處理連言語句（$p \land q$）的兩大基礎推論規則。

---

## 1. 形式定義

### 1.1 簡化律 (Simplification, Simp)
- **形式**：
  $$p \land q \vdash p \quad \text{或} \quad p \land q \vdash q$$
- **語意**：既然連言為真要求兩者皆真，則單獨抽取其中任一個連言肢必然為真。
- **嚴格禁忌**：**只能對整列語句使用**！絕不可對複合句中的子連言進行簡化（例如從 $(A \land B) \lor C$ 簡化出 $A \lor C$ 是無效推論）。

### 1.2 連言律 (Conjunction, Conj)
- **形式**：
  $$\begin{aligned}
  & p \\
  & q \\
  \hline
  \therefore\ & p \land q
  \end{aligned}$$
- **語意**：若兩個語句各自已在證明中被確立為真，則將兩者以「$\land$」結合的複句亦必然為真。

---

## 2. 相關鏈結

- 語意定義：[[真值函應與邏輯連接詞]]
- 證明框架：[[自然演繹法_Natural_Deduction]]
- 替代系統對應：[[引進與消去規則系統]]（$\land I, \land E$）
