---
title: 附加律與建設性兩難 (Addition & Constructive Dilemma)
aliases: [Add, CD, 附加規則, 兩難推論, 建設性二難]
category: rules
tags:
  - 推論規則
  - 命題邏輯
  - 自然演繹法
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]"
---

# 附加律 (Add) 與 建設性兩難 (CD)

**附加律 (Add)** 與 **建設性兩難 (CD)** 是自然演繹推論中極具戰略價值的進階推論規則。

---

## 1. 附加律 (Addition, Add)

- **句法形式**：
  $$p \vdash p \lor q \quad \text{或} \quad p \vdash q \lor p$$
- **語意保真**：相容選言只要有一項為真，全句即為真。既然已知 $p$ 為真，附加任何任意語句 $q$ 所構成的選言必定為真。
- **核心戰略地位**：
  > **「新訊息引進器」**：若結論中出現了在任何前提中都**完全未曾出現過**的全新原子語句，**附加律 (Add) 是在演繹系統中合法引進該新變元的唯一合法途徑！**

---

## 2. 建設性兩難 (Constructive Dilemma, CD)

- **句法形式**：
  $$\begin{aligned}
  & p \lor q \\
  & p \rightarrow r \\
  & q \rightarrow s \\
  \hline
  \therefore\ & r \lor s
  \end{aligned}$$
- **規則特徵**：在 18 條規則體系中，**CD 是唯一需要消耗三個前提**的推論規則。
- **語意**：已知兩條路徑必擇其一（$p \lor q$），而第一條路通往 $r$，第二條路通往 $s$，故最終必然落入 $r$ 或 $s$。

---

## 3. 相關鏈結

- 推論規則：[[選言三段論_Disjunctive_Syllogism]]
- 證明框架：[[自然演繹法_Natural_Deduction]]
- 替代系統對應：[[引進與消去規則系統]]（$\lor I$）
