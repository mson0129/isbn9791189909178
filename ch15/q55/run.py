# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {'s': "A man, a plan, a canal: Panama"},
    'output': [True]
    })
# TestCase 2
testcases.append({
    'input': {'s': "race a car"},
    'output': [False]
    })
# TestCase 3
testcases.append({
    'input': {'s': " "},
    'output': [True]
    })

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t", testcase['input'])
    print("Output:\t")
    print("Exp.:\t", testcase['output'])
    # 테스트케이스 통과 여부 출력
    if sol.findKthLargest(testcase['input']['s']) in testcase['output']:
        print("⭕️")
    else:
        print("❌")