---
title: 等同規則與反身律 (Identity Rule & Reflexivity)
aliases: [ID, IR, 等同規則, 萊布尼茲律, 等同反身律]
category: rules
tags:
  - 述詞邏輯
  - 等同
  - 萊布尼茲律
  - 推論規則
updated: 2026-11-17
sources:
  - "[[raw/lectures/ch11_等同與確定描述詞.md]]"
---

# 等同規則 (ID) 與 反身律 (IR)

當述詞邏輯擴展至包含等號「$=$」的一階等同邏輯（First-Order Logic with Identity）時，系統引入兩條專屬的核心公理與規則。

---

## 1. 等同規則 (Rule of Identity, ID / 萊布尼茲不可區分之同一性律)

### 1.1 形式定義
$$\begin{aligned}
& \phi(u) \\
& u = w \quad (\text{或 } w = u) \\
\hline
\therefore\ & \phi(w)
\end{aligned}$$
其中 $u, w$ 為任意個體常元或變元，$\phi(w)$ 是用 $w$ 替換 $\phi(u)$ 中自由出現的 $u$ 所得之結果。

### 1.2 哲學本質
- **相同事物的可替換性 (Substitutivity of Identicals)**：若兩名稱指向同一個實體（例如「金庸」$=$「查良鏞」），則任何關於金庸的客觀真陳述，在將名稱代換為查良鏞後，其真值保證完全不變。

---

## 2. 等同反身律 (Identity Reflexivity, IR)

### 2.1 形式定義
$$\vdash (x)(x = x)$$
在證明的任何步驟中，**均可直接引入零前提公理：$(x)(x = x)$**。

### 2.2 為什麼需要 IR？
在某些涉及等同的有效論證中（例如 $(x)[(x = a) \rightarrow Fx] \vdash Fa$），若缺少 IR，證明將陷入僵局，系統將不完備：
```markdown
1. (x)[(x = a) -> Fx]          (前提)  /∴ Fa
2. (a = a) -> Fa               (1 UI)
3. (x)(x = x)                  (IR，引入反身公理)
4. a = a                       (3 UI)
5. Fa                          (2, 4 MP)
Q.E.D.
```

---

## 3. 相關鏈結

- 哲學概念：[[等同與確定描述詞]]
- 有數量化：[[展開式與有數量化]]
- 證明體系：[[述詞邏輯演繹證明法]]
