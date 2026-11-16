# 講義補充：述詞邏輯量化定理與前綴移入移出 (Q17, Q18 定理)

## 述詞邏輯前綴移入移出重要定理 (Theorems on Quantifier Shifts)

當條件句中的前件或後件**不含有該量詞所量限拘束的自由變元**時，量詞可以合法移入或移出括弧。移入移出時須特別注意量詞的轉換：

### 定理 Q17 (前件量化全稱轉存在)
若命題 $P$ 中不含自由變元 $x$：
$$(x)(Fx \rightarrow P) \equiv [(\exists x)Fx \rightarrow P]$$
- **日常語意**：
  - 左式：「對任何人而言，若他動了，橋就會塌。」
  - 右式：「只要有人動了，橋就會塌。」
  - 兩者完全等價！
- **重要考點 (Ex 9, 10-6 第 3 題)**：
  “If any frontrunners don’t cater to all potential voters, then some longshots are going to win.”
  - 兩種符號化完全等價：
    $$(\exists x)[Fx \land \neg(y)(Vy \rightarrow Cxy)] \rightarrow (\exists x)(Lx \land Wx)$$
    $$(x)\{[Fx \land \neg(y)(Vy \rightarrow Cxy)] \rightarrow (\exists x)(Lx \land Wx)\}$$

### 定理 Q18 (前件量化存在轉全稱)
若命題 $P$ 中不含自由變元 $x$：
$$(\exists x)(Fx \rightarrow P) \equiv [(x)Fx \rightarrow P]$$
- **日常語意**：「如果所有人都移動了，則橋將會倒塌。」

---

## 複雜多元關係述詞翻譯範例 (Ex 9, 10-6 第 13 題)
- 題目：“If some of us owe money to Isaac Newton, then there will come a time when we should pay him what we owe.”
- 符號化結構（涉及人 $P$、金錢 $M$、欠錢關係 $O$、時間點 $T$、還錢關係 $B$）：
  $$(\exists x)[Px \land (\exists y)(My \land Oxyn)] \rightarrow (\exists x)\{Tx \land (y)(z)[(Py \land Mz \land Oyzn) \rightarrow Byznx]\}$$
