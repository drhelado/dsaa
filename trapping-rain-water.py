class Solution:
    def trap(self, height: List[int]) -> int:

        print(height)

        # maintain two pointers left and right, pointing to the leftmost and
        # rightmost index of the input list
        (left, right) = (0, len(height) - 1)

        print('left, right', (left, right))

        water = 0

        maxLeft = height[left]
        maxRight = height[right]

        while left < right:

            if height[left] <= height[right]:
                left += 1
                maxLeft = max(maxLeft, height[left])
                water += (maxLeft - height[left])
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                water += (maxRight - height[right])

        return water
