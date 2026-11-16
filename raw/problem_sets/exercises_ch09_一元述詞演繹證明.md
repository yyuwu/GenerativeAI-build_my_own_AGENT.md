# Chapter 9 習題與解答 (一元述詞邏輯演繹證明)

## Exercise 9-1: 基本推導
### (1)
1. $(x)Fx \lor (x)\neg Gx$ (p)
2. $\neg(x)Fx$ (p)
3. $(x)(Dx \rightarrow Gx)$ (p)  /∴ $(\exists x)(\neg Dx \lor Gx)$
4. $(x)\neg Gx$ (1, 2 DS)
5. $\neg Gx$ (4 UI)
6. $Dx \rightarrow Gx$ (3 UI)
7. $\neg Dx$ (5, 6 MT)
8. $\neg Dx \lor Gx$ (7 Add)
9. $(\exists x)(\neg Dx \lor Gx)$ (8 EG)
Q.E.D.

### (5)
1. $Ab \lor Bc$ (p)
2. $(x)\neg Bx$ (p)  /∴ $(\exists x)Ax$
3. $\neg Bc$ (2 UI)
4. $Ab$ (1, 3 DS)
5. $(\exists x)Ax$ (4 EG)
Q.E.D.

---

## Exercise 9-2: 辨別無效的推論步驟
(1) 第 4 步 $Mx$ (1, 3 MP) **無效**：MP 只能作用於整列語句，不可作用於量詞控制內部的子句。  
(3) 第 4 步 $Fy \land \neg My$ (1 EI) **無效**：$y$ 在第 3 步已經出現過，EI 必須引進全新變元！  
(5) 第 3 步 Simp **無效**（作用於子句）；第 6 步 UG **無效**（$x$ 是由 EI 引進的準變元，不可 UG！）。  

---

## Exercise 9-3: 四大規則推導
### (1)
1. $(x)(Rx \rightarrow Bx)$ (p)
2. $(\exists x)\neg Bx$ (p)  /∴ $(\exists x)\neg Rx$
3. $\neg Bx$ (2 EI，★先做 EI)
4. $Rx \rightarrow Bx$ (1 UI，★後做 UI 配合 x)
5. $\neg Rx$ (3, 4 MT)
6. $(\exists x)\neg Rx$ (5 EG)
Q.E.D.

### (7)
1. $(\exists x)(Ax \land Bx)$ (p)
2. $(y)(Ay \rightarrow Cy)$ (p)  /∴ $(\exists x)(Bx \land Cx)$
3. $Ax \land Bx$ (1 EI)
4. $Ax$ (3 Simp)
5. $Ax \rightarrow Cx$ (2 UI)
6. $Cx$ (4, 5 MP)
7. $Bx$ (3 Simp)
8. $Bx \land Cx$ (6, 7 Conj)
9. $(\exists x)(Bx \land Cx)$ (8 EG)
Q.E.D.

---

## Exercise 9-4: 判斷 QN 運用正確性
(1) $(x)\neg Fx \implies \neg(\exists x)Fx$（原寫法錯）。  
(3) $(x)\neg(\neg Fx \lor Gx) \implies \neg(\exists x)(\neg Fx \lor Gx)$（原寫法錯）。  
(7) 正確。  

---

## Exercise 9-5: 結合 QN 的推導
### (1)
1. $(\exists x)Fx \lor (\exists x)Gx$ (p)
2. $(x)\neg Fx$ (p)  /∴ $(\exists x)Gx$
3. $\neg(\exists x)Fx$ (2 QN)
4. $(\exists x)Gx$ (1, 3 DS)
Q.E.D.

### (7)
1. $(x)[(Fx \lor Hx) \rightarrow (Gx \land Ax)]$ (p)
2. $\neg(x)(Ax \land Gx)$ (p)  /∴ $(\exists x)\neg Hx$
3. $(\exists x)\neg(Ax \land Gx)$ (2 QN)
4. $\neg(Ax \land Gx)$ (3 EI)
5. $\neg(Gx \land Ax)$ (4 Comm)
6. $(Fx \lor Hx) \rightarrow (Gx \land Ax)$ (1 UI)
7. $\neg(Fx \lor Hx)$ (5, 6 MT)
8. $\neg Fx \land \neg Hx$ (7 DeM)
9. $\neg Hx$ (8 Simp)
10. $(\exists x)\neg Hx$ (9 EG)
Q.E.D.

### (19) 全稱條件句綜合證明
1. $(x)[Px \rightarrow (Qx \lor Rx)]$ (p)
2. $(x)[(Sx \land Px) \rightarrow \neg Qx]$ (p)  /∴ $(x)(Sx \rightarrow Px) \rightarrow (x)(Sx \rightarrow Rx)$
3. | $(x)(Sx \rightarrow Px)$ (AP)  /∴ $(x)(Sx \rightarrow Rx)$
4. | | $Sx$ (AP)  /∴ $Rx$
5. | | $Sx \rightarrow Px$ (3 UI)
6. | | $Px$ (4, 5 MP)
7. | | $Sx \land Px$ (4, 6 Conj)
8. | | $(Sx \land Px) \rightarrow \neg Qx$ (2 UI)
9. | | $\neg Qx$ (7, 8 MP)
10. | | $Px \rightarrow (Qx \lor Rx)$ (1 UI)
11. | | $Qx \lor Rx$ (6, 10 MP)
12. | | $Rx$ (9, 11 DS)
13. | $Sx \rightarrow Rx$ (4-12 CP)
14. | $(x)(Sx \rightarrow Rx)$ (13 UG，變元 x 獲得完全自由)
15. $(x)(Sx \rightarrow Px) \rightarrow (x)(Sx \rightarrow Rx)$ (3-14 CP)
Q.E.D.
