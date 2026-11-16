# 邏輯 (115上) 期中考解答 (Midterm Exam Solutions)

**日期**：2026/10/29  
**滿分**：100 分  

---

## 1. 是非題與理由/反例說明 (30%)

### (1) 「如果太陽從西邊升起來，我就請你吃飯。」這句話可以恰當地翻譯為實質條件句 (material conditional)。
- **Ans.：F**
- **理由**：因為「如果太陽從西邊升起來，我就請你吃飯。」是反事實條件句（Counterfactual Conditional），它其實所表達的語用語意（Pragmatic meaning）是：「我絕不會請你吃飯」。但是，如果把它翻譯成實質條件句，當前件（太陽從西邊升起）為假時，不論後件真假，整個條件句都恆為真。因此，反事實條件句根據其語用意義，不可以恰當地翻譯為邏輯的實質條件句。

### (2) 「小明不在家」的否定句是「小明在家」。
- **Ans.：F**
- **理由**：因為「小明不在家」（$\sim A$）的嚴格語法否定句是「並非小明不在家」（$\sim\sim A$）。雖然根據雙重否定律 (DN)，「小明在家」（$A$）在邏輯語意上等值於「並非小明不在家」（$\sim\sim A$），但是「小明在家」在語法形式上是肯定句，而「並非小明不在家」才是真正的否定句。

### (3) $p \supset \sim(q \cdot r)$ 是 $\sim B \supset \sim(\sim B \cdot B)$ 的一個語句形式。
- **Ans.：T**
- **理由**：因為 $\sim B \supset \sim(\sim B \cdot B)$ 是以 $\sim B$ 取代 $p \supset \sim(q \cdot r)$ 中所有出現的 $p$，以 $\sim B$ 取代 $q$，以 $B$ 取代 $r$ 所得的結果。所以，$\sim B \supset \sim(\sim B \cdot B)$ 是 $p \supset \sim(q \cdot r)$ 的一個取代實例，反之 $p \supset \sim(q \cdot r)$ 即為其語句形式。

### (4) 若一個語句集中的所有語句都同時為假，則此語句集是不一致的。
- **Ans.：F**
- **理由**：此語句集可能是一致的，也可能是不一致的。
  1. 一致的例子：$\{A, B\}$，其形式是 $\{p, q\}$，取代實例可以同時都為真（例如：$\{\text{清華在台灣},\ \text{台大在台灣}\}$），也可以同時都為假（例如：$\{\text{清華在巴黎},\ \text{台大在柏林}\}$），但集合依然是一致的。
  2. 不一致的例子：兩個矛盾句組成的集合。
  - 根據定義，不一致是「不可能同時為真」，但「可以同時為假」。

### (5) 若一個論證具有一致的前提集且結論為假，則此論證必然是無效的。
- **Ans.：F**
- **理由**：一個具有一致前提集且結論為假的論證不必然是無效的，也可能是有效的。
  - 例如：若清華大學在金門，則台灣大學在澎湖。清華大學在金門。/∴ 台灣大學在澎湖。
  - 此論證形式為 MP（有效），其前提集是一致的，且其結論在現實中為假（前提 2 在現實中為假）。

### (6) 無效的論證形式之取代實例都是無效的論證。
- **Ans.：F**
- **理由**：例如 $p, q \vdash r$ 是無效的論證形式；但其取代實例可以構造為 $A \supset B,\ A \vdash B$（有效論證）。

### (7) 一個恆真句的語句形式之取代實例必然也是恆真句。
- **Ans.：F**
- **理由**：$p$ 是恆真句 $A \lor \sim A$ 的一個語句形式，而 $A$ 是 $p$ 的一個取代實例，但是 $A$ 卻不是恆真句。

### (8) 若一個有效論證的結論為恆真句，則此論證是健全的 (sound)。
- **Ans.：F**
- **理由**：健全論證必須同時滿足「形式有效」且「所有前提事實上為真」。例如：
  1. 清華大學在金門。(F)
  /∴ 2. 清華大學在金門或清華大學不在金門。($A \lor \sim A$，恆真句)
  此論證有效且結論恆真，但前提為假，故不健全。

### (9) 若在有效論證的前提集中添加新的前提，則由此構成的新論證還是有效的。
- **Ans.：T**
- **理由**：
  1. 語法途徑：原論證已能由既有前提推得結論，添加新前提絕不會破壞原有的推導鏈。
  2. 語意途徑：原有效論證的反例集是不一致的，在不一致的集合中加入任何新語句，新集合必然依然是不一致的（古典邏輯的單調性 Monotonicity）。

### (10) 若 $A_1 \cdot A_2 \dots A_n$ 邏輯地蘊含 $C$，則 $A_1, A_2 \dots A_n \vdash C$ 是一個有效論證。
- **Ans.：T**
- **理由**：邏輯蘊含定義即代表 $(A_1 \cdot A_2 \dots A_n) \supset C$ 是恆真句，不可能前提全真而結論為假，故論證必有效。

---

## 2. 集合一致性判定 (10%)

### (1) $\{\sim(A \cdot B),\ \sim(B \cdot C),\ \sim(A \cdot C),\ A \lor (B \cdot C)\}$
- **Ans.：一致 (Consistent)**
- **證明**：
  - 相應形式：$\sim(p \cdot q),\ \sim(q \cdot r),\ \sim(p \cdot r),\ p \lor (q \cdot r)$
  - 取賦值：$V(p)=T,\ V(q)=F,\ V(r)=F$
  - 檢驗：
    - $\sim(T \cdot F) = T$
    - $\sim(F \cdot F) = T$
    - $\sim(T \cdot F) = T$
    - $T \lor (F \cdot F) = T$
  - 全體成員同時為真，故集合**一致**。

### (2) $\{\sim(J \lor (H \supset L)),\ L \equiv (\sim J \lor \sim H),\ H \equiv (J \lor L)\}$
- **Ans.：不一致 (Inconsistent)**
- **證明（導出矛盾）**：
  1. $\sim(J \lor (H \supset L))$ (p)
  2. $L \equiv (\sim J \lor \sim H)$ (p)
  3. $H \equiv (J \lor L)$ (p)
  4. $\sim J \cdot \sim(H \supset L)$ (1 DeM)
  5. $\sim(H \supset L)$ (4 Simp)
  6. $\sim(\sim H \lor L)$ (5 Impl)
  7. $H \cdot \sim L$ (6 DeM, DN)
  8. $H$ (7 Simp)
  9. $\sim L$ (7 Simp)
  10. $\sim J$ (4 Simp)
  11. $H \supset (J \lor L)$ (3 Equiv, Simp)
  12. $J \lor L$ (8, 11 MP)
  13. $L$ (10, 12 DS)
  14. $L \cdot \sim L$ (9, 13 Conj，導出矛盾！)
  - 證畢集合不一致。

---

## 3. 短真值表法判定有效性與推論證明 (15%)

### (1) $P \supset Q,\ R \supset S,\ R \lor Q \vdash P \lor S$
- **Ans.：無效**
- **短真值表反例**：
  - 令結論 $P \lor S = F \implies V(P)=F, V(S)=F$。
  - 令前提 3 $R \lor Q = T$，取 $V(R)=F, V(Q)=T$。
  - 此時 $V(P \supset Q) = F \supset T = T$；$V(R \supset S) = F \supset F = T$。
  - 當 $V(P)=F, V(S)=F, V(R)=F, V(Q)=T$ 時，前提皆真而結論為假，證畢**無效**。

### (2) $\sim(A \lor \sim B),\ C \supset A \vdash C \supset D$
- **Ans.：有效 (Valid)**
- **證明**：
  1. $\sim(A \lor \sim B)$ (p)
  2. $C \supset A$ (p)  /∴ $C \supset D$
  3. $\sim A \cdot \sim\sim B$ (1 DeM)
  4. $\sim A$ (3 Simp)
  5. $\sim C$ (2, 4 MT)
  6. $\sim C \lor D$ (5 Add)
  7. $C \supset D$ (6 Impl)
  Q.E.D.

---

## 4. 純用 18 條推論規則證明（禁用 CP / IP）(30%)

### (1)
前提：$P \supset \sim R,\ (S \cdot N) \supset R,\ \sim S \supset Q,\ \sim(P \supset Q)$；結論：$\sim N$
```markdown
1. P ⊃ ~R                      p
2. (S · N) ⊃ R                 p
3. ~S ⊃ Q                      p
4. ~(P ⊃ Q)                    p  /∴ ~N
5. ~(~P v Q)                   4 Impl
6. P · ~Q                      5 DeM, DN
7. P                           6 Simp
8. ~Q                          6 Simp
9. ~R                          1, 7 MP
10. ~~S                        3, 8 MT
11. ~(S · N)                   2, 9 MT
12. ~S v ~N                    11 DeM
13. ~N                         10, 12 DS
Q.E.D.
```

### (2)
前提：$C \lor D,\ C \supset B,\ \sim C \supset \sim D$；結論：$B$
```markdown
1. C v D                       p
2. C ⊃ B                       p
3. ~C ⊃ ~D                     p  /∴ B
4. D ⊃ C                       3 Contra
5. D ⊃ B                       2, 4 HS
6. B v B                       1, 2, 5 CD
7. B                           6 Taut
Q.E.D.
```

### (3)
前提：$(A \cdot B) \supset R,\ A,\ C \supset \sim R$；結論：$\sim(C \cdot B)$
```markdown
1. (A · B) ⊃ R                 p
2. A                           p
3. C ⊃ ~R                      p  /∴ ~(C · B)
4. A ⊃ (B ⊃ R)                 1 Exp
5. B ⊃ R                       2, 4 MP
6. ~R ⊃ ~B                     5 Contra
7. C ⊃ ~B                      3, 6 HS
8. ~C v ~B                     7 Impl
9. ~(C · B)                    8 DeM
Q.E.D.
```

---

## 5. 推論規則證明定理 (15%)

### (1) $\vdash [(\sim A \supset (D \cdot C)) \cdot \sim(B \cdot A)] \supset (\sim C \supset \sim B)$
```markdown
1. | [~A ⊃ (D · C)] · ~(B · A)            AP  /∴ ~C ⊃ ~B
2. | | ~C                                 AP  /∴ ~B
3. | | ~A ⊃ (D · C)                       1 Simp
4. | | ~(B · A)                           1 Simp
5. | | ~B v ~A                            4 DeM
6. | | ~C v ~D                            2 Add
7. | | ~D v ~C                            6 Comm
8. | | ~(D · C)                           7 DeM
9. | | ~~A                                3, 8 MT
10. | | ~B                                5, 9 DS
11. | ~C ⊃ ~B                             2-10 CP
12. [~A ⊃ (D · C)] · ~(B · A) ⊃ (~C ⊃ ~B) 1-11 CP
Q.E.D.
```

### (2) $\vdash ((P \supset Q) \supset Q) \supset ((Q \supset P) \supset P)$
```markdown
1. | (P ⊃ Q) ⊃ Q                          AP  /∴ (Q ⊃ P) ⊃ P
2. | | Q ⊃ P                              AP  /∴ P
3. | | (P ⊃ Q) ⊃ P                        1, 2 HS
4. | | ~(~P v Q) v P                      3 Impl (x2)
5. | | (P · ~Q) v P                       4 DeM, DN
6. | | P v (P · ~Q)                       5 Comm
7. | | (P v P) · (P v ~Q)                 6 Dist
8. | | P v P                              7 Simp
9. | | P                                  8 Taut
10. | (Q ⊃ P) ⊃ P                         2-9 CP
11. ((P ⊃ Q) ⊃ Q) ⊃ ((Q ⊃ P) ⊃ P)         1-10 CP
Q.E.D.
```

### (3) $\vdash ((A \supset B) \cdot (B \supset C)) \lor (C \supset A)$
```markdown
1. | ~(C ⊃ A)                             AP  /∴ (A ⊃ B) · (B ⊃ C)
2. | ~(~C v A)                            1 Impl
3. | C · ~A                               2 DeM, DN
4. | C                                    3 Simp
5. | ~A                                   3 Simp
6. | ~A v B                               5 Add
7. | A ⊃ B                                6 Impl
8. | C v ~B                               4 Add
9. | ~B v C                               8 Comm
10. | B ⊃ C                               9 Impl
11. | (A ⊃ B) · (B ⊃ C)                   7, 10 Conj
12. ~(C ⊃ A) ⊃ ((A ⊃ B) · (B ⊃ C))        1-11 CP
13. ~~(C ⊃ A) v ((A ⊃ B) · (B ⊃ C))       12 Impl
14. ((A ⊃ B) · (B ⊃ C)) v (C ⊃ A)         13 DN, Comm
Q.E.D.
```
