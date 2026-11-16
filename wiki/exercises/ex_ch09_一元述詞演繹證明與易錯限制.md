---
title: 習題解析 Ch. 9 - 一元述詞演繹證明與易錯限制
aliases: [Exercise 9, 述詞演繹習題, 量詞規則防錯]
category: exercises
tags:
  - 習題詳解
  - 述詞邏輯
  - 演繹證明
  - 量詞限制
updated: 2026-11-17
sources:
  - "[[raw/problem_sets/exercises_ch09_一元述詞演繹證明.md]]"
  - "[[raw/problem_sets/quiz_述詞邏輯小考_05_06_07.md]]"
---

# 習題解析 Ch. 9：一元述詞演繹證明與易錯限制

本篇精選第九章與期末小考中關於識別無效量詞步驟、先 EI 後 UI 策略、QN 破除否定量詞以及綜合 CP/UG 的實戰推導。

---

## 一、 抓出常見無效推論步驟 (Ex 9-2 經典辨析)

在演繹證明作業中，初學者最常違反量詞五大限制：

1. **禁令：單向規則不可作用於局部子句**：
   - 錯誤步驟：$(x)[(Hx \land Kx) \rightarrow Mx],\ (\exists x)(Hx \land Kx) \vdash (\exists x)Mx$（第 4 步直接用 MP 推出 $Mx$）。
   - **辨析**：$(Hx \land Kx) \rightarrow Mx$ 是處在量詞控制下的子式，不是獨立語句，不能直接與第 2 步施行 MP！必須先將量詞消去。
2. **禁令：EI 必須引進全新變元**：
   - 錯誤步驟：第 3 步已由 UI 引進 $y$ 導出 $(Gy \lor Hy) \rightarrow My$，第 4 步又對 $(\exists x)(Fx \land \neg Mx)$ 做 EI 引進 $y$ 導出 $Fy \land \neg My$。
   - **辨析**：$y$ 已經被使用過，EI 必須引進全新的準變元（如 $z$），否則會造成不同存在項強行重合的嚴重錯誤！
3. **禁令：不可對 EI 引進的變元做全稱一般化 (UG)**：
   - 錯誤步驟：由存在引例得 $Px$，再對 $Px$ 做 UG 導出 $(x)Px$。
   - **辨析**：以偏概全！EI 的變元代表未知的特定個體，失去了任意性，嚴禁使用 UG。

---

## 二、 結合 QN 與 MT 的經典證明 (期末小考 7)

**題目**：$(\exists x)(Ax \land Bx) \rightarrow (y)Cy,\ \neg Ca \vdash (x)(Ax \rightarrow \neg Bx)$

```markdown
前提：
1. (∃x)(Ax · Bx) -> (y)Cy      (前提)
2. ~Ca                         (前提)  /∴ (x)(Ax -> ~Bx)

證明步驟：
3. (∃y)~Cy                     (2 EG)
4. ~(y)Cy                      (3 QN，將存在否定化為否定全稱)
5. ~(∃x)(Ax · Bx)              (1, 4 MT，成功觸發前件否定)
6. (x)~(Ax · Bx)               (5 QN，打開括弧前面的否定號！)
7. ~(Ax · Bx)                  (6 UI，提取任意代表 x)
8. ~Ax v ~Bx                   (7 DeM)
9. Ax -> ~Bx                   (8 Impl)
10. (x)(Ax -> ~Bx)             (9 UG，變元 x 具完全任意性)
Q.E.D.
```
> **戰略點評**：第 5 步到第 6 步是整個證明的命脈。**$\neg(\exists x)$ 不能直接做 UI**，必須先透過 **QN** 翻轉成 $(x)\neg$，才能合法施展 UI！

---

## 相關知識鏈結

- 推論規則與五大限制：[[量詞推論四規則_UI_UG_EI_EG]]
- 雙向置換工具：[[量詞否定規則_QN]]
- 證明方法論：[[述詞邏輯演繹證明法]]
