# 附錄二：述詞邏輯 55 條重要定理集 (Theorems of Predicate Logic)

> 參考文獻：林正弘，《邏輯》，三民書局 (1970)，pp. 346-365。課本 p. 239 習題 10-12。

---

## 一、 量詞對條件句與邏輯聯結詞的分配與等值定理

### Q1: $(x)(Fx \rightarrow Gx) \rightarrow [(x)Fx \rightarrow (x)Gx]$ （反之不然！）
```markdown
1. (x)(Fx -> Gx)               AP /∴ (x)Fx -> (x)Gx
2. | (x)Fx                     AP /∴ (x)Gx
3. | Fx -> Gx                  1 UI
4. | Fx                        2 UI
5. | Gx                        3, 4 MP
6. | (x)Gx                     5 UG (x 未自由出現在 AP 中)
7. (x)Fx -> (x)Gx              2-6 CP
8. (x)(Fx -> Gx) -> [(x)Fx -> (x)Gx] 1-7 CP
```

### Q2: $(x)(Fx \rightarrow Gx) \rightarrow [(\exists x)Fx \rightarrow (\exists x)Gx]$ （反之不然！）
```markdown
1. (x)(Fx -> Gx)               AP /∴ (∃x)Fx -> (∃x)Gx
2. | (∃x)Fx                    AP /∴ (∃x)Gx
3. | Fx                        2 EI
4. | Fx -> Gx                  1 UI
5. | Gx                        3, 4 MP
6. | (∃x)Gx                    5 EG
7. (∃x)Fx -> (∃x)Gx            2-6 CP
8. (x)(Fx -> Gx) -> [(∃x)Fx -> (∃x)Gx] 1-7 CP
```

### Q3: $(x)(Fx \lor Gx) \equiv [(\exists x)\neg Fx \rightarrow (x)Gx]$
（雙向證明詳見講義原文，結合 EI, QN, UI, DS 與 IP）

### Q4: $(x)(Fx \land Gx) \equiv [(x)Fx \land (x)Gx]$ （全稱對連言之分配等值律）
### Q5: $[(x)Fx \lor (x)Gx] \rightarrow (x)(Fx \lor Gx)$ （全稱對選言僅單向蘊涵，反之不然！）
### Q6: $(\exists x)(Fx \land Gx) \rightarrow [(\exists x)Fx \land (\exists x)Gx]$ （存在對連言僅單向蘊涵，反之不然！）
### Q7: $[(x)Fx \rightarrow (\exists x)Gx] \equiv (\exists x)(Fx \rightarrow Gx)$
### Q8: $[(\exists x)Fx \rightarrow (x)Gx] \rightarrow (x)(Fx \rightarrow Gx)$ （反之不然！）
### Q9: $(x)(Fx \lor Gx) \equiv [(x)Fx \lor (\exists x)Gx]$
### Q10: $(\exists x)(Fx \lor Gx) \equiv [(\exists x)Fx \lor (\exists x)Gx]$ （存在對選言之分配等值律）

---

## 二、 獨立命題 $P$ 之量詞前綴移入移出定理 (Q11 ~ Q22)

（前提假定命題 $P$ 中不含自由變元 $x$）

### Q11: $(x)(P \land Gx) \equiv [P \land (x)Gx]$
### Q12: $(\exists x)(P \land Gx) \equiv [P \land (\exists x)Gx]$
### Q13: $(x)(P \lor Gx) \equiv [P \lor (x)Gx]$
### Q14: $(\exists x)(P \lor Gx) \equiv [P \lor (\exists x)Gx]$
### Q15: $(x)(P \rightarrow Gx) \equiv [P \rightarrow (x)Gx]$
### Q16: $(\exists x)(P \rightarrow Gx) \equiv [P \rightarrow (\exists x)Gx]$

### ★ Q17: $(x)(Fx \rightarrow P) \equiv [(\exists x)Fx \rightarrow P]$
（前件全稱移出轉為存在，核心定理，詳見講義完整證明）

### ★ Q18: $(\exists x)(Fx \rightarrow P) \equiv [(x)Fx \rightarrow P]$
（前件存在移出轉為全稱，核心定理）

### Q19: $(x)(Fx \lor P) \equiv [(x)Fx \lor P]$
### Q20: $(\exists x)(Fx \lor P) \equiv [(\exists x)Fx \lor P]$
### Q21: $[(x)Fx \equiv P] \rightarrow (x)(Fx \equiv P)$
### Q22: $[(\exists x)Fx \equiv P] \rightarrow (\exists x)(Fx \equiv P)$

---

## 三、 自我蘊涵、變元重命名與基本關係定理 (Q23 ~ Q33)

### Q23: $\vdash (x)[(x)Fx \rightarrow Fx]$
### Q24: $\vdash (x)[Fx \rightarrow (\exists x)Fx]$
### Q25: $(x)Fx \equiv (y)Fy$ （全稱變元重命名）
### Q26: $(\exists x)Fx \equiv (\exists y)Fy$ （存在變元重命名）
### Q27: $(x)Fx \rightarrow (\exists x)Fx$ （非空論域下的全稱蘊涵存在）
### Q28: $(x)[Fx \rightarrow (Gx \rightarrow Hx)] \equiv [(x)(Fx \rightarrow Gx) \rightarrow (x)(Fx \land Hx)]$
### Q29: $(x)(Fx \rightarrow Gx) \equiv \neg(\exists x)(Fx \land \neg Gx)$
### Q30: $(x)(Fx \land Gx) \equiv \neg(\exists x)(Fx \rightarrow \neg Gx)$
### Q31: $(x)Fx \equiv (x)(y)(Fx \land Fy)$
### Q32: $[(x)Fx \land (x)Gx] \rightarrow \{[(x)(Fx \rightarrow Hx) \land (x)(Gx \rightarrow Jx)] \equiv (x)(y)[(Fx \land Gy) \rightarrow (Hx \land Jy)]\}$
### Q33: $\{[(\exists x)Fx \equiv (\exists x)Gx] \land (x)(y)[(Fx \land Gy) \rightarrow (Hx \equiv Jy)]\} \rightarrow [(x)(Fx \rightarrow Hx) \equiv (x)(Gx \rightarrow Jx)]$

---

## 四、 多重量詞交換律與不對稱性核心定理 (Q34 ~ Q55)

### Q34: $(x)(y)Fxy \equiv (x)(y)Fxy$
### Q35: $(x)(y)(z)Fxyz \equiv (x)(y)(z)Fxyz$
### ★ Q36: $(x)(y)Fxy \equiv (y)(x)Fxy$ （同種全稱量詞位置可任意互換）
### ★ Q37: $(\exists x)(\exists y)Fxy \equiv (\exists y)(\exists x)Fxy$ （同種存在量詞位置可任意互換）

### ★★★ Q38 / Q39: 異種量詞不對稱性定理
$$(x)(y)Fxy \rightarrow (y)(x)Fxy \quad \text{成立}$$
$$(\exists x)(y)Fxy \rightarrow (y)(\exists x)Fxy \quad \text{（成立，但反之不然！）}$$
> **重要警示**：$(y)(\exists x)Fxy \rightarrow (\exists x)(y)Fxy$ **是無效的！**  
> （每個人都有媽媽 $\not\implies$ 存在一個人是所有人的媽媽）。

### Q40: $(x)(y)Fxy \rightarrow (x)(y)(Fxy \land Fyx)$
### Q41: $(y)(x)(Fxy \rightarrow Fxx)$
### Q42: $(z)(y)(x)[Fxy \rightarrow (Fxz \land Fxx)] \rightarrow (z)(x)Fxz$
### Q43: $(y)(x)(Fx \equiv Fy) \equiv [(x)Fx \lor (x)\neg Fx]$
### Q44: $(x)(y)(Fx \equiv Fy) \equiv [(\exists x)Fx \rightarrow (x)Fx]$
### Q46: $[(\exists x)Fx \rightarrow (\exists x)Gx] \equiv (x)(\exists y)(Fx \rightarrow Gy)$
### Q48: $\{(\exists x)Fx \rightarrow [(\exists x)Gx \rightarrow (\exists x)Hx]\} \equiv (x)(y)(z)[(Fx \land Gy) \rightarrow Hz]$
### Q51 & Q52: $(x)(y)(Fx \rightarrow Gy) \equiv (y)(x)(Fx \rightarrow Gy)$
### Q54: $(\exists y)(x)(Fx \land Gy) \equiv (x)(\exists y)(Fx \land Gy)$
### Q55: $(x)(y)(z)[(Fx \land Gy) \rightarrow Hz] \equiv (y)(z)(x)[(Fx \land Gy) \rightarrow Hz]$
