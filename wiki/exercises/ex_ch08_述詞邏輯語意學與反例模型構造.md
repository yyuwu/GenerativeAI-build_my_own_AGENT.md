---
title: 習題解析 Ch. 8 - 述詞邏輯語意學與反例模型構造
aliases: [Exercise 8, 述詞反例模型, 展開式證偽]
category: exercises
tags:
  - 習題詳解
  - 述詞邏輯
  - 語意學
  - 反例構造
updated: 2026-11-17
sources:
  - "[[raw/problem_sets/exercises_ch08_述詞語意學與反例.md]]"
  - "[[raw/problem_sets/quiz_述詞邏輯小考_05_06_07.md]]"
---

# 習題解析 Ch. 8：述詞邏輯語意學與反例模型構造

本篇精選第八章及期末小考關於構造數學模型反例、微型論域展開式證偽無效論證的核心技巧。

---

## 一、 構造數學模型反例 (Ex 8-2)

在述詞邏輯中，要證明論證無效，最嚴密的方法是建立一個**數學模型解釋**，使前提皆真而結論為假：

### 題目：$(\exists x)(Ax \land Bx),\ (\exists x)(Bx \land Cx) \vdash (\exists x)(Ax \land Cx)$
- **直覺誤區**：很多初學者誤以為由「有些 $A$ 是 $B$」且「有些 $B$ 是 $C$」能推得「有些 $A$ 是 $C$」。
- **構造嚴格數學反例**：
  - 設定 $\text{Domain} = \{\text{自然數 } 1, 2, 3 \dots\}$
  - $Ax$: $x$ 是偶數
  - $Bx$: $x$ 能被 3 整除
  - $Cx$: $x$ 是奇數
- **檢驗模型**：
  - 前提 1：存在自然數既是偶數又能被 3 整除（如 $x = 6$）$\implies$ **真 (True)**。
  - 前提 2：存在自然數能被 3 整除且是奇數（如 $x = 3$）$\implies$ **真 (True)**。
  - 結論：存在自然數既是偶數又是奇數 $\implies$ **假 (False)！**
- **結論**：成功在數學模型中確立反例，**論證形式無效 (Invalid)**。

---

## 二、 微型論域展開式短真值表證偽法 (Ex 8-3, 期末小考 6)

### 題目：$(\exists x)(Ax \rightarrow Bx),\ (x)[(Ax \land Bx) \rightarrow Cx] \vdash (x)Cx$

1. **設定微型論域**：$\text{Domain} = \{a, b\}$。
2. **寫出命題展開式**：
   - 前提 1 展開：$(Aa \rightarrow Ba) \lor (Ab \rightarrow Bb)$
   - 前提 2 展開：$[(Aa \land Ba) \rightarrow Ca] \land [(Ab \land Bb) \rightarrow Cb]$
   - 結論展開：$Ca \land Cb$
3. **強制設定反例賦值**：
   - 令結論為假：取 $V(Ca) = F,\ V(Cb) = F$。
   - 令前提 1 為真：取 $V(Aa) = T,\ V(Ba) = T \implies Aa \rightarrow Ba = T$。
   - 帶入前提 2 檢驗：若 $Aa \land Ba = T$ 且 $Ca = F$，則 $(Aa \land Ba) \rightarrow Ca = F$（衝突！）。
   - **調整賦值**：
     - 改取 $V(Aa) = F \implies Aa \rightarrow Ba = T$（前提 1 真）；且 $Aa \land Ba = F \implies (Aa \land Ba) \rightarrow Ca = T$。
     - 同理取 $V(Ab) = F \implies (Ab \land Bb) \rightarrow Cb = T$。
4. **成功構造反例賦值**：
   $$\text{Domain}=\{a, b\},\ V(Aa)=F,\ V(Ab)=F,\ V(Ca)=F,\ V(Cb)=F$$
   在此模型下，兩前提皆為真，但結論 $Ca \land Cb$ 為假！
5. **裁決結論**：**論證形式無效**。

---

## 相關知識鏈結

- 語意理論：[[述詞邏輯語意學與無效性證明]]
- 模型技術：[[展開式與有數量化]]
- 知識地圖：[[邏輯學知識體系地圖]]
