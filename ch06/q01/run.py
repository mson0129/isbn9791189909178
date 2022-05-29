# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

import solution

testcases = list()
# TestCase 1
testcases.append({'input': {'s': "A man, a plan, a canal: Panama"}, 'output': True})
# TestCase 2
testcases.append({'input': {'s': "race a car"}, 'output': False})
# TestCase 3
testcases.append({'input': {'s': " "}, 'output': True})

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    print("Input:\t", testcase['input']['s'])
    print("Output:\t", sol.isPalindrome(testcase['input']['s']))
    print("Exp.:\t", testcase['output'])
    if sol.isPalindrome(testcase['input']['s']) == testcase['output']:
        print("⭕️")
    else:
        print("❌")