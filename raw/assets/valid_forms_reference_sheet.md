# 語句邏輯有效推論形式參考卡 (Valid Forms for Sentential Logic)

## 一、 8 條單向蘊涵推論規則 (Implicational Rules)
1. **Modus Ponens (MP)**:
   $$p \rightarrow q,\ p \vdash q$$
2. **Modus Tollens (MT)**:
   $$p \rightarrow q,\ \sim q \vdash \sim p$$
3. **Disjunctive Syllogism (DS)**:
   $$p \lor q,\ \sim p \vdash q \quad \text{或} \quad p \lor q,\ \sim q \vdash p$$
4. **Simplification (Simp)**:
   $$p \cdot q \vdash p \quad \text{或} \quad p \cdot q \vdash q$$
5. **Conjunction (Conj)**:
   $$p,\ q \vdash p \cdot q$$
6. **Hypothetical Syllogism (HS)**:
   $$p \rightarrow q,\ q \rightarrow r \vdash p \rightarrow r$$
7. **Addition (Add)**:
   $$p \vdash p \lor q$$
8. **Constructive Dilemma (CD)**:
   $$p \lor q,\ p \rightarrow r,\ q \rightarrow s \vdash r \lor s$$

---

## 二、 10 條雙向等值置換規則 (Replacement Rules)
9. **Double Negation (DN)**:
   $$p :: \sim\sim p$$
10. **DeMorgan’s Theorem (DeM)**:
    $$\sim(p \cdot q) :: (\sim p \lor \sim q)$$
    $$\sim(p \lor q) :: (\sim p \cdot \sim q)$$
11. **Commutation (Comm)**:
    $$(p \lor q) :: (q \lor p)$$
    $$(p \cdot q) :: (q \cdot p)$$
12. **Association (Assoc)**:
    $$[p \lor (q \lor r)] :: [(p \lor q) \lor r]$$
    $$[p \cdot (q \cdot r)] :: [(p \cdot q) \cdot r]$$
13. **Distribution (Dist)**:
    $$[p \cdot (q \lor r)] :: [(p \cdot q) \lor (p \cdot r)]$$
    $$[p \lor (q \cdot r)] :: [(p \lor q) \cdot (p \lor r)]$$
14. **Contraposition (Contra)**:
    $$(p \rightarrow q) :: (\sim q \rightarrow \sim p)$$
15. **Implication (Impl)**:
    $$(p \rightarrow q) :: (\sim p \lor q)$$
16. **Exportation (Exp)**:
    $$[(p \cdot q) \rightarrow r] :: [p \rightarrow (q \rightarrow r)]$$
17. **Tautology (Taut)**:
    $$p :: (p \cdot p)$$
    $$p :: (p \lor p)$$
18. **Equivalence (Equiv)**:
    $$(p \equiv q) :: [(p \rightarrow q) \cdot (q \rightarrow p)]$$
    $$(p \equiv q) :: [(p \cdot q) \lor (\sim p \cdot \sim q)]$$

---

## 三、 假設證明法 (Hypothetical Proof Methods)
- **Conditional Proof (CP)**:
  $$\begin{aligned}
  \rightarrow\ & p \quad (\text{AP} \ /∴ q) \\
  & \dots \\
  & q \\
  \hline
  & p \rightarrow q \quad \text{CP}
  \end{aligned}$$
- **Indirect Proof (IP)**:
  $$\begin{aligned}
  \rightarrow\ & \sim p \quad (\text{AP} \ /∴ p) \\
  & \dots \\
  & q \cdot \sim q \\
  \hline
  & p \quad \text{IP}
  \end{aligned}$$
