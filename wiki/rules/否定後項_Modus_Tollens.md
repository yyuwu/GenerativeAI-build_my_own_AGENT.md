---
title: 否定後項 (Modus Tollens)
aliases: [Modus Tollens, MT, 否定後項規則]
category: rules
tags:
  - 推論規則
  - 命題邏輯
  - 自然演繹法
updated: 2026-11-17
---

# 否定後項 (Modus Tollens, MT)

**否定後項**（拉丁語：Modus Tollens，字面意思為「藉由否定而否定的模式」），簡稱 **MT**，是自然演繹法中用於條件句反向推導的核心規則。

---

## 1. 形式定義

- **句法形式**：
  $$\begin{aligned}
  & P \rightarrow Q \\
  & \neg Q \\
  \hline
  \therefore\ & \neg P
  \end{aligned}$$
- **規則表述**：若給定一個條件句（若 $P$ 則 $Q$），且給定該條件句後項的否定 $\neg Q$，則可合法推導出前項的否定 $\neg P$。

---

## 2. 哲學與科學方法意涵

- 卡爾·波普爾（Karl Popper）的**否證論 (Falsificationism)** 即奠基於 Modus Tollens：
  - 假說 $H$ 蘊涵觀察預測 $O$（$H \rightarrow O$）。
  - 實驗觀察到了 $\neg O$。
  - 因此假說被駁斥：$\neg H$。

---

## 3. 常見謬誤警訊

- **禁止逆用**：由 $P \rightarrow Q$ 與 $\neg P$，不能推導出 $\neg Q$！
  - 犯此錯誤稱為：否定前項的謬誤 (Denying the Antecedent)。

---

## 4. 相關鏈結

- 正向規則：[[假言推理_Modus_Ponens]]
- 證明框架：[[自然演繹法_Natural_Deduction]]
- 應用演練：[[ex_001_基本演繹推導與有效性判定]]
