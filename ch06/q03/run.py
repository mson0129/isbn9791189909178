# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {'logs': ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]},
    'output': ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    })
# TestCase 2
testcases.append({
    'input': {'logs': ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]},
    'output': ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    })

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t", testcase['input']['logs'])
    print("Output:\t", sol.reorderLogFiles(testcase['input']['logs']))
    print("Exp.:\t", testcase['output'])
    # 정답 여부 출력
    if sol.reorderLogFiles(testcase['input']['logs']) == testcase['output']:
        print("⭕️")
    else:
        print("❌")