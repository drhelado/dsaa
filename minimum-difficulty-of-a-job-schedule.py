class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        n = len(jobDifficulty)

        # print('n', (n))

        # if there are less jobs than days, we can't divide them
        if n < d:
            return -1

        @lru_cache(None)
        def dynamicProgramming(index, remainingDays):

            # base case. if there is only one day remaining, return most difficult job
            if remainingDays == 1:
                # check jobs from current index - everything prior has already been checked
                mostDifficult = max(jobDifficulty[index:])
                return mostDifficult

            # recurrence relation
            maxsofar = 0

            answer = float('inf')

            # for j in range(index, n - remainingDays + 1):
            for j in range(index, n - remainingDays + 1):
            # for j in range(index, n - 1):
                print(j)

                maxsofar = max(maxsofar, jobDifficulty[j])
                # print('maxsofar', (maxsofar))
                answer = min(answer, maxsofar + dynamicProgramming(j + 1, remainingDays - 1))

            return answer

        return dynamicProgramming(0, d)
