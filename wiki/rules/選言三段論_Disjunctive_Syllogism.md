---
title: 選言三段論 (Disjunctive Syllogism)
aliases: [Disjunctive Syllogism, DS, 選言推理]
category: rules
tags:
  - 推論規則
  - 命題邏輯
  - 自然演繹法
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch01_導論.md]]"
---

# 選言三段論 (Disjunctive Syllogism, DS)

**選言三段論**（Disjunctive Syllogism，簡稱 **DS**），又稱析取三段論，是[[自然演繹法_Natural_Deduction]]中處理選言語句（$P \lor Q$）的核心推論規則。

---

## 1. 形式定義

- **句法形式 1**：
  $$\begin{aligned}
  & P \lor Q \\
  & \neg P \\
  \hline
  \therefore\ & Q
  \end{aligned}$$
- **句法形式 2**：
  $$\begin{aligned}
  & P \lor Q \\
  & \neg Q \\
  \hline
  \therefore\ & P
  \end{aligned}$$
- **規則表述**：若給定一個選言語句（$P$ 或 $Q$），且否定了其中一個選言肢，則可以合法推導出另一個選言肢必然為真。

---

## 2. 講義經典範例

### 範例 1：小明的居住地 (Example A)
1. 小明是新竹人，或者小明是台北人。($P \lor Q$)
2. 並非小明是新竹人。($\neg P$)
$\therefore$ 3. 小明是台北人。($Q$)
- **分析**：此論證形式完全有效，無論我們實際上是否知道小明的戶籍事實。

### 範例 2：天氣預測 (Example B)
1. 今天會下雨或者今天會下雪。($P \lor Q$)
2. 並非今天會下雨。($\neg P$)
$\therefore$ 3. 今天會下雪。($Q$)

### 範例 3：健全論證示範（十八尖山與陽明山）
1. 十八尖山在新竹，或者陽明山在高雄。(T)
2. 並非「陽明山在高雄」。(T)
$\therefore$ 3. 十八尖山在新竹。(T)
- 形式符合 DS（有效），且兩前提均為事實真相，因此構成了[[有效性與健全性|健全論證 (Sound Argument)]]。

---

## 3. 語意保真證明 (真值表)

| $P$ | $Q$ | $P \lor Q$ (前提1) | $\neg P$ (前提2) | $Q$ (結論) |
| :---: | :---: | :---: | :---: | :---: |
| T | T | T | F | T |
| T | F | T | F | F |
| **F** | **T** | **T** | **T** | **T**（唯一前提皆真列） |
| F | F | F | T | F |

在所有前提均為真（第三列）的情況下，結論 $Q$ 必然為真，因此形式保證[[有效性與健全性|有效 (Valid)]]。

---

## 4. 相關鏈結

- 其他演繹規則：[[假言推理_Modus_Ponens]]、[[否定後項_Modus_Tollens]]
- 證明框架：[[自然演繹法_Natural_Deduction]]
- 論證品質：[[有效性與健全性]]
- 知識地圖：[[邏輯學知識體系地圖]]
