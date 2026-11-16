# Chapter 3 習題與解答 (Truth Tables)

## Ex 3-1: 給定賦值計算真值
假定 $V(A) = V(B) = T,\ V(C) = V(D) = V(E) = F$：
7. $(A \lor B) \rightarrow (A \land \neg B)$
   - 前件 $T \lor T = T$；後件 $T \land \neg T = F$；$T \rightarrow F = F$。
   - $V = F$。
9. $[(A \land B) \land C] \rightarrow [(A \land C) \lor (A \land D)]$
   - 前件 $(T \land T) \land F = F$；假前件條件句恆為真。
   - $V = T$。
11. $[(A \land B) \lor (C \land D)] \rightarrow E$
    - 前件 $(T \land T) \lor (F \land F) = T$；後件 $E = F$；$T \rightarrow F = F$。
    - $V = F$。
15. $[(E \lor \neg D) \land \neg A] \rightarrow \{(\neg A \land \neg B) \land [(C \land D) \land E]\}$
    - 前件中含有 $\neg A = F$，連言為假；假前件蘊涵全句為真。
    - $V = T$。

---

## Ex 3-2: 含未知變元的真值推導
假定 $V(A) = V(B) = T,\ V(C) = V(D) = F,\ V(Q) = V(R) = ?$：
3. $\neg C \rightarrow (D \rightarrow Q)$
   - $\neg C = T$；後件中 $D = F$，故 $D \rightarrow Q$ 必然為 $T$（不論 $Q$ 為何）；$T \rightarrow T = T$。
   - $V = T$。
5. $\neg[R \land \neg R]$
   - 不論 $R$ 為真或假，$R \land \neg R$ 必然為矛盾句 $F$；$\neg F = T$。
   - $V = T$。
9. $(A \lor R) \rightarrow (\neg A \land R)$
   - 前件 $T \lor R = T$；後件 $F \land R = F$；$T \rightarrow F = F$。
   - $V = F$。
11. $(A \land C) \rightarrow [(D \land Q) \rightarrow (\neg A \land R)]$
    - 前件 $A \land C = T \land F = F$；假前件保證全句為真。
    - $V = T$。

---

## Ex 3-3: 語句形式之取代實例判別
1. $A \land (B \rightarrow C)$ 不是 $p \rightarrow q$ 的取代實例（因為主連接詞是 $\land$ 而非 $\rightarrow$）。
3. $\neg A$、$\neg\neg A$、$\neg(A \rightarrow B)$ 皆為 $\neg p$ 的取代實例。
5. $\neg A \rightarrow (B \rightarrow C)$ 是 $p$、$p \rightarrow q$、$\neg p \rightarrow q$ 以及 $p \rightarrow (q \rightarrow r)$ 的取代實例。

---

## Ex 3-5: 決定語句的所有語句形式
1. $A \land \neg B$ $\implies p,\ p \land q,\ p \land \neg q$
5. $\neg(\neg R \lor S)$ $\implies p,\ \neg p,\ \neg(p \lor q),\ \neg(\neg p \lor q)$
7. $\neg A \lor (B \lor A)$ $\implies p,\ p \lor q,\ \neg p \lor q,\ p \lor (q \lor r),\ \neg p \lor (q \lor r),\ \neg p \lor (q \lor p)$
9. $(A \lor B) \lor C$ $\implies p,\ p \lor q,\ (p \lor q) \lor r$
11. $\neg(B \land D) \lor (R \lor D)$ $\implies p,\ p \lor q,\ \neg p \lor q,\ p \lor (q \lor r),\ \neg p \lor (q \lor r),\ \neg(p \land q) \lor r,\ \neg(p \land q) \lor (r \lor s),\ \neg(p \land q) \lor (r \lor q)$

---

## Ex 3-6: 判定恆真、矛盾與適真句
3. $A \rightarrow (A \lor B)$ $\implies$ **恆真句 (Tautology)**。
7. $(A \land B) \rightarrow (\neg A \lor \neg B)$ $\implies$ **適真句 (Contingent)**（$A=B=T$ 時為 $F$；$A=B=F$ 時為 $T$）。
9. $(A \rightarrow B) \land (A \land \neg B)$ $\implies$ **矛盾句 (Contradiction)**。

---

## Ex 3-8: 短真值表檢驗有效性
(3) 前提：$(A \land B) \rightarrow C,\ A$；結論：$B \rightarrow C$
- 令結論 $B \rightarrow C$ 為假 $\implies V(B)=T, V(C)=F$。
- 為使前提皆真，需 $V(A)=T$，此時 $A \land B = T$，但後件 $C=F$，導致 $(A \land B) \rightarrow C = F$，爆發衝突！
- $\implies$ **論證有效 (Valid)**。

(7) 前提：$\neg(D \land \neg K),\ H \rightarrow D$；結論：$H \rightarrow K$
- 令結論為假 $\implies V(H)=T, V(K)=F$。
- 前提 2 真 $\implies V(D)=T$。
- 此時 $D \land \neg K = T \land T = T$，導致 $\neg(D \land \neg K) = F$，衝突！
- $\implies$ **論證有效 (Valid)**。

(11) 前提：$F \rightarrow G,\ (G \land H) \rightarrow K$；結論：$F$
- 令結論為假 $\implies V(F)=F$。
- 取 $V(G)=T, V(H)=T, V(K)=T$，前提 1 與 2 皆為真，且結論為假，成功構造反例！
- $\implies$ **論證無效 (Invalid)**。

(17) 前提：$\neg(A \land \neg B),\ C \rightarrow A$；結論：$C \rightarrow D$
- 令結論為假 $\implies V(C)=T, V(D)=F$。
- 前提 2 真 $\implies V(A)=T$。若令 $V(B)=F$，前提 1 為假；若令 $V(B)=T$，前提 1 雖真但無法推得結論。構造反例：$V(C)=T, V(A)=T, V(B)=T, V(D)=F$，前提皆真結論假！
- $\implies$ **論證無效 (Invalid)**。

---

## Ex 3-10: 短真值表反例證偽
(1) $H \rightarrow K,\ H \vdash \neg K$
- 反例賦值：$V(H)=T, V(K)=T$（前提皆真結論假）$\implies$ **無效**。
(3) $(H \land K) \rightarrow L \vdash L \rightarrow (H \land K)$
- 反例賦值：$V(L)=T, V(K)=F, V(H)=T$ $\implies$ **無效**。
(5) $(R \lor M) \rightarrow N,\ \neg N \vdash R$
- 反例賦值：$V(R)=F, V(M)=F, V(N)=F$ $\implies$ **無效**。
(11) $P \rightarrow Q,\ R \rightarrow S,\ R \lor Q \vdash P \lor S$
- 反例賦值：$V(P)=F, V(S)=F, V(R)=F, V(Q)=T$ $\implies$ **無效**。

---

## Ex 3-11: 集合一致性短真值表檢測
(1) $\{B \rightarrow A,\ C \rightarrow B,\ \neg C \land A\}$
- 賦值：$V(A)=T, V(C)=F, V(B)=T$，全體語句同時為真 $\implies$ **一致 (Consistent)**。
(5) $\{A \land \neg B,\ B \equiv C,\ \neg(C \land \neg B)\}$
- 賦值：$V(A)=T, V(B)=F, V(C)=F$，全體語句同時為真 $\implies$ **一致 (Consistent)**。

---

## Ex 3-13: 概念問答
1. 賦值原則：二值原則，每一原子句每次只能賦予 $T$ 或 $F$ 恰有一者。
3. 恆真的語句形式的所有取代實例是否皆為恆真句？是。
5. 含有 $n$ 個變元的語句形式有 $2^n$ 列可能的真值條件。4 個變元有 $2^4 = 16$ 列。
7. 一個前提一致的有效論證其結論是否必然為真？**否！** 一致僅表示「可能同時為真」，並非事實上為真。只有健全論證（前提事實上為真）其結論才必然為真。
