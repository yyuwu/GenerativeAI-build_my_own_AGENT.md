---
title: 自然演繹法
aliases: [Natural Deduction, 演繹證明法, 18條推論規則]
category: methods
tags:
  - 演繹證明
  - 命題邏輯
  - 證明方法
  - 推論規則
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch04_演繹證明_18條推論與等值規則.md]]"
  - "[[raw/lectures/ch05_條件證法與間接證法及後設邏輯.md]]"
---

# 自然演繹法 (Natural Deduction)

**自然演繹法**是現代符號邏輯中最核心的語法推導系統。相較於真值表法，自然演繹法能避免指數級膨脹的真值列，並精準模擬人類合理的推論步調。

---

## 1. 兩大規則體系之根本區別 (Implication vs. Replacement)

自然演繹系統由 **8 條單向推論規則** 與 **10 條雙向等值規則** 構成，兩者在使用權限上有極其嚴格的劃分：

| 比較維度 | 8 條蘊涵推論規則 (Rules of Inference) | 10 條等值置換規則 (Rules of Replacement) |
| :--- | :--- | :--- |
| **推論方向** | **單向推導 ($\vdash$)**：只能由前提推導結論，不可反推。 | **雙向等值 ($::$)**：左右式完全等價，可互換。 |
| **作用範圍** | **只能運用於「整列語句（Whole line）」！** | **可運用於「局部子句（Any subformula）」！** |
| **代表規則** | MP, MT, DS, HS, Simp, Conj, Add, CD | DN, DeM, Comm, Assoc, Dist, Contra, Impl, Exp, Taut, Equiv |

> [!CAUTION]
> **致命禁忌**：絕不可將單向推論規則應用於語句的區域性子句！例如：
> - 從 $(A \land B) \lor C$ 試圖用 Simp 推導出 $A \lor C$ 是**完全無效的錯誤推論**！
> - 只有等值規則（如 DeM）才能在括弧內外自由進行局部替換。

---

## 2. 自然演繹 18 條核心規則總覽

### 2.1 8 條單向推論規則 (Implicational Rules)
1. **[[假言推理_Modus_Ponens|MP (Modus Ponens)]]**：$p \rightarrow q,\ p \vdash q$
2. **[[否定後項_Modus_Tollens|MT (Modus Tollens)]]**：$p \rightarrow q,\ \neg q \vdash \neg p$
3. **[[選言三段論_Disjunctive_Syllogism|DS (Disjunctive Syllogism)]]**：$p \lor q,\ \neg p \vdash q$（或否定 $q$ 導出 $p$）
4. **[[假言三段論_Hypothetical_Syllogism|HS (Hypothetical Syllogism)]]**：$p \rightarrow q,\ q \rightarrow r \vdash p \rightarrow r$
5. **[[簡化律與連言律_Simp_and_Conj|Simp (Simplification)]]**：$p \land q \vdash p$（或導出 $q$）
6. **[[簡化律與連言律_Simp_and_Conj|Conj (Conjunction)]]**：$p,\ q \vdash p \land q$
7. **[[附加律與兩難推論_Add_and_CD|Add (Addition)]]**：$p \vdash p \lor q$
8. **[[附加律與兩難推論_Add_and_CD|CD (Constructive Dilemma)]]**：$p \lor q,\ p \rightarrow r,\ q \rightarrow s \vdash r \lor s$

### 2.2 10 條雙向等值規則 (Replacement Rules)
9. **DN (Double Negation)**：$p :: \neg\neg p$
10. **[[笛摩根定律_DeMorgans_Laws|DeM (DeMorgan's Theorem)]]**：$\neg(p \land q) :: \neg p \lor \neg q$；$\neg(p \lor q) :: \neg p \land \neg q$
11. **[[分配律與結合律_Dist_and_Assoc|Comm (Commutation)]]**：$p \lor q :: q \lor p$；$p \land q :: q \land p$
12. **[[分配律與結合律_Dist_and_Assoc|Assoc (Association)]]**：$p \lor (q \lor r) :: (p \lor q) \lor r$；$p \land (q \land r) :: (p \land q) \land r$
13. **[[分配律與結合律_Dist_and_Assoc|Dist (Distribution)]]**：$p \land (q \lor r) :: (p \land q) \lor (p \land r)$；$p \lor (q \land r) :: (p \lor q) \land (p \lor r)$
14. **[[實質蘊涵律與異質換位_Impl_and_Contra|Contra (Contraposition)]]**：$p \rightarrow q :: \neg q \rightarrow \neg p$
15. **[[實質蘊涵律與異質換位_Impl_and_Contra|Impl (Material Implication)]]**：$p \rightarrow q :: \neg p \lor q$
16. **[[輸出入律與重言律_Exp_and_Taut|Exp (Exportation)]]**：$(p \land q) \rightarrow r :: p \rightarrow (q \rightarrow r)$
17. **[[輸出入律與重言律_Exp_and_Taut|Taut (Tautology)]]**：$p :: p \land p$；$p :: p \lor p$
18. **[[實質等值律_Material_Equivalence|Equiv (Equivalence)]]**：$p \leftrightarrow q :: (p \rightarrow q) \land (q \rightarrow p)$；$p \leftrightarrow q :: (p \land q) \lor (\neg p \land \neg q)$

---

## 3. 六大證明解題戰略心法 (Proof Strategies)

1. **結構模式匹配**：留心重覆出現的子句，優先思考能否運用 MP, MT, DS, HS。
2. **善用短小語句**：短句是最佳推論槓桿，若能由前提推出單一字元短句，務必儘快導出。
3. **從結論逆向倒推 (Work Backward)**：檢視結論的主連接詞：
   - 結論若為條件句，優先考慮用 CP 或 HS 倒推。
   - 結論若為連言，分別推導兩個連言肢再用 Conj。
4. **引入新訊息**：若結論中出現前提完全沒有的新原子語句，**必須大膽使用 Add 規則引進**。
5. **消去多餘中間項**：若某語句僅出現一次且結論中不需要它，通常是多餘的，設法運用 HS、Dist 或 Simp 割離。
6. **選言與條件互化**：遇到條件句與選言混雜無從著手時，使用 Impl 統一其邏輯結構。

---

## 4. 進階推論方法（完備性所必需）

單靠 18 條規則無法證明零前提定理（如恆真句），為達成系統的[[後設邏輯_健全性與完備性|完備性]]，必須擴充：
- **[[條件證明法_Conditional_Proof|條件證明法 (CP)]]**：針對條件句假設前件推導後件。
- **[[間接證明法_Indirect_Proof|間接證明法 (IP)]]**：歸謬法，假設否定式推導矛盾。
- **簡化替代系統**：[[引進與消去規則系統]]（Gentzen 風格 11 條規則）。

---

## 5. 相關鏈結

- 語意學對照：[[真值表判定法]]
- 實戰範例：[[ex_001_基本演繹推導與有效性判定]]
- 知識地圖：[[邏輯學知識體系地圖]]
