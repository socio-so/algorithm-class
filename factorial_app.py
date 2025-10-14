import time

def factorial_iter(n):  #1
    """반복문 기반 팩토리얼"""
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def factorial_rec(n):  #2
    """재귀 기반 팩토리얼"""
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

def compare(n):  #3
    """반복 vs 재귀 결과 및 시간 비교"""
    start_a = time.time()
    iter_s = factorial_iter(n)
    end_a = time.time()

    start_b = time.time()
    rec_s = factorial_rec(n)
    end_b = time.time()

    print(f"[반복] {n}! = {iter_s}")
    print(f"[재귀] {n}! = {rec_s}")

    print("결과 일치 여부:", end=" ")
    if iter_s == rec_s:
        print("일치")
    else:
        print("불일치")
    print(f"[반복] 시간 : {end_a - start_a:.6f}    |    [재귀] 시간 : {end_b - start_b:.6f}")

def test():  #4
    test = [0, 1, 3, 5, 10, 15, 20, 30, 50, 100]
    print("\n[테스트 데이터 실행]")
    for n in test:
        start_a = time.time()
        iter_s = factorial_iter(n)
        end_a = time.time()

        start_b = time.time()
        rec_s = factorial_rec(n)
        end_b = time.time()

        print(f"n = {n} | same = {'True' if iter_s == rec_s else 'False'} | iter = {end_a - start_a:.6f} | rec = {end_b - start_b:.6f}")
        print(f"{n}! = {iter_s}")

def check(s):
    if not s.isdigit():  # 숫자로만 구성되어 있는지 확인
        print("정수(0 이상의 숫자)만 입력하세요.\n")
        return None
    return int(s)

def menu():
    """메뉴 출력"""
    print("=" * 55)
    print("============== Factorial Tester ===============")
    print("1) n을 반복문으로 계산하기")
    print("2) n을 재귀함수로 계산하기")
    print("3) 두 방법의 결과/시간 비교")
    print("4) 준비된 테스트 데이터 일괄 실행")
    print("q) 종료")
    print("========================================================")

def main():
    """메인 함수"""
    while True:
        menu()
        cc = input("메뉴를 선택하세요: ").strip().lower()

        if cc == "1":
            s = input("정수를 입력하세요: ").strip()
            n = check(s)
            if n is None:
                continue
            print(f"[반복] {n}! = {factorial_iter(n)}\n")

        elif cc == "2":
            s = input("정수를 입력하세요: ").strip()
            n = check(s)
            if n is None:
                continue
            try:
                print(f"[재귀] {n}! = {factorial_rec(n)}\n")
            except RecursionError:
                print("입력값이 너무 커서 재귀 계산은 불가능합니다.\n")

        elif cc == "3":
            s = input("정수를 입력하세요: ").strip()
            n = check(s)
            if n is None:
                continue
            compare(n)
            print()

        elif cc == "4":
            test()

        elif cc == "q":
            print("종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 입력해주세요\n")

if __name__ == "__main__":
    main()
