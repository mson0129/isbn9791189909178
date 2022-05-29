# 15. 3Sum
# https://leetcode.com/problems/3sum/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {'nums': [-1,0,1,2,-1,-4]},
    'output': [[[-1,-1,2],[-1,0,1]]]
    })
# TestCase 2
testcases.append({
    'input': {'nums': []},
    'output': [[]]
    })
# TestCase 3
testcases.append({
    'input': {'nums': [0]},
    'output': [[]]
    })

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t", testcase['input'])
    print("Output:\t", sol.threeSum(testcase['input']['nums']))
    print("Exp.:\t", testcase['output'])
    # 테스트케이스 통과 여부 출력
    if sol.threeSum(testcase['input']['nums']) in testcase['output']:
        print("⭕️")
    else:
        print("❌")