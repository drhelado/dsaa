# trynna have fun while leetcoding away hahaha
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        area = 0

        while left < right:

            shortest_penile_object = min(height[left], height[right])
            penile_object_girth = right - left

            highest_penetration_achievable = shortest_penile_object * penile_object_girth

            area = max(area, highest_penetration_achievable)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                right -= 1

            print(area)

            # print(highest_penetration)
            # break

        return area
