# Example 1
# 시간 복잡도 표기할 때 널리 쓰이는 방법
# n은 입력 값의 수
# 목표 값을 찾는 것은 사전에 정렬한 후에 투 포인터를 사용하는 것이 시간 복잡도 성능이 더 좋음
# 반복문은 O(n), 이중 반복문은 O(n^2), 삼중 반복문은 O(n^3) ...
for n in range(1, 15 + 1):
    print(n, n ** 2, 2 ** n)