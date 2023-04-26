import random

answer = random.randint(10, 100)

while True:
    user_input = int(input())
    if user_input == answer:
        print("정답입니다")
        break
    else:
        if answer > user_input:
            print("틀렸습니다. 답은 더욱 큰 수 입니다.")
        elif answer < user_input:
            print("틀렸습니다. 답은 더욱 작은수입니다.")
        print("다시 답을 입력해주세요 : ",end="")
        user_input
print("게임이 끝났습니다")
