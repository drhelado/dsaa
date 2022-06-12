class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        a = nums
        n = len(nums)

        prefix = [1] * n
        postfix = [1] * n
        result = [1] * n

        for i in range(n - 1):
            v = a[i]
            if i == 0:
                prefix[i] = v
            else:
                prefix[i] = prefix[i - 1] * v

        # print(pre)

        for i in range(n - 1, 0, -1):
            v = a[i]
            if i == n - 1:
                postfix[i] = v
            else:
                postfix[i] = postfix[i + 1] * v


        # print(pos)



#         # r = []

        for i in range(n):
            # v = a[i]
            if i == 0:
                result[i] = postfix[i + 1]
            elif i == n -1:
                result[i] = prefix[i - 1]
            else:
                result[i] = prefix[i - 1] * postfix[i + 1]
                # s = pre[i - 1] * pos[i + 1]

            # r.append(s)

        return result
