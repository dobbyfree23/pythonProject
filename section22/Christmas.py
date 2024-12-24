import time
import random
import os


def clear_screen():
    # 운영체제에 따라 화면 지우기
    os.system('cls' if os.name == 'nt' else 'clear')


def create_tree(height, decorations):
    tree = []
    # 트리의 꼭대기 별
    tree.append(" " * (height - 2) + "★")

    # 트리의 몸통
    for i in range(height):
        spaces = " " * (height - i - 1)
        if random.random() < 0.5:  # 50% 확률로 장식 추가
            body = random.choice(decorations) * (2 * i + 1)
        else:
            body = "*" * (2 * i + 1)
        tree.append(spaces + body)

    # 트리 기둥
    tree.append(" " * (height - 2) + "|||")
    tree.append(" " * (height - 2) + "|||")

    return "\n".join(tree)


def main():
    height = 10  # 트리의 높이
    decorations = ["@", "o", "+", "*", "✿"]  # 트리 장식들
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]  # ANSI 색상 코드

    try:
        while True:
            clear_screen()
            # 랜덤 색상 선택
            color = random.choice(colors)
            # 트리 생성 및 출력
            tree = create_tree(height, decorations)
            print(color + tree)
            # "Merry Christmas!" 메시지 출력
            message = "\n" + " " * (height - 5) + "Merry Christmas! 🎄"
            print("\033[97m" + message)  # 흰색으로 메시지 출력
            time.sleep(0.5)  # 0.5초 대기

    except KeyboardInterrupt:
        print("\n\n프로그램을 종료합니다. 즐거운 크리스마스 되세요! 🎅")


if __name__ == "__main__":
    main()