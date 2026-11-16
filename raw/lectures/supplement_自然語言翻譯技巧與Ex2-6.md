# 講義補充：自然語言翻譯技巧與 Exercise 2-6 (Textbook pp. 44-45)

## 翻譯心法與反向檢查 (Double-Check)
- **拒絕過度機械化**：自然語言的連接詞具有高度彈性與語境相依性。
- **雙向檢驗法**：將擬定好的符號邏輯式「反向翻譯回日常語言」，比對兩者是否在所有情境下具有相同的真值條件。

---

## 課本精選例題 (Examples 1-12)
- $A$: Art watched General Hospital
- $B$: Betsy watched General Hospital
- $F$: Betsy flunked chemistry
- $M$: a miracle occurred
- $G$: Melissa graduates with a strong academic record
- $J$: Melissa gets a good job
- $L$: Melissa makes lots of money
- $O$: Melissa pursues other goals
- $M$: we control the money supply
- $O$: we break the power of OPEC
- $I$: we control inflation
- $E$: the economy will collapse
- $D$: there is an international economic debacle

1. Art watched General Hospital, but Betsy didn’t. $\implies A \land \neg B$
2. If Art watched General Hospital, then Betsy didn’t. $\implies A \rightarrow \neg B$
3. If Betsy watched General Hospital, either she flunked her chemistry exam or a miracle occurred. $\implies B \rightarrow (F \lor M)$
4. If Betsy watched General Hospital and no miracle occurred, then she flunked her chemistry exam. $\implies (B \land \neg M) \rightarrow F$
5. Either Betsy watched General Hospital and a miracle occurred, or she flunked her chemistry exam. $\implies (B \land M) \lor F$
6. If Melissa graduates with a strong academic record, she gets a good job and makes lots of money. $\implies G \rightarrow (J \land L)$
7. If Melissa graduates with a strong academic record, she gets a good job and makes lots of money—if she doesn't pursue other goals. $\implies (G \land \neg O) \rightarrow (J \land L)$ 或 $G \rightarrow [\neg O \rightarrow (J \land L)]$
8. If Melissa doesn't make lots of money, then either she doesn't graduate with a strong academic record, or she doesn't get a good job, or she pursues other goals. $\implies \neg L \rightarrow [(\neg G \lor \neg J) \lor O]$
9. Melissa doesn't make lots of money or pursue other goals, but she does graduate with a strong academic record and she gets a good job. $\implies (\neg L \land \neg O) \land (G \land J)$
10. If we don’t control the money supply and break the power of OPEC, we won’t control inflation. $\implies \neg(M \land O) \rightarrow \neg I \equiv I \rightarrow (M \land O)$
11. Either we control the money supply and break the power of OPEC, or we won’t control inflation and the economy will collapse. $\implies (M \land O) \lor (\neg I \land E)$
12. If the economy collapses, we’ll know that we didn’t break the power of OPEC, or perhaps didn’t control the money supply—or maybe it’ll be because of some international economic debacle. $\implies E \rightarrow [(\neg O \lor \neg M) \lor D]$

---

## Exercise 2-6 原始題目
- $A$: Art attends class.
- $G$: Art graduates.
- $H$: Art completes his homework.
- $L$: Art does well in logic.
- $M$: Art does well in math.
- $P$: Art does well in philosophy.
- $T$: Art pays tuition.
- $W$: Art does well in all his classes.

1. Art does not do well in either logic or math.
2. If Art completes his homework, he does well in both logic and math.
3. If Art does not complete his homework, he does well in neither logic nor math.
4. If Art does well in logic or math, he graduates.
5. Art graduates only if he does well in logic or math.
6. If Art neither pays tuition nor attends classes, he does not graduate.
7. Art does well in logic if he completes his homework and attends class.
8. Art does well in logic only if he either completes his homework or attends class.
9. If Art pays his tuition, he graduates, unless he doesn’t attend class.
10. Art does well in all his classes if he does well in logic and philosophy.
11. Art does well in all his classes unless he doesn’t do well in logic or philosophy.
12. Art does well in all his classes only if he does well in logic, philosophy, and math.
