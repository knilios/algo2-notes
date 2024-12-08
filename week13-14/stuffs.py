def multiply(answer, n):
    if answer * 2 > n:
        return answer
    return answer * 2

answer = 0
count = 0
N = int(input("Enter N: "))
while answer < N:
    answer = max(multiply(answer, N), answer + 1)
    count += 1
print(count)