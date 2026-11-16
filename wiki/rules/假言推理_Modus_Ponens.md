---
title: 假言推理 (Modus Ponens)
aliases: [Modus Ponens, MP, 肯定前項規則]
category: rules
tags:
  - 推論規則
  - 命題邏輯
  - 自然演繹法
updated: 2026-11-17
---

# 假言推理 (Modus Ponens, MP)

**假言推理**（拉丁語：Modus Ponens，字面意思為「藉由肯定而肯定的模式」），簡稱 **MP**，是[[命題邏輯]]與[[自然演繹法_Natural_Deduction]]中最基本且直觀的推論規則。

---

## 1. 形式定義

- **句法形式**：
  $$\begin{aligned}
  & P \rightarrow Q \\
  & P \\
  \hline
  \therefore\ & Q
  \end{aligned}$$
- **規則表述**：若給定一個條件句（若 $P$ 則 $Q$），且同時給定該條件句的前項 $P$，則可合法推導出其後項 $Q$。

---

## 2. 語意保真證明 (真值表)

| $P$ | $Q$ | $P \rightarrow Q$ (前提1) | $P$ (前提2) | $Q$ (結論) |
| :---: | :---: | :---: | :---: | :---: |
| **T** | **T** | **T** | **T** | **T**（有效列） |
| T | F | F | T | F |
| F | T | T | F | T |
| F | F | T | F | F |

在所有前提均為真（第一列）的情況下，結論 $Q$ 必然為真。因此形式保證[[有效性與健全性|有效 (Valid)]]。

---

## 3. 常見謬誤警訊

- **禁止逆用**：由 $P \rightarrow Q$ 與 $Q$ 不能推導出 $P$！
  - 犯此錯誤稱為：[[肯定後項的謬誤]]（形式謬誤）。

---

## 4. 相關鏈結

- 對偶規則：[[否定後項_Modus_Tollens]]
- 證明框架：[[自然演繹法_Natural_Deduction]]
- 範例應用：[[ex_001_基本演繹推導與有效性判定]]
