# Chapter 10 習題與解答 (關係述詞與多重量詞)

## Exercise 10-1 & 10-3: 關係符號化
- 10-1 (7) $(x)(Bxd \rightarrow \neg Idx)$
- 10-1 (15) $(\exists x)(Mxa \land Lmx) \land (\exists x)(Mxa \land \neg Lmx)$
- 10-3 (1) $(\exists x)[Sx \land (y)\neg Kxy]$
- 10-3 (11) $\neg(\exists x)[Cx \land (y)(Py \rightarrow Tyx)]$ 或 $(x)[Cx \rightarrow (\exists y)(Py \land \neg Tyx)]$

---

## Exercise 10-4: 自然語言深層改寫 (Paraphrasing)
- (3) “In every place there are cheaters” $\implies (x)[Px \rightarrow (\exists y)(Cy \land Ayx)]$
- (5) 「人的工作永遠做不完。」 $\implies (x)\{Px \rightarrow (y)[Ty \rightarrow (\exists z)(Wzx \land \neg Dzxy)]\}$
- (7) “Sometimes you can fool all of the people” $\implies (\exists x)[Tx \land (y)(Py \rightarrow Fyx)]$
- (11) 「會叫的狗不咬人。」 $\implies (x)[(Dx \land Kx) \rightarrow \neg(\exists y)(Ty \land Bxy)]$
- (13) 「罪惡無時不有、無所不在。」 $\implies (x)(y)[(Tx \land Py) \rightarrow (\exists z)(Sz \land Azxy)]$

---

## Exercise 10-8: 多重量詞證明無效性
### (1) $(\exists x)(y)Fxy \vdash (x)(y)Fyx$
- **自然數反例**：$Fxy$: $x \cdot y = y$。
  - 當 $x = 1$ 時，對所有 $y$ 皆有 $1 \cdot y = y$（前提真）。
  - 但結論斷言對所有 $x, y$ 都有 $y \cdot x = x$（顯然為假，如 $2 \cdot 3 \neq 3$）。
- **$\text{Domain} = \{a, b\}$ 反例**：
  - 前提展開：$(Faa \land Fab) \lor (Fba \land Fbb) = (F \land T) \lor (T \land T) = T$。
  - 結論展開：$(Faa \land Fba) \land (Fab \land Fbb) = (F \land T) \land (T \land T) = F$。
  - $\implies$ **無效**。

### (7) $(x)(y)(\exists z)Fxyz \vdash (\exists x)(y)(z)Fxyz$
- **自然數反例**：$Fxyz$: $x + y = z$。
  - 前提：任兩數相加皆存在一和（真）。
  - 結論：存在一數 $x$ 使得與任意兩數 $y, z$ 滿足 $x + y = z \implies x = z - y$（不可能存在固定單一常數 $x$ 滿足此式，為假）。
  - $\implies$ **無效**。

---

## Exercise 10-10 & 10-11: 多重量詞演繹證明
### 10-10 (7) $(\exists x)(y)(z)Azyx \vdash (x)(y)(\exists z)Axyz$
```markdown
1. (∃x)(y)(z)Azyx              p  /∴ (x)(y)(∃z)Axyz
2. | ~(x)(y)(∃z)Axyz           AP /∴ (x)(y)(∃z)Axyz
3. | (∃x)~(y)(∃z)Axyz          2 QN
4. | (∃x)(∃y)~(∃z)Axyz         3 QN
5. | (∃x)(∃y)(z)~Axyz          4 QN
6. | (∃y)(z)~Axyz              5 EI
7. | (z)~Axyz                  6 EI (變元 x, y, z 皆確定)
8. | (y)(z)Azyu                1 EI (引入新變元 u)
9. | (z)Azyu                   8 UI
10.| Axyu                      9 UI
11.| ~Axyu                     7 UI
12.| Axyu · ~Axyu              10, 11 Conj (矛盾爆發！)
13. (x)(y)(∃z)Axyz             2-12 IP
Q.E.D.
```

---

## Exercise 10-12: 量詞定理證明 (Theorems with CP/IP)
### (1) 證明全稱量詞交換律：$\vdash (x)(y)Fxy \equiv (y)(x)Fxy$
- 利用 CP 證明正向 $(x)(y)Fxy \rightarrow (y)(x)Fxy$，再證明反向 $(y)(x)Fxy \rightarrow (x)(y)Fxy$，最後由 Conj + Equiv 建立雙條件句定理。

### (13) 證明定理 Q17：$\vdash (x)(Fx \rightarrow P) \equiv [(\exists x)Fx \rightarrow P]$
```markdown
1. | (x)(Fx -> P)              AP /∴ (∃x)Fx -> P
2. | | (∃x)Fx                  AP /∴ P
3. | | Fx                      2 EI
4. | | Fx -> P                 1 UI
5. | | P                       3, 4 MP
6. | (∃x)Fx -> P               2-5 CP
7. (x)(Fx -> P) -> [(∃x)Fx -> P] 1-6 CP

8. | (∃x)Fx -> P               AP /∴ (x)(Fx -> P)
9. | | Fx                      AP /∴ P
10.| | (∃x)Fx                  9 EG
11.| | P                       8, 10 MP
12.| Fx -> P                   9-11 CP
13.| (x)(Fx -> P)              12 UG (x 具任意性)
14. [(∃x)Fx -> P] -> (x)(Fx -> P) 8-13 CP

15. (x)(Fx -> P) ≡ [(∃x)Fx -> P] 7, 14 Conj, Equiv
Q.E.D.
```
