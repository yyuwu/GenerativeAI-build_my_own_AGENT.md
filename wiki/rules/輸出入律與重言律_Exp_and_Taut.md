---
title: 輸出入律與重言律 (Exportation & Tautology)
aliases: [Exp, Taut, 輸出入律, 重言律]
category: rules
tags:
  - 等值規則
  - 條件句
  - 自然演繹法
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]"
---

# 輸出入律 (Exp) 與 重言律 (Taut)

**輸出入律 (Exp)** 與 **重言律 (Taut)** 是自然演繹證明中處理多重條件與化簡重複項的利器。

---

## 1. 輸出入律 (Exportation, Exp)

- **形式**：
  $$(p \land q) \rightarrow r :: p \rightarrow (q \rightarrow r)$$
- **語意**：「若 $p$ 且 $q$ 同時成立則 $r$」等價於「若 $p$ 成立，則只要 $q$ 成立便會得到 $r$」。
- **戰略價值**：
  - 將多重條件句逐層解包（Unpack）或打包（Pack）。
  - 能大幅簡化巢狀[[條件證明法_Conditional_Proof|CP]]推導步驟。

---

## 2. 重言律 / 恆真律 (Tautology, Taut)

- **形式**：
  $$\begin{aligned}
  p &:: p \land p \\
  p &:: p \lor p
  \end{aligned}$$
- **戰略價值**：
  - **消去重複累贅**：例如由推導得出 $A \lor A$，套用 Taut 即可直接化簡為單一語句 $A$。
  - 常用標準推導鏈：$p \rightarrow p \implies \neg p \lor p$ 或從 $p \lor p \vdash p$。

---

## 3. 相關鏈結

- 證明體系：[[自然演繹法_Natural_Deduction]]
- 證明技術：[[條件證明法_Conditional_Proof]]
