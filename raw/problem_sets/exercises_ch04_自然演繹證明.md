# Chapter 4 習題與解答 (Natural Deduction: 18 Rules)

## Ex 4-1 至 Ex 4-3: 基本單向規則推導
### Ex 4-1 (7)
1. $A \rightarrow (B \rightarrow C)$ (p)
2. $H \rightarrow A$ (p)
3. $H \lor (A \rightarrow B)$ (p)
4. $\neg(B \rightarrow C)$ (p)  /∴ $B$
5. $\neg A$ (1, 4 MT)
6. $\neg H$ (2, 5 MT)
7. $A \rightarrow B$ (3, 6 DS)
8. $B$ (5, 7 DS)

### Ex 4-2 (9)
1. $\neg G \rightarrow (A \lor B)$ (p)
2. $\neg B$ (p)
3. $A \rightarrow D$ (p)
4. $\neg G$ (p)  /∴ $D$
5. $A \lor B$ (1, 4 MP)
6. $A$ (2, 5 DS)
7. $D$ (3, 6 MP)

### Ex 4-3 (11)
1. $(H \land K) \rightarrow L$ (p)
2. $\neg R \land K$ (p)
3. $K \rightarrow (H \lor R)$ (p)  /∴ $L$
4. $K$ (2 Simp)
5. $H \lor R$ (3, 4 MP)
6. $\neg R$ (2 Simp)
7. $H$ (5, 6 DS)
8. $H \land K$ (4, 7 Conj)
9. $L$ (1, 8 MP)

---

## Ex 4-5 至 Ex 4-8: 等值規則與綜合推導
### Ex 4-5 (11)
1. $R \lor \neg W$ (p)
2. $\neg W \rightarrow L$ (p)
3. $R \rightarrow T$ (p)  /∴ $T \lor L$
4. $T \lor L$ (1, 2, 3 CD)

### Ex 4-6 (5)
1. $\neg(F \land G)$ (p)
2. $F$ (p)  /∴ $\neg G$
3. $\neg F \lor \neg G$ (1 DeM)
4. $\neg\neg F$ (2 DN)
5. $\neg G$ (3, 4 DS)

### Ex 4-7 (1)
1. $(B \land C) \lor D$ (p)
2. $\neg C$ (p)  /∴ $D$
3. $D \lor (B \land C)$ (1 Comm)
4. $(D \lor B) \land (D \lor C)$ (3 Dist)
5. $D \lor C$ (4 Simp)
6. $D$ (2, 5 DS)

### Ex 4-8 (1)
1. $(A \land B) \rightarrow C$ (p)
2. $A$ (p)  /∴ $B \rightarrow C$
- 方法一（Exp）：
  3. $A \rightarrow (B \rightarrow C)$ (1 Exp)
  4. $B \rightarrow C$ (2, 3 MP)
- 方法二（Impl & Assoc）：
  3. $\neg(A \land B) \lor C$ (1 Impl)
  4. $(\neg A \lor \neg B) \lor C$ (3 DeM)
  5. $\neg A \lor (\neg B \lor C)$ (4 Assoc)
  6. $\neg\neg A$ (2 DN)
  7. $\neg B \lor C$ (5, 6 DS)
  8. $B \rightarrow C$ (7 Impl)

---

## Ex 4-13 & Ex 4-14: 高難度推導與後設邏輯問答
### Ex 4-13 (7)
1. $A \rightarrow B$ (p)
2. $A \lor (B \land C)$ (p)  /∴ $B$
- 推導：
  3. $(A \lor B) \land (A \lor C)$ (2 Dist)
  4. $A \lor B$ (3 Simp)
  5. $B \lor A$ (4 Comm)
  6. $\neg\neg B \lor A$ (5 DN)
  7. $\neg B \rightarrow A$ (6 Impl)
  8. $\neg B \rightarrow B$ (1, 7 HS)
  9. $\neg\neg B \lor B$ (8 Impl)
  10. $B \lor B$ (9 DN)
  11. $B$ (10 Taut)

### Ex 4-14: 後設邏輯五大核心問題
1. **為什麼單向蘊涵推論規則不能用在語句的局部子式？**
   - 若允許單向規則作用於局部子式，會產生無效推論。例如：從 $(A \land B) \lor C$ 誤用 Simp 得 $A \lor C$。當 $A=T, B=F, C=F$ 時，前提為假但結論為真；反之若構造類似形式則可能前真後假，摧毀保真性。
3. **為什麼有效論證形式的一切取代實例都是有效論證？**
   - 因為形式決定有效性。所有取代實例共享相同的抽象結構，其語意條件確保不可能出現前提皆真而結論為假。
5. **為什麼不把所有恆真條件句全部當作自然演繹推論規則？**
   - 恆真條件句有無限多個。邏輯系統追求**經濟性（簡潔）**與**實用性（證明短且直觀）**的平衡。18 條規則＋CP/IP 既能保證完備性，又具備良好的實用推導效率。
7. **證明算子 $\{\sim, \lor\}$ 具有表達完備性 (Expressive Completeness)**：
   - $p \land q \coloneqq \neg(\neg p \lor \neg q)$
   - $p \rightarrow q \coloneqq \neg p \lor q$
   - $p \leftrightarrow q \coloneqq \neg(\neg(\neg p \lor q) \lor \neg(\neg q \lor p))$
9. **析取範式 (DNF) 與 表達完備性**：
   - 含有 $n$ 個變元的語句真值表有 $2^{2^n}$ 種可能性。
   - 任何真值表均可將輸出為 $T$ 的列寫成連言項，再以選言符號（$\lor$）將所有真值列串聯，即為析取範式 (Disjunctive Normal Form, DNF)。這證明了 $\{\sim, \land, \lor\}$ 乃至 $\{\sim, \lor\}$ 具有完整的表達完備性。
