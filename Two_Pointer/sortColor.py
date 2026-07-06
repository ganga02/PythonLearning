def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:   # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


nums = [2, 0, 2, 1, 1, 0]

print(sort_colors(nums))

=================================================================

Iteration 1

Current array

2 0 2 1 1 0

L
M
          H

Current values

nums[mid] = nums[0] = 2

Since

nums[mid] == 2

execute

nums[mid], nums[high] = nums[high], nums[mid]

Swap

2 ↔ 0

Array becomes

0 0 2 1 1 2

Now

high -= 1
high = 4

Notice

mid

does NOT move.

Pointers

0 0 2 1 1 2

L
M
        H

Why?

Because the new value

0

came from the end.

We haven't checked it yet.

Iteration 2

Current array

0 0 2 1 1 2

L
M
        H

Current value

nums[mid]=0

Since

nums[mid]==0

Swap

nums[low]

with

nums[mid]

Both are the same index.

Nothing changes.

Array

0 0 2 1 1 2

Move

low+=1
mid+=1

Pointers

0 0 2 1 1 2

  L
  M
        H

Current

low=1
mid=1
high=4
Iteration 3

Current array

0 0 2 1 1 2

  L
  M
        H

Current value

nums[mid]=0

Again

Swap

0 ↔ 0

Array

0 0 2 1 1 2

Move

low=2
mid=2

Pointers

0 0 2 1 1 2

    L
    M
        H
Iteration 4

Current

0 0 2 1 1 2

    L
    M
        H

Current value

nums[mid]=2

Swap

nums[mid]

with

nums[high]

Swap

2 ↔ 1

Array

0 0 1 1 2 2

Move

high=3

Do NOT move

mid

Pointers

0 0 1 1 2 2

    L
    M
      H

Why?

Because the new value

1

came from the right.

Need to check it.

Iteration 5

Current

0 0 1 1 2 2

    L
    M
      H

Current value

nums[mid]=1

For

1

Nothing to swap.

Just

mid+=1

Pointers

0 0 1 1 2 2

    L
      M
      H

Current

low=2
mid=3
high=3
Iteration 6

Current

0 0 1 1 2 2

    L
      M
      H

Current value

nums[mid]=1

Again

Move

mid+=1

Current

mid=4

Pointers

0 0 1 1 2 2

    L
        H
        M
Loop Condition

Check

mid<=high

becomes

4<=3

False

Loop stops.

Final Answer
0 0 1 1 2 2


| Iteration | Array           | low | mid | high | Action           |
| --------- | --------------- | --- | --- | ---- | ---------------- |
| Start     | `[2,0,2,1,1,0]` | 0   | 0   | 5    | Initialize       |
| 1         | `[0,0,2,1,1,2]` | 0   | 0   | 4    | Swap 2 with high |
| 2         | `[0,0,2,1,1,2]` | 1   | 1   | 4    | Swap 0 with low  |
| 3         | `[0,0,2,1,1,2]` | 2   | 2   | 4    | Swap 0 with low  |
| 4         | `[0,0,1,1,2,2]` | 2   | 2   | 3    | Swap 2 with high |
| 5         | `[0,0,1,1,2,2]` | 2   | 3   | 3    | 1 → move mid     |
| 6         | `[0,0,1,1,2,2]` | 2   | 4   | 3    | 1 → move mid     |
