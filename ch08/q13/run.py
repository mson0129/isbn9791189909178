# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {'head': [1,2,2,1]},
    'output': [True]
    })
# TestCase 2
testcases.append({
    'input': {'head': [1,2]},
    'output': [False]
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
    if sol.isPalindrome(testcase['input']['head']) in testcase['output']:
        print("⭕️")
    else:
        print("❌")