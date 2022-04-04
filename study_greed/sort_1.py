from numpy import True_


N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(K):
    if A[i] < B[i]:
        # 두 원소를 교체
        A[i], B[i] = B[i], A[i]

    else:
        break

print(sum(A))
