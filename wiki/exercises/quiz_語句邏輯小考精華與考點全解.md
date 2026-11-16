---
title: 語句邏輯小考精華與考點全解 (Weekly Quizzes Master Review)
aliases: [小考全解, 語句邏輯小考, 小考1至7解答, 期中複習精華]
category: exercises
tags:
  - 習題詳解
  - 小考精華
  - 語句邏輯
  - 考點全解
  - 自然演繹證明
updated: 2026-11-17
sources:
  - "[[raw/problem_sets/quiz_01_論證有效性與一致性是非題.md]]"
  - "[[raw/problem_sets/quiz_02_語句邏輯符號化.md]]"
  - "[[raw/problem_sets/quiz_03_真值表檢驗有效性與一致性.md]]"
  - "[[raw/problem_sets/quiz_04_自然演繹法18條規則推導.md]]"
  - "[[raw/problem_sets/quiz_05_自然演繹法多重證法演練.md]]"
  - "[[raw/problem_sets/quiz_06_推論規則證明定理_CP_IP.md]]"
  - "[[raw/problem_sets/quiz_07_語句邏輯綜合觀念選擇題.md]]"
---

# 語句邏輯小考精華與考點全解 (Weekly Quizzes Master Review)

本篇整合課堂 7 次「語句邏輯小考」的全部核心試題，涵蓋論證是非觀念、高階自然語言符號化、短真值表檢驗、18 條規則一題多解、CP/IP 定理推導與概念單選題。

---

## 第一單元：論證有效性與集合一致性是非觀念（小考 1）

1. **前提與結論都真的論證不必然有效**：
   - 清華在新竹 (T)，台大在台北 (T) $\vdash$ 清華在新竹 (有效)。
   - 清華在新竹 (T) $\vdash$ 台大在台北 (T)（無邏輯關聯，無效！）。
2. **結論為假的有效論證，其前提「至少有一為假」，不必然全假**。
3. **一致的集合所有語句可以全部為假**（只要邏輯上有可能同真即可，如 $\{\text{清華在澎湖},\ \text{台大在金門}\}$）。
4. **前提集不一致的論證必然是有效的**（平凡有效 Trivially Valid，因為在邏輯上絕不可能出現「前提全真而結論為假」）。
5. **結論為假的有效論證，其前提集可以一致，也可以不一致**。

---

## 第二單元：自然語言複雜符號化五大經典句型（小考 2）

1. **貨幣供給與通貨膨脹（De Morgan 轉換）**：
   - 「如果我們不控制貨幣供給或不打破石油輸出國家組織的力量，我們將無法控制通貨膨脹。」
   - $\implies (\neg M \lor \neg O) \rightarrow \neg I \iff \neg(M \land O) \rightarrow \neg I \iff I \rightarrow (M \land O)$
2. **小明畢業成績（嵌套條件句）**：
   - 「如果小明有好的畢業成績，那麼他就會找到好工作且賺很多錢——假如他沒有追求其他目標的話。」
   - $\implies G \rightarrow (\neg O \rightarrow (J \land L)) \iff (G \land \neg O) \rightarrow (J \land L)$
3. **除非（Unless）與政府赤字**：
   - 「如果我們增加稅收並消除政府浪費支出，那麼，除非有自然的大災害，否則赤字將會降低。」
   - $\implies (T \land S) \rightarrow (N \lor D) \iff (T \land S) \rightarrow (\neg N \rightarrow D)$
4. **兩者並非皆是（Not both ... but ...）**：
   - 「並非小明與小華兩者都是笨蛋，但小芬卻是。」
   - $\implies \neg(A \land B) \land C \iff (\neg A \lor \neg B) \land C$

---

## 第三單元：短真值表檢驗有效性與集合一致性（小考 3）

- **檢驗論證無效性核心心法**：強制設定結論為假，嘗試為前提賦值使全為真。
  - 例：$P \rightarrow Q,\ (Q \land R) \rightarrow P \vdash \neg Q$
  - 取 $V(Q)=T, V(P)=T, V(R)=T$，所有前提均為真且結論 $\neg Q = F$ 成功，判定**無效**！
- **檢驗集合一致性核心心法**：尋找至少一組賦值使全體成員同時為真。
  - 集合 $\{B \rightarrow A,\ C \rightarrow B,\ \neg C \land A\}$ 在 $V(A)=T, V(C)=F$ 時所有語句恆真，判定**一致**。

---

## 第四單元：18 條規則自然演繹一題多解精華（小考 4 & 5）

### 經典難題：$(A \land B) \lor (C \land D),\ \neg C \vdash A$
- **解法一（利用 DeM 與 Add）**：
  由 $\neg C$ 得 $\neg C \lor \neg D$ (Add) $\to \neg(C \land D)$ (DeM) $\to A \land B$ (DS) $\to A$ (Simp)。
- **解法二（利用 Dist 分配律）**：
  直接展開為 $[(A \land B) \lor C] \land [(A \land B) \lor D]$ (Dist) $\to (A \land B) \lor C$ (Simp) $\to A \land B$ (DS) $\to A$ (Simp)。

---

## 第五單元：條件證明 (CP) 與 間接證明 (IP) 證明定理（小考 6）

### 經典定理：$\vdash A \rightarrow (\neg A \rightarrow B)$（假前項保證條件句恆真）
- **解法一（嵌套 CP）**：假設 $A$，再假設 $\neg A$，由 $\neg A \lor B$ (Add) 與 $\neg A$ 行 DS 得 $B$，消去得 $\neg A \rightarrow B$，再消去得全句。
- **解法二（IP 歸謬法）**：假設否定式 $\neg[A \rightarrow (\neg A \rightarrow B)]$，展開為 $A \land (\neg A \land \neg B)$，提取 $A \land \neg A$ 矛盾式，由 IP 解除假設。
- **解法三（DN + Impl 極速代數法）**：由假設 $A$ 得 $\neg\neg A$，加項 $\neg\neg A \lor B$ (Add)，化為 $\neg A \rightarrow B$ (Impl)，消去 AP 即得定理。

---

## 第六單元：語句邏輯十大核心觀念單選避坑指南（小考 7）

| 考點核心 | 正確結論 | 深度解析與反例 |
| :--- | :---: | :--- |
| **前提全真的有效論證結論** | **必然為真** | 健全論證的定義，不可能前真後假。 |
| **事實上無「前真後假」之論證** | **無法判定** | 有效性取決於形式結構。$A \vdash B$ 事實上若碰巧皆真，形式依然無效。 |
| **結論為假的有效論證前提** | **無法判定** | 前提至少有一假，但前提集可以一致，也可以不一致。 |
| **語句形式的代換限制** | **不可違背變元綁定** | $A \lor (A \rightarrow B)$ 絕不具有 $p \lor (p \rightarrow p)$ 的形式。 |
| **含未知變元的短路求值** | **看後件或前件特徵** | 若後件已確定為 $T$（如 $R \rightarrow B$，已知 $B=T$），整個條件句恆為真！ |
| **取代實例的結構複雜度** | **絕不可比原形式簡單** | 取代只能作用於變元，不能用單一常元 $A$ 代換複合結構 $q \rightarrow r$。 |
| **論證形式的多重性** | **有效論證必有無效形式** | 任何有效論證 $A_1 \dots A_n \vdash C$ 必有無效形式 $p_1 \dots p_n \vdash q$；但它**至少具有一個有效的展開形式**。 |
| **無效論證形式的取代實例** | **無法判定** | 無效形式 $p \vdash q$ 的實例可以是無效論證（$A \vdash B$），也可以是有效論證（$A \vdash A \lor \neg A$）。 |

---

## 相關知識鏈結

- 語意理論：[[真值表判定法]]、[[實質條件句的哲學爭論與證成]]
- 推論方法：[[自然演繹法_Natural_Deduction]]、[[條件證明法_Conditional_Proof]]、[[間接證明法_Indirect_Proof]]
- 考試總複習：[[exam_期中考精華詳解與觀念避坑]]
- 知識地圖：[[邏輯學知識體系地圖]]
