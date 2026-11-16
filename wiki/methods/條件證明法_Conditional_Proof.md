---
title: 條件證明法 (Conditional Proof)
aliases: [Conditional Proof, CP, 條件證法]
category: methods
tags:
  - 演繹證明
  - 證明方法
  - 假設推論
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch05_條件證法與間接證法及後設邏輯.md]]"
---

# 條件證明法 (Conditional Proof, CP)

**條件證明法 (CP)** 是自然演繹法中用於推導條件句（$P \rightarrow Q$）的強大證明技術。它藉由引入「暫時性假設」，突破了 18 條規則系統無法證明恆真句與特定有效論證的限制。

---

## 1. 核心推導理念

若欲證明結論形如 $P \rightarrow Q$：
1. **設定假設前提 (Assumed Premise, AP)**：暫時假定前件 $P$ 為真。
2. **在假設子作用域內推導**：結合已知前提與 $P$，逐步導出後件 $Q$。
3. **解除假設 (Discharge)**：一旦導出 $Q$，便關閉假設區間，正式斷定：**若 $P$ 成立，則 $Q$ 必成立**，即得到 $P \rightarrow Q$。

---

## 2. 標準排版格式與作用域封閉線

```markdown
前提：
1. A -> B                      (前提)
2. B -> C                      (前提)  /∴ A -> C

證明步驟：
3. | A                         (AP，假設前件，求證 C)
4. | B                         (1, 3 MP)
5. | C                         (2, 4 MP)
6. A -> C                      (3-5 CP，消去假設)
Q.E.D.
```

---

## 3. 使用 CP 的四大嚴格鐵律

> [!CAUTION]
> 1. **作用域隔離原則**：封閉線（直線區間）內由 AP 所推出的任何步驟，**在封閉線關閉後，絕對不可被封閉線外的後續步驟單獨引用**！
> 2. **所有假設必須全數解除**：證明完畢時，不可殘留任何未被 CP 或 IP 消去的 AP。
> 3. **封閉線不可交叉重疊**：多重假設可以**巢狀 (Nested)** 逐層包覆，或在完成一個 CP 後**並列**開啟另一個 CP，但絕不可錯位交叉。
> 4. **結論形式約束**：CP 解除假設後所得出的那一列，其結構必然是以該 AP 為前件的**條件句**。

---

## 4. 巢狀 CP (Nested CP) 示範

欲證明：$C \rightarrow D \vdash A \rightarrow [B \rightarrow (C \rightarrow D)]$
```markdown
1. C -> D                      (前提)  /∴ A -> [B -> (C -> D)]
2. | A                         (AP 1)
3. | | B                       (AP 2)
4. | | | C                     (AP 3)
5. | | | D                     (1, 4 MP)
6. | | C -> D                  (4-5 CP)
7. | B -> (C -> D)             (3-6 CP)
8. A -> [B -> (C -> D)]        (2-7 CP)
```

---

## 5. 相關鏈結

- 對偶方法：[[間接證明法_Indirect_Proof]]
- 證明體系：[[自然演繹法_Natural_Deduction]]
- 完備性證明：[[後設邏輯_健全性與完備性]]
- 替代簡約規則：[[引進與消去規則系統]]（$\supset I$）
