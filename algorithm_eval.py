#예제 : 리스트에서 최대값 찾기
#비교연간 및 이동연산 기반 효율성 분석
def find_max(A):
    #A는 리스트
    n = len(A) # 입력 크기
    move_count = 0 # 이동 연산 횟수
    comp_count = 0 # 비교 연산 횟수


    max_val = A[0] # 초기화(이동 1회)
    move_count += 1


    for i in range(1,n): # 1~n-1까지 반복
        comp_count += 1 #A[i] > max_val 비교 연산 1회
        if A[i] > max_val:
            max_val = A[i]
            move_count += 1
    return max_val, comp_count, move_count


#=====================
#테스트
#=====================
if __name__ == "__main__":
    data = [3, 9, 2, 7, 5, 10, 4]
    result, comp, move = find_max(data)
    print(f"비교연산횟수 : {comp}, & 이동연산횟수{move}")