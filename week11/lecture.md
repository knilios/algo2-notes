# NP
## Classes of Problems
- IP Problems (Polynomial-time problem)
- NP Problem (Non-polynomial-time problems) - None determistic polynomial time problem
    - The meaning of deterministic means that it does what you think.
    - Non-deterministic means that you somehow 
- EXP Problem - The problem that can be solve in exponential time. = $O(c^n)$
    - Knapsack problem $O(nW)$ 

## Can a problem be solved?
- Cannot be solved at all
    - Eg. Halting problem
- Took too long to solve => EXP problem\

## The idea
- If you already know the answer to NP problem, you can solve it in polynomial time.

# Reduction
- I want to solve a using B
- A is reduced to B
- Use B to solve A
- B is harder than A
- Has to be done in polynomial time
## Example
- solve max2(a,b) using max3(a,b,c)
    - max2(x,y) = max3(x,x,y)
- solve max3 using max2
    - max3(x,y,z) = max2(max2(x,y),z)

# Polynomial-time reduction
- $A\leq{_pB}$
- A is reduced to B in poly-time
- Use multiple Bs to solve A\
- If we can solve B in polynomial time  => we can solve a in polynomial time too

## Theorem
- James Cook showed that:
- All $NP$ problems $\leq_p$ Circut SAT (Satisfaction)
- if circle SAT $\epsilon{P}$ => All $NP\epsilon{P}$

### NP-Complete Problems
- If we can solve any Circuit SAT, we can solve any NP problems in polynomial.

## Maximum Independent set problem
- 