---
title: 實質蘊涵律與異質換位 (Material Implication & Contraposition)
aliases: [Impl, Contra, 實質蘊涵律, 換位律, 異質換位]
category: rules
tags:
  - 等值規則
  - 條件句
  - 自然演繹法
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]"
---

# 實質蘊涵律 (Impl) 與 異質換位 (Contra)

在自然演繹法中，**實質蘊涵律 (Impl)** 與 **異質換位律 (Contra)** 是處理條件句（$\rightarrow$）時不可或缺的兩大雙向等值工具。

---

## 1. 實質蘊涵律 (Material Implication, Impl)

- **形式**：
  $$p \rightarrow q :: \neg p \lor q$$
- **語意本質**：「若 $p$ 則 $q$」在真值函應上的極小意義，即「不可能前真後假」（$\neg(p \land \neg q)$），由笛摩根定律轉化即為「要麼前件為假，要麼後件為真」（$\neg p \lor q$）。
- **戰略樞紐地位**：
  - **連接條件句與選言的唯一雙向橋樑**。
  - 當推論過程中條件句與選言語句雜陳、無法套用 MP/MT/DS 時，使用 Impl 能將兩者結構統一。

---

## 2. 異質換位律 (Contraposition, Contra)

- **形式**：
  $$p \rightarrow q :: \neg q \rightarrow \neg p$$
- **語意本質**：逆否命題與原條件句完全等值。
- **戰略價值**：
  - 調整條件句前件與後件的位置，便於與其他前提進行[[假言三段論_Hypothetical_Syllogism|HS]]串聯。
  - 搭配否定符號調整目標結論。

---

## 3. 相關鏈結

- 語意學定義：[[真值函應與邏輯連接詞]]
- 證明體系：[[自然演繹法_Natural_Deduction]]
- 搭配規則：[[笛摩根定律_DeMorgans_Laws]]、[[假言三段論_Hypothetical_Syllogism]]
