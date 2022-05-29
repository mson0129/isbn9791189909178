# ###. name
# https://leetcode.com/problems/name/

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
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t")
    print("Output:\t")
    print("Exp.:\t")
    # 정답 여부 출력
    if sol.answer_function() == testcase['output']:
        print("⭕️")
    else:
        print("❌")