# Ford-Fulkerson algorithm


```
Gf = g
Delta = largest number than 2^k <= n
While (Delta >= 1){
    F = F U P
    Update Gf
}
```
- The idea is to go to the larger street first and then go to the smaller ones later.

# Capacity scalling
```
Gf = g 
n is the largest capacity
Delta: largest number that makes 2^delta <= n
While (Delta >= 1){
    get the augment path which the capacity >= Delta
    F = F U P
    Update Gf
    Delta = Delta / 2
}
```

# Matching Problems
- Given the matching we can now solve it with network flow.

# Edge disjoint path using network flow
- Assign all of the edge to be 1 and then solve it like network flow. Boom, it's done!