---
title: 量詞否定規則 (Quantifier Negation, QN)
aliases: [Quantifier Negation, QN, 量詞否定, 量詞對偶律]
category: rules
tags:
  - 述詞邏輯
  - 等值規則
  - 對當方陣
  - 演繹證明
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch09_述詞邏輯的證明.md]]"
---

# 量詞否定規則 (Quantifier Negation, QN)

**量詞否定規則 (QN)** 是述詞邏輯中處理「帶有否定號之量化語句」的核心雙向等值規則（Rules of Replacement）。它精準體現了[[對當方陣與範恩圖|對當方陣]]中的矛盾對角線關係。

---

## 1. 四大等值公式 (雙向等值 $::$)

$$\begin{aligned}
1. \quad \neg(u)\phi(u) &:: (\exists u)\neg\phi(u) \quad &\text{（並非所有 $u$ 都具 $\phi$ $\iff$ 存在某些 $u$ 不具 $\phi$）} \\
2. \quad (u)\neg\phi(u) &:: \neg(\exists u)\phi(u) \quad &\text{（所有 $u$ 都不具 $\phi$ $\iff$ 不存在任何 $u$ 具有 $\phi$）} \\
3. \quad \neg(\exists u)\phi(u) &:: (u)\neg\phi(u) \quad &\text{（不存在任何 $u$ 具有 $\phi$ $\iff$ 所有 $u$ 都不具 $\phi$）} \\
4. \quad (\exists u)\neg\phi(u) &:: \neg(u)\phi(u) \quad &\text{（存在某些 $u$ 不具 $\phi$ $\iff$ 並非所有 $u$ 都具 $\phi$）}
\end{aligned}$$

---

## 2. 局部適用性與戰略價值

不同於單向量詞四規則（UI, UG, EI, EG），QN 作為**等值置換規則**：
1. **可直接應用於任何複雜句式的局部子式**。
2. **打開括弧的先行工序**：
   - 傳統的 UI 或 EI **絕無法直接作用於開頭帶有否定號的量詞**（例如 $\neg(x)Fx$ 不能直接做 UI！）。
   - 透過 QN，先將 $\neg(x)Fx$ 等值轉換為 $(\exists x)\neg Fx$，便可合法施展 EI 解開量詞！

---

## 3. QN 的導出規則性質

- 雖然 QN 極度便利，但在後設邏輯中，**QN 是一條導出規則 (Derived Rule)**。
- 只要憑藉 UI、EI、UG、EG 與語句邏輯的 IP（歸謬法），即可完全證明 QN 的四條公式成立。

---

## 4. 相關鏈結

- 量詞推論規則：[[量詞推論四規則_UI_UG_EI_EG]]
- 語意理論來源：[[對當方陣與範恩圖]]
- 證明實戰指南：[[述詞邏輯演繹證明法]]
