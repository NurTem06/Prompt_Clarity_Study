# Programming problems: Clear / Ambigious

45 pairs. Clear reproduces the original statement. Ambigious changes only the introductory problem description; the original constraints (where separately marked), input, output, examples, and subsequent notes are retained verbatim.


## Task 01 — problem_id 4045

### Clear

You are given two strings $s$ and $t$ both of length $2$ and both consisting only of characters 'a', 'b' and 'c'.

Possible examples of strings $s$ and $t$: "ab", "ca", "bb".

You have to find a string $res$ consisting of $3n$ characters, $n$ characters should be 'a', $n$ characters should be 'b' and $n$ characters should be 'c' and $s$ and $t$ should not occur in $res$ as substrings.

A substring of a string is a contiguous subsequence of that string. So, the strings "ab", "ac" and "cc" are substrings of the string "abacc", but the strings "bc", "aa" and "cb" are not substrings of the string "abacc".

If there are multiple answers, you can print any of them.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 10^5$) — the number of characters 'a', 'b' and 'c' in the resulting string.

The second line of the input contains one string $s$ of length $2$ consisting of characters 'a', 'b' and 'c'.

The third line of the input contains one string $t$ of length $2$ consisting of characters 'a', 'b' and 'c'.


-----Output-----

If it is impossible to find the suitable string, print "NO" on the first line. 

Otherwise print "YES" on the first line and string $res$ on the second line. $res$ should consist of $3n$ characters, $n$ characters should be 'a', $n$ characters should be 'b' and $n$ characters should be 'c' and $s$ and $t$ should not occur in $res$ as substrings.

If there are multiple answers, you can print any of them.


-----Examples-----
Input
2
ab
bc

Output
YES
acbbac

Input
3
aa
bc

Output
YES
cacbacbab

Input
1
cb
ac

Output
YES
abc

### Ambigious

You are given two short strings $s$ and $t$ made of 'a', 'b' and 'c'. Build a string $res$ using $n$ of each letter, arranging them so the given strings do not appear in the wrong places. The result should avoid those combinations when the letters are put togetehr. If several arrangements work, any is fine.

-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 10^5$) — the number of characters 'a', 'b' and 'c' in the resulting string.

The second line of the input contains one string $s$ of length $2$ consisting of characters 'a', 'b' and 'c'.

The third line of the input contains one string $t$ of length $2$ consisting of characters 'a', 'b' and 'c'.


-----Output-----

If it is impossible to find the suitable string, print "NO" on the first line. 

Otherwise print "YES" on the first line and string $res$ on the second line. $res$ should consist of $3n$ characters, $n$ characters should be 'a', $n$ characters should be 'b' and $n$ characters should be 'c' and $s$ and $t$ should not occur in $res$ as substrings.

If there are multiple answers, you can print any of them.


-----Examples-----
Input
2
ab
bc

Output
YES
acbbac

Input
3
aa
bc

Output
YES
cacbacbab

Input
1
cb
ac

Output
YES
abc

---


## Task 02 — problem_id 4046

### Clear

An array of integers $p_1, p_2, \dots, p_n$ is called a permutation if it contains each number from $1$ to $n$ exactly once. For example, the following arrays are permutations: $[3, 1, 2]$, $[1]$, $[1, 2, 3, 4, 5]$ and $[4, 3, 1, 2]$. The following arrays are not permutations: $[2]$, $[1, 1]$, $[2, 3, 4]$.

Polycarp invented a really cool permutation $p_1, p_2, \dots, p_n$ of length $n$. It is very disappointing, but he forgot this permutation. He only remembers the array $q_1, q_2, \dots, q_{n-1}$ of length $n-1$, where $q_i=p_{i+1}-p_i$.

Given $n$ and $q=q_1, q_2, \dots, q_{n-1}$, help Polycarp restore the invented permutation.


-----Input-----

The first line contains the integer $n$ ($2 \le n \le 2\cdot10^5$) — the length of the permutation to restore. The second line contains $n-1$ integers $q_1, q_2, \dots, q_{n-1}$ ($-n < q_i < n$).


-----Output-----

Print the integer -1 if there is no such permutation of length $n$ which corresponds to the given array $q$. Otherwise, if it exists, print $p_1, p_2, \dots, p_n$. Print any such permutation if there are many of them.


-----Examples-----
Input
3
-2 1

Output
3 1 2 
Input
5
1 1 1 1

Output
1 2 3 4 5 
Input
4
-1 2 2

Output
-1

### Ambigious

Polycarp forgot a permutation of length $n$, but kept an array $q$ describing the changes between its elements. Each value tells how one element differs from the next one. Restore the permutation from these differnces, or report that it cannot be restored.

-----Input-----

The first line contains the integer $n$ ($2 \le n \le 2\cdot10^5$) — the length of the permutation to restore. The second line contains $n-1$ integers $q_1, q_2, \dots, q_{n-1}$ ($-n < q_i < n$).


-----Output-----

Print the integer -1 if there is no such permutation of length $n$ which corresponds to the given array $q$. Otherwise, if it exists, print $p_1, p_2, \dots, p_n$. Print any such permutation if there are many of them.


-----Examples-----
Input
3
-2 1

Output
3 1 2 
Input
5
1 1 1 1

Output
1 2 3 4 5 
Input
4
-1 2 2

Output
-1

---


## Task 03 — problem_id 4047

### Clear

You are given $n$ chips on a number line. The $i$-th chip is placed at the integer coordinate $x_i$. Some chips can have equal coordinates.

You can perform each of the two following types of moves any (possibly, zero) number of times on any chip:

  Move the chip $i$ by $2$ to the left or $2$ to the right for free (i.e. replace the current coordinate $x_i$ with $x_i - 2$ or with $x_i + 2$);  move the chip $i$ by $1$ to the left or $1$ to the right and pay one coin for this move (i.e. replace the current coordinate $x_i$ with $x_i - 1$ or with $x_i + 1$). 

Note that it's allowed to move chips to any integer coordinate, including negative and zero.

Your task is to find the minimum total number of coins required to move all $n$ chips to the same coordinate (i.e. all $x_i$ should be equal after some sequence of moves).


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of chips.

The second line of the input contains $n$ integers $x_1, x_2, \dots, x_n$ ($1 \le x_i \le 10^9$), where $x_i$ is the coordinate of the $i$-th chip.


-----Output-----

Print one integer — the minimum total number of coins required to move all $n$ chips to the same coordinate.


-----Examples-----
Input
3
1 2 3

Output
1

Input
5
2 2 2 3 3

Output
2



-----Note-----

In the first example you need to move the first chip by $2$ to the right and the second chip by $1$ to the right or move the third chip by $2$ to the left and the second chip by $1$ to the left so the answer is $1$.

In the second example you need to move two chips with coordinate $3$ by $1$ to the left so the answer is $2$.

### Ambigious

There are $n$ chips at integer coordinates $x_i$, possibly sharing a position. You can shift chips left or right: a move of two is free, while a move of one costs a coin. Bring the chips together as cheaply as possible. Moves may be combined, and the final place should be one of the suitable positons.

-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of chips.

The second line of the input contains $n$ integers $x_1, x_2, \dots, x_n$ ($1 \le x_i \le 10^9$), where $x_i$ is the coordinate of the $i$-th chip.


-----Output-----

Print one integer — the minimum total number of coins required to move all $n$ chips to the same coordinate.


-----Examples-----
Input
3
1 2 3

Output
1

Input
5
2 2 2 3 3

Output
2



-----Note-----

In the first example you need to move the first chip by $2$ to the right and the second chip by $1$ to the right or move the third chip by $2$ to the left and the second chip by $1$ to the left so the answer is $1$.

In the second example you need to move two chips with coordinate $3$ by $1$ to the left so the answer is $2$.

---


## Task 04 — problem_id 4048

### Clear

Takahashi is standing on a multiplication table with infinitely many rows and columns.
The square (i,j) contains the integer i \times j. Initially, Takahashi is standing at (1,1).
In one move, he can move from (i,j) to either (i+1,j) or (i,j+1).
Given an integer N, find the minimum number of moves needed to reach a square that contains N.

-----Constraints-----
 - 2 \leq N \leq 10^{12}
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the minimum number of moves needed to reach a square that contains the integer N.

-----Sample Input-----
10

-----Sample Output-----
5

(2,5) can be reached in five moves. We cannot reach a square that contains 10 in less than five moves.

### Ambigious

Takahashi stands on an infinite multiplication table, where square $(i,j)$ contains $i \times j$. He starts in the first square and can move towards the next row or column. Find how many moves are needed to get to $N$, choosing the closest suitable square. Count the steps from the start in the usual way, not the whole traveld route.

-----Constraints-----
 - 2 \leq N \leq 10^{12}
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the minimum number of moves needed to reach a square that contains the integer N.

-----Sample Input-----
10

-----Sample Output-----
5

(2,5) can be reached in five moves. We cannot reach a square that contains 10 in less than five moves.

---


## Task 05 — problem_id 4049

### Clear

Alice and Bob have decided to play the game "Rock, Paper, Scissors". 

The game consists of several rounds, each round is independent of each other. In each round, both players show one of the following things at the same time: rock, paper or scissors. If both players showed the same things then the round outcome is a draw. Otherwise, the following rules applied:

  if one player showed rock and the other one showed scissors, then the player who showed rock is considered the winner and the other one is considered the loser;  if one player showed scissors and the other one showed paper, then the player who showed scissors is considered the winner and the other one is considered the loser;  if one player showed paper and the other one showed rock, then the player who showed paper is considered the winner and the other one is considered the loser. 

Alice and Bob decided to play exactly $n$ rounds of the game described above. Alice decided to show rock $a_1$ times, show scissors $a_2$ times and show paper $a_3$ times. Bob decided to show rock $b_1$ times, show scissors $b_2$ times and show paper $b_3$ times. Though, both Alice and Bob did not choose the sequence in which they show things. It is guaranteed that $a_1 + a_2 + a_3 = n$ and $b_1 + b_2 + b_3 = n$.

Your task is to find two numbers:

  the minimum number of round Alice can win;  the maximum number of rounds Alice can win. 


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 10^{9}$) — the number of rounds.

The second line of the input contains three integers $a_1, a_2, a_3$ ($0 \le a_i \le n$) — the number of times Alice will show rock, scissors and paper, respectively. It is guaranteed that $a_1 + a_2 + a_3 = n$.

The third line of the input contains three integers $b_1, b_2, b_3$ ($0 \le b_j \le n$) — the number of times Bob will show rock, scissors and paper, respectively. It is guaranteed that $b_1 + b_2 + b_3 = n$.


-----Output-----

Print two integers: the minimum and the maximum number of rounds Alice can win.


-----Examples-----
Input
2
0 1 1
1 1 0

Output
0 1

Input
15
5 5 5
5 5 5

Output
0 15

Input
3
0 0 3
3 0 0

Output
3 3

Input
686
479 178 29
11 145 530

Output
22 334

Input
319
10 53 256
182 103 34

Output
119 226



-----Note-----

In the first example, Alice will not win any rounds if she shows scissors and then paper and Bob shows rock and then scissors. In the best outcome, Alice will win one round if she shows paper and then scissors, and Bob shows rock and then scissors.

In the second example, Alice will not win any rounds if Bob shows the same things as Alice each round.

In the third example, Alice always shows paper and Bob always shows rock so Alice will win all three rounds anyway.

### Ambigious

Alice and Bob play $n$ rounds of rock, scissors and paper with the usual winning rules. Their numbers of each gesture are $a_1,a_2,a_3$ and $b_1,b_2,b_3$, but the order has not been fixed. Find the smallest and largest number of wins Alice can get when the rounds are arranged. The players may choose their order to get the required result, taking the other player's choices into acount.

-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 10^{9}$) — the number of rounds.

The second line of the input contains three integers $a_1, a_2, a_3$ ($0 \le a_i \le n$) — the number of times Alice will show rock, scissors and paper, respectively. It is guaranteed that $a_1 + a_2 + a_3 = n$.

The third line of the input contains three integers $b_1, b_2, b_3$ ($0 \le b_j \le n$) — the number of times Bob will show rock, scissors and paper, respectively. It is guaranteed that $b_1 + b_2 + b_3 = n$.


-----Output-----

Print two integers: the minimum and the maximum number of rounds Alice can win.


-----Examples-----
Input
2
0 1 1
1 1 0

Output
0 1

Input
15
5 5 5
5 5 5

Output
0 15

Input
3
0 0 3
3 0 0

Output
3 3

Input
686
479 178 29
11 145 530

Output
22 334

Input
319
10 53 256
182 103 34

Output
119 226



-----Note-----

In the first example, Alice will not win any rounds if she shows scissors and then paper and Bob shows rock and then scissors. In the best outcome, Alice will win one round if she shows paper and then scissors, and Bob shows rock and then scissors.

In the second example, Alice will not win any rounds if Bob shows the same things as Alice each round.

In the third example, Alice always shows paper and Bob always shows rock so Alice will win all three rounds anyway.

---


## Task 06 — problem_id 4050

### Clear

This problem is given in two editions, which differ exclusively in the constraints on the number $n$.

You are given an array of integers $a[1], a[2], \dots, a[n].$ A block is a sequence of contiguous (consecutive) elements $a[l], a[l+1], \dots, a[r]$ ($1 \le l \le r \le n$). Thus, a block is defined by a pair of indices $(l, r)$.

Find a set of blocks $(l_1, r_1), (l_2, r_2), \dots, (l_k, r_k)$ such that:

  They do not intersect (i.e. they are disjoint). Formally, for each pair of blocks $(l_i, r_i)$ and $(l_j, r_j$) where $i \neq j$ either $r_i < l_j$ or $r_j < l_i$.  For each block the sum of its elements is the same. Formally, $$a[l_1]+a[l_1+1]+\dots+a[r_1]=a[l_2]+a[l_2+1]+\dots+a[r_2]=$$ $$\dots =$$ $$a[l_k]+a[l_k+1]+\dots+a[r_k].$$  The number of the blocks in the set is maximum. Formally, there does not exist a set of blocks $(l_1', r_1'), (l_2', r_2'), \dots, (l_{k'}', r_{k'}')$ satisfying the above two requirements with $k' > k$. 

 $\left. \begin{array}{|l|l|l|l|l|l|} \hline 4 & {1} & {2} & {2} & {1} & {5} & {3} \\ \hline \end{array} \right.$ The picture corresponds to the first example. Blue boxes illustrate blocks. 

Write a program to find such a set of blocks.


-----Input-----

The first line contains integer $n$ ($1 \le n \le 50$) — the length of the given array. The second line contains the sequence of elements $a[1], a[2], \dots, a[n]$ ($-10^5 \le a_i \le 10^5$).


-----Output-----

In the first line print the integer $k$ ($1 \le k \le n$). The following $k$ lines should contain blocks, one per line. In each line print a pair of indices $l_i, r_i$ ($1 \le l_i \le r_i \le n$) — the bounds of the $i$-th block. You can print blocks in any order. If there are multiple answers, print any of them.


-----Examples-----
Input
7
4 1 2 2 1 5 3

Output
3
7 7
2 3
4 5

Input
11
-5 -4 -3 -2 -1 0 1 2 3 4 5

Output
2
3 4
1 1

Input
4
1 1 1 1

Output
4
4 4
1 1
2 2
3 3

### Ambigious

Given an integer array, choose as many blocks as possible with equal totals. A block is taken from a range of the array, and the chosen blocks should stay separate, though touching boundaries can be handled as usual. Find a largest collection with the same sum; unused elements do not have to be included. Output the block positons.

-----Input-----

The first line contains integer $n$ ($1 \le n \le 50$) — the length of the given array. The second line contains the sequence of elements $a[1], a[2], \dots, a[n]$ ($-10^5 \le a_i \le 10^5$).


-----Output-----

In the first line print the integer $k$ ($1 \le k \le n$). The following $k$ lines should contain blocks, one per line. In each line print a pair of indices $l_i, r_i$ ($1 \le l_i \le r_i \le n$) — the bounds of the $i$-th block. You can print blocks in any order. If there are multiple answers, print any of them.


-----Examples-----
Input
7
4 1 2 2 1 5 3

Output
3
7 7
2 3
4 5

Input
11
-5 -4 -3 -2 -1 0 1 2 3 4 5

Output
2
3 4
1 1

Input
4
1 1 1 1

Output
4
4 4
1 1
2 2
3 3

---


## Task 07 — problem_id 4051

### Clear

Everybody knows of spaghetti sort. You decided to implement an analog sorting algorithm yourself, but as you survey your pantry you realize you're out of spaghetti! The only type of pasta you have is ravioli, but you are not going to let this stop you...

You come up with the following algorithm. For each number in the array a_{i}, build a stack of a_{i} ravioli. The image shows the stack for a_{i} = 4.

 [Image] 

Arrange the stacks in one row in the order in which the corresponding numbers appear in the input array. Find the tallest one (if there are several stacks of maximal height, use the leftmost one). Remove it and add its height to the end of the output array. Shift the stacks in the row so that there is no gap between them. Repeat the procedure until all stacks have been removed.

At first you are very happy with your algorithm, but as you try it on more inputs you realize that it doesn't always produce the right sorted array. Turns out when two stacks of ravioli are next to each other (at any step of the process) and differ in height by two or more, the top ravioli of the taller stack slides down on top of the lower stack.

Given an input array, figure out whether the described algorithm will sort it correctly.


-----Input-----

The first line of input contains a single number n (1 ≤ n ≤ 10) — the size of the array.

The second line of input contains n space-separated integers a_{i} (1 ≤ a_{i} ≤ 100) — the elements of the array.


-----Output-----

Output "YES" if the array can be sorted using the described procedure and "NO" if it can not.


-----Examples-----
Input
3
1 2 3

Output
YES

Input
3
3 1 2

Output
NO



-----Note-----

In the second example the array will change even before the tallest stack is chosen for the first time: ravioli from stack of height 3 will slide on the stack of height 1, and the algorithm will output an array {2, 2, 2}.

### Ambigious

Build stacks of ravioli with heights given by the array and keep them in input order. Repeatedly take a tallest stack, preferring the left one, and write its height to the result. Nearby stacks may spill ravioli when their heights differ too much, changing the heights during the process. Decide whether this procedure still sorts the original numbers corectly.

-----Input-----

The first line of input contains a single number n (1 ≤ n ≤ 10) — the size of the array.

The second line of input contains n space-separated integers a_{i} (1 ≤ a_{i} ≤ 100) — the elements of the array.


-----Output-----

Output "YES" if the array can be sorted using the described procedure and "NO" if it can not.


-----Examples-----
Input
3
1 2 3

Output
YES

Input
3
3 1 2

Output
NO



-----Note-----

In the second example the array will change even before the tallest stack is chosen for the first time: ravioli from stack of height 3 will slide on the stack of height 1, and the algorithm will output an array {2, 2, 2}.

---


## Task 08 — problem_id 4052

### Clear

You are given two strings $s$ and $t$. Both strings have length $n$ and consist of lowercase Latin letters. The characters in the strings are numbered from $1$ to $n$.

You can successively perform the following move any number of times (possibly, zero):  swap any two adjacent (neighboring) characters of $s$ (i.e. for any $i = \{1, 2, \dots, n - 1\}$ you can swap $s_i$ and $s_{i + 1})$. 

You can't apply a move to the string $t$. The moves are applied to the string $s$ one after another.

Your task is to obtain the string $t$ from the string $s$. Find any way to do it with at most $10^4$ such moves.

You do not have to minimize the number of moves, just find any sequence of moves of length $10^4$ or less to transform $s$ into $t$.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 50$) — the length of strings $s$ and $t$.

The second line of the input contains the string $s$ consisting of $n$ lowercase Latin letters.

The third line of the input contains the string $t$ consisting of $n$ lowercase Latin letters.


-----Output-----

If it is impossible to obtain the string $t$ using moves, print "-1".

Otherwise in the first line print one integer $k$ — the number of moves to transform $s$ to $t$. Note that $k$ must be an integer number between $0$ and $10^4$ inclusive.

In the second line print $k$ integers $c_j$ ($1 \le c_j < n$), where $c_j$ means that on the $j$-th move you swap characters $s_{c_j}$ and $s_{c_j + 1}$.

If you do not need to apply any moves, print a single integer $0$ in the first line and either leave the second line empty or do not print it at all.


-----Examples-----
Input
6
abcdef
abdfec

Output
4
3 5 4 5 

Input
4
abcd
accd

Output
-1



-----Note-----

In the first example the string $s$ changes as follows: "abcdef" $\rightarrow$ "abdcef" $\rightarrow$ "abdcfe" $\rightarrow$ "abdfce" $\rightarrow$ "abdfec".

In the second example there is no way to transform the string $s$ into the string $t$ through any allowed moves.

### Ambigious

You are given strings $s$ and $t$ of the same length. Transform $s$ into $t$ by exchanging nearby characters, leaving $t$ unchanged. Perform at most $10^4$ moves; the exchange positions should describe the neighboring letters involved at that stage. You do not need the shortest sequence, just a vaild one.

-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 50$) — the length of strings $s$ and $t$.

The second line of the input contains the string $s$ consisting of $n$ lowercase Latin letters.

The third line of the input contains the string $t$ consisting of $n$ lowercase Latin letters.


-----Output-----

If it is impossible to obtain the string $t$ using moves, print "-1".

Otherwise in the first line print one integer $k$ — the number of moves to transform $s$ to $t$. Note that $k$ must be an integer number between $0$ and $10^4$ inclusive.

In the second line print $k$ integers $c_j$ ($1 \le c_j < n$), where $c_j$ means that on the $j$-th move you swap characters $s_{c_j}$ and $s_{c_j + 1}$.

If you do not need to apply any moves, print a single integer $0$ in the first line and either leave the second line empty or do not print it at all.


-----Examples-----
Input
6
abcdef
abdfec

Output
4
3 5 4 5 

Input
4
abcd
accd

Output
-1



-----Note-----

In the first example the string $s$ changes as follows: "abcdef" $\rightarrow$ "abdcef" $\rightarrow$ "abdcfe" $\rightarrow$ "abdfce" $\rightarrow$ "abdfec".

In the second example there is no way to transform the string $s$ into the string $t$ through any allowed moves.

---


## Task 09 — problem_id 4053

### Clear

Ivan wants to play a game with you. He picked some string $s$ of length $n$ consisting only of lowercase Latin letters. 

You don't know this string. Ivan has informed you about all its improper prefixes and suffixes (i.e. prefixes and suffixes of lengths from $1$ to $n-1$), but he didn't tell you which strings are prefixes and which are suffixes.

Ivan wants you to guess which of the given $2n-2$ strings are prefixes of the given string and which are suffixes. It may be impossible to guess the string Ivan picked (since multiple strings may give the same set of suffixes and prefixes), but Ivan will accept your answer if there is at least one string that is consistent with it. Let the game begin!


-----Input-----

The first line of the input contains one integer number $n$ ($2 \le n \le 100$) — the length of the guessed string $s$.

The next $2n-2$ lines are contain prefixes and suffixes, one per line. Each of them is the string of length from $1$ to $n-1$ consisting only of lowercase Latin letters. They can be given in arbitrary order.

It is guaranteed that there are exactly $2$ strings of each length from $1$ to $n-1$. It is also guaranteed that these strings are prefixes and suffixes of some existing string of length $n$.


-----Output-----

Print one string of length $2n-2$ — the string consisting only of characters 'P' and 'S'. The number of characters 'P' should be equal to the number of characters 'S'. The $i$-th character of this string should be 'P' if the $i$-th of the input strings is the prefix and 'S' otherwise.

If there are several possible answers, you can print any.


-----Examples-----
Input
5
ba
a
abab
a
aba
baba
ab
aba

Output
SPPSPSPS

Input
3
a
aa
aa
a

Output
PPSS

Input
2
a
c

Output
PS



-----Note-----

The only string which Ivan can guess in the first example is "ababa".

The only string which Ivan can guess in the second example is "aaa". Answers "SPSP", "SSPP" and "PSPS" are also acceptable.

In the third example Ivan can guess the string "ac" or the string "ca". The answer "SP" is also acceptable.

### Ambigious

Ivan chose a lowercase string of length $n$ and gave you its shorter starting and ending pieces, without saying which kind each piece is. Label the given strings as prefixes or suffixes so they can belong to a common string. If a piece fits both ends, assign it where it is needed; the listed pieces should account for the required lengths in some consistant way.

-----Input-----

The first line of the input contains one integer number $n$ ($2 \le n \le 100$) — the length of the guessed string $s$.

The next $2n-2$ lines are contain prefixes and suffixes, one per line. Each of them is the string of length from $1$ to $n-1$ consisting only of lowercase Latin letters. They can be given in arbitrary order.

It is guaranteed that there are exactly $2$ strings of each length from $1$ to $n-1$. It is also guaranteed that these strings are prefixes and suffixes of some existing string of length $n$.


-----Output-----

Print one string of length $2n-2$ — the string consisting only of characters 'P' and 'S'. The number of characters 'P' should be equal to the number of characters 'S'. The $i$-th character of this string should be 'P' if the $i$-th of the input strings is the prefix and 'S' otherwise.

If there are several possible answers, you can print any.


-----Examples-----
Input
5
ba
a
abab
a
aba
baba
ab
aba

Output
SPPSPSPS

Input
3
a
aa
aa
a

Output
PPSS

Input
2
a
c

Output
PS



-----Note-----

The only string which Ivan can guess in the first example is "ababa".

The only string which Ivan can guess in the second example is "aaa". Answers "SPSP", "SSPP" and "PSPS" are also acceptable.

In the third example Ivan can guess the string "ac" or the string "ca". The answer "SP" is also acceptable.

---


## Task 10 — problem_id 4054

### Clear

Salve, mi amice.

Et tu quidem de lapis philosophorum. Barba non facit philosophum. Labor omnia vincit. Non potest creatio ex nihilo. Necesse est partibus.

Rp:

    I Aqua Fortis

    I Aqua Regia

    II Amalgama

    VII Minium

    IV Vitriol

Misce in vitro et æstus, et nil admirari. Festina lente, et nulla tenaci invia est via.

Fac et spera,

Vale,

Nicolas Flamel


-----Input-----

The first line of input contains several space-separated integers a_{i} (0 ≤ a_{i} ≤ 100).


-----Output-----

Print a single integer.


-----Examples-----
Input
2 4 6 8 10

Output
1

### Ambigious

Salve, mi amice.

De lapis philosophorum: aqua et metalla in vitro misce. Partes serva, sed eas pro rebus datis compone; quod deest ex reliquis accipe.

Rp: I Aqua Fortis, I Aqua Regia, II Amalgama, VII Minium, IV Vitriol.

Aestus adhibe donec res conveniat. Numeros aptos invenire debes, secundum eandem rationem aut partium summam, ut opus perficiatr.

Vale, Nicolas Flamel.

-----Input-----

The first line of input contains several space-separated integers a_{i} (0 ≤ a_{i} ≤ 100).


-----Output-----

Print a single integer.


-----Examples-----
Input
2 4 6 8 10

Output
1

---


## Task 11 — problem_id 4055

### Clear

There is a house with $n$ flats situated on the main street of Berlatov. Vova is watching this house every night. The house can be represented as an array of $n$ integer numbers $a_1, a_2, \dots, a_n$, where $a_i = 1$ if in the $i$-th flat the light is on and $a_i = 0$ otherwise.

Vova thinks that people in the $i$-th flats are disturbed and cannot sleep if and only if $1 < i < n$ and $a_{i - 1} = a_{i + 1} = 1$ and $a_i = 0$.

Vova is concerned by the following question: what is the minimum number $k$ such that if people from exactly $k$ pairwise distinct flats will turn off the lights then nobody will be disturbed? Your task is to find this number $k$.


-----Input-----

The first line of the input contains one integer $n$ ($3 \le n \le 100$) — the number of flats in the house.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($a_i \in \{0, 1\}$), where $a_i$ is the state of light in the $i$-th flat.


-----Output-----

Print only one integer — the minimum number $k$ such that if people from exactly $k$ pairwise distinct flats will turn off the light then nobody will be disturbed.


-----Examples-----
Input
10
1 1 0 1 1 0 1 0 1 0

Output
2

Input
5
1 1 0 0 0

Output
0

Input
4
1 1 1 1

Output
0



-----Note-----

In the first example people from flats $2$ and $7$ or $4$ and $7$ can turn off the light and nobody will be disturbed. It can be shown that there is no better answer in this example.

There are no disturbed people in second and third examples.

### Ambigious

The lights of $n$ flats are represented by zeros and ones. A person may be disturbed when their flat is dark and lights are on around it. Turn off lights in as few flats as possible so that these unpleasant patterns disappear. Check the nearby flats after the changes; flats at the ends are treated as boundary cases in the normal way. Find the minimum numbr of changes.

-----Input-----

The first line of the input contains one integer $n$ ($3 \le n \le 100$) — the number of flats in the house.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($a_i \in \{0, 1\}$), where $a_i$ is the state of light in the $i$-th flat.


-----Output-----

Print only one integer — the minimum number $k$ such that if people from exactly $k$ pairwise distinct flats will turn off the light then nobody will be disturbed.


-----Examples-----
Input
10
1 1 0 1 1 0 1 0 1 0

Output
2

Input
5
1 1 0 0 0

Output
0

Input
4
1 1 1 1

Output
0



-----Note-----

In the first example people from flats $2$ and $7$ or $4$ and $7$ can turn off the light and nobody will be disturbed. It can be shown that there is no better answer in this example.

There are no disturbed people in second and third examples.

---


## Task 12 — problem_id 4056

### Clear

You are given an array $a$ consisting of $n$ integers.

Your task is to say the number of such positive integers $x$ such that $x$ divides each number from the array. In other words, you have to find the number of common divisors of all elements in the array.

For example, if the array $a$ will be $[2, 4, 6, 2, 10]$, then $1$ and $2$ divide each number from the array (so the answer for this test is $2$).


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 4 \cdot 10^5$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^{12}$), where $a_i$ is the $i$-th element of $a$.


-----Output-----

Print one integer — the number of such positive integers $x$ such that $x$ divides each number from the given array (in other words, the answer is the number of common divisors of all elements in the array).


-----Examples-----
Input
5
1 2 3 4 5

Output
1

Input
6
6 90 12 18 30 18

Output
4

### Ambigious

Given an array of $n$ integers, count the positive numbers that divide the array elements. The divisor should work for the numbers together, so do not count the same value several times when it appears for different elements. Return the total number of suitable divisors for the whole aray.

-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 4 \cdot 10^5$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^{12}$), where $a_i$ is the $i$-th element of $a$.


-----Output-----

Print one integer — the number of such positive integers $x$ such that $x$ divides each number from the given array (in other words, the answer is the number of common divisors of all elements in the array).


-----Examples-----
Input
5
1 2 3 4 5

Output
1

Input
6
6 90 12 18 30 18

Output
4

---


## Task 13 — problem_id 4057

### Clear

Polycarp has $n$ coins, the value of the $i$-th coin is $a_i$. Polycarp wants to distribute all the coins between his pockets, but he cannot put two coins with the same value into the same pocket.

For example, if Polycarp has got six coins represented as an array $a = [1, 2, 4, 3, 3, 2]$, he can distribute the coins into two pockets as follows: $[1, 2, 3], [2, 3, 4]$.

Polycarp wants to distribute all the coins with the minimum number of used pockets. Help him to do that.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of coins.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$) — values of coins.


-----Output-----

Print only one integer — the minimum number of pockets Polycarp needs to distribute all the coins so no two coins with the same value are put into the same pocket.


-----Examples-----
Input
6
1 2 4 3 3 2

Output
2

Input
1
100

Output
1

### Ambigious

Polycarp wants to distribute all his coins among pockets. Coins have values $a_i$, and repeated values should be separated when putting them away. Use the smallest number of pockets that lets him store all the coins without an unwanted repeat. The order in which coins are put into pockets may also be choosen.

-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the number of coins.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$) — values of coins.


-----Output-----

Print only one integer — the minimum number of pockets Polycarp needs to distribute all the coins so no two coins with the same value are put into the same pocket.


-----Examples-----
Input
6
1 2 4 3 3 2

Output
2

Input
1
100

Output
1

---


## Task 14 — problem_id 4058

### Clear

Vova's house is an array consisting of $n$ elements (yeah, this is the first problem, I think, where someone lives in the array). There are heaters in some positions of the array. The $i$-th element of the array is $1$ if there is a heater in the position $i$, otherwise the $i$-th element of the array is $0$.

Each heater has a value $r$ ($r$ is the same for all heaters). This value means that the heater at the position $pos$ can warm up all the elements in range $[pos - r + 1; pos + r - 1]$.

Vova likes to walk through his house while he thinks, and he hates cold positions of his house. Vova wants to switch some of his heaters on in such a way that each element of his house will be warmed up by at least one heater. 

Vova's target is to warm up the whole house (all the elements of the array), i.e. if $n = 6$, $r = 2$ and heaters are at positions $2$ and $5$, then Vova can warm up the whole house if he switches all the heaters in the house on (then the first $3$ elements will be warmed up by the first heater and the last $3$ elements will be warmed up by the second heater).

Initially, all the heaters are off.

But from the other hand, Vova didn't like to pay much for the electricity. So he wants to switch the minimum number of heaters on in such a way that each element of his house is warmed up by at least one heater.

Your task is to find this number of heaters or say that it is impossible to warm up the whole house.


-----Input-----

The first line of the input contains two integers $n$ and $r$ ($1 \le n, r \le 1000$) — the number of elements in the array and the value of heaters.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($0 \le a_i \le 1$) — the Vova's house description.


-----Output-----

Print one integer — the minimum number of heaters needed to warm up the whole house or -1 if it is impossible to do it.


-----Examples-----
Input
6 2
0 1 1 0 0 1

Output
3

Input
5 3
1 0 0 0 1

Output
2

Input
5 10
0 0 0 0 0

Output
-1

Input
10 3
0 0 1 1 0 1 0 0 0 1

Output
3



-----Note-----

In the first example the heater at the position $2$ warms up elements $[1; 3]$, the heater at the position $3$ warms up elements $[2, 4]$ and the heater at the position $6$ warms up elements $[5; 6]$ so the answer is $3$.

In the second example the heater at the position $1$ warms up elements $[1; 3]$ and the heater at the position $5$ warms up elements $[3; 5]$ so the answer is $2$.

In the third example there are no heaters so the answer is -1.

In the fourth example the heater at the position $3$ warms up elements $[1; 5]$, the heater at the position $6$ warms up elements $[4; 8]$ and the heater at the position $10$ warms up elements $[8; 10]$ so the answer is $3$.

### Ambigious

A house is an array, with heaters at positions marked by one. Each heater warms nearby positions according to the common range $r$, extending to either side of its position. Switch on as few heaters as possible so the entire house is warm. The heater's own position belongs to its range; count the reach near its ends in the usual way. If the available heaters cannot cover it, say so. Initially they are all offf.

-----Input-----

The first line of the input contains two integers $n$ and $r$ ($1 \le n, r \le 1000$) — the number of elements in the array and the value of heaters.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($0 \le a_i \le 1$) — the Vova's house description.


-----Output-----

Print one integer — the minimum number of heaters needed to warm up the whole house or -1 if it is impossible to do it.


-----Examples-----
Input
6 2
0 1 1 0 0 1

Output
3

Input
5 3
1 0 0 0 1

Output
2

Input
5 10
0 0 0 0 0

Output
-1

Input
10 3
0 0 1 1 0 1 0 0 0 1

Output
3



-----Note-----

In the first example the heater at the position $2$ warms up elements $[1; 3]$, the heater at the position $3$ warms up elements $[2, 4]$ and the heater at the position $6$ warms up elements $[5; 6]$ so the answer is $3$.

In the second example the heater at the position $1$ warms up elements $[1; 3]$ and the heater at the position $5$ warms up elements $[3; 5]$ so the answer is $2$.

In the third example there are no heaters so the answer is -1.

In the fourth example the heater at the position $3$ warms up elements $[1; 5]$, the heater at the position $6$ warms up elements $[4; 8]$ and the heater at the position $10$ warms up elements $[8; 10]$ so the answer is $3$.

---


## Task 15 — problem_id 4059

### Clear

Given is a positive integer N.
How many tuples (A,B,C) of positive integers satisfy A \times B + C = N?

-----Constraints-----
 -  2 \leq N \leq 10^6
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the answer.

-----Sample Input-----
3

-----Sample Output-----
3

There are 3 tuples of integers that satisfy A \times B + C = 3: (A, B, C) = (1, 1, 2), (1, 2, 1), (2, 1, 1).

### Ambigious

Given a positive integer $N$, count the choices of positive integers $A,B,C$ for which the product of the first two plus the third gives $N$. Count different choices only once; swapping the two multiplied values should be handled as the same sort of choice. Find the total numbr of valid triples.

-----Constraints-----
 -  2 \leq N \leq 10^6
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the answer.

-----Sample Input-----
3

-----Sample Output-----
3

There are 3 tuples of integers that satisfy A \times B + C = 3: (A, B, C) = (1, 1, 2), (1, 2, 1), (2, 1, 1).

---


## Task 16 — problem_id 45

### Clear

You are given positive integer number n. You should create such strictly increasing sequence of k positive numbers a_1, a_2, ..., a_{k}, that their sum is equal to n and greatest common divisor is maximal.

Greatest common divisor of sequence is maximum of such numbers that every element of sequence is divisible by them.

If there is no possible sequence then output -1.


-----Input-----

The first line consists of two numbers n and k (1 ≤ n, k ≤ 10^10).


-----Output-----

If the answer exists then output k numbers — resulting sequence. Otherwise output -1. If there are multiple answers, print any of them.


-----Examples-----
Input
6 3

Output
1 2 3

Input
8 2

Output
2 6

Input
5 3

Output
-1

### Ambigious

Given $n$ and $k$, construct $k$ increasing positive numbers whose total is $n$. Make their common divisor as large as possible. The numbers should grow along the sequence, with equality treated according to the increasing-order requirement. If there is no suitable sequence, print -1. Any optimal sequence can be choosen.

-----Input-----

The first line consists of two numbers n and k (1 ≤ n, k ≤ 10^10).


-----Output-----

If the answer exists then output k numbers — resulting sequence. Otherwise output -1. If there are multiple answers, print any of them.


-----Examples-----
Input
6 3

Output
1 2 3

Input
8 2

Output
2 6

Input
5 3

Output
-1

---


## Task 17 — problem_id 46

### Clear

After finishing eating her bun, Alyona came up with two integers n and m. She decided to write down two columns of integers — the first column containing integers from 1 to n and the second containing integers from 1 to m. Now the girl wants to count how many pairs of integers she can choose, one from the first column and the other from the second column, such that their sum is divisible by 5.

Formally, Alyona wants to count the number of pairs of integers (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m and $(x + y) \operatorname{mod} 5$ equals 0.

As usual, Alyona has some troubles and asks you to help.


-----Input-----

The only line of the input contains two integers n and m (1 ≤ n, m ≤ 1 000 000).


-----Output-----

Print the only integer — the number of pairs of integers (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m and (x + y) is divisible by 5.


-----Examples-----
Input
6 12

Output
14

Input
11 14

Output
31

Input
1 5

Output
1

Input
3 8

Output
5

Input
5 7

Output
7

Input
21 21

Output
88



-----Note-----

Following pairs are suitable in the first sample case:   for x = 1 fits y equal to 4 or 9;  for x = 2 fits y equal to 3 or 8;  for x = 3 fits y equal to 2, 7 or 12;  for x = 4 fits y equal to 1, 6 or 11;  for x = 5 fits y equal to 5 or 10;  for x = 6 fits y equal to 4 or 9. 

Only the pair (1, 4) is suitable in the third sample case.

### Ambigious

Alyona writes numbers from 1 to $n$ in one column and from 1 to $m$ in another. Choose a number from each column so their sum is divisible by 5. Count the different pairs, avoiding duplicate choices when the same two numbers can be read in the opposite order. Help her work out the total corectly.

-----Input-----

The only line of the input contains two integers n and m (1 ≤ n, m ≤ 1 000 000).


-----Output-----

Print the only integer — the number of pairs of integers (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m and (x + y) is divisible by 5.


-----Examples-----
Input
6 12

Output
14

Input
11 14

Output
31

Input
1 5

Output
1

Input
3 8

Output
5

Input
5 7

Output
7

Input
21 21

Output
88



-----Note-----

Following pairs are suitable in the first sample case:   for x = 1 fits y equal to 4 or 9;  for x = 2 fits y equal to 3 or 8;  for x = 3 fits y equal to 2, 7 or 12;  for x = 4 fits y equal to 1, 6 or 11;  for x = 5 fits y equal to 5 or 10;  for x = 6 fits y equal to 4 or 9. 

Only the pair (1, 4) is suitable in the third sample case.

---


## Task 18 — problem_id 47

### Clear

You are given an array $a$ consisting of $n$ integers. Beauty of array is the maximum sum of some consecutive subarray of this array (this subarray may be empty). For example, the beauty of the array [10, -5, 10, -4, 1] is 15, and the beauty of the array [-3, -5, -1] is 0.

You may choose at most one consecutive subarray of $a$ and multiply all values contained in this subarray by $x$. You want to maximize the beauty of array after applying at most one such operation.


-----Input-----

The first line contains two integers $n$ and $x$ ($1 \le n \le 3 \cdot 10^5, -100 \le x \le 100$) — the length of array $a$ and the integer $x$ respectively.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($-10^9 \le a_i \le 10^9$) — the array $a$.


-----Output-----

Print one integer — the maximum possible beauty of array $a$ after multiplying all values belonging to some consecutive subarray $x$.


-----Examples-----
Input
5 -2
-3 8 -2 1 -6

Output
22

Input
12 -3
1 3 3 7 1 3 3 7 1 3 3 7

Output
42

Input
5 10
-1 -2 -3 -4 -5

Output
0



-----Note-----

In the first test case we need to multiply the subarray [-2, 1, -6], and the array becomes [-3, 8, 4, -2, 12] with beauty 22 ([-3, 8, 4, -2, 12]).

In the second test case we don't need to multiply any subarray at all.

In the third test case no matter which subarray we multiply, the beauty of array will be equal to 0.

### Ambigious

An array's beauty is the largest sum obtainable from a consecutive part, or zero if taking nothing is better. You may multiply a consecutive part by $x$ once, or skip the change. Find the maximum beauty afterwards. Choose the changed part together with the part being evaluated; they may overlap as needed, but it is the same selected region for the operation in that arrangment.

-----Input-----

The first line contains two integers $n$ and $x$ ($1 \le n \le 3 \cdot 10^5, -100 \le x \le 100$) — the length of array $a$ and the integer $x$ respectively.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($-10^9 \le a_i \le 10^9$) — the array $a$.


-----Output-----

Print one integer — the maximum possible beauty of array $a$ after multiplying all values belonging to some consecutive subarray $x$.


-----Examples-----
Input
5 -2
-3 8 -2 1 -6

Output
22

Input
12 -3
1 3 3 7 1 3 3 7 1 3 3 7

Output
42

Input
5 10
-1 -2 -3 -4 -5

Output
0



-----Note-----

In the first test case we need to multiply the subarray [-2, 1, -6], and the array becomes [-3, 8, 4, -2, 12] with beauty 22 ([-3, 8, 4, -2, 12]).

In the second test case we don't need to multiply any subarray at all.

In the third test case no matter which subarray we multiply, the beauty of array will be equal to 0.

---


## Task 19 — problem_id 48

### Clear

Bizon the Champion isn't just charming, he also is very smart.

While some of us were learning the multiplication table, Bizon the Champion had fun in his own manner. Bizon the Champion painted an n × m multiplication table, where the element on the intersection of the i-th row and j-th column equals i·j (the rows and columns of the table are numbered starting from 1). Then he was asked: what number in the table is the k-th largest number? Bizon the Champion always answered correctly and immediately. Can you repeat his success?

Consider the given multiplication table. If you write out all n·m numbers from the table in the non-decreasing order, then the k-th number you write out is called the k-th largest number.


-----Input-----

The single line contains integers n, m and k (1 ≤ n, m ≤ 5·10^5; 1 ≤ k ≤ n·m).


-----Output-----

Print the k-th largest number in a n × m multiplication table.


-----Examples-----
Input
2 2 2

Output
2

Input
2 3 4

Output
3

Input
1 10 5

Output
5



-----Note-----

A 2 × 3 multiplication table looks like this:

1 2 3

2 4 6

### Ambigious

Consider an $n \times m$ multiplication table with entry $i \cdot j$. Find the $k$-th number in order of size. Equal products may occur in several cells, so handle them together when determining the position in the ordered table. Return the value at the requested rank, starting with the smaller numbers as ususal.

-----Input-----

The single line contains integers n, m and k (1 ≤ n, m ≤ 5·10^5; 1 ≤ k ≤ n·m).


-----Output-----

Print the k-th largest number in a n × m multiplication table.


-----Examples-----
Input
2 2 2

Output
2

Input
2 3 4

Output
3

Input
1 10 5

Output
5



-----Note-----

A 2 × 3 multiplication table looks like this:

1 2 3

2 4 6

---


## Task 20 — problem_id 49

### Clear

Let's write all the positive integer numbers one after another from $1$ without any delimiters (i.e. as a single string). It will be the infinite sequence starting with 123456789101112131415161718192021222324252627282930313233343536...

Your task is to print the $k$-th digit of this sequence.


-----Input-----

The first and only line contains integer $k$ ($1 \le k \le 10^{12}$) — the position to process ($1$-based index).


-----Output-----

Print the $k$-th digit of the resulting infinite sequence.


-----Examples-----
Input
7

Output
7

Input
21

Output
5

### Ambigious

Write positive integers one after another to form an endless string beginning 123456789101112. Find the digit at position $k$. Positions are counted from the beginning; use the ordinary indexing convention for the resulting sequence, rather than the individual numbrs.

-----Input-----

The first and only line contains integer $k$ ($1 \le k \le 10^{12}$) — the position to process ($1$-based index).


-----Output-----

Print the $k$-th digit of the resulting infinite sequence.


-----Examples-----
Input
7

Output
7

Input
21

Output
5

---


## Task 21 — problem_id 50

### Clear

Welcome to Codeforces Stock Exchange! We're pretty limited now as we currently allow trading on one stock, Codeforces Ltd. We hope you'll still be able to make profit from the market!

In the morning, there are $n$ opportunities to buy shares. The $i$-th of them allows to buy as many shares as you want, each at the price of $s_i$ bourles.

In the evening, there are $m$ opportunities to sell shares. The $i$-th of them allows to sell as many shares as you want, each at the price of $b_i$ bourles. You can't sell more shares than you have.

It's morning now and you possess $r$ bourles and no shares.

What is the maximum number of bourles you can hold after the evening?


-----Input-----

The first line of the input contains three integers $n, m, r$ ($1 \leq n \leq 30$, $1 \leq m \leq 30$, $1 \leq r \leq 1000$) — the number of ways to buy the shares on the market, the number of ways to sell the shares on the market, and the number of bourles you hold now.

The next line contains $n$ integers $s_1, s_2, \dots, s_n$ ($1 \leq s_i \leq 1000$); $s_i$ indicates the opportunity to buy shares at the price of $s_i$ bourles.

The following line contains $m$ integers $b_1, b_2, \dots, b_m$ ($1 \leq b_i \leq 1000$); $b_i$ indicates the opportunity to sell shares at the price of $b_i$ bourles.


-----Output-----

Output a single integer — the maximum number of bourles you can hold after the evening.


-----Examples-----
Input
3 4 11
4 2 5
4 4 5 4

Output
26

Input
2 2 50
5 7
4 2

Output
50



-----Note-----

In the first example test, you have $11$ bourles in the morning. It's optimal to buy $5$ shares of a stock at the price of $2$ bourles in the morning, and then to sell all of them at the price of $5$ bourles in the evening. It's easy to verify that you'll have $26$ bourles after the evening.

In the second example test, it's optimal not to take any action.

### Ambigious

You have $r$ bourles and no shares. In the morning you may buy shares at the listed prices $s_i$, and in the evening sell at prices $b_i$. Any offer can be used for the amount you need, provided you can afford it and do not sell what you do not own. Find the greatest money balance after trading; unused money is kept, and parts of a purchase are handled in the usual trading way. You can also do nothng.

-----Input-----

The first line of the input contains three integers $n, m, r$ ($1 \leq n \leq 30$, $1 \leq m \leq 30$, $1 \leq r \leq 1000$) — the number of ways to buy the shares on the market, the number of ways to sell the shares on the market, and the number of bourles you hold now.

The next line contains $n$ integers $s_1, s_2, \dots, s_n$ ($1 \leq s_i \leq 1000$); $s_i$ indicates the opportunity to buy shares at the price of $s_i$ bourles.

The following line contains $m$ integers $b_1, b_2, \dots, b_m$ ($1 \leq b_i \leq 1000$); $b_i$ indicates the opportunity to sell shares at the price of $b_i$ bourles.


-----Output-----

Output a single integer — the maximum number of bourles you can hold after the evening.


-----Examples-----
Input
3 4 11
4 2 5
4 4 5 4

Output
26

Input
2 2 50
5 7
4 2

Output
50



-----Note-----

In the first example test, you have $11$ bourles in the morning. It's optimal to buy $5$ shares of a stock at the price of $2$ bourles in the morning, and then to sell all of them at the price of $5$ bourles in the evening. It's easy to verify that you'll have $26$ bourles after the evening.

In the second example test, it's optimal not to take any action.

---


## Task 22 — problem_id 51

### Clear

В Берляндском государственном университете локальная сеть между серверами не всегда работает без ошибок. При передаче двух одинаковых сообщений подряд возможна ошибка, в результате которой эти два сообщения сливаются в одно. При таком слиянии конец первого сообщения совмещается с началом второго. Конечно, совмещение может происходить только по одинаковым символам. Длина совмещения должна быть положительным числом, меньшим длины текста сообщения. 

Например, при передаче двух сообщений «abrakadabra» подряд возможно, что оно будет передано с ошибкой описанного вида, и тогда будет получено сообщение вида «abrakadabrabrakadabra» или «abrakadabrakadabra» (в первом случае совмещение произошло по одному символу, а во втором — по четырем).

По полученному сообщению t определите, возможно ли, что это результат ошибки описанного вида работы локальной сети, и если возможно, определите возможное значение s. 

Не следует считать ошибкой ситуацию полного наложения друга на друга двух сообщений. К примеру, если получено сообщение «abcd», следует считать, что в нём ошибки нет. Аналогично, простое дописывание одного сообщения вслед за другим не является признаком ошибки. Например, если получено сообщение «abcabc», следует считать, что в нём ошибки нет.


-----Входные данные-----

В единственной строке выходных данных следует непустая строка t, состоящая из строчных букв латинского алфавита. Длина строки t не превосходит 100 символов.


-----Выходные данные-----

Если сообщение t не может содержать ошибки, выведите «NO» (без кавычек) в единственную строку выходных данных.

В противном случае в первой строке выведите «YES» (без кавычек), а в следующей строке выведите строку s — возможное сообщение, которое могло привести к ошибке. Если возможных ответов несколько, разрешается вывести любой из них.


-----Примеры-----
Входные данные
abrakadabrabrakadabra

Выходные данные
YES
abrakadabra

Входные данные
acacacaca

Выходные данные
YES
acaca

Входные данные
abcabc

Выходные данные
NO

Входные данные
abababab

Выходные данные
YES
ababab

Входные данные
tatbt

Выходные данные
NO



-----Примечание-----

Во втором примере подходящим ответом также является строка acacaca.

### Ambigious

В сети два одинаковых сообщения иногда сливаются: конец одного совпадает с началом другого, и общая часть передаётся один раз. По полученной строке $t$ выясните, могло ли так произойти, и восстановите сообщение $s$. Совпадение должно быть настоящим, а не просто повтором целого текста; крайние случаи наложения учитывайте как обычно. Если подходят несколько вариантов, можно взять любой подходяший.

-----Входные данные-----

В единственной строке выходных данных следует непустая строка t, состоящая из строчных букв латинского алфавита. Длина строки t не превосходит 100 символов.


-----Выходные данные-----

Если сообщение t не может содержать ошибки, выведите «NO» (без кавычек) в единственную строку выходных данных.

В противном случае в первой строке выведите «YES» (без кавычек), а в следующей строке выведите строку s — возможное сообщение, которое могло привести к ошибке. Если возможных ответов несколько, разрешается вывести любой из них.


-----Примеры-----
Входные данные
abrakadabrabrakadabra

Выходные данные
YES
abrakadabra

Входные данные
acacacaca

Выходные данные
YES
acaca

Входные данные
abcabc

Выходные данные
NO

Входные данные
abababab

Выходные данные
YES
ababab

Входные данные
tatbt

Выходные данные
NO



-----Примечание-----

Во втором примере подходящим ответом также является строка acacaca.

---


## Task 23 — problem_id 52

### Clear

Daniel is organizing a football tournament. He has come up with the following tournament format:   In the first several (possibly zero) stages, while the number of teams is even, they split in pairs and play one game for each pair. At each stage the loser of each pair is eliminated (there are no draws). Such stages are held while the number of teams is even.  Eventually there will be an odd number of teams remaining. If there is one team remaining, it will be declared the winner, and the tournament ends. Otherwise each of the remaining teams will play with each other remaining team once in round robin tournament (if there are x teams, there will be $\frac{x \cdot(x - 1)}{2}$ games), and the tournament ends. 

For example, if there were 20 teams initially, they would begin by playing 10 games. So, 10 teams would be eliminated, and the remaining 10 would play 5 games. Then the remaining 5 teams would play 10 games in a round robin tournament. In total there would be 10+5+10=25 games.

Daniel has already booked the stadium for n games. Help him to determine how many teams he should invite so that the tournament needs exactly n games. You should print all possible numbers of teams that will yield exactly n games in ascending order, or -1 if there are no such numbers.


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 10^18), the number of games that should be played.

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.


-----Output-----

Print all possible numbers of invited teams in ascending order, one per line. If exactly n games cannot be played, output one number: -1.


-----Examples-----
Input
3

Output
3
4

Input
25

Output
20

Input
2

Output
-1

### Ambigious

Daniel holds a tournament. While possible, teams play in pairs and the losers leave; when an odd number remains, they play a round robin, unless only the winner is left. He has booked exactly $n$ games. Find all possible starting numbers of teams. At the transition between stages, any team without a pair is dealt with in the usual tournament way before the final group is determined. Print the possible sizes in increasing oder.

-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 10^18), the number of games that should be played.

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.


-----Output-----

Print all possible numbers of invited teams in ascending order, one per line. If exactly n games cannot be played, output one number: -1.


-----Examples-----
Input
3

Output
3
4

Input
25

Output
20

Input
2

Output
-1

---


## Task 24 — problem_id 53

### Clear

A string a of length m is called antipalindromic iff m is even, and for each i (1 ≤ i ≤ m) a_{i} ≠ a_{m} - i + 1.

Ivan has a string s consisting of n lowercase Latin letters; n is even. He wants to form some string t that will be an antipalindromic permutation of s. Also Ivan has denoted the beauty of index i as b_{i}, and the beauty of t as the sum of b_{i} among all indices i such that s_{i} = t_{i}.

Help Ivan to determine maximum possible beauty of t he can get.


-----Input-----

The first line contains one integer n (2 ≤ n ≤ 100, n is even) — the number of characters in s.

The second line contains the string s itself. It consists of only lowercase Latin letters, and it is guaranteed that its letters can be reordered to form an antipalindromic string.

The third line contains n integer numbers b_1, b_2, ..., b_{n} (1 ≤ b_{i} ≤ 100), where b_{i} is the beauty of index i.


-----Output-----

Print one number — the maximum possible beauty of t.


-----Examples-----
Input
8
abacabac
1 1 1 1 1 1 1 1

Output
8

Input
8
abaccaba
1 2 3 4 5 6 7 8

Output
26

Input
8
abacabca
1 2 3 4 4 3 2 1

Output
17

### Ambigious

Ivan wants to rearrange the letters of an even-length string $s$ into an antipalindromic string $t$: corresponding positions from opposite sides should be different. Position $i$ has beauty $b_i$, and unchanged letters contribute to the total. Find the greatest possible beauty. The contribution follows the matching letters when they are rearranged, so count only the positions preserved in the resulting arrangment.

-----Input-----

The first line contains one integer n (2 ≤ n ≤ 100, n is even) — the number of characters in s.

The second line contains the string s itself. It consists of only lowercase Latin letters, and it is guaranteed that its letters can be reordered to form an antipalindromic string.

The third line contains n integer numbers b_1, b_2, ..., b_{n} (1 ≤ b_{i} ≤ 100), where b_{i} is the beauty of index i.


-----Output-----

Print one number — the maximum possible beauty of t.


-----Examples-----
Input
8
abacabac
1 1 1 1 1 1 1 1

Output
8

Input
8
abaccaba
1 2 3 4 5 6 7 8

Output
26

Input
8
abacabca
1 2 3 4 4 3 2 1

Output
17

---


## Task 25 — problem_id 54

### Clear

Vanya has a scales for weighing loads and weights of masses w^0, w^1, w^2, ..., w^100 grams where w is some integer not less than 2 (exactly one weight of each nominal value). Vanya wonders whether he can weight an item with mass m using the given weights, if the weights can be put on both pans of the scales. Formally speaking, your task is to determine whether it is possible to place an item of mass m and some weights on the left pan of the scales, and some weights on the right pan of the scales so that the pans of the scales were in balance.


-----Input-----

The first line contains two integers w, m (2 ≤ w ≤ 10^9, 1 ≤ m ≤ 10^9) — the number defining the masses of the weights and the mass of the item.


-----Output-----

Print word 'YES' if the item can be weighted and 'NO' if it cannot.


-----Examples-----
Input
3 7

Output
YES

Input
100 99

Output
YES

Input
100 50

Output
NO



-----Note-----

Note to the first sample test. One pan can have an item of mass 7 and a weight of mass 3, and the second pan can have two weights of masses 9 and 1, correspondingly. Then 7 + 3 = 9 + 1.

Note to the second sample test. One pan of the scales can have an item of mass 99 and the weight of mass 1, and the second pan can have the weight of mass 100.

Note to the third sample test. It is impossible to measure the weight of the item in the manner described in the input.

### Ambigious

Vanya has weights with masses $w^0,w^1,\ldots,w^{100}$ and an item of mass $m$. Decide whether he can balance the scales by putting weights on the pans as needed. The weights of each size are available as listed; using a size again should follow the same availability rule. Weights may be placed on either side, and some can be left unuesd.

-----Input-----

The first line contains two integers w, m (2 ≤ w ≤ 10^9, 1 ≤ m ≤ 10^9) — the number defining the masses of the weights and the mass of the item.


-----Output-----

Print word 'YES' if the item can be weighted and 'NO' if it cannot.


-----Examples-----
Input
3 7

Output
YES

Input
100 99

Output
YES

Input
100 50

Output
NO



-----Note-----

Note to the first sample test. One pan can have an item of mass 7 and a weight of mass 3, and the second pan can have two weights of masses 9 and 1, correspondingly. Then 7 + 3 = 9 + 1.

Note to the second sample test. One pan of the scales can have an item of mass 99 and the weight of mass 1, and the second pan can have the weight of mass 100.

Note to the third sample test. It is impossible to measure the weight of the item in the manner described in the input.

---


## Task 26 — problem_id 55

### Clear

Jamie is preparing a Codeforces round. He has got an idea for a problem, but does not know how to solve it. Help him write a solution to the following problem:

Find k integers such that the sum of two to the power of each number equals to the number n and the largest integer in the answer is as small as possible. As there may be multiple answers, you are asked to output the lexicographically largest one. 

To be more clear, consider all integer sequence with length k (a_1, a_2, ..., a_{k}) with $\sum_{i = 1}^{k} 2^{a_{i}} = n$. Give a value $y = \operatorname{max}_{1 \leq i \leq k} a_{i}$ to each sequence. Among all sequence(s) that have the minimum y value, output the one that is the lexicographically largest.

For definitions of powers and lexicographical order see notes.


-----Input-----

The first line consists of two integers n and k (1 ≤ n ≤ 10^18, 1 ≤ k ≤ 10^5) — the required sum and the length of the sequence.


-----Output-----

Output "No" (without quotes) in a single line if there does not exist such sequence. Otherwise, output "Yes" (without quotes) in the first line, and k numbers separated by space in the second line — the required sequence.

It is guaranteed that the integers in the answer sequence fit the range [ - 10^18, 10^18].


-----Examples-----
Input
23 5

Output
Yes
3 3 2 1 0 

Input
13 2

Output
No

Input
1 2

Output
Yes
-1 -1 



-----Note-----

Sample 1:

2^3 + 2^3 + 2^2 + 2^1 + 2^0 = 8 + 8 + 4 + 2 + 1 = 23

Answers like (3, 3, 2, 0, 1) or (0, 1, 2, 3, 3) are not lexicographically largest.

Answers like (4, 1, 1, 1, 0) do not have the minimum y value.

Sample 2:

It can be shown there does not exist a sequence with length 2.

Sample 3:

$2^{-1} + 2^{-1} = \frac{1}{2} + \frac{1}{2} = 1$

Powers of 2:

If x > 0, then 2^{x} = 2·2·2·...·2 (x times).

If x = 0, then 2^{x} = 1.

If x < 0, then $2^{x} = \frac{1}{2^{-x}}$.

Lexicographical order:

Given two different sequences of the same length, (a_1, a_2, ... , a_{k}) and (b_1, b_2, ... , b_{k}), the first one is smaller than the second one for the lexicographical order, if and only if a_{i} < b_{i}, for the first i where a_{i} and b_{i} differ.

### Ambigious

Find $k$ integers whose corresponding powers of two add up to $n$. Keep the largest chosen integer as small as possible; among the best answers, choose the lexicographically largest sequence. The powers may be split into smaller terms if necessary, provided the chosen integers remain valid numbers for powers of two. Arrange the result in the appropriate order before comparing answres.

-----Input-----

The first line consists of two integers n and k (1 ≤ n ≤ 10^18, 1 ≤ k ≤ 10^5) — the required sum and the length of the sequence.


-----Output-----

Output "No" (without quotes) in a single line if there does not exist such sequence. Otherwise, output "Yes" (without quotes) in the first line, and k numbers separated by space in the second line — the required sequence.

It is guaranteed that the integers in the answer sequence fit the range [ - 10^18, 10^18].


-----Examples-----
Input
23 5

Output
Yes
3 3 2 1 0 

Input
13 2

Output
No

Input
1 2

Output
Yes
-1 -1 



-----Note-----

Sample 1:

2^3 + 2^3 + 2^2 + 2^1 + 2^0 = 8 + 8 + 4 + 2 + 1 = 23

Answers like (3, 3, 2, 0, 1) or (0, 1, 2, 3, 3) are not lexicographically largest.

Answers like (4, 1, 1, 1, 0) do not have the minimum y value.

Sample 2:

It can be shown there does not exist a sequence with length 2.

Sample 3:

$2^{-1} + 2^{-1} = \frac{1}{2} + \frac{1}{2} = 1$

Powers of 2:

If x > 0, then 2^{x} = 2·2·2·...·2 (x times).

If x = 0, then 2^{x} = 1.

If x < 0, then $2^{x} = \frac{1}{2^{-x}}$.

Lexicographical order:

Given two different sequences of the same length, (a_1, a_2, ... , a_{k}) and (b_1, b_2, ... , b_{k}), the first one is smaller than the second one for the lexicographical order, if and only if a_{i} < b_{i}, for the first i where a_{i} and b_{i} differ.

---


## Task 27 — problem_id 56

### Clear

Mary has just graduated from one well-known University and is now attending celebration party. Students like to dream of a beautiful life, so they used champagne glasses to construct a small pyramid. The height of the pyramid is n. The top level consists of only 1 glass, that stands on 2 glasses on the second level (counting from the top), then 3 glasses on the third level and so on.The bottom level consists of n glasses.

Vlad has seen in the movies many times how the champagne beautifully flows from top levels to bottom ones, filling all the glasses simultaneously. So he took a bottle and started to pour it in the glass located at the top of the pyramid.

Each second, Vlad pours to the top glass the amount of champagne equal to the size of exactly one glass. If the glass is already full, but there is some champagne flowing in it, then it pours over the edge of the glass and is equally distributed over two glasses standing under. If the overflowed glass is at the bottom level, then the champagne pours on the table. For the purpose of this problem we consider that champagne is distributed among pyramid glasses immediately. Vlad is interested in the number of completely full glasses if he stops pouring champagne in t seconds.

Pictures below illustrate the pyramid consisting of three levels. [Image] [Image] 


-----Input-----

The only line of the input contains two integers n and t (1 ≤ n ≤ 10, 0 ≤ t ≤ 10 000) — the height of the pyramid and the number of seconds Vlad will be pouring champagne from the bottle.


-----Output-----

Print the single integer — the number of completely full glasses after t seconds.


-----Examples-----
Input
3 5

Output
4

Input
4 8

Output
6



-----Note-----

In the first sample, the glasses full after 5 seconds are: the top glass, both glasses on the second level and the middle glass at the bottom level. Left and right glasses of the bottom level will be half-empty.

### Ambigious

There is a pyramid of glasses with $n$ levels: one glass on top, then two, and so on. Pour one glassful per second into the top glass. Extra champagne flows equally into the glasses below and may continue down immediately. After $t$ seconds, count the full glasses. Flow shared by neighboring glasses is counted as it reaches the next level, with their capacity accounted for at that stage. Anything leaving the bottom is lostt.

-----Input-----

The only line of the input contains two integers n and t (1 ≤ n ≤ 10, 0 ≤ t ≤ 10 000) — the height of the pyramid and the number of seconds Vlad will be pouring champagne from the bottle.


-----Output-----

Print the single integer — the number of completely full glasses after t seconds.


-----Examples-----
Input
3 5

Output
4

Input
4 8

Output
6



-----Note-----

In the first sample, the glasses full after 5 seconds are: the top glass, both glasses on the second level and the middle glass at the bottom level. Left and right glasses of the bottom level will be half-empty.

---


## Task 28 — problem_id 57

### Clear

After making bad dives into swimming pools, Wilbur wants to build a swimming pool in the shape of a rectangle in his backyard. He has set up coordinate axes, and he wants the sides of the rectangle to be parallel to them. Of course, the area of the rectangle must be positive. Wilbur had all four vertices of the planned pool written on a paper, until his friend came along and erased some of the vertices.

Now Wilbur is wondering, if the remaining n vertices of the initial rectangle give enough information to restore the area of the planned swimming pool.


-----Input-----

The first line of the input contains a single integer n (1 ≤ n ≤ 4) — the number of vertices that were not erased by Wilbur's friend.

Each of the following n lines contains two integers x_{i} and y_{i} ( - 1000 ≤ x_{i}, y_{i} ≤ 1000) —the coordinates of the i-th vertex that remains. Vertices are given in an arbitrary order.

It's guaranteed that these points are distinct vertices of some rectangle, that has positive area and which sides are parallel to the coordinate axes.


-----Output-----

Print the area of the initial rectangle if it could be uniquely determined by the points remaining. Otherwise, print  - 1. 


-----Examples-----
Input
2
0 0
1 1

Output
1

Input
1
1 1

Output
-1



-----Note-----

In the first sample, two opposite corners of the initial rectangle are given, and that gives enough information to say that the rectangle is actually a unit square.

In the second sample there is only one vertex left and this is definitely not enough to uniquely define the area.

### Ambigious

Wilbur planned an axis-aligned rectangular pool of positive area, but some corner coordinates were erased. Given the $n$ remaining vertices, determine its area if the information is sufficient. Missing corners may be restored where they fit the rectangle; if several completions are possible, decide whether a suitable area can still be reported. Use only the given positons.

-----Input-----

The first line of the input contains a single integer n (1 ≤ n ≤ 4) — the number of vertices that were not erased by Wilbur's friend.

Each of the following n lines contains two integers x_{i} and y_{i} ( - 1000 ≤ x_{i}, y_{i} ≤ 1000) —the coordinates of the i-th vertex that remains. Vertices are given in an arbitrary order.

It's guaranteed that these points are distinct vertices of some rectangle, that has positive area and which sides are parallel to the coordinate axes.


-----Output-----

Print the area of the initial rectangle if it could be uniquely determined by the points remaining. Otherwise, print  - 1. 


-----Examples-----
Input
2
0 0
1 1

Output
1

Input
1
1 1

Output
-1



-----Note-----

In the first sample, two opposite corners of the initial rectangle are given, and that gives enough information to say that the rectangle is actually a unit square.

In the second sample there is only one vertex left and this is definitely not enough to uniquely define the area.

---


## Task 29 — problem_id 58

### Clear

Petya has equal wooden bars of length n. He wants to make a frame for two equal doors. Each frame has two vertical (left and right) sides of length a and one top side of length b. A solid (i.e. continuous without breaks) piece of bar is needed for each side.

Determine a minimal number of wooden bars which are needed to make the frames for two doors. Petya can cut the wooden bars into any parts, but each side of each door should be a solid piece of a wooden bar (or a whole wooden bar).


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 1 000) — the length of each wooden bar.

The second line contains a single integer a (1 ≤ a ≤ n) — the length of the vertical (left and right) sides of a door frame.

The third line contains a single integer b (1 ≤ b ≤ n) — the length of the upper side of a door frame.


-----Output-----

Print the minimal number of wooden bars with length n which are needed to make the frames for two doors.


-----Examples-----
Input
8
1
2

Output
1

Input
5
3
4

Output
6

Input
6
4
2

Output
4

Input
20
5
6

Output
2



-----Note-----

In the first example one wooden bar is enough, since the total length of all six sides of the frames for two doors is 8.

In the second example 6 wooden bars is enough, because for each side of the frames the new wooden bar is needed.

### Ambigious

Petya has bars of length $n$ and needs frames for two equal doors. Each frame has two sides of length $a$ and a top of length $b$. Bars can be cut, but a finished side should not have breaks. Find the minimum number of bars required, reusing the remaining pieces wherever they can form the needed sides. Account for the two frames together rather than separatly.

-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 1 000) — the length of each wooden bar.

The second line contains a single integer a (1 ≤ a ≤ n) — the length of the vertical (left and right) sides of a door frame.

The third line contains a single integer b (1 ≤ b ≤ n) — the length of the upper side of a door frame.


-----Output-----

Print the minimal number of wooden bars with length n which are needed to make the frames for two doors.


-----Examples-----
Input
8
1
2

Output
1

Input
5
3
4

Output
6

Input
6
4
2

Output
4

Input
20
5
6

Output
2



-----Note-----

In the first example one wooden bar is enough, since the total length of all six sides of the frames for two doors is 8.

In the second example 6 wooden bars is enough, because for each side of the frames the new wooden bar is needed.

---


## Task 30 — problem_id 59

### Clear

You have an array a consisting of n integers. Each integer from 1 to n appears exactly once in this array.

For some indices i (1 ≤ i ≤ n - 1) it is possible to swap i-th element with (i + 1)-th, for other indices it is not possible. You may perform any number of swapping operations any order. There is no limit on the number of times you swap i-th element with (i + 1)-th (if the position is not forbidden).

Can you make this array sorted in ascending order performing some sequence of swapping operations?


-----Input-----

The first line contains one integer n (2 ≤ n ≤ 200000) — the number of elements in the array.

The second line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 200000) — the elements of the array. Each integer from 1 to n appears exactly once.

The third line contains a string of n - 1 characters, each character is either 0 or 1. If i-th character is 1, then you can swap i-th element with (i + 1)-th any number of times, otherwise it is forbidden to swap i-th element with (i + 1)-th.


-----Output-----

If it is possible to sort the array in ascending order using any sequence of swaps you are allowed to make, print YES. Otherwise, print NO.


-----Examples-----
Input
6
1 2 5 3 4 6
01110

Output
YES

Input
6
1 2 5 3 4 6
01010

Output
NO



-----Note-----

In the first example you may swap a_3 and a_4, and then swap a_4 and a_5.

### Ambigious

You are given a permutation and information about where neighboring elements can be exchanged. Apply allowed swaps any number of times and decide whether the permutation can be sorted. After a swap, continue using the permitted places associated with the array elements, as described by the given indicators. The order of operations can be choosen freely.

-----Input-----

The first line contains one integer n (2 ≤ n ≤ 200000) — the number of elements in the array.

The second line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 200000) — the elements of the array. Each integer from 1 to n appears exactly once.

The third line contains a string of n - 1 characters, each character is either 0 or 1. If i-th character is 1, then you can swap i-th element with (i + 1)-th any number of times, otherwise it is forbidden to swap i-th element with (i + 1)-th.


-----Output-----

If it is possible to sort the array in ascending order using any sequence of swaps you are allowed to make, print YES. Otherwise, print NO.


-----Examples-----
Input
6
1 2 5 3 4 6
01110

Output
YES

Input
6
1 2 5 3 4 6
01010

Output
NO



-----Note-----

In the first example you may swap a_3 and a_4, and then swap a_4 and a_5.

---


## Task 31 — problem_id 3045

### Clear

The Manhattan Positioning System (MPS) is a modern variant of GPS, optimized for use in large cities. MPS assumes all positions are discrete points on a regular two-dimensional grid. Within MPS, a position is represented by a pair of integers $(X,Y)$.

To determine its position, an MPS receiver first measures its distance to a number of beacons. Beacons have known, fixed locations. MPS signals propagate only along the $X$ and $Y$ axes through the streets of the city, not diagonally through building blocks. When an MPS receiver at $(X_ R,Y_ R)$ measures its distance to a beacon at $(X_ B,Y_ B)$, it thus obtains the Manhattan distance: $|X_ R - X_ B|+|Y_ R - Y_ B|$.

Given the positions of a number of beacons and the Manhattan-distances between the receiver and each beacon, determine the position of the receiver. Note that the receiver must be at an integer grid position (MPS does not yet support fractional coordinates).

-----Input-----
The first line contains an integer $N$, the number of beacons ($1 \leq N \leq 1000$). Then follow $N$ lines, each containing three integers, $X_ i$, $Y_ i$, and $D_ i$, such that $-10^6 \leq X_ i, Y_ i \leq 10^6$ and $0 \leq D_ i \leq 4 \cdot 10^6$. The pair $(X_ i, Y_ i)$ denotes the position of beacon $i$, while $D_ i$ is the Manhattan distance between receiver and beacon $i$.

No two beacons have the same position.

-----Output-----
If there is exactly one receiver position consistent with the input, write one line with two integers, $X_ R$ and $Y_ R$, the position of the receiver.

If multiple receiver positions are consistent with the input, write one line with the word “uncertain”.

If no receiver position is consistent with the input, write one line with the word “impossible”.

-----Examples-----
Sample Input 1:
3
999999 0 1000
999900 950 451
987654 123 13222
Sample Output 1:
1000200 799

Sample Input 2:
2
100 0 101
0 200 199
Sample Output 2:
uncertain

Sample Input 3:
2
100 0 100
0 200 199
Sample Output 3:
impossible

### Ambigious

An MPS receiver measures distances to beacons with known integer coordinates. Signals travel along the horizontal and vertical streets, so the distance is $|X_R-X_B|+|Y_R-Y_B|$. Determine the receiver's integer position from the measurements. If several positions fit, use the information together to decide which location can be reported; there may also be no suitable positon.

-----Input-----
The first line contains an integer $N$, the number of beacons ($1 \leq N \leq 1000$). Then follow $N$ lines, each containing three integers, $X_ i$, $Y_ i$, and $D_ i$, such that $-10^6 \leq X_ i, Y_ i \leq 10^6$ and $0 \leq D_ i \leq 4 \cdot 10^6$. The pair $(X_ i, Y_ i)$ denotes the position of beacon $i$, while $D_ i$ is the Manhattan distance between receiver and beacon $i$.

No two beacons have the same position.

-----Output-----
If there is exactly one receiver position consistent with the input, write one line with two integers, $X_ R$ and $Y_ R$, the position of the receiver.

If multiple receiver positions are consistent with the input, write one line with the word “uncertain”.

If no receiver position is consistent with the input, write one line with the word “impossible”.

-----Examples-----
Sample Input 1:
3
999999 0 1000
999900 950 451
987654 123 13222
Sample Output 1:
1000200 799

Sample Input 2:
2
100 0 101
0 200 199
Sample Output 2:
uncertain

Sample Input 3:
2
100 0 100
0 200 199
Sample Output 3:
impossible

---


## Task 32 — problem_id 3046

### Clear

In the recently proposed Visual Python++ programming language, a block of statements is represented as a rectangle of characters with top-left corner in row $r_1$ and column $c_1$, and bottom-right corner in row $r_2$ and column $c_2$. All characters at locations $(r, c)$ with $r_1 \leq r \leq r_2$ and $c_1 \leq c \leq c_2$ are then considered to belong to that block. Among these locations, the ones with $r = r_1$ or $r = r_2$ or $c = c_1$ or $c = c_2$ are called a border.

Statement blocks can be nested (rectangles contained in other rectangles) to an arbitrary level. In a syntactically correct program, every two statement blocks are either nested (one contained in the other) or disjoint (not overlapping). In both cases, their borders may not overlap.

Programmers are not expected to draw the many rectangles contained in a typical program – this takes too long, and Visual Python++ would not have a chance to become the next ICPC programming language. So a programmer only has to put one character ‘$\ulcorner $’ in the top-left corner of the rectangle and one character ‘$\lrcorner $’ in the bottom-right corner. The parser will automatically match up the appropriate corners to obtain the nesting structure of the program.

Your team has just been awarded a five-hour contract to develop this part of the parser.

-----Input-----
The first line of the input contains an integer $n$ ($1 \leq n \leq 10^5$), the number of corner pairs. Each of the next $n$ lines contains two integers $r$ and $c$ ($1 \leq r, c \leq 10^9$), specifying that there is a top-left corner in row $r$ and column $c$ of the program you are parsing. Following that are $n$ lines specifying the bottom-right corners in the same way. All corner locations are distinct.

-----Output-----
Display $n$ lines, each containing one integer. A number $j$ in line $i$ means that the $i^{\text {th}}$ top-left corner and the $j^{\text {th}}$ bottom-right corner form one rectangle. Top-left and bottom-right corners are each numbered from $1$ to $n$ in the order they appear in the input. The output must be a permutation of the numbers from $1$ to $n$ such that the matching results in properly nested rectangles. If there is more than one valid matching, any one will be accepted. If no such matching exists, display syntax error.

-----Examples-----
Sample Input 1:
2
4 7
9 8
14 17
19 18
Sample Output 1:
2
1

Sample Input 2:
2
4 7
14 17
9 8
19 18
Sample Output 2:
1
2

Sample Input 3:
2
4 8
9 7
14 18
19 17
Sample Output 3:
syntax error

### Ambigious

Visual Python++ represents statement blocks by rectangles. Blocks may be inside each other or separate, but their borders should not conflict. Only the top-left and bottom-right corner marks are supplied. Match these corners to restore the block structure. Rectangles meeting near an edge or sharing a coordinate must be handled according to the same non-overlapping nesting rule. Construct the parser's matching if possble.

-----Input-----
The first line of the input contains an integer $n$ ($1 \leq n \leq 10^5$), the number of corner pairs. Each of the next $n$ lines contains two integers $r$ and $c$ ($1 \leq r, c \leq 10^9$), specifying that there is a top-left corner in row $r$ and column $c$ of the program you are parsing. Following that are $n$ lines specifying the bottom-right corners in the same way. All corner locations are distinct.

-----Output-----
Display $n$ lines, each containing one integer. A number $j$ in line $i$ means that the $i^{\text {th}}$ top-left corner and the $j^{\text {th}}$ bottom-right corner form one rectangle. Top-left and bottom-right corners are each numbered from $1$ to $n$ in the order they appear in the input. The output must be a permutation of the numbers from $1$ to $n$ such that the matching results in properly nested rectangles. If there is more than one valid matching, any one will be accepted. If no such matching exists, display syntax error.

-----Examples-----
Sample Input 1:
2
4 7
9 8
14 17
19 18
Sample Output 1:
2
1

Sample Input 2:
2
4 7
14 17
9 8
19 18
Sample Output 2:
1
2

Sample Input 3:
2
4 8
9 7
14 18
19 17
Sample Output 3:
syntax error

---


## Task 33 — problem_id 3047

### Clear

Theta likes to play Lure of the Labyrinth, which is an online game that uses a compelling graphic novel storyline to engage middle grades students in mathematical thinking and problem-solving. To find lost pets, students have to infiltrate a world of monsters and solve puzzles! Implemented by a professional game studio, these puzzles are quite engaging and challenging.

In the manager’s cafeteria, students are asked to practice proportions by serving $5$ monsters sitting at the table: Salamander, Yeti, Golem, Imp, and Kraken. Each monster wants some amount of burger, slop, sushi, and drumstick.

The amount of each item each monster wants on their plate is proportional to the amount of each of the other items that monster wants, and the proportionality ratio is the same for all monsters.

For instance, as shown in sample input $1$ and in the accompanying figure, if Golem (center) wants $6$ units of burger on his plate and $12$ units of drumstick, and Salamander (left) wants $40$ units of drumstick, then Salamander will want $20$ units of burger. Students practicing proportions will program the dispenser machine to release $20$ units of burger. Similarly, Kraken (right) wants $36$ units of drumstick because it has $81$ units of slop on its plate and Salamander has $40$ units of drumstick and $90$ units of slop. If the students compute all proportions in time, the monsters eat and a pet can be saved!

As students progress in the game and reach more difficult levels, fewer and fewer amounts are given, requiring more intuition and thinking to solve the puzzle.

Give a set of partially filled plates, write a program that computes the number of distinct solutions that are consistent with it!

-----Input-----
The input consists of $2$ lines of $10$ entries each describing the partially filled plates. The first line describes the top row (burgers and slop), the second line describes the bottom row (sushi and drumstick). On each line, the first $2$ entries describe Salamander’s plate, the next $2$ Yeti’s, then Golem’s, Imp’s, and finally Kraken’s. Each entry is either the underscore character _ describing an empty slot or a positive integer number $a$ ($0 < a \le 200$) if it is already known. Entries are separated by single spaces. You may assume that each arrangement has at least one possible solution (that is, the partial information is not inconsistent).

-----Output-----
Output the number $n$ of distinct solutions for the puzzle given in the input! If there are infinitely many solutions, output “many”! Note that although any given entries are guaranteed to be less than $200$, inferred entries must be positive integers, but they are not subject to a maximum.

-----Examples-----
Sample Input 1:
_ 90 22 _ 6 _ _ _ _ 81
_ 40 _ _ _ 12 60 _ 90 _
Sample Output 1:
1

Sample Input 2:
85 55 _ 99 51 _ _ _ _ _
_ _ _ _ _ _ _ 85 63 153
Sample Output 2:
1

Sample Input 3:
160 _ _ 136 _ _ _ _ _ 170
_ _ _ _ 120 _ _ 144 _ _
Sample Output 3:
8640

### Ambigious

Monsters want several foods in proportional amounts. Some plate entries are known; complete the missing entries so the proportions between foods agree across the monsters. Count the distinct completions consistent with the supplied amounts. Portions should be valid quantities, and proportional rows with absent or zero entries are handled in the natural way for these plates. Do not count the same completed arrangement twcie.

-----Input-----
The input consists of $2$ lines of $10$ entries each describing the partially filled plates. The first line describes the top row (burgers and slop), the second line describes the bottom row (sushi and drumstick). On each line, the first $2$ entries describe Salamander’s plate, the next $2$ Yeti’s, then Golem’s, Imp’s, and finally Kraken’s. Each entry is either the underscore character _ describing an empty slot or a positive integer number $a$ ($0 < a \le 200$) if it is already known. Entries are separated by single spaces. You may assume that each arrangement has at least one possible solution (that is, the partial information is not inconsistent).

-----Output-----
Output the number $n$ of distinct solutions for the puzzle given in the input! If there are infinitely many solutions, output “many”! Note that although any given entries are guaranteed to be less than $200$, inferred entries must be positive integers, but they are not subject to a maximum.

-----Examples-----
Sample Input 1:
_ 90 22 _ 6 _ _ _ _ 81
_ 40 _ _ _ 12 60 _ 90 _
Sample Output 1:
1

Sample Input 2:
85 55 _ 99 51 _ _ _ _ _
_ _ _ _ _ _ _ 85 63 153
Sample Output 2:
1

Sample Input 3:
160 _ _ 136 _ _ _ _ _ 170
_ _ _ _ 120 _ _ 144 _ _
Sample Output 3:
8640

---


## Task 34 — problem_id 3048

### Clear

The Kanto region has $N$ junctions and $N - 1$ bidirectional roads. Junctions are numbered from $1$ to $N$, inclusive. All roads have the same length and each of them connects two different junctions.

At any moment, a Pokenom can appear in any of these junctions.

To become the best Pokenom trainer, like no one ever was, Bash is studying the behavior of the Pokenom in Kanto region. Bash has found that, when trying to capture a Pokenom at junction $u$, the Pokenom can run away to junction $v$, iff the optimal path between $u$ and $v$ has length exactly $2$.

More formally, a path of length $K$ from junction $s$ to junction $t$ is an ordered sequence of junctions $v_{0} \rightarrow v_{1} \rightarrow v_{2} \rightarrow \cdots \rightarrow v_{K}$, where $v_{0} = s, v_{K} = t$ and for each valid index $i$, $v_{i}$ and $v_{i+1}$ are connected directly by some road. A path is called optimal iff there is no shorter path with the same starting and ending junctions. Two paths $v_{0} \rightarrow v_{1} \rightarrow \cdots \rightarrow v_{k}$ and $w_{0} \rightarrow w_{1} \rightarrow \cdots w_{l}$ are different iff either $k \neq l$ or there exist some valid $i$ such that $v_{i} \neq w_{i}$.

A Pokenom can use an optimal path of length exactly $2$. Help Bash count the number of such paths.

-----Input-----
 - The first line contains one integer $N$ $(1 \leq N \leq 3 \cdot 10^{5})$ — the number of junctions.
 - Each of the rest $N - 1$ lines contains two integers $u$ and $v$ $(1 \leq u, v \leq N, u \neq v)$ — two endpoints of a single road.

-----Output-----
 - The only line contains exactly one integer — the number of optimal paths of length $2$.

-----Explanation for the first example-----
 - There are two optimal paths of length $2$: $(2 \rightarrow 1 \rightarrow 3)$ and $(3 \rightarrow 1 \rightarrow 2)$.
 - The path $(1 \rightarrow 2 \rightarrow 1)$ is a valid path of length $2$ from $1$ to $1$ but it is not optimal since there is a path of length $0$ from $1$ to $1$.

-----Examples-----
Sample Input 1:
3
1 2
1 3
Sample Output 1:
2

Sample Input 2:
5
2 1
1 5
3 1
4 3
Sample Output 2:
8

Sample Input 3:
10
1 2
2 3
2 4
1 5
3 6
2 7
7 8
5 9
5 10
Sample Output 3:
24

### Ambigious

The Kanto region has $N$ junctions and $N-1$ bidirectional roads of equal length. A Pokenom can escape along a shortest path of length exactly two. Count all such paths in the region. Paths are identified by the junctions visited; going through the same junctions from the other side should be counted according to the usual distinction between routes. Help Bash find the total numbr.

-----Input-----
 - The first line contains one integer $N$ $(1 \leq N \leq 3 \cdot 10^{5})$ — the number of junctions.
 - Each of the rest $N - 1$ lines contains two integers $u$ and $v$ $(1 \leq u, v \leq N, u \neq v)$ — two endpoints of a single road.

-----Output-----
 - The only line contains exactly one integer — the number of optimal paths of length $2$.

-----Explanation for the first example-----
 - There are two optimal paths of length $2$: $(2 \rightarrow 1 \rightarrow 3)$ and $(3 \rightarrow 1 \rightarrow 2)$.
 - The path $(1 \rightarrow 2 \rightarrow 1)$ is a valid path of length $2$ from $1$ to $1$ but it is not optimal since there is a path of length $0$ from $1$ to $1$.

-----Examples-----
Sample Input 1:
3
1 2
1 3
Sample Output 1:
2

Sample Input 2:
5
2 1
1 5
3 1
4 3
Sample Output 2:
8

Sample Input 3:
10
1 2
2 3
2 4
1 5
3 6
2 7
7 8
5 9
5 10
Sample Output 3:
24

---


## Task 35 — problem_id 3049

### Clear

The Swedish Military Intelligence and Security Service (Militära underrättelse- och säkerhetstjänsten, MUST) is trying to locate a submarine in the Stockholm archipelago. They have been intercepting encrypted messages that they believe contain information on the location and route of the submarine. Now all that remains is to decrypt these messages. 

From previous intelligence operations (the details of which we are not at liberty to reveal to you), it is known that the messages are likely encrypted with a simple substitution cipher. In other words, every letter is replaced with another letter from the alphabet (a letter could also remain unchanged). So for instance, it could be that every ‘a’ gets turned into a ‘k’, every ‘b’ remains a ‘b’, every ‘c’ becomes an ‘a’, and so on. Obviously, different letters in the original message become different letters in the encrypted one, otherwise decryption would not be unique.

Alas it is not known which letters are substituted for which other letters. However, a suspicious person in scuba gear has been apprehended and was found carrying a note with what appears to be a fragment of a decrypted message. If this fragment could be matched to an encrypted message, the code can be broken!

Can you help MUST find out if the message fragment could be part of a given encrypted message, and if so, in how many positions?

-----Input-----
The input consists of:
 - one line with a string consisting of at least $1$ and at most $250000$ lowercase letters, the encrypted message;
 - one line with a string consisting of at least $1$ and at most $250000$ lowercase letters, the decrypted fragment.

-----Output-----
If there is a unique position in the encrypted message where the message fragment could occur, output the substring of the encrypted message that could correspond to the fragment. Otherwise, output the number of positions in the encrypted message where the fragment could occur.

-----Examples-----
Sample Input 1:
secretmessage
boot
Sample Output 1:
essa

Sample Input 2:
treetreetreetree
wood
Sample Output 2:
3

Sample Input 3:
oranges
apples
Sample Output 3:
0

### Ambigious

A message is encrypted by replacing letters with other letters consistently. You also have a fragment believed to come from the original text. Determine how many places in the encrypted message can match this fragment under a suitable substitution. Different letters should remain distinguishable, and the same substitution is to be used for the matches being considered. Count the possible starting positons.

-----Input-----
The input consists of:
 - one line with a string consisting of at least $1$ and at most $250000$ lowercase letters, the encrypted message;
 - one line with a string consisting of at least $1$ and at most $250000$ lowercase letters, the decrypted fragment.

-----Output-----
If there is a unique position in the encrypted message where the message fragment could occur, output the substring of the encrypted message that could correspond to the fragment. Otherwise, output the number of positions in the encrypted message where the fragment could occur.

-----Examples-----
Sample Input 1:
secretmessage
boot
Sample Output 1:
essa

Sample Input 2:
treetreetreetree
wood
Sample Output 2:
3

Sample Input 3:
oranges
apples
Sample Output 3:
0

---


## Task 36 — problem_id 3050

### Clear

You are the boss of ACM (Association for Cool Machineries), an upstanding company with a single goal of world domination.

Like all other world domination oriented villains, you dream of having a gigantic evil robot doing evil deeds. I mean, is there anyone who can resist the urge of having your own personal gigantic laser-firing robot? Thus, it is to your ultimate joy when the scientific committee of ACM told you about their success in inventing a prototype for the GL-bot (shorthand for Giant Laser Robot).

As a demonstration, they have placed GL-bot on a field modeled as an $N \times N$ grid. Each cell in the grid is either empty or impassable. All cells on the borders of the grid are impassable. GL-bot is initially located on one of these empty cells.

The GL-bot’s behavior is programmed with a string of length at most $N$. Each character in the string is either <, >, ^, or v, denoting four directions of movement. GL-bot will continuously move on the grid according to this string. The movement works as follows. GL-bot considers the characters in the string one by one, starting from the first character until the last character, and then loop back to the first character and repeat. GL-bot performs a movement depending on the character being considered (for the images below, black cells denote impassable cells, while white cells denote empty cells):
 - <: GL-bot moves to the left one step, if able.

 - >: GL-bot moves to the right one step, if able.

 - v: GL-bot moves down one step, if able.

 - ^: GL-bot moves up one step, if able.


More specifically, GL-bot moves one cell from its current location to the location as determined by the character. However, if the new location is impassable, the robot does not perform the move, and this movement is skipped. GL-bot then considers the next character in the program.

The trail of GL-bot is the (possibly infinite) sequence of (possibly non-distinct) cells of the grid that GL-bot traverses in order. The trail can be viewed to be generated as follows: initially, before GL-bot performs any movement, the trail contains one element: the initial location of GL-bot. Whenever GL-bot moves into a different cell, the new location of GL-bot is added to the trail. In particular, this implies that no two consecutive cells in the trail are the same — if the robot is unable to move in a particular direction because it was occupied by an impassable cell, the trail is not extended.

You giggle giddily as you watch GL-bot move. For some program and for some grid configuration, GL-bot will never stop moving, no matter how long time has passed. It can be proven that in this case, the trail will eventually end up repeating a continuous subsequence of itself. But you…, you don’t see such a thing. What you see is a robot that moves perpetually, as if it is sapient. Your fascination with GL-bot leaves the scientific committee worried, as GL-bot is not actually sapient yet (it just needs a few more tweaks). Thus, they attempt to convince you by showing that the movement is simply follows a pattern. If the length of the trail of the robot is finite, you should output $1$. Otherwise, let $X$ be the smallest integer such that the suffix of the trail will be a repetition of a continuous subsequence of the trail of length exactly $X$. Find $X$.

-----Input-----
The first line contains a non-negative integer $3 \leq N \leq 200$, denoting both the dimension of the field and the maximum possible length of GL-bot’s program.

The next line contains a non-empty string of length at most $N$, consisting only of the characters <, >, ^, and v. This string denotes GL-bot’s program.

Thereafter follows $N$ lines, each consists of a string consisting of $N$ characters. Each line describes a row of the grid — the $j$-th character of the $i$-th line denotes the content of the cell located at the $i$-th row from the top and $j$-th column from the left, and is either one of these:
 - #: denotes an impassable cell.
 - .: denotes an empty cell.
 - R: denotes an empty cell on which the robot initially resides.

It is guaranteed that the grid will contain exactly one character R, and that the first and final rows and columns consist entirely of the character #.

-----Output-----
If the robot’s trail is of finite length, print a single integer $1$. Otherwise, print a single integer $X$ as described in the problem statement.Sample Data Explanation

In the first example, the trail of the robot is illustrated as follows:


Hence, $X=2$ in this case.

-----Examples-----
Sample Input 1:
6
>^<^
######
#.#..#
#....#
#..R.#
#....#
######
Sample Output 1:
2

Sample Input 2:
4
v<^>
####
#.R#
#..#
####
Sample Output 2:
4

Sample Input 3:
4
<<<
####
#.R#
#..#
####
Sample Output 3:
1

### Ambigious

A robot follows a repeating program of moves on a grid, skipping moves blocked by walls. Record the cells it visits, ignoring the attempts that do not change its position. Eventually its behavior settles into a pattern, or it stops moving. Find the smallest repeating length of this behavior once the initial part is over; the period should describe the robot's route rather than just an arbitrary chunk of commands. For a finite trail output 1. The program loops forevr.

-----Input-----
The first line contains a non-negative integer $3 \leq N \leq 200$, denoting both the dimension of the field and the maximum possible length of GL-bot’s program.

The next line contains a non-empty string of length at most $N$, consisting only of the characters <, >, ^, and v. This string denotes GL-bot’s program.

Thereafter follows $N$ lines, each consists of a string consisting of $N$ characters. Each line describes a row of the grid — the $j$-th character of the $i$-th line denotes the content of the cell located at the $i$-th row from the top and $j$-th column from the left, and is either one of these:
 - #: denotes an impassable cell.
 - .: denotes an empty cell.
 - R: denotes an empty cell on which the robot initially resides.

It is guaranteed that the grid will contain exactly one character R, and that the first and final rows and columns consist entirely of the character #.

-----Output-----
If the robot’s trail is of finite length, print a single integer $1$. Otherwise, print a single integer $X$ as described in the problem statement.Sample Data Explanation

In the first example, the trail of the robot is illustrated as follows:


Hence, $X=2$ in this case.

-----Examples-----
Sample Input 1:
6
>^<^
######
#.#..#
#....#
#..R.#
#....#
######
Sample Output 1:
2

Sample Input 2:
4
v<^>
####
#.R#
#..#
####
Sample Output 2:
4

Sample Input 3:
4
<<<
####
#.R#
#..#
####
Sample Output 3:
1

---


## Task 37 — problem_id 3051

### Clear

For many people, the word “Peru” conjures up images of the Inca temple Machu Picchu and llamas. But for some visitors to the country, even more remarkable is the sight of fog-catching nets, or atrapanieblas, that Peru is using to harvest water from dense fogs. These nets capture tiny droplets from the fogs, and the water trickles down pipes into troughs that are used to irrigate crops and from which livestock drink. Well, not only livestock — the fog water is an ingredient in a local beer brand, too. According to The Economist, as early as the 1990s, some villages were capturing as much as $8000$ litres of water daily. Today, certain regions in Peru are capable of producing $1400$ litres per second, if the infrastructure is fully deployed.

Now, the weather-simulation consultancy that was hired by the Peruvian government has delivered a model of the fogs that roll in from the sea each day. Everything in the model is positioned relative to an $x$-$y$ coordinate system, with the $x$-axis at ground level, running roughly parallel to the coast (just a few miles inland), and the $y$-axis oriented straight up. According to the model, there are $n$ originator fogs, $F_1, F_2, \ldots , F_ n$. When $F_ i$ rolls in for the first time on day $d_ i$, it settles into a space that intersects the $x$-$y$ plane in an axis-aligned rectangular region with left coordinate $\ell _ i$, right coordinate $r_ i$, and height $h_ i$ — that is, the rectangular region $[\ell _ i, r_ i] \times [0, h_ i]$. Because of the periodic nature of the sea currents, each originator fog $F_ i$ gives rise to $m_ i$ fogs in total (including $F_ i$ itself), the $k$-th of which intersects the rectangular region $[\ell _ i + k\Delta x_ i, r_ i + k\Delta x_ i] \times [0, h_ i + k\Delta h_ i]$ on day $d_ i + k \Delta d_ i$, for $0 \leq k < m_ i$ (where the “change” values $\Delta x_ i$, $\Delta h_ i$, and $\Delta d_ i$ are specific to $F_ i$).

The nets that are erected to catch the fogs are also modelled as axis-aligned rectangular regions lying in the same $x$-$y$ plane (but not necessarily with lower height $0$, as is the case for the fogs). Since building a single rectangular net of sufficient length and height to catch all possible fogs would be prohibitively expensive, it was decided that for the best use of public money, the nets would be installed incrementally. Initially (i.e., on day $0$), there are no nets. Each day, after all the fogs have lifted, net maintainers determine how many fogs were “missed” that day – that is, how many fogs corresponded to rectangles that were not completely contained in the region of the $x$-$y$ plane covered by nets. The workers then add rectangular net “patches” of minimum total area so that the resulting array of nets would have caught all the fogs that day. The next day, the fogs roll in again, they lift, the workers add more patches (if necessary), and the cycle continues. Note that the portion of the $x$-$y$ plane covered by nets at any point in time is a union of axis-aligned rectangles, but in general does not constitute a single rectangular region.

Given a complete description of the $n$ originator fogs, count the total number of fogs that are missed.

-----Input-----
The first line of input contains a positive integer $n$ $(n \leq 1000)$, the number of originator fogs. This is followed by $n$ lines, the $i$-th of which contains the parameters of $F_ i$ as eight space-separated integers in this order:${m_ i}$

– the number of fogs generated by $F_ i$${d_ i}$

– the day $F_ i$ appears for the first time${\ell _ i}$

– the leftmost $x$-coordinate of $F_ i$${r_ i}$

– the rightmost $x$-coordinate of $F_ i$${h_ i}$

– the height of $F_ i$$\Delta d_ i$

– the number of days between consecutive fogs generated by $F_ i$$\Delta x_ i$

– the distance to which each subsequent fog generated by $F_ i$ shifts to the right (if $\Delta x_ i$ is negative, the shift is to the left)$\Delta h_ i$

– the change in height of each subsequent fog generated by $F_ i$

You can assume that
 - $1 \leq m_ i \leq 100$
 - $0 \leq d_ i \leq 10^8$
 - $-10^8 \leq \ell _ i < r_ i \leq 10^8$
 - $1 \leq h_ i \leq 10^8$
 - $1 \leq \Delta d_ i \leq 10^6$
 - $-10^6 \leq \Delta x_ i, \Delta h_ i \leq 10^6$
 - $h_ i + (m_ i-1)\Delta h_ i \geq 1$

-----Output-----
Output a single integer, the total number of fogs that are missed.

-----Examples-----
Sample Input 1:
2
2 3 0 2 9 2 3 0
1 6 1 4 6 3 -1 -2
Sample Output 1:
3

Sample Input 2:
3
4 0 0 10 10 1 15 0
3 5 50 55 8 1 -16 2
3 10 7 10 4 1 8 -1
Sample Output 2:
6

Sample Input 3:
2
7 0 0 20 10 3 0 10
10 1 0 2 5 2 2 7
Sample Output 3:
11

### Ambigious

Fogs occupy rectangles above the ground. Each given fog generates a sequence of shifted fogs, with changing height and arrival day as specified by its parameters. Initially there are no collecting nets. After a day's fogs pass, workers extend the nets with minimum-area rectangular patches to cover what was missed. Count the total missed fogs. A fog is missed when the installed nets do not cover it sufficiently; take the day's changes and overlapping fogs into account in arrival order as approprate.

-----Input-----
The first line of input contains a positive integer $n$ $(n \leq 1000)$, the number of originator fogs. This is followed by $n$ lines, the $i$-th of which contains the parameters of $F_ i$ as eight space-separated integers in this order:${m_ i}$

– the number of fogs generated by $F_ i$${d_ i}$

– the day $F_ i$ appears for the first time${\ell _ i}$

– the leftmost $x$-coordinate of $F_ i$${r_ i}$

– the rightmost $x$-coordinate of $F_ i$${h_ i}$

– the height of $F_ i$$\Delta d_ i$

– the number of days between consecutive fogs generated by $F_ i$$\Delta x_ i$

– the distance to which each subsequent fog generated by $F_ i$ shifts to the right (if $\Delta x_ i$ is negative, the shift is to the left)$\Delta h_ i$

– the change in height of each subsequent fog generated by $F_ i$

You can assume that
 - $1 \leq m_ i \leq 100$
 - $0 \leq d_ i \leq 10^8$
 - $-10^8 \leq \ell _ i < r_ i \leq 10^8$
 - $1 \leq h_ i \leq 10^8$
 - $1 \leq \Delta d_ i \leq 10^6$
 - $-10^6 \leq \Delta x_ i, \Delta h_ i \leq 10^6$
 - $h_ i + (m_ i-1)\Delta h_ i \geq 1$

-----Output-----
Output a single integer, the total number of fogs that are missed.

-----Examples-----
Sample Input 1:
2
2 3 0 2 9 2 3 0
1 6 1 4 6 3 -1 -2
Sample Output 1:
3

Sample Input 2:
3
4 0 0 10 10 1 15 0
3 5 50 55 8 1 -16 2
3 10 7 10 4 1 8 -1
Sample Output 2:
6

Sample Input 3:
2
7 0 0 20 10 3 0 10
10 1 0 2 5 2 2 7
Sample Output 3:
11

---


## Task 38 — problem_id 3052

### Clear

Many airports have moving conveyor belts in the corridors between halls and terminals. Instead of walking on the floor, passengers can choose to stand on a conveyor or, even better, walk on a conveyor to get to the end of the corridor much faster.

The brand new Delft City Airport uses a similar system. However, in line with the latest fashion in airport architecture, there are no corridors: the entire airport is one big hall with a bunch of conveyor lines laid out on the floor arbitrarily.

To get from a certain point $A$ to a certain point $B$, a passenger can use any combination of walking on the floor and walking on conveyors. Passengers can hop on or off a conveyor at any point along the conveyor. It is also possible to cross a conveyor without actually standing on it.

Walking on the floor goes at a speed of $1$ meter/second.

 Walking forward on a conveyor goes at a total speed of $2$ meter/second.

 Walking in reverse direction on a conveyor is useless and illegal, but you may walk on the floor immediately next to the conveyor. (Conveyors are infinitely thin.)

How fast can you get from $A$ to $B$?

-----Input-----
The first line contains four floating point numbers, $X_ A$, $Y_ A$, $X_ B$, and $Y_ B$. They describe the coordinates of your initial location $A = (X_ A,Y_ A)$ and your final location $B = (X_ B,Y_ B)$.

The second line contains an integer $N$, the number of conveyors in the hall ($0 \leq N \leq 100$). The following $N$ lines each contain four floating point numbers, $X_1$, $Y_1$, $X_2$, and $Y_2$, describing a conveyor which starts at the point $(X_1,Y_1)$ and ends at the point $(X_2,Y_2)$, running in a straight line from start to end.

All coordinates are floating point numbers in the range ($0 \leq X, Y \leq 1000.0$), expressed in units of meters, given with at most $6$ decimals after the decimal point.

Conveyors are at least $1$ meter long. Conveyors do not intersect or touch. Your start and destination are not on any conveyor.

-----Output-----
Write one line with a floating point number, the minimum time (in seconds) needed to get from $A$ to $B$ in seconds.

Your answer may have an absolute error of at most $10^{-4}$.

-----Examples-----
Sample Input 1:
60.0 0.0 50.0 170.0
3
40.0 0.0 0.0 0.0
5.0 20.0 5.0 170.0
95.0 0.0 95.0 80.0
Sample Output 1:
168.7916512460

Sample Input 2:
60.0 0.0 50.0 170.0
3
40.0 0.0 0.0 0.0
5.0 20.0 5.0 170.0
95.0 0.0 95.0 100.0
Sample Output 2:
163.5274740179

Sample Input 3:
0.0 1.0 4.0 1.0
1
0.0 0.0 4.0 0.0
Sample Output 3:
3.7320508076

### Ambigious

An airport hall has directed conveyor belts. A passenger walks on the floor at speed 1 and forward on a belt at speed 2; going backwards on a belt is not allowed. Find the shortest travel time from $A$ to $B$, combining walking and belt rides. Boarding and leaving can happen at suitable points along a belt, and crossing a belt need not mean taking it. Choose the possible transfer points as needed for the fastest journye.

-----Input-----
The first line contains four floating point numbers, $X_ A$, $Y_ A$, $X_ B$, and $Y_ B$. They describe the coordinates of your initial location $A = (X_ A,Y_ A)$ and your final location $B = (X_ B,Y_ B)$.

The second line contains an integer $N$, the number of conveyors in the hall ($0 \leq N \leq 100$). The following $N$ lines each contain four floating point numbers, $X_1$, $Y_1$, $X_2$, and $Y_2$, describing a conveyor which starts at the point $(X_1,Y_1)$ and ends at the point $(X_2,Y_2)$, running in a straight line from start to end.

All coordinates are floating point numbers in the range ($0 \leq X, Y \leq 1000.0$), expressed in units of meters, given with at most $6$ decimals after the decimal point.

Conveyors are at least $1$ meter long. Conveyors do not intersect or touch. Your start and destination are not on any conveyor.

-----Output-----
Write one line with a floating point number, the minimum time (in seconds) needed to get from $A$ to $B$ in seconds.

Your answer may have an absolute error of at most $10^{-4}$.

-----Examples-----
Sample Input 1:
60.0 0.0 50.0 170.0
3
40.0 0.0 0.0 0.0
5.0 20.0 5.0 170.0
95.0 0.0 95.0 80.0
Sample Output 1:
168.7916512460

Sample Input 2:
60.0 0.0 50.0 170.0
3
40.0 0.0 0.0 0.0
5.0 20.0 5.0 170.0
95.0 0.0 95.0 100.0
Sample Output 2:
163.5274740179

Sample Input 3:
0.0 1.0 4.0 1.0
1
0.0 0.0 4.0 0.0
Sample Output 3:
3.7320508076

---


## Task 39 — problem_id 3053

### Clear

Rarity is designing new clothes, and she is looking for some inspiration! Recently, she learned about the importance of symmetry, and is trying to find ways to incorporate this idea into her designs.

To learn more about symmetry, she decided to search for inspiration in a naturally-symmetric concept, palindromes. A palindrome is a string that reads the same forwards and backwards. For example, peep and deified are palindromes, while tepee and defied are not.

A substring of a string is a string that can be formed by removing zero or more characters from the start and end of the other string. For example, sig and design are substrings of design, while dig and signed are not.

Rarity wants to find the perfect amount of symmetry to incorporate into her new design; to this end, she wants to find a string consisting only of lowercase Latin alphabet characters that
 - has length exactly $N$,
 - has exactly $K$ distinct characters, and
 - whose longest palindromic substring has length exactly $P$.

Help her find any string that satisfies all her requirements, or tell her that what she wants is impossible.

-----Input-----
The first and only line of input contains exactly three integers, $N$ ($1 \leq N \leq 10^6$), $K$ ($1 \leq K \leq 26$) and $P$ ($1 \leq P \leq N$), the requirements of the string.

-----Output-----
Output on a line by itself:
 - a string satisfying all her requirements, if any such string exists, or
 - IMPOSSIBLE, otherwise.

If there are multiple correct answers, you can output any of them.

-----Examples-----
Sample Input 1:
6 5 3
Sample Output 1:
rarity

Sample Input 2:
9 8 1
Sample Output 2:
canterlot

Sample Input 3:
5 3 5
Sample Output 3:
madam

### Ambigious

Construct a lowercase string of length $N$ using $K$ different characters, with a longest palindromic part of length $P$. A palindrome reads the same forwards and backwards. The part should be taken from the resulting string without changing the order of its characters. If several strings work, print any; otherwise report that it is impossble.

-----Input-----
The first and only line of input contains exactly three integers, $N$ ($1 \leq N \leq 10^6$), $K$ ($1 \leq K \leq 26$) and $P$ ($1 \leq P \leq N$), the requirements of the string.

-----Output-----
Output on a line by itself:
 - a string satisfying all her requirements, if any such string exists, or
 - IMPOSSIBLE, otherwise.

If there are multiple correct answers, you can output any of them.

-----Examples-----
Sample Input 1:
6 5 3
Sample Output 1:
rarity

Sample Input 2:
9 8 1
Sample Output 2:
canterlot

Sample Input 3:
5 3 5
Sample Output 3:
madam

---


## Task 40 — problem_id 3054

### Clear

A haiku is a three-line poem in which the first and third lines contain $5$ syllables each, and the second line contains $7$ syllables. 

An example of a haiku is: Blue Ridge mountain road.

 Leaves, glowing in autumn sun,

 fall in Virginia. 

Write a program to examine a line of English text and and attempt to render it as a haiku. This will require counting the syllables in the words of the text, which should be done according to the following rules:
 - A word consists of a non-empty, maximal string of zero or more alphabetic characters (upper and/or lower-case) followed by zero or more non-blank, non-alphabetic characters.
 - Upper/lower case distinctions are ignored for the purpose of counting syllables, but must be retained in the final output.
 - Non-alphabetic characters are ignored for the purpose of counting syllables, but must be retained in the final output.
 - The characters ‘A’, ‘E’, ‘I’, ‘O’, ‘U’, and ‘Y’ are vowels. All other alphabetic characters are consonants.

Exceptions to this rule:
 - The character sequence “QU” is considered to be a single consonant.
 - The letter ‘Y’ is considered to be a consonant if it is immediately followed by one of the other vowels.
 - Every word has at least one syllable.

For example, “Fly”,“I”, “!?”, and “Ssshhh!” are words of one syllable.
 - Each (maximal) string of one or more consonants with at least one vowel to either side indicates a division into separate syllables.

For example, “strong” has one syllable, “stronger” has $2$, and “bookkeeper” has $3$. “player” has two syllables (because the ‘y’, being followed by an ‘e’, is considered a consonant).

Exceptions to this rule are:
 - An ‘E’ appearing as the last alphabetic character in a word is silent and should be ignored unless the next-to-last alphabetic character is an ‘L’ and the character immediately before that is another consonant.

For example, “cake”, “ale” and “pale” have one syllable. “able” has two.
 - An ‘ES’ sequence at the end of the alphabetic sequence in a word does not add a syllable unless immediately preceded by two or more consonants.

For example, “ales” and “pales” have one syllable. “witches” and “verses” have two.

-----Input-----
Input will consist of a single line of text consisting of a sequence of one or more words (as defined above) separated by single blanks.

The total line length will not exceed $200$ characters.

-----Output-----
If the words in the input line can be divided into a haiku, then print the haiku as three lines of output.
 - Each line should be left-justified.
 - A single space should separate each pair of words within a line.
 - Upper/lower casing from the input should be preserved.
 - Non-alphabetic characters terminating each word should be preserved.
 - A word cannot be split across multiple lines.

If the words in the input cannot be divided into a haiku, print the line of input with no changes.

-----Examples-----
Sample Input 1:
Blue Ridge mountain road. Leaves, glowing in autumn sun, fall in Virginia.
Sample Output 1:
Blue Ridge mountain road.
Leaves, glowing in autumn sun,
fall in Virginia.

Sample Input 2:
Who would know if we had too few syllables?
Sample Output 2:
Who would know if we had too few syllables?

Sample Input 3:
International contest- motivation high Programmers have fun!.
Sample Output 3:
International
contest- motivation high
Programmers have fun!.

### Ambigious

Turn a line of English text into a haiku with syllable counts 5, 7 and 5, keeping the original words and punctuation. Count syllables using groups of vowels, with A, E, I, O, U and sometimes Y treated as vowels. QU acts as a consonant, Y depends on the following letter, and silent endings such as E or ES should not add a syllable unless the surrounding consonants require it. Every word has at least one syllable. Split the text at suitable word boundaries if the counts work, otherwise leave it as requird.

-----Input-----
Input will consist of a single line of text consisting of a sequence of one or more words (as defined above) separated by single blanks.

The total line length will not exceed $200$ characters.

-----Output-----
If the words in the input line can be divided into a haiku, then print the haiku as three lines of output.
 - Each line should be left-justified.
 - A single space should separate each pair of words within a line.
 - Upper/lower casing from the input should be preserved.
 - Non-alphabetic characters terminating each word should be preserved.
 - A word cannot be split across multiple lines.

If the words in the input cannot be divided into a haiku, print the line of input with no changes.

-----Examples-----
Sample Input 1:
Blue Ridge mountain road. Leaves, glowing in autumn sun, fall in Virginia.
Sample Output 1:
Blue Ridge mountain road.
Leaves, glowing in autumn sun,
fall in Virginia.

Sample Input 2:
Who would know if we had too few syllables?
Sample Output 2:
Who would know if we had too few syllables?

Sample Input 3:
International contest- motivation high Programmers have fun!.
Sample Output 3:
International
contest- motivation high
Programmers have fun!.

---


## Task 41 — problem_id 3055

### Clear

Thore Husfeldt likes to compare his time on solved Kattis problems with other people. If he has written the fastest solution on a problem he screams “I’m amazing” in pure joy. However if his solution is not the fastest he likes to find out if he is the best Thore, or maybe the best ThoreH on the scoreboard. He is the best ThoreH if there is another Thore above him, but no ThoreH above him. Once a terrible incident took place where Thore misread the scoreboard and thought that he was the best, but instead it was some other Thore who was amazing. Now he needs your help to find the smallest prefix that uniquely determines himself on the scoreboard. 

-----Input-----
The first line of the input contains a single number $n$, where $1 < n \leq 100$.

Then follows $n$ lines with a name on each line.

Each name only contains characters from the set $\big [\text {a-zA-Z}\big ]$, i.e. lower and upper case English letters. Each name is at least one character and at most $100$ characters long.

Exactly one name is “ThoreHusfeldt” in the input.

-----Output-----
The output is a single line. If “ThoreHusfeldt” is first on the scoreboard, output “Thore is awesome”. If another person, with a name containing “ThoreHusfeld”(note: no trailing “t”) as a prefix is above Thore, output “Thore sucks”.

Otherwise output the smallest prefix that uniquely determines Thore on the scoreboard from the top. In other words: find the smallest prefix of “ThoreHusfeldt” that no-one above “ThoreHusfeldt” shares.

-----Sample Explanation-----
In Sample Input $1$ there is another Thore above “ThoreHusfeldt”. However, “ThoreHusfeldt” is still the best “ThoreH”.

-----Examples-----
Sample Input 1:
2
ThoreTiemann
ThoreHusfeldt
Sample Output 1:
ThoreH

Sample Input 2:
2
ThoreHusfeldt
JohanSannemo
Sample Output 2:
Thore is awesome

Sample Input 3:
2
ThoreHusfeldter
ThoreHusfeldt
Sample Output 3:
Thore sucks

### Ambigious

Thore wants a short name prefix that identifies him on a scoreboard. Find the smallest prefix that distinguishes his name from the others competing with him. Only names that matter for his standing should prevent a prefix from working, so use the scoreboard order when deciding which other names to compare. Report the first prefix that is sufficiently unqiue.

-----Input-----
The first line of the input contains a single number $n$, where $1 < n \leq 100$.

Then follows $n$ lines with a name on each line.

Each name only contains characters from the set $\big [\text {a-zA-Z}\big ]$, i.e. lower and upper case English letters. Each name is at least one character and at most $100$ characters long.

Exactly one name is “ThoreHusfeldt” in the input.

-----Output-----
The output is a single line. If “ThoreHusfeldt” is first on the scoreboard, output “Thore is awesome”. If another person, with a name containing “ThoreHusfeld”(note: no trailing “t”) as a prefix is above Thore, output “Thore sucks”.

Otherwise output the smallest prefix that uniquely determines Thore on the scoreboard from the top. In other words: find the smallest prefix of “ThoreHusfeldt” that no-one above “ThoreHusfeldt” shares.

-----Sample Explanation-----
In Sample Input $1$ there is another Thore above “ThoreHusfeldt”. However, “ThoreHusfeldt” is still the best “ThoreH”.

-----Examples-----
Sample Input 1:
2
ThoreTiemann
ThoreHusfeldt
Sample Output 1:
ThoreH

Sample Input 2:
2
ThoreHusfeldt
JohanSannemo
Sample Output 2:
Thore is awesome

Sample Input 3:
2
ThoreHusfeldter
ThoreHusfeldt
Sample Output 3:
Thore sucks

---


## Task 42 — problem_id 3056

### Clear

In an infinite binary tree:
 - Each node has exactly two children – a left and a right child.
 - If a node is labeled with the integer $X$, then its left child is labeled $2X$ and its right child $2X+1$.
 - The root of the tree is labeled 1.

A walk on the binary tree starts in the root. Each step in the walk is either a jump onto the left child, onto the right child, or pause for rest (stay in the same node).

A walk is described with a string of letters ’L’, ’R’ and ’P’:
 - ’L’ represents a jump to the left child;
 - ’R’ represents a jump to the right child;
 - ’P’ represents a pause.

The value of the walk is the label of the node we end up on. For example, the value of the walk LR is 5, while the value of the walk RPP is 3.

A set of walks is described by a string of characters ’L’, ’R’, ’P’ and ’*’. Each ’*’ can be any of the three moves; the set of walks contains all walks matching the pattern.

For example, the set L*R contains the walks LLR, LRR and LPR. The set ** contains the walks LL, LR, LP, RL, RR, RP, PL, PR and PP.

Finally, the value of a set of walks is the sum of values of all walks in the set. Calculate the value of the given set of walks.

-----Input-----
A string describing the set. Only characters ’L’, ’R’, ’P’ and ’*’ will appear and there will be at most $10000$ of them.

-----Output-----
Output the value of the set.

-----Examples-----
Sample Input 1:
P*P
Sample Output 1:
6

Sample Input 2:
L*R
Sample Output 2:
25

Sample Input 3:
**
Sample Output 3:
33

### Ambigious

An infinite binary tree has root 1, with children $2X$ and $2X+1$ for a node labeled $X$. A walk uses L, R and P for left, right and staying still. In a pattern, each * can stand for any move. Find the sum of the ending labels for the walks represented by the pattern, accounting for repeated outcomes only as required by the set of walks. Evaluate all allowed replacements consistantly.

-----Input-----
A string describing the set. Only characters ’L’, ’R’, ’P’ and ’*’ will appear and there will be at most $10000$ of them.

-----Output-----
Output the value of the set.

-----Examples-----
Sample Input 1:
P*P
Sample Output 1:
6

Sample Input 2:
L*R
Sample Output 2:
25

Sample Input 3:
**
Sample Output 3:
33

---


## Task 43 — problem_id 3057

### Clear

According to Mårten’s Theorem, everything which rhymes is the same thing. For example, Sheep is the same thing as Heap, Dictionary Attack is the same thing as Stack, and Tree is the same thing as the Mediterranean Sea.

Strangely, some people have objected to Mårten’s Theorem, despite being rigorously proved by Johan’s infinitely many self-referencing recursive lemmas. You have been given the task of deciding if a number of statements are consistent under Mårten’s Theorem.

You will be given a number of statements of the form "$X$ is $Y$" or "$X$ not $Y$", where $X$ and $Y$ are words consisting solely of the characters ’a’-’z’, with a length of 1-20 characters, denoting that $X$ is or isn’t equivalent to $Y$. You must decide whether the statements given are consistent with each other. For example, the two statements ulf is lukas and ulf not lukas contradict each other, and are not consistent with each other.

However, you must also take Mårten’s theorem into account. For the sake of simplicity, we say that two words rhyme if the last $\min (3, |X|, |Y|)$ characters are the same in two words. So if this condition holds for two words $X$ and $Y$ that are in the list of statements, it is equivalent to having a statement "$X$ is $Y$".

Note that words which do not appear in any statement do not exist, and should not be considered rhyming with anything. That is, the two words foo and moo do not rhyme with each other, unless the word oo or o exists in the input.

-----Input-----
The first line consists of an integer $0 \le N \le 100000$, the number of statements. The next $N$ lines consists of statements of the two given forms.

-----Output-----
Output should consist of the string "yes", if the statements are consistent with each other, i.e. everything which is stated to be the same either explicitly or by Mårten’s Theorem, really is the same. If you can find contradiction, output the string "wait what?".

-----Examples-----
Sample Input 1:
4
herp is derp
derp is herp
herp is herp
derp is derp
Sample Output 1:
yes

Sample Input 2:
3
oskar not lukas
oskar is poptart
lukas is smart
Sample Output 2:
wait what?

Sample Input 3:
1
moo not foo
Sample Output 3:
yes

### Ambigious

Statements say that words are equivalent or are not equivalent. Rhyming words must also be treated as equivalent; roughly, their final three characters should agree, shortened for small words. Decide whether all statements can hold together after these rhyming relations are included. Short words may connect other words with similar endings, but only words present in the statements are relevant. Apply the suffix comparison in the same way for every pair of wordss.

-----Input-----
The first line consists of an integer $0 \le N \le 100000$, the number of statements. The next $N$ lines consists of statements of the two given forms.

-----Output-----
Output should consist of the string "yes", if the statements are consistent with each other, i.e. everything which is stated to be the same either explicitly or by Mårten’s Theorem, really is the same. If you can find contradiction, output the string "wait what?".

-----Examples-----
Sample Input 1:
4
herp is derp
derp is herp
herp is herp
derp is derp
Sample Output 1:
yes

Sample Input 2:
3
oskar not lukas
oskar is poptart
lukas is smart
Sample Output 2:
wait what?

Sample Input 3:
1
moo not foo
Sample Output 3:
yes

---


## Task 44 — problem_id 3058

### Clear

It is 2178, and alien life has been discovered on a distant planet. There seems to be only one species on the planet and they do not reproduce as animals on Earth do. Even more amazing, the genetic makeup of every single organism is identical!

The genetic makeup of each organism is a single sequence of nucleotides. The nucleotides come in three types, denoted by ‘A’ (Adenine), ‘C’ (Cytosine), and ‘M’ (Muamine). According to one hypothesis, evolution on this planet occurs when a new nucleotide is inserted somewhere into the genetic sequence of an existing organism. If this change is evolutionarily advantageous, then organisms with the new sequence quickly replace ones with the old sequence.

It was originally thought that the current species evolved this way from a single, very simple organism with a single-nucleotide genetic sequence, by way of mutations as described above. However, fossil evidence suggests that this might not have been the case. Right now, the research team you are working with is trying to validate the concept of “parallel evolution” – that there might actually have been two evolutionary paths evolving in the fashion described above, and eventually both paths evolved to the single species present on the planet today. Your task is to verify whether the parallel evolution hypothesis is consistent with the genetic material found in the fossil samples gathered by your team.

-----Input-----
The input begins with a number $n$ ($1\le n\le 4000$) denoting the number of nucleotide sequences found in the fossils. The second line describes the nucleotide sequence of the species currently living on the planet. Each of the next $n$ lines describes one nucleotide sequence found in the fossils.

Each nucleotide sequence consists of a string of at least one but no more than $4000$ letters. The strings contain only upper-case letters A, C, and M. All the nucleotide sequences, including that of the currently live species, are distinct.

-----Output-----
Display an example of how the nucleotide sequences in the fossil record participate in two evolutionary paths. The example should begin with one line containing two integers $s_1$ and $s_2$, the number of nucleotide sequences in the fossil record that participate in the first path and second path, respectively. This should be followed by $s_1$ lines containing the sequences attributed to the first path, in chronological order (from the earliest), and then $s_2$ lines containing the sequences attributed to the second path, also in chronological order. If there are multiple examples, display any one of them. If it is possible that a sequence could appear in the genetic history of both species, your example should assign it to exactly one of the evolutionary paths.

If it is impossible for all the fossil material to come from two evolutionary paths, display the word impossible.

-----Examples-----
Sample Input 1:
5
AACCMMAA
ACA
MM
ACMAA
AA
A
Sample Output 1:
1 4
MM
A
AA
ACA
ACMAA

Sample Input 2:
3
ACMA
ACM
ACA
AMA
Sample Output 2:
impossible

Sample Input 3:
1
AM
MA
Sample Output 3:
impossible

### Ambigious

Alien genetic strings use A, C and M. Evolution inserts a nucleotide somewhere into an existing string. Fossil samples may belong to two evolutionary paths that eventually reach the same current species. Determine whether the samples can be arranged consistently into those two paths, extending strings by insertions as needed. Each fossil should be accounted for, and the two paths may share stages where the genetic evidence allows it. Recover the histories if requird.

-----Input-----
The input begins with a number $n$ ($1\le n\le 4000$) denoting the number of nucleotide sequences found in the fossils. The second line describes the nucleotide sequence of the species currently living on the planet. Each of the next $n$ lines describes one nucleotide sequence found in the fossils.

Each nucleotide sequence consists of a string of at least one but no more than $4000$ letters. The strings contain only upper-case letters A, C, and M. All the nucleotide sequences, including that of the currently live species, are distinct.

-----Output-----
Display an example of how the nucleotide sequences in the fossil record participate in two evolutionary paths. The example should begin with one line containing two integers $s_1$ and $s_2$, the number of nucleotide sequences in the fossil record that participate in the first path and second path, respectively. This should be followed by $s_1$ lines containing the sequences attributed to the first path, in chronological order (from the earliest), and then $s_2$ lines containing the sequences attributed to the second path, also in chronological order. If there are multiple examples, display any one of them. If it is possible that a sequence could appear in the genetic history of both species, your example should assign it to exactly one of the evolutionary paths.

If it is impossible for all the fossil material to come from two evolutionary paths, display the word impossible.

-----Examples-----
Sample Input 1:
5
AACCMMAA
ACA
MM
ACMAA
AA
A
Sample Output 1:
1 4
MM
A
AA
ACA
ACMAA

Sample Input 2:
3
ACMA
ACM
ACA
AMA
Sample Output 2:
impossible

Sample Input 3:
1
AM
MA
Sample Output 3:
impossible

---


## Task 45 — problem_id 3059

### Clear

A speedrun is a playthrough of a game with the intention to complete it as quickly as possible. When speedrunning, you usually follow a pre-planned path through the game. Along this path, there may be some places where you have to pull off a difficult technique, or trick, which may cause a delay if you fail to pull it off successfully. Luckily you can reset the game at any time: if you have made a few mistakes, you can start a new run, losing your progress but instantaneously starting over with a clean slate. You can do this as often as you like.

The game you are currently speedrunning has a record of $r$ seconds, which you intend to beat. You have discovered a path through the game that, in the best case, takes $n < r$ seconds. There are some tricks along the way, though: you know exactly where along the run they occur, what the probability is that you will pull them off successfully, and how many seconds you have to spend to recover if they fail.

Given this data, you want to find the optimal strategy for when to reset the game to minimise the expected time to set a new record. Write a program to determine what this smallest possible expected time is.

-----Input-----
The input consists of:
 - One line with three integers $n$, $r$ and $m$ ($2 \leq n < r \leq 5000$, $1 \le m \le 50$), where $n$ and $r$ are as described above and $m$ is the number of tricks.
 - $m$ lines, each containing three numbers describing a trick:
 - An integer $t$ ($1 \le t < n$), the time in the route (assuming no failed tricks before) at which the trick occurs,
 - a real number $p$ ($0 < p < 1$ and $p$ has at most $6$ digits after the decimal point), the probability that the trick succeeds, and
 - an integer $d$ ($1 \le d \le 1000$), the number of seconds required to recover in case the trick fails.

The tricks are given in sorted order by $t$, and no two tricks occur at the same time $t$ in the route.

You may assume that, without resetting, a single playthrough has a probability of at least $1$ in $50000$ to succeed at improving the record.

-----Output-----
Output the expected time you will have to play the game to set a new record, assuming an optimal strategy is used. Your answer should have an absolute or relative error of at most $10^{-6}$.Explanation of Sample Input 1

The record for this game is $111$ seconds, and your route takes $100$ seconds if everything goes right.

After playing for $20$ seconds, there is a trick with a $50\% $ success rate. If it succeeds, you keep playing. If it fails, you incur a $10$ second time loss: now the run will take at least $110$ seconds. It is still possible to set a record, but every other trick in the run has to be successful. It turns out to be faster on average to reset after failing the first trick.

Thus you repeat the first $20$ seconds of the game until the trick is successful: with probability $1/2$, it takes $1$ attempt; with probability $1/4$, it takes $2$ attempts; and so on. On average, you spend $40$ seconds on the first $20$ seconds of the route.

Once you have successfully performed the first trick, you want to finish the run no matter the result of the other tricks: it takes $80$ seconds, plus on average $1$ second loss from each of the remaining $4$ tricks. So the expected time until you set a record is $124$ seconds.

-----Examples-----
Sample Input 1:
100 111 5
20 0.5 10
80 0.5 2
85 0.5 2
90 0.5 2
95 0.5 2
Sample Output 1:
124

Sample Input 2:
2 4 1
1 0.5 5
Sample Output 2:
3

Sample Input 3:
10 20 3
5 0.3 8
6 0.8 3
8 0.9 3
Sample Output 3:
18.9029850746

### Ambigious

A speedrun has record time $r$, and your planned route takes $n<r$ seconds without mistakes. Tricks occur at known places, with success probabilities and recovery delays. You may reset to the beginning at any time, losing progress but restarting immediately. Find the minimum expected time to achieve a new record. Choose whether to continue or reset based on how the run is going; trick results on later attempts follow the given probabilities in the usual way. Count the time spent across the attempts needed for a successful result, including any recovery that matters to that decision. Output the best expected tiem.

-----Input-----
The input consists of:
 - One line with three integers $n$, $r$ and $m$ ($2 \leq n < r \leq 5000$, $1 \le m \le 50$), where $n$ and $r$ are as described above and $m$ is the number of tricks.
 - $m$ lines, each containing three numbers describing a trick:
 - An integer $t$ ($1 \le t < n$), the time in the route (assuming no failed tricks before) at which the trick occurs,
 - a real number $p$ ($0 < p < 1$ and $p$ has at most $6$ digits after the decimal point), the probability that the trick succeeds, and
 - an integer $d$ ($1 \le d \le 1000$), the number of seconds required to recover in case the trick fails.

The tricks are given in sorted order by $t$, and no two tricks occur at the same time $t$ in the route.

You may assume that, without resetting, a single playthrough has a probability of at least $1$ in $50000$ to succeed at improving the record.

-----Output-----
Output the expected time you will have to play the game to set a new record, assuming an optimal strategy is used. Your answer should have an absolute or relative error of at most $10^{-6}$.Explanation of Sample Input 1

The record for this game is $111$ seconds, and your route takes $100$ seconds if everything goes right.

After playing for $20$ seconds, there is a trick with a $50\% $ success rate. If it succeeds, you keep playing. If it fails, you incur a $10$ second time loss: now the run will take at least $110$ seconds. It is still possible to set a record, but every other trick in the run has to be successful. It turns out to be faster on average to reset after failing the first trick.

Thus you repeat the first $20$ seconds of the game until the trick is successful: with probability $1/2$, it takes $1$ attempt; with probability $1/4$, it takes $2$ attempts; and so on. On average, you spend $40$ seconds on the first $20$ seconds of the route.

Once you have successfully performed the first trick, you want to finish the run no matter the result of the other tricks: it takes $80$ seconds, plus on average $1$ second loss from each of the remaining $4$ tricks. So the expected time until you set a record is $124$ seconds.

-----Examples-----
Sample Input 1:
100 111 5
20 0.5 10
80 0.5 2
85 0.5 2
90 0.5 2
95 0.5 2
Sample Output 1:
124

Sample Input 2:
2 4 1
1 0.5 5
Sample Output 2:
3

Sample Input 3:
10 20 3
5 0.3 8
6 0.8 3
8 0.9 3
Sample Output 3:
18.9029850746

---
