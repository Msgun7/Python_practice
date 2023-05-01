import random

user = 0
computer = 0


def match_result(user_input, computer_choice):
    global user
    global computer
    print(f"당신은 {user_input}을(를) 냈습니다!")
    print(f"컴퓨터는 {computer_choice}을(를) 냈습니다!")
    if user_input == '가위':
        if computer_choice == '가위':
            return "비겼다."
        elif computer_choice == '바위':
            computer += 1
            return "졌다."
        else:
            user += 1
            return "이겼다."
    elif user_input == '바위':
        if computer_choice == '가위':
            user += 1
            return "이겼다."
        elif computer_choice == '바위':
            return "비겼다."
        else:
            computer += 1
            return "졌다."
    else:
        if computer_choice == '가위':
            computer += 1
            return "졌다."
        elif computer_choice == '바위':
            user += 1
            return "이겼다."
        else:
            return "비겼다."


options = ['가위', '바위', '보']


while user < 2 and computer < 2:
    computer_choice = random.choice(options)
    user_input = input("가위, 바위, 보 중에서 골라주세요: ")
    if user_input not in options:
        print("잘못 입력하셨습니다.")
        continue

    result = match_result(user_input, computer_choice)
    print(result)
    print(f"전적 당신:{user}승 , 컴퓨터{computer}승")

if user == 2:
    print("당신의 승리입니다.")
elif computer == 2:
    print("컴퓨터의 승리입니다.")
