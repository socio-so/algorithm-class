def climbing_stairs(n):
    # 1차원 테이블 준비
    table = [0] * (n + 1)

    table[0] = 1
    if n >= 1:
        table[1] = 1

    # Bottom-up 방식으로 테이블 채우기
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table

n = int(input("계단의 개수를 입력하시오 : "))
table = climbing_stairs(n)

print(f"{n}개의 계단을 오르는 방법의 수는 {table[n]}가지 수입니다ef climb_stairs_dp(n):
