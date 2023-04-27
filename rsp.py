# 가위 바위 보
import random

rsp = ["가위", "바위", "보"]
computer_choice = random.choice(rsp)
print("게임 가위 바위 보를 시작합니다.")

while True:
    user_choice = input()
    if user_choice in rsp:
        print("당신은", user_choice, "를 냈습니다.")
        print("컴퓨터는", computer_choice, "를 냈습니다.")
        if user_choice == "가위":
            computer_choice == "바위"
            print("당신의 패배입니다")
        elif user_choice == "가위":
            computer_choice == "가위"
            print("무승부입니다")
        elif user_choice == "가위":
            computer_choice == "보"
            print("당신의 승리입니다")

        if user_choice == "바위":
            computer_choice == "바위"
            print("무승부입니다")
        elif user_choice == "바위":
            computer_choice == "가위"
            print("당신의 승리입니다")
        elif user_choice == "바위":
            computer_choice == "보"
            print("당신의 패배입니다")

        if user_choice == "보":
            computer_choice == "바위"
            print("당신의 승리입니다")
        elif user_choice == "보":
            computer_choice == "가위"
            print("당신의 패배입니다")
        elif user_choice == "보":
            computer_choice == "보"
            print("무승부입니다")

#무지성으로 만들다가 break문을 넣을 위치가 없어졌다 했습니다. ㅠㅠ