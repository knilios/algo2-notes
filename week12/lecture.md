## halting problem
- Is it halting or it runs forever?

## SAT Problems
- Given a boolean expression in CNF formula.
- Example $(\lor{\lor})$
- 3 SAT
- ex: $(O\lor{O}\lor{O})\lor{}(O\lor{O}\lor{O})\lor(O\lor{O}\lor{O})$
- SAT $\propto_p$ 3SAT => Turns SAT problem into 3SAT problem
    - $(a)\equiv{(a\lor{a\lor{a}})}$
    - $(a\lor{b\lor{c\lor{d}}})\equiv(a\lor{b\lor{x}})\land(x\lor{c}\lor{d})$ - Wait... There a problem with this! It's not equal! In the case where the left side is false, the right side can still be true.
        - X can only make some of the case true.
    - $(a\lor{b\lor{c\lor{d}}})\equiv(a\lor{b\lor{x}})\land(\bar{x}\lor{c}\lor{d})$ - The x bar makes things better.
        - Now, X has no power anymore.
    - $(a\lor{b\lor{c\lor{d}}}\lor{e})\equiv(a\lor{b}\lor{x})\land(\bar{x}\lor{c}\lor{y})\land(\bar{y}\lor{d}\lor{e})$
        - This one has the same idea with the one above. x and y have no power to change any value.
