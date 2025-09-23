#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 홍길동
#  작성일: 2024-09-15
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################


def factorial_iter(n):
    #반복문 기반 n! 계산
    result = 1
    for k in range(2, n+1):
        result *= k
    return result


def factorial_rec(n):
    #재귀 호풀
    if n==1:
        return 1
    return n * factorial_rec(n-1)


def main():
    """Main console loop"""
    while True:
        s = input("정수를 입력하시오(종료를 원하시면 q 또는 quit 입력):").strip()
        if s.lower() in ("q", "quit"): #if s == 'q' or s == 'quit':로 사용해도 되지만 그럴 경우 소문자 q와 quit만 가능함
            print("프로그램을 종료합니다")
            break

        n = int(s)
        print(f"반복문 기반: {factorial_iter(n)}")

        try:
            print(f"재귀 기반: {factorial_rec(n)}")
        except RecursionError:
            print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

if __name__ == "__main__":
    main()
