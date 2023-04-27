import random

answer = random.randint(10, 100)

chance = 10
count = 0
while True:
    user_input = int(input())
    count += 1
    if user_input == answer:
        print("정답입니다.")
        chance = int(input())  # 정답이 나왔을 시에는 반복횟수 변경
        count = 0
        answer = random.randint(10, 100)

    elif user_input > answer:
        print("down")
    else:
        print("up")
    if chance == count:
        print('횟수가 초과되었습니다.')
        break
print("게임이 끝났습니다.")


