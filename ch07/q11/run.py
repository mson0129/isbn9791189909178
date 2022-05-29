# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {'nums': [1,2,3,4]},
    'output': [[24,12,8,6]]
    })
# TestCase 2
testcases.append({
    'input': {'nums': [-1,1,0,-3,3]},
    'output': [[0,0,9,0,0]]
    })

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t", testcase['input'])
    print("Output:\t", sol.productExceptSelf(testcase['input']['nums']))
    print("Exp.:\t", testcase['output'])
    # 테스트케이스 통과 여부 출력
    if sol.productExceptSelf(testcase['input']['nums']) in testcase['output']:
        print("⭕️")
    else:
        print("❌")