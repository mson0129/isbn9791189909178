# 561. Array Partition I
# https://leetcode.com/problems/array-partition-i/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {'nums': [1,4,3,2]},
    'output': [4]
    })
# TestCase 2
testcases.append({
    'input': {'nums': [6,2,6,5,1,2]},
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
    if sol.arrayPairSum(testcase['input']['nums']) in testcase['output']:
        print("⭕️")
    else:
        print("❌")