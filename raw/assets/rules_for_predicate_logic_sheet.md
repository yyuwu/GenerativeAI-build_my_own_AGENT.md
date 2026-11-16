# 述詞邏輯推論規則參考卡 (Rules for Predicate Logic Cheat Sheet)

## 1. Rule UI (Universal Instantiation)
$$(u)(\dots u \dots) \vdash (\dots w \dots)$$
**Provided**:
1. $(\dots w \dots)$ results from replacing each occurrence of $u$ free in $(\dots u \dots)$ with a $w$ that is either a constant or a variable free in $(\dots w \dots)$ (making no other changes).

---

## 2. Rule EI (Existential Instantiation)
$$(\exists u)(\dots u \dots) \vdash (\dots w \dots)$$
**Provided**:
1. $w$ is not a constant.
2. $w$ does not occur free previously in the proof.
3. $(\dots w \dots)$ results from replacing each occurrence of $u$ free in $(\dots u \dots)$ with a $w$ that is free in $(\dots w \dots)$ (making no other changes).

---

## 3. Rule UG (Universal Generalization)
$$(\dots u \dots) \vdash (w)(\dots w \dots)$$
**Provided**:
1. $u$ is not a constant.
2. $u$ does not occur free previously in a line obtained by **EI**.
3. $u$ does not occur free previously in an assumed premise that has not yet been discharged.
4. $(\dots w \dots)$ results from replacing each occurrence of $u$ free in $(\dots u \dots)$ with a $w$ that is free in $(\dots w \dots)$ (making no other changes) and there are no additional free occurrences of $w$ already contained in $(\dots u \dots)$.

---

## 4. Rule EG (Existential Generalization)
$$(\dots u \dots) \vdash (\exists w)(\dots w \dots)$$
**Provided**:
1. $(\dots w \dots)$ results from replacing **at least one** occurrence of $u$, where $u$ is a constant or a variable free in $(\dots u \dots)$ with a $w$ that is free in $(\dots w \dots)$ (making no other changes) and there are no additional free occurrences of $w$ already contained in $(\dots u \dots)$.

---

## 5. Rule QN (Quantifier Negation)
$$\begin{aligned}
(u)(\dots u \dots) &:: \sim(\exists u)\sim(\dots u \dots) \\
(\exists u)(\dots u \dots) &:: \sim(u)\sim(\dots u \dots) \\
(u)\sim(\dots u \dots) &:: \sim(\exists u)(\dots u \dots) \\
(\exists u)\sim(\dots u \dots) &:: \sim(u)(\dots u \dots)
\end{aligned}$$

---

## 6. Rule ID (Identity)
$$\begin{aligned}
& (\dots u \dots) \\
& u = w \quad (\text{or } w = u) \\
\hline
\therefore\ & (\dots w \dots)
\end{aligned}$$

---

## 7. Rule IR (Identity Reflexivity)
$$\vdash (x)(x = x)$$
