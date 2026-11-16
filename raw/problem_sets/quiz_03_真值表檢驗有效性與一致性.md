# 邏輯小考 (3) 解答 (真值表檢驗有效性與一致性)

**日期**：2024.10.03  

---

## I. 請用真值表法證明下列論證是有效的或無效的

### (1) 論證：$\neg(A \land \neg B),\ C \rightarrow A \vdash C \rightarrow D$
- **相對應形式**：$\neg(p \land \neg q),\ r \rightarrow p \vdash r \rightarrow s$
- **判斷**：**無效 (Invalid)**（題目中若目標為 $C \rightarrow D$，反例顯然；若目標為 $C \rightarrow B$ 則有效）。
- **短真值表檢驗**：
  - 令結論 $r \rightarrow s = F \implies V(r)=T, V(s)=F$。
  - 前提 2 $r \rightarrow p = T \implies V(p)=T$。
  - 前提 1 $\neg(p \land \neg q) = T \implies p \land \neg q = F$；因 $V(p)=T$，必令 $V(q)=T$。
  - 當 $V(r)=T, V(p)=T, V(q)=T, V(s)=F$ 時，前提皆為真，但結論為假！
  - **結論**：成功找到反例，**論證無效**。

### (2) 論證：$A \rightarrow B,\ (B \land C) \rightarrow A \vdash \neg B$
- **相對應形式**：$p \rightarrow q,\ (q \land r) \rightarrow p \vdash \neg q$
- **短真值表檢驗**：
  - 令結論 $\neg q = F \implies V(q)=T$。
  - 取 $V(p)=T, V(r)=T$。
  - 檢驗前提：$p \rightarrow q = T \rightarrow T = T$；$(q \land r) \rightarrow p = (T \land T) \rightarrow T = T$。
  - 當 $V(p)=T, V(q)=T, V(r)=T$ 時，前提皆真而結論為假！
  - **結論**：**論證無效**。

---

## II. 請用真值表法證明下列語句集合是一致的或不一致的

### (3) 集合：$\{B \rightarrow A,\ C \rightarrow B,\ \neg C \land A\}$
- **相對應形式**：$\{q \rightarrow p,\ r \rightarrow q,\ \neg r \land p\}$
- **短真值表檢驗**：
  - 令 $\neg r \land p = T \implies V(r)=F, V(p)=T$。
  - 此時 $r \rightarrow q = F \rightarrow q = T$（恆真）。
  - $q \rightarrow p = q \rightarrow T = T$（恆真）。
  - 當 $V(p)=T, V(r)=F, V(q)=\text{任意}$ 時，所有語句同時為真。
  - **結論**：**集合是一致的 (Consistent)**。
