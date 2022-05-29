# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {'height': [0,1,0,2,1,0,1,3,2,1,2,1]},
    'output': [6]
    })
# TestCase 2
testcases.append({
    'input': {'height': [4,2,0,3,2,5]},
    'output': [9]
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
    if sol.trap(testcase['input']['height']) in testcase['output']:
        print("⭕️")
    else:
        print("❌")