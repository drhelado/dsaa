class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if (len(digits) == 0):
            return [];

        nos = list(digits)

        data = dict()
        data[0] = []
        data[1] = []
        data[2] = ['a', 'b', 'c']
        data[3] = ['d', 'e', 'f']
        data[4] = ['g', 'h', 'i']
        data[5] = ['j', 'k', 'l']
        data[6] = ['m', 'n', 'o']
        data[7] = ['p', 'q', 'r', 's']
        data[8] = ['t', 'u', 'v']
        data[9] = ['w', 'x', 'y', 'z']

        combs = []
        execute = ''
        execute_2 = ''
        execute_3 = ''

        for i, v in enumerate(nos):
            execute += 'for letter'+ str(i) +' in data['+ v +']: \n'
            _i = i + 1
            execute += '\t' * _i

        for i, v in enumerate(nos):
            execute_3 +=  'letter'+ str(i) +' + '

        execute_3 = execute_3[:-3]

        execute_2 += 'combs.append('+ execute_3 +')'

        # print(execute + execute_2)
        # return []
        exec(execute + execute_2)
        return combs
