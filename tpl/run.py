# ###. name
# https://leetcode.com/problems/name/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {
        'nums': [2,7,11,15],
        'target': 9
        },
    'output': [[0, 1]]
    })
# TestCase 2
testcases.append({
    'input': {
        'nums': [3,2,4],
        'target': 6
        },
    'output': [[1,2]]
    })
# TestCase 3
testcases.append({
    'input': {
        'nums': [3,3],
        'target': 6
        },
    'output': [[0, 1]]
    })

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t", testcase['input'])
    print("Output:\t", sol.solution(testcase['input']['nums'], testcase['input']['target']))
    print("Exp.:\t", testcase['output'])
    # 테스트케이스 통과 여부 출력
    if sol.solution(testcase['input']['nums'], testcase['input']['target']) in testcase['output']:
        print("⭕️")
    else:
        print("❌")