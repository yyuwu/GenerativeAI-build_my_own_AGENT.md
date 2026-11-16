# Chapter 5 習題與解答 (Conditional & Indirect Proofs)

## Ex 5-1: 條件證法 (CP)
### (9)
1. $R \rightarrow (L \land S)$ (p)
2. $(L \lor M) \rightarrow P$ (p)  /∴ $\neg P \rightarrow \neg R$
3. | $R$ (AP)  /∴ $P$
4. | $L \land S$ (1, 3 MP)
5. | $L$ (4 Simp)
6. | $L \lor M$ (5 Add)
7. | $P$ (2, 6 MP)
8. $R \rightarrow P$ (3-7 CP)
9. $\neg P \rightarrow \neg R$ (8 Contra)

---

## Ex 5-3: 間接證法 (IP)
### (5)
1. $A \rightarrow \neg B$ (p)
2. $B \lor C$ (p)
3. $A \lor C$ (p)  /∴ $C$
4. | $\neg C$ (AP，求證矛盾)
5. | $A$ (3, 4 DS)
6. | $\neg B$ (1, 5 MP)
7. | $C$ (2, 6 DS)
8. | $C \land \neg C$ (4, 7 Conj，矛盾！)
9. $C$ (4-8 IP)

---

## Ex 5-4: 直接證法 vs. IP 對比
### (1) 前提：$A \lor B,\ C \rightarrow A,\ C \lor (B \land D)$；目標：$B$
- **不使用 IP（13 步，依賴 Dist, HS, Taut）**：
  4. $(C \lor B) \land (C \lor D)$ (3 Dist)
  5. $C \lor B$ (4 Simp)
  ...
  10. $\neg B \rightarrow B$ (1, 9 HS)
  13. $B$ (12 Taut)
- **使用 IP（僅 10 步，極速推導）**：
  4. | $\neg B$ (AP)  /∴ $B$
  5. | $\neg A$ (1, 4 DS)
  6. | $\neg C$ (2, 5 MT)
  7. | $B \land D$ (3, 6 DS)
  8. | $B$ (7 Simp)
  9. | $B \land \neg B$ (4, 8 Conj)
  10. $B$ (4-9 IP)

---

## Ex 5-6: 零前提定理證明 (Zero-Premise Deductions)
### (5) 證明定理：$(A \lor B) \rightarrow [C \rightarrow (A \lor B)]$
1. | $A \lor B$ (AP)  /∴ $C \rightarrow (A \lor B)$
2. | $(A \lor B) \lor \neg C$ (1 Add)
3. | $\neg C \lor (A \lor B)$ (2 Comm)
4. | $C \rightarrow (A \lor B)$ (3 Impl)
5. $(A \lor B) \rightarrow [C \rightarrow (A \lor B)]$ (1-4 CP)

---

## Ex 5-7: 演繹證明前提不一致
### (5) 前提：$A \rightarrow (B \rightarrow C),\ \neg(\neg A \lor C),\ \neg B$
4. $\neg\neg A \land \neg C$ (2 DeM)
5. $A \land \neg C$ (4 DN)
6. $A$ (5 Simp)
7. $B \rightarrow C$ (1, 6 MP)
8. $\neg C$ (5 Simp)
9. $\neg B$ (7, 8 MT)
10. $B \land \neg B$ (3, 9 Conj，成功導出矛盾式，證畢前提不一致！)

---

## Ex 5-8: 新規則添加評估
(1) 評估規則：$p \lor (q \lor r) :: r \lor (q \lor p)$
- **結論**：可以添加進推論規則。因為藉由結合律與交換律，可證明 $[p \lor (q \lor r)] \equiv [r \lor (q \lor p)]$ 為**零前提定理**，左右雙向保真。
(3) 評估規則：$p \rightarrow (q \rightarrow r) :: r \rightarrow (q \rightarrow p)$
- **結論**：**不可以添加**！反例：當 $P=F, Q=T, R=T$ 時，前式為 $T$ 但後式為 $F$。該推論形式無效。
(5) 評估規則：$p \rightarrow q \vdash \neg(\neg q \rightarrow p)$
- **結論**：**不可以添加**！反例：當 $P=T, Q=T$ 時，前式為 $T$，但後式 $\neg(\neg T \rightarrow T) = \neg(F \rightarrow T) = \neg T = F$。推論無效。
