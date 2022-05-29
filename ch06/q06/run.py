# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

import solution

testcases = list()
# TestCase 1
testcases.append({'input': {'s': "babad"}, 'output': ["bab", "ada"]})
# TestCase 2
testcases.append({'input': {'s': "cbbd"}, 'output': ["bb"]})

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t", testcase['input']['s'])
    print("Output:\t", sol.longestPalindrome(testcase['input']['s']))
    print("Exp.:\t", testcase['output'])
    # 정답 여부 출력
    if sol.longestPalindrome(testcase['input']['s']) in testcase['output']:
        print("⭕️")
    else:
        print("❌")