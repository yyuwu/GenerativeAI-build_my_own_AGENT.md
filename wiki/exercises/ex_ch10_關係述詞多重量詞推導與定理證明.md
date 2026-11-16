---
title: 習題解析 Ch. 10 - 關係述詞、多重量詞推導與定理證明
aliases: [Exercise 10, 多重量詞證明, Q17定理證明, 關係述詞習題]
category: exercises
tags:
  - 習題詳解
  - 關係述詞
  - 多重量詞
  - 定理證明
updated: 2026-11-17
sources:
  - "[[raw/problem_sets/exercises_ch10_關係述詞與多重量詞證明.md]]"
---

# 習題解析 Ch. 10：關係述詞、多重量詞推導與定理證明

本篇精選第十章關於多元關係符號化、多重量詞的無效性證偽、高階演繹證明以及全稱/存在移位定理（Q17, Q18）的完整零前提證明。

---

## 一、 自然語言深層關係改寫 (Paraphrasing Ex 10-4)

日常哲理諺語通常包含隱含的「時間」與「空間」全稱概括：

1. **「人的工作永遠做不完。」**
   - **深層改寫**：每個人在任何時間都有某些工作是做不完的。
   - **符號化**：$(x)\{Px \rightarrow (y)[Ty \rightarrow (\exists z)(Wzx \land \neg Dzxy)]\}$
2. **「罪惡無時不有、無所不在。」**
   - **深層改寫**：對任何時間與任何地點，都存在著某種罪惡。
   - **符號化**：$(x)(y)[(Tx \land Py) \rightarrow (\exists z)(Sz \land Azxy)]$

---

## 二、 多重量詞無效性數學反例 (Ex 10-8)

### 題目：$(\exists x)(y)Fxy \vdash (x)(y)Fyx$
- **反例模型（自然數乘法單位元素）**：
  - $\text{Domain} = \{\text{自然數 } 1, 2, 3 \dots\}$
  - $Fxy$: $x \cdot y = y$
- **檢驗**：
  - 前提：存在自然數 $x = 1$，對所有自然數 $y$ 滿足 $1 \cdot y = y$（前提**為真**）。
  - 結論：對所有自然數 $x, y$ 滿足 $y \cdot x = x$（例如 $2 \cdot 3 \neq 3$，結論**顯然為假**！）。
- **結論**：多重量詞的先後順序交換是**形式無效的**！

---

## 三、 定理 Q17 完整零前提演繹證明 (Ex 10-12 (13))

**目標定理**：$\vdash (x)(Fx \rightarrow P) \equiv [(\exists x)Fx \rightarrow P]$（其中命題 $P$ 不含自由變元 $x$）

```markdown
證明第一部分：(x)(Fx -> P) ⊃ [(∃x)Fx -> P]
1.  | (x)(Fx -> P)                     AP /∴ (∃x)Fx -> P
2.  | | (∃x)Fx                         AP /∴ P
3.  | | Fx                             2 EI (★引入全新變元 x)
4.  | | Fx -> P                        1 UI (★配合變元 x)
5.  | | P                              3, 4 MP
6.  | (∃x)Fx -> P                      2-5 CP
7.  (x)(Fx -> P) -> [(∃x)Fx -> P]      1-6 CP

證明第二部分：[(∃x)Fx -> P] ⊃ (x)(Fx -> P)
8.  | (∃x)Fx -> P                      AP /∴ (x)(Fx -> P)
9.  | | Fx                             AP /∴ P
10. | | (∃x)Fx                         9 EG
11. | | P                              8, 10 MP
12. | Fx -> P                          9-11 CP
13. | (x)(Fx -> P)                     12 UG (變元 x 具完全任意性！)
14. [(∃x)Fx -> P] -> (x)(Fx -> P)      8-13 CP

定理成立：
15. (x)(Fx -> P) ≡ [(∃x)Fx -> P]       7, 14 Conj, Equiv
Q.E.D.
```

---

## 相關知識鏈結

- 定理理論：[[量詞前綴移入移出定理_Q17_Q18]]
- 證明體系：[[述詞邏輯演繹證明法]]、[[條件證明法_Conditional_Proof]]
- 知識地圖：[[邏輯學知識體系地圖]]
