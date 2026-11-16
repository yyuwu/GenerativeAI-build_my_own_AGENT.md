# Chapter 8 習題與解答 (述詞邏輯語意學與反例)

## Exercise 8-1: 解釋模型 (Interpretations)
(1) $(\exists x)(Ax \land Bx)$
- **解釋 A (真)**：Domain: 自然數；$Ax$: $x$ 是偶數；$Bx$: $x$ 可被 3 整除。（如 6 為偶數且被 3 整除，句為真）
- **解釋 B (假)**：Domain: 自然數；$Ax$: $x$ 是偶數；$Bx$: $x$ 是奇數。（無自然數既偶又奇，句為假）

(3) $(x)(Ax \rightarrow \neg Bx)$
- **解釋 A (真)**：Domain: 全人類；$Ax$: $x$ 是人；$Bx$: $x$ 全知全能。（所有人皆非全知全能，句為真）
- **解釋 B (假)**：Domain: 全人類；$Ax$: $x$ 是人；$Bx$: $x$ 是男性。（並非所有人皆非男性，句為假）

(5) $(x)[(Ax \lor Bx) \rightarrow Cx]$
- **解釋 A (真)**：$Ax$: 男人；$Bx$: 女人；$Cx$: 人類。（男人和女人皆為人類，句為真）
- **解釋 B (假)**：$Ax$: 男人；$Bx$: 女人；$Cx$: 狗。（男人和女人是狗，句為假）

---

## Exercise 8-2: 數學模型反例構造 (Mathematical Counterexamples)
(1) 前提：$(\exists x)(Ax \land Bx),\ (\exists x)(Bx \land Cx)$；結論：$(\exists x)(Ax \land Cx)$
- **反例模型**：
  - Domain: 自然數 $\{1, 2, 3 \dots\}$
  - $Ax$: $x$ 是偶數；$Bx$: $x$ 能被 3 整除；$Cx$: $x$ 是奇數。
  - 檢驗：6 是偶數且被 3 整除 (前提 1 真)；3 被 3 整除且是奇數 (前提 2 真)；但不存在既偶又奇的數 (結論為假)！
  - $\implies$ **論證無效 (Invalid)**。

(7) 前提：$(x)(Px \rightarrow Qx),\ (x)(Qx \rightarrow Rx)$；結論：$(x)(Px \land Rx)$
- **反例模型**：
  - Domain: 自然數；$Px$: 能被 4 整除；$Qx$: 能被 2 整除；$Rx$: 是偶數。
  - 被 4 整除必被 2 整除 (T)；被 2 整除必為偶數 (T)；但並非所有自然數都被 4 整除且為偶數 (F)。
  - $\implies$ **論證無效 (Invalid)**。

---

## Exercise 8-3: 有限論域展開式短真值表反例法
(1) 前提：$(\exists x)(Ax \land Bx),\ (\exists x)(Bx \land Cx)$；結論：$(\exists x)(Ax \land Cx)$
- 令 $\text{Domain} = \{a, b\}$：
  - 前提 1 展開：$(Aa \land Ba) \lor (Ab \land Bb)$
  - 前提 2 展開：$(Ba \land Ca) \lor (Bb \land Cb)$
  - 結論展開：$(Aa \land Ca) \lor (Ab \land Cb)$
- **構造賦值**：
  - 取 $V(Ba)=T, V(Ca)=T, V(Aa)=F \implies Ba \land Ca = T$（前提 2 真），$Aa \land Ca = F$。
  - 取 $V(Ab)=T, V(Bb)=T, V(Cb)=F \implies Ab \land Bb = T$（前提 1 真），$Ab \land Cb = F$。
  - 結論 $(F \land T) \lor (T \land F) = F \lor F = F$！
  - $\implies$ 前提全真而結論為假，**論證無效**。
