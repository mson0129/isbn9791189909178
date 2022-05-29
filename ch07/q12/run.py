# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {'prices': [7,1,5,3,6,4]},
    'output': [5]
    })
# TestCase 2
testcases.append({
    'input': {'prices': [7,6,4,3,1]},
    'output': [0]
    })

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t", testcase['input'])
    print("Output:\t", sol.maxProfit(testcase['input']['prices']))
    print("Exp.:\t", testcase['output'])
    # 테스트케이스 통과 여부 출력
    if sol.maxProfit(testcase['input']['prices']) in testcase['output']:
        print("⭕️")
    else:
        print("❌")