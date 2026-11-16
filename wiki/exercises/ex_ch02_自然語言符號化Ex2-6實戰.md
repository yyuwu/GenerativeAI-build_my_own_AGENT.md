---
title: 習題解析 Ch. 2 - 自然語言符號化 Exercise 2-6 實戰
aliases: [Exercise 2-6, 課本符號化實戰, 條件句與Unless翻譯]
category: exercises
tags:
  - 習題詳解
  - 語句邏輯
  - 符號化
  - 充要條件
updated: 2026-11-17
sources:
  - "[[raw/lectures/supplement_自然語言翻譯技巧與Ex2-6.md]]"
---

# 習題解析 Ch. 2：自然語言符號化 Exercise 2-6 實戰

本篇完整收錄課本第 45 頁 Exercise 2-6 的 12 道經典符號化題目與詳解，精確剖析日常語言中 "if"、"only if"、"unless" 與 "neither nor" 的邏輯轉換。

---

## 符號常元對照表 (Key)
- $A$: Art attends class.（阿圖出席上課）
- $G$: Art graduates.（阿圖畢業）
- $H$: Art completes his homework.（阿圖完成作業）
- $L$: Art does well in logic.（阿圖邏輯成績優異）
- $M$: Art does well in math.（阿圖數學成績優異）
- $P$: Art does well in philosophy.（阿圖哲學成績優異）
- $T$: Art pays tuition.（阿圖繳交學費）
- $W$: Art does well in all his classes.（阿圖所有課程皆優異）

---

## Exercise 2-6 題目與標準解答

| 題號 | 自然語言原文 | 邏輯符號化 | 核心語法與充要條件剖析 |
| :---: | :--- | :---: | :--- |
| **1** | Art does not do well in either logic or math. | $\neg(L \lor M)$ 或 $\neg L \land \neg M$ | 「兩者皆不」，否定選言等價於連言否定 (DeM)。 |
| **2** | If Art completes his homework, he does well in both logic and math. | $H \rightarrow (L \land M)$ | 標準條件句，後件為連言。 |
| **3** | If Art does not complete his homework, he does well in neither logic nor math. | $\neg H \rightarrow (\neg L \land \neg M)$ | 前件否定，後件為 "neither nor"。 |
| **4** | If Art does well in logic or math, he graduates. | $(L \lor M) \rightarrow G$ | 選言為充分條件（前件）。 |
| **5** | Art graduates only if he does well in logic or math. | $G \rightarrow (L \lor M)$ | **"Only if" 引導必要條件（後件）**，不可顛倒！ |
| **6** | If Art neither pays tuition nor attends classes, he does not graduate. | $(\neg T \land \neg A) \rightarrow \neg G$ | 前件為 "neither nor"，後件為否定。 |
| **7** | Art does well in logic if he completes his homework and attends class. | $(H \land A) \rightarrow L$ | **"if" 引導充分條件（前件）**。 |
| **8** | Art does well in logic only if he either completes his homework or attends class. | $L \rightarrow (H \lor A)$ | **"only if" 引導必要條件（後件）**。 |
| **9** | If Art pays his tuition, he graduates, unless he doesn’t attend class. | $T \rightarrow (A \rightarrow G)$ 或 $(T \land A) \rightarrow G$ | 複合條件句嵌套或利用 Unless 轉化為附加前件。 |
| **10** | Art does well in all his classes if he does well in logic and philosophy. | $(L \land P) \rightarrow W$ | $L \land P$ 是 $W$ 的充分條件。 |
| **11** | Art does well in all his classes unless he doesn’t do well in logic or philosophy. | $(\neg L \lor \neg P) \rightarrow \neg W$ 或 $W \lor (\neg L \lor \neg P)$ | Unless 標準轉為 $\neg A \rightarrow B$ 或 $A \lor B$。 |
| **12** | Art does well in all his classes only if he does well in logic, philosophy, and math. | $W \rightarrow (L \land P \land M)$ | $L \land P \land M$ 是 $W$ 的必要條件（後件）。 |

---

## 相關知識鏈結

- 語意理論：[[自然語言翻譯與充要條件]]、[[真值函應與邏輯連接詞]]
- 哲學深究：[[實質條件句的哲學爭論與證成]]
- 知識地圖：[[邏輯學知識體系地圖]]
