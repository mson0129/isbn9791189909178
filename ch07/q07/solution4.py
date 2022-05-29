from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums가 정렬되어 있지 않으므로 사용 불가능한 답 - 테스트케이스 2에서 right 포인터가 2와 1 사이를 오가며 무한 루프에 빠진다.
        # 문제에 명시되어 있지 않은 가정(nums는 순서대로 정렬되어 있다)에 기반하여 코드를 작성하지 말 것!
        # nums를 정렬하여 사용할 수는 있으나 본래 인덱스 값을 별도로 저장하고, 다시 매칭시키는 과정이 필요하므로 코드가 지저분해지고 시간 내 풀이가 어려워진다.
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]