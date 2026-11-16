---
title: 習題解析 Ch. 2 - 語句符號化與真值函應判準
aliases: [Exercise 2-7, Exercise 2-10, 符號化習題]
category: exercises
tags:
  - 習題詳解
  - 語句邏輯
  - 符號化
  - 真值函應
updated: 2026-11-17
sources:
  - "[[raw/problem_sets/exercises_ch02_符號化.md]]"
---

# 習題解析 Ch. 2：語句符號化與真值函應判準

本篇精選第二章（Exercise 2-7, 2-10）關於自然語言符號化、原子句 vs 複合句判定，以及非真值函應算子的檢驗重點。

---

## 一、 符號化實戰精選 (Exercise 2-7)

| 原文日常語句 | 邏輯符號化 | 解構分析重點 |
| :--- | :---: | :--- |
| If nothing is perfect, then I can’t be blamed for my mistakes. | $N \rightarrow \neg B$ | 標準條件句，後項帶有否定號。 |
| $E$ 僅當不是 $M$ 且不是 $B$ | $E \rightarrow (\neg M \land \neg B)$ | "Only if" 引導必要條件（後件），"neither M nor B" 譯為 $\neg M \land \neg B$。 |
| 不會既 $S$ 又 $G$，除非 $\neg D$ | $\neg(S \land G) \lor D$ 或 $\neg D \rightarrow \neg(S \land G)$ | "Not both" 為 $\neg(S \land G)$；"Unless" 譯為選言或否定前件之條件句。 |
| $(T \land S)$ 意味著 $N$ 若且唯若 $D$ | $(T \land S) \rightarrow (N \equiv D)$ | 主連接詞為條件句，後件為雙條件句（實質等值）。 |

---

## 二、 概念與哲學問答 (Exercise 2-10)

### Q1: 為什麼不能用單一字母 $P$ 來縮寫否定句「George 不是公眾人物」？
> **答案**：因為 $P$ 是原子語句常元。在語法學上，原子語句不含任何邏輯運算子。若用 $P$ 代表否定句，會**遮蔽該句子內在的否定邏輯結構**，導致後續演繹時無法套用如 DN、MT、DS 等推論規則。應符號化為 $\neg P$。

### Q2: 為什麼算子「眾所周知 (It is well known that ...)」不是真值函應的？
> **答案**：因為複句真值無法單由成分句的真假唯一決定！
- 「$2 + 2 = 4$」為真 $\implies$「眾所周知 $2+2=4$」為真 (T)。
- 「小明暗戀小華」事實上為真 $\implies$「眾所周知小明暗戀小華」事實上為假 (F)。
- 兩者成分句皆真，但加上前綴後一真一假，違背了[[真值函應與邏輯連接詞|真值函應原則]]。

### Q3: Lady Gaga 經典句子比較：原子句 vs. 複合句
1. **「Lady Gaga 與 Stefani Joanne 都是著名公眾人物」**：
   - $\implies$ **複合句 (Compound)**。因為 "and" 在此並無「共同行動」之意，可無損拆解為兩句獨立陳述的連言。
2. **「Lady Gaga 與 Stefani Joanne 是終生摯友」**：
   - $\implies$ **原子句 (Atomic)**。因為 "and" 表達的是兩人間的**相互二元關係**（是朋友）。若硬拆成「她是朋友且她是朋友」則失去原本語意。

---

## 相關知識鏈結

- 概念體系：[[真值函應與邏輯連接詞]]、[[自然語言翻譯與充要條件]]
- 形式結構：[[語句形式與取代實例]]
