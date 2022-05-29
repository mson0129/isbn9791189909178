# 344. Reverse String
# https://leetcode.com/problems/reverse-string/

import solution

testcases = list()
# TestCase 1
testcases.append({'input': {'s': ["h","e","l","l","o"]}, 'output': ["o","l","l","e","h"]})
# TestCase 2
testcases.append({'input': {'s': ["H","a","n","n","a","h"]}, 'output': ["h","a","n","n","a","H"]})

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    print("Input:\t", testcase['input']['s'])
    sol.reverseString(testcase['input']['s'])
    print("Output:\t", testcase['input']['s'])
    print("Exp.:\t", testcase['output'])
    if testcase['input']['s'] == testcase['output']:
        print("⭕️")
    else:
        print("❌")