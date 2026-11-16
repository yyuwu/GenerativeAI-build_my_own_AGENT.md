# Exercise 2-7 & Exercise 2-10: 語句符號化與真值函應

## Exercise 2-7
1. If nothing is perfect, then I can’t be blamed for my mistakes. (N = “nothing is perfect”; B = “I can be blamed for my mistakes”)
   - **Ans.**：$N \rightarrow \neg B$
3. $(N \land M) \rightarrow B$
5. $E \rightarrow (\neg M \land \neg B)$
7. $M \rightarrow H$
9. $D \rightarrow G$
11. $\neg(S \land G) \rightarrow \neg D$ 或 $\neg D \lor (S \land G)$
13. $\neg C \land \neg L$ 或 $\neg(C \lor L)$
15. $M \land (S \lor B)$
17. $S \rightarrow (B \lor H)$ 或 $S \rightarrow (\neg H \rightarrow B)$
19. $(\neg D \land \neg E) \rightarrow G$ 或 $\neg(D \lor E) \rightarrow G$
21. $(\neg D \land \neg E) \land \neg G$ 或 $\neg(D \lor E) \land \neg G$
23. $B \land (\neg W \rightarrow O)$ 或 $B \land (\neg O \rightarrow W)$
25. $D \rightarrow (T \land S)$
27. $T \rightarrow (\neg D \rightarrow S)$ 或 $T \rightarrow (\neg S \rightarrow D)$
29. $(T \land S) \rightarrow (N \equiv D)$ 或 $(T \land S) \rightarrow (\neg N \equiv \neg D)$

---

## Exercise 2-10
1. **What’s wrong with abbreviating the sentence “George Plimpton is not a public figure” by the letter P?**
   - **Ans.**：因為 “George Plimpton is not a public figure” 是否定句，而 $P$ 是原子語句常元。在邏輯上，原子語句不含邏輯連接詞，因此 $P$ 無法揭示該語句含有否定詞的內在邏輯結構。

3. **Why isn’t the expression “It is well known that . . .” truth-functional?**
   - **Ans.**：“It is well known that …” 不是真值函應的。因為某些真的語句是眾所周知的，但某些真的語句卻不為人知。例如「眾所周知 2+2=4」為真；但「眾所周知小明愛小華」卻為假，即使「小明愛小華」事實上為真。其真假無法單由被連接語句的真值唯一決定，違反真值函應原則。

5. **Is the sentence “Lady Gaga and Stefani Joanne Angelina Germanotta are well-known public figures” atomic or compound?**
   - **Ans.**：是複合語句（Compound sentence）。因為 “and” 在此沒有「共同」或「一起行動」的意思。該句真值與「Lady Gaga is a well-known public figure and Stefani Joanne Angelina Germanotta is a well-known public figure」完全相同。

7. **And how about “Lady Gaga and Stefani Joanne Angelina Germanotta have been lifelong best friends”?**
   - **Ans.**：是原子語句（Atomic sentence）。因為 “and” 在此具有「彼此相互的終生摯友」的關係性意涵。若硬將其拆為兩句單句，則失去其相互關係的原意甚至無意義。
