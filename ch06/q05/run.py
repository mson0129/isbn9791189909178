# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

import solution

testcases = list()
# TestCase 1
testcases.append({
    'input': {'strs': ["eat","tea","tan","ate","nat","bat"]},
    'output': [["bat"],["nat","tan"],["ate","eat","tea"]]
    })
# TestCase 2
testcases.append({
    'input': {'strs': [""]},
    'output': [[""]]
    })
# TestCase 3
testcases.append({
    'input': {'strs': ["a"]},
    'output': [["a"]]
    })

# Run
sol = solution.Solution()
for id, testcase in enumerate(testcases):
    print("[", "Testcase", id+1, "]")
    # Input, Output, Expectation(입력값, 출력값, 기대값)
    print("Input:\t", testcase['input']['strs'])
    print("Output:\t", sol.groupAnagrams(testcase['input']['strs']))
    print("Exp.:\t", testcase['output'])
    # 테스트케이스 통과 여부 출력
    is_correct = True
    for anagram in sol.groupAnagrams(testcase['input']['strs']):
        if sorted(anagram) not in testcase['output']:
            is_correct *= False
            break
    if is_correct:
        print("⭕️")
    else:
        print("❌")