# 邏輯小考 (6) 解答 (條件證法與間接證法證明定理)

**日期**：2023.11.14  

---

## 證明題

### (1) 證明定理：$\vdash A \rightarrow (A \rightarrow B)$（當前件假或已知 $\neg A$ 時成立之定理變形）

#### 證明一（兩層嵌套 CP + DS）：
```markdown
1. | A                         AP  /∴ A -> B
2. | | ~A                      AP  /∴ B
3. | | ~A v B                  1 DN, Add (或 2 Add)
4. | | B                       2, 3 DS
5. | ~A -> B                   2-4 CP
6. A -> (~A -> B)              1-5 CP
Q.E.D.
```

#### 證明二（間接證法 IP）：
```markdown
1. | ~(A -> (~A -> B))         AP  /∴ A -> (~A -> B)
2. | ~(~A v (~~A v B))         1 Impl x2
3. | A · (~A · ~B)             2 DeM x2, DN
4. | (A · ~A) · ~B             3 Assoc
5. | A · ~A                    4 Simp
6. A -> (~A -> B)              1-5 IP
Q.E.D.
```

#### 證明三（CP + DN + Add + Impl）：
```markdown
1. | A                         AP  /∴ ~A -> B
2. | ~~A                       1 DN
3. | ~~A v B                   2 Add
4. | ~A -> B                   3 Impl
5. A -> (~A -> B)              1-4 CP
Q.E.D.
```

---

### (2) 證明定理：$\vdash [(S \lor (T \rightarrow R)) \land ((S \rightarrow T) \land \neg(T \rightarrow R))] \rightarrow T$

#### 證明一（IP 歸謬法）：
```markdown
1. | (S v (T -> R)) · ((S -> T) · ~(T -> R)) AP  /∴ T
2. | | ~T                                   AP  /∴ T
3. | | S v (T -> R)                         1 Simp
4. | | S -> T                               1 Simp
5. | | ~(T -> R)                            1 Simp
6. | | ~S                                   2, 4 MT
7. | | T -> R                               3, 6 DS
8. | | (T -> R) · ~(T -> R)                 5, 7 Conj (矛盾！)
9. | T                                      2-8 IP
10. [(S v (T -> R)) · ((S -> T) · ~(T -> R))] -> T 1-9 CP
Q.E.D.
```

#### 證明二（直接拆解 $\neg(T \rightarrow R)$）：
```markdown
1. | (S v (T -> R)) · ((S -> T) · ~(T -> R)) AP  /∴ T
2. | ~(T -> R)                              1 Simp
3. | ~(~T v R)                              2 Impl
4. | ~~T · ~R                               3 DeM
5. | T                                      4 Simp, DN
6. [(S v (T -> R)) · ((S -> T) · ~(T -> R))] -> T 1-5 CP
Q.E.D.
```
