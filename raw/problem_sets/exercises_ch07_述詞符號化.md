# Chapter 7 習題與解答 (述詞邏輯的符號化)

## Exercise 7-3
(1) $(x)(Ex \rightarrow Cx)$  
(3) $\neg(x)(Ex \rightarrow Cx)$  
(5) $(x)[(Nx \land Ex) \rightarrow Cx]$  
(7) $(x)[(\neg Nx \land Ex) \rightarrow \neg Cx]$ 或 $\neg(x)[(\neg Nx \land Ex) \land Cx]$  
(9) $(x)[(Nx \land Ex) \rightarrow Cx]$ 或 $\neg(x)[(Nx \land Ex) \land \neg Cx]$  
(11) $(x)[Mx \rightarrow (\neg Nx \land Ex)]$  
(13) $\neg(x)(\neg Cx \land Ex) \land (x)(Ex \land Mx)$ 或 $(x)(Ex \rightarrow Cx) \land \neg(x)(Ex \rightarrow \neg Mx)$  

---

## Exercise 7-4
(1) $(x)(Px \rightarrow Ix)$  
(3) $\neg(x)(Px \rightarrow Ix)$  
(5) $Ib \land \neg(x)(Px \rightarrow \neg Ix)$  
(7) $(x)(Sx \rightarrow Lx)$  
(9) $\neg(x)(Sx \rightarrow Lx)$  
(11) $(x)(Sx \rightarrow Lx) \lor (x)(Sx \rightarrow \neg Px)$ 或 $(x)(Sx \rightarrow Lx) \lor \neg(x)(Sx \land Px)$  
(13) $\neg(x)(\neg Px \rightarrow \neg Lx)$  
(15) $\neg La \land \neg[(x)(Sx \rightarrow Lx) \lor (x)(\neg Px \rightarrow Lx)]$  

---

## Exercise 7-5
(1) $(\exists x)(Ax \land Ox)$  
(3) $\neg(\exists x)(Ax \land Ox)$  
(5) $(\exists x)(Ex \land \neg Ox)$  
(7) $(\exists x)[Ax \land (Px \land Tx)]$  
(9) $(\exists x)(Ax \land \neg Px) \land (\exists x)(Ax \land \neg Tx)$  
(11) $(\exists x)(Rx \land Dx)$  
(13) $(x)[(Rx \land Dx) \rightarrow \neg Fx]$ 或 $\neg(\exists x)[Rx \land (Dx \land Fx)]$  
(15) $(\exists x)\{Rx \land [(Sx \land Dx) \land \neg Fx]\} \land \{(\exists x)[Rx \land (Fx \land \neg Dx)] \land (\exists x)(Rx \land \neg Sx)\}$  

---

## Exercise 7-6
(1) $(x)(Mx \rightarrow Px)$ ($Mx$ = x is a marsupial, $Px$ = x has a pouch)  
(3) $\neg(x)(Mx \rightarrow Px)$  
(5) $(x)[(Kx \lor Ox) \rightarrow Mx]$ 或 $(x)(Kx \rightarrow Mx) \land (x)(Ox \rightarrow Mx)$  
(7) $(x)(Kx \rightarrow \neg Bx)$  
(9) $(\exists x)(Mx \land Ax) \land (\exists x)(Mx \land Nx)$  
(11) $(x)[(Mx \land Fx) \rightarrow Px] \land (x)[(Mx \land Yx) \rightarrow \neg Px]$  
(13) $(x)[(Fx \land Px) \rightarrow Hx]$  
(15) $(x)[Cx \rightarrow (Gx \rightarrow Sx)]$  
(17) $(x)[(Gx \lor Bx) \rightarrow Cx]$ 或 $(x)(Gx \rightarrow Cx) \land (x)(Bx \rightarrow Cx)$  
(19) $(\exists x)(Ox \land Cx) \land (\exists x)(Ox \land Jx)$  

---

## Exercise 7-7 (自然語言反向翻譯)
(1) 有些電視主播有優雅的人格。  
(3) 沒有電視主播是政治專家。  
(5) 並非所有電視主播都是政治專家。  
(7) 有些電視主播並非既是有優雅的人格也是政治專家。（或：有些電視主播不具有優雅的人格，或者有些電視主播不是政治專家。）  
(9) 如果所有電視主播都是政治專家，則 Barbara Walters 不是電視主播。  
(11) 如果 John Madden 有優雅的人格但不是政治專家，則他不是電視主播。  

---

## Exercise 7-8 (展開式)
(1) $(Fa \land Ga) \land (Fb \land Gb)$  
(3) $[Fa \rightarrow (Ga \rightarrow Ha)] \land [Fb \rightarrow (Gb \rightarrow Hb)]$  
(5) $\neg(Fa \rightarrow Ga) \land \neg(Fb \rightarrow Gb)$  
(7) $\neg[(Fa \rightarrow Ga) \land (Fb \rightarrow Gb)]$  
(9) $[Fa \rightarrow (Ga \lor Ha)] \land [Fb \rightarrow (Gb \lor Hb)]$  
(11) $[(Fa \land Ga) \rightarrow (Ha \land Ka)] \land [(Fb \land Gb) \rightarrow (Hb \land Kb)]$  
(13) $\neg[(Fa \rightarrow Ga) \lor (Fa \rightarrow Ha)] \lor \neg[(Fb \rightarrow Gb) \lor (Fb \rightarrow Hb)]$  

---

## Exercise 7-9 & 7-10 & 7-11
### 7-9
(1) $(x)[(Sx \land Fx) \rightarrow \neg Rx]$  
(3) $(x)(Hx \rightarrow Px)$  
(5) $(x)(Dx \rightarrow Sx)$  
(7) $\neg(x)(Dx \rightarrow Sx)$  
(9) $\neg(x)(Ex \rightarrow Px) \rightarrow (x)(Ex \rightarrow Dx)$ 或 $(x)(Ex \land Px) \rightarrow (x)(Ex \rightarrow Dx)$  
(11) $(x)[(Rx \land Tx) \rightarrow Cx]$ 或 $(x)[Rx \rightarrow (Tx \rightarrow Cx)]$  

### 7-10
(1) $\neg(\exists x)(Lx \land Fx)$（天下沒有白吃的午餐）  
(3) $(x)(Wx \rightarrow Bx)$  
(5) $\neg(x)(Gx \rightarrow Lx)$（並非所有發光的都是金子，部分否定）  
(7) $(x)[(Px \land Cx) \rightarrow Dx] \land (x)[(Px \land \neg Cx) \rightarrow Tx]$（能者為之，不能者教之）  
(9) $(x)[(Px \land Ex) \rightarrow Ox]$  
(11) $(\exists x)[(Px \land Bx) \land Sx]$  
(13) $\neg(x)[(Bx \land Sx) \rightarrow Cx]$ 或 $(\exists x)[(Bx \land Sx) \land \neg Cx]$  
(15) $(x)\{[Sx \land (\neg Bx \lor \neg Cx)] \rightarrow \neg Lx\}$  
(17) $\neg(\exists x)[(Px \land Bx) \land Sx] \rightarrow \neg(\exists x)[(Px \land Bx) \land \neg Lx]$  
(19) $(x)(Px \rightarrow Sx) \rightarrow (x)(Px \rightarrow \neg Lx)$  

### 7-11 經典考點剖析
“If all elephants are not protected, all elephants are doomed.”
- **正解**：$\neg(x)(Ex \rightarrow Px) \rightarrow (x)(Ex \rightarrow Dx)$
- **說明**：英語 “All ... are not ...” 在此是**部分否定 (Not all)**，而非全部否定 $(x)(Ex \rightarrow \neg Px)$（No elephants are protected）。因後者極可能為假，會使整句條件句變成瑣碎真理。
