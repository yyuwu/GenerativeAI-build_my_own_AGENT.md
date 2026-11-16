---
title: 習題解析 Ch. 7 - 述詞邏輯符號化與量詞陷阱
aliases: [Exercise 7, 述詞符號化習題, 部分否定與全部否定]
category: exercises
tags:
  - 習題詳解
  - 述詞邏輯
  - 符號化
  - 否定範圍
updated: 2026-11-17
sources:
  - "[[raw/problem_sets/exercises_ch07_述詞符號化.md]]"
  - "[[raw/problem_sets/quiz_述詞邏輯小考_05_06_07.md]]"
---

# 習題解析 Ch. 7：述詞邏輯符號化與量詞陷阱

本篇精選第七章及期末小考關於全稱量詞、存在量詞、部分否定 vs. 全部否定、自然語言隱含全稱以及複合詞劃分的核心考點。

---

## 一、 部分否定 (Not all) vs. 全部否定 (No / None)

這是述詞邏輯期末考最致命的易錯點：

| 日常英文表述 | 中文嚴格語意 | 錯誤翻譯 | 正確邏輯符號化 |
| :--- | :--- | :---: | :---: |
| **All elephants are not protected.** | **並非**所有大象都被保護（部分否定）。 | $(x)(Ex \rightarrow \neg Px)$<br>(成了「沒有大象受保護」) | **$\neg(x)(Ex \rightarrow Px)$**<br>$\equiv (\exists x)(Ex \land \neg Px)$ |
| **All that glitters is not gold.** | 發光的**不全都是**金子（部分否定）。 | $(x)(Gx \rightarrow \neg Lx)$ | **$\neg(x)(Gx \rightarrow Lx)$** |
| **No doctors are moneygrubbers.** | 沒有任何醫生貪財（全部否定）。 | $\neg(x)(Dx \rightarrow Mx)$ | **$(x)(Dx \rightarrow \neg Mx)$**<br>$\equiv \neg(\exists x)(Dx \land Mx)$ |

> **判準指引 (7-11 詳解)**：
> 在日常英語中，“All S are not P” 通常意指 “Not all S are P”。若翻為全部否定 $(x)(Sx \rightarrow \neg Px)$，只要存在一隻受保護的大象，前件便為假，使得全句「瑣碎地真 (trivially true)」。因此必須仔細辨析說話者的語用意圖。

---

## 二、 複合專用名詞不可擅自拆解

- **題目**：「有些職業運動員既會踢足球又會打棒球。」
  - **正確翻譯**：$(\exists x)[Px \land (Fx \land Bx)]$（其中 $Px$ =「$x$ 是職業運動員」）。
  - **錯誤拆解**：$(\exists x)[(Px \land Ax) \land (Fx \land Bx)]$（將 $Px$ 拆為「專業人士」與「運動員」）。
  - **原因**：合庫棒球隊的業餘選手是運動員也是專業人士，但他不是「職業運動員」。

---

## 三、 自然語言隱含的時間與全稱概括

- **「會叫的狗不咬人。」**：
  $$(x)[(Dx \land Kx) \rightarrow \neg(\exists y)(Ty \land Bxy)]$$
  （任何一隻吠叫的狗，在任何時間都不會咬人）。
- **「天下沒有白吃的午餐。」**：
  $$\neg(\exists x)(Lx \land Fx) \iff (x)(Lx \rightarrow \neg Fx)$$

---

## 相關知識鏈結

- 語法理論：[[個體_述詞與量詞]]、[[對當方陣與範恩圖]]
- 雙向轉換：[[量詞否定規則_QN]]
- 知識地圖：[[邏輯學知識體系地圖]]
