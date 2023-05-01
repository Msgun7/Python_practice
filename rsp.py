# 가위 바위 보
import random

# def match_result(user_choice, computer_choice):


rsp = ["가위", "바위", "보"]
computer_choice = random.choice(rsp)
print("게임 가위 바위 보를 시작합니다.")

# def match_result(user_choice, computer_choice):
while True:
    user_choice = input()
    if user_choice in rsp:
        print("당신은", user_choice, "를 냈습니다.")
        print("컴퓨터는", computer_choice, "를 냈습니다.")
        if user_choice == "가위":
            if computer_choice == "가위":
                print("무승부입니다")
            elif computer_choice == "보":
                print("당신의 승리입니다")
            else:
                print("당신의 패배입니다")
        if user_choice == "바위":
            if computer_choice == "가위":
                print("당신의 승리입니다")
            elif computer_choice == "보":
                print("당신의 패배입니다")
            else:
                print("무승부입니다")

        if user_choice == "보":
            if computer_choice == "가위":
                print("당신의 패배입니다")
            elif computer_choice == "보":
                print("무승부입니다")
            else:
                print("당신의 승리입니다")
    break


# 3판 2선승제로 구현하시오.
# 무지성으로 만들다가 break문을 넣을 위치가 없어졌다 했습니다. ㅠㅠ
