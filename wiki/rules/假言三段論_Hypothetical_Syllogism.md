---
title: 假言三段論 (Hypothetical Syllogism)
aliases: [Hypothetical Syllogism, HS, 純假言三段論]
category: rules
tags:
  - 推論規則
  - 命題邏輯
  - 自然演繹法
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]"
---

# 假言三段論 (Hypothetical Syllogism, HS)

**假言三段論 (HS)** 是[[自然演繹法_Natural_Deduction]]中用於串聯條件句的單向推論規則，體現了條件蘊涵關係的**遞移性 (Transitivity)**。

---

## 1. 形式定義

- **句法形式**：
  $$\begin{aligned}
  & p \rightarrow q \\
  & q \rightarrow r \\
  \hline
  \therefore\ & p \rightarrow r
  \end{aligned}$$
- **規則表述**：給定兩個條件句，若第一個條件句的後項與第二個條件句的前項相同（居間媒介項 $q$），則可合法推導出由第一個條件句的前項指向第二個條件句後項的新條件句。

---

## 2. 證明實戰戰略地位

- **消去居間項的利器**：當論證目標是建立兩個不相干命題之間的因果或條件鏈條時，HS 是最直觀的串接工具。
- **限制**：HS 屬於單向推論規則，**只能運用於整列語句**，絕不可應用於括弧內部的子句。

---

## 3. 相關鏈結

- 條件推論規則：[[假言推理_Modus_Ponens]]、[[否定後項_Modus_Tollens]]
- 等值換位：[[實質蘊涵律與異質換位_Impl_and_Contra]]
- 證明框架：[[自然演繹法_Natural_Deduction]]
