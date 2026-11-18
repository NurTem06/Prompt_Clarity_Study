# Person 2 — 45 revised Clear / Less-explicit prompt pairs (Python 3)

**Status:** Complete *candidate* dataset. Independent semantic-equivalence and clarity review has not yet been conducted.
**Source:** `person_2_tasks_45.json`: 45 tasks, 15 in each Introductory / Interview / Competition category.
**Clear provenance:** For 43 tasks, the Clear prompt is unchanged from the source JSON. For **4042 (Codeforces 409E)** and **36 (Codeforces 615E)**, the original problem relies on essential illustrations missing from the source JSON, so both conditions now contain the **same complete technical reconstruction in text**; these two Clear variants are not verbatim originals.
**Less-explicit:** Indirect task-objective wording that preserves the target computation and input/output protocol. The `-----Input-----`, `-----Output-----`, `-----Examples-----`, and `-----Note-----` sections are preserved verbatim from the Clear prompt.
**Image-source reference:** These URLs are for manual audit only and are **not inserted into model prompts**.
- 409E: https://espresso.codeforces.com/c31986fa51b42dbd7b302f5c55e5f7c7836dc848.png
- 615E coordinate image: https://espresso.codeforces.com/3b2337e9f4aadba64c4f33339db20ad466e772b7.png
- 615E spiral image: https://espresso.codeforces.com/5662ae948778adbfe5476af10bd0c1c576d7afb1.png
**Methodology:** This is an oversized 45-task candidate pool, not the final 30-task/person selection. Every pair must pass independent full-prompt explicitness and equivalence checks.

## Common system message (identical for Clear and Less-explicit)

```text
Solve the programming problem using Python 3. Read from standard input and write to standard output. Return only executable Python 3 source code, without Markdown or explanations.
```

## Inventory

| Category | Task IDs |
|---|---|
| introductory | 4030, 4031, 4032, 4033, 4034, 4035, 4036, 4037, 4038, 4039, 4040, 4041, 4042, 4043, 4044 |
| interview | 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44 |
| competition | 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3041, 3042, 3043, 3044 |

## Recovered image-based source problems

| ID | Original source issue | Recovery and automated validation |
|---|---|---|
| **4042** | Diagram is the entire task objective | Square-pyramid/hemisphere geometry reconstructed; **44/44** supplied pairs satisfy the formula |
| **36** | Two essential diagrams missing (coordinate convention, spiral) | Both encoded in shared textual rules; **135/135** supplied pairs reproduced |

**Note:** Reconstructing a diagram as text changes the presentation relative to the original Codeforces statement. This is documented explicitly rather than claiming that these two Clear prompts remain canonical byte-for-byte.

## Prompt pairs

---

### introductory — ID 4030

**Source:** https://codeforces.com/problemset/problem/1296/E2
**Review status:** `candidate_requires_human_review`

**Source and design flags:**

- DEPENDENCY: Same conceptual problem as ID 4034 (hard/easy versions). This reduces task independence.

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You have to color all its characters the minimum number of colors (each character to exactly one color, the same letters can be colored the same or different colors, i.e. you can choose exactly one color for each index in $s$).

> **After:** Assign exactly one color to every character. The palette may be reused across equal or different letters; its size should be no larger than necessary for the sorting arrangement.

2. **body**

> **Before:** Your task is to find the minimum number of colors which you have to color the given string in so that after coloring it can become sorted by some sequence of swaps. Note that you have to restore only coloring, not the sequence of swaps.

> **After:** Give a coloring that lets the permitted swaps put the string in alphabetical order, using as economical a palette as possible. The swaps themselves are not part of the requested answer.

#### Clear prompt

````text
This is a hard version of the problem. The actual problems are different, but the easy version is almost a subtask of the hard version. Note that the constraints and the output format are different.

You are given a string $s$ consisting of $n$ lowercase Latin letters.

You have to color all its characters the minimum number of colors (each character to exactly one color, the same letters can be colored the same or different colors, i.e. you can choose exactly one color for each index in $s$).

After coloring, you can swap any two neighboring characters of the string that are colored different colors. You can perform such an operation arbitrary (possibly, zero) number of times.

The goal is to make the string sorted, i.e. all characters should be in alphabetical order.

Your task is to find the minimum number of colors which you have to color the given string in so that after coloring it can become sorted by some sequence of swaps. Note that you have to restore only coloring, not the sequence of swaps.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the length of $s$.

The second line of the input contains the string $s$ consisting of exactly $n$ lowercase Latin letters.


-----Output-----

In the first line print one integer $res$ ($1 \le res \le n$) — the minimum number of colors in which you have to color the given string so that after coloring it can become sorted by some sequence of swaps.

In the second line print any possible coloring that can be used to sort the string using some sequence of swaps described in the problem statement. The coloring is the array $c$ of length $n$, where $1 \le c_i \le res$ and $c_i$ means the color of the $i$-th character.


-----Examples-----
Input
9
abacbecfd

Output
2
1 1 2 1 2 1 2 1 2 

Input
8
aaabbcbb

Output
2
1 2 1 2 1 2 1 1

Input
7
abcdedc

Output
3
1 1 1 1 1 2 3 

Input
5
abcde

Output
1
1 1 1 1 1
````

#### Less-explicit prompt

````text
This is a hard version of the problem. The actual problems are different, but the easy version is almost a subtask of the hard version. Note that the constraints and the output format are different.

You are given a string $s$ consisting of $n$ lowercase Latin letters.

Assign exactly one color to every character. The palette may be reused across equal or different letters; its size should be no larger than necessary for the sorting arrangement.

After coloring, you can swap any two neighboring characters of the string that are colored different colors. You can perform such an operation arbitrary (possibly, zero) number of times.

The goal is to make the string sorted, i.e. all characters should be in alphabetical order.

Give a coloring that lets the permitted swaps put the string in alphabetical order, using as economical a palette as possible. The swaps themselves are not part of the requested answer.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the length of $s$.

The second line of the input contains the string $s$ consisting of exactly $n$ lowercase Latin letters.


-----Output-----

In the first line print one integer $res$ ($1 \le res \le n$) — the minimum number of colors in which you have to color the given string so that after coloring it can become sorted by some sequence of swaps.

In the second line print any possible coloring that can be used to sort the string using some sequence of swaps described in the problem statement. The coloring is the array $c$ of length $n$, where $1 \le c_i \le res$ and $c_i$ means the color of the $i$-th character.


-----Examples-----
Input
9
abacbecfd

Output
2
1 1 2 1 2 1 2 1 2 

Input
8
aaabbcbb

Output
2
1 2 1 2 1 2 1 1

Input
7
abcdedc

Output
3
1 1 1 1 1 2 3 

Input
5
abcde

Output
1
1 1 1 1 1
````

---

### introductory — ID 4031

**Source:** https://codeforces.com/problemset/problem/988/B
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Rearrange (reorder) the given strings in such a way that for every string, all strings that are placed before it are its substrings.

> **After:** Consider an ordering of the given strings in which every earlier string can be found as a contiguous part of each string that follows it.

#### Clear prompt

````text
You are given $n$ strings. Each string consists of lowercase English letters. Rearrange (reorder) the given strings in such a way that for every string, all strings that are placed before it are its substrings.

String $a$ is a substring of string $b$ if it is possible to choose several consecutive letters in $b$ in such a way that they form $a$. For example, string "for" is contained as a substring in strings "codeforces", "for" and "therefore", but is not contained as a substring in strings "four", "fofo" and "rof".


-----Input-----

The first line contains an integer $n$ ($1 \le n \le 100$) — the number of strings.

The next $n$ lines contain the given strings. The number of letters in each string is from $1$ to $100$, inclusive. Each string consists of lowercase English letters.

Some strings might be equal.


-----Output-----

If it is impossible to reorder $n$ given strings in required order, print "NO" (without quotes).

Otherwise print "YES" (without quotes) and $n$ given strings in required order.


-----Examples-----
Input
5
a
aba
abacaba
ba
aba

Output
YES
a
ba
aba
aba
abacaba

Input
5
a
abacaba
ba
aba
abab

Output
NO

Input
3
qwerty
qwerty
qwerty

Output
YES
qwerty
qwerty
qwerty



-----Note-----

In the second example you cannot reorder the strings because the string "abab" is not a substring of the string "abacaba".
````

#### Less-explicit prompt

````text
You are given $n$ strings. Each string consists of lowercase English letters. Consider an ordering of the given strings in which every earlier string can be found as a contiguous part of each string that follows it.

String $a$ is a substring of string $b$ if it is possible to choose several consecutive letters in $b$ in such a way that they form $a$. For example, string "for" is contained as a substring in strings "codeforces", "for" and "therefore", but is not contained as a substring in strings "four", "fofo" and "rof".


-----Input-----

The first line contains an integer $n$ ($1 \le n \le 100$) — the number of strings.

The next $n$ lines contain the given strings. The number of letters in each string is from $1$ to $100$, inclusive. Each string consists of lowercase English letters.

Some strings might be equal.


-----Output-----

If it is impossible to reorder $n$ given strings in required order, print "NO" (without quotes).

Otherwise print "YES" (without quotes) and $n$ given strings in required order.


-----Examples-----
Input
5
a
aba
abacaba
ba
aba

Output
YES
a
ba
aba
aba
abacaba

Input
5
a
abacaba
ba
aba
abab

Output
NO

Input
3
qwerty
qwerty
qwerty

Output
YES
qwerty
qwerty
qwerty



-----Note-----

In the second example you cannot reorder the strings because the string "abab" is not a substring of the string "abacaba".
````

---

### introductory — ID 4032

**Source:** https://codeforces.com/problemset/problem/999/A
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** How many problems can Mishka solve?

> **After:** Determine how far Mishka can get through the list before the end-only rule and the difficulty threshold leave no available move.

#### Clear prompt

````text
Mishka started participating in a programming contest. There are $n$ problems in the contest. Mishka's problem-solving skill is equal to $k$.

Mishka arranges all problems from the contest into a list. Because of his weird principles, Mishka only solves problems from one of the ends of the list. Every time, he chooses which end (left or right) he will solve the next problem from. Thus, each problem Mishka solves is either the leftmost or the rightmost problem in the list.

Mishka cannot solve a problem with difficulty greater than $k$. When Mishka solves the problem, it disappears from the list, so the length of the list decreases by $1$. Mishka stops when he is unable to solve any problem from any end of the list.

How many problems can Mishka solve?


-----Input-----

The first line of input contains two integers $n$ and $k$ ($1 \le n, k \le 100$) — the number of problems in the contest and Mishka's problem-solving skill.

The second line of input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$), where $a_i$ is the difficulty of the $i$-th problem. The problems are given in order from the leftmost to the rightmost in the list.


-----Output-----

Print one integer — the maximum number of problems Mishka can solve.


-----Examples-----
Input
8 4
4 2 3 1 5 1 6 4

Output
5

Input
5 2
3 1 2 1 3

Output
0

Input
5 100
12 34 55 43 21

Output
5



-----Note-----

In the first example, Mishka can solve problems in the following order: $[4, 2, 3, 1, 5, 1, 6, 4] \rightarrow [2, 3, 1, 5, 1, 6, 4] \rightarrow [2, 3, 1, 5, 1, 6] \rightarrow [3, 1, 5, 1, 6] \rightarrow [1, 5, 1, 6] \rightarrow [5, 1, 6]$, so the number of solved problems will be equal to $5$.

In the second example, Mishka can't solve any problem because the difficulties of problems from both ends are greater than $k$.

In the third example, Mishka's solving skill is so amazing that he can solve all the problems.
````

#### Less-explicit prompt

````text
Mishka started participating in a programming contest. There are $n$ problems in the contest. Mishka's problem-solving skill is equal to $k$.

Mishka arranges all problems from the contest into a list. Because of his weird principles, Mishka only solves problems from one of the ends of the list. Every time, he chooses which end (left or right) he will solve the next problem from. Thus, each problem Mishka solves is either the leftmost or the rightmost problem in the list.

Mishka cannot solve a problem with difficulty greater than $k$. When Mishka solves the problem, it disappears from the list, so the length of the list decreases by $1$. Mishka stops when he is unable to solve any problem from any end of the list.

Determine how far Mishka can get through the list before the end-only rule and the difficulty threshold leave no available move.


-----Input-----

The first line of input contains two integers $n$ and $k$ ($1 \le n, k \le 100$) — the number of problems in the contest and Mishka's problem-solving skill.

The second line of input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 100$), where $a_i$ is the difficulty of the $i$-th problem. The problems are given in order from the leftmost to the rightmost in the list.


-----Output-----

Print one integer — the maximum number of problems Mishka can solve.


-----Examples-----
Input
8 4
4 2 3 1 5 1 6 4

Output
5

Input
5 2
3 1 2 1 3

Output
0

Input
5 100
12 34 55 43 21

Output
5



-----Note-----

In the first example, Mishka can solve problems in the following order: $[4, 2, 3, 1, 5, 1, 6, 4] \rightarrow [2, 3, 1, 5, 1, 6, 4] \rightarrow [2, 3, 1, 5, 1, 6] \rightarrow [3, 1, 5, 1, 6] \rightarrow [1, 5, 1, 6] \rightarrow [5, 1, 6]$, so the number of solved problems will be equal to $5$.

In the second example, Mishka can't solve any problem because the difficulties of problems from both ends are greater than $k$.

In the third example, Mishka's solving skill is so amazing that he can solve all the problems.
````

---

### introductory — ID 4033

**Source:** https://codeforces.com/problemset/problem/1029/F
**Review status:** `needs_source_illustration_review`

**Source and design flags:**

- SOURCE CHECK: Correct/incorrect coloring illustrations are replaced by [Image]; written constraints appear to define the objective, but verify before main experiment.

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Among all correct colorings Vova wants to choose the one with the minimal perimeter. What is the minimal perimeter Vova can obtain?

> **After:** Of the colorings meeting both shape conditions, Vova prefers one whose outer boundary is as short as possible. Determine the perimeter of his preferred outcome.

#### Clear prompt

````text
There is an infinite board of square tiles. Initially all tiles are white.

Vova has a red marker and a blue marker. Red marker can color $a$ tiles. Blue marker can color $b$ tiles. If some tile isn't white then you can't use marker of any color on it. Each marker must be drained completely, so at the end there should be exactly $a$ red tiles and exactly $b$ blue tiles across the board.

Vova wants to color such a set of tiles that:

  they would form a rectangle, consisting of exactly $a+b$ colored tiles;  all tiles of at least one color would also form a rectangle. 

Here are some examples of correct colorings:

 [Image] 

Here are some examples of incorrect colorings:

 [Image] 

Among all correct colorings Vova wants to choose the one with the minimal perimeter. What is the minimal perimeter Vova can obtain?

It is guaranteed that there exists at least one correct coloring.


-----Input-----

A single line contains two integers $a$ and $b$ ($1 \le a, b \le 10^{14}$) — the number of tiles red marker should color and the number of tiles blue marker should color, respectively.


-----Output-----

Print a single integer — the minimal perimeter of a colored rectangle Vova can obtain by coloring exactly $a$ tiles red and exactly $b$ tiles blue.

It is guaranteed that there exists at least one correct coloring.


-----Examples-----
Input
4 4

Output
12

Input
3 9

Output
14

Input
9 3

Output
14

Input
3 6

Output
12

Input
506 2708

Output
3218



-----Note-----

The first four examples correspond to the first picture of the statement.

Note that for there exist multiple correct colorings for all of the examples.

In the first example you can also make a rectangle with sides $1$ and $8$, though its perimeter will be $18$ which is greater than $8$.

In the second example you can make the same resulting rectangle with sides $3$ and $4$, but red tiles will form the rectangle with sides $1$ and $3$ and blue tiles will form the rectangle with sides $3$ and $3$.
````

#### Less-explicit prompt

````text
There is an infinite board of square tiles. Initially all tiles are white.

Vova has a red marker and a blue marker. Red marker can color $a$ tiles. Blue marker can color $b$ tiles. If some tile isn't white then you can't use marker of any color on it. Each marker must be drained completely, so at the end there should be exactly $a$ red tiles and exactly $b$ blue tiles across the board.

Vova wants to color such a set of tiles that:

  they would form a rectangle, consisting of exactly $a+b$ colored tiles;  all tiles of at least one color would also form a rectangle. 

Here are some examples of correct colorings:

 [Image] 

Here are some examples of incorrect colorings:

 [Image] 

Of the colorings meeting both shape conditions, Vova prefers one whose outer boundary is as short as possible. Determine the perimeter of his preferred outcome.

It is guaranteed that there exists at least one correct coloring.


-----Input-----

A single line contains two integers $a$ and $b$ ($1 \le a, b \le 10^{14}$) — the number of tiles red marker should color and the number of tiles blue marker should color, respectively.


-----Output-----

Print a single integer — the minimal perimeter of a colored rectangle Vova can obtain by coloring exactly $a$ tiles red and exactly $b$ tiles blue.

It is guaranteed that there exists at least one correct coloring.


-----Examples-----
Input
4 4

Output
12

Input
3 9

Output
14

Input
9 3

Output
14

Input
3 6

Output
12

Input
506 2708

Output
3218



-----Note-----

The first four examples correspond to the first picture of the statement.

Note that for there exist multiple correct colorings for all of the examples.

In the first example you can also make a rectangle with sides $1$ and $8$, though its perimeter will be $18$ which is greater than $8$.

In the second example you can make the same resulting rectangle with sides $3$ and $4$, but red tiles will form the rectangle with sides $1$ and $3$ and blue tiles will form the rectangle with sides $3$ and $3$.
````

---

### introductory — ID 4034

**Source:** https://codeforces.com/problemset/problem/1296/E1
**Review status:** `candidate_requires_human_review`

**Source and design flags:**

- DEPENDENCY: Same conceptual problem as ID 4030 (easy/hard versions). This reduces task independence.

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You have to color all its characters one of the two colors (each character to exactly one color, the same letters can be colored the same or different colors, i.e. you can choose exactly one color for each index in $s$).

> **After:** Each character is to receive exactly one of two colors; equal letters do not have to share the same color.

2. **body**

> **Before:** Your task is to say if it is possible to color the given string so that after coloring it can become sorted by some sequence of swaps. Note that you have to restore only coloring, not the sequence of swaps.

> **After:** Consider whether some assignment of those colors would allow the permitted swaps to sort the string. Only the assignment, rather than the swap sequence, would need to be exhibited.

#### Clear prompt

````text
This is an easy version of the problem. The actual problems are different, but the easy version is almost a subtask of the hard version. Note that the constraints and the output format are different.

You are given a string $s$ consisting of $n$ lowercase Latin letters.

You have to color all its characters one of the two colors (each character to exactly one color, the same letters can be colored the same or different colors, i.e. you can choose exactly one color for each index in $s$).

After coloring, you can swap any two neighboring characters of the string that are colored different colors. You can perform such an operation arbitrary (possibly, zero) number of times.

The goal is to make the string sorted, i.e. all characters should be in alphabetical order.

Your task is to say if it is possible to color the given string so that after coloring it can become sorted by some sequence of swaps. Note that you have to restore only coloring, not the sequence of swaps.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 200$) — the length of $s$.

The second line of the input contains the string $s$ consisting of exactly $n$ lowercase Latin letters.


-----Output-----

If it is impossible to color the given string so that after coloring it can become sorted by some sequence of swaps, print "NO" (without quotes) in the first line.

Otherwise, print "YES" in the first line and any correct coloring in the second line (the coloring is the string consisting of $n$ characters, the $i$-th character should be '0' if the $i$-th character is colored the first color and '1' otherwise).


-----Examples-----
Input
9
abacbecfd

Output
YES
001010101

Input
8
aaabbcbb

Output
YES
01011011

Input
7
abcdedc

Output
NO

Input
5
abcde

Output
YES
00000
````

#### Less-explicit prompt

````text
This is an easy version of the problem. The actual problems are different, but the easy version is almost a subtask of the hard version. Note that the constraints and the output format are different.

You are given a string $s$ consisting of $n$ lowercase Latin letters.

Each character is to receive exactly one of two colors; equal letters do not have to share the same color.

After coloring, you can swap any two neighboring characters of the string that are colored different colors. You can perform such an operation arbitrary (possibly, zero) number of times.

The goal is to make the string sorted, i.e. all characters should be in alphabetical order.

Consider whether some assignment of those colors would allow the permitted swaps to sort the string. Only the assignment, rather than the swap sequence, would need to be exhibited.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 200$) — the length of $s$.

The second line of the input contains the string $s$ consisting of exactly $n$ lowercase Latin letters.


-----Output-----

If it is impossible to color the given string so that after coloring it can become sorted by some sequence of swaps, print "NO" (without quotes) in the first line.

Otherwise, print "YES" in the first line and any correct coloring in the second line (the coloring is the string consisting of $n$ characters, the $i$-th character should be '0' if the $i$-th character is colored the first color and '1' otherwise).


-----Examples-----
Input
9
abacbecfd

Output
YES
001010101

Input
8
aaabbcbb

Output
YES
01011011

Input
7
abcdedc

Output
NO

Input
5
abcde

Output
YES
00000
````

---

### introductory — ID 4035

**Source:** https://atcoder.jp/contests/abc158/tasks/abc158_c
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Find the price of a product before tax such that, when the consumption tax rate is 8 percent and 10 percent, the amount of consumption tax levied on it is A yen and B yen, respectively. (Yen is the currency of Japan.)

> **After:** A product has an unknown pre-tax price. Its tax amount would be A yen at 8 percent and B yen at 10 percent; infer a compatible price. (Yen is the currency of Japan.)

2. **body**

> **Before:** If multiple prices satisfy the condition, print the lowest such price; if no price satisfies the condition, print -1.

> **After:** Of compatible prices, use the first one in increasing order. If there is none, use -1.

#### Clear prompt

````text
Find the price of a product before tax such that, when the consumption tax rate is 8 percent and 10 percent, the amount of consumption tax levied on it is A yen and B yen, respectively. (Yen is the currency of Japan.)
Here, the price before tax must be a positive integer, and the amount of consumption tax is rounded down to the nearest integer.
If multiple prices satisfy the condition, print the lowest such price; if no price satisfies the condition, print -1.

-----Constraints-----
 - 1 \leq A \leq B \leq 100
 - A and B are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
If there is a price that satisfies the condition, print an integer representing the lowest such price; otherwise, print -1.

-----Sample Input-----
2 2

-----Sample Output-----
25

If the price of a product before tax is 25 yen, the amount of consumption tax levied on it is:
 - When the consumption tax rate is 8 percent: \lfloor 25 \times 0.08 \rfloor = \lfloor 2 \rfloor = 2 yen.
 - When the consumption tax rate is 10 percent: \lfloor 25 \times 0.1 \rfloor = \lfloor 2.5 \rfloor = 2 yen.
Thus, the price of 25 yen satisfies the condition. There are other possible prices, such as 26 yen, but print the minimum such price, 25.
````

#### Less-explicit prompt

````text
A product has an unknown pre-tax price. Its tax amount would be A yen at 8 percent and B yen at 10 percent; infer a compatible price. (Yen is the currency of Japan.)
Here, the price before tax must be a positive integer, and the amount of consumption tax is rounded down to the nearest integer.
Of compatible prices, use the first one in increasing order. If there is none, use -1.

-----Constraints-----
 - 1 \leq A \leq B \leq 100
 - A and B are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
If there is a price that satisfies the condition, print an integer representing the lowest such price; otherwise, print -1.

-----Sample Input-----
2 2

-----Sample Output-----
25

If the price of a product before tax is 25 yen, the amount of consumption tax levied on it is:
 - When the consumption tax rate is 8 percent: \lfloor 25 \times 0.08 \rfloor = \lfloor 2 \rfloor = 2 yen.
 - When the consumption tax rate is 10 percent: \lfloor 25 \times 0.1 \rfloor = \lfloor 2.5 \rfloor = 2 yen.
Thus, the price of 25 yen satisfies the condition. There are other possible prices, such as 26 yen, but print the minimum such price, 25.
````

---

### introductory — ID 4036

**Source:** https://codeforces.com/problemset/problem/1157/D
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Your problem is to find any array $a$ of length $k$ satisfying the conditions above or say that it is impossible to do it.

> **After:** Determine whether Polycarp can distribute the training over the $k$ days consistently with those rules and, if so, exhibit one daily allocation.

#### Clear prompt

````text
Polycarp has to solve exactly $n$ problems to improve his programming skill before an important programming competition. But this competition will be held very soon, most precisely, it will start in $k$ days. It means that Polycarp has exactly $k$ days for training!

Polycarp doesn't want to procrastinate, so he wants to solve at least one problem during each of $k$ days. He also doesn't want to overwork, so if he solves $x$ problems during some day, he should solve no more than $2x$ problems during the next day. And, at last, he wants to improve his skill, so if he solves $x$ problems during some day, he should solve at least $x+1$ problem during the next day.

More formally: let $[a_1, a_2, \dots, a_k]$ be the array of numbers of problems solved by Polycarp. The $i$-th element of this array is the number of problems Polycarp solves during the $i$-th day of his training. Then the following conditions must be satisfied:   sum of all $a_i$ for $i$ from $1$ to $k$ should be $n$;  $a_i$ should be greater than zero for each $i$ from $1$ to $k$;  the condition $a_i < a_{i + 1} \le 2 a_i$ should be satisfied for each $i$ from $1$ to $k-1$. 

Your problem is to find any array $a$ of length $k$ satisfying the conditions above or say that it is impossible to do it.


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n \le 10^9, 1 \le k \le 10^5$) — the number of problems Polycarp wants to solve and the number of days Polycarp wants to train.


-----Output-----

If it is impossible to find any array $a$ of length $k$ satisfying Polycarp's rules of training, print "NO" in the first line.

Otherwise print "YES" in the first line, then print $k$ integers $a_1, a_2, \dots, a_k$ in the second line, where $a_i$ should be the number of problems Polycarp should solve during the $i$-th day. If there are multiple answers, you can print any.


-----Examples-----
Input
26 6

Output
YES
1 2 4 5 6 8 

Input
8 3

Output
NO

Input
1 1

Output
YES
1 

Input
9 4

Output
NO
````

#### Less-explicit prompt

````text
Polycarp has to solve exactly $n$ problems to improve his programming skill before an important programming competition. But this competition will be held very soon, most precisely, it will start in $k$ days. It means that Polycarp has exactly $k$ days for training!

Polycarp doesn't want to procrastinate, so he wants to solve at least one problem during each of $k$ days. He also doesn't want to overwork, so if he solves $x$ problems during some day, he should solve no more than $2x$ problems during the next day. And, at last, he wants to improve his skill, so if he solves $x$ problems during some day, he should solve at least $x+1$ problem during the next day.

More formally: let $[a_1, a_2, \dots, a_k]$ be the array of numbers of problems solved by Polycarp. The $i$-th element of this array is the number of problems Polycarp solves during the $i$-th day of his training. Then the following conditions must be satisfied:   sum of all $a_i$ for $i$ from $1$ to $k$ should be $n$;  $a_i$ should be greater than zero for each $i$ from $1$ to $k$;  the condition $a_i < a_{i + 1} \le 2 a_i$ should be satisfied for each $i$ from $1$ to $k-1$. 

Determine whether Polycarp can distribute the training over the $k$ days consistently with those rules and, if so, exhibit one daily allocation.


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n \le 10^9, 1 \le k \le 10^5$) — the number of problems Polycarp wants to solve and the number of days Polycarp wants to train.


-----Output-----

If it is impossible to find any array $a$ of length $k$ satisfying Polycarp's rules of training, print "NO" in the first line.

Otherwise print "YES" in the first line, then print $k$ integers $a_1, a_2, \dots, a_k$ in the second line, where $a_i$ should be the number of problems Polycarp should solve during the $i$-th day. If there are multiple answers, you can print any.


-----Examples-----
Input
26 6

Output
YES
1 2 4 5 6 8 

Input
8 3

Output
NO

Input
1 1

Output
YES
1 

Input
9 4

Output
NO
````

---

### introductory — ID 4037

**Source:** https://codeforces.com/problemset/problem/1203/F2
**Review status:** `candidate_requires_human_review`

**Source and design flags:**

- DEPENDENCY: Same project-rating problem as ID 4039 (hard/easy versions).

#### Change log (not part of either model prompt)

1. **body**

> **Before:** To gain more experience (and money, of course) Polycarp wants to choose the subset of projects having maximum possible size and the order in which he will complete them, so he has enough rating before starting each project, and has non-negative rating after completing each project.

> **After:** Polycarp may select and order projects, but every selected project must be feasible at the moment it begins and leave his rating non-negative. He would rather complete more projects than fewer.

2. **body**

> **Before:** Your task is to calculate the maximum possible size of such subset of projects.

> **After:** Work out how many projects he can manage in the most favorable feasible selection.

#### Clear prompt

````text
The only difference between easy and hard versions is that you should complete all the projects in easy version but this is not necessary in hard version.

Polycarp is a very famous freelancer. His current rating is $r$ units.

Some very rich customers asked him to complete some projects for their companies. To complete the $i$-th project, Polycarp needs to have at least $a_i$ units of rating; after he completes this project, his rating will change by $b_i$ (his rating will increase or decrease by $b_i$) ($b_i$ can be positive or negative). Polycarp's rating should not fall below zero because then people won't trust such a low rated freelancer.

Polycarp can choose the order in which he completes projects. Furthermore, he can even skip some projects altogether.

To gain more experience (and money, of course) Polycarp wants to choose the subset of projects having maximum possible size and the order in which he will complete them, so he has enough rating before starting each project, and has non-negative rating after completing each project.

Your task is to calculate the maximum possible size of such subset of projects.


-----Input-----

The first line of the input contains two integers $n$ and $r$ ($1 \le n \le 100, 1 \le r \le 30000$) — the number of projects and the initial rating of Polycarp, respectively.

The next $n$ lines contain projects, one per line. The $i$-th project is represented as a pair of integers $a_i$ and $b_i$ ($1 \le a_i \le 30000$, $-300 \le b_i \le 300$) — the rating required to complete the $i$-th project and the rating change after the project completion.


-----Output-----

Print one integer — the size of the maximum possible subset (possibly, empty) of projects Polycarp can choose.


-----Examples-----
Input
3 4
4 6
10 -2
8 -1

Output
3

Input
5 20
45 -6
34 -15
10 34
1 27
40 -45

Output
5

Input
3 2
300 -300
1 299
1 123

Output
3
````

#### Less-explicit prompt

````text
The only difference between easy and hard versions is that you should complete all the projects in easy version but this is not necessary in hard version.

Polycarp is a very famous freelancer. His current rating is $r$ units.

Some very rich customers asked him to complete some projects for their companies. To complete the $i$-th project, Polycarp needs to have at least $a_i$ units of rating; after he completes this project, his rating will change by $b_i$ (his rating will increase or decrease by $b_i$) ($b_i$ can be positive or negative). Polycarp's rating should not fall below zero because then people won't trust such a low rated freelancer.

Polycarp can choose the order in which he completes projects. Furthermore, he can even skip some projects altogether.

Polycarp may select and order projects, but every selected project must be feasible at the moment it begins and leave his rating non-negative. He would rather complete more projects than fewer.

Work out how many projects he can manage in the most favorable feasible selection.


-----Input-----

The first line of the input contains two integers $n$ and $r$ ($1 \le n \le 100, 1 \le r \le 30000$) — the number of projects and the initial rating of Polycarp, respectively.

The next $n$ lines contain projects, one per line. The $i$-th project is represented as a pair of integers $a_i$ and $b_i$ ($1 \le a_i \le 30000$, $-300 \le b_i \le 300$) — the rating required to complete the $i$-th project and the rating change after the project completion.


-----Output-----

Print one integer — the size of the maximum possible subset (possibly, empty) of projects Polycarp can choose.


-----Examples-----
Input
3 4
4 6
10 -2
8 -1

Output
3

Input
5 20
45 -6
34 -15
10 34
1 27
40 -45

Output
5

Input
3 2
300 -300
1 299
1 123

Output
3
````

---

### introductory — ID 4038

**Source:** https://codeforces.com/problemset/problem/1118/C
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You are given $n^2$ integers. Put them into a matrix of $n$ rows and $n$ columns so that each number is used exactly once, each cell contains exactly one number and the resulting matrix is palindromic. If there are multiple answers, print any. If there is no solution, print "NO".

> **After:** The $n^2$ given integers are to fill an $n$-by-$n$ matrix, one occurrence per cell, without changing their multiplicities. Investigate whether a placement can have the row- and column-reversal symmetry described above; any such placement is suitable.

#### Clear prompt

````text
Let's call some square matrix with integer values in its cells palindromic if it doesn't change after the order of rows is reversed and it doesn't change after the order of columns is reversed.

For example, the following matrices are palindromic: $\left[ \begin{array}{l l l}{1} & {3} & {1} \\{3} & {1} & {3} \\{1} & {3} & {1} \end{array} \right] \quad \left[ \begin{array}{l l l l}{1} & {2} & {2} & {1} \\{8} & {2} & {2} & {8} \\{8} & {2} & {2} & {8} \\{1} & {2} & {2} & {1} \end{array} \right]$ 

The following matrices are not palindromic because they change after the order of rows is reversed: $\left[ \begin{array}{l l l}{1} & {3} & {1} \\{3} & {1} & {3} \\{2} & {3} & {2} \end{array} \right] \rightarrow \left[ \begin{array}{l l l}{2} & {3} & {2} \\{3} & {1} & {3} \\{1} & {3} & {1} \end{array} \right] \quad \left[ \begin{array}{l l l l}{1} & {8} & {8} & {9} \\{2} & {4} & {3} & {2} \\{1} & {3} & {4} & {1} \\{9} & {8} & {8} & {1} \end{array} \right] \rightarrow \left[ \begin{array}{l l l l}{9} & {8} & {8} & {1} \\{1} & {3} & {4} & {1} \\{2} & {4} & {3} & {2} \\{1} & {8} & {8} & {9} \end{array} \right]$ 

The following matrices are not palindromic because they change after the order of columns is reversed: $\left[ \begin{array}{l l l}{1} & {3} & {2} \\{3} & {1} & {3} \\{1} & {3} & {2} \end{array} \right] \rightarrow \left[ \begin{array}{l l l}{2} & {3} & {1} \\{3} & {1} & {3} \\{2} & {3} & {1} \end{array} \right] \quad \left[ \begin{array}{l l l l}{1} & {2} & {1} & {9} \\{8} & {4} & {3} & {8} \\{8} & {3} & {4} & {8} \\{9} & {2} & {1} & {1} \end{array} \right] \rightarrow \left[ \begin{array}{l l l l}{9} & {1} & {2} & {1} \\{8} & {3} & {4} & {8} \\{8} & {4} & {3} & {8} \\{1} & {1} & {2} & {9} \end{array} \right]$ 

You are given $n^2$ integers. Put them into a matrix of $n$ rows and $n$ columns so that each number is used exactly once, each cell contains exactly one number and the resulting matrix is palindromic. If there are multiple answers, print any. If there is no solution, print "NO".


-----Input-----

The first line contains one integer $n$ ($1 \le n \le 20$).

The second line contains $n^2$ integers $a_1, a_2, \dots, a_{n^2}$ ($1 \le a_i \le 1000$) — the numbers to put into a matrix of $n$ rows and $n$ columns.


-----Output-----

If it is possible to put all of the $n^2$ numbers into a matrix of $n$ rows and $n$ columns so that each number is used exactly once, each cell contains exactly one number and the resulting matrix is palindromic, then print "YES". Then print $n$ lines with $n$ space-separated numbers — the resulting matrix.

If it's impossible to construct any matrix, then print "NO".

You can print each letter in any case (upper or lower). For example, "YeS", "no" and "yES" are all acceptable.


-----Examples-----
Input
4
1 8 8 1 2 2 2 2 2 2 2 2 1 8 8 1

Output
YES
1 2 2 1
8 2 2 8
8 2 2 8
1 2 2 1

Input
3
1 1 1 1 1 3 3 3 3

Output
YES
1 3 1
3 1 3
1 3 1

Input
4
1 2 1 9 8 4 3 8 8 3 4 8 9 2 1 1

Output
NO

Input
1
10

Output
YES
10 



-----Note-----

Note that there exist multiple answers for the first two examples.
````

#### Less-explicit prompt

````text
Let's call some square matrix with integer values in its cells palindromic if it doesn't change after the order of rows is reversed and it doesn't change after the order of columns is reversed.

For example, the following matrices are palindromic: $\left[ \begin{array}{l l l}{1} & {3} & {1} \\{3} & {1} & {3} \\{1} & {3} & {1} \end{array} \right] \quad \left[ \begin{array}{l l l l}{1} & {2} & {2} & {1} \\{8} & {2} & {2} & {8} \\{8} & {2} & {2} & {8} \\{1} & {2} & {2} & {1} \end{array} \right]$ 

The following matrices are not palindromic because they change after the order of rows is reversed: $\left[ \begin{array}{l l l}{1} & {3} & {1} \\{3} & {1} & {3} \\{2} & {3} & {2} \end{array} \right] \rightarrow \left[ \begin{array}{l l l}{2} & {3} & {2} \\{3} & {1} & {3} \\{1} & {3} & {1} \end{array} \right] \quad \left[ \begin{array}{l l l l}{1} & {8} & {8} & {9} \\{2} & {4} & {3} & {2} \\{1} & {3} & {4} & {1} \\{9} & {8} & {8} & {1} \end{array} \right] \rightarrow \left[ \begin{array}{l l l l}{9} & {8} & {8} & {1} \\{1} & {3} & {4} & {1} \\{2} & {4} & {3} & {2} \\{1} & {8} & {8} & {9} \end{array} \right]$ 

The following matrices are not palindromic because they change after the order of columns is reversed: $\left[ \begin{array}{l l l}{1} & {3} & {2} \\{3} & {1} & {3} \\{1} & {3} & {2} \end{array} \right] \rightarrow \left[ \begin{array}{l l l}{2} & {3} & {1} \\{3} & {1} & {3} \\{2} & {3} & {1} \end{array} \right] \quad \left[ \begin{array}{l l l l}{1} & {2} & {1} & {9} \\{8} & {4} & {3} & {8} \\{8} & {3} & {4} & {8} \\{9} & {2} & {1} & {1} \end{array} \right] \rightarrow \left[ \begin{array}{l l l l}{9} & {1} & {2} & {1} \\{8} & {3} & {4} & {8} \\{8} & {4} & {3} & {8} \\{1} & {1} & {2} & {9} \end{array} \right]$ 

The $n^2$ given integers are to fill an $n$-by-$n$ matrix, one occurrence per cell, without changing their multiplicities. Investigate whether a placement can have the row- and column-reversal symmetry described above; any such placement is suitable.


-----Input-----

The first line contains one integer $n$ ($1 \le n \le 20$).

The second line contains $n^2$ integers $a_1, a_2, \dots, a_{n^2}$ ($1 \le a_i \le 1000$) — the numbers to put into a matrix of $n$ rows and $n$ columns.


-----Output-----

If it is possible to put all of the $n^2$ numbers into a matrix of $n$ rows and $n$ columns so that each number is used exactly once, each cell contains exactly one number and the resulting matrix is palindromic, then print "YES". Then print $n$ lines with $n$ space-separated numbers — the resulting matrix.

If it's impossible to construct any matrix, then print "NO".

You can print each letter in any case (upper or lower). For example, "YeS", "no" and "yES" are all acceptable.


-----Examples-----
Input
4
1 8 8 1 2 2 2 2 2 2 2 2 1 8 8 1

Output
YES
1 2 2 1
8 2 2 8
8 2 2 8
1 2 2 1

Input
3
1 1 1 1 1 3 3 3 3

Output
YES
1 3 1
3 1 3
1 3 1

Input
4
1 2 1 9 8 4 3 8 8 3 4 8 9 2 1 1

Output
NO

Input
1
10

Output
YES
10 



-----Note-----

Note that there exist multiple answers for the first two examples.
````

---

### introductory — ID 4039

**Source:** https://codeforces.com/problemset/problem/1203/F1
**Review status:** `candidate_requires_human_review`

**Source and design flags:**

- DEPENDENCY: Same project-rating problem as ID 4037 (easy/hard versions).

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Is it possible to complete all the projects? Formally, write a program to check if such an order of the projects exists, that Polycarp has enough rating before starting each project, and he has non-negative rating after completing each project.

> **After:** Consider whether the entire set of projects can be handled in some order without ever beginning a project below its required rating or finishing it with negative rating.

2. **body**

> **Before:** In other words, you have to check that there exists such an order of projects in which Polycarp will complete them, so he has enough rating before starting each project, and has non-negative rating after completing each project.

> **After:** The question concerns the existence of a feasible order for every project, not merely some subset of projects.

#### Clear prompt

````text
The only difference between easy and hard versions is that you should complete all the projects in easy version but this is not necessary in hard version.

Polycarp is a very famous freelancer. His current rating is $r$ units.

Some very rich customers asked him to complete some projects for their companies. To complete the $i$-th project, Polycarp needs to have at least $a_i$ units of rating; after he completes this project, his rating will change by $b_i$ (his rating will increase or decrease by $b_i$) ($b_i$ can be positive or negative). Polycarp's rating should not fall below zero because then people won't trust such a low rated freelancer.

Is it possible to complete all the projects? Formally, write a program to check if such an order of the projects exists, that Polycarp has enough rating before starting each project, and he has non-negative rating after completing each project.

In other words, you have to check that there exists such an order of projects in which Polycarp will complete them, so he has enough rating before starting each project, and has non-negative rating after completing each project.


-----Input-----

The first line of the input contains two integers $n$ and $r$ ($1 \le n \le 100, 1 \le r \le 30000$) — the number of projects and the initial rating of Polycarp, respectively.

The next $n$ lines contain projects, one per line. The $i$-th project is represented as a pair of integers $a_i$ and $b_i$ ($1 \le a_i \le 30000$, $-300 \le b_i \le 300$) — the rating required to complete the $i$-th project and the rating change after the project completion.


-----Output-----

Print "YES" or "NO".


-----Examples-----
Input
3 4
4 6
10 -2
8 -1

Output
YES

Input
3 5
4 -5
4 -2
1 3

Output
YES

Input
4 4
5 2
5 -3
2 1
4 -2

Output
YES

Input
3 10
10 0
10 -10
30 0

Output
NO



-----Note-----

In the first example, the possible order is: $1, 2, 3$.

In the second example, the possible order is: $2, 3, 1$.

In the third example, the possible order is: $3, 1, 4, 2$.
````

#### Less-explicit prompt

````text
The only difference between easy and hard versions is that you should complete all the projects in easy version but this is not necessary in hard version.

Polycarp is a very famous freelancer. His current rating is $r$ units.

Some very rich customers asked him to complete some projects for their companies. To complete the $i$-th project, Polycarp needs to have at least $a_i$ units of rating; after he completes this project, his rating will change by $b_i$ (his rating will increase or decrease by $b_i$) ($b_i$ can be positive or negative). Polycarp's rating should not fall below zero because then people won't trust such a low rated freelancer.

Consider whether the entire set of projects can be handled in some order without ever beginning a project below its required rating or finishing it with negative rating.

The question concerns the existence of a feasible order for every project, not merely some subset of projects.


-----Input-----

The first line of the input contains two integers $n$ and $r$ ($1 \le n \le 100, 1 \le r \le 30000$) — the number of projects and the initial rating of Polycarp, respectively.

The next $n$ lines contain projects, one per line. The $i$-th project is represented as a pair of integers $a_i$ and $b_i$ ($1 \le a_i \le 30000$, $-300 \le b_i \le 300$) — the rating required to complete the $i$-th project and the rating change after the project completion.


-----Output-----

Print "YES" or "NO".


-----Examples-----
Input
3 4
4 6
10 -2
8 -1

Output
YES

Input
3 5
4 -5
4 -2
1 3

Output
YES

Input
4 4
5 2
5 -3
2 1
4 -2

Output
YES

Input
3 10
10 0
10 -10
30 0

Output
NO



-----Note-----

In the first example, the possible order is: $1, 2, 3$.

In the second example, the possible order is: $2, 3, 1$.

In the third example, the possible order is: $3, 1, 4, 2$.
````

---

### introductory — ID 4040

**Source:** https://codeforces.com/problemset/problem/1256/C
**Review status:** `needs_source_illustration_review`

**Source and design flags:**

- SOURCE CHECK: The example placement illustration is replaced by [Image]; text and output give the main constraints.

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You want to know if it is possible to reach $n+1$ from $0$ if you can move any platform to the left or to the right arbitrary number of times (possibly, zero) as long as they do not intersect each other (but two platforms can touch each other). It also means that you cannot change the relative order of platforms.

> **After:** Consider how the platforms might be repositioned to make a crossing from cell $0$ to cell $n+1$ possible. They may be shifted left or right, but must never overlap; touching is allowed and their original relative order must be preserved.

#### Clear prompt

````text
There is a river of width $n$. The left bank of the river is cell $0$ and the right bank is cell $n + 1$ (more formally, the river can be represented as a sequence of $n + 2$ cells numbered from $0$ to $n + 1$). There are also $m$ wooden platforms on a river, the $i$-th platform has length $c_i$ (so the $i$-th platform takes $c_i$ consecutive cells of the river). It is guaranteed that the sum of lengths of platforms does not exceed $n$.

You are standing at $0$ and want to reach $n+1$ somehow. If you are standing at the position $x$, you can jump to any position in the range $[x + 1; x + d]$. However you don't really like the water so you can jump only to such cells that belong to some wooden platform. For example, if $d=1$, you can jump only to the next position (if it belongs to the wooden platform). You can assume that cells $0$ and $n+1$ belong to wooden platforms.

You want to know if it is possible to reach $n+1$ from $0$ if you can move any platform to the left or to the right arbitrary number of times (possibly, zero) as long as they do not intersect each other (but two platforms can touch each other). It also means that you cannot change the relative order of platforms.

Note that you should move platforms until you start jumping (in other words, you first move the platforms and then start jumping).

For example, if $n=7$, $m=3$, $d=2$ and $c = [1, 2, 1]$, then one of the ways to reach $8$ from $0$ is follow:

 [Image] The first example: $n=7$. 


-----Input-----

The first line of the input contains three integers $n$, $m$ and $d$ ($1 \le n, m, d \le 1000, m \le n$) — the width of the river, the number of platforms and the maximum distance of your jump, correspondingly.

The second line of the input contains $m$ integers $c_1, c_2, \dots, c_m$ ($1 \le c_i \le n, \sum\limits_{i=1}^{m} c_i \le n$), where $c_i$ is the length of the $i$-th platform.


-----Output-----

If it is impossible to reach $n+1$ from $0$, print NO in the first line. Otherwise, print YES in the first line and the array $a$ of length $n$ in the second line — the sequence of river cells (excluding cell $0$ and cell $n + 1$).

If the cell $i$ does not belong to any platform, $a_i$ should be $0$. Otherwise, it should be equal to the index of the platform ($1$-indexed, platforms are numbered from $1$ to $m$ in order of input) to which the cell $i$ belongs.

Note that all $a_i$ equal to $1$ should form a contiguous subsegment of the array $a$ of length $c_1$, all $a_i$ equal to $2$ should form a contiguous subsegment of the array $a$ of length $c_2$, ..., all $a_i$ equal to $m$ should form a contiguous subsegment of the array $a$ of length $c_m$. The leftmost position of $2$ in $a$ should be greater than the rightmost position of $1$, the leftmost position of $3$ in $a$ should be greater than the rightmost position of $2$, ..., the leftmost position of $m$ in $a$ should be greater than the rightmost position of $m-1$.

See example outputs for better understanding.


-----Examples-----
Input
7 3 2
1 2 1

Output
YES
0 1 0 2 2 0 3 

Input
10 1 11
1

Output
YES
0 0 0 0 0 0 0 0 0 1 

Input
10 1 5
2

Output
YES
0 0 0 0 1 1 0 0 0 0 



-----Note-----

Consider the first example: the answer is $[0, 1, 0, 2, 2, 0, 3]$. The sequence of jumps you perform is $0 \rightarrow 2 \rightarrow 4 \rightarrow 5 \rightarrow 7 \rightarrow 8$.

Consider the second example: it does not matter how to place the platform because you always can jump from $0$ to $11$.

Consider the third example: the answer is $[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]$. The sequence of jumps you perform is $0 \rightarrow 5 \rightarrow 6 \rightarrow 11$.
````

#### Less-explicit prompt

````text
There is a river of width $n$. The left bank of the river is cell $0$ and the right bank is cell $n + 1$ (more formally, the river can be represented as a sequence of $n + 2$ cells numbered from $0$ to $n + 1$). There are also $m$ wooden platforms on a river, the $i$-th platform has length $c_i$ (so the $i$-th platform takes $c_i$ consecutive cells of the river). It is guaranteed that the sum of lengths of platforms does not exceed $n$.

You are standing at $0$ and want to reach $n+1$ somehow. If you are standing at the position $x$, you can jump to any position in the range $[x + 1; x + d]$. However you don't really like the water so you can jump only to such cells that belong to some wooden platform. For example, if $d=1$, you can jump only to the next position (if it belongs to the wooden platform). You can assume that cells $0$ and $n+1$ belong to wooden platforms.

Consider how the platforms might be repositioned to make a crossing from cell $0$ to cell $n+1$ possible. They may be shifted left or right, but must never overlap; touching is allowed and their original relative order must be preserved.

Note that you should move platforms until you start jumping (in other words, you first move the platforms and then start jumping).

For example, if $n=7$, $m=3$, $d=2$ and $c = [1, 2, 1]$, then one of the ways to reach $8$ from $0$ is follow:

 [Image] The first example: $n=7$. 


-----Input-----

The first line of the input contains three integers $n$, $m$ and $d$ ($1 \le n, m, d \le 1000, m \le n$) — the width of the river, the number of platforms and the maximum distance of your jump, correspondingly.

The second line of the input contains $m$ integers $c_1, c_2, \dots, c_m$ ($1 \le c_i \le n, \sum\limits_{i=1}^{m} c_i \le n$), where $c_i$ is the length of the $i$-th platform.


-----Output-----

If it is impossible to reach $n+1$ from $0$, print NO in the first line. Otherwise, print YES in the first line and the array $a$ of length $n$ in the second line — the sequence of river cells (excluding cell $0$ and cell $n + 1$).

If the cell $i$ does not belong to any platform, $a_i$ should be $0$. Otherwise, it should be equal to the index of the platform ($1$-indexed, platforms are numbered from $1$ to $m$ in order of input) to which the cell $i$ belongs.

Note that all $a_i$ equal to $1$ should form a contiguous subsegment of the array $a$ of length $c_1$, all $a_i$ equal to $2$ should form a contiguous subsegment of the array $a$ of length $c_2$, ..., all $a_i$ equal to $m$ should form a contiguous subsegment of the array $a$ of length $c_m$. The leftmost position of $2$ in $a$ should be greater than the rightmost position of $1$, the leftmost position of $3$ in $a$ should be greater than the rightmost position of $2$, ..., the leftmost position of $m$ in $a$ should be greater than the rightmost position of $m-1$.

See example outputs for better understanding.


-----Examples-----
Input
7 3 2
1 2 1

Output
YES
0 1 0 2 2 0 3 

Input
10 1 11
1

Output
YES
0 0 0 0 0 0 0 0 0 1 

Input
10 1 5
2

Output
YES
0 0 0 0 1 1 0 0 0 0 



-----Note-----

Consider the first example: the answer is $[0, 1, 0, 2, 2, 0, 3]$. The sequence of jumps you perform is $0 \rightarrow 2 \rightarrow 4 \rightarrow 5 \rightarrow 7 \rightarrow 8$.

Consider the second example: it does not matter how to place the platform because you always can jump from $0$ to $11$.

Consider the third example: the answer is $[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]$. The sequence of jumps you perform is $0 \rightarrow 5 \rightarrow 6 \rightarrow 11$.
````

---

### introductory — ID 4041

**Source:** https://codeforces.com/problemset/problem/1203/D1
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You want to remove some substring (contiguous subsequence) from $s$ of maximum possible length such that after removing this substring $t$ will remain a subsequence of $s$.

> **After:** A single contiguous part of $s$ may be deleted, provided the remaining characters still contain $t$ in order. You would like the removed portion to be as long as the rule allows.

2. **body**

> **Before:** Your task is to find the maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$.

> **After:** Determine the length achievable by the most extensive such deletion.

#### Clear prompt

````text
The only difference between easy and hard versions is the length of the string.

You are given a string $s$ and a string $t$, both consisting only of lowercase Latin letters. It is guaranteed that $t$ can be obtained from $s$ by removing some (possibly, zero) number of characters (not necessary contiguous) from $s$ without changing order of remaining characters (in other words, it is guaranteed that $t$ is a subsequence of $s$).

For example, the strings "test", "tst", "tt", "et" and "" are subsequences of the string "test". But the strings "tset", "se", "contest" are not subsequences of the string "test".

You want to remove some substring (contiguous subsequence) from $s$ of maximum possible length such that after removing this substring $t$ will remain a subsequence of $s$.

If you want to remove the substring $s[l;r]$ then the string $s$ will be transformed to $s_1 s_2 \dots s_{l-1} s_{r+1} s_{r+2} \dots s_{|s|-1} s_{|s|}$ (where $|s|$ is the length of $s$).

Your task is to find the maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$.


-----Input-----

The first line of the input contains one string $s$ consisting of at least $1$ and at most $200$ lowercase Latin letters.

The second line of the input contains one string $t$ consisting of at least $1$ and at most $200$ lowercase Latin letters.

It is guaranteed that $t$ is a subsequence of $s$.


-----Output-----

Print one integer — the maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$.


-----Examples-----
Input
bbaba
bb

Output
3

Input
baaba
ab

Output
2

Input
abcde
abcde

Output
0

Input
asdfasdf
fasd

Output
3
````

#### Less-explicit prompt

````text
The only difference between easy and hard versions is the length of the string.

You are given a string $s$ and a string $t$, both consisting only of lowercase Latin letters. It is guaranteed that $t$ can be obtained from $s$ by removing some (possibly, zero) number of characters (not necessary contiguous) from $s$ without changing order of remaining characters (in other words, it is guaranteed that $t$ is a subsequence of $s$).

For example, the strings "test", "tst", "tt", "et" and "" are subsequences of the string "test". But the strings "tset", "se", "contest" are not subsequences of the string "test".

A single contiguous part of $s$ may be deleted, provided the remaining characters still contain $t$ in order. You would like the removed portion to be as long as the rule allows.

If you want to remove the substring $s[l;r]$ then the string $s$ will be transformed to $s_1 s_2 \dots s_{l-1} s_{r+1} s_{r+2} \dots s_{|s|-1} s_{|s|}$ (where $|s|$ is the length of $s$).

Determine the length achievable by the most extensive such deletion.


-----Input-----

The first line of the input contains one string $s$ consisting of at least $1$ and at most $200$ lowercase Latin letters.

The second line of the input contains one string $t$ consisting of at least $1$ and at most $200$ lowercase Latin letters.

It is guaranteed that $t$ is a subsequence of $s$.


-----Output-----

Print one integer — the maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$.


-----Examples-----
Input
bbaba
bb

Output
3

Input
baaba
ab

Output
2

Input
abcde
abcde

Output
0

Input
asdfasdf
fasd

Output
3
````

---

### introductory — ID 4042

**Source:** https://codeforces.com/problemset/problem/409/E
**Review status:** `candidate_requires_human_review`

**Source and design flags:**

- IMAGE-BASED SOURCE: canonical Codeforces statement relies on diagram(s); Clear here is a documented text-only reconstruction, NOT byte-for-byte original.
- BENCHMARK CAUTION: changing image-based problems to text-based statements may affect difficulty; consider excluding from strictly original-statement analyses or report separately.

**Original source figure(s) (not part of model prompts):**

- https://espresso.codeforces.com/c31986fa51b42dbd7b302f5c55e5f7c7836dc848.png

**Reconstruction check:** 44/44 supplied test pairs match.

**Exact original question as supplied by source dataset (retained in JSON as `source_clear_original`):**

````text
$\text{A}$ 


-----Input-----

The input contains a single floating-point number x with exactly 6 decimal places (0 < x < 5).


-----Output-----

Output two integers separated by a single space. Each integer should be between 1 and 10, inclusive. If several solutions exist, output any of them. Solution will exist for all tests.


-----Examples-----
Input
1.200000

Output
3 2

Input
2.572479

Output
10 3

Input
4.024922

Output
9 9
````

#### Change log (not part of either model prompt)

1. **shared_technical_reconstruction**

> **Before:** Original Codeforces figure(s), absent from source JSON

> **After:** A square pyramid has a square base of side length $a$ and a perpendicular height $h$. A hemispherical dome is centered on the base directly below the apex, with its flat face in the base plane and its curved surface tangent to the pyramid's side faces. The radius $r$ of the inscribed dome is determined by the dimensions through $r = \frac{ah}{\sqrt{a^2+4h^2}}$. Both $a$ and $h$ must be integers from $1$ to $10$, inclusive. The given value $x$ is $r$ rounded to six digits after the decimal point.

2. **objective**

> **Before:** Find any integer pair $(a,h)$ within these bounds whose calculated dome radius, rounded to six decimal places, equals $x$. Output the base side length $a$ first, followed by the pyramid height $h$.

> **After:** Determine a permissible set of dimensions consistent with the dome measurement. The resulting pair should be given in the order base-side dimension followed by height; any compatible choice is acceptable.

#### Clear prompt

````text
A square pyramid has a square base of side length $a$ and a perpendicular height $h$. A hemispherical dome is centered on the base directly below the apex, with its flat face in the base plane and its curved surface tangent to the pyramid's side faces. The radius $r$ of the inscribed dome is determined by the dimensions through $r = \frac{ah}{\sqrt{a^2+4h^2}}$. Both $a$ and $h$ must be integers from $1$ to $10$, inclusive. The given value $x$ is $r$ rounded to six digits after the decimal point.

Find any integer pair $(a,h)$ within these bounds whose calculated dome radius, rounded to six decimal places, equals $x$. Output the base side length $a$ first, followed by the pyramid height $h$.

-----Input-----

The input contains a single floating-point number x with exactly 6 decimal places (0 < x < 5).


-----Output-----

Output two integers separated by a single space. Each integer should be between 1 and 10, inclusive. If several solutions exist, output any of them. Solution will exist for all tests.


-----Examples-----
Input
1.200000

Output
3 2

Input
2.572479

Output
10 3

Input
4.024922

Output
9 9
````

#### Less-explicit prompt

````text
A square pyramid has a square base of side length $a$ and a perpendicular height $h$. A hemispherical dome is centered on the base directly below the apex, with its flat face in the base plane and its curved surface tangent to the pyramid's side faces. The radius $r$ of the inscribed dome is determined by the dimensions through $r = \frac{ah}{\sqrt{a^2+4h^2}}$. Both $a$ and $h$ must be integers from $1$ to $10$, inclusive. The given value $x$ is $r$ rounded to six digits after the decimal point.

Determine a permissible set of dimensions consistent with the dome measurement. The resulting pair should be given in the order base-side dimension followed by height; any compatible choice is acceptable.

-----Input-----

The input contains a single floating-point number x with exactly 6 decimal places (0 < x < 5).


-----Output-----

Output two integers separated by a single space. Each integer should be between 1 and 10, inclusive. If several solutions exist, output any of them. Solution will exist for all tests.


-----Examples-----
Input
1.200000

Output
3 2

Input
2.572479

Output
10 3

Input
4.024922

Output
9 9
````

---

### introductory — ID 4043

**Source:** https://codeforces.com/problemset/problem/1003/E
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Your task is to construct an undirected tree on $n$ vertices with diameter $d$ and degree of each vertex at most $k$, or say that it is impossible.

> **After:** Consider whether an undirected tree with $n$ vertices can meet both the requested diameter $d$ and the per-vertex degree limit $k$. Where it can, provide one example.

#### Clear prompt

````text
You are given three integers $n$, $d$ and $k$.

Your task is to construct an undirected tree on $n$ vertices with diameter $d$ and degree of each vertex at most $k$, or say that it is impossible.

An undirected tree is a connected undirected graph with $n - 1$ edges.

Diameter of a tree is the maximum length of a simple path (a path in which each vertex appears at most once) between all pairs of vertices of this tree.

Degree of a vertex is the number of edges incident to this vertex (i.e. for a vertex $u$ it is the number of edges $(u, v)$ that belong to the tree, where $v$ is any other vertex of a tree).


-----Input-----

The first line of the input contains three integers $n$, $d$ and $k$ ($1 \le n, d, k \le 4 \cdot 10^5$).


-----Output-----

If there is no tree satisfying the conditions above, print only one word "NO" (without quotes).

Otherwise in the first line print "YES" (without quotes), and then print $n - 1$ lines describing edges of a tree satisfying the conditions above. Vertices of the tree must be numbered from $1$ to $n$. You can print edges and vertices connected by an edge in any order. If there are multiple answers, print any of them.1


-----Examples-----
Input
6 3 3

Output
YES
3 1
4 1
1 2
5 2
2 6

Input
6 2 3

Output
NO

Input
10 4 3

Output
YES
2 9
2 10
10 3
3 1
6 10
8 2
4 3
5 6
6 7

Input
8 5 3

Output
YES
2 5
7 2
3 7
3 1
1 6
8 7
4 3
````

#### Less-explicit prompt

````text
You are given three integers $n$, $d$ and $k$.

Consider whether an undirected tree with $n$ vertices can meet both the requested diameter $d$ and the per-vertex degree limit $k$. Where it can, provide one example.

An undirected tree is a connected undirected graph with $n - 1$ edges.

Diameter of a tree is the maximum length of a simple path (a path in which each vertex appears at most once) between all pairs of vertices of this tree.

Degree of a vertex is the number of edges incident to this vertex (i.e. for a vertex $u$ it is the number of edges $(u, v)$ that belong to the tree, where $v$ is any other vertex of a tree).


-----Input-----

The first line of the input contains three integers $n$, $d$ and $k$ ($1 \le n, d, k \le 4 \cdot 10^5$).


-----Output-----

If there is no tree satisfying the conditions above, print only one word "NO" (without quotes).

Otherwise in the first line print "YES" (without quotes), and then print $n - 1$ lines describing edges of a tree satisfying the conditions above. Vertices of the tree must be numbered from $1$ to $n$. You can print edges and vertices connected by an edge in any order. If there are multiple answers, print any of them.1


-----Examples-----
Input
6 3 3

Output
YES
3 1
4 1
1 2
5 2
2 6

Input
6 2 3

Output
NO

Input
10 4 3

Output
YES
2 9
2 10
10 3
3 1
6 10
8 2
4 3
5 6
6 7

Input
8 5 3

Output
YES
2 5
7 2
3 7
3 1
1 6
8 7
4 3
````

---

### introductory — ID 4044

**Source:** https://codeforces.com/problemset/problem/1003/B
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Your task is to construct a binary string $s$ of length $n = a + b$ such that there are exactly $a$ zeroes, exactly $b$ ones and exactly $x$ indices $i$ (where $1 \le i < n$) such that $s_i \ne s_{i + 1}$. It is guaranteed that the answer always exists.

> **After:** Form a binary string of length $n=a+b$ with $a$ zeroes and $b$ ones, arranged so that neighboring characters switch between 0 and 1 at exactly $x$ positions $i$ ($1 \le i<n$). A suitable arrangement is guaranteed to exist.

#### Clear prompt

````text
You are given three integers $a$, $b$ and $x$. Your task is to construct a binary string $s$ of length $n = a + b$ such that there are exactly $a$ zeroes, exactly $b$ ones and exactly $x$ indices $i$ (where $1 \le i < n$) such that $s_i \ne s_{i + 1}$. It is guaranteed that the answer always exists.

For example, for the string "01010" there are four indices $i$ such that $1 \le i < n$ and $s_i \ne s_{i + 1}$ ($i = 1, 2, 3, 4$). For the string "111001" there are two such indices $i$ ($i = 3, 5$).

Recall that binary string is a non-empty sequence of characters where each character is either 0 or 1.


-----Input-----

The first line of the input contains three integers $a$, $b$ and $x$ ($1 \le a, b \le 100, 1 \le x < a + b)$.


-----Output-----

Print only one string $s$, where $s$ is any binary string satisfying conditions described above. It is guaranteed that the answer always exists.


-----Examples-----
Input
2 2 1

Output
1100

Input
3 3 3

Output
101100

Input
5 3 6

Output
01010100



-----Note-----

All possible answers for the first example:   1100;  0011. 

All possible answers for the second example:   110100;  101100;  110010;  100110;  011001;  001101;  010011;  001011.
````

#### Less-explicit prompt

````text
You are given three integers $a$, $b$ and $x$. Form a binary string of length $n=a+b$ with $a$ zeroes and $b$ ones, arranged so that neighboring characters switch between 0 and 1 at exactly $x$ positions $i$ ($1 \le i<n$). A suitable arrangement is guaranteed to exist.

For example, for the string "01010" there are four indices $i$ such that $1 \le i < n$ and $s_i \ne s_{i + 1}$ ($i = 1, 2, 3, 4$). For the string "111001" there are two such indices $i$ ($i = 3, 5$).

Recall that binary string is a non-empty sequence of characters where each character is either 0 or 1.


-----Input-----

The first line of the input contains three integers $a$, $b$ and $x$ ($1 \le a, b \le 100, 1 \le x < a + b)$.


-----Output-----

Print only one string $s$, where $s$ is any binary string satisfying conditions described above. It is guaranteed that the answer always exists.


-----Examples-----
Input
2 2 1

Output
1100

Input
3 3 3

Output
101100

Input
5 3 6

Output
01010100



-----Note-----

All possible answers for the first example:   1100;  0011. 

All possible answers for the second example:   110100;  101100;  110010;  100110;  011001;  001101;  010011;  001011.
````

---

### interview — ID 30

**Source:** https://codeforces.com/problemset/problem/1027/G
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You are responsible to catch the $x$-mouse in the campus, so you are guessing about minimum possible number of traps (one trap in one room) you need to place. You are sure that if the $x$-mouse enters a trapped room, it immediately gets caught.

> **After:** Place traps in rooms so that, whatever the mouse’s initial room, its repeated jumps eventually bring it to a trap. You would like to achieve that coverage without using unnecessary traps (at most one per room).

#### Clear prompt

````text
The campus has $m$ rooms numbered from $0$ to $m - 1$. Also the $x$-mouse lives in the campus. The $x$-mouse is not just a mouse: each second $x$-mouse moves from room $i$ to the room $i \cdot x \mod{m}$ (in fact, it teleports from one room to another since it doesn't visit any intermediate room). Starting position of the $x$-mouse is unknown.

You are responsible to catch the $x$-mouse in the campus, so you are guessing about minimum possible number of traps (one trap in one room) you need to place. You are sure that if the $x$-mouse enters a trapped room, it immediately gets caught.

And the only observation you made is $\text{GCD} (x, m) = 1$.


-----Input-----

The only line contains two integers $m$ and $x$ ($2 \le m \le 10^{14}$, $1 \le x < m$, $\text{GCD} (x, m) = 1$) — the number of rooms and the parameter of $x$-mouse. 


-----Output-----

Print the only integer — minimum number of traps you need to install to catch the $x$-mouse.


-----Examples-----
Input
4 3

Output
3

Input
5 2

Output
2



-----Note-----

In the first example you can, for example, put traps in rooms $0$, $2$, $3$. If the $x$-mouse starts in one of this rooms it will be caught immediately. If $x$-mouse starts in the $1$-st rooms then it will move to the room $3$, where it will be caught.

In the second example you can put one trap in room $0$ and one trap in any other room since $x$-mouse will visit all rooms $1..m-1$ if it will start in any of these rooms.
````

#### Less-explicit prompt

````text
The campus has $m$ rooms numbered from $0$ to $m - 1$. Also the $x$-mouse lives in the campus. The $x$-mouse is not just a mouse: each second $x$-mouse moves from room $i$ to the room $i \cdot x \mod{m}$ (in fact, it teleports from one room to another since it doesn't visit any intermediate room). Starting position of the $x$-mouse is unknown.

Place traps in rooms so that, whatever the mouse’s initial room, its repeated jumps eventually bring it to a trap. You would like to achieve that coverage without using unnecessary traps (at most one per room).

And the only observation you made is $\text{GCD} (x, m) = 1$.


-----Input-----

The only line contains two integers $m$ and $x$ ($2 \le m \le 10^{14}$, $1 \le x < m$, $\text{GCD} (x, m) = 1$) — the number of rooms and the parameter of $x$-mouse. 


-----Output-----

Print the only integer — minimum number of traps you need to install to catch the $x$-mouse.


-----Examples-----
Input
4 3

Output
3

Input
5 2

Output
2



-----Note-----

In the first example you can, for example, put traps in rooms $0$, $2$, $3$. If the $x$-mouse starts in one of this rooms it will be caught immediately. If $x$-mouse starts in the $1$-st rooms then it will move to the room $3$, where it will be caught.

In the second example you can put one trap in room $0$ and one trap in any other room since $x$-mouse will visit all rooms $1..m-1$ if it will start in any of these rooms.
````

---

### interview — ID 31

**Source:** https://codeforces.com/problemset/problem/711/E
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** He is interested in the probability of at least two of them have the birthday at the same day.

> **After:** He is interested in the chance that a shared birthday occurs among those $k$ people.

2. **body**

> **Before:** ZS the Coder knows that the answer can be written as an irreducible fraction $\frac{A}{B}$. He wants to find the values of A and B (he does not like to deal with floating point numbers). Can you help him?

> **After:** Represent that chance as a fraction $\frac{A}{B}$ in lowest terms rather than as a floating-point value.

#### Clear prompt

````text
ZS the Coder has recently found an interesting concept called the Birthday Paradox. It states that given a random set of 23 people, there is around 50% chance that some two of them share the same birthday. ZS the Coder finds this very interesting, and decides to test this with the inhabitants of Udayland.

In Udayland, there are 2^{n} days in a year. ZS the Coder wants to interview k people from Udayland, each of them has birthday in one of 2^{n} days (each day with equal probability). He is interested in the probability of at least two of them have the birthday at the same day. 

ZS the Coder knows that the answer can be written as an irreducible fraction $\frac{A}{B}$. He wants to find the values of A and B (he does not like to deal with floating point numbers). Can you help him?


-----Input-----

The first and only line of the input contains two integers n and k (1 ≤ n ≤ 10^18, 2 ≤ k ≤ 10^18), meaning that there are 2^{n} days in a year and that ZS the Coder wants to interview exactly k people.


-----Output-----

If the probability of at least two k people having the same birthday in 2^{n} days long year equals $\frac{A}{B}$ (A ≥ 0, B ≥ 1, $\operatorname{gcd}(A, B) = 1$), print the A and B in a single line.

Since these numbers may be too large, print them modulo 10^6 + 3. Note that A and B must be coprime before their remainders modulo 10^6 + 3 are taken.


-----Examples-----
Input
3 2

Output
1 8
Input
1 3

Output
1 1
Input
4 3

Output
23 128


-----Note-----

In the first sample case, there are 2^3 = 8 days in Udayland. The probability that 2 people have the same birthday among 2 people is clearly $\frac{1}{8}$, so A = 1, B = 8.

In the second sample case, there are only 2^1 = 2 days in Udayland, but there are 3 people, so it is guaranteed that two of them have the same birthday. Thus, the probability is 1 and A = B = 1.
````

#### Less-explicit prompt

````text
ZS the Coder has recently found an interesting concept called the Birthday Paradox. It states that given a random set of 23 people, there is around 50% chance that some two of them share the same birthday. ZS the Coder finds this very interesting, and decides to test this with the inhabitants of Udayland.

In Udayland, there are 2^{n} days in a year. ZS the Coder wants to interview k people from Udayland, each of them has birthday in one of 2^{n} days (each day with equal probability). He is interested in the chance that a shared birthday occurs among those $k$ people. 

Represent that chance as a fraction $\frac{A}{B}$ in lowest terms rather than as a floating-point value.


-----Input-----

The first and only line of the input contains two integers n and k (1 ≤ n ≤ 10^18, 2 ≤ k ≤ 10^18), meaning that there are 2^{n} days in a year and that ZS the Coder wants to interview exactly k people.


-----Output-----

If the probability of at least two k people having the same birthday in 2^{n} days long year equals $\frac{A}{B}$ (A ≥ 0, B ≥ 1, $\operatorname{gcd}(A, B) = 1$), print the A and B in a single line.

Since these numbers may be too large, print them modulo 10^6 + 3. Note that A and B must be coprime before their remainders modulo 10^6 + 3 are taken.


-----Examples-----
Input
3 2

Output
1 8
Input
1 3

Output
1 1
Input
4 3

Output
23 128


-----Note-----

In the first sample case, there are 2^3 = 8 days in Udayland. The probability that 2 people have the same birthday among 2 people is clearly $\frac{1}{8}$, so A = 1, B = 8.

In the second sample case, there are only 2^1 = 2 days in Udayland, but there are 3 people, so it is guaranteed that two of them have the same birthday. Thus, the probability is 1 and A = B = 1.
````

---

### interview — ID 32

**Source:** https://codeforces.com/problemset/problem/750/B
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Limak isn’t sure whether the description is valid. You must help him to check the following conditions:

> **After:** Limak needs to know whether the itinerary can be followed under these requirements:

2. **body**

> **Before:** Check if the above conditions are satisfied and print "YES" or "NO" on a single line.

> **After:** Indicate whether the itinerary obeys all three requirements.

#### Clear prompt

````text
In this problem we assume the Earth to be a completely round ball and its surface a perfect sphere. The length of the equator and any meridian is considered to be exactly 40 000 kilometers. Thus, travelling from North Pole to South Pole or vice versa takes exactly 20 000 kilometers.

Limak, a polar bear, lives on the North Pole. Close to the New Year, he helps somebody with delivering packages all around the world. Instead of coordinates of places to visit, Limak got a description how he should move, assuming that he starts from the North Pole. The description consists of n parts. In the i-th part of his journey, Limak should move t_{i} kilometers in the direction represented by a string dir_{i} that is one of: "North", "South", "West", "East".

Limak isn’t sure whether the description is valid. You must help him to check the following conditions:  If at any moment of time (before any of the instructions or while performing one of them) Limak is on the North Pole, he can move only to the South.  If at any moment of time (before any of the instructions or while performing one of them) Limak is on the South Pole, he can move only to the North.  The journey must end on the North Pole. 

Check if the above conditions are satisfied and print "YES" or "NO" on a single line.


-----Input-----

The first line of the input contains a single integer n (1 ≤ n ≤ 50).

The i-th of next n lines contains an integer t_{i} and a string dir_{i} (1 ≤ t_{i} ≤ 10^6, $\operatorname{dir}_{i} \in \{\text{North, South, West, East} \}$) — the length and the direction of the i-th part of the journey, according to the description Limak got.


-----Output-----

Print "YES" if the description satisfies the three conditions, otherwise print "NO", both without the quotes.


-----Examples-----
Input
5
7500 South
10000 East
3500 North
4444 West
4000 North

Output
YES

Input
2
15000 South
4000 East

Output
NO

Input
5
20000 South
1000 North
1000000 West
9000 North
10000 North

Output
YES

Input
3
20000 South
10 East
20000 North

Output
NO

Input
2
1000 North
1000 South

Output
NO

Input
4
50 South
50 North
15000 South
15000 North

Output
YES



-----Note-----

Drawings below show how Limak's journey would look like in first two samples. In the second sample the answer is "NO" because he doesn't end on the North Pole. [Image]
````

#### Less-explicit prompt

````text
In this problem we assume the Earth to be a completely round ball and its surface a perfect sphere. The length of the equator and any meridian is considered to be exactly 40 000 kilometers. Thus, travelling from North Pole to South Pole or vice versa takes exactly 20 000 kilometers.

Limak, a polar bear, lives on the North Pole. Close to the New Year, he helps somebody with delivering packages all around the world. Instead of coordinates of places to visit, Limak got a description how he should move, assuming that he starts from the North Pole. The description consists of n parts. In the i-th part of his journey, Limak should move t_{i} kilometers in the direction represented by a string dir_{i} that is one of: "North", "South", "West", "East".

Limak needs to know whether the itinerary can be followed under these requirements:  If at any moment of time (before any of the instructions or while performing one of them) Limak is on the North Pole, he can move only to the South.  If at any moment of time (before any of the instructions or while performing one of them) Limak is on the South Pole, he can move only to the North.  The journey must end on the North Pole. 

Indicate whether the itinerary obeys all three requirements.


-----Input-----

The first line of the input contains a single integer n (1 ≤ n ≤ 50).

The i-th of next n lines contains an integer t_{i} and a string dir_{i} (1 ≤ t_{i} ≤ 10^6, $\operatorname{dir}_{i} \in \{\text{North, South, West, East} \}$) — the length and the direction of the i-th part of the journey, according to the description Limak got.


-----Output-----

Print "YES" if the description satisfies the three conditions, otherwise print "NO", both without the quotes.


-----Examples-----
Input
5
7500 South
10000 East
3500 North
4444 West
4000 North

Output
YES

Input
2
15000 South
4000 East

Output
NO

Input
5
20000 South
1000 North
1000000 West
9000 North
10000 North

Output
YES

Input
3
20000 South
10 East
20000 North

Output
NO

Input
2
1000 North
1000 South

Output
NO

Input
4
50 South
50 North
15000 South
15000 North

Output
YES



-----Note-----

Drawings below show how Limak's journey would look like in first two samples. In the second sample the answer is "NO" because he doesn't end on the North Pole. [Image]
````

---

### interview — ID 33

**Source:** https://codeforces.com/problemset/problem/710/D
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Find the number of integers x such that L ≤ x ≤ R and x = a_1k' + b_1 = a_2l' + b_2, for some integers k', l' ≥ 0.

> **After:** Look for the values appearing in both progressions, taking only terms with non-negative indices and lying within L ≤ x ≤ R. Determine how many such values there are.

#### Clear prompt

````text
You are given two arithmetic progressions: a_1k + b_1 and a_2l + b_2. Find the number of integers x such that L ≤ x ≤ R and x = a_1k' + b_1 = a_2l' + b_2, for some integers k', l' ≥ 0.


-----Input-----

The only line contains six integers a_1, b_1, a_2, b_2, L, R (0 < a_1, a_2 ≤ 2·10^9,  - 2·10^9 ≤ b_1, b_2, L, R ≤ 2·10^9, L ≤ R).


-----Output-----

Print the desired number of integers x.


-----Examples-----
Input
2 0 3 3 5 21

Output
3

Input
2 4 3 0 6 17

Output
2
````

#### Less-explicit prompt

````text
You are given two arithmetic progressions: a_1k + b_1 and a_2l + b_2. Look for the values appearing in both progressions, taking only terms with non-negative indices and lying within L ≤ x ≤ R. Determine how many such values there are.


-----Input-----

The only line contains six integers a_1, b_1, a_2, b_2, L, R (0 < a_1, a_2 ≤ 2·10^9,  - 2·10^9 ≤ b_1, b_2, L, R ≤ 2·10^9, L ≤ R).


-----Output-----

Print the desired number of integers x.


-----Examples-----
Input
2 0 3 3 5 21

Output
3

Input
2 4 3 0 6 17

Output
2
````

---

### interview — ID 34

**Source:** https://codeforces.com/problemset/problem/911/B
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** To make his guests happy, Ivan wants to distribute the cakes in such a way that the minimum number of pieces on the plate is maximized. Formally, Ivan wants to know the maximum possible number x such that he can distribute the cakes according to the aforementioned conditions, and each plate will contain at least x pieces of cake.

> **After:** Among distributions following those rules, Ivan prefers to make the least-served plate as well supplied as possible. Call the number of pieces guaranteed on every plate in the best distribution $x$.

2. **body**

> **Before:** Help Ivan to calculate this number x!

> **After:** Find the value of $x$ for the most even-handed achievable arrangement.

#### Clear prompt

````text
It's New Year's Eve soon, so Ivan decided it's high time he started setting the table. Ivan has bought two cakes and cut them into pieces: the first cake has been cut into a pieces, and the second one — into b pieces.

Ivan knows that there will be n people at the celebration (including himself), so Ivan has set n plates for the cakes. Now he is thinking about how to distribute the cakes between the plates. Ivan wants to do it in such a way that all following conditions are met:  Each piece of each cake is put on some plate;  Each plate contains at least one piece of cake;  No plate contains pieces of both cakes. 

To make his guests happy, Ivan wants to distribute the cakes in such a way that the minimum number of pieces on the plate is maximized. Formally, Ivan wants to know the maximum possible number x such that he can distribute the cakes according to the aforementioned conditions, and each plate will contain at least x pieces of cake.

Help Ivan to calculate this number x!


-----Input-----

The first line contains three integers n, a and b (1 ≤ a, b ≤ 100, 2 ≤ n ≤ a + b) — the number of plates, the number of pieces of the first cake, and the number of pieces of the second cake, respectively.


-----Output-----

Print the maximum possible number x such that Ivan can distribute the cake in such a way that each plate will contain at least x pieces of cake.


-----Examples-----
Input
5 2 3

Output
1

Input
4 7 10

Output
3



-----Note-----

In the first example there is only one way to distribute cakes to plates, all of them will have 1 cake on it.

In the second example you can have two plates with 3 and 4 pieces of the first cake and two plates both with 5 pieces of the second cake. Minimal number of pieces is 3.
````

#### Less-explicit prompt

````text
It's New Year's Eve soon, so Ivan decided it's high time he started setting the table. Ivan has bought two cakes and cut them into pieces: the first cake has been cut into a pieces, and the second one — into b pieces.

Ivan knows that there will be n people at the celebration (including himself), so Ivan has set n plates for the cakes. Now he is thinking about how to distribute the cakes between the plates. Ivan wants to do it in such a way that all following conditions are met:  Each piece of each cake is put on some plate;  Each plate contains at least one piece of cake;  No plate contains pieces of both cakes. 

Among distributions following those rules, Ivan prefers to make the least-served plate as well supplied as possible. Call the number of pieces guaranteed on every plate in the best distribution $x$.

Find the value of $x$ for the most even-handed achievable arrangement.


-----Input-----

The first line contains three integers n, a and b (1 ≤ a, b ≤ 100, 2 ≤ n ≤ a + b) — the number of plates, the number of pieces of the first cake, and the number of pieces of the second cake, respectively.


-----Output-----

Print the maximum possible number x such that Ivan can distribute the cake in such a way that each plate will contain at least x pieces of cake.


-----Examples-----
Input
5 2 3

Output
1

Input
4 7 10

Output
3



-----Note-----

In the first example there is only one way to distribute cakes to plates, all of them will have 1 cake on it.

In the second example you can have two plates with 3 and 4 pieces of the first cake and two plates both with 5 pieces of the second cake. Minimal number of pieces is 3.
````

---

### interview — ID 35

**Source:** https://codeforces.com/problemset/problem/837/B
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You are given a field n × m, consisting of characters 'R', 'G' and 'B'. Output "YES" (without quotes) if this field corresponds to correct flag of Berland. Otherwise, print "NO" (without quotes).

> **After:** Given an $n \times m$ field of 'R', 'G', and 'B' characters, decide whether the arrangement fits the flag pattern just described.

#### Clear prompt

````text
The flag of Berland is such rectangular field n × m that satisfies following conditions:

  Flag consists of three colors which correspond to letters 'R', 'G' and 'B'.  Flag consists of three equal in width and height stripes, parralel to each other and to sides of the flag. Each stripe has exactly one color.  Each color should be used in exactly one stripe. 

You are given a field n × m, consisting of characters 'R', 'G' and 'B'. Output "YES" (without quotes) if this field corresponds to correct flag of Berland. Otherwise, print "NO" (without quotes).


-----Input-----

The first line contains two integer numbers n and m (1 ≤ n, m ≤ 100) — the sizes of the field.

Each of the following n lines consisting of m characters 'R', 'G' and 'B' — the description of the field.


-----Output-----

Print "YES" (without quotes) if the given field corresponds to correct flag of Berland . Otherwise, print "NO" (without quotes).


-----Examples-----
Input
6 5
RRRRR
RRRRR
BBBBB
BBBBB
GGGGG
GGGGG

Output
YES

Input
4 3
BRG
BRG
BRG
BRG

Output
YES

Input
6 7
RRRGGGG
RRRGGGG
RRRGGGG
RRRBBBB
RRRBBBB
RRRBBBB

Output
NO

Input
4 4
RRRR
RRRR
BBBB
GGGG

Output
NO



-----Note-----

The field in the third example doesn't have three parralel stripes.

Rows of the field in the fourth example are parralel to each other and to borders. But they have different heights — 2, 1 and 1.
````

#### Less-explicit prompt

````text
The flag of Berland is such rectangular field n × m that satisfies following conditions:

  Flag consists of three colors which correspond to letters 'R', 'G' and 'B'.  Flag consists of three equal in width and height stripes, parralel to each other and to sides of the flag. Each stripe has exactly one color.  Each color should be used in exactly one stripe. 

Given an $n \times m$ field of 'R', 'G', and 'B' characters, decide whether the arrangement fits the flag pattern just described.


-----Input-----

The first line contains two integer numbers n and m (1 ≤ n, m ≤ 100) — the sizes of the field.

Each of the following n lines consisting of m characters 'R', 'G' and 'B' — the description of the field.


-----Output-----

Print "YES" (without quotes) if the given field corresponds to correct flag of Berland . Otherwise, print "NO" (without quotes).


-----Examples-----
Input
6 5
RRRRR
RRRRR
BBBBB
BBBBB
GGGGG
GGGGG

Output
YES

Input
4 3
BRG
BRG
BRG
BRG

Output
YES

Input
6 7
RRRGGGG
RRRGGGG
RRRGGGG
RRRBBBB
RRRBBBB
RRRBBBB

Output
NO

Input
4 4
RRRR
RRRR
BBBB
GGGG

Output
NO



-----Note-----

The field in the third example doesn't have three parralel stripes.

Rows of the field in the fourth example are parralel to each other and to borders. But they have different heights — 2, 1 and 1.
````

---

### interview — ID 36

**Source:** https://codeforces.com/problemset/problem/615/E
**Review status:** `candidate_requires_human_review`

**Source and design flags:**

- IMAGE-BASED SOURCE: canonical Codeforces statement relies on diagram(s); Clear here is a documented text-only reconstruction, NOT byte-for-byte original.
- BENCHMARK CAUTION: changing image-based problems to text-based statements may affect difficulty; consider excluding from strictly original-statement analyses or report separately.

**Original source figure(s) (not part of model prompts):**

- https://espresso.codeforces.com/3b2337e9f4aadba64c4f33339db20ad466e772b7.png
- https://espresso.codeforces.com/5662ae948778adbfe5476af10bd0c1c576d7afb1.png

**Reconstruction check:** 135/135 supplied test pairs match.

**Exact original question as supplied by source dataset (retained in JSON as `source_clear_original`):**

````text
Ayrat is looking for the perfect code. He decided to start his search from an infinite field tiled by hexagons. For convenience the coordinate system is introduced, take a look at the picture to see how the coordinates of hexagon are defined: 

[Image] [Image] Ayrat is searching through the field. He started at point (0, 0) and is moving along the spiral (see second picture). Sometimes he forgets where he is now. Help Ayrat determine his location after n moves.


-----Input-----

The only line of the input contains integer n (0 ≤ n ≤ 10^18) — the number of Ayrat's moves.


-----Output-----

Print two integers x and y — current coordinates of Ayrat coordinates.


-----Examples-----
Input
3

Output
-2 0

Input
7

Output
3 2
````

#### Change log (not part of either model prompt)

1. **shared_technical_reconstruction**

> **Before:** Original Codeforces figure(s), absent from source JSON

> **After:** Ayrat walks on an infinite hexagonal tiling. The center of his starting hexagon is labeled $(0,0)$. The six neighbors of any hexagon $(x,y)$ have coordinate offsets $(1,2)$, $(-1,2)$, $(-2,0)$, $(-1,-2)$, $(1,-2)$ and $(2,0)$.
> 
> His route is an outward spiral through complete hexagonal rings. Ring $k$ contains the $6k$ hexagons at hex-grid distance $k$ from the origin, and rings are visited in increasing order $k=1,2,\ldots$. After ring $k-1$ (or the origin when $k=1$), he is at $(2(k-1),0)$. He enters ring $k$ at $(2k-1,2)$, then walks counterclockwise through all the hexagons in that ring exactly once, finishing at $(2k,0)$. Every move is to one neighboring hexagon. In particular, the first six positions after leaving $(0,0)$ are $(1,2)$, $(-1,2)$, $(-2,0)$, $(-1,-2)$, $(1,-2)$, and $(2,0)$.

2. **objective**

> **Before:** Given $n$ moves, determine the exact coordinates $(x,y)$ occupied after those $n$ moves. At $n=0$ the position is $(0,0)$.

> **After:** Ayrat has lost track of the labeled hexagon associated with his progress along this route. For the supplied move count, provide the corresponding position; the starting position counts as zero moves.

#### Clear prompt

````text
Ayrat walks on an infinite hexagonal tiling. The center of his starting hexagon is labeled $(0,0)$. The six neighbors of any hexagon $(x,y)$ have coordinate offsets $(1,2)$, $(-1,2)$, $(-2,0)$, $(-1,-2)$, $(1,-2)$ and $(2,0)$.

His route is an outward spiral through complete hexagonal rings. Ring $k$ contains the $6k$ hexagons at hex-grid distance $k$ from the origin, and rings are visited in increasing order $k=1,2,\ldots$. After ring $k-1$ (or the origin when $k=1$), he is at $(2(k-1),0)$. He enters ring $k$ at $(2k-1,2)$, then walks counterclockwise through all the hexagons in that ring exactly once, finishing at $(2k,0)$. Every move is to one neighboring hexagon. In particular, the first six positions after leaving $(0,0)$ are $(1,2)$, $(-1,2)$, $(-2,0)$, $(-1,-2)$, $(1,-2)$, and $(2,0)$.

Given $n$ moves, determine the exact coordinates $(x,y)$ occupied after those $n$ moves. At $n=0$ the position is $(0,0)$.

-----Input-----

The only line of the input contains integer n (0 ≤ n ≤ 10^18) — the number of Ayrat's moves.


-----Output-----

Print two integers x and y — current coordinates of Ayrat coordinates.


-----Examples-----
Input
3

Output
-2 0

Input
7

Output
3 2
````

#### Less-explicit prompt

````text
Ayrat walks on an infinite hexagonal tiling. The center of his starting hexagon is labeled $(0,0)$. The six neighbors of any hexagon $(x,y)$ have coordinate offsets $(1,2)$, $(-1,2)$, $(-2,0)$, $(-1,-2)$, $(1,-2)$ and $(2,0)$.

His route is an outward spiral through complete hexagonal rings. Ring $k$ contains the $6k$ hexagons at hex-grid distance $k$ from the origin, and rings are visited in increasing order $k=1,2,\ldots$. After ring $k-1$ (or the origin when $k=1$), he is at $(2(k-1),0)$. He enters ring $k$ at $(2k-1,2)$, then walks counterclockwise through all the hexagons in that ring exactly once, finishing at $(2k,0)$. Every move is to one neighboring hexagon. In particular, the first six positions after leaving $(0,0)$ are $(1,2)$, $(-1,2)$, $(-2,0)$, $(-1,-2)$, $(1,-2)$, and $(2,0)$.

Ayrat has lost track of the labeled hexagon associated with his progress along this route. For the supplied move count, provide the corresponding position; the starting position counts as zero moves.

-----Input-----

The only line of the input contains integer n (0 ≤ n ≤ 10^18) — the number of Ayrat's moves.


-----Output-----

Print two integers x and y — current coordinates of Ayrat coordinates.


-----Examples-----
Input
3

Output
-2 0

Input
7

Output
3 2
````

---

### interview — ID 37

**Source:** https://codeforces.com/problemset/problem/633/A
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** In order to break the shield Dante has to deal exactly c units of damage. Find out if this is possible.

> **After:** The shield requires a total of exactly $c$ damage, neither more nor less. Determine whether some combination of the available shots achieves that total.

#### Clear prompt

````text
Dante is engaged in a fight with "The Savior". Before he can fight it with his sword, he needs to break its shields. He has two guns, Ebony and Ivory, each of them is able to perform any non-negative number of shots.

For every bullet that hits the shield, Ebony deals a units of damage while Ivory deals b units of damage. In order to break the shield Dante has to deal exactly c units of damage. Find out if this is possible.


-----Input-----

The first line of the input contains three integers a, b, c (1 ≤ a, b ≤ 100, 1 ≤ c ≤ 10 000) — the number of units of damage dealt by Ebony gun and Ivory gun, and the total number of damage required to break the shield, respectively.


-----Output-----

Print "Yes" (without quotes) if Dante can deal exactly c damage to the shield and "No" (without quotes) otherwise.


-----Examples-----
Input
4 6 15

Output
No

Input
3 2 7

Output
Yes

Input
6 11 6

Output
Yes



-----Note-----

In the second sample, Dante can fire 1 bullet from Ebony and 2 from Ivory to deal exactly 1·3 + 2·2 = 7 damage. In the third sample, Dante can fire 1 bullet from ebony and no bullets from ivory to do 1·6 + 0·11 = 6 damage.
````

#### Less-explicit prompt

````text
Dante is engaged in a fight with "The Savior". Before he can fight it with his sword, he needs to break its shields. He has two guns, Ebony and Ivory, each of them is able to perform any non-negative number of shots.

For every bullet that hits the shield, Ebony deals a units of damage while Ivory deals b units of damage. The shield requires a total of exactly $c$ damage, neither more nor less. Determine whether some combination of the available shots achieves that total.


-----Input-----

The first line of the input contains three integers a, b, c (1 ≤ a, b ≤ 100, 1 ≤ c ≤ 10 000) — the number of units of damage dealt by Ebony gun and Ivory gun, and the total number of damage required to break the shield, respectively.


-----Output-----

Print "Yes" (without quotes) if Dante can deal exactly c damage to the shield and "No" (without quotes) otherwise.


-----Examples-----
Input
4 6 15

Output
No

Input
3 2 7

Output
Yes

Input
6 11 6

Output
Yes



-----Note-----

In the second sample, Dante can fire 1 bullet from Ebony and 2 from Ivory to deal exactly 1·3 + 2·2 = 7 damage. In the third sample, Dante can fire 1 bullet from ebony and no bullets from ivory to do 1·6 + 0·11 = 6 damage.
````

---

### interview — ID 38

**Source:** https://codeforces.com/problemset/problem/761/B
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Write the program which will check that Kefa's and Sasha's tracks coincide (it means that one can be obtained from the other by changing the start position). Note that they always run the track in one direction — counterclockwise, if you look on a track from above.

> **After:** Decide whether the recorded barrier distances might describe the same circular arrangement viewed from different integral starting points, without reversing the running direction (counterclockwise).

#### Clear prompt

````text
Running with barriers on the circle track is very popular in the country where Dasha lives, so no wonder that on her way to classes she saw the following situation:

The track is the circle with length L, in distinct points of which there are n barriers. Athlete always run the track in counterclockwise direction if you look on him from above. All barriers are located at integer distance from each other along the track. 

Her friends the parrot Kefa and the leopard Sasha participated in competitions and each of them ran one lap. Each of the friends started from some integral point on the track. Both friends wrote the distance from their start along the track to each of the n barriers. Thus, each of them wrote n integers in the ascending order, each of them was between 0 and L - 1, inclusively. [Image] Consider an example. Let L = 8, blue points are barriers, and green points are Kefa's start (A) and Sasha's start (B). Then Kefa writes down the sequence [2, 4, 6], and Sasha writes down [1, 5, 7]. 

There are several tracks in the country, all of them have same length and same number of barriers, but the positions of the barriers can differ among different tracks. Now Dasha is interested if it is possible that Kefa and Sasha ran the same track or they participated on different tracks. 

Write the program which will check that Kefa's and Sasha's tracks coincide (it means that one can be obtained from the other by changing the start position). Note that they always run the track in one direction — counterclockwise, if you look on a track from above. 


-----Input-----

The first line contains two integers n and L (1 ≤ n ≤ 50, n ≤ L ≤ 100) — the number of barriers on a track and its length. 

The second line contains n distinct integers in the ascending order — the distance from Kefa's start to each barrier in the order of its appearance. All integers are in the range from 0 to L - 1 inclusively.

The second line contains n distinct integers in the ascending order — the distance from Sasha's start to each barrier in the order of its overcoming. All integers are in the range from 0 to L - 1 inclusively.


-----Output-----

Print "YES" (without quotes), if Kefa and Sasha ran the coinciding tracks (it means that the position of all barriers coincides, if they start running from the same points on the track). Otherwise print "NO" (without quotes).


-----Examples-----
Input
3 8
2 4 6
1 5 7

Output
YES

Input
4 9
2 3 5 8
0 1 3 6

Output
YES

Input
2 4
1 3
1 2

Output
NO



-----Note-----

The first test is analyzed in the statement.
````

#### Less-explicit prompt

````text
Running with barriers on the circle track is very popular in the country where Dasha lives, so no wonder that on her way to classes she saw the following situation:

The track is the circle with length L, in distinct points of which there are n barriers. Athlete always run the track in counterclockwise direction if you look on him from above. All barriers are located at integer distance from each other along the track. 

Her friends the parrot Kefa and the leopard Sasha participated in competitions and each of them ran one lap. Each of the friends started from some integral point on the track. Both friends wrote the distance from their start along the track to each of the n barriers. Thus, each of them wrote n integers in the ascending order, each of them was between 0 and L - 1, inclusively. [Image] Consider an example. Let L = 8, blue points are barriers, and green points are Kefa's start (A) and Sasha's start (B). Then Kefa writes down the sequence [2, 4, 6], and Sasha writes down [1, 5, 7]. 

There are several tracks in the country, all of them have same length and same number of barriers, but the positions of the barriers can differ among different tracks. Now Dasha is interested if it is possible that Kefa and Sasha ran the same track or they participated on different tracks. 

Decide whether the recorded barrier distances might describe the same circular arrangement viewed from different integral starting points, without reversing the running direction (counterclockwise). 


-----Input-----

The first line contains two integers n and L (1 ≤ n ≤ 50, n ≤ L ≤ 100) — the number of barriers on a track and its length. 

The second line contains n distinct integers in the ascending order — the distance from Kefa's start to each barrier in the order of its appearance. All integers are in the range from 0 to L - 1 inclusively.

The second line contains n distinct integers in the ascending order — the distance from Sasha's start to each barrier in the order of its overcoming. All integers are in the range from 0 to L - 1 inclusively.


-----Output-----

Print "YES" (without quotes), if Kefa and Sasha ran the coinciding tracks (it means that the position of all barriers coincides, if they start running from the same points on the track). Otherwise print "NO" (without quotes).


-----Examples-----
Input
3 8
2 4 6
1 5 7

Output
YES

Input
4 9
2 3 5 8
0 1 3 6

Output
YES

Input
2 4
1 3
1 2

Output
NO



-----Note-----

The first test is analyzed in the statement.
````

---

### interview — ID 39

**Source:** https://codeforces.com/problemset/problem/981/A
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Namely, each word $s$ is changed into its longest substring that is not a palindrome. If all the substrings of $s$ are palindromes, she skips the word at all.

> **After:** For each word $s$, Ann keeps a contiguous part that is not a palindrome and prefers one of greatest possible length. If no such part exists, she skips the word.

2. **body**

> **Before:** Some time ago Ann read the word $s$. What is the word she changed it into?

> **After:** Consider what results from applying Ann’s preference to the supplied word.

#### Clear prompt

````text
A string is a palindrome if it reads the same from the left to the right and from the right to the left. For example, the strings "kek", "abacaba", "r" and "papicipap" are palindromes, while the strings "abb" and "iq" are not.

A substring $s[l \ldots r]$ ($1 \leq l \leq r \leq |s|$) of a string $s = s_{1}s_{2} \ldots s_{|s|}$ is the string $s_{l}s_{l + 1} \ldots s_{r}$.

Anna does not like palindromes, so she makes her friends call her Ann. She also changes all the words she reads in a similar way. Namely, each word $s$ is changed into its longest substring that is not a palindrome. If all the substrings of $s$ are palindromes, she skips the word at all.

Some time ago Ann read the word $s$. What is the word she changed it into?


-----Input-----

The first line contains a non-empty string $s$ with length at most $50$ characters, containing lowercase English letters only.


-----Output-----

If there is such a substring in $s$ that is not a palindrome, print the maximum length of such a substring. Otherwise print $0$.

Note that there can be multiple longest substrings that are not palindromes, but their length is unique.


-----Examples-----
Input
mew

Output
3

Input
wuffuw

Output
5

Input
qqqqqqqq

Output
0



-----Note-----

"mew" is not a palindrome, so the longest substring of it that is not a palindrome, is the string "mew" itself. Thus, the answer for the first example is $3$.

The string "uffuw" is one of the longest non-palindrome substrings (of length $5$) of the string "wuffuw", so the answer for the second example is $5$.

All substrings of the string "qqqqqqqq" consist of equal characters so they are palindromes. This way, there are no non-palindrome substrings. Thus, the answer for the third example is $0$.
````

#### Less-explicit prompt

````text
A string is a palindrome if it reads the same from the left to the right and from the right to the left. For example, the strings "kek", "abacaba", "r" and "papicipap" are palindromes, while the strings "abb" and "iq" are not.

A substring $s[l \ldots r]$ ($1 \leq l \leq r \leq |s|$) of a string $s = s_{1}s_{2} \ldots s_{|s|}$ is the string $s_{l}s_{l + 1} \ldots s_{r}$.

Anna does not like palindromes, so she makes her friends call her Ann. She also changes all the words she reads in a similar way. For each word $s$, Ann keeps a contiguous part that is not a palindrome and prefers one of greatest possible length. If no such part exists, she skips the word.

Consider what results from applying Ann’s preference to the supplied word.


-----Input-----

The first line contains a non-empty string $s$ with length at most $50$ characters, containing lowercase English letters only.


-----Output-----

If there is such a substring in $s$ that is not a palindrome, print the maximum length of such a substring. Otherwise print $0$.

Note that there can be multiple longest substrings that are not palindromes, but their length is unique.


-----Examples-----
Input
mew

Output
3

Input
wuffuw

Output
5

Input
qqqqqqqq

Output
0



-----Note-----

"mew" is not a palindrome, so the longest substring of it that is not a palindrome, is the string "mew" itself. Thus, the answer for the first example is $3$.

The string "uffuw" is one of the longest non-palindrome substrings (of length $5$) of the string "wuffuw", so the answer for the second example is $5$.

All substrings of the string "qqqqqqqq" consist of equal characters so they are palindromes. This way, there are no non-palindrome substrings. Thus, the answer for the third example is $0$.
````

---

### interview — ID 40

**Source:** https://codeforces.com/problemset/problem/807/A
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Determine if the current round is rated, unrated, or it's impossible to determine whether it is rated of not.

> **After:** Based only on the given rules and standings, classify what can actually be concluded about this round’s rating status; do not assume any other rating-system behavior.

#### Clear prompt

````text
Is it rated?

Here it is. The Ultimate Question of Competitive Programming, Codeforces, and Everything. And you are here to answer it.

Another Codeforces round has been conducted. No two participants have the same number of points. For each participant, from the top to the bottom of the standings, their rating before and after the round is known.

It's known that if at least one participant's rating has changed, then the round was rated for sure.

It's also known that if the round was rated and a participant with lower rating took a better place in the standings than a participant with higher rating, then at least one round participant's rating has changed.

In this problem, you should not make any other assumptions about the rating system.

Determine if the current round is rated, unrated, or it's impossible to determine whether it is rated of not.


-----Input-----

The first line contains a single integer n (2 ≤ n ≤ 1000) — the number of round participants.

Each of the next n lines contains two integers a_{i} and b_{i} (1 ≤ a_{i}, b_{i} ≤ 4126) — the rating of the i-th participant before and after the round, respectively. The participants are listed in order from the top to the bottom of the standings.


-----Output-----

If the round is rated for sure, print "rated". If the round is unrated for sure, print "unrated". If it's impossible to determine whether the round is rated or not, print "maybe".


-----Examples-----
Input
6
3060 3060
2194 2194
2876 2903
2624 2624
3007 2991
2884 2884

Output
rated

Input
4
1500 1500
1300 1300
1200 1200
1400 1400

Output
unrated

Input
5
3123 3123
2777 2777
2246 2246
2246 2246
1699 1699

Output
maybe



-----Note-----

In the first example, the ratings of the participants in the third and fifth places have changed, therefore, the round was rated.

In the second example, no one's rating has changed, but the participant in the second place has lower rating than the participant in the fourth place. Therefore, if the round was rated, someone's rating would've changed for sure.

In the third example, no one's rating has changed, and the participants took places in non-increasing order of their rating. Therefore, it's impossible to determine whether the round is rated or not.
````

#### Less-explicit prompt

````text
Is it rated?

Here it is. The Ultimate Question of Competitive Programming, Codeforces, and Everything. And you are here to answer it.

Another Codeforces round has been conducted. No two participants have the same number of points. For each participant, from the top to the bottom of the standings, their rating before and after the round is known.

It's known that if at least one participant's rating has changed, then the round was rated for sure.

It's also known that if the round was rated and a participant with lower rating took a better place in the standings than a participant with higher rating, then at least one round participant's rating has changed.

In this problem, you should not make any other assumptions about the rating system.

Based only on the given rules and standings, classify what can actually be concluded about this round’s rating status; do not assume any other rating-system behavior.


-----Input-----

The first line contains a single integer n (2 ≤ n ≤ 1000) — the number of round participants.

Each of the next n lines contains two integers a_{i} and b_{i} (1 ≤ a_{i}, b_{i} ≤ 4126) — the rating of the i-th participant before and after the round, respectively. The participants are listed in order from the top to the bottom of the standings.


-----Output-----

If the round is rated for sure, print "rated". If the round is unrated for sure, print "unrated". If it's impossible to determine whether the round is rated or not, print "maybe".


-----Examples-----
Input
6
3060 3060
2194 2194
2876 2903
2624 2624
3007 2991
2884 2884

Output
rated

Input
4
1500 1500
1300 1300
1200 1200
1400 1400

Output
unrated

Input
5
3123 3123
2777 2777
2246 2246
2246 2246
1699 1699

Output
maybe



-----Note-----

In the first example, the ratings of the participants in the third and fifth places have changed, therefore, the round was rated.

In the second example, no one's rating has changed, but the participant in the second place has lower rating than the participant in the fourth place. Therefore, if the round was rated, someone's rating would've changed for sure.

In the third example, no one's rating has changed, and the participants took places in non-increasing order of their rating. Therefore, it's impossible to determine whether the round is rated or not.
````

---

### interview — ID 41

**Source:** https://codeforces.com/problemset/problem/803/B
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** For each element find the distance to the nearest zero (to the element which equals to zero).

> **After:** For each position, consider how close it lies to any occurrence of zero in the array, measured in index steps; use the closest occurrence.

#### Clear prompt

````text
You are given the array of integer numbers a_0, a_1, ..., a_{n} - 1. For each element find the distance to the nearest zero (to the element which equals to zero). There is at least one zero element in the given array.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 2·10^5) — length of the array a. The second line contains integer elements of the array separated by single spaces ( - 10^9 ≤ a_{i} ≤ 10^9).


-----Output-----

Print the sequence d_0, d_1, ..., d_{n} - 1, where d_{i} is the difference of indices between i and nearest j such that a_{j} = 0. It is possible that i = j.


-----Examples-----
Input
9
2 1 0 3 0 0 3 2 4

Output
2 1 0 1 0 0 1 2 3 
Input
5
0 1 2 3 4

Output
0 1 2 3 4 
Input
7
5 6 0 1 -2 3 4

Output
2 1 0 1 2 3 4
````

#### Less-explicit prompt

````text
You are given the array of integer numbers a_0, a_1, ..., a_{n} - 1. For each position, consider how close it lies to any occurrence of zero in the array, measured in index steps; use the closest occurrence. There is at least one zero element in the given array.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 2·10^5) — length of the array a. The second line contains integer elements of the array separated by single spaces ( - 10^9 ≤ a_{i} ≤ 10^9).


-----Output-----

Print the sequence d_0, d_1, ..., d_{n} - 1, where d_{i} is the difference of indices between i and nearest j such that a_{j} = 0. It is possible that i = j.


-----Examples-----
Input
9
2 1 0 3 0 0 3 2 4

Output
2 1 0 1 0 0 1 2 3 
Input
5
0 1 2 3 4

Output
0 1 2 3 4 
Input
7
5 6 0 1 -2 3 4

Output
2 1 0 1 2 3 4
````

---

### interview — ID 42

**Source:** https://codeforces.com/problemset/problem/1038/F
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Find the number of distinct cyclical binary strings of length $n$ which contain $s$ as a substring.

> **After:** Consider all length-$n$ binary strings interpreted cyclically under the definition below. Determine how many contain the given $s$.

#### Clear prompt

````text
You are given a binary string $s$.

Find the number of distinct cyclical binary strings of length $n$ which contain $s$ as a substring.

The cyclical string $t$ contains $s$ as a substring if there is some cyclical shift of string $t$, such that $s$ is a substring of this cyclical shift of $t$.

For example, the cyclical string "000111" contains substrings "001", "01110" and "10", but doesn't contain "0110" and "10110".

Two cyclical strings are called different if they differ from each other as strings. For example, two different strings, which differ from each other by a cyclical shift, are still considered different cyclical strings.


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 40$) — the length of the target string $t$.

The next line contains the string $s$ ($1 \le |s| \le n$) — the string which must be a substring of cyclical string $t$. String $s$ contains only characters '0' and '1'.


-----Output-----

Print the only integer — the number of distinct cyclical binary strings $t$, which contain $s$ as a substring.


-----Examples-----
Input
2
0

Output
3
Input
4
1010

Output
2
Input
20
10101010101010

Output
962


-----Note-----

In the first example, there are three cyclical strings, which contain "0" — "00", "01" and "10".

In the second example, there are only two such strings — "1010", "0101".
````

#### Less-explicit prompt

````text
You are given a binary string $s$.

Consider all length-$n$ binary strings interpreted cyclically under the definition below. Determine how many contain the given $s$.

The cyclical string $t$ contains $s$ as a substring if there is some cyclical shift of string $t$, such that $s$ is a substring of this cyclical shift of $t$.

For example, the cyclical string "000111" contains substrings "001", "01110" and "10", but doesn't contain "0110" and "10110".

Two cyclical strings are called different if they differ from each other as strings. For example, two different strings, which differ from each other by a cyclical shift, are still considered different cyclical strings.


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 40$) — the length of the target string $t$.

The next line contains the string $s$ ($1 \le |s| \le n$) — the string which must be a substring of cyclical string $t$. String $s$ contains only characters '0' and '1'.


-----Output-----

Print the only integer — the number of distinct cyclical binary strings $t$, which contain $s$ as a substring.


-----Examples-----
Input
2
0

Output
3
Input
4
1010

Output
2
Input
20
10101010101010

Output
962


-----Note-----

In the first example, there are three cyclical strings, which contain "0" — "00", "01" and "10".

In the second example, there are only two such strings — "1010", "0101".
````

---

### interview — ID 43

**Source:** https://codeforces.com/problemset/problem/598/C
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Your task is to find a pair of vectors with the minimal non-oriented angle between them.

> **After:** Among the available pairs, identify two whose directions are closest in the non-oriented angular sense defined below.

#### Clear prompt

````text
You are given the set of vectors on the plane, each of them starting at the origin. Your task is to find a pair of vectors with the minimal non-oriented angle between them.

Non-oriented angle is non-negative value, minimal between clockwise and counterclockwise direction angles. Non-oriented angle is always between 0 and π. For example, opposite directions vectors have angle equals to π.


-----Input-----

First line of the input contains a single integer n (2 ≤ n ≤ 100 000) — the number of vectors.

The i-th of the following n lines contains two integers x_{i} and y_{i} (|x|, |y| ≤ 10 000, x^2 + y^2 > 0) — the coordinates of the i-th vector. Vectors are numbered from 1 to n in order of appearing in the input. It is guaranteed that no two vectors in the input share the same direction (but they still can have opposite directions).


-----Output-----

Print two integer numbers a and b (a ≠ b) — a pair of indices of vectors with the minimal non-oriented angle. You can print the numbers in any order. If there are many possible answers, print any.


-----Examples-----
Input
4
-1 0
0 -1
1 0
1 1

Output
3 4

Input
6
-1 0
0 -1
1 0
1 1
-4 -5
-4 -6

Output
6 5
````

#### Less-explicit prompt

````text
You are given the set of vectors on the plane, each of them starting at the origin. Among the available pairs, identify two whose directions are closest in the non-oriented angular sense defined below.

Non-oriented angle is non-negative value, minimal between clockwise and counterclockwise direction angles. Non-oriented angle is always between 0 and π. For example, opposite directions vectors have angle equals to π.


-----Input-----

First line of the input contains a single integer n (2 ≤ n ≤ 100 000) — the number of vectors.

The i-th of the following n lines contains two integers x_{i} and y_{i} (|x|, |y| ≤ 10 000, x^2 + y^2 > 0) — the coordinates of the i-th vector. Vectors are numbered from 1 to n in order of appearing in the input. It is guaranteed that no two vectors in the input share the same direction (but they still can have opposite directions).


-----Output-----

Print two integer numbers a and b (a ≠ b) — a pair of indices of vectors with the minimal non-oriented angle. You can print the numbers in any order. If there are many possible answers, print any.


-----Examples-----
Input
4
-1 0
0 -1
1 0
1 1

Output
3 4

Input
6
-1 0
0 -1
1 0
1 1
-4 -5
-4 -6

Output
6 5
````

---

### interview — ID 44

**Source:** https://codeforces.com/problemset/problem/702/D
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Your task is to find minimal time after which Vasiliy will be able to reach the post office. Consider that in every moment of time Vasiliy can left his car and start to go on foot.

> **After:** Vasiliy can abandon the car and continue on foot at any point. Work out how soon he can arrive if he chooses his travel and repair decisions favorably.

#### Clear prompt

````text
Vasiliy has a car and he wants to get from home to the post office. The distance which he needs to pass equals to d kilometers.

Vasiliy's car is not new — it breaks after driven every k kilometers and Vasiliy needs t seconds to repair it. After repairing his car Vasiliy can drive again (but after k kilometers it will break again, and so on). In the beginning of the trip the car is just from repair station.

To drive one kilometer on car Vasiliy spends a seconds, to walk one kilometer on foot he needs b seconds (a < b).

Your task is to find minimal time after which Vasiliy will be able to reach the post office. Consider that in every moment of time Vasiliy can left his car and start to go on foot.


-----Input-----

The first line contains 5 positive integers d, k, a, b, t (1 ≤ d ≤ 10^12; 1 ≤ k, a, b, t ≤ 10^6; a < b), where:  d — the distance from home to the post office;  k — the distance, which car is able to drive before breaking;  a — the time, which Vasiliy spends to drive 1 kilometer on his car;  b — the time, which Vasiliy spends to walk 1 kilometer on foot;  t — the time, which Vasiliy spends to repair his car. 


-----Output-----

Print the minimal time after which Vasiliy will be able to reach the post office.


-----Examples-----
Input
5 2 1 4 10

Output
14

Input
5 2 1 4 5

Output
13



-----Note-----

In the first example Vasiliy needs to drive the first 2 kilometers on the car (in 2 seconds) and then to walk on foot 3 kilometers (in 12 seconds). So the answer equals to 14 seconds.

In the second example Vasiliy needs to drive the first 2 kilometers on the car (in 2 seconds), then repair his car (in 5 seconds) and drive 2 kilometers more on the car (in 2 seconds). After that he needs to walk on foot 1 kilometer (in 4 seconds). So the answer equals to 13 seconds.
````

#### Less-explicit prompt

````text
Vasiliy has a car and he wants to get from home to the post office. The distance which he needs to pass equals to d kilometers.

Vasiliy's car is not new — it breaks after driven every k kilometers and Vasiliy needs t seconds to repair it. After repairing his car Vasiliy can drive again (but after k kilometers it will break again, and so on). In the beginning of the trip the car is just from repair station.

To drive one kilometer on car Vasiliy spends a seconds, to walk one kilometer on foot he needs b seconds (a < b).

Vasiliy can abandon the car and continue on foot at any point. Work out how soon he can arrive if he chooses his travel and repair decisions favorably.


-----Input-----

The first line contains 5 positive integers d, k, a, b, t (1 ≤ d ≤ 10^12; 1 ≤ k, a, b, t ≤ 10^6; a < b), where:  d — the distance from home to the post office;  k — the distance, which car is able to drive before breaking;  a — the time, which Vasiliy spends to drive 1 kilometer on his car;  b — the time, which Vasiliy spends to walk 1 kilometer on foot;  t — the time, which Vasiliy spends to repair his car. 


-----Output-----

Print the minimal time after which Vasiliy will be able to reach the post office.


-----Examples-----
Input
5 2 1 4 10

Output
14

Input
5 2 1 4 5

Output
13



-----Note-----

In the first example Vasiliy needs to drive the first 2 kilometers on the car (in 2 seconds) and then to walk on foot 3 kilometers (in 12 seconds). So the answer equals to 14 seconds.

In the second example Vasiliy needs to drive the first 2 kilometers on the car (in 2 seconds), then repair his car (in 5 seconds) and drive 2 kilometers more on the car (in 2 seconds). After that he needs to walk on foot 1 kilometer (in 4 seconds). So the answer equals to 13 seconds.
````

---

### competition — ID 3030

**Source:** https://open.kattis.com/problems/heapstrees
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You would like to turn this tree into a heap. That is, you would like to choose the largest possible subset of nodes that satisfy this Heap Property: For every node pair $i$,$j$ in the subset, if node $i$ is an ancestor of node $j$ in the tree, then $v_ i > v_ j$. Note that equality is not allowed.

> **After:** You are interested in retaining as many tree nodes as the following Heap Property permits: whenever a retained node $i$ is an ancestor of another retained node $j$, its value $v_i$ must be strictly greater than $v_j$; equality does not count.

2. **body**

> **Before:** Figure out the maximum number of nodes you can choose to form such a subset.

> **After:** Determine the size of the most extensive selection that respects this property.

#### Clear prompt

````text
You are given a rooted tree with $n$ nodes. The nodes are labeled $1$ to $n$, and node $1$ is the root. Each node has a value $v_ i$.

You would like to turn this tree into a heap. That is, you would like to choose the largest possible subset of nodes that satisfy this Heap Property: For every node pair $i$,$j$ in the subset, if node $i$ is an ancestor of node $j$ in the tree, then $v_ i > v_ j$. Note that equality is not allowed.

Figure out the maximum number of nodes you can choose to form such a subset. The subset does not have to form a subtree.

-----Input-----
Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. The first line of input will contain a single integer $n$ ($1 \le n \le 2 \cdot 10^5$), which is the number of nodes in the tree. The nodes are numbered $1$ to $n$.

Each of the next $n$ lines will describe the nodes, in order from $i=1$ to $n$. They will each contain two integers $v_ i$ and $p_ i$, where $v_ i$ ($0 \le v_ i \le 10^9$) is the value in the node, and $p_ i$ ($0 \le p_ i < i$) is the index of its parent. Every node’s index will be strictly greater than its parent node’s index. Only node 1, the root, will have $p_1=0$, since it has no parent. For all other nodes ($i=2, 3, \ldots , n$), $1 \le p_ i < i$.

-----Output-----
Output a single integer representing the number of nodes in the largest subset satisfying the Heap Property.

-----Examples-----
Sample Input 1:
5
3 0
3 1
3 2
3 3
3 4
Sample Output 1:
1

Sample Input 2:
5
4 0
3 1
2 2
1 3
0 4
Sample Output 2:
5

Sample Input 3:
6
3 0
1 1
2 1
3 1
4 1
5 1
Sample Output 3:
5
````

#### Less-explicit prompt

````text
You are given a rooted tree with $n$ nodes. The nodes are labeled $1$ to $n$, and node $1$ is the root. Each node has a value $v_ i$.

You are interested in retaining as many tree nodes as the following Heap Property permits: whenever a retained node $i$ is an ancestor of another retained node $j$, its value $v_i$ must be strictly greater than $v_j$; equality does not count.

Determine the size of the most extensive selection that respects this property. The subset does not have to form a subtree.

-----Input-----
Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. The first line of input will contain a single integer $n$ ($1 \le n \le 2 \cdot 10^5$), which is the number of nodes in the tree. The nodes are numbered $1$ to $n$.

Each of the next $n$ lines will describe the nodes, in order from $i=1$ to $n$. They will each contain two integers $v_ i$ and $p_ i$, where $v_ i$ ($0 \le v_ i \le 10^9$) is the value in the node, and $p_ i$ ($0 \le p_ i < i$) is the index of its parent. Every node’s index will be strictly greater than its parent node’s index. Only node 1, the root, will have $p_1=0$, since it has no parent. For all other nodes ($i=2, 3, \ldots , n$), $1 \le p_ i < i$.

-----Output-----
Output a single integer representing the number of nodes in the largest subset satisfying the Heap Property.

-----Examples-----
Sample Input 1:
5
3 0
3 1
3 2
3 3
3 4
Sample Output 1:
1

Sample Input 2:
5
4 0
3 1
2 2
1 3
0 4
Sample Output 2:
5

Sample Input 3:
6
3 0
1 1
2 1
3 1
4 1
5 1
Sample Output 3:
5
````

---

### competition — ID 3031

**Source:** https://open.kattis.com/problems/rainbowroads
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Find all the good nodes in the given tree.

> **After:** Identify which stations meet the definition of a good node under every path starting from them.

#### Clear prompt

````text
The Transit Authority of Greater Podunk is planning its holiday decorations. They want to create an illuminated display of their light rail map in which each stretch of track between stations can be illuminated in one of several colors. 

At periodic intervals, the controlling software will choose two stations at random and illuminate all of the segments connecting those two stations. By design, for any two stations on the Greater Podunk Railway, there is a unique path connecting the two.

For maximum color and cheer, the display designers want to avoid having two adjacent segments of track lighting up in the same color. They fear, however, that they may have lost track of this guideline in the process of building the display. One of them has gone so far as to propose a means of measuring just how far from that ideal they may have fallen.

-----Description-----
You are given a tree with $n$ nodes (stations), conveniently numbered from $1$ to $n$. Each edge in this tree has one of $n$ colors. A path in this tree is called a rainbow if all adjacent edges in the path have different colors. Also, a node is called good if every simple path with that node as one of its endpoints is a rainbow path. (A simple path is a path that does not repeat any vertex or edge.)

Find all the good nodes in the given tree.

-----Input-----
The first line of input contains a single integer $n$ ($1 \le n \le 50000$).

Each of the next $n-1$ lines contains three space-separated integers $a_ i$, $b_ i$, and $c_ i$ ($1 \le a_ i, b_ i, c_ i \le n$; $a_ i \ne b_ i$), describing an edge of color $c_ i$ that connects nodes $a_ i$ and $b_ i$.

It is guaranteed that the given edges form a tree.

-----Output-----
On the first line of the output, print $k$, the number of good nodes.

In the next $k$ lines, print the indices of all good nodes in numerical order, one per line.

-----Examples-----
(For the first sample, node $3$ is good because all paths that have node $3$ as an endpoint are rainbow. In particular, even though the path $3 \rightarrow 4 \rightarrow 5 \rightarrow 6$ has two edges of the same color (i.e. $3 \rightarrow 4$, $5 \rightarrow 6$), it is still rainbow because these edges are not adjacent.)

-----Examples-----
Sample Input 1:
8
1 3 1
2 3 1
3 4 3
4 5 4
5 6 3
6 7 2
6 8 2
Sample Output 1:
4
3
4
5
6

Sample Input 2:
8
1 2 2
1 3 1
2 4 3
2 7 1
3 5 2
5 6 2
7 8 1
Sample Output 2:
0

Sample Input 3:
9
1 2 2
1 3 1
1 4 5
1 5 5
2 6 3
3 7 3
4 8 1
5 9 2
Sample Output 3:
5
1
2
3
6
7
````

#### Less-explicit prompt

````text
The Transit Authority of Greater Podunk is planning its holiday decorations. They want to create an illuminated display of their light rail map in which each stretch of track between stations can be illuminated in one of several colors. 

At periodic intervals, the controlling software will choose two stations at random and illuminate all of the segments connecting those two stations. By design, for any two stations on the Greater Podunk Railway, there is a unique path connecting the two.

For maximum color and cheer, the display designers want to avoid having two adjacent segments of track lighting up in the same color. They fear, however, that they may have lost track of this guideline in the process of building the display. One of them has gone so far as to propose a means of measuring just how far from that ideal they may have fallen.

-----Description-----
You are given a tree with $n$ nodes (stations), conveniently numbered from $1$ to $n$. Each edge in this tree has one of $n$ colors. A path in this tree is called a rainbow if all adjacent edges in the path have different colors. Also, a node is called good if every simple path with that node as one of its endpoints is a rainbow path. (A simple path is a path that does not repeat any vertex or edge.)

Identify which stations meet the definition of a good node under every path starting from them.

-----Input-----
The first line of input contains a single integer $n$ ($1 \le n \le 50000$).

Each of the next $n-1$ lines contains three space-separated integers $a_ i$, $b_ i$, and $c_ i$ ($1 \le a_ i, b_ i, c_ i \le n$; $a_ i \ne b_ i$), describing an edge of color $c_ i$ that connects nodes $a_ i$ and $b_ i$.

It is guaranteed that the given edges form a tree.

-----Output-----
On the first line of the output, print $k$, the number of good nodes.

In the next $k$ lines, print the indices of all good nodes in numerical order, one per line.

-----Examples-----
(For the first sample, node $3$ is good because all paths that have node $3$ as an endpoint are rainbow. In particular, even though the path $3 \rightarrow 4 \rightarrow 5 \rightarrow 6$ has two edges of the same color (i.e. $3 \rightarrow 4$, $5 \rightarrow 6$), it is still rainbow because these edges are not adjacent.)

-----Examples-----
Sample Input 1:
8
1 3 1
2 3 1
3 4 3
4 5 4
5 6 3
6 7 2
6 8 2
Sample Output 1:
4
3
4
5
6

Sample Input 2:
8
1 2 2
1 3 1
2 4 3
2 7 1
3 5 2
5 6 2
7 8 1
Sample Output 2:
0

Sample Input 3:
9
1 2 2
1 3 1
1 4 5
1 5 5
2 6 3
3 7 3
4 8 1
5 9 2
Sample Output 3:
5
1
2
3
6
7
````

---

### competition — ID 3032

**Source:** https://open.kattis.com/problems/harvard
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Your problem is to determine the minimum running time of programs. In particular, given the number and size of the memory banks and a program to be executed, find the minimum number of instructions (which reference memory location and possibly set the BSR) that must be executed to run the program. To do this you must identify a mapping of variables to memory banks that yields the smallest execution time, and report that execution time – that is, the number of memory references and BSR register settings required.

> **After:** Variable-to-bank assignments determine how often the bank-selection register needs changing as the program executes. Consider assignments that make the resulting stream of memory references and required BSR settings as short as possible, and report the instruction count for the best assignment.

#### Clear prompt

````text
The term “Harvard architecture” applies to a computer that has physically separate memories for instructions and data. The term originated with the Harvard Mark I computer, delivered by IBM in 1944, which used paper tape for instructions and relays for data. 

Some modern microcontrollers use the Harvard architecture – but not paper tape and relays! Data memory is organized in banks, each containing the same number of data items. Each data-referencing instruction has a byte offset $f$ to a bank, and a bit $a$ that is used to select the bank to be referenced. If $a$ is $0$, then bank $0$ is referenced. If $a$ is $1$, then the value in a bank select register (BSR) identifies the bank to be used. Assume each instruction takes the same time to execute, and there is an instruction that can set the BSR’s value.

For example, suppose there are $4$ banks of $8$ bytes each. To access location $5$, either use a single instruction with $a = 0$ and $f = 5$, or set the BSR to $0$ in one instruction and then use an instruction with $a = 1$ and $f = 5$. The first approach is faster since it does not require setting the BSR.

Now suppose (with the same memory) the location to access is $20$. Only one approach will work here: execute an instruction that sets the BSR to $2$ (unless the BSR already has the value $2$) and then use an instruction with $a = 1$ and $f = 4$.

A program is a sequence of operations. Each operation is either
 - a variable reference, written as V$i$, where $i$ is a positive integer, or
 - a repetition, written as R$n$ <program> E, where $n$ is a positive integer and <program> is an arbitrary program. This operation is equivalent to $n$ sequential occurrences of <program>.

Your problem is to determine the minimum running time of programs. In particular, given the number and size of the memory banks and a program to be executed, find the minimum number of instructions (which reference memory location and possibly set the BSR) that must be executed to run the program. To do this you must identify a mapping of variables to memory banks that yields the smallest execution time, and report that execution time – that is, the number of memory references and BSR register settings required. The BSR’s value is initially undefined, and changes only when an instruction explicitly sets its value.




-----Input-----
The input consists of a single test case. A test case consists of two lines. The first line contains two integers $b$ and $s$, where $1 \le b \le 13$ is the number of memory banks and $1 \le s \le 13$ is the number of variables that can be stored in each memory bank. The second line contains a non-empty program with at most $1000$ space-separated elements (each R$n$, V$i$, and E counts as one element).

You may assume the following:
 - In a repetition R$n$, the number of repetitions satisfies $1 \le n \le 10^6$.
 - In a loop operation R$n$ <program> E, the loop body <program> is not empty.
 - In a variable reference V$i$, the variable index satisfies $1 \le i \le \min (b \cdot s, 13)$.
 - The total number of variable references performed by an execution of the program is at most $10^{12}$.

-----Output-----
Display the minimum number of instructions that must be executed to complete the program.

-----Examples-----
Sample Input 1:
1 2
V1 V2 V1 V1 V2
Sample Output 1:
5

Sample Input 2:
2 1
V1 V2 V1 V1 V2
Sample Output 2:
6

Sample Input 3:
1 2
R10 V1 V2 V1 E
Sample Output 3:
30
````

#### Less-explicit prompt

````text
The term “Harvard architecture” applies to a computer that has physically separate memories for instructions and data. The term originated with the Harvard Mark I computer, delivered by IBM in 1944, which used paper tape for instructions and relays for data. 

Some modern microcontrollers use the Harvard architecture – but not paper tape and relays! Data memory is organized in banks, each containing the same number of data items. Each data-referencing instruction has a byte offset $f$ to a bank, and a bit $a$ that is used to select the bank to be referenced. If $a$ is $0$, then bank $0$ is referenced. If $a$ is $1$, then the value in a bank select register (BSR) identifies the bank to be used. Assume each instruction takes the same time to execute, and there is an instruction that can set the BSR’s value.

For example, suppose there are $4$ banks of $8$ bytes each. To access location $5$, either use a single instruction with $a = 0$ and $f = 5$, or set the BSR to $0$ in one instruction and then use an instruction with $a = 1$ and $f = 5$. The first approach is faster since it does not require setting the BSR.

Now suppose (with the same memory) the location to access is $20$. Only one approach will work here: execute an instruction that sets the BSR to $2$ (unless the BSR already has the value $2$) and then use an instruction with $a = 1$ and $f = 4$.

A program is a sequence of operations. Each operation is either
 - a variable reference, written as V$i$, where $i$ is a positive integer, or
 - a repetition, written as R$n$ <program> E, where $n$ is a positive integer and <program> is an arbitrary program. This operation is equivalent to $n$ sequential occurrences of <program>.

Variable-to-bank assignments determine how often the bank-selection register needs changing as the program executes. Consider assignments that make the resulting stream of memory references and required BSR settings as short as possible, and report the instruction count for the best assignment. The BSR’s value is initially undefined, and changes only when an instruction explicitly sets its value.




-----Input-----
The input consists of a single test case. A test case consists of two lines. The first line contains two integers $b$ and $s$, where $1 \le b \le 13$ is the number of memory banks and $1 \le s \le 13$ is the number of variables that can be stored in each memory bank. The second line contains a non-empty program with at most $1000$ space-separated elements (each R$n$, V$i$, and E counts as one element).

You may assume the following:
 - In a repetition R$n$, the number of repetitions satisfies $1 \le n \le 10^6$.
 - In a loop operation R$n$ <program> E, the loop body <program> is not empty.
 - In a variable reference V$i$, the variable index satisfies $1 \le i \le \min (b \cdot s, 13)$.
 - The total number of variable references performed by an execution of the program is at most $10^{12}$.

-----Output-----
Display the minimum number of instructions that must be executed to complete the program.

-----Examples-----
Sample Input 1:
1 2
V1 V2 V1 V1 V2
Sample Output 1:
5

Sample Input 2:
2 1
V1 V2 V1 V1 V2
Sample Output 2:
6

Sample Input 3:
1 2
R10 V1 V2 V1 E
Sample Output 3:
30
````

---

### competition — ID 3033

**Source:** https://open.kattis.com/problems/multiplyingdigits
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** We want you to solve the reverse problem: given a base $B$ and a number $N$, what is the smallest positive integer $X$ such that $f_ B(X) = N$?

> **After:** Now work backward from a base $B$ and a digit product $N$. Consider positive integers $X$ having $f_B(X)=N$, with preference for the least such integer.

#### Clear prompt

````text
For every positive integer we may obtain a non-negative integer by multiplying its digits. This defines a function $f$, e.g. $f(38) = 24$.

This function gets more interesting if we allow for other bases. In base $3$, the number $80$ is written as $2222$, so: $f_3(80) = 16$.

We want you to solve the reverse problem: given a base $B$ and a number $N$, what is the smallest positive integer $X$ such that $f_ B(X) = N$?

-----Input-----
The input consists of a single line containing two integers $B$ and $N$, satisfying $2 < B \leq 10000$ and $0 < N < 2^{63}$.

-----Output-----
Output the smallest positive integer solution $X$ of the equation $f_ B(X) = N$. If no such $X$ exists, output the word “impossible”. The input is carefully chosen such that $X < 2^{63}$ holds (if $X$ exists).

-----Examples-----
Sample Input 1:
10 24
Sample Output 1:
38

Sample Input 2:
10 11
Sample Output 2:
impossible

Sample Input 3:
9 216
Sample Output 3:
546
````

#### Less-explicit prompt

````text
For every positive integer we may obtain a non-negative integer by multiplying its digits. This defines a function $f$, e.g. $f(38) = 24$.

This function gets more interesting if we allow for other bases. In base $3$, the number $80$ is written as $2222$, so: $f_3(80) = 16$.

Now work backward from a base $B$ and a digit product $N$. Consider positive integers $X$ having $f_B(X)=N$, with preference for the least such integer.

-----Input-----
The input consists of a single line containing two integers $B$ and $N$, satisfying $2 < B \leq 10000$ and $0 < N < 2^{63}$.

-----Output-----
Output the smallest positive integer solution $X$ of the equation $f_ B(X) = N$. If no such $X$ exists, output the word “impossible”. The input is carefully chosen such that $X < 2^{63}$ holds (if $X$ exists).

-----Examples-----
Sample Input 1:
10 24
Sample Output 1:
38

Sample Input 2:
10 11
Sample Output 2:
impossible

Sample Input 3:
9 216
Sample Output 3:
546
````

---

### competition — ID 3034

**Source:** https://open.kattis.com/problems/expectingrain
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You wish to minimize the expected amount of rain that would fall on you. To reach the bus you must get to the bus stop within $t$ seconds from now. You have timed your walking speed to be exactly $1 \frac{m}{s}$.

> **After:** You would prefer the route and timing that leave you exposed to as little rain as possible on average. You must reach the stop no later than $t$ seconds from now and walk at exactly $1 \frac{m}{s}$.

#### Clear prompt

````text
The Bluewater Geocloud Organization (BGO) has recently developed brand new software able to predict with pinpoint precision at which second any particular cloud will start and stop raining, and with what intensity. There is, however, some uncertainty about how a cloud will move around; for each zip code, each cloud will be over that zip code with some probability.

You have scraped some information about your zip code from the BGO website, and want to use it to plan your walk to the bus stop. You wish to minimize the expected amount of rain that would fall on you. To reach the bus you must get to the bus stop within $t$ seconds from now. You have timed your walking speed to be exactly $1 \frac{m}{s}$.

To complicate matters, some parts of the walk to the bus are covered by roofs where it might be beneficial to make shorts breaks whilst waiting for the worst rain to pass. Your front door (at $d$ meters from the bus stop) is always under a roof – but the bus stop need not be.

-----Input-----
The first line of input is four space-separated integers: $d$ ($1 \leq d \leq 1000$), the distance to the bus stop in meters, $t$ ($d \leq t \leq 10000$) the time until the bus leaves, $c$ ($0 \leq c \leq 1000000$), the number of clouds tracked by BGO, and finally $r$ ($0 \leq r \leq d$), the number of roofs. The next $c$ lines describe the clouds; the $i$’th such line contains four numbers $s_ i$, $e_ i$, $p_ i$ and $a_ i$ describing the $i$’th cloud:
 - $s_ i$ ($0 \leq s_ i < t$) is an integer giving the number of seconds until the cloud starts its raining period,
 - $e_ i$ ($s_ i < e_ i \leq t$) is an integer giving the number of seconds until the cloud ends its raining period,
 - $p_ i$ ($0 \leq p_ i \leq 1$) is a real number (with at most $6$ digits after the decimal point) giving the probability that the cloud is in your zip code during its raining period, and
 - $a_ i$ ($0 \leq a_ i \leq 100$) is an integer indicating the amount of rain the cloud will release during its raining period, given as nm per second.

Finally $r$ roof segments follow, each on its own line; the $j$’th such line contains two integers $x_ j$ and $y_ j$ ($0 \leq x_ j < y_ j \leq d+1$), indicating that there is a roof segment starting at distance $x_ j$ away from home, ending at distance $y_ j$ away from home along the route to the bus stop. Both your home, the bus stop an the entire route between them are in the same zip code. No two roofs overlap, however one roof may start at the same exact location as another ends.

-----Output-----
The output consists of single a real value, the minimum amount of rain in nm you can expect on your route if you reach the bus stop in time. Answers with absolute or relative precision $10^{-5}$ of the actual value will be accepted.

-----Examples-----
Sample Input 1:
20 60 2 1
5 15 0.33333 30
22 60 0.66666 70
0 10
Sample Output 1:
466.662

Sample Input 2:
3 4 2 1
1 3 0.25 8
2 4 0.66667 15
1 2
Sample Output 2:
10.00005

Sample Input 3:
3 4 1 0
0 2 0.25 8
Sample Output 3:
2.0
````

#### Less-explicit prompt

````text
The Bluewater Geocloud Organization (BGO) has recently developed brand new software able to predict with pinpoint precision at which second any particular cloud will start and stop raining, and with what intensity. There is, however, some uncertainty about how a cloud will move around; for each zip code, each cloud will be over that zip code with some probability.

You have scraped some information about your zip code from the BGO website, and want to use it to plan your walk to the bus stop. You would prefer the route and timing that leave you exposed to as little rain as possible on average. You must reach the stop no later than $t$ seconds from now and walk at exactly $1 \frac{m}{s}$.

To complicate matters, some parts of the walk to the bus are covered by roofs where it might be beneficial to make shorts breaks whilst waiting for the worst rain to pass. Your front door (at $d$ meters from the bus stop) is always under a roof – but the bus stop need not be.

-----Input-----
The first line of input is four space-separated integers: $d$ ($1 \leq d \leq 1000$), the distance to the bus stop in meters, $t$ ($d \leq t \leq 10000$) the time until the bus leaves, $c$ ($0 \leq c \leq 1000000$), the number of clouds tracked by BGO, and finally $r$ ($0 \leq r \leq d$), the number of roofs. The next $c$ lines describe the clouds; the $i$’th such line contains four numbers $s_ i$, $e_ i$, $p_ i$ and $a_ i$ describing the $i$’th cloud:
 - $s_ i$ ($0 \leq s_ i < t$) is an integer giving the number of seconds until the cloud starts its raining period,
 - $e_ i$ ($s_ i < e_ i \leq t$) is an integer giving the number of seconds until the cloud ends its raining period,
 - $p_ i$ ($0 \leq p_ i \leq 1$) is a real number (with at most $6$ digits after the decimal point) giving the probability that the cloud is in your zip code during its raining period, and
 - $a_ i$ ($0 \leq a_ i \leq 100$) is an integer indicating the amount of rain the cloud will release during its raining period, given as nm per second.

Finally $r$ roof segments follow, each on its own line; the $j$’th such line contains two integers $x_ j$ and $y_ j$ ($0 \leq x_ j < y_ j \leq d+1$), indicating that there is a roof segment starting at distance $x_ j$ away from home, ending at distance $y_ j$ away from home along the route to the bus stop. Both your home, the bus stop an the entire route between them are in the same zip code. No two roofs overlap, however one roof may start at the same exact location as another ends.

-----Output-----
The output consists of single a real value, the minimum amount of rain in nm you can expect on your route if you reach the bus stop in time. Answers with absolute or relative precision $10^{-5}$ of the actual value will be accepted.

-----Examples-----
Sample Input 1:
20 60 2 1
5 15 0.33333 30
22 60 0.66666 70
0 10
Sample Output 1:
466.662

Sample Input 2:
3 4 2 1
1 3 0.25 8
2 4 0.66667 15
1 2
Sample Output 2:
10.00005

Sample Input 3:
3 4 1 0
0 2 0.25 8
Sample Output 3:
2.0
````

---

### competition — ID 3035

**Source:** https://open.kattis.com/problems/lemonadetrade
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Of course, you want to maximise the amount of blue lemonade you end up with.

> **After:** Naturally, you would prefer to finish with as much blue lemonade as the trades allow.

2. **body**

> **Before:** Fortunately, you know in advance what everybody is offering for trade. Your task is to write a program to find the maximum amount of blue lemonade that you can obtain.

> **After:** Given the offers in their fixed visiting order, work out the best final quantity of blue lemonade available to you.

#### Clear prompt

````text
The lunch break just started! Your mother gave you one litre of pink lemonade. You do not like pink lemonade and want blue lemonade instead. Fortunately for you the other children in class are willing to trade with you.

Each of them is willing to offer you any quantity of the virtually infinite amount of lemonade they got from their mother, in exchange for their favourite lemonade, according to some exchange rate. The other children are sitting in a long row in the class room and you will walk along the row, passing each child only once. You are not allowed to walk back! Of course, you want to maximise the amount of blue lemonade you end up with. In case you can obtain more than $10$ litres of blue lemonade, this is more than you will need, and you will throw away any excess (and keep the $10$ litres).

Fortunately, you know in advance what everybody is offering for trade. Your task is to write a program to find the maximum amount of blue lemonade that you can obtain.

-----Input-----
The input consists of the following:
 - One line containing a single integer $0\leq N \leq 10^5$, the number of children in the class room, excluding yourself;
 - $N$ lines, each containing two strings $O, W$ and a floating point number $0.5 < R < 2$, the name of the lemonade that is offered, the name of the lemonade that is wanted, and the exchange rate: for every litre of lemonade $W$ that you trade you get $R$ litres of lemonade $O$ in return. Exchange rates are given with at most $7$ digits after the decimal point.

All strings are guaranteed to have at most $10$ alphanumeric characters.

-----Output-----
Output a single line containing a single floating point number $M$, the maximum amount (in litres) of blue lemonade that you can obtain. In case you could obtain more than $10$ litres, $M$ is considered to be $10$. You are required to output $M$ with absolute precision $10^{-6}$.

-----Examples-----
Sample Input 1:
3
blue pink 1.0
red pink 1.5
blue red 1.0
Sample Output 1:
1.500000000000000

Sample Input 2:
2
blue red 1.0
red pink 1.5
Sample Output 2:
0.000000000000000

Sample Input 3:
4
orange pink 1.9
yellow orange 1.9
green yellow 1.9
blue green 1.9
Sample Output 3:
10.000000000000000
````

#### Less-explicit prompt

````text
The lunch break just started! Your mother gave you one litre of pink lemonade. You do not like pink lemonade and want blue lemonade instead. Fortunately for you the other children in class are willing to trade with you.

Each of them is willing to offer you any quantity of the virtually infinite amount of lemonade they got from their mother, in exchange for their favourite lemonade, according to some exchange rate. The other children are sitting in a long row in the class room and you will walk along the row, passing each child only once. You are not allowed to walk back! Naturally, you would prefer to finish with as much blue lemonade as the trades allow. In case you can obtain more than $10$ litres of blue lemonade, this is more than you will need, and you will throw away any excess (and keep the $10$ litres).

Given the offers in their fixed visiting order, work out the best final quantity of blue lemonade available to you.

-----Input-----
The input consists of the following:
 - One line containing a single integer $0\leq N \leq 10^5$, the number of children in the class room, excluding yourself;
 - $N$ lines, each containing two strings $O, W$ and a floating point number $0.5 < R < 2$, the name of the lemonade that is offered, the name of the lemonade that is wanted, and the exchange rate: for every litre of lemonade $W$ that you trade you get $R$ litres of lemonade $O$ in return. Exchange rates are given with at most $7$ digits after the decimal point.

All strings are guaranteed to have at most $10$ alphanumeric characters.

-----Output-----
Output a single line containing a single floating point number $M$, the maximum amount (in litres) of blue lemonade that you can obtain. In case you could obtain more than $10$ litres, $M$ is considered to be $10$. You are required to output $M$ with absolute precision $10^{-6}$.

-----Examples-----
Sample Input 1:
3
blue pink 1.0
red pink 1.5
blue red 1.0
Sample Output 1:
1.500000000000000

Sample Input 2:
2
blue red 1.0
red pink 1.5
Sample Output 2:
0.000000000000000

Sample Input 3:
4
orange pink 1.9
yellow orange 1.9
green yellow 1.9
blue green 1.9
Sample Output 3:
10.000000000000000
````

---

### competition — ID 3036

**Source:** https://open.kattis.com/problems/kitchencombinatorics
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** While waiting for the meecaroo, Swedish Chef starts wondering: how many different dinner experiences are there that he could make, by different choices of dishes and brands for the ingredients?

> **After:** Swedish Chef wonders about the range of distinct complete dinners possible when both dish selections and ingredient brands are varied, subject to the compatibility and shared-brand rules.

#### Clear prompt

````text
The world-renowned Swedish Chef is planning a gourmet three-course dinner for some muppets: a starter course, a main course, and a dessert. His famous Swedish cook-book offers a wide variety of choices for each of these three courses, though some of them do not go well together (for instance, you of course cannot serve chocolate moose and sooted shreemp at the same dinner). 

Each potential dish has a list of ingredients. Each ingredient is in turn available from a few different brands. Each brand is of course unique in its own special way, so using a particular brand of an ingredient will always result in a completely different dinner experience than using another brand of the same ingredient.

Some common ingredients such as pølårber may appear in two of the three chosen dishes, or in all three of them. When an ingredient is used in more than one of the three selected dishes, Swedish Chef will use the same brand of the ingredient in all of them.

While waiting for the meecaroo, Swedish Chef starts wondering: how many different dinner experiences are there that he could make, by different choices of dishes and brands for the ingredients?

-----Input-----
The input consists of:
 - one line containing five integers $r$, $s$, $m$, $d$, $n$, where $1 \le r \le 1000$ is the number of different ingredients that exist, $1 \le s, m, d \le 25$ are the number of available starter dishes, main dishes, and desserts, respectively, and $0 \le n \le 2000$ is the number of pairs of dishes that do not go well together.
 - one line containing $r$ integers $b_1, \ldots , b_ r$, where $1 \le b_ i \le 100$ is the number of different brands of ingredient $i$.
 - $s+m+d$ lines describing the $s$ starter dishes, then the $m$ main dishes, then the $d$ desserts. Each such line starts with an integer $1 \le k \le 20$ denoting the number of ingredients of the dish, and is followed by $k$ distinct integers $i_1, \ldots , i_ k$, where for each $1 \le j \le k$, $1 \le i_ j \le r$ is an ingredient.
 - $n$ lines each containing two incompatible dishes. Each dish is identified by an integer $1 \le j \le s+m+d$, referring to the $j$’th dish given in the input (so $1 \le j \le s$ refers to the starter dishes, $s < j \le s+m$ refers to the main dishes, and $s+m < j \le s+m+d$ refers to the desserts).

Each pair of incompatible dishes in the input consists of two dishes of different types, and any one pair of dishes is listed at most once.

-----Output-----
If the number of different dinner experiences Swedish Chef can make is at most $10^{18}$, then output that number. Otherwise, output “too many”.

-----Examples-----
Sample Input 1:
6 1 1 1 0
2 3 1 5 3 2
2 1 2
3 3 4 5
1 6
Sample Output 1:
180

Sample Input 2:
3 2 2 1 1
2 3 2
1 1
1 2
1 2
1 3
1 1
2 3
Sample Output 2:
22

Sample Input 3:
3 1 1 1 1
5 5 5
3 1 2 3
3 1 2 3
3 1 2 3
2 1
Sample Output 3:
0
````

#### Less-explicit prompt

````text
The world-renowned Swedish Chef is planning a gourmet three-course dinner for some muppets: a starter course, a main course, and a dessert. His famous Swedish cook-book offers a wide variety of choices for each of these three courses, though some of them do not go well together (for instance, you of course cannot serve chocolate moose and sooted shreemp at the same dinner). 

Each potential dish has a list of ingredients. Each ingredient is in turn available from a few different brands. Each brand is of course unique in its own special way, so using a particular brand of an ingredient will always result in a completely different dinner experience than using another brand of the same ingredient.

Some common ingredients such as pølårber may appear in two of the three chosen dishes, or in all three of them. When an ingredient is used in more than one of the three selected dishes, Swedish Chef will use the same brand of the ingredient in all of them.

Swedish Chef wonders about the range of distinct complete dinners possible when both dish selections and ingredient brands are varied, subject to the compatibility and shared-brand rules.

-----Input-----
The input consists of:
 - one line containing five integers $r$, $s$, $m$, $d$, $n$, where $1 \le r \le 1000$ is the number of different ingredients that exist, $1 \le s, m, d \le 25$ are the number of available starter dishes, main dishes, and desserts, respectively, and $0 \le n \le 2000$ is the number of pairs of dishes that do not go well together.
 - one line containing $r$ integers $b_1, \ldots , b_ r$, where $1 \le b_ i \le 100$ is the number of different brands of ingredient $i$.
 - $s+m+d$ lines describing the $s$ starter dishes, then the $m$ main dishes, then the $d$ desserts. Each such line starts with an integer $1 \le k \le 20$ denoting the number of ingredients of the dish, and is followed by $k$ distinct integers $i_1, \ldots , i_ k$, where for each $1 \le j \le k$, $1 \le i_ j \le r$ is an ingredient.
 - $n$ lines each containing two incompatible dishes. Each dish is identified by an integer $1 \le j \le s+m+d$, referring to the $j$’th dish given in the input (so $1 \le j \le s$ refers to the starter dishes, $s < j \le s+m$ refers to the main dishes, and $s+m < j \le s+m+d$ refers to the desserts).

Each pair of incompatible dishes in the input consists of two dishes of different types, and any one pair of dishes is listed at most once.

-----Output-----
If the number of different dinner experiences Swedish Chef can make is at most $10^{18}$, then output that number. Otherwise, output “too many”.

-----Examples-----
Sample Input 1:
6 1 1 1 0
2 3 1 5 3 2
2 1 2
3 3 4 5
1 6
Sample Output 1:
180

Sample Input 2:
3 2 2 1 1
2 3 2
1 1
1 2
1 2
1 3
1 1
2 3
Sample Output 2:
22

Sample Input 3:
3 1 1 1 1
5 5 5
3 1 2 3
3 1 2 3
3 1 2 3
2 1
Sample Output 3:
0
````

---

### competition — ID 3037

**Source:** https://open.kattis.com/problems/whiteboard
**Review status:** `needs_source_illustration_review`

**Source and design flags:**

- SOURCE CHECK: Narrative refers to diagrams not embedded in text. Check that timestep behavior and trajectory are independently understood.

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Mr. Turtle wants to know the earliest and latest time his marker can dry out, and he’ll still obtain the drawing in his head. Can you help him?

> **After:** He is interested in the range of dry-out moments that would still produce exactly the intended final picture, from the first viable moment through the last.

#### Clear prompt

````text
Mr. Turtle loves drawing on his whiteboard at home. One day when he was drawing, his marker dried out! Mr. Turtle then noticed that the marker behaved like an eraser for the remainder of his drawing.

Mr. Turtle has a picture in his head of how he wants his final drawing to appear. He plans out his entire drawing ahead of time, step by step. Mr. Turtle’s plan is a sequence of commands: up, down, left or right, with a distance. He starts drawing in the bottom left corner of his whiteboard. Consider the $6 \times 8$ whiteboard and sequence of commands in the first diagram. If the marker runs dry at timestep $17$, the board will look like the second diagram (the numbers indicate the timestep when the marker is at each cell). Note that it will make a mark at timestep $17$, but not at timestep $18$. 

Mr. Turtle wants to know the earliest and latest time his marker can dry out, and he’ll still obtain the drawing in his head. Can you help him? Note that timestep $0$ is the moment before the marker touches the board. It is valid for a marker to dry out at timestep $0$.

-----Input-----
Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. The input will start with a line with $3$ space-separated integers $h$, $w$ and $n$ ($1 \le h,w,n \le 1000000, w \cdot h \le 1000000$) where $h$ and $w$ are the height and width of the whiteboard respectively, and $n$ is the number of commands in Mr. Turtle’s plan.

The next $h$ lines will each consist of exactly $w$ characters, with each character being either ‘#’ or ‘.’ . This is the pattern in Mr. Turtle’s head, where ’#’ is a marked cell, and ‘.’ is a blank cell.

The next $n$ lines will each consist of a command, of the form “direction distance”, with a single space between the direction and the distance and no other spaces on the line. The direction will be exactly one of the set $\{ \texttt{up}, \texttt{down}, \texttt{left}, \texttt{right} \} $, guaranteed to be all lower case. The distance will be between $1$ and $1000000$ inclusive. The commands must be executed in order. It is guaranteed that no command will take the marker off of the whiteboard.

-----Output-----
Output two integers, first the minimum, then the maximum time that can pass before the marker dries out, and Mr. Turtle can still end up with the target drawing. Neither number should be larger than the last timestep that the marker is on the board, so if the marker can run to the end and still draw the target drawing, use the last timestep that the marker is on the board. If it’s not possible to end up with the target drawing, output -1 -1.

-----Examples-----
Sample Input 1:
6 8 5
........
...#....
########
#..#...#
#..#####
#.......
up 3
right 7
down 2
left 4
up 3
Sample Output 1:
20 20

Sample Input 2:
6 8 5
........
........
###.####
#......#
#..#####
#.......
up 3
right 7
down 2
left 4
up 3
Sample Output 2:
17 17

Sample Input 3:
3 3 2
...
.#.
...
up 2
right 2
Sample Output 3:
-1 -1
````

#### Less-explicit prompt

````text
Mr. Turtle loves drawing on his whiteboard at home. One day when he was drawing, his marker dried out! Mr. Turtle then noticed that the marker behaved like an eraser for the remainder of his drawing.

Mr. Turtle has a picture in his head of how he wants his final drawing to appear. He plans out his entire drawing ahead of time, step by step. Mr. Turtle’s plan is a sequence of commands: up, down, left or right, with a distance. He starts drawing in the bottom left corner of his whiteboard. Consider the $6 \times 8$ whiteboard and sequence of commands in the first diagram. If the marker runs dry at timestep $17$, the board will look like the second diagram (the numbers indicate the timestep when the marker is at each cell). Note that it will make a mark at timestep $17$, but not at timestep $18$. 

He is interested in the range of dry-out moments that would still produce exactly the intended final picture, from the first viable moment through the last. Note that timestep $0$ is the moment before the marker touches the board. It is valid for a marker to dry out at timestep $0$.

-----Input-----
Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. The input will start with a line with $3$ space-separated integers $h$, $w$ and $n$ ($1 \le h,w,n \le 1000000, w \cdot h \le 1000000$) where $h$ and $w$ are the height and width of the whiteboard respectively, and $n$ is the number of commands in Mr. Turtle’s plan.

The next $h$ lines will each consist of exactly $w$ characters, with each character being either ‘#’ or ‘.’ . This is the pattern in Mr. Turtle’s head, where ’#’ is a marked cell, and ‘.’ is a blank cell.

The next $n$ lines will each consist of a command, of the form “direction distance”, with a single space between the direction and the distance and no other spaces on the line. The direction will be exactly one of the set $\{ \texttt{up}, \texttt{down}, \texttt{left}, \texttt{right} \} $, guaranteed to be all lower case. The distance will be between $1$ and $1000000$ inclusive. The commands must be executed in order. It is guaranteed that no command will take the marker off of the whiteboard.

-----Output-----
Output two integers, first the minimum, then the maximum time that can pass before the marker dries out, and Mr. Turtle can still end up with the target drawing. Neither number should be larger than the last timestep that the marker is on the board, so if the marker can run to the end and still draw the target drawing, use the last timestep that the marker is on the board. If it’s not possible to end up with the target drawing, output -1 -1.

-----Examples-----
Sample Input 1:
6 8 5
........
...#....
########
#..#...#
#..#####
#.......
up 3
right 7
down 2
left 4
up 3
Sample Output 1:
20 20

Sample Input 2:
6 8 5
........
........
###.####
#......#
#..#####
#.......
up 3
right 7
down 2
left 4
up 3
Sample Output 2:
17 17

Sample Input 3:
3 3 2
...
.#.
...
up 2
right 2
Sample Output 3:
-1 -1
````

---

### competition — ID 3038

**Source:** https://open.kattis.com/problems/kallaxconstruction
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Therefore you start a quest of figuring out which pack has the lowest advertised amount, while still containing at least the number of bolts you need.

> **After:** You would rather buy a pack with a lower label value, but only if its actual contents are guaranteed to meet your requirement despite all permitted repacking choices.

#### Clear prompt

````text
You are the owner of IKEA, and you need to order a large number of bolts $B$. There is a single bolt manufacturer, but there are multiple companies reselling these bolts in packs (e.g. boxes, pallets). These companies form a directed chain, where each company buys packs from the previous company and combines these into new packs (with, of course, the logo of the company displayed brilliantly).

At first glance, it might seem that these intermediate companies offer no advantage, as they just repack the packs of the previous company into larger packs. However, every company has their own target audience, so they want to sell packs with a specific amount of bolts. Because every company only uses the packs of the previous company, it might not be possible to create a pack that has the exact number of bolts specified. Instead, if a company wants to create a pack which is guaranteed to contain $X$ bolts, it bundles various packs from the previous company where the displayed amount of bolts on these packs sums to no less than $X$. If there are multiple such combinations it picks any from those whose displayed sum is minimal. For a better understanding, see the example below. Note that individual companies have no knowledge of the supply chain other than the pack sizes the previous company offers them.

You realise you can take advantage of this: when a company specifies that a pack has a certain number of bolts, it might in practice contain more! Therefore you start a quest of figuring out which pack has the lowest advertised amount, while still containing at least the number of bolts you need. Thanks to your business relations, you can freely choose the company to buy a pack from, including the manufacturer.

Explanation of first sample

Suppose that we would like to buy $B=310$ bolts, and that there are three companies. The manufacturer (company one) sells packs of $40$ and $65$ bolts. Company two sells packs of $100$ and $150$ bolts. It cannot get these exact amounts from company one, and instead composes them as $100 \leq 40+65$ and $150 \leq 40+40+40+40$.

Next comes company three, offering packs of $300$ and $320$ bolts. It can assemble its $300$-pack using three $100$-packs (which we know actually contains $105+105+105 = 315$ bolts) or using two $150$-packs (which we know actually contains $160+160 = 320$ bolts). However, for company three either combination is fine, so you do not know how many bolts a pack actually contains. In this case you assume the worst, i.e. that this pack contains $315$ bolts.

For its second pack of $320$ bolts, company three uses $100+100+150 \geq 320$ (which we know really contains $105+105+160=370$ bolts). There are other combinations adding up to more than $320$, but none achieve the minimum of $350$, so we know company three picks that combination.

Note in particular, that company three does not know that the $150$-packs of company two actually contain $160$ bolts (otherwise it could compose its $320$-pack out of two of these). It only knows the amounts advertised by company two.

The packet of size $300$ sold by company three is the smallest advertised packet that contains at least $B=310$ bolts, so this is the packet we should buy. 

Pack one

Pack two 

Advertised amount

Real amount

Advertised amount

Real amount

Company one

$40$

$40$

$65$

$65$

Company two

$100$

$105$

$150$

$160$

Company three

$300$

$315$ or $320$

$320$

$370$

-----Input-----
 - The first line of the input contains an integer $1 \leq B \leq 10^3$ giving the number of bolts that you need.
 - The second line of the input contains an integer $1 \leq k \leq 10$ giving the number of companies.
 - The next $k$ lines each describe a company. Each line consists of the integers $l_ i, n_1, n_2, \ldots , n_{l_ i}$ meaning that the company $i$ produces $1\leq l_ i\leq 10$ types of packages of sizes $0 < n_1< n_2< \ldots < n_{l_ i} \leq 10^3$, respectively.

-----Output-----
 - A single integer giving the smallest size of a package that you can buy which contains at least $B$ bolts no matter how the companies build their packages, or impossible if this cannot be achieved.

-----Examples-----
Sample Input 1:
371
3
2 40 65
2 100 150
2 300 320
Sample Output 1:
impossible

Sample Input 2:
310
3
2 40 65
2 100 150
2 300 320
Sample Output 2:
300

Sample Input 3:
90
2
2 20 35
2 88 200
Sample Output 3:
88
````

#### Less-explicit prompt

````text
You are the owner of IKEA, and you need to order a large number of bolts $B$. There is a single bolt manufacturer, but there are multiple companies reselling these bolts in packs (e.g. boxes, pallets). These companies form a directed chain, where each company buys packs from the previous company and combines these into new packs (with, of course, the logo of the company displayed brilliantly).

At first glance, it might seem that these intermediate companies offer no advantage, as they just repack the packs of the previous company into larger packs. However, every company has their own target audience, so they want to sell packs with a specific amount of bolts. Because every company only uses the packs of the previous company, it might not be possible to create a pack that has the exact number of bolts specified. Instead, if a company wants to create a pack which is guaranteed to contain $X$ bolts, it bundles various packs from the previous company where the displayed amount of bolts on these packs sums to no less than $X$. If there are multiple such combinations it picks any from those whose displayed sum is minimal. For a better understanding, see the example below. Note that individual companies have no knowledge of the supply chain other than the pack sizes the previous company offers them.

You realise you can take advantage of this: when a company specifies that a pack has a certain number of bolts, it might in practice contain more! You would rather buy a pack with a lower label value, but only if its actual contents are guaranteed to meet your requirement despite all permitted repacking choices. Thanks to your business relations, you can freely choose the company to buy a pack from, including the manufacturer.

Explanation of first sample

Suppose that we would like to buy $B=310$ bolts, and that there are three companies. The manufacturer (company one) sells packs of $40$ and $65$ bolts. Company two sells packs of $100$ and $150$ bolts. It cannot get these exact amounts from company one, and instead composes them as $100 \leq 40+65$ and $150 \leq 40+40+40+40$.

Next comes company three, offering packs of $300$ and $320$ bolts. It can assemble its $300$-pack using three $100$-packs (which we know actually contains $105+105+105 = 315$ bolts) or using two $150$-packs (which we know actually contains $160+160 = 320$ bolts). However, for company three either combination is fine, so you do not know how many bolts a pack actually contains. In this case you assume the worst, i.e. that this pack contains $315$ bolts.

For its second pack of $320$ bolts, company three uses $100+100+150 \geq 320$ (which we know really contains $105+105+160=370$ bolts). There are other combinations adding up to more than $320$, but none achieve the minimum of $350$, so we know company three picks that combination.

Note in particular, that company three does not know that the $150$-packs of company two actually contain $160$ bolts (otherwise it could compose its $320$-pack out of two of these). It only knows the amounts advertised by company two.

The packet of size $300$ sold by company three is the smallest advertised packet that contains at least $B=310$ bolts, so this is the packet we should buy. 

Pack one

Pack two 

Advertised amount

Real amount

Advertised amount

Real amount

Company one

$40$

$40$

$65$

$65$

Company two

$100$

$105$

$150$

$160$

Company three

$300$

$315$ or $320$

$320$

$370$

-----Input-----
 - The first line of the input contains an integer $1 \leq B \leq 10^3$ giving the number of bolts that you need.
 - The second line of the input contains an integer $1 \leq k \leq 10$ giving the number of companies.
 - The next $k$ lines each describe a company. Each line consists of the integers $l_ i, n_1, n_2, \ldots , n_{l_ i}$ meaning that the company $i$ produces $1\leq l_ i\leq 10$ types of packages of sizes $0 < n_1< n_2< \ldots < n_{l_ i} \leq 10^3$, respectively.

-----Output-----
 - A single integer giving the smallest size of a package that you can buy which contains at least $B$ bolts no matter how the companies build their packages, or impossible if this cannot be achieved.

-----Examples-----
Sample Input 1:
371
3
2 40 65
2 100 150
2 300 320
Sample Output 1:
impossible

Sample Input 2:
310
3
2 40 65
2 100 150
2 300 320
Sample Output 2:
300

Sample Input 3:
90
2
2 20 35
2 88 200
Sample Output 3:
88
````

---

### competition — ID 3039

**Source:** https://open.kattis.com/problems/foldingacube
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** But what about other initial shapes? That is, given six unit squares that are attached together along some of their sides, can we form a unit cube by folding this arrangement?

> **After:** For another arrangement of six edge-connected unit squares, consider whether folding along their shared edges could produce all six faces of a unit cube.

#### Clear prompt

````text
It is well known that a set of six unit squares that are attached together in a “cross” can be folded into a cube.

But what about other initial shapes? That is, given six unit squares that are attached together along some of their sides, can we form a unit cube by folding this arrangement?

-----Input-----
Input consists of $6$ lines each containing $6$ characters, describing the initial arrangement of unit squares. Each character is either a ., meaning it is empty, or a # meaning it is a unit square.

There are precisely $6$ occurrences of # indicating the unit squares. These form a connected component, meaning it is possible to reach any # from any other # without touching a . by making only horizontal and vertical movements. Furthermore, there is no $2 \times 2$ subsquare consisting of only #. That is, the pattern

##
##

does not appear in the input.

-----Output-----
If you can fold the unit squares into a cube, display can fold. Otherwise display cannot fold.

-----Examples-----
Sample Input 1:
......
......
######
......
......
......
Sample Output 1:
cannot fold

Sample Input 2:
......
#.....
####..
#.....
......
......
Sample Output 2:
can fold

Sample Input 3:
..##..
...#..
..##..
...#..
......
......
Sample Output 3:
cannot fold
````

#### Less-explicit prompt

````text
It is well known that a set of six unit squares that are attached together in a “cross” can be folded into a cube.

For another arrangement of six edge-connected unit squares, consider whether folding along their shared edges could produce all six faces of a unit cube.

-----Input-----
Input consists of $6$ lines each containing $6$ characters, describing the initial arrangement of unit squares. Each character is either a ., meaning it is empty, or a # meaning it is a unit square.

There are precisely $6$ occurrences of # indicating the unit squares. These form a connected component, meaning it is possible to reach any # from any other # without touching a . by making only horizontal and vertical movements. Furthermore, there is no $2 \times 2$ subsquare consisting of only #. That is, the pattern

##
##

does not appear in the input.

-----Output-----
If you can fold the unit squares into a cube, display can fold. Otherwise display cannot fold.

-----Examples-----
Sample Input 1:
......
......
######
......
......
......
Sample Output 1:
cannot fold

Sample Input 2:
......
#.....
####..
#.....
......
......
Sample Output 2:
can fold

Sample Input 3:
..##..
...#..
..##..
...#..
......
......
Sample Output 3:
cannot fold
````

---

### competition — ID 3040

**Source:** https://open.kattis.com/problems/repeatedsubstrings
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Given an input string composed solely of lowercase English letters, find the longest substring that occurs more than once in the input string. The two occurrences are allowed to partially overlap.

> **After:** Consider the substrings appearing at least twice in the lowercase input string, including pairs of occurrences that overlap. Prefer candidates of greatest length.

#### Clear prompt

````text
Given an input string composed solely of lowercase English letters, find the longest substring that occurs more than once in the input string. The two occurrences are allowed to partially overlap.

-----Input-----
The input is a single line containing a string of lowercase letters. The string contains more than one character, but no more than $10^5$. At least one letter will appear at least twice.

-----Output-----
Print a single line of output: the longest substring that occurs more than once in the input string. If there are multiple longest repeated substrings, print the one the would come first when the longest substrings are sorted in lexicographical (alphabetical) order.

-----Examples-----
Sample Input 1:
abcefgabc
Sample Output 1:
abc

Sample Input 2:
abcbabcba
Sample Output 2:
abcba

Sample Input 3:
aaaa
Sample Output 3:
aaa
````

#### Less-explicit prompt

````text
Consider the substrings appearing at least twice in the lowercase input string, including pairs of occurrences that overlap. Prefer candidates of greatest length.

-----Input-----
The input is a single line containing a string of lowercase letters. The string contains more than one character, but no more than $10^5$. At least one letter will appear at least twice.

-----Output-----
Print a single line of output: the longest substring that occurs more than once in the input string. If there are multiple longest repeated substrings, print the one the would come first when the longest substrings are sorted in lexicographical (alphabetical) order.

-----Examples-----
Sample Input 1:
abcefgabc
Sample Output 1:
abc

Sample Input 2:
abcbabcba
Sample Output 2:
abcba

Sample Input 3:
aaaa
Sample Output 3:
aaa
````

---

### competition — ID 3041

**Source:** https://open.kattis.com/problems/coupons
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Initially, Johan is located in zone $0$. Help him minimize the number of coupons he must purchase!

> **After:** Johan begins in zone $0$ and would like his sequence of ticket purchases to cost as few coupons as possible while covering every trip.

#### Clear prompt

````text
Johan lives in Stockholm, which means he has to travel a lot by bus and subway. To travel, he needs to pay a number of coupons, depending on which zones his trip goes between.

A ticket is specified by an interval $[A, B]$ of zones it is valid in, and costs $2 + |A - B|$ coupons to purchase. When Johan buys a ticket, it is valid for exactly $10000$ seconds and can be used for any trip which both starts and ends in zones in the interval $[A, B]$.

Johan is now going to make $N$ trips in order. For each trip, you will be given the zone Johan travels to, as well as the time at which he starts his trip. Initially, Johan is located in zone $0$. Help him minimize the number of coupons he must purchase!

Notes: Johan can buy a new ticket at any point, even if he already has a valid ticket. A ticket only needs to be valid at the moment Johan starts a trip, it is OK if the $10000$ seconds expire while Johan is taking the trip.

-----Input-----
The first line contains the integer $0 \le N \le 400000$ – the number of trips Johan wants to make.

The next $N$ lines contains two space-separated integers $0 \le Z \le 10$ and $0 \le T \le 10^9$, the zone and time for Johan’s next trip (in seconds from now). The values of $T$ will be strictly increasing.

-----Output-----
The first and only line should contain a single integer: the minimum number of coupons Johan must purchase to make all his trips.

-----Examples-----
Sample Input 1:
2
1 4
2 5
Sample Output 1:
4

Sample Input 2:
2
1 4
2 10005
Sample Output 2:
6

Sample Input 3:
3
1 4
2 10
0 15
Sample Output 3:
4
````

#### Less-explicit prompt

````text
Johan lives in Stockholm, which means he has to travel a lot by bus and subway. To travel, he needs to pay a number of coupons, depending on which zones his trip goes between.

A ticket is specified by an interval $[A, B]$ of zones it is valid in, and costs $2 + |A - B|$ coupons to purchase. When Johan buys a ticket, it is valid for exactly $10000$ seconds and can be used for any trip which both starts and ends in zones in the interval $[A, B]$.

Johan is now going to make $N$ trips in order. For each trip, you will be given the zone Johan travels to, as well as the time at which he starts his trip. Johan begins in zone $0$ and would like his sequence of ticket purchases to cost as few coupons as possible while covering every trip.

Notes: Johan can buy a new ticket at any point, even if he already has a valid ticket. A ticket only needs to be valid at the moment Johan starts a trip, it is OK if the $10000$ seconds expire while Johan is taking the trip.

-----Input-----
The first line contains the integer $0 \le N \le 400000$ – the number of trips Johan wants to make.

The next $N$ lines contains two space-separated integers $0 \le Z \le 10$ and $0 \le T \le 10^9$, the zone and time for Johan’s next trip (in seconds from now). The values of $T$ will be strictly increasing.

-----Output-----
The first and only line should contain a single integer: the minimum number of coupons Johan must purchase to make all his trips.

-----Examples-----
Sample Input 1:
2
1 4
2 5
Sample Output 1:
4

Sample Input 2:
2
1 4
2 10005
Sample Output 2:
6

Sample Input 3:
3
1 4
2 10
0 15
Sample Output 3:
4
````

---

### competition — ID 3042

**Source:** https://open.kattis.com/problems/lcmtree
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You are given $n$ nodes with positive integer values to be arranged into an LCM tree. In how many ways (modulo $10^9 + 7$) can you do that?

> **After:** Consider the different parent-child arrangements of the $n$ given valued nodes that could satisfy the LCM-tree rule. Determine the number of such arrangements, taken modulo $10^9+7$.

#### Clear prompt

````text
An LCM tree is a binary tree in which each node has a positive integer value, and either zero or two children. If two nodes $x$ and $y$ are the children of node $z$, then the Least Common Multiple (LCM) of the values of node $x$ and node $y$ must equal the value of node $z$. 

You are given $n$ nodes with positive integer values to be arranged into an LCM tree. In how many ways (modulo $10^9 + 7$) can you do that? Two ways are considered different if there are two nodes $x$ and $y$ so that $x$ is a child of $y$ in one way but not in the other way.

The illustration shows one of the two ways for the first sample case. The other way can be obtained by swapping the two nodes with value $4$. Note that swapping the two leaves with values $2$ and $4$ does not give a different way.

-----Input-----
The first line has an odd integer $n$ ($1 \leq n \leq 25$). The second line has $n$ positive integers no larger than $10^9$, giving the values of the nodes.

-----Output-----
Output the number of ways to arrange the given nodes into an LCM tree, modulo $10^9 + 7$.

-----Examples-----
Sample Input 1:
7
2 3 4 4 8 12 24
Sample Output 1:
2

Sample Input 2:
3
7 7 7
Sample Output 2:
3

Sample Input 3:
5
1 2 3 2 1
Sample Output 3:
0
````

#### Less-explicit prompt

````text
An LCM tree is a binary tree in which each node has a positive integer value, and either zero or two children. If two nodes $x$ and $y$ are the children of node $z$, then the Least Common Multiple (LCM) of the values of node $x$ and node $y$ must equal the value of node $z$. 

Consider the different parent-child arrangements of the $n$ given valued nodes that could satisfy the LCM-tree rule. Determine the number of such arrangements, taken modulo $10^9+7$. Two ways are considered different if there are two nodes $x$ and $y$ so that $x$ is a child of $y$ in one way but not in the other way.

The illustration shows one of the two ways for the first sample case. The other way can be obtained by swapping the two nodes with value $4$. Note that swapping the two leaves with values $2$ and $4$ does not give a different way.

-----Input-----
The first line has an odd integer $n$ ($1 \leq n \leq 25$). The second line has $n$ positive integers no larger than $10^9$, giving the values of the nodes.

-----Output-----
Output the number of ways to arrange the given nodes into an LCM tree, modulo $10^9 + 7$.

-----Examples-----
Sample Input 1:
7
2 3 4 4 8 12 24
Sample Output 1:
2

Sample Input 2:
3
7 7 7
Sample Output 2:
3

Sample Input 3:
5
1 2 3 2 1
Sample Output 3:
0
````

---

### competition — ID 3043

**Source:** https://open.kattis.com/problems/treasure
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** Of course, you want to head to the treasure as fast as possible.

> **After:** Naturally, you would prefer a trip requiring as little calendar time as possible.

2. **body**

> **Before:** Plan wisely with the map and determine the minimum number of days you need to reach the treasure.

> **After:** Using the grid, stamina costs, and overnight-rest rule, work out how soon you could reach the treasure.

#### Clear prompt

````text
You are a treasure hunter searching for gold in the wild. Luckily you got a map of the area from a black marketeer. The map clearly shows where a box of gold is along with the surrounding terrain. Of course, you want to head to the treasure as fast as possible. However, the trip might not be easy.

The area is described by a grid of $N$ rows and $M$ columns. You are currently located at the cell labeled ‘S’. The treasure is located at the cell labeled ‘G’. Despite your eagerness for the treasure, you cannot keep moving tirelessly. The surrounding area has different landforms: plain (‘.’), forest (‘F’), mountain (‘M’) or river (‘#’). Rivers are impassable since no boats are currently available. You can navigate in four directions (up, down, left, right) between neighboring cells.

At the beginning of your trip you have $K$ stamina points. Moving onto a plain, forest, and mountain costs you $1$, $2$, and $3$ points of stamina respectively. Once you run out of stamina and can no longer move to nearby cells, you must camp and rest. Your stamina is replenished to the full $K$ points on the second day so that you can start moving again.

Plan wisely with the map and determine the minimum number of days you need to reach the treasure.

-----Input-----
The first line has three integers $N$, $M$ ($1\leq N, M \leq 50$), and $K$ ($1 \leq K \leq 100$). Each of the next $N$ lines has $M$ characters describing the grid shown by the treasure map. The grid contains only characters ‘.’, ‘F’, ‘M’, ‘#’, ‘S’, and ‘G’. It is guaranteed that ‘S’ and ‘G’ appear exactly once in the grid. You may assume your starting point (‘S’) and the treasure (‘G’) are both on a plain.

-----Output-----
Output the minimum number of days you need to reach the treasure. If it is impossible to get to the treasure, output “-1”.

-----Examples-----
Sample Input 1:
2 5 4
S#.F.
.MFMG
Sample Output 1:
3

Sample Input 2:
1 2 1
GS
Sample Output 2:
1

Sample Input 3:
2 2 10
S#
#G
Sample Output 3:
-1
````

#### Less-explicit prompt

````text
You are a treasure hunter searching for gold in the wild. Luckily you got a map of the area from a black marketeer. The map clearly shows where a box of gold is along with the surrounding terrain. Naturally, you would prefer a trip requiring as little calendar time as possible. However, the trip might not be easy.

The area is described by a grid of $N$ rows and $M$ columns. You are currently located at the cell labeled ‘S’. The treasure is located at the cell labeled ‘G’. Despite your eagerness for the treasure, you cannot keep moving tirelessly. The surrounding area has different landforms: plain (‘.’), forest (‘F’), mountain (‘M’) or river (‘#’). Rivers are impassable since no boats are currently available. You can navigate in four directions (up, down, left, right) between neighboring cells.

At the beginning of your trip you have $K$ stamina points. Moving onto a plain, forest, and mountain costs you $1$, $2$, and $3$ points of stamina respectively. Once you run out of stamina and can no longer move to nearby cells, you must camp and rest. Your stamina is replenished to the full $K$ points on the second day so that you can start moving again.

Using the grid, stamina costs, and overnight-rest rule, work out how soon you could reach the treasure.

-----Input-----
The first line has three integers $N$, $M$ ($1\leq N, M \leq 50$), and $K$ ($1 \leq K \leq 100$). Each of the next $N$ lines has $M$ characters describing the grid shown by the treasure map. The grid contains only characters ‘.’, ‘F’, ‘M’, ‘#’, ‘S’, and ‘G’. It is guaranteed that ‘S’ and ‘G’ appear exactly once in the grid. You may assume your starting point (‘S’) and the treasure (‘G’) are both on a plain.

-----Output-----
Output the minimum number of days you need to reach the treasure. If it is impossible to get to the treasure, output “-1”.

-----Examples-----
Sample Input 1:
2 5 4
S#.F.
.MFMG
Sample Output 1:
3

Sample Input 2:
1 2 1
GS
Sample Output 2:
1

Sample Input 3:
2 2 10
S#
#G
Sample Output 3:
-1
````

---

### competition — ID 3044

**Source:** https://open.kattis.com/problems/buggyrobot
**Review status:** `candidate_requires_human_review`

#### Change log (not part of either model prompt)

1. **body**

> **Before:** You would like to fix the string so that the robot will reach the goal, but you do not want your friend to feel bad, so you are hoping to make as few changes to the program as are needed.

> **After:** You want the command sequence to reach the goal while disturbing as little of your friend’s program as possible.

#### Clear prompt

````text
Your friend just bought a new programmable robot and has asked for your help. The robot operates in a 2D grid that may contain obstacles. The environment has a known start location and a known goal location. The robot is controlled with a string consisting of commands L, R, U, and D, which respectively instruct the robot to move one square to the left, right, up or down in the grid. The robot will ignore a command (but continue with future commands) if the command would cause it to leave the grid or to run into an obstacle. If the robot were to reach the goal position, it immediately stops its program with success (even if further commands exist).

Your friend has already programmed the robot with a command string, but the problem is that your friend is not a very good programmer, and so it may be that the commands do not lead the robot successfully to the goal. You would like to fix the string so that the robot will reach the goal, but you do not want your friend to feel bad, so you are hoping to make as few changes to the program as are needed. A single change consists either of deleting an arbitrary character of the command string, or inserting an arbitrary command anywhere within the string.

As an example, if we consider Sample Input 1, we see that your friend’s command string of DRRDD does not succeed. The initial D moves the robot one spot down. From there, the R (and the subsequent R) are ignored because of the obstacle to the robot’s right. The subsequent D moves the robot down once again and the final D is ignored. However, by deleting the initial D, we can rely on the command string RRDD which does successfully lead the robot to the goal.

If we consider Sample Input 2, we find that your friend’s original command string LDLDLLDR is flawed. However, if we insert the single command U after the fifth command, the resulting string LDLDLULDR successfully guides the robot to the goal. It starts by moving left-down-left; the next down command is ignored because the robot is not allowed to leave the grid. The subsequent left-up-left completes the path to the goal (and the final DR commands are ignored as the robot stops immediately upon reaching the goal).

With Sample Input 3, your friend’s command string can be corrected with two changes, for example with the new command ULDLDLLDLR (although this is not the only way to use two changes to produce a valid sequence).

-----Input-----
The first line of the input contains the two integers $H$ and $W$ that respectively define the height and width of the grid such that $1 \le H, W \le 50$. The next $H$ lines each has $W$ characters, describing the corresponding row of the grid, such that the character ’S’ designates the starting location, ’G’ designates the goal location, ’#’ designates an obstacle, and ’.’ designates an empty location. There will always be precisely one ’S’ and one ’G’ in the grid, and there will always exist an unobstructed path from the start position to the goal position. The final line of the input contains your friend’s original command string consisting of between $1$ and $50$ characters, inclusive.

-----Output-----
Output a single integer indicating the minimum number of changes that are needed to fix the program.

-----Examples-----
Sample Input 1:
3 3
S..
.#.
..G
DRRDD
Sample Output 1:
1

Sample Input 2:
3 7
.......
.G.#.S.
.......
LDLDLLDR
Sample Output 2:
1

Sample Input 3:
3 7
.#.....
.G.##S.
.......
LDLDLLDR
Sample Output 3:
2
````

#### Less-explicit prompt

````text
Your friend just bought a new programmable robot and has asked for your help. The robot operates in a 2D grid that may contain obstacles. The environment has a known start location and a known goal location. The robot is controlled with a string consisting of commands L, R, U, and D, which respectively instruct the robot to move one square to the left, right, up or down in the grid. The robot will ignore a command (but continue with future commands) if the command would cause it to leave the grid or to run into an obstacle. If the robot were to reach the goal position, it immediately stops its program with success (even if further commands exist).

Your friend has already programmed the robot with a command string, but the problem is that your friend is not a very good programmer, and so it may be that the commands do not lead the robot successfully to the goal. You want the command sequence to reach the goal while disturbing as little of your friend’s program as possible. A single change consists either of deleting an arbitrary character of the command string, or inserting an arbitrary command anywhere within the string.

As an example, if we consider Sample Input 1, we see that your friend’s command string of DRRDD does not succeed. The initial D moves the robot one spot down. From there, the R (and the subsequent R) are ignored because of the obstacle to the robot’s right. The subsequent D moves the robot down once again and the final D is ignored. However, by deleting the initial D, we can rely on the command string RRDD which does successfully lead the robot to the goal.

If we consider Sample Input 2, we find that your friend’s original command string LDLDLLDR is flawed. However, if we insert the single command U after the fifth command, the resulting string LDLDLULDR successfully guides the robot to the goal. It starts by moving left-down-left; the next down command is ignored because the robot is not allowed to leave the grid. The subsequent left-up-left completes the path to the goal (and the final DR commands are ignored as the robot stops immediately upon reaching the goal).

With Sample Input 3, your friend’s command string can be corrected with two changes, for example with the new command ULDLDLLDLR (although this is not the only way to use two changes to produce a valid sequence).

-----Input-----
The first line of the input contains the two integers $H$ and $W$ that respectively define the height and width of the grid such that $1 \le H, W \le 50$. The next $H$ lines each has $W$ characters, describing the corresponding row of the grid, such that the character ’S’ designates the starting location, ’G’ designates the goal location, ’#’ designates an obstacle, and ’.’ designates an empty location. There will always be precisely one ’S’ and one ’G’ in the grid, and there will always exist an unobstructed path from the start position to the goal position. The final line of the input contains your friend’s original command string consisting of between $1$ and $50$ characters, inclusive.

-----Output-----
Output a single integer indicating the minimum number of changes that are needed to fix the program.

-----Examples-----
Sample Input 1:
3 3
S..
.#.
..G
DRRDD
Sample Output 1:
1

Sample Input 2:
3 7
.......
.G.#.S.
.......
LDLDLLDR
Sample Output 2:
1

Sample Input 3:
3 7
.#.....
.G.##S.
.......
LDLDLLDR
Sample Output 3:
2
````