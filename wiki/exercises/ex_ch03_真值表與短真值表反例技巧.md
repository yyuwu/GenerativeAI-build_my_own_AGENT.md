---
title: 習題解析 Ch. 3 - 真值表與短真值表反例技巧
aliases: [Exercise 3, 短真值表習題, 矛盾與一致性檢驗]
category: exercises
tags:
  - 習題詳解
  - 語意學
  - 短真值表法
  - 反例構造
updated: 2026-11-17
sources:
  - "[[raw/problem_sets/exercises_ch03_真值表.md]]"
---

# 習題解析 Ch. 3：真值表與短真值表反例技巧

本篇精選第三章關於計算未知變元、形式層次拆解、短真值表快速判定有效性及集合一致性的核心題型。

---

## 一、 含未知變元的快速短路求值 (Ex 3-2)

當複合語句中含有未知真值的命題變元（如 $Q, R = ?$）時，善用**實質條件句與排中律的代數特徵**可極速解題：

1. **題目**：$\neg C \rightarrow (D \rightarrow Q)$，已知 $V(C)=F, V(D)=F$。
   - **解析**：在後件 $D \rightarrow Q$ 中，前項 $D$ 為假。根據實質條件句定義，假前項保證條件句必為真，故 $D \rightarrow Q = T$（不論 $Q$ 為何）。
   - 前件 $\neg C = T$；$T \rightarrow T = T$。
   - **答案**：**$V = T$**。
2. **題目**：$\neg[R \land \neg R]$，已知 $V(R) = ?$。
   - **解析**：$R$ 與 $\neg R$ 必然互為矛盾，其連言 $R \land \neg R$ 恆等於假 ($F$)。否定假命題必然為真。
   - **答案**：**$V = T$**。

---

## 二、 短真值表法判定有效性 (Ex 3-8, 3-10)

短真值表法藉由「強制假設反例存在（前提皆真且結論為假）」，以最小代價判定有效性：

### 示範 1：證明有效性（導出矛盾）
**論證**：$(A \land B) \rightarrow C,\ A \vdash B \rightarrow C$
1. 假設結論為假：$V(B \rightarrow C) = F \implies V(B) = T,\ V(C) = F$。
2. 假設前提皆為真：
   - 前提 2：$V(A) = T$。
   - 此時 $A \land B = T \land T = T$。
   - 帶入前提 1：前項為 $T$ 但後項 $C = F$，導致 $(A \land B) \rightarrow C = F$，與前提全真的假設產生**致命矛盾**！
3. **結論**：反例不可能存在，**論證有效 (Valid)**。

### 示範 2：證明無效性（成功構作反例賦值）
**論證**：$P \rightarrow Q,\ R \rightarrow S,\ R \lor Q \vdash P \lor S$
1. 假設結論為假：$V(P \lor S) = F \implies V(P) = F,\ V(S) = F$。
2. 嘗試為前提賦值使全為真：
   - 前提 1：$P \rightarrow Q$，因 $P = F$，不論 $Q$ 為何皆為真。取 $V(Q) = T$。
   - 前提 2：$R \rightarrow S$，因 $S = F$，為使全句真，必取 $V(R) = F$。
   - 檢驗前提 3：$R \lor Q = F \lor T = T$（成立！）。
3. 成功找到一組完整反例賦值：
   $$V(P) = F,\ V(Q) = T,\ V(R) = F,\ V(S) = F$$
4. **結論**：前提全真而結論為假，**論證無效 (Invalid)**。

---

## 三、 集合一致性檢測 (Ex 3-11)

**集合**：$\{B \rightarrow A,\ C \rightarrow B,\ \neg C \land A\}$
- 目標：尋找是否存在一組賦值使全體成員同時為真。
- 由 $\neg C \land A = T \implies V(C) = F,\ V(A) = T$。
- 帶入 $C \rightarrow B$：因 $C = F$，條件句自動為真。
- 帶入 $B \rightarrow A$：因後項 $A = T$，條件句自動為真。
- **結論**：當 $V(A)=T, V(C)=F, V(B)=\text{任意}$ 時，全體成員同時為真，故該集合為**一致 (Consistent)**。

---

## 相關知識鏈結

- 語意理論：[[真值表判定法]]、[[恆真句_矛盾句與適真句]]
- 判定本質：[[有效性與健全性]]、[[一致性與有效性檢測]]
