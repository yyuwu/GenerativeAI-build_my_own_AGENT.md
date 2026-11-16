---
title: 習題解析 Ch. 5 - 條件證法、間接證法與零前提定理
aliases: [Exercise 5, CP與IP習題, 零前提定理推導]
category: exercises
tags:
  - 習題詳解
  - 條件證明
  - 間接證明
  - 定理證明
updated: 2026-11-17
sources:
  - "[[raw/problem_sets/exercises_ch05_條件與間接證法.md]]"
---

# 習題解析 Ch. 5：條件證法、間接證法與零前提定理

本篇精選第五章高階推導技術，包括直接證法 vs. IP 的效率對比、零前提定理推導，以及證明前提不一致之標準解題套路。

---

## 一、 直接證法 vs. 間接證法 (IP) 效率大對決 (Ex 5-4)

**題目**：$A \lor B,\ C \rightarrow A,\ C \lor (B \land D) \vdash B$

### 對照 A：純用 18 條規則直接證明（繁複 13 步）
需要依賴分配律、質變換位律、假言三段論及重言律等多層轉換：
$$\dots \implies \neg B \rightarrow B \implies \neg\neg B \lor B \implies B \lor B \implies B$$

### 對照 B：採用間接證明法 IP（極速 10 步）
```markdown
1. A v B                       (前提)
2. C -> A                      (前提)
3. C v (B · D)                 (前提)  /∴ B

證明步驟：
4.  | ~B                       (AP，假設結論為假，求證矛盾)
5.  | A                        (1, 4 DS)
6.  | ~C                       (2, 5 MT)
7.  | B · D                    (3, 6 DS)
8.  | B                        (7 Simp)
9.  | B · ~B                   (4, 8 Conj，矛盾爆發！)
10. B                          (4-9 IP，成功解除假設)
Q.E.D.
```
> **戰略洞察**：當目標結論為單一短句（如 $B$），直接推導缺乏代數著力點時，**果斷假設 $\neg B$ 開啟 IP**，能立即獲得一個好用的短前提來觸發 DS 或 MT！

---

## 二、 零前提定理推導 (Ex 5-6)

**題目**：在沒有任何給定前提下，證明定理：
$$\vdash (A \lor B) \rightarrow [C \rightarrow (A \lor B)]$$

```markdown
證明步驟：
1. | A v B                     (AP 1，假設最外層前件)
2. | | (A v B) v ~C            (1 Add)
3. | | ~C v (A v B)            (2 Comm)
4. | | C -> (A v B)            (3 Impl)
5. (A v B) -> [C -> (A v B)]   (1-4 CP，消去所有 AP，形成零前提定理)
Q.E.D.
```

---

## 三、 演繹證明前提集合不一致 (Ex 5-7)

**題目**：證明前提集合 $\{A \rightarrow (B \rightarrow C),\ \neg(\neg A \lor C),\ \neg B\}$ 是不一致的。

```markdown
前提：
1. A -> (B -> C)               (前提)
2. ~(~A v C)                   (前提)
3. ~B                          (前提)

證明步驟：
4. ~~A · ~C                    (2 DeM)
5. A · ~C                      (4 DN)
6. A                           (5 Simp)
7. B -> C                      (1, 6 MP)
8. ~C                          (5 Simp)
9. ~B                          (3 重申)
10. B                          (7, 8 MT)
11. B · ~B                     (9, 10 Conj，成功導出顯然矛盾式！)
Q.E.D. 集合被嚴格證實為不一致！
```

---

## 相關知識鏈結

- 方法詳解：[[條件證明法_Conditional_Proof]]、[[間接證明法_Indirect_Proof]]
- 後設理論：[[後設邏輯_健全性與完備性]]
- 知識地圖：[[邏輯學知識體系地圖]]
