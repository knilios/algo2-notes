# Dynamic programming (Continue)

## Example
- Fibonacci frequence
    - Divide and Conquer => O(log(n))
    - Traditional Approach => O(n)

- Observe
```
let A = | 0 1 |
        | 1 1 |


| 0 1 | X | 0 1 |
| 1 1 |   | 1 1 |

=> | something |
   | fibo-like |

```
$A^n=fibo_n$
- Now we only have to find $A^n$ which is just $A\times{A}\times{A}\times{...}$ => $O(n)$
- But wait! We can do even better!
- Try => $(((..)^2\times{A})^2)^2$
- Congratulations! You are now able to do it in $O(log(n))$!! AMAZING!

## Longest Common Subsequence (LCS)
- Given the string X and Y, find the longest common substrings
```
X="ALGORITHM"
Y="ARITHMATIC"
```
```
            | L[i-1,j-1] + 1 if X_i = Y-j
L[i,j]=max {  L[i-1,j] + 0
            | L[i,j-1] + 0
```
- **Answer** $L[m,n]$
- **Time** $O(mn)$

## Knapsack problem
- Given ```n``` items. Item ```i``` has weight $w_i$, value $v_i$. Given a bag of size $W$, find what is the maximum value that you can have.

Formally, max A $\sum_{i\epsilon{A}}v_i$ such that, $\sum_{i\epsilon{A}}w_i\leq{W}$

- Ex

|i|1|2|3|4|5|6|
|--|--|--|--|--|--|--|
|value $v_i$|1|2|3|4|5|6|
|weight $w_i$|1|2|3|3|5|3|
|value/weight|5|3|2.7|1.3|2|1.7|

- Last time, we tried every greedy algorithm. But none of them. Which in this case, greedy will not work.


