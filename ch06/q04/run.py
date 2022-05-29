# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {
        'paragraph': "Bob hit a ball, the hit BALL flew far after it was hit.",
        'banned': ["hit"]
        },
    'output': "ball"})
# TestCase 2
testcases.append({
    'input': {
        'paragraph': "a.",
        'banned': []
        },
    'output': "a"})

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t", testcase['input'])
    print("Output:\t", sol.mostCommonWord(testcase['input']['paragraph'], testcase['input']['banned']))
    print("Exp.:\t", testcase['output'])
    # 테스트케이스 통과 여부 출력
    if sol.mostCommonWord(testcase['input']['paragraph'], testcase['input']['banned']) == testcase['output']:
        print("⭕️")
    else:
        print("❌")