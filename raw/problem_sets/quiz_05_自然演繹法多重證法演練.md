# 邏輯小考 (5) 解答 (18 條推論規則多重證法演練)

**日期**：2023.11.07  

---

## 證明題

### (1) 前提：$(A \land B) \lor (C \land D),\ \neg C$；結論：$A$

#### 證明一（DeM + Add + DS）：
```markdown
1. (A · B) v (C · D)           p
2. ~C                          p  /∴ A
3. ~C v ~D                     2 Add
4. ~(C · D)                    3 DeM
5. A · B                       1, 4 DS
6. A                           5 Simp
Q.E.D.
```

#### 證明二（Dist + Simp + DS）：
```markdown
1. (A · B) v (C · D)           p
2. ~C                          p  /∴ A
3. [(A · B) v C] · [(A · B) v D] 1 Dist
4. (A · B) v C                 3 Simp
5. A · B                       2, 4 DS
6. A                           5 Simp
Q.E.D.
```

---

### (2) 前提：$A \rightarrow B,\ C \rightarrow D,\ (B \lor D) \rightarrow E,\ \neg E$；結論：$\neg(A \lor C)$

#### 證明一（MT + DeM 串接）：
```markdown
1. A -> B                      p
2. C -> D                      p
3. (B v D) -> E                p
4. ~E                          p  /∴ ~(A v C)
5. ~(B v D)                    3, 4 MT
6. ~B · ~D                     5 DeM
7. ~B                          6 Simp
8. ~D                          6 Simp
9. ~A                          1, 7 MT
10. ~C                         2, 8 MT
11. ~A · ~C                    9, 10 Conj
12. ~(A v C)                   11 DeM
Q.E.D.
```
