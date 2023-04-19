# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
# 들여쓰기를 잘못하면 값이 달라진다
# print문의 위치 하나로 출력되는 행수가 달라질 수 있다.
