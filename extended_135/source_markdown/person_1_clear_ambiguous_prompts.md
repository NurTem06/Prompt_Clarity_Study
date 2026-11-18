# Extended Dataset — Person 1 (N = 45 Tasks)

Распределение: по 15 задач каждого уровня сложности (Introductory, Interview, Competition).

---

## Task 1: Problem ID 4015 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1141/A](https://codeforces.com/problemset/problem/1141/A)

### Clear Prompt (Canonical Baseline)
```text
Polycarp plays "Game 23". Initially he has a number $n$ and his goal is to transform it to $m$. In one move, he can multiply $n$ by $2$ or multiply $n$ by $3$. He can perform any number of moves.

Print the number of moves needed to transform $n$ to $m$. Print -1 if it is impossible to do so.

It is easy to prove that any way to transform $n$ to $m$ contains the same number of moves (i.e. number of moves doesn't depend on the way of transformation).


-----Input-----

The only line of the input contains two integers $n$ and $m$ ($1 \le n \le m \le 5\cdot10^8$).


-----Output-----

Print the number of moves to transform $n$ to $m$, or -1 if there is no solution.


-----Examples-----
Input
120 51840

Output
7

Input
42 42

Output
0

Input
48 72

Output
-1



-----Note-----

In the first example, the possible sequence of moves is: $120 \rightarrow 240 \rightarrow 720 \rightarrow 1440 \rightarrow 4320 \rightarrow 12960 \rightarrow 25920 \rightarrow 51840.$ The are $7$ steps in total.

In the second example, no moves are needed. Thus, the answer is $0$.

In the third example, it is impossible to transform $48$ to $72$.
```

### Ambiguous Promt
```text
I have two numbers n and m, i need to turn the first number into the second one and In one move, i can multiply my current number by 2 or by 3 and i can do this as many times as i want, anyway write a program to calculate how many moves it takes to transform n to m.

-----Input-----

The only line of the input contains two integers $n$ and $m$ ($1 \le n \le m \le 5\cdot10^8$).


-----Output-----

Print the number of moves to transform $n$ to $m$, or -1 if there is no solution.


-----Examples-----
Input
120 51840

Output
7

Input
42 42

Output
0

Input
48 72

Output
-1



-----Note-----

In the first example, the possible sequence of moves is: $120 \rightarrow 240 \rightarrow 720 \rightarrow 1440 \rightarrow 4320 \rightarrow 12960 \rightarrow 25920 \rightarrow 51840.$ The are $7$ steps in total.

In the second example, no moves are needed. Thus, the answer is $0$.

In the third example, it is impossible to transform $48$ to $72$.
```

---

## Task 2: Problem ID 4016 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1029/A](https://codeforces.com/problemset/problem/1029/A)

### Clear Prompt (Canonical Baseline)
```text
You are given a string $t$ consisting of $n$ lowercase Latin letters and an integer number $k$.

Let's define a substring of some string $s$ with indices from $l$ to $r$ as $s[l \dots r]$.

Your task is to construct such string $s$ of minimum possible length that there are exactly $k$ positions $i$ such that $s[i \dots i + n - 1] = t$. In other words, your task is to construct such string $s$ of minimum possible length that there are exactly $k$ substrings of $s$ equal to $t$.

It is guaranteed that the answer is always unique.


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n, k \le 50$) — the length of the string $t$ and the number of substrings.

The second line of the input contains the string $t$ consisting of exactly $n$ lowercase Latin letters.


-----Output-----

Print such string $s$ of minimum possible length that there are exactly $k$ substrings of $s$ equal to $t$.

It is guaranteed that the answer is always unique.


-----Examples-----
Input
3 4
aba

Output
ababababa

Input
3 2
cat

Output
catcat
```

### Ambiguous Promt
```text
i have a string t of lenght n and a number k, i need to make a new string s with the smallest lenght possible so that t appears inside it as a substring exactly k times and they can overlap if needed, anyway write a program to build this string s.

-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n, k \le 50$) — the length of the string $t$ and the number of substrings.

The second line of the input contains the string $t$ consisting of exactly $n$ lowercase Latin letters.


-----Output-----

Print such string $s$ of minimum possible length that there are exactly $k$ substrings of $s$ equal to $t$.

It is guaranteed that the answer is always unique.


-----Examples-----
Input
3 4
aba

Output
ababababa

Input
3 2
cat

Output
catcat
```

---

## Task 3: Problem ID 4017 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1077/C](https://codeforces.com/problemset/problem/1077/C)

### Clear Prompt (Canonical Baseline)
```text
Let's call an array good if there is an element in the array that equals to the sum of all other elements. For example, the array $a=[1, 3, 3, 7]$ is good because there is the element $a_4=7$ which equals to the sum $1 + 3 + 3$.

You are given an array $a$ consisting of $n$ integers. Your task is to print all indices $j$ of this array such that after removing the $j$-th element from the array it will be good (let's call such indices nice).

For example, if $a=[8, 3, 5, 2]$, the nice indices are $1$ and $4$:   if you remove $a_1$, the array will look like $[3, 5, 2]$ and it is good;  if you remove $a_4$, the array will look like $[8, 3, 5]$ and it is good. 

You have to consider all removals independently, i. e. remove the element, check if the resulting array is good, and return the element into the array.


-----Input-----

The first line of the input contains one integer $n$ ($2 \le n \le 2 \cdot 10^5$) — the number of elements in the array $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^6$) — elements of the array $a$.


-----Output-----

In the first line print one integer $k$ — the number of indices $j$ of the array $a$ such that after removing the $j$-th element from the array it will be good (i.e. print the number of the nice indices).

In the second line print $k$ distinct integers $j_1, j_2, \dots, j_k$ in any order — nice indices of the array $a$.

If there are no such indices in the array $a$, just print $0$ in the first line and leave the second line empty or do not print it at all.


-----Examples-----
Input
5
2 5 1 2 2

Output
3
4 1 5
Input
4
8 3 5 2

Output
2
1 4 

Input
5
2 1 2 4 3

Output
0




-----Note-----

In the first example you can remove any element with the value $2$ so the array will look like $[5, 1, 2, 2]$. The sum of this array is $10$ and there is an element equals to the sum of remaining elements ($5 = 1 + 2 + 2$).

In the second example you can remove $8$ so the array will look like $[3, 5, 2]$. The sum of this array is $10$ and there is an element equals to the sum of remaining elements ($5 = 3 + 2$). You can also remove $2$ so the array will look like $[8, 3, 5]$. The sum of this array is $16$ and there is an element equals to the sum of remaining elements ($8 = 3 + 5$).

In the third example you cannot make the given array good by removing exactly one element.
```

### Ambiguous Promt
```text
so i have an array of n numbers and i want to find wich indices i can remove one by one so that in the remaining array one element equals the sum of all the other elements left, anyway write a code to print how many such good indices exist and list them.

-----Input-----

The first line of the input contains one integer $n$ ($2 \le n \le 2 \cdot 10^5$) — the number of elements in the array $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^6$) — elements of the array $a$.


-----Output-----

In the first line print one integer $k$ — the number of indices $j$ of the array $a$ such that after removing the $j$-th element from the array it will be good (i.e. print the number of the nice indices).

In the second line print $k$ distinct integers $j_1, j_2, \dots, j_k$ in any order — nice indices of the array $a$.

If there are no such indices in the array $a$, just print $0$ in the first line and leave the second line empty or do not print it at all.


-----Examples-----
Input
5
2 5 1 2 2

Output
3
4 1 5
Input
4
8 3 5 2

Output
2
1 4 

Input
5
2 1 2 4 3

Output
0




-----Note-----

In the first example you can remove any element with the value $2$ so the array will look like $[5, 1, 2, 2]$. The sum of this array is $10$ and there is an element equals to the sum of remaining elements ($5 = 1 + 2 + 2$).

In the second example you can remove $8$ so the array will look like $[3, 5, 2]$. The sum of this array is $10$ and there is an element equals to the sum of remaining elements ($5 = 3 + 2$). You can also remove $2$ so the array will look like $[8, 3, 5]$. The sum of this array is $16$ and there is an element equals to the sum of remaining elements ($8 = 3 + 5$).

In the third example you cannot make the given array good by removing exactly one element.
```

---

## Task 4: Problem ID 4018 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1183/H](https://codeforces.com/problemset/problem/1183/H)

### Clear Prompt (Canonical Baseline)
```text
The only difference between the easy and the hard versions is constraints.

A subsequence is a string that can be derived from another string by deleting some or no symbols without changing the order of the remaining symbols. Characters to be deleted are not required to go successively, there can be any gaps between them. For example, for the string "abaca" the following strings are subsequences: "abaca", "aba", "aaa", "a" and "" (empty string). But the following strings are not subsequences: "aabaca", "cb" and "bcaa".

You are given a string $s$ consisting of $n$ lowercase Latin letters.

In one move you can take any subsequence $t$ of the given string and add it to the set $S$. The set $S$ can't contain duplicates. This move costs $n - |t|$, where $|t|$ is the length of the added subsequence (i.e. the price equals to the number of the deleted characters).

Your task is to find out the minimum possible total cost to obtain a set $S$ of size $k$ or report that it is impossible to do so.


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n \le 100, 1 \le k \le 10^{12}$) — the length of the string and the size of the set, correspondingly.

The second line of the input contains a string $s$ consisting of $n$ lowercase Latin letters.


-----Output-----

Print one integer — if it is impossible to obtain the set $S$ of size $k$, print -1. Otherwise, print the minimum possible total cost to do it.


-----Examples-----
Input
4 5
asdf

Output
4

Input
5 6
aaaaa

Output
15

Input
5 7
aaaaa

Output
-1

Input
10 100
ajihiushda

Output
233



-----Note-----

In the first example we can generate $S$ = { "asdf", "asd", "adf", "asf", "sdf" }. The cost of the first element in $S$ is $0$ and the cost of the others is $1$. So the total cost of $S$ is $4$.
```

### Ambiguous Promt
```text
i got a string s of lenght n and i need to pick k different subsequences from it by deleting some letters and each subsequence costs however many letters i deleted from s, anyway write a program to find the minimum total cost to collect k unique subsequences.

-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n \le 100, 1 \le k \le 10^{12}$) — the length of the string and the size of the set, correspondingly.

The second line of the input contains a string $s$ consisting of $n$ lowercase Latin letters.


-----Output-----

Print one integer — if it is impossible to obtain the set $S$ of size $k$, print -1. Otherwise, print the minimum possible total cost to do it.


-----Examples-----
Input
4 5
asdf

Output
4

Input
5 6
aaaaa

Output
15

Input
5 7
aaaaa

Output
-1

Input
10 100
ajihiushda

Output
233



-----Note-----

In the first example we can generate $S$ = { "asdf", "asd", "adf", "asf", "sdf" }. The cost of the first element in $S$ is $0$ and the cost of the others is $1$. So the total cost of $S$ is $4$.
```

---

## Task 5: Problem ID 4019 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1133/F2](https://codeforces.com/problemset/problem/1133/F2)

### Clear Prompt (Canonical Baseline)
```text
You are given an undirected unweighted connected graph consisting of $n$ vertices and $m$ edges. It is guaranteed that there are no self-loops or multiple edges in the given graph.

Your task is to find any spanning tree of this graph such that the degree of the first vertex (vertex with label $1$ on it) is equal to $D$ (or say that there are no such spanning trees). Recall that the degree of a vertex is the number of edges incident to it.


-----Input-----

The first line contains three integers $n$, $m$ and $D$ ($2 \le n \le 2 \cdot 10^5$, $n - 1 \le m \le min(2 \cdot 10^5, \frac{n(n-1)}{2}), 1 \le D < n$) — the number of vertices, the number of edges and required degree of the first vertex, respectively.

The following $m$ lines denote edges: edge $i$ is represented by a pair of integers $v_i$, $u_i$ ($1 \le v_i, u_i \le n$, $u_i \ne v_i$), which are the indices of vertices connected by the edge. There are no loops or multiple edges in the given graph, i. e. for each pair ($v_i, u_i$) there are no other pairs ($v_i, u_i$) or ($u_i, v_i$) in the list of edges, and for each pair $(v_i, u_i)$ the condition $v_i \ne u_i$ is satisfied.


-----Output-----

If there is no spanning tree satisfying the condition from the problem statement, print "NO" in the first line.

Otherwise print "YES" in the first line and then print $n-1$ lines describing the edges of a spanning tree such that the degree of the first vertex (vertex with label $1$ on it) is equal to $D$. Make sure that the edges of the printed spanning tree form some subset of the input edges (order doesn't matter and edge $(v, u)$ is considered the same as the edge $(u, v)$).

If there are multiple possible answers, print any of them.


-----Examples-----
Input
4 5 1
1 2
1 3
1 4
2 3
3 4

Output
YES
2 1
2 3
3 4

Input
4 5 3
1 2
1 3
1 4
2 3
3 4

Output
YES
1 2
1 3
4 1

Input
4 4 3
1 2
1 4
2 3
3 4

Output
NO



-----Note-----

The picture corresponding to the first and second examples: [Image]

The picture corresponding to the third example: [Image]
```

### Ambiguous Promt
```text
i have a connected undirected graph with n nodes and m edges and i need to build a spanning tree where node 1 has exacty D edges connected to it, anyway write a program to find any spanning tree like that or say if its impossible.

-----Input-----

The first line contains three integers $n$, $m$ and $D$ ($2 \le n \le 2 \cdot 10^5$, $n - 1 \le m \le min(2 \cdot 10^5, \frac{n(n-1)}{2}), 1 \le D < n$) — the number of vertices, the number of edges and required degree of the first vertex, respectively.

The following $m$ lines denote edges: edge $i$ is represented by a pair of integers $v_i$, $u_i$ ($1 \le v_i, u_i \le n$, $u_i \ne v_i$), which are the indices of vertices connected by the edge. There are no loops or multiple edges in the given graph, i. e. for each pair ($v_i, u_i$) there are no other pairs ($v_i, u_i$) or ($u_i, v_i$) in the list of edges, and for each pair $(v_i, u_i)$ the condition $v_i \ne u_i$ is satisfied.


-----Output-----

If there is no spanning tree satisfying the condition from the problem statement, print "NO" in the first line.

Otherwise print "YES" in the first line and then print $n-1$ lines describing the edges of a spanning tree such that the degree of the first vertex (vertex with label $1$ on it) is equal to $D$. Make sure that the edges of the printed spanning tree form some subset of the input edges (order doesn't matter and edge $(v, u)$ is considered the same as the edge $(u, v)$).

If there are multiple possible answers, print any of them.


-----Examples-----
Input
4 5 1
1 2
1 3
1 4
2 3
3 4

Output
YES
2 1
2 3
3 4

Input
4 5 3
1 2
1 3
1 4
2 3
3 4

Output
YES
1 2
1 3
4 1

Input
4 4 3
1 2
1 4
2 3
3 4

Output
NO



-----Note-----

The picture corresponding to the first and second examples: [Image]

The picture corresponding to the third example: [Image]
```

---

## Task 6: Problem ID 4020 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1133/A](https://codeforces.com/problemset/problem/1133/A)

### Clear Prompt (Canonical Baseline)
```text
Polycarp is going to participate in the contest. It starts at $h_1:m_1$ and ends at $h_2:m_2$. It is guaranteed that the contest lasts an even number of minutes (i.e. $m_1 \% 2 = m_2 \% 2$, where $x \% y$ is $x$ modulo $y$). It is also guaranteed that the entire contest is held during a single day. And finally it is guaranteed that the contest lasts at least two minutes.

Polycarp wants to know the time of the midpoint of the contest. For example, if the contest lasts from $10:00$ to $11:00$ then the answer is $10:30$, if the contest lasts from $11:10$ to $11:12$ then the answer is $11:11$.


-----Input-----

The first line of the input contains two integers $h_1$ and $m_1$ in the format hh:mm.

The second line of the input contains two integers $h_2$ and $m_2$ in the same format (hh:mm).

It is guaranteed that $0 \le h_1, h_2 \le 23$ and $0 \le m_1, m_2 \le 59$.

It is guaranteed that the contest lasts an even number of minutes (i.e. $m_1 \% 2 = m_2 \% 2$, where $x \% y$ is $x$ modulo $y$). It is also guaranteed that the entire contest is held during a single day. And finally it is guaranteed that the contest lasts at least two minutes.


-----Output-----

Print two integers $h_3$ and $m_3$ ($0 \le h_3 \le 23, 0 \le m_3 \le 59$) corresponding to the midpoint of the contest in the format hh:mm. Print each number as exactly two digits (prepend a number with leading zero if needed), separate them with ':'.


-----Examples-----
Input
10:00
11:00

Output
10:30

Input
11:10
11:12

Output
11:11

Input
01:02
03:02

Output
02:02
```

### Ambiguous Promt
```text
i have a start time and an end time in the same day and i just need to find the exact middle time between them, anyway write a program to calculate and print that midpoint time.

-----Input-----

The first line of the input contains two integers $h_1$ and $m_1$ in the format hh:mm.

The second line of the input contains two integers $h_2$ and $m_2$ in the same format (hh:mm).

It is guaranteed that $0 \le h_1, h_2 \le 23$ and $0 \le m_1, m_2 \le 59$.

It is guaranteed that the contest lasts an even number of minutes (i.e. $m_1 \% 2 = m_2 \% 2$, where $x \% y$ is $x$ modulo $y$). It is also guaranteed that the entire contest is held during a single day. And finally it is guaranteed that the contest lasts at least two minutes.


-----Output-----

Print two integers $h_3$ and $m_3$ ($0 \le h_3 \le 23, 0 \le m_3 \le 59$) corresponding to the midpoint of the contest in the format hh:mm. Print each number as exactly two digits (prepend a number with leading zero if needed), separate them with ':'.


-----Examples-----
Input
10:00
11:00

Output
10:30

Input
11:10
11:12

Output
11:11

Input
01:02
03:02

Output
02:02
```

---

## Task 7: Problem ID 4021 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/409/F](https://codeforces.com/problemset/problem/409/F)

### Clear Prompt (Canonical Baseline)
```text
-----Input-----

The input contains a single integer a (1 ≤ a ≤ 64).


-----Output-----

Output a single integer.


-----Examples-----
Input
2

Output
1

Input
4

Output
2

Input
27

Output
5

Input
42

Output
6
```

### Ambiguous Promt
```text
i dont really have a text description for this one so just look at the input and output examples to figure out the pattern for integer a and write a program that outputs the right integer.

-----Input-----

The input contains a single integer a (1 ≤ a ≤ 64).


-----Output-----

Output a single integer.


-----Examples-----
Input
2

Output
1

Input
4

Output
2

Input
27

Output
5

Input
42

Output
6
```

---

## Task 8: Problem ID 4022 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1029/C](https://codeforces.com/problemset/problem/1029/C)

### Clear Prompt (Canonical Baseline)
```text
You are given $n$ segments on a number line; each endpoint of every segment has integer coordinates. Some segments can degenerate to points. Segments can intersect with each other, be nested in each other or even coincide.

The intersection of a sequence of segments is such a maximal set of points (not necesserily having integer coordinates) that each point lies within every segment from the sequence. If the resulting set isn't empty, then it always forms some continuous segment. The length of the intersection is the length of the resulting segment or $0$ in case the intersection is an empty set.

For example, the intersection of segments $[1;5]$ and $[3;10]$ is $[3;5]$ (length $2$), the intersection of segments $[1;5]$ and $[5;7]$ is $[5;5]$ (length $0$) and the intersection of segments $[1;5]$ and $[6;6]$ is an empty set (length $0$).

Your task is to remove exactly one segment from the given sequence in such a way that the intersection of the remaining $(n - 1)$ segments has the maximal possible length.


-----Input-----

The first line contains a single integer $n$ ($2 \le n \le 3 \cdot 10^5$) — the number of segments in the sequence.

Each of the next $n$ lines contains two integers $l_i$ and $r_i$ ($0 \le l_i \le r_i \le 10^9$) — the description of the $i$-th segment.


-----Output-----

Print a single integer — the maximal possible length of the intersection of $(n - 1)$ remaining segments after you remove exactly one segment from the sequence.


-----Examples-----
Input
4
1 3
2 6
0 4
3 3

Output
1

Input
5
2 6
1 3
0 4
1 20
0 4

Output
2

Input
3
4 5
1 2
9 20

Output
0

Input
2
3 10
1 5

Output
7



-----Note-----

In the first example you should remove the segment $[3;3]$, the intersection will become $[2;3]$ (length $1$). Removing any other segment will result in the intersection $[3;3]$ (length $0$).

In the second example you should remove the segment $[1;3]$ or segment $[2;6]$, the intersection will become $[2;4]$ (length $2$) or $[1;3]$ (length $2$), respectively. Removing any other segment will result in the intersection $[2;3]$ (length $1$).

In the third example the intersection will become an empty set no matter the segment you remove.

In the fourth example you will get the intersection $[3;10]$ (length $7$) if you remove the segment $[1;5]$ or the intersection $[1;5]$ (length $4$) if you remove the segment $[3;10]$.
```

### Ambiguous Promt
```text
i have n line segments with start and end points and i need to delete exacty one segment so that the overlapping part of all the remaining segments has the biggest possible lenght, anyway write a code to find that maximum intersection lenght.

-----Input-----

The first line contains a single integer $n$ ($2 \le n \le 3 \cdot 10^5$) — the number of segments in the sequence.

Each of the next $n$ lines contains two integers $l_i$ and $r_i$ ($0 \le l_i \le r_i \le 10^9$) — the description of the $i$-th segment.


-----Output-----

Print a single integer — the maximal possible length of the intersection of $(n - 1)$ remaining segments after you remove exactly one segment from the sequence.


-----Examples-----
Input
4
1 3
2 6
0 4
3 3

Output
1

Input
5
2 6
1 3
0 4
1 20
0 4

Output
2

Input
3
4 5
1 2
9 20

Output
0

Input
2
3 10
1 5

Output
7



-----Note-----

In the first example you should remove the segment $[3;3]$, the intersection will become $[2;3]$ (length $1$). Removing any other segment will result in the intersection $[3;3]$ (length $0$).

In the second example you should remove the segment $[1;3]$ or segment $[2;6]$, the intersection will become $[2;4]$ (length $2$) or $[1;3]$ (length $2$), respectively. Removing any other segment will result in the intersection $[2;3]$ (length $1$).

In the third example the intersection will become an empty set no matter the segment you remove.

In the fourth example you will get the intersection $[3;10]$ (length $7$) if you remove the segment $[1;5]$ or the intersection $[1;5]$ (length $4$) if you remove the segment $[3;10]$.
```

---

## Task 9: Problem ID 4023 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1092/D2](https://codeforces.com/problemset/problem/1092/D2)

### Clear Prompt (Canonical Baseline)
```text
Vova's family is building the Great Vova Wall (named by Vova himself). Vova's parents, grandparents, grand-grandparents contributed to it. Now it's totally up to Vova to put the finishing touches.

The current state of the wall can be respresented by a sequence $a$ of $n$ integers, with $a_i$ being the height of the $i$-th part of the wall.

Vova can only use $2 \times 1$ bricks to put in the wall (he has infinite supply of them, however).

Vova can put bricks only horizontally on the neighbouring parts of the wall of equal height. It means that if for some $i$ the current height of part $i$ is the same as for part $i + 1$, then Vova can put a brick there and thus increase both heights by 1. Obviously, Vova can't put bricks in such a way that its parts turn out to be off the borders (to the left of part $1$ of the wall or to the right of part $n$ of it).

Note that Vova can't put bricks vertically.

Vova is a perfectionist, so he considers the wall completed when:  all parts of the wall has the same height;  the wall has no empty spaces inside it. 

Can Vova complete the wall using any amount of bricks (possibly zero)?


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of parts in the wall.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^9$) — the initial heights of the parts of the wall.


-----Output-----

Print "YES" if Vova can complete the wall using any amount of bricks (possibly zero).

Print "NO" otherwise.


-----Examples-----
Input
5
2 1 1 2 5

Output
YES

Input
3
4 5 3

Output
NO

Input
2
10 10

Output
YES



-----Note-----

In the first example Vova can put a brick on parts 2 and 3 to make the wall $[2, 2, 2, 2, 5]$ and then put 3 bricks on parts 1 and 2 and 3 bricks on parts 3 and 4 to make it $[5, 5, 5, 5, 5]$.

In the second example Vova can put no bricks in the wall.

In the third example the wall is already complete.
```

### Ambiguous Promt
```text
i have an array of n heights representing a wall and i can only place 2x1 bricks flat across two adjacent columns if they currently have the exact same height wich raises both by 1, anyway write a program to check if i can make all columns the exact same height without leaving gaps.

-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of parts in the wall.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^9$) — the initial heights of the parts of the wall.


-----Output-----

Print "YES" if Vova can complete the wall using any amount of bricks (possibly zero).

Print "NO" otherwise.


-----Examples-----
Input
5
2 1 1 2 5

Output
YES

Input
3
4 5 3

Output
NO

Input
2
10 10

Output
YES



-----Note-----

In the first example Vova can put a brick on parts 2 and 3 to make the wall $[2, 2, 2, 2, 5]$ and then put 3 bricks on parts 1 and 2 and 3 bricks on parts 3 and 4 to make it $[5, 5, 5, 5, 5]$.

In the second example Vova can put no bricks in the wall.

In the third example the wall is already complete.
```

---

## Task 10: Problem ID 4024 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1183/E](https://codeforces.com/problemset/problem/1183/E)

### Clear Prompt (Canonical Baseline)
```text
The only difference between the easy and the hard versions is constraints.

A subsequence is a string that can be derived from another string by deleting some or no symbols without changing the order of the remaining symbols. Characters to be deleted are not required to go successively, there can be any gaps between them. For example, for the string "abaca" the following strings are subsequences: "abaca", "aba", "aaa", "a" and "" (empty string). But the following strings are not subsequences: "aabaca", "cb" and "bcaa".

You are given a string $s$ consisting of $n$ lowercase Latin letters.

In one move you can take any subsequence $t$ of the given string and add it to the set $S$. The set $S$ can't contain duplicates. This move costs $n - |t|$, where $|t|$ is the length of the added subsequence (i.e. the price equals to the number of the deleted characters).

Your task is to find out the minimum possible total cost to obtain a set $S$ of size $k$ or report that it is impossible to do so.


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n, k \le 100$) — the length of the string and the size of the set, correspondingly.

The second line of the input contains a string $s$ consisting of $n$ lowercase Latin letters.


-----Output-----

Print one integer — if it is impossible to obtain the set $S$ of size $k$, print -1. Otherwise, print the minimum possible total cost to do it.


-----Examples-----
Input
4 5
asdf

Output
4

Input
5 6
aaaaa

Output
15

Input
5 7
aaaaa

Output
-1

Input
10 100
ajihiushda

Output
233



-----Note-----

In the first example we can generate $S$ = { "asdf", "asd", "adf", "asf", "sdf" }. The cost of the first element in $S$ is $0$ and the cost of the others is $1$. So the total cost of $S$ is $4$.
```

### Ambiguous Promt
```text
so i have a string s of lenght n and i want to build a set of k unique subsequences by removing characters from s and each one costs the number of deleted characters, anyway write a code to find the minimum total cost to get k distinct subsequences.

-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n, k \le 100$) — the length of the string and the size of the set, correspondingly.

The second line of the input contains a string $s$ consisting of $n$ lowercase Latin letters.


-----Output-----

Print one integer — if it is impossible to obtain the set $S$ of size $k$, print -1. Otherwise, print the minimum possible total cost to do it.


-----Examples-----
Input
4 5
asdf

Output
4

Input
5 6
aaaaa

Output
15

Input
5 7
aaaaa

Output
-1

Input
10 100
ajihiushda

Output
233



-----Note-----

In the first example we can generate $S$ = { "asdf", "asd", "adf", "asf", "sdf" }. The cost of the first element in $S$ is $0$ and the cost of the others is $1$. So the total cost of $S$ is $4$.
```

---

## Task 11: Problem ID 4025 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1154/C](https://codeforces.com/problemset/problem/1154/C)

### Clear Prompt (Canonical Baseline)
```text
Polycarp has a cat and his cat is a real gourmet! Dependent on a day of the week he eats certain type of food:  on Mondays, Thursdays and Sundays he eats fish food;  on Tuesdays and Saturdays he eats rabbit stew;  on other days of week he eats chicken stake. 

Polycarp plans to go on a trip and already packed his backpack. His backpack contains:  $a$ daily rations of fish food;  $b$ daily rations of rabbit stew;  $c$ daily rations of chicken stakes. 

Polycarp has to choose such day of the week to start his trip that his cat can eat without additional food purchases as long as possible. Print the maximum number of days the cat can eat in a trip without additional food purchases, if Polycarp chooses the day of the week to start his trip optimally.


-----Input-----

The first line of the input contains three positive integers $a$, $b$ and $c$ ($1 \le a, b, c \le 7\cdot10^8$) — the number of daily rations of fish food, rabbit stew and chicken stakes in Polycarps backpack correspondingly.


-----Output-----

Print the maximum number of days the cat can eat in a trip without additional food purchases, if Polycarp chooses the day of the week to start his trip optimally.


-----Examples-----
Input
2 1 1

Output
4

Input
3 2 2

Output
7

Input
1 100 1

Output
3

Input
30 20 10

Output
39



-----Note-----

In the first example the best day for start of the trip is Sunday. In this case, during Sunday and Monday the cat will eat fish food, during Tuesday — rabbit stew and during Wednesday — chicken stake. So, after four days of the trip all food will be eaten.

In the second example Polycarp can start his trip in any day of the week. In any case there are food supplies only for one week in Polycarps backpack.

In the third example Polycarp can start his trip in any day, excluding Wednesday, Saturday and Sunday. In this case, the cat will eat three different dishes in three days. Nevertheless that after three days of a trip there will be $99$ portions of rabbit stew in a backpack, can cannot eat anything in fourth day of a trip.
```

### Ambiguous Promt
```text
i have a, b, and c portions of three types of cat food and a cat eats fish on mon thu sun, rabbit on tue sat, and chicken on wed fri, anyway write a program to find the max number of days the cat can eat if i pick the best day of the week to start.

-----Input-----

The first line of the input contains three positive integers $a$, $b$ and $c$ ($1 \le a, b, c \le 7\cdot10^8$) — the number of daily rations of fish food, rabbit stew and chicken stakes in Polycarps backpack correspondingly.


-----Output-----

Print the maximum number of days the cat can eat in a trip without additional food purchases, if Polycarp chooses the day of the week to start his trip optimally.


-----Examples-----
Input
2 1 1

Output
4

Input
3 2 2

Output
7

Input
1 100 1

Output
3

Input
30 20 10

Output
39



-----Note-----

In the first example the best day for start of the trip is Sunday. In this case, during Sunday and Monday the cat will eat fish food, during Tuesday — rabbit stew and during Wednesday — chicken stake. So, after four days of the trip all food will be eaten.

In the second example Polycarp can start his trip in any day of the week. In any case there are food supplies only for one week in Polycarps backpack.

In the third example Polycarp can start his trip in any day, excluding Wednesday, Saturday and Sunday. In this case, the cat will eat three different dishes in three days. Nevertheless that after three days of a trip there will be $99$ portions of rabbit stew in a backpack, can cannot eat anything in fourth day of a trip.
```

---

## Task 12: Problem ID 4026 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1426/B](https://codeforces.com/problemset/problem/1426/B)

### Clear Prompt (Canonical Baseline)
```text
Masha has $n$ types of tiles of size $2 \times 2$. Each cell of the tile contains one integer. Masha has an infinite number of tiles of each type.

Masha decides to construct the square of size $m \times m$ consisting of the given tiles. This square also has to be a symmetric with respect to the main diagonal matrix, and each cell of this square has to be covered with exactly one tile cell, and also sides of tiles should be parallel to the sides of the square. All placed tiles cannot intersect with each other. Also, each tile should lie inside the square. See the picture in Notes section for better understanding.

Symmetric with respect to the main diagonal matrix is such a square $s$ that for each pair $(i, j)$ the condition $s[i][j] = s[j][i]$ holds. I.e. it is true that the element written in the $i$-row and $j$-th column equals to the element written in the $j$-th row and $i$-th column.

Your task is to determine if Masha can construct a square of size $m \times m$ which is a symmetric matrix and consists of tiles she has. Masha can use any number of tiles of each type she has to construct the square. Note that she can not rotate tiles, she can only place them in the orientation they have in the input.

You have to answer $t$ independent test cases.


-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 100$) — the number of test cases. Then $t$ test cases follow.

The first line of the test case contains two integers $n$ and $m$ ($1 \le n \le 100$, $1 \le m \le 100$) — the number of types of tiles and the size of the square Masha wants to construct.

The next $2n$ lines of the test case contain descriptions of tiles types. Types of tiles are written one after another, each type is written on two lines. 

The first line of the description contains two positive (greater than zero) integers not exceeding $100$ — the number written in the top left corner of the tile and the number written in the top right corner of the tile of the current type. The second line of the description contains two positive (greater than zero) integers not exceeding $100$ — the number written in the bottom left corner of the tile and the number written in the bottom right corner of the tile of the current type.

It is forbidden to rotate tiles, it is only allowed to place them in the orientation they have in the input.


-----Output-----

For each test case print the answer: "YES" (without quotes) if Masha can construct the square of size $m \times m$ which is a symmetric matrix. Otherwise, print "NO" (withtout quotes).


-----Example-----
Input
6
3 4
1 2
5 6
5 7
7 4
8 9
9 8
2 5
1 1
1 1
2 2
2 2
1 100
10 10
10 10
1 2
4 5
8 4
2 2
1 1
1 1
1 2
3 4
1 2
1 1
1 1

Output
YES
NO
YES
NO
YES
YES



-----Note-----

The first test case of the input has three types of tiles, they are shown on the picture below. [Image] 

Masha can construct, for example, the following square of size $4 \times 4$ which is a symmetric matrix: $\left. \begin{array}{|c|c|c|c|} \hline 5 & {7} & {8} & {9} \\ \hline 7 & {4} & {9} & {8} \\ \hline 8 & {9} & {5} & {7} \\ \hline 9 & {8} & {7} & {4} \\ \hline \end{array} \right.$
```

### Ambiguous Promt
```text
i have n types of 2x2 tiles with numbers in them and unlimited copies of each and i want to tile an mxm square without rotating or overlapping them so that the whole grid is symetric across the main diagonal, anyway write a program to check if its possible for each test case.

-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 100$) — the number of test cases. Then $t$ test cases follow.

The first line of the test case contains two integers $n$ and $m$ ($1 \le n \le 100$, $1 \le m \le 100$) — the number of types of tiles and the size of the square Masha wants to construct.

The next $2n$ lines of the test case contain descriptions of tiles types. Types of tiles are written one after another, each type is written on two lines. 

The first line of the description contains two positive (greater than zero) integers not exceeding $100$ — the number written in the top left corner of the tile and the number written in the top right corner of the tile of the current type. The second line of the description contains two positive (greater than zero) integers not exceeding $100$ — the number written in the bottom left corner of the tile and the number written in the bottom right corner of the tile of the current type.

It is forbidden to rotate tiles, it is only allowed to place them in the orientation they have in the input.


-----Output-----

For each test case print the answer: "YES" (without quotes) if Masha can construct the square of size $m \times m$ which is a symmetric matrix. Otherwise, print "NO" (withtout quotes).


-----Example-----
Input
6
3 4
1 2
5 6
5 7
7 4
8 9
9 8
2 5
1 1
1 1
2 2
2 2
1 100
10 10
10 10
1 2
4 5
8 4
2 2
1 1
1 1
1 2
3 4
1 2
1 1
1 1

Output
YES
NO
YES
NO
YES
YES



-----Note-----

The first test case of the input has three types of tiles, they are shown on the picture below. [Image] 

Masha can construct, for example, the following square of size $4 \times 4$ which is a symmetric matrix: $\left. \begin{array}{|c|c|c|c|} \hline 5 & {7} & {8} & {9} \\ \hline 7 & {4} & {9} & {8} \\ \hline 8 & {9} & {5} & {7} \\ \hline 9 & {8} & {7} & {4} \\ \hline \end{array} \right.$
```

---

## Task 13: Problem ID 4027 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1102/A](https://codeforces.com/problemset/problem/1102/A)

### Clear Prompt (Canonical Baseline)
```text
You are given an integer sequence $1, 2, \dots, n$. You have to divide it into two sets $A$ and $B$ in such a way that each element belongs to exactly one set and $|sum(A) - sum(B)|$ is minimum possible.

The value $|x|$ is the absolute value of $x$ and $sum(S)$ is the sum of elements of the set $S$.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^9$).


-----Output-----

Print one integer — the minimum possible value of $|sum(A) - sum(B)|$ if you divide the initial sequence $1, 2, \dots, n$ into two sets $A$ and $B$.


-----Examples-----
Input
3

Output
0

Input
5

Output
1

Input
6

Output
1



-----Note-----

Some (not all) possible answers to examples:

In the first example you can divide the initial sequence into sets $A = \{1, 2\}$ and $B = \{3\}$ so the answer is $0$.

In the second example you can divide the initial sequence into sets $A = \{1, 3, 4\}$ and $B = \{2, 5\}$ so the answer is $1$.

In the third example you can divide the initial sequence into sets $A = \{1, 4, 5\}$ and $B = \{2, 3, 6\}$ so the answer is $1$.
```

### Ambiguous Promt
```text
i have numbers from 1 to n and i want to split them into two groups so the absolute difference between their sums is as small as posible, anyway write a code to find that minimum difference.

-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^9$).


-----Output-----

Print one integer — the minimum possible value of $|sum(A) - sum(B)|$ if you divide the initial sequence $1, 2, \dots, n$ into two sets $A$ and $B$.


-----Examples-----
Input
3

Output
0

Input
5

Output
1

Input
6

Output
1



-----Note-----

Some (not all) possible answers to examples:

In the first example you can divide the initial sequence into sets $A = \{1, 2\}$ and $B = \{3\}$ so the answer is $0$.

In the second example you can divide the initial sequence into sets $A = \{1, 3, 4\}$ and $B = \{2, 5\}$ so the answer is $1$.

In the third example you can divide the initial sequence into sets $A = \{1, 4, 5\}$ and $B = \{2, 3, 6\}$ so the answer is $1$.
```

---

## Task 14: Problem ID 4028 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1015/F](https://codeforces.com/problemset/problem/1015/F)

### Clear Prompt (Canonical Baseline)
```text
You are given a bracket sequence $s$ (not necessarily a regular one). A bracket sequence is a string containing only characters '(' and ')'.

A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters '1' and '+' between the original characters of the sequence. For example, bracket sequences "()()" and "(())" are regular (the resulting expressions are: "(1)+(1)" and "((1+1)+1)"), and ")(", "(" and ")" are not.

Your problem is to calculate the number of regular bracket sequences of length $2n$ containing the given bracket sequence $s$ as a substring (consecutive sequence of characters) modulo $10^9+7$ ($1000000007$).


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the half-length of the resulting regular bracket sequences (the resulting sequences must have length equal to $2n$).

The second line of the input contains one string $s$ ($1 \le |s| \le 200$) — the string $s$ that should be a substring in each of the resulting regular bracket sequences ($|s|$ is the length of $s$).


-----Output-----

Print only one integer — the number of regular bracket sequences containing the given bracket sequence $s$ as a substring. Since this number can be huge, print it modulo $10^9+7$ ($1000000007$).


-----Examples-----
Input
5
()))()

Output
5

Input
3
(()

Output
4

Input
2
(((

Output
0



-----Note-----

All regular bracket sequences satisfying the conditions above for the first example:   "(((()))())";  "((()()))()";  "((()))()()";  "(()(()))()";  "()((()))()". 

All regular bracket sequences satisfying the conditions above for the second example:   "((()))";  "(()())";  "(())()";  "()(())". 

And there is no regular bracket sequences of length $4$ containing "(((" as a substring in the third example.
```

### Ambiguous Promt
```text
i got a string s made of brackets and a number n, i need to count how many valid balanced bracket strings of total lenght 2n contain s inside them as a continuous substring, anyway write a program to print this count modulo 1000000007.

-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 100$) — the half-length of the resulting regular bracket sequences (the resulting sequences must have length equal to $2n$).

The second line of the input contains one string $s$ ($1 \le |s| \le 200$) — the string $s$ that should be a substring in each of the resulting regular bracket sequences ($|s|$ is the length of $s$).


-----Output-----

Print only one integer — the number of regular bracket sequences containing the given bracket sequence $s$ as a substring. Since this number can be huge, print it modulo $10^9+7$ ($1000000007$).


-----Examples-----
Input
5
()))()

Output
5

Input
3
(()

Output
4

Input
2
(((

Output
0



-----Note-----

All regular bracket sequences satisfying the conditions above for the first example:   "(((()))())";  "((()()))()";  "((()))()()";  "(()(()))()";  "()((()))()". 

All regular bracket sequences satisfying the conditions above for the second example:   "((()))";  "(()())";  "(())()";  "()(())". 

And there is no regular bracket sequences of length $4$ containing "(((" as a substring in the third example.
```

---

## Task 15: Problem ID 4029 (Introductory)
- **Difficulty Tier:** Introductory
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/988/E](https://codeforces.com/problemset/problem/988/E)

### Clear Prompt (Canonical Baseline)
```text
You are given an integer $n$ from $1$ to $10^{18}$ without leading zeroes.

In one move you can swap any two adjacent digits in the given number in such a way that the resulting number will not contain leading zeroes. In other words, after each move the number you have cannot contain any leading zeroes.

What is the minimum number of moves you have to make to obtain a number that is divisible by $25$? Print -1 if it is impossible to obtain a number that is divisible by $25$.


-----Input-----

The first line contains an integer $n$ ($1 \le n \le 10^{18}$). It is guaranteed that the first (left) digit of the number $n$ is not a zero.


-----Output-----

If it is impossible to obtain a number that is divisible by $25$, print -1. Otherwise print the minimum number of moves required to obtain such number.

Note that you can swap only adjacent digits in the given number.


-----Examples-----
Input
5071

Output
4

Input
705

Output
1

Input
1241367

Output
-1



-----Note-----

In the first example one of the possible sequences of moves is 5071 $\rightarrow$ 5701 $\rightarrow$ 7501 $\rightarrow$ 7510 $\rightarrow$ 7150.
```

### Ambiguous Promt
```text
i have a big number n and in one step i can swap two neighbouring digits as long as it doesnt create a leading zero, anyway write a program to find the fewest swaps needed to make the number divisible by 25.

-----Input-----

The first line contains an integer $n$ ($1 \le n \le 10^{18}$). It is guaranteed that the first (left) digit of the number $n$ is not a zero.


-----Output-----

If it is impossible to obtain a number that is divisible by $25$, print -1. Otherwise print the minimum number of moves required to obtain such number.

Note that you can swap only adjacent digits in the given number.


-----Examples-----
Input
5071

Output
4

Input
705

Output
1

Input
1241367

Output
-1



-----Note-----

In the first example one of the possible sequences of moves is 5071 $\rightarrow$ 5701 $\rightarrow$ 7501 $\rightarrow$ 7510 $\rightarrow$ 7150.
```

---

## Task 16: Problem ID 15 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/675/A](https://codeforces.com/problemset/problem/675/A)

### Clear Prompt (Canonical Baseline)
```text
Vasya likes everything infinite. Now he is studying the properties of a sequence s, such that its first element is equal to a (s_1 = a), and the difference between any two neighbouring elements is equal to c (s_{i} - s_{i} - 1 = c). In particular, Vasya wonders if his favourite integer b appears in this sequence, that is, there exists a positive integer i, such that s_{i} = b. Of course, you are the person he asks for a help.


-----Input-----

The first line of the input contain three integers a, b and c ( - 10^9 ≤ a, b, c ≤ 10^9) — the first element of the sequence, Vasya's favorite number and the difference between any two neighbouring elements of the sequence, respectively.


-----Output-----

If b appears in the sequence s print "YES" (without quotes), otherwise print "NO" (without quotes).


-----Examples-----
Input
1 7 3

Output
YES

Input
10 10 0

Output
YES

Input
1 -4 5

Output
NO

Input
0 60 50

Output
NO



-----Note-----

In the first sample, the sequence starts from integers 1, 4, 7, so 7 is its element.

In the second sample, the favorite integer of Vasya is equal to the first element of the sequence.

In the third sample all elements of the sequence are greater than Vasya's favorite integer.

In the fourth sample, the sequence starts from 0, 50, 100, and all the following elements are greater than Vasya's favorite integer.
```

### Ambiguous Promt
```text
i have an infinite arithmetic sequence starting at a where every next number adds c and i want to know if a target number b ever shows up in this sequence, anyway write a code to check if b is in it.

-----Input-----

The first line of the input contain three integers a, b and c ( - 10^9 ≤ a, b, c ≤ 10^9) — the first element of the sequence, Vasya's favorite number and the difference between any two neighbouring elements of the sequence, respectively.


-----Output-----

If b appears in the sequence s print "YES" (without quotes), otherwise print "NO" (without quotes).


-----Examples-----
Input
1 7 3

Output
YES

Input
10 10 0

Output
YES

Input
1 -4 5

Output
NO

Input
0 60 50

Output
NO



-----Note-----

In the first sample, the sequence starts from integers 1, 4, 7, so 7 is its element.

In the second sample, the favorite integer of Vasya is equal to the first element of the sequence.

In the third sample all elements of the sequence are greater than Vasya's favorite integer.

In the fourth sample, the sequence starts from 0, 50, 100, and all the following elements are greater than Vasya's favorite integer.
```

---

## Task 17: Problem ID 16 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1132/A](https://codeforces.com/problemset/problem/1132/A)

### Clear Prompt (Canonical Baseline)
```text
A string is called bracket sequence if it does not contain any characters other than "(" and ")". A bracket sequence is called regular if it it is possible to obtain correct arithmetic expression by inserting characters "+" and "1" into this sequence. For example, "", "(())" and "()()" are regular bracket sequences; "))" and ")((" are bracket sequences (but not regular ones), and "(a)" and "(1)+(1)" are not bracket sequences at all.

You have a number of strings; each string is a bracket sequence of length $2$. So, overall you have $cnt_1$ strings "((", $cnt_2$ strings "()", $cnt_3$ strings ")(" and $cnt_4$ strings "))". You want to write all these strings in some order, one after another; after that, you will get a long bracket sequence of length $2(cnt_1 + cnt_2 + cnt_3 + cnt_4)$. You wonder: is it possible to choose some order of the strings you have such that you will get a regular bracket sequence? Note that you may not remove any characters or strings, and you may not add anything either.


-----Input-----

The input consists of four lines, $i$-th of them contains one integer $cnt_i$ ($0 \le cnt_i \le 10^9$).


-----Output-----

Print one integer: $1$ if it is possible to form a regular bracket sequence by choosing the correct order of the given strings, $0$ otherwise.


-----Examples-----
Input
3
1
4
3

Output
1

Input
0
0
0
0

Output
1

Input
1
2
3
4

Output
0



-----Note-----

In the first example it is possible to construct a string "(())()(()((()()()())))", which is a regular bracket sequence.

In the second example it is possible to construct a string "", which is a regular bracket sequence.
```

### Ambiguous Promt
```text
i have some counts of four 2-character bracket pieces "((", "()", ")(", and "))" and i have to glue all of them together in some order without dropping anything, anyway write a program to check if i can form one valid balanced bracket string.

-----Input-----

The input consists of four lines, $i$-th of them contains one integer $cnt_i$ ($0 \le cnt_i \le 10^9$).


-----Output-----

Print one integer: $1$ if it is possible to form a regular bracket sequence by choosing the correct order of the given strings, $0$ otherwise.


-----Examples-----
Input
3
1
4
3

Output
1

Input
0
0
0
0

Output
1

Input
1
2
3
4

Output
0



-----Note-----

In the first example it is possible to construct a string "(())()(()((()()()())))", which is a regular bracket sequence.

In the second example it is possible to construct a string "", which is a regular bracket sequence.
```

---

## Task 18: Problem ID 17 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/851/A](https://codeforces.com/problemset/problem/851/A)

### Clear Prompt (Canonical Baseline)
```text
Arpa is researching the Mexican wave.

There are n spectators in the stadium, labeled from 1 to n. They start the Mexican wave at time 0. 

  At time 1, the first spectator stands.  At time 2, the second spectator stands.  ...  At time k, the k-th spectator stands.  At time k + 1, the (k + 1)-th spectator stands and the first spectator sits.  At time k + 2, the (k + 2)-th spectator stands and the second spectator sits.  ...  At time n, the n-th spectator stands and the (n - k)-th spectator sits.  At time n + 1, the (n + 1 - k)-th spectator sits.  ...  At time n + k, the n-th spectator sits. 

Arpa wants to know how many spectators are standing at time t.


-----Input-----

The first line contains three integers n, k, t (1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, 1 ≤ t < n + k).


-----Output-----

Print single integer: how many spectators are standing at time t.


-----Examples-----
Input
10 5 3

Output
3

Input
10 5 7

Output
5

Input
10 5 12

Output
3



-----Note-----

In the following a sitting spectator is represented as -, a standing spectator is represented as ^.

  At t = 0  ---------- $\Rightarrow$ number of standing spectators = 0.  At t = 1  ^--------- $\Rightarrow$ number of standing spectators = 1.  At t = 2  ^^-------- $\Rightarrow$ number of standing spectators = 2.  At t = 3  ^^^------- $\Rightarrow$ number of standing spectators = 3.  At t = 4  ^^^^------ $\Rightarrow$ number of standing spectators = 4.  At t = 5  ^^^^^----- $\Rightarrow$ number of standing spectators = 5.  At t = 6  -^^^^^---- $\Rightarrow$ number of standing spectators = 5.  At t = 7  --^^^^^--- $\Rightarrow$ number of standing spectators = 5.  At t = 8  ---^^^^^-- $\Rightarrow$ number of standing spectators = 5.  At t = 9  ----^^^^^- $\Rightarrow$ number of standing spectators = 5.  At t = 10 -----^^^^^ $\Rightarrow$ number of standing spectators = 5.  At t = 11 ------^^^^ $\Rightarrow$ number of standing spectators = 4.  At t = 12 -------^^^ $\Rightarrow$ number of standing spectators = 3.  At t = 13 --------^^ $\Rightarrow$ number of standing spectators = 2.  At t = 14 ---------^ $\Rightarrow$ number of standing spectators = 1.  At t = 15 ---------- $\Rightarrow$ number of standing spectators = 0.
```

### Ambiguous Promt
```text
there are n people doing a stadium wave where one person stands up every second until k people are standing and then as the next person stands up the oldest standing one sits down until the wave finishes, anyway write a program to find how many people are standing at time t.

-----Input-----

The first line contains three integers n, k, t (1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, 1 ≤ t < n + k).


-----Output-----

Print single integer: how many spectators are standing at time t.


-----Examples-----
Input
10 5 3

Output
3

Input
10 5 7

Output
5

Input
10 5 12

Output
3



-----Note-----

In the following a sitting spectator is represented as -, a standing spectator is represented as ^.

  At t = 0  ---------- $\Rightarrow$ number of standing spectators = 0.  At t = 1  ^--------- $\Rightarrow$ number of standing spectators = 1.  At t = 2  ^^-------- $\Rightarrow$ number of standing spectators = 2.  At t = 3  ^^^------- $\Rightarrow$ number of standing spectators = 3.  At t = 4  ^^^^------ $\Rightarrow$ number of standing spectators = 4.  At t = 5  ^^^^^----- $\Rightarrow$ number of standing spectators = 5.  At t = 6  -^^^^^---- $\Rightarrow$ number of standing spectators = 5.  At t = 7  --^^^^^--- $\Rightarrow$ number of standing spectators = 5.  At t = 8  ---^^^^^-- $\Rightarrow$ number of standing spectators = 5.  At t = 9  ----^^^^^- $\Rightarrow$ number of standing spectators = 5.  At t = 10 -----^^^^^ $\Rightarrow$ number of standing spectators = 5.  At t = 11 ------^^^^ $\Rightarrow$ number of standing spectators = 4.  At t = 12 -------^^^ $\Rightarrow$ number of standing spectators = 3.  At t = 13 --------^^ $\Rightarrow$ number of standing spectators = 2.  At t = 14 ---------^ $\Rightarrow$ number of standing spectators = 1.  At t = 15 ---------- $\Rightarrow$ number of standing spectators = 0.
```

---

## Task 19: Problem ID 18 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/797/C](https://codeforces.com/problemset/problem/797/C)

### Clear Prompt (Canonical Baseline)
```text
Petya recieved a gift of a string s with length up to 10^5 characters for his birthday. He took two more empty strings t and u and decided to play a game. This game has two possible moves:  Extract the first character of s and append t with this character.  Extract the last character of t and append u with this character. 

Petya wants to get strings s and t empty and string u lexicographically minimal.

You should write a program that will help Petya win the game.


-----Input-----

First line contains non-empty string s (1 ≤ |s| ≤ 10^5), consisting of lowercase English letters.


-----Output-----

Print resulting string u.


-----Examples-----
Input
cab

Output
abc

Input
acdb

Output
abdc
```

### Ambiguous Promt
```text
i got a string s and two empty strings t and u and i can either move the first char of s to the end of t or pop the last char of t and put it at the end of u until s and t are empty, anyway write a code to make u as alphabetically small as posible.

-----Input-----

First line contains non-empty string s (1 ≤ |s| ≤ 10^5), consisting of lowercase English letters.


-----Output-----

Print resulting string u.


-----Examples-----
Input
cab

Output
abc

Input
acdb

Output
abdc
```

---

## Task 20: Problem ID 19 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/1334/A](https://codeforces.com/problemset/problem/1334/A)

### Clear Prompt (Canonical Baseline)
```text
Polycarp has recently created a new level in this cool new game Berlio Maker 85 and uploaded it online. Now players from all over the world can try his level.

All levels in this game have two stats to them: the number of plays and the number of clears. So when a player attempts the level, the number of plays increases by $1$. If he manages to finish the level successfully then the number of clears increases by $1$ as well. Note that both of the statistics update at the same time (so if the player finishes the level successfully then the number of plays will increase at the same time as the number of clears).

Polycarp is very excited about his level, so he keeps peeking at the stats to know how hard his level turns out to be.

So he peeked at the stats $n$ times and wrote down $n$ pairs of integers — $(p_1, c_1), (p_2, c_2), \dots, (p_n, c_n)$, where $p_i$ is the number of plays at the $i$-th moment of time and $c_i$ is the number of clears at the same moment of time. The stats are given in chronological order (i.e. the order of given pairs is exactly the same as Polycarp has written down).

Between two consecutive moments of time Polycarp peeked at the stats many players (but possibly zero) could attempt the level.

Finally, Polycarp wonders if he hasn't messed up any records and all the pairs are correct. If there could exist such a sequence of plays (and clears, respectively) that the stats were exactly as Polycarp has written down, then he considers his records correct.

Help him to check the correctness of his records.

For your convenience you have to answer multiple independent test cases.


-----Input-----

The first line contains a single integer $T$ $(1 \le T \le 500)$ — the number of test cases.

The first line of each test case contains a single integer $n$ ($1 \le n \le 100$) — the number of moments of time Polycarp peeked at the stats.

Each of the next $n$ lines contains two integers $p_i$ and $c_i$ ($0 \le p_i, c_i \le 1000$) — the number of plays and the number of clears of the level at the $i$-th moment of time.

Note that the stats are given in chronological order.


-----Output-----

For each test case print a single line.

If there could exist such a sequence of plays (and clears, respectively) that the stats were exactly as Polycarp has written down, then print "YES".

Otherwise, print "NO".

You can print each letter in any case (upper or lower).


-----Example-----
Input
6
3
0 0
1 1
1 2
2
1 0
1000 3
4
10 1
15 2
10 2
15 2
1
765 432
2
4 4
4 3
5
0 0
1 0
1 0
1 0
1 0

Output
NO
YES
NO
YES
NO
YES



-----Note-----

In the first test case at the third moment of time the number of clears increased but the number of plays did not, that couldn't have happened.

The second test case is a nice example of a Super Expert level.

In the third test case the number of plays decreased, which is impossible.

The fourth test case is probably an auto level with a single jump over the spike.

In the fifth test case the number of clears decreased, which is also impossible.

Nobody wanted to play the sixth test case; Polycarp's mom attempted it to make him feel better, however, she couldn't clear it.
```

### Ambiguous Promt
```text
i recorded n pairs of game level stats over time showing total plays and total clears where every clear also counts as a play, anyway write a program to check if these recorded numbers actually make sense chronologically.

-----Input-----

The first line contains a single integer $T$ $(1 \le T \le 500)$ — the number of test cases.

The first line of each test case contains a single integer $n$ ($1 \le n \le 100$) — the number of moments of time Polycarp peeked at the stats.

Each of the next $n$ lines contains two integers $p_i$ and $c_i$ ($0 \le p_i, c_i \le 1000$) — the number of plays and the number of clears of the level at the $i$-th moment of time.

Note that the stats are given in chronological order.


-----Output-----

For each test case print a single line.

If there could exist such a sequence of plays (and clears, respectively) that the stats were exactly as Polycarp has written down, then print "YES".

Otherwise, print "NO".

You can print each letter in any case (upper or lower).


-----Example-----
Input
6
3
0 0
1 1
1 2
2
1 0
1000 3
4
10 1
15 2
10 2
15 2
1
765 432
2
4 4
4 3
5
0 0
1 0
1 0
1 0
1 0

Output
NO
YES
NO
YES
NO
YES



-----Note-----

In the first test case at the third moment of time the number of clears increased but the number of plays did not, that couldn't have happened.

The second test case is a nice example of a Super Expert level.

In the third test case the number of plays decreased, which is impossible.

The fourth test case is probably an auto level with a single jump over the spike.

In the fifth test case the number of clears decreased, which is also impossible.

Nobody wanted to play the sixth test case; Polycarp's mom attempted it to make him feel better, however, she couldn't clear it.
```

---

## Task 21: Problem ID 20 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/816/A](https://codeforces.com/problemset/problem/816/A)

### Clear Prompt (Canonical Baseline)
```text
Karen is getting ready for a new school day!

 [Image] 

It is currently hh:mm, given in a 24-hour format. As you know, Karen loves palindromes, and she believes that it is good luck to wake up when the time is a palindrome.

What is the minimum number of minutes she should sleep, such that, when she wakes up, the time is a palindrome?

Remember that a palindrome is a string that reads the same forwards and backwards. For instance, 05:39 is not a palindrome, because 05:39 backwards is 93:50. On the other hand, 05:50 is a palindrome, because 05:50 backwards is 05:50.


-----Input-----

The first and only line of input contains a single string in the format hh:mm (00 ≤  hh  ≤ 23, 00 ≤  mm  ≤ 59).


-----Output-----

Output a single integer on a line by itself, the minimum number of minutes she should sleep, such that, when she wakes up, the time is a palindrome.


-----Examples-----
Input
05:39

Output
11

Input
13:31

Output
0

Input
23:59

Output
1



-----Note-----

In the first test case, the minimum number of minutes Karen should sleep for is 11. She can wake up at 05:50, when the time is a palindrome.

In the second test case, Karen can wake up immediately, as the current time, 13:31, is already a palindrome.

In the third test case, the minimum number of minutes Karen should sleep for is 1 minute. She can wake up at 00:00, when the time is a palindrome.
```

### Ambiguous Promt
```text
given a 24-hour clock time hh:mm i want to know the minimum number of minutes to wait until the time string reads the same backwards and forwards like a palindrome, anyway write a program to find that number of minutes.

-----Input-----

The first and only line of input contains a single string in the format hh:mm (00 ≤  hh  ≤ 23, 00 ≤  mm  ≤ 59).


-----Output-----

Output a single integer on a line by itself, the minimum number of minutes she should sleep, such that, when she wakes up, the time is a palindrome.


-----Examples-----
Input
05:39

Output
11

Input
13:31

Output
0

Input
23:59

Output
1



-----Note-----

In the first test case, the minimum number of minutes Karen should sleep for is 11. She can wake up at 05:50, when the time is a palindrome.

In the second test case, Karen can wake up immediately, as the current time, 13:31, is already a palindrome.

In the third test case, the minimum number of minutes Karen should sleep for is 1 minute. She can wake up at 00:00, when the time is a palindrome.
```

---

## Task 22: Problem ID 21 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/676/A](https://codeforces.com/problemset/problem/676/A)

### Clear Prompt (Canonical Baseline)
```text
Nicholas has an array a that contains n distinct integers from 1 to n. In other words, Nicholas has a permutation of size n.

Nicholas want the minimum element (integer 1) and the maximum element (integer n) to be as far as possible from each other. He wants to perform exactly one swap in order to maximize the distance between the minimum and the maximum elements. The distance between two elements is considered to be equal to the absolute difference between their positions.


-----Input-----

The first line of the input contains a single integer n (2 ≤ n ≤ 100) — the size of the permutation.

The second line of the input contains n distinct integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ n), where a_{i} is equal to the element at the i-th position.


-----Output-----

Print a single integer — the maximum possible distance between the minimum and the maximum elements Nicholas can achieve by performing exactly one swap.


-----Examples-----
Input
5
4 5 1 3 2

Output
3

Input
7
1 6 5 3 4 7 2

Output
6

Input
6
6 5 4 3 2 1

Output
5



-----Note-----

In the first sample, one may obtain the optimal answer by swapping elements 1 and 2.

In the second sample, the minimum and the maximum elements will be located in the opposite ends of the array if we swap 7 and 2.

In the third sample, the distance between the minimum and the maximum elements is already maximum possible, so we just perform some unnecessary swap, for example, one can swap 5 and 2.
```

### Ambiguous Promt
```text
i have a permutation array of numbers from 1 to n and i am allowed to swap exacty two elements once to push the 1 and the n as far apart in index distance as posible, anyway write a code to find that max distance.

-----Input-----

The first line of the input contains a single integer n (2 ≤ n ≤ 100) — the size of the permutation.

The second line of the input contains n distinct integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ n), where a_{i} is equal to the element at the i-th position.


-----Output-----

Print a single integer — the maximum possible distance between the minimum and the maximum elements Nicholas can achieve by performing exactly one swap.


-----Examples-----
Input
5
4 5 1 3 2

Output
3

Input
7
1 6 5 3 4 7 2

Output
6

Input
6
6 5 4 3 2 1

Output
5



-----Note-----

In the first sample, one may obtain the optimal answer by swapping elements 1 and 2.

In the second sample, the minimum and the maximum elements will be located in the opposite ends of the array if we swap 7 and 2.

In the third sample, the distance between the minimum and the maximum elements is already maximum possible, so we just perform some unnecessary swap, for example, one can swap 5 and 2.
```

---

## Task 23: Problem ID 22 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/691/B](https://codeforces.com/problemset/problem/691/B)

### Clear Prompt (Canonical Baseline)
```text
Let's call a string "s-palindrome" if it is symmetric about the middle of the string. For example, the string "oHo" is "s-palindrome", but the string "aa" is not. The string "aa" is not "s-palindrome", because the second half of it is not a mirror reflection of the first half.

 [Image] English alphabet 

You are given a string s. Check if the string is "s-palindrome".


-----Input-----

The only line contains the string s (1 ≤ |s| ≤ 1000) which consists of only English letters.


-----Output-----

Print "TAK" if the string s is "s-palindrome" and "NIE" otherwise.


-----Examples-----
Input
oXoxoXo

Output
TAK

Input
bod

Output
TAK

Input
ER

Output
NIE
```

### Ambiguous Promt
```text
i got a string s of english letters and i need to check if it looks visually symetric like a mirror reflection when flipped horizontally like "bod" or "oHo", anyway write a program to check if the string is mirror symetric.

-----Input-----

The only line contains the string s (1 ≤ |s| ≤ 1000) which consists of only English letters.


-----Output-----

Print "TAK" if the string s is "s-palindrome" and "NIE" otherwise.


-----Examples-----
Input
oXoxoXo

Output
TAK

Input
bod

Output
TAK

Input
ER

Output
NIE
```

---

## Task 24: Problem ID 23 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/915/C](https://codeforces.com/problemset/problem/915/C)

### Clear Prompt (Canonical Baseline)
```text
You are given two positive integer numbers a and b. Permute (change order) of the digits of a to construct maximal number not exceeding b. No number in input and/or output can start with the digit 0.

It is allowed to leave a as it is.


-----Input-----

The first line contains integer a (1 ≤ a ≤ 10^18). The second line contains integer b (1 ≤ b ≤ 10^18). Numbers don't have leading zeroes. It is guaranteed that answer exists.


-----Output-----

Print the maximum possible number that is a permutation of digits of a and is not greater than b. The answer can't have any leading zeroes. It is guaranteed that the answer exists.

The number in the output should have exactly the same length as number a. It should be a permutation of digits of a.


-----Examples-----
Input
123
222

Output
213

Input
3921
10000

Output
9321

Input
4940
5000

Output
4940
```

### Ambiguous Promt
```text
i have two numbers a and b and i want to rearrange the digits of a without leading zeros to make the biggest number possible that is still less than or equal to b, anyway write a code to print that rearranged number.

-----Input-----

The first line contains integer a (1 ≤ a ≤ 10^18). The second line contains integer b (1 ≤ b ≤ 10^18). Numbers don't have leading zeroes. It is guaranteed that answer exists.


-----Output-----

Print the maximum possible number that is a permutation of digits of a and is not greater than b. The answer can't have any leading zeroes. It is guaranteed that the answer exists.

The number in the output should have exactly the same length as number a. It should be a permutation of digits of a.


-----Examples-----
Input
123
222

Output
213

Input
3921
10000

Output
9321

Input
4940
5000

Output
4940
```

---

## Task 25: Problem ID 24 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/825/B](https://codeforces.com/problemset/problem/825/B)

### Clear Prompt (Canonical Baseline)
```text
Alice and Bob play 5-in-a-row game. They have a playing field of size 10 × 10. In turns they put either crosses or noughts, one at a time. Alice puts crosses and Bob puts noughts.

In current match they have made some turns and now it's Alice's turn. She wonders if she can put cross in such empty cell that she wins immediately.

Alice wins if some crosses in the field form line of length not smaller than 5. This line can be horizontal, vertical and diagonal.


-----Input-----

You are given matrix 10 × 10 (10 lines of 10 characters each) with capital Latin letters 'X' being a cross, letters 'O' being a nought and '.' being an empty cell. The number of 'X' cells is equal to the number of 'O' cells and there is at least one of each type. There is at least one empty cell.

It is guaranteed that in the current arrangement nobody has still won.


-----Output-----

Print 'YES' if it's possible for Alice to win in one turn by putting cross in some empty cell. Otherwise print 'NO'.


-----Examples-----
Input
XX.XX.....
.....OOOO.
..........
..........
..........
..........
..........
..........
..........
..........

Output
YES

Input
XXOXX.....
OO.O......
..........
..........
..........
..........
..........
..........
..........
..........

Output
NO
```

### Ambiguous Promt
```text
i got a 10x10 tic tac toe board with X, O, and dots and its X's turn so i want to know if putting just one X in an empty spot makes at least 5 X's in a row horizontally vertically or diagonally, anyway write a program to check if X can win right now.

-----Input-----

You are given matrix 10 × 10 (10 lines of 10 characters each) with capital Latin letters 'X' being a cross, letters 'O' being a nought and '.' being an empty cell. The number of 'X' cells is equal to the number of 'O' cells and there is at least one of each type. There is at least one empty cell.

It is guaranteed that in the current arrangement nobody has still won.


-----Output-----

Print 'YES' if it's possible for Alice to win in one turn by putting cross in some empty cell. Otherwise print 'NO'.


-----Examples-----
Input
XX.XX.....
.....OOOO.
..........
..........
..........
..........
..........
..........
..........
..........

Output
YES

Input
XXOXX.....
OO.O......
..........
..........
..........
..........
..........
..........
..........
..........

Output
NO
```

---

## Task 26: Problem ID 25 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/803/A](https://codeforces.com/problemset/problem/803/A)

### Clear Prompt (Canonical Baseline)
```text
You are given matrix with n rows and n columns filled with zeroes. You should put k ones in it in such a way that the resulting matrix is symmetrical with respect to the main diagonal (the diagonal that goes from the top left to the bottom right corner) and is lexicographically maximal.

One matrix is lexicographically greater than the other if the first different number in the first different row from the top in the first matrix is greater than the corresponding number in the second one.

If there exists no such matrix then output -1.


-----Input-----

The first line consists of two numbers n and k (1 ≤ n ≤ 100, 0 ≤ k ≤ 10^6).


-----Output-----

If the answer exists then output resulting matrix. Otherwise output -1.


-----Examples-----
Input
2 1

Output
1 0 
0 0 

Input
3 2

Output
1 0 0 
0 1 0 
0 0 0 

Input
2 5

Output
-1
```

### Ambiguous Promt
```text
i have an nxn grid of zeros and i need to place exacty k ones into it so the grid is symetric across the main diagonal and lexicographically as big as posible row by row from top to bottom, anyway write a code to build this matrix or print -1 if i cant.

-----Input-----

The first line consists of two numbers n and k (1 ≤ n ≤ 100, 0 ≤ k ≤ 10^6).


-----Output-----

If the answer exists then output resulting matrix. Otherwise output -1.


-----Examples-----
Input
2 1

Output
1 0 
0 0 

Input
3 2

Output
1 0 0 
0 1 0 
0 0 0 

Input
2 5

Output
-1
```

---

## Task 27: Problem ID 26 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/621/D](https://codeforces.com/problemset/problem/621/D)

### Clear Prompt (Canonical Baseline)
```text
Wet Shark asked Rat Kwesh to generate three positive real numbers x, y and z, from 0.1 to 200.0, inclusive. Wet Krash wants to impress Wet Shark, so all generated numbers will have exactly one digit after the decimal point.

Wet Shark knows Rat Kwesh will want a lot of cheese. So he will give the Rat an opportunity to earn a lot of cheese. He will hand the three numbers x, y and z to Rat Kwesh, and Rat Kwesh will pick one of the these twelve options:  a_1 = x^{y}^{z};  a_2 = x^{z}^{y};  a_3 = (x^{y})^{z};  a_4 = (x^{z})^{y};  a_5 = y^{x}^{z};  a_6 = y^{z}^{x};  a_7 = (y^{x})^{z};  a_8 = (y^{z})^{x};  a_9 = z^{x}^{y};  a_10 = z^{y}^{x};  a_11 = (z^{x})^{y};  a_12 = (z^{y})^{x}. 

Let m be the maximum of all the a_{i}, and c be the smallest index (from 1 to 12) such that a_{c} = m. Rat's goal is to find that c, and he asks you to help him. Rat Kwesh wants to see how much cheese he gets, so he you will have to print the expression corresponding to that a_{c}.

 


-----Input-----

The only line of the input contains three space-separated real numbers x, y and z (0.1 ≤ x, y, z ≤ 200.0). Each of x, y and z is given with exactly one digit after the decimal point.


-----Output-----

Find the maximum value of expression among x^{y}^{z}, x^{z}^{y}, (x^{y})^{z}, (x^{z})^{y}, y^{x}^{z}, y^{z}^{x}, (y^{x})^{z}, (y^{z})^{x}, z^{x}^{y}, z^{y}^{x}, (z^{x})^{y}, (z^{y})^{x} and print the corresponding expression. If there are many maximums, print the one that comes first in the list. 

x^{y}^{z} should be outputted as x^y^z (without brackets), and (x^{y})^{z} should be outputted as (x^y)^z (quotes for clarity). 


-----Examples-----
Input
1.1 3.4 2.5

Output
z^y^x

Input
2.0 2.0 2.0

Output
x^y^z

Input
1.9 1.8 1.7

Output
(x^y)^z
```

### Ambiguous Promt
```text
given three decimal numbers x, y, and z i need to compare all 12 ways of raising them to powers like x^y^z or (x^y)^z and figure out wich formula produces the biggest value without overflowing numbers, anyway write a program to print the winning formula.

-----Input-----

The only line of the input contains three space-separated real numbers x, y and z (0.1 ≤ x, y, z ≤ 200.0). Each of x, y and z is given with exactly one digit after the decimal point.


-----Output-----

Find the maximum value of expression among x^{y}^{z}, x^{z}^{y}, (x^{y})^{z}, (x^{z})^{y}, y^{x}^{z}, y^{z}^{x}, (y^{x})^{z}, (y^{z})^{x}, z^{x}^{y}, z^{y}^{x}, (z^{x})^{y}, (z^{y})^{x} and print the corresponding expression. If there are many maximums, print the one that comes first in the list. 

x^{y}^{z} should be outputted as x^y^z (without brackets), and (x^{y})^{z} should be outputted as (x^y)^z (quotes for clarity). 


-----Examples-----
Input
1.1 3.4 2.5

Output
z^y^x

Input
2.0 2.0 2.0

Output
x^y^z

Input
1.9 1.8 1.7

Output
(x^y)^z
```

---

## Task 28: Problem ID 27 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/954/B](https://codeforces.com/problemset/problem/954/B)

### Clear Prompt (Canonical Baseline)
```text
You are given a string s consisting of n lowercase Latin letters. You have to type this string using your keyboard.

Initially, you have an empty string. Until you type the whole string, you may perform the following operation:  add a character to the end of the string. 

Besides, at most once you may perform one additional operation: copy the string and append it to itself.

For example, if you have to type string abcabca, you can type it in 7 operations if you type all the characters one by one. However, you can type it in 5 operations if you type the string abc first and then copy it and type the last character.

If you have to type string aaaaaaaaa, the best option is to type 4 characters one by one, then copy the string, and then type the remaining character.

Print the minimum number of operations you need to type the given string.


-----Input-----

The first line of the input containing only one integer number n (1 ≤ n ≤ 100) — the length of the string you have to type. The second line containing the string s consisting of n lowercase Latin letters.


-----Output-----

Print one integer number — the minimum number of operations you need to type the given string.


-----Examples-----
Input
7
abcabca

Output
5

Input
8
abcdefgh

Output
8



-----Note-----

The first test described in the problem statement.

In the second test you can only type all the characters one by one.
```

### Ambiguous Promt
```text
i want to type a string s of lenght n starting from empty where each step i can type one letter at the end plus at most one time in the whole process i can copy everything i typed so far and paste it at the end, anyway write a program to find the fewest steps to finish typing s.

-----Input-----

The first line of the input containing only one integer number n (1 ≤ n ≤ 100) — the length of the string you have to type. The second line containing the string s consisting of n lowercase Latin letters.


-----Output-----

Print one integer number — the minimum number of operations you need to type the given string.


-----Examples-----
Input
7
abcabca

Output
5

Input
8
abcdefgh

Output
8



-----Note-----

The first test described in the problem statement.

In the second test you can only type all the characters one by one.
```

---

## Task 29: Problem ID 28 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/858/E](https://codeforces.com/problemset/problem/858/E)

### Clear Prompt (Canonical Baseline)
```text
The All-Berland National Olympiad in Informatics has just ended! Now Vladimir wants to upload the contest from the Olympiad as a gym to a popular Codehorses website.

Unfortunately, the archive with Olympiad's data is a mess. For example, the files with tests are named arbitrary without any logic.

Vladimir wants to rename the files with tests so that their names are distinct integers starting from 1 without any gaps, namely, "1", "2", ..., "n', where n is the total number of tests.

Some of the files contain tests from statements (examples), while others contain regular tests. It is possible that there are no examples, and it is possible that all tests are examples. Vladimir wants to rename the files so that the examples are the first several tests, all all the next files contain regular tests only.

The only operation Vladimir can perform is the "move" command. Vladimir wants to write a script file, each of the lines in which is "move file_1 file_2", that means that the file "file_1" is to be renamed to "file_2". If there is a file "file_2" at the moment of this line being run, then this file is to be rewritten. After the line "move file_1 file_2" the file "file_1" doesn't exist, but there is a file "file_2" with content equal to the content of "file_1" before the "move" command.

Help Vladimir to write the script file with the minimum possible number of lines so that after this script is run:  all examples are the first several tests having filenames "1", "2", ..., "e", where e is the total number of examples;  all other files contain regular tests with filenames "e + 1", "e + 2", ..., "n", where n is the total number of all tests. 


-----Input-----

The first line contains single integer n (1 ≤ n ≤ 10^5) — the number of files with tests.

n lines follow, each describing a file with test. Each line has a form of "name_i type_i", where "name_i" is the filename, and "type_i" equals "1", if the i-th file contains an example test, and "0" if it contains a regular test. Filenames of each file are strings of digits and small English letters with length from 1 to 6 characters. The filenames are guaranteed to be distinct.


-----Output-----

In the first line print the minimum number of lines in Vladimir's script file.

After that print the script file, each line should be "move file_1 file_2", where "file_1" is an existing at the moment of this line being run filename, and "file_2" — is a string of digits and small English letters with length from 1 to 6.


-----Examples-----
Input
5
01 0
2 1
2extra 0
3 1
99 0

Output
4
move 3 1
move 01 5
move 2extra 4
move 99 3

Input
2
1 0
2 1

Output
3
move 1 3
move 2 1
move 3 2
Input
5
1 0
11 1
111 0
1111 1
11111 0

Output
5
move 1 5
move 11 1
move 1111 2
move 111 4
move 11111 3
```

### Ambiguous Promt
```text
i got n test files with messy names where e of them are sample tests and the rest are regular tests and i need to rename them using "move old new" commands without overwriting existing files accidentally so sample tests become 1 to e and regular tests become e+1 to n, anyway write a program to output the shortest list of move commands.

-----Input-----

The first line contains single integer n (1 ≤ n ≤ 10^5) — the number of files with tests.

n lines follow, each describing a file with test. Each line has a form of "name_i type_i", where "name_i" is the filename, and "type_i" equals "1", if the i-th file contains an example test, and "0" if it contains a regular test. Filenames of each file are strings of digits and small English letters with length from 1 to 6 characters. The filenames are guaranteed to be distinct.


-----Output-----

In the first line print the minimum number of lines in Vladimir's script file.

After that print the script file, each line should be "move file_1 file_2", where "file_1" is an existing at the moment of this line being run filename, and "file_2" — is a string of digits and small English letters with length from 1 to 6.


-----Examples-----
Input
5
01 0
2 1
2extra 0
3 1
99 0

Output
4
move 3 1
move 01 5
move 2extra 4
move 99 3

Input
2
1 0
2 1

Output
3
move 1 3
move 2 1
move 3 2
Input
5
1 0
11 1
111 0
1111 1
11111 0

Output
5
move 1 5
move 11 1
move 1111 2
move 111 4
move 11111 3
```

---

## Task 30: Problem ID 29 (Interview)
- **Difficulty Tier:** Interview
- **Benchmark Source URL:** [https://codeforces.com/problemset/problem/845/B](https://codeforces.com/problemset/problem/845/B)

### Clear Prompt (Canonical Baseline)
```text
Luba has a ticket consisting of 6 digits. In one move she can choose digit in any position and replace it with arbitrary digit. She wants to know the minimum number of digits she needs to replace in order to make the ticket lucky.

The ticket is considered lucky if the sum of first three digits equals to the sum of last three digits.


-----Input-----

You are given a string consisting of 6 characters (all characters are digits from 0 to 9) — this string denotes Luba's ticket. The ticket can start with the digit 0.


-----Output-----

Print one number — the minimum possible number of digits Luba needs to replace to make the ticket lucky.


-----Examples-----
Input
000000

Output
0

Input
123456

Output
2

Input
111000

Output
1



-----Note-----

In the first example the ticket is already lucky, so the answer is 0.

In the second example Luba can replace 4 and 5 with zeroes, and the ticket will become lucky. It's easy to see that at least two replacements are required.

In the third example Luba can replace any zero with 3. It's easy to see that at least one replacement is required.
```

### Ambiguous Promt
```text
i have a 6-digit string and i can change any digit to another digit from 0 to 9 so i want to know the minimum changes needed to make the sum of the first 3 digits equal to the sum of the last 3 digits, anyway write a code to find that minimum number of changes.

-----Input-----

You are given a string consisting of 6 characters (all characters are digits from 0 to 9) — this string denotes Luba's ticket. The ticket can start with the digit 0.


-----Output-----

Print one number — the minimum possible number of digits Luba needs to replace to make the ticket lucky.


-----Examples-----
Input
000000

Output
0

Input
123456

Output
2

Input
111000

Output
1



-----Note-----

In the first example the ticket is already lucky, so the answer is 0.

In the second example Luba can replace 4 and 5 with zeroes, and the ticket will become lucky. It's easy to see that at least two replacements are required.

In the third example Luba can replace any zero with 3. It's easy to see that at least one replacement is required.
```

---

## Task 31: Problem ID 3015 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/hamster](https://open.kattis.com/problems/hamster)

### Clear Prompt (Canonical Baseline)
```text
Harry the Hamster lives in a giant hamster cage. Inside the cage there is a set of $n$ plastic balls connected by unidirectional hamster tubes of varying lengths. Harry is currently in ball $s$ and his bed is in ball $t$.

Being a simple hamster, the hemispheres of Harry’s brain are not so great at communicating with each other and have a mind of their own. Harry’s left hemisphere, usually being active when Harry is in the hamster wheel, likes running for as long as possible. Harry’s right hemisphere, rarely active at all, would like to go to sleep as soon as possible. Together, Harry’s hemispheres will be navigating Harry through the maze of tubes, in each ball deciding which of the outgoing tubes to follow.

Harry’s hemispheres get really tired after making a decision and then need to rest a bit, so they cannot make two decisions in a row. Thus, they make decisions on which tube to take in alternating turns, with the left hemisphere going first. So starting in ball $s$, Harry’s left hemisphere will decide on a tube to follow, ending in some ball $u$, where Harry’s left hemisphere will rest and Harry’s right hemisphere will pick an outgoing tube, et cetera.

Counterintuitively, the hemispheres are familiar with the entire hamster cage and can plan arbitrarily far ahead. Assuming both hemispheres make optimal decisions, how long will it take for Harry to reach his bed? It is guaranteed that each ball has at least one outgoing tube, except the ball containing Harry’s bed which has none (there Harry will rest easily). There are no tubes connecting a ball to itself, but there may be multiple tubes going from one ball to another.

-----Input-----
 - On the first line are four space-separated integers: the number of plastic balls $1 \leq n \leq 10^5$, the number of tubes $0 \leq m \leq 2 \cdot 10^5$, and the locations of Harry and his bed $0 \leq s, t < n$.
 - Then $m$ lines follow, each containing three space-separated integers describing a single tube: the ball in which the tube starts $0 \leq a_ i < n$, in which it ends $0 \leq b_ i < n$ and the time it takes to traverse $1 \leq w_ i \leq 10^4$. Note that each tube can only be traversed in one direction.

-----Output-----
Print the time it takes for Harry to reach his bed, or the string infinity if Harry is doomed to roam the tubes forever.

-----Examples-----
Sample Input 1:
4 5 0 3
0 1 1
1 2 2
2 0 4
2 3 1
2 3 3
Sample Output 1:
11

Sample Input 2:
5 5 0 4
0 1 1
1 2 1
2 3 1
3 0 1
2 4 1
Sample Output 2:
infinity

Sample Input 3:
2 1 0 1
0 1 2
Sample Output 3:
2

Sample Input 4:
3 3 1 2
0 1 1
1 0 1
1 2 1
Sample Output 4:
infinity
```

### Ambiguous Promt
```text
i got a directed weighted graph from node s to target node t where two players take turns picking the next edge starting with player one who wants to maximize total travel time while player two wants to minimize it, anyway write a program to find the final travel time or print infinity if it loops forever.

-----Input-----
 - On the first line are four space-separated integers: the number of plastic balls $1 \leq n \leq 10^5$, the number of tubes $0 \leq m \leq 2 \cdot 10^5$, and the locations of Harry and his bed $0 \leq s, t < n$.
 - Then $m$ lines follow, each containing three space-separated integers describing a single tube: the ball in which the tube starts $0 \leq a_ i < n$, in which it ends $0 \leq b_ i < n$ and the time it takes to traverse $1 \leq w_ i \leq 10^4$. Note that each tube can only be traversed in one direction.

-----Output-----
Print the time it takes for Harry to reach his bed, or the string infinity if Harry is doomed to roam the tubes forever.

-----Examples-----
Sample Input 1:
4 5 0 3
0 1 1
1 2 2
2 0 4
2 3 1
2 3 3
Sample Output 1:
11

Sample Input 2:
5 5 0 4
0 1 1
1 2 1
2 3 1
3 0 1
2 4 1
Sample Output 2:
infinity

Sample Input 3:
2 1 0 1
0 1 2
Sample Output 3:
2

Sample Input 4:
3 3 1 2
0 1 1
1 0 1
1 2 1
Sample Output 4:
infinity
```

---

## Task 32: Problem ID 3016 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/ballcolors](https://open.kattis.com/problems/ballcolors)

### Clear Prompt (Canonical Baseline)
```text
Baby Timmy has a pool of balls that he plays with. The pool is made up of balls with $n$ different colors with a certain number of each color. Baby Timmy finds it interesting to order these balls in a line given certain conditions he made. Timmy has two conditions when playing his own game:
 - Balls of certain colors may not be next to each other
 - One particular sequence of colors which Timmy likes most must appear as many times as possible

Can you compute the total number of different ways in which Timmy can arrange his balls?

For instance, suppose Timmy has $2$ red, $1$ yellow, $2$ green, and $1$ blue ball(s). He doesn’t like for red or yellow balls to be next to each other, and his favorite sequence is “green blue.” The following six arrangements meet the requirements:

red green blue red green yellow 
red green blue yellow green red 
red green red green blue yellow 
red green yellow green blue red 
yellow green blue red green red 
yellow green red green blue red 

This arrangement corresponds to Sample Input 1.

Note that Timmy insists on including his favorite sequence as often as the available balls allow, even if that means not being able to complete the arrangement of balls at all.

-----Input-----
The input consists of a single test case with three lines. The first line contains an integer $n$ ($2 \le n \le 50$), which describe the number of different colors. The remaining $n$ integers on that line denote how many balls Timmy has of each color (colors are numbered $1$ through $n$ and their frequencies appear in order). The number of balls he has of each color is between $1$ and $50$, inclusive.

The second line of input describes which colors Timmy does not want next to each other. The first integer $k$ ($0 \le k \le n$) gives the number of colors. This is followed by $k$ integers $c_ i$ ($1 \le c_ i \le n$) denoting the colors that prevent balls having any of these colors from being next to each other. Each $c_ i$ is unique.

The third line of input describes the sequence Timmy likes most. This first integer $l$ ($0 \le l \le n$) describes the length of this sequence, and the following $l$ integers $s_ i$ ($1 \le s_ i \le n$) describe the sequence that must appear as often as possible in the arrangement. Each $s_ i$ is unique and the sets $\{ c_ i \} $ and $\{ s_ i \} $ do not intersect.

-----Output-----
Output the number of arrangements Timmy can make that satisfy the given conditions. Since the number can be large, output its value modulo $1000000007$.

-----Examples-----
Sample Input 1:
4 2 1 2 1
2 1 2
2 3 4
Sample Output 1:
6

Sample Input 2:
3 3 1 1
1 1
2 2 3
Sample Output 2:
0

Sample Input 3:
3 2 2 3
1 1
2 2 3
Sample Output 3:
18

Sample Input 4:
3 1 2 3
2 1 2
0
Sample Output 4:
12
```

### Ambiguous Promt
```text
i have colored balls of n colors with given counts and i want to line them all up so that a given forbidden subset of colors never touch each other or themselves while a specific target sequence of distinct colors appears the maximum possible number of times, anyway write a code to count valid arrangements modulo 1000000007.

-----Input-----
The input consists of a single test case with three lines. The first line contains an integer $n$ ($2 \le n \le 50$), which describe the number of different colors. The remaining $n$ integers on that line denote how many balls Timmy has of each color (colors are numbered $1$ through $n$ and their frequencies appear in order). The number of balls he has of each color is between $1$ and $50$, inclusive.

The second line of input describes which colors Timmy does not want next to each other. The first integer $k$ ($0 \le k \le n$) gives the number of colors. This is followed by $k$ integers $c_ i$ ($1 \le c_ i \le n$) denoting the colors that prevent balls having any of these colors from being next to each other. Each $c_ i$ is unique.

The third line of input describes the sequence Timmy likes most. This first integer $l$ ($0 \le l \le n$) describes the length of this sequence, and the following $l$ integers $s_ i$ ($1 \le s_ i \le n$) describe the sequence that must appear as often as possible in the arrangement. Each $s_ i$ is unique and the sets $\{ c_ i \} $ and $\{ s_ i \} $ do not intersect.

-----Output-----
Output the number of arrangements Timmy can make that satisfy the given conditions. Since the number can be large, output its value modulo $1000000007$.

-----Examples-----
Sample Input 1:
4 2 1 2 1
2 1 2
2 3 4
Sample Output 1:
6

Sample Input 2:
3 3 1 1
1 1
2 2 3
Sample Output 2:
0

Sample Input 3:
3 2 2 3
1 1
2 2 3
Sample Output 3:
18

Sample Input 4:
3 1 2 3
2 1 2
0
Sample Output 4:
12
```

---

## Task 33: Problem ID 3017 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/powersof2](https://open.kattis.com/problems/powersof2)

### Clear Prompt (Canonical Baseline)
```text
Theta has been learning about powers of $2$ in school. She notices that some numbers when written out contain powers of $2$ in their digit representation: for instance, $12560$ contains $256$ which is a power of $2$. She has been wondering how many such numbers there are.

Can you write a program that counts how many numbers contain a given power of $2$?

-----Input-----
The input consists of a single line with two integers $n$ and $e$ ($0 \le n \le 9 \cdot 10^{18}, 0 \le e \le 62$).

-----Output-----
Output a single integer that is equal to the number of distinct integers $k$ ($0 \le k \le n$) whose decimal representation contains the digits of $2^e$ as a substring.

-----Examples-----
Sample Input 1:
1000000 1
Sample Output 1:
468559

Sample Input 2:
1000000 5
Sample Output 2:
49401

Sample Input 3:
1000000 16
Sample Output 3:
20

Sample Input 4:
9000000000000000000 62
Sample Output 4:
1
```

### Ambiguous Promt
```text
given two integers n and e i need to count how many integers from 0 up to n have the digits of 2^e appearing as a substring inside their decimal representation, anyway write a program to compute that count.

-----Input-----
The input consists of a single line with two integers $n$ and $e$ ($0 \le n \le 9 \cdot 10^{18}, 0 \le e \le 62$).

-----Output-----
Output a single integer that is equal to the number of distinct integers $k$ ($0 \le k \le n$) whose decimal representation contains the digits of $2^e$ as a substring.

-----Examples-----
Sample Input 1:
1000000 1
Sample Output 1:
468559

Sample Input 2:
1000000 5
Sample Output 2:
49401

Sample Input 3:
1000000 16
Sample Output 3:
20

Sample Input 4:
9000000000000000000 62
Sample Output 4:
1
```

---

## Task 34: Problem ID 3018 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/pickingupthedice](https://open.kattis.com/problems/pickingupthedice)

### Clear Prompt (Canonical Baseline)
```text
Two players are playing a game with a set of $K$ six-sided dice. One player calls out a number in the range $K\ldots 6K$ and the other tries to roll that number. After the first roll, the player is allowed to pick up any number ($0\ldots K$) of dice and re-roll them.

Given the number of dice, the target number the player wants to roll, and the set of numbers the player obtained on the first roll, what number of dice should the player pick up to maximize their chances of getting the target number on the second roll?

-----Input-----
Input begins with a line containing $2$ integers, $K$, the number of dice, and $T$, the target number. The bounds are $2 \leq K \leq 24$ and $K \leq T \leq 6K$.

The next line contains $K$ integers, indicating the numbers that were rolled on each of the dice on the first roll. All will be integers in the range $1\ldots 6$.

-----Output-----
Print a single line containing an integer denoting the number of dice that the roller should pick up and re-roll in order to maximize the chances of getting an overall sum of $T$. (The roller will be able to choose which dice to pick up, but you are only asked to print the number of dice, not which ones.)

If there are more than one numbers of dice that can be picked up to achieve the same probability of getting to $T$, print the smallest such value.

-----Examples-----
Sample Input 1:
3 9
5 4 1
Sample Output 1:
1

Sample Input 2:
4 13
2 2 2 2
Sample Output 2:
3

Sample Input 3:
18 90
1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6
Sample Output 3:
12
```

### Ambiguous Promt
```text
i rolled K six-sided dice and got some initial numbers and now i can pick any subset of those dice to reroll once so that the final sum hits a target T with the highest probability, anyway write a code to find the smallest number of dice i should pick up and reroll.

-----Input-----
Input begins with a line containing $2$ integers, $K$, the number of dice, and $T$, the target number. The bounds are $2 \leq K \leq 24$ and $K \leq T \leq 6K$.

The next line contains $K$ integers, indicating the numbers that were rolled on each of the dice on the first roll. All will be integers in the range $1\ldots 6$.

-----Output-----
Print a single line containing an integer denoting the number of dice that the roller should pick up and re-roll in order to maximize the chances of getting an overall sum of $T$. (The roller will be able to choose which dice to pick up, but you are only asked to print the number of dice, not which ones.)

If there are more than one numbers of dice that can be picked up to achieve the same probability of getting to $T$, print the smallest such value.

-----Examples-----
Sample Input 1:
3 9
5 4 1
Sample Output 1:
1

Sample Input 2:
4 13
2 2 2 2
Sample Output 2:
3

Sample Input 3:
18 90
1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6
Sample Output 3:
12
```

---

## Task 35: Problem ID 3019 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/data](https://open.kattis.com/problems/data)

### Clear Prompt (Canonical Baseline)
```text
Today everyone is talking about big data. As a renowned data provider in the area, you now have $N$ precious pieces of data. You want to sell all $N$ pieces of data to $N$ customers. You can sell multiple pieces of data (including all and none) to a single customer. However, each piece of data must be sold to exactly one customer (you cannot split a single piece of data and sell it to multiple customers).

In your previous transactions you simply sold bigger data for higher prices. Unfortunately, that did not work quite well and your customers were a bit unsatisfied about the value of the data they got. Obviously, the value of data is not necessarily positively correlated with its volume.

This time you decide to do something different. After many meetings you finally sign a new contract with your customers. You number the $N$ pieces of data from $1$ to $N$ and figure out that the $i^\textrm {th}$ piece of data has a special property $S_ i$. The new contract specifies that each customer shall pay you an amount of money that is equal to the number of distinct prime factors in the sum of $S_ i$’s of the data pieces sold to him/her.

Based on the new contract, what is the maximum revenue you can achieve by selling all $N$ pieces of data?

-----Input-----
The first line has a single integer $N$ ($1 \leq N \leq 14$). The second line has $N$ positive integers, $S_1, S_2, \ldots , S_ N$. These integers are no larger than $1000$.

-----Output-----
Output the maximum revenue you can achieve by selling all $N$ pieces of data.

-----Examples-----
Sample Input 1:
1
1
Sample Output 1:
0

Sample Input 2:
3
4 7 8
Sample Output 2:
3

Sample Input 3:
5
2 3 4 5 8
Sample Output 3:
5
```

### Ambiguous Promt
```text
i have N numbers and i want to partition all of them into non-overlapping groups so that the sum of the number of distinct prime factors of each group's sum is as big as posible, anyway write a program to find the maximum total score.

-----Input-----
The first line has a single integer $N$ ($1 \leq N \leq 14$). The second line has $N$ positive integers, $S_1, S_2, \ldots , S_ N$. These integers are no larger than $1000$.

-----Output-----
Output the maximum revenue you can achieve by selling all $N$ pieces of data.

-----Examples-----
Sample Input 1:
1
1
Sample Output 1:
0

Sample Input 2:
3
4 7 8
Sample Output 2:
3

Sample Input 3:
5
2 3 4 5 8
Sample Output 3:
5
```

---

## Task 36: Problem ID 3020 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/newmaths](https://open.kattis.com/problems/newmaths)

### Clear Prompt (Canonical Baseline)
```text
“Drat!” cursed Charles. “This stupid carry bar is not working in my Engine! I just tried to calculate the square of a number, but it’s wrong; all of the carries are lost.”

“Hmm,” mused Ada, “arithmetic without carries! I wonder if I can figure out what your original input was, based on the result I see on the Engine.”

Carryless addition, denoted by $\oplus $, is the same as normal addition, except any carries are ignored (in base $10$). Thus, $37 \oplus 48$ is $75$, not $85$.

Carryless multiplication, denoted by $\otimes $, is performed using the schoolboy algorithm for multiplication, column by column, but the intermediate additions are calculated using carryless addition. More formally, Let $a_ m a_{m-1} \ldots a_1 a_0$ be the digits of $a$, where $a_0$ is its least significant digit. Similarly define $b_ n b_{n-1} \ldots b_1 b_0$ be the digits of $b$. The digits of $c = a \otimes b$ are given by the following equation:\[ c_ k = \left( a_0 b_ k \oplus a_1 b_{k-1} \oplus \cdots \oplus a_{k-1} b_1 \oplus a_ k b_0 \right) \bmod {10}, \]

where any $a_ i$ or $b_ j$ is considered zero if $i > m$ or $j > n$. For example, $9 \otimes 1234$ is $9876$, $90 \otimes 1234$ is $98760$, and $99 \otimes 1234$ is $97536$.

Given $N$, find the smallest positive integer $a$ such that $a \otimes a = N$.

-----Input-----
The input consists of a single line with a positive integer $N$, with at most $25$ digits and no leading zeros.

-----Output-----
Print, on a single line, the least positive number $a$ such that $a \otimes a = N$. If there is no such $a$, print ‘-1’ instead.

-----Examples-----
Sample Input 1:
6
Sample Output 1:
4

Sample Input 2:
149
Sample Output 2:
17

Sample Input 3:
123476544
Sample Output 3:
11112
```

### Ambiguous Promt
```text
in base-10 carryless math where adding digits drops any carry over 10 and multiplying is standard column multiplication without carries i have a result N and need to find the smallest positive integer a whose carryless square equals N, anyway write a code to find a or print -1.

-----Input-----
The input consists of a single line with a positive integer $N$, with at most $25$ digits and no leading zeros.

-----Output-----
Print, on a single line, the least positive number $a$ such that $a \otimes a = N$. If there is no such $a$, print ‘-1’ instead.

-----Examples-----
Sample Input 1:
6
Sample Output 1:
4

Sample Input 2:
149
Sample Output 2:
17

Sample Input 3:
123476544
Sample Output 3:
11112
```

---

## Task 37: Problem ID 3021 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/easyascab](https://open.kattis.com/problems/easyascab)

### Clear Prompt (Canonical Baseline)
```text
We all know how to alphabetize a list of distinct words when you know the alphabet: One word may be a prefix of another longer word, in which case the shorter word always comes before the longer word. With any other two words there must be a first place in the words where their letters differ. Then the order of the words is determined by the lexicographical order of these first differing letters.

How about the reverse problem: Can you find the lexicographic order of the alphabet from an ordered list of words? Suppose an alphabet exists where the following list of word strings is given in lexicographical order:

cab
cda
ccc
badca

It is clear that c comes before b in the underlying alphabet because cab comes before badca. Similarly, we know a comes before d, because cab < cda, a comes before c because cab < ccc, and d comes before c because cda < ccc. The only ordering of the 4 alphabet characters that is possible is adcb.

However, it may be that a list contains inconsistencies that make it impossible to be ordered under any proposed alphabet. For example, in the following list it must be that a comes before b in the alphabet since abc < bca, yet it also must be that b comes before a in the alphabet since bca < aca.

abc
bca
cab
aca

Finally, some lists may not provide enough clues to derive a unique alphabet order, such as the following:

dea
cfb

In this list, d comes before c but we don’t know about the relative positions of any of the other letters, so we are unable to uniquely discern the order of the alphabet characters.

-----Input-----
The first line of input will contain $L$ and $N$, separated by a space, where $L$ is a lowercase character $\texttt{b} \le L \le \texttt{z}$ representing the highest character in the English alphabet that appears in the derived alphabet, and $N$ is an integer $1 \leq N \leq 1000$ that is equal to the number of strings in the list. Each of the next $N$ lines will contain a single nonempty string of length at most $1000$, consisting only of characters in the derived alphabet. No two strings will be the same.

-----Output-----
If the input is consistent with a unique ordering of the alphabet, output a string that designates that ordered alphabet. If the data is inconsistent with any ordering, output IMPOSSIBLE. If the data is consistent with multiple orderings, output AMBIGUOUS.

-----Examples-----
Sample Input 1:
d 4
cab
cda
ccc
badca
Sample Output 1:
adcb

Sample Input 2:
c 4
abc
bca
cab
aca
Sample Output 2:
IMPOSSIBLE

Sample Input 3:
f 2
dea
cfb
Sample Output 3:
AMBIGUOUS
```

### Ambiguous Promt
```text
i have N words sorted according to some unknown alien alphabet using letters from 'a' up to L and i need to reconstruct the exact letter order of that alphabet, anyway write a program to print the alphabet order or say if its IMPOSSIBLE or AMBIGUOUS.

-----Input-----
The first line of input will contain $L$ and $N$, separated by a space, where $L$ is a lowercase character $\texttt{b} \le L \le \texttt{z}$ representing the highest character in the English alphabet that appears in the derived alphabet, and $N$ is an integer $1 \leq N \leq 1000$ that is equal to the number of strings in the list. Each of the next $N$ lines will contain a single nonempty string of length at most $1000$, consisting only of characters in the derived alphabet. No two strings will be the same.

-----Output-----
If the input is consistent with a unique ordering of the alphabet, output a string that designates that ordered alphabet. If the data is inconsistent with any ordering, output IMPOSSIBLE. If the data is consistent with multiple orderings, output AMBIGUOUS.

-----Examples-----
Sample Input 1:
d 4
cab
cda
ccc
badca
Sample Output 1:
adcb

Sample Input 2:
c 4
abc
bca
cab
aca
Sample Output 2:
IMPOSSIBLE

Sample Input 3:
f 2
dea
cfb
Sample Output 3:
AMBIGUOUS
```

---

## Task 38: Problem ID 3022 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/diversecookies](https://open.kattis.com/problems/diversecookies)

### Clear Prompt (Canonical Baseline)
```text
Is a world without cookies really worth living in? Alf and Beata do not think so. That’s why they spent the entire weekend baking an enormous amount of cookies. They baked $A$ almond biscuits, $B$ butter cookies and $C$ chocolate macarons.

It is now time to eat all these delicious cookies with their friends. The cookies will be divided up among all the friends. However, this division must be done such that everyone can eat all of their cookies without having to eat the same kind of cookie twice in a row (that would be very unpleasant).

Furthermore, Alf and Beata wants as few cookies as possible to go to waste – they spent a lot of time preparing them, after all. Can you determine the maximum amount of cookies that can be distributed among everyone?

-----Input-----
The first and only line contains four integers $N$ ($2 \le N \le 10^9$), the number of friends eating cookies including Alf and Beata, and $A$, $B$ and $C$ ($0 \le A, B, C \le 10^9$), the amount of cookies of each of the three times Alf and Beata baked.

-----Output-----
Output a single integer – the number of cookies Alf and Beata are able to distribute.

-----Examples-----
Sample Input 1:
2 3 3 3
Sample Output 1:
9

Sample Input 2:
10 20 0 0
Sample Output 2:
10

Sample Input 3:
100 20 543 12
Sample Output 3:
164
```

### Ambiguous Promt
```text
i have N people and A, B, and C cookies of three different flavors and i want to give out as many cookies as posible so that each person can order their own pile without eating the same flavor twice in a row, anyway write a program to find the max total cookies distributed.

-----Input-----
The first and only line contains four integers $N$ ($2 \le N \le 10^9$), the number of friends eating cookies including Alf and Beata, and $A$, $B$ and $C$ ($0 \le A, B, C \le 10^9$), the amount of cookies of each of the three times Alf and Beata baked.

-----Output-----
Output a single integer – the number of cookies Alf and Beata are able to distribute.

-----Examples-----
Sample Input 1:
2 3 3 3
Sample Output 1:
9

Sample Input 2:
10 20 0 0
Sample Output 2:
10

Sample Input 3:
100 20 543 12
Sample Output 3:
164
```

---

## Task 39: Problem ID 3023 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/birthdaycake](https://open.kattis.com/problems/birthdaycake)

### Clear Prompt (Canonical Baseline)
```text
On his birthday, John’s parents made him a huge birthday cake! Everyone had a wonderful dinner, and now it’s time to eat the cake. There are $n$ candles on the cake. John wants to divide the cake into $n$ pieces so that each piece has exactly one candle on it, and there are no left-over pieces. For that, he made $m$ cuts across the cake. Could you help check if John’s cuts successfully divide the candles on the cake?

Formally, the cake is a circle of radius $r$ centered at $(0, 0)$. The candles are $n$ distinct points located strictly inside the circle. Each cut is a straight line $ax + by + c = 0$, described by three coefficients $a$, $b$, and $c$.

-----Input-----
Input starts with three integers $n$ ($1 \leq n \leq 50$), $m$ ($1 \leq m \leq 15$), and $r$ ($1 \leq r \leq 100$) on the first line.

The next $n$ lines give the locations of the candles. Each line has two integers $x$ and $y$ giving the coordinates of one candle ($0 \leq \sqrt {x^2 + y^2} < r$).

The next $m$ lines give the coefficients of the cutting lines. Each line has three integers $a$, $b$, and $c$ ($0 \leq |a|, |b| \leq 100, 0 \leq |c| \leq 20000$) describing a line of the form $ax + by + c = 0$. The values $a$ and $b$ are not both zero.

All candles and lines are distinct. No candle is on a cut line. No line is completely outside or tangent to the cake. The input guarantees that the number of cake pieces remains the same if any cut line is shifted by at most $10^{-4}$ in any direction. The input also guarantees that each candle remains in the interior of the same piece of cake if its position is shifted by at most $10^{-4}$ in any direction.

-----Output-----
Output “yes” if John’s cuts successfully divide the cake so that each piece he obtains has exactly one candle on it. Otherwise, output “no”.

-----Examples-----
Sample Input 1:
4 2 3
0 1
1 0
-1 0
0 -1
-1 1 0
2 1 0
Sample Output 1:
yes

Sample Input 2:
4 3 3
0 1
1 2
-1 2
0 -1
-1 1 -2
-1 -1 2
0 -1 0
Sample Output 2:
no

Sample Input 3:
3 2 3
2 1
0 0
-1 -2
1 1 -2
3 6 12
Sample Output 3:
yes
```

### Ambiguous Promt
```text
i have a circular cake of radius r centered at origin with n points inside it and m straight lines ax+by+c=0 slicing across the circle and i want to check if the lines split the circle into exacty n regions with one point in each region, anyway write a code to print yes or no.

-----Input-----
Input starts with three integers $n$ ($1 \leq n \leq 50$), $m$ ($1 \leq m \leq 15$), and $r$ ($1 \leq r \leq 100$) on the first line.

The next $n$ lines give the locations of the candles. Each line has two integers $x$ and $y$ giving the coordinates of one candle ($0 \leq \sqrt {x^2 + y^2} < r$).

The next $m$ lines give the coefficients of the cutting lines. Each line has three integers $a$, $b$, and $c$ ($0 \leq |a|, |b| \leq 100, 0 \leq |c| \leq 20000$) describing a line of the form $ax + by + c = 0$. The values $a$ and $b$ are not both zero.

All candles and lines are distinct. No candle is on a cut line. No line is completely outside or tangent to the cake. The input guarantees that the number of cake pieces remains the same if any cut line is shifted by at most $10^{-4}$ in any direction. The input also guarantees that each candle remains in the interior of the same piece of cake if its position is shifted by at most $10^{-4}$ in any direction.

-----Output-----
Output “yes” if John’s cuts successfully divide the cake so that each piece he obtains has exactly one candle on it. Otherwise, output “no”.

-----Examples-----
Sample Input 1:
4 2 3
0 1
1 0
-1 0
0 -1
-1 1 0
2 1 0
Sample Output 1:
yes

Sample Input 2:
4 3 3
0 1
1 2
-1 2
0 -1
-1 1 -2
-1 -1 2
0 -1 0
Sample Output 2:
no

Sample Input 3:
3 2 3
2 1
0 0
-1 -2
1 1 -2
3 6 12
Sample Output 3:
yes
```

---

## Task 40: Problem ID 3024 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/isomorphicinversion](https://open.kattis.com/problems/isomorphicinversion)

### Clear Prompt (Canonical Baseline)
```text
Let $s$ be a given string of up to $10^6$ digits. Find the maximal $k$ for which it is possible to partition $s$ into $k$ consecutive contiguous substrings, such that the $k$ parts form a palindrome. More precisely, we say that strings $s_0, s_1, \dots , s_{k-1}$ form a palindrome if $s_ i = s_{k-1-i}$ for all $0\leq i < k$.

In the first sample case, we can split the string 652526 into $4$ parts as 6|52|52|6, and these parts together form a palindrome. It turns out that it is impossible to split this input into more than $4$ parts while still making sure the parts form a palindrome.

-----Input-----
 - A nonempty string of up to $10^6$ digits.

-----Output-----
 - Print the maximal value of $k$ on a single line.

-----Examples-----
Sample Input 1:
652526
Sample Output 1:
4

Sample Input 2:
12121131221
Sample Output 2:
7

Sample Input 3:
123456789
Sample Output 3:
1
```

### Ambiguous Promt
```text
i got a long digit string s and i want to chop it into as many consecutive chunks as posible so that the sequence of chunks reads the same from left to right and right to left without reversing individual chunks, anyway write a program to find the maximum number of chunks.

-----Input-----
 - A nonempty string of up to $10^6$ digits.

-----Output-----
 - Print the maximal value of $k$ on a single line.

-----Examples-----
Sample Input 1:
652526
Sample Output 1:
4

Sample Input 2:
12121131221
Sample Output 2:
7

Sample Input 3:
123456789
Sample Output 3:
1
```

---

## Task 41: Problem ID 3025 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/goldbandits](https://open.kattis.com/problems/goldbandits)

### Clear Prompt (Canonical Baseline)
```text
In the hills of a distant land there is a valley with many villages. The villages are all ruled by a cruel king who demands that each village pay him tribute in gold each year. The villages are required to bring gold to the king as quickly as possible when he demands it.

There is a bandit village in the kingdom. The bandit village has saved no gold for the king, because they spent every bit of gold that they had! What are they going to do? Well, since they’re bandits, when they travel through other villages to get to the castle, they may (or may not) choose to steal the gold from any of those villages on their path to the castle, and present it to the king as their own.

The bandits travel through as few villages as possible to reach the castle. They also have one other consideration-after delivering the gold to the king the bandits must be able to return home. They consider it unsafe to return home traveling through a village from whom they stole gold. The bandits do not otherwise care how long it takes to return home.

Determine the maximum amount of gold the bandits can steal on their way to the king’s castle and still be able to return home safely.

-----Input-----
There will be a single test case in the input. This test case will begin with a line with two integers, $n$ ($3 \le n \le 36$) and $m$ ($n-1 \le m \le n(n-1)/2$), where $n$ is the number of villages, and $m$ is the number of roads. The villages are numbered $1 \ldots n$. Village $1$ is the bandit’s home, and village $2$ holds the king’s castle. On the next line will be $n-2$ space-separated integers $g$ ($1 \le g \le 5000$), which are the amount of gold in each village $3, 4, \ldots , n$, skipping the bandit’s home and the king’s castle. On each of the following $m$ lines will be two integers, $a$ and $b$ ($1 \le a < b \le n$) indicating that there is a road between villages $a$ and $b$. All roads are two-way. All $m$ $(a,b)$ pairs will be unique. There will be a path, direct or indirect, from every village to every other village.

-----Output-----
Output a single integer, indicating the maximum amount of gold that the bandits can purloin and still get safely home.

-----Examples-----
Sample Input 1:
3 3
1
1 2
2 3
1 3
Sample Output 1:
0

Sample Input 2:
4 4
24 10
1 3
2 3
2 4
1 4
Sample Output 2:
24

Sample Input 3:
6 8
100 500 300 75
1 3
1 4
3 6
4 5
3 5
4 6
2 5
2 6
Sample Output 3:
800
```

### Ambiguous Promt
```text
i have an unweighted graph of n nodes where i need to take a shortest path from node 1 to node 2 and collect weights from some nodes along that path such that there still exists some path back from node 2 to node 1 avoiding all nodes i took weight from, anyway write a code to find the max weight i can collect.

-----Input-----
There will be a single test case in the input. This test case will begin with a line with two integers, $n$ ($3 \le n \le 36$) and $m$ ($n-1 \le m \le n(n-1)/2$), where $n$ is the number of villages, and $m$ is the number of roads. The villages are numbered $1 \ldots n$. Village $1$ is the bandit’s home, and village $2$ holds the king’s castle. On the next line will be $n-2$ space-separated integers $g$ ($1 \le g \le 5000$), which are the amount of gold in each village $3, 4, \ldots , n$, skipping the bandit’s home and the king’s castle. On each of the following $m$ lines will be two integers, $a$ and $b$ ($1 \le a < b \le n$) indicating that there is a road between villages $a$ and $b$. All roads are two-way. All $m$ $(a,b)$ pairs will be unique. There will be a path, direct or indirect, from every village to every other village.

-----Output-----
Output a single integer, indicating the maximum amount of gold that the bandits can purloin and still get safely home.

-----Examples-----
Sample Input 1:
3 3
1
1 2
2 3
1 3
Sample Output 1:
0

Sample Input 2:
4 4
24 10
1 3
2 3
2 4
1 4
Sample Output 2:
24

Sample Input 3:
6 8
100 500 300 75
1 3
1 4
3 6
4 5
3 5
4 6
2 5
2 6
Sample Output 3:
800
```

---

## Task 42: Problem ID 3026 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/criticalelements](https://open.kattis.com/problems/criticalelements)

### Clear Prompt (Canonical Baseline)
```text
Zapray really loves the Algorithmic Problem Solving course, but he is struggling with it. Recently the class studied Longest Increasing Subsequence (LIS). Zapray knows well how to compute the length of LIS for a given sequence. But on the exam paper there appears to be a different question: “We say an element in a sequence is critical, if removing it will cause the sequence’s LIS length to decrease. Can you find all the critical elements in the sequence below?” Zapray soon realizes that this is a much bigger challenge.

-----Input-----
The input starts with a single integer $n$ ($2 \leq n \leq 10^5$), the length of the given sequence. The next line has $n$ integers giving the numbers in the sequence. The given sequence is a permutation in which each integer from $1$ to $n$ appears exactly once.

-----Output-----
Output all critical elements in the sequence in ascending order. If none of the elements are critical, output “-1”.

-----Examples-----
Sample Input 1:
4
1 3 2 4
Sample Output 1:
1 4

Sample Input 2:
5
1 2 3 4 5
Sample Output 2:
1 2 3 4 5

Sample Input 3:
4
2 1 4 3
Sample Output 3:
-1
```

### Ambiguous Promt
```text
i have a permutation of length n and i want to find all numbers in it that belong to every single longest increasing subsequence so removing them would shrink the LIS lenght, anyway write a program to print those critical values in sorted order or -1.

-----Input-----
The input starts with a single integer $n$ ($2 \leq n \leq 10^5$), the length of the given sequence. The next line has $n$ integers giving the numbers in the sequence. The given sequence is a permutation in which each integer from $1$ to $n$ appears exactly once.

-----Output-----
Output all critical elements in the sequence in ascending order. If none of the elements are critical, output “-1”.

-----Examples-----
Sample Input 1:
4
1 3 2 4
Sample Output 1:
1 4

Sample Input 2:
5
1 2 3 4 5
Sample Output 2:
1 2 3 4 5

Sample Input 3:
4
2 1 4 3
Sample Output 3:
-1
```

---

## Task 43: Problem ID 3027 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/stampstamp](https://open.kattis.com/problems/stampstamp)

### Clear Prompt (Canonical Baseline)
```text
Bureaucrats love bureaucracy. This assertion seems fairly obvious but a less obvious observation is the amount of paperwork this means!

When paperwork is complete, a bureaucrat stamps the official document with their official stamp of office. Some bureaucrats are extra thorough and stamp the document multiple times. We are interested primarily in bureaucrats that stamp their documents exactly twice.

A bureaucrat stamp takes up some rectangular area. For example, the below is a bureaucrat stamp:

       ..#..#.. .######. ..#..#..

When the bureaucrat stamps the paper twice it is potentially moved to a different location on the paper, but it is not rotated. The stamp will always be axis aligned. The ’#’ symbol on a stamp covers the paper with black ink at the cell on the paper that is pressed. A ’.’ doesn’t leave any marks on the paper nor does it remove a mark. If a cell of the paper is marked twice it is not discernable from a cell that is marked once.

You will be given a mark on a paper that was stamped twice by a stamp. Your task is to determine the minimum number of nubs (’#’ symbols) that could have possibly been on the original stamp. The paper is guaranteed to be stamped twice by the entire stamp. (All of the stamp will be on the paper in both stampings)

Consider the following mark on paper:

       ..#..#.. .######. .######. ..#..#..

It could have been made with the first stamp example, with the second stamping exactly one cell below the first. Or, it could have been made with a stamp that looks like this, stamped side-by-side:

       ..#.. .###. .###. ..#..

In this case, 8 would be the correct answer.

-----Input-----
Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. Each test case will begin with a line with two integers, $n$ and $m$ ($1 \le n, m \le 500$) indicating the height and width of the mark on the paper. Each of the next $n$ lines will have exactly $m$ characters, consisting only of ‘#’ and ‘.’, representing the mark. Every test case will have at least one ‘#’.

-----Output-----
Output a single line with a single integer, indicating the minimum number of nubs of a bureaucrat’s stamp that could have possibly made the input mark by stamping exactly twice.

-----Examples-----
Sample Input 1:
4 8
..#..#..
.######.
.######.
..#..#..
Sample Output 1:
8

Sample Input 2:
3 3
...
.#.
...
Sample Output 2:
1

Sample Input 3:
2 6
.#####
#####.
Sample Output 3:
5
```

### Ambiguous Promt
```text
i have an nxm grid of '#' and '.' formed by stamping the exact same pattern twice without rotating it at two possibly shifted positions inside the grid, anyway write a code to find the smallest number of '#' cells the original stamp could have.

-----Input-----
Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. Each test case will begin with a line with two integers, $n$ and $m$ ($1 \le n, m \le 500$) indicating the height and width of the mark on the paper. Each of the next $n$ lines will have exactly $m$ characters, consisting only of ‘#’ and ‘.’, representing the mark. Every test case will have at least one ‘#’.

-----Output-----
Output a single line with a single integer, indicating the minimum number of nubs of a bureaucrat’s stamp that could have possibly made the input mark by stamping exactly twice.

-----Examples-----
Sample Input 1:
4 8
..#..#..
.######.
.######.
..#..#..
Sample Output 1:
8

Sample Input 2:
3 3
...
.#.
...
Sample Output 2:
1

Sample Input 3:
2 6
.#####
#####.
Sample Output 3:
5
```

---

## Task 44: Problem ID 3028 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/primonimo](https://open.kattis.com/problems/primonimo)

### Clear Prompt (Canonical Baseline)
```text
Primonimo is a game played on an $n \times m$ board filled with numbers taken from the range $1 \ldots p$ for some prime number $p$. At each move, a player selects a square and adds $1$ to the numbers in all squares in the same row and column as the selected square. If a square already shows the number $p$, it wraps around to $1$.

The game is won if all squares show $p$. Given an initial board, find a sequence of moves that wins the game!

-----Input-----
The input consists of a single test case. The first line contains three numbers $n \ m \ p$ denoting the number of rows $n$ ($1 \le n \le 20$), the number of columns $m$ ($1 \le m \le 20$), and a prime number $p$ ($2 \le p \le 97$). Each of the next $n$ lines consists of $m$ numbers in the range $1 \ldots p$.

-----Output-----
If a winning sequence of at most $p \cdot m \cdot n$ moves exists, output an integer $k \le p \cdot m \cdot n$ denoting the number of moves in the sequence. Then output $k$ moves as a sequence of integers that numbers the board in row-major order, starting with $1$. If there are multiple such sequences, you may output any one of them. If no winning sequence exists, output -1.

-----Examples-----
Sample Input 1:
4 5 5
2 1 1 1 2
5 3 4 4 3
4 3 3 3 2
3 1 3 3 1
Sample Output 1:
6
19 12 2 18 5 5

Sample Input 2:
3 3 3
3 1 1
1 3 2
3 2 3
Sample Output 2:
13
4 2 6 1 9 7 5 5 7 1 2 3 3

Sample Input 3:
3 2 2
1 2
2 1
1 2
Sample Output 3:
-1
```

### Ambiguous Promt
```text
i got an nxm grid of numbers from 1 to prime p where clicking a cell adds 1 modulo p (wrapping p to 1) to every cell in its entire row and column and i want to make every single cell equal to p, anyway write a program to print any valid sequence of moves or -1.

-----Input-----
The input consists of a single test case. The first line contains three numbers $n \ m \ p$ denoting the number of rows $n$ ($1 \le n \le 20$), the number of columns $m$ ($1 \le m \le 20$), and a prime number $p$ ($2 \le p \le 97$). Each of the next $n$ lines consists of $m$ numbers in the range $1 \ldots p$.

-----Output-----
If a winning sequence of at most $p \cdot m \cdot n$ moves exists, output an integer $k \le p \cdot m \cdot n$ denoting the number of moves in the sequence. Then output $k$ moves as a sequence of integers that numbers the board in row-major order, starting with $1$. If there are multiple such sequences, you may output any one of them. If no winning sequence exists, output -1.

-----Examples-----
Sample Input 1:
4 5 5
2 1 1 1 2
5 3 4 4 3
4 3 3 3 2
3 1 3 3 1
Sample Output 1:
6
19 12 2 18 5 5

Sample Input 2:
3 3 3
3 1 1
1 3 2
3 2 3
Sample Output 2:
13
4 2 6 1 9 7 5 5 7 1 2 3 3

Sample Input 3:
3 2 2
1 2
2 1
1 2
Sample Output 3:
-1
```

---

## Task 45: Problem ID 3029 (Competition)
- **Difficulty Tier:** Competition
- **Benchmark Source URL:** [https://open.kattis.com/problems/neverjumpdown](https://open.kattis.com/problems/neverjumpdown)

### Clear Prompt (Canonical Baseline)
```text
You are given a rooted tree of $N$ vertices where each vertex $v_1$ through $v_ N$ is labeled with a non-negative integer $u_1$ through $u_ N$. The vertex $v_1$ is the root.

Define a “jumping path” within the tree to be a sequence $a_1, a_2, \ldots , a_ k$ of length $k$ where $v_{a_ i}$ is an ancestor of $v_{a_ j}$ for all $1 \le i < j \le k$.

Compute two quantities for the given tree:
 - The length $L$ of the longest jumping path where the labels of the vertices are nondecreasing. That is, $u_{a_ i} \le u_{a_ j}$ for all $1 \le i < j \le L$.
 - The number $M$ of jumping paths of length $L$ where the labels of the vertices are nondecreasing. Since this number may be large, give the remainder of $M$ when divided by the prime $11092019$.

-----Input-----
The first line of input contains an integer $N$ denoting the number of vertices in the tree ($1 \leq N \leq 10^6$).

This is followed by $N$ lines of input indicating the labels $u_1$ through $u_ N$. Each label is an integer in the range $[0, 10^6]$.

The remaining $N-1$ lines describe the tree structure. Skipping the root (which has no parent) and starting with $i=2$, line $i$ gives the parent $p_ i < i$ of vertex $v_ i$.

-----Output-----
Print a single line of output with two integers separated by a space. The first integer is $L$, and the second integer is $M$ modulo the prime $11092019$.

-----Examples-----
Sample Input 1:
5
3
3
3
3
3
1
2
3
4
Sample Output 1:
5 1

Sample Input 2:
5
4
3
2
1
0
1
2
3
4
Sample Output 2:
1 5

Sample Input 3:
4
1
5
3
6
1
2
3
Sample Output 3:
3 2
```

### Ambiguous Promt
```text
i have a rooted tree with N nodes that each have a number value and i can jump downwards from any ancestor to any descendant as long as the values never decrease, anyway write a code to find the maximum number of nodes i can visit in one such path and how many different paths achieve that max length modulo 11092019.

-----Input-----
The first line of input contains an integer $N$ denoting the number of vertices in the tree ($1 \leq N \leq 10^6$).

This is followed by $N$ lines of input indicating the labels $u_1$ through $u_ N$. Each label is an integer in the range $[0, 10^6]$.

The remaining $N-1$ lines describe the tree structure. Skipping the root (which has no parent) and starting with $i=2$, line $i$ gives the parent $p_ i < i$ of vertex $v_ i$.

-----Output-----
Print a single line of output with two integers separated by a space. The first integer is $L$, and the second integer is $M$ modulo the prime $11092019$.

-----Examples-----
Sample Input 1:
5
3
3
3
3
3
1
2
3
4
Sample Output 1:
5 1

Sample Input 2:
5
4
3
2
1
0
1
2
3
4
Sample Output 2:
1 5

Sample Input 3:
4
1
5
3
6
1
2
3
Sample Output 3:
3 2
```