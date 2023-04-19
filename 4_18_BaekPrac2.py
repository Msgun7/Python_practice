# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    a + b
    print(a+b)

# T를 입력받고 반복문 안에 T만큼의 횟수를 입력받도록 수식을 넣어 합을 그때그때 출력하는방식으로 짜보았습니다.
