def max_area(height):
    left = 0
    right = len(height) - 1

    max_water = 0

    while left < right:

        width = right - left
        current_area = min(height[left], height[right]) * width

        if current_area > max_water:
            max_water = current_area

        # Move the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Input
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

result = max_area(height)

print(result)