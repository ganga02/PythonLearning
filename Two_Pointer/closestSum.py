def closest_pair(arr, target):
    left = 0
    right = len(arr) - 1

    min_diff = float('inf')
    pair = ()

    while left < right:

        current_sum = arr[left] + arr[right]
        diff = abs(target - current_sum)

        if diff < min_diff:
            min_diff = diff
            pair = (arr[left], arr[right])

        if current_sum < target:
            left += 1

        elif current_sum > target:
            right -= 1

        else:
            break

    return pair


# Input
arr = [1, 3, 4, 7, 10]
target = 15

result = closest_pair(arr, target)

print("Closest Pair =", result)
====================================================

Input
arr = [1, 3, 4, 7, 10]
target = 15

Array with indices

Index : 0  1  2  3   4
Value : 1  3  4  7  10
Initial Values
left = 0
right = 4

min_diff = float('inf')
pair = ()
What is float('inf')?

It means positive infinity.

Initially we don't know the closest pair, so we assume the difference is infinitely large.

min_diff = ∞

Pointers

1   3   4   7   10
L               R
Iteration 1
Current pointers
left = 0
right = 4

Values

arr[left] = 1
arr[right] = 10
Calculate current sum
current_sum = arr[left] + arr[right]
current_sum = 1 + 10
11
Difference from target
diff = abs(target - current_sum)
= abs(15 - 11)
= abs(4)
= 4
Compare with minimum difference

Current

diff = 4
min_diff = ∞

Check

if diff < min_diff
4 < ∞

✔ True

Update

min_diff = 4
pair = (1,10)

Current best answer

Closest Pair = (1,10)
Minimum Difference = 4
Move Pointer

Check

if current_sum < target
11 < 15

✔ True

Current sum is too small.

We need a larger sum.

Move

left += 1

Now

left = 1
right = 4

Pointers

1   3   4   7   10
    L           R
Iteration 2

Values

3
10

Current sum

3 + 10 = 13

Difference

abs(15-13)
2

Compare

2 < 4

✔ True

Update

min_diff = 2
pair = (3,10)

Current answer

Closest Pair = (3,10)
Difference = 2

Current sum

13 < 15

Move

left += 1

Now

left = 2
right = 4

Pointers

1   3   4   7   10
        L       R
Iteration 3

Values

4
10

Current sum

4 + 10
14

Difference

abs(15-14)
1

Compare

1 < 2

✔ True

Update

min_diff = 1
pair = (4,10)

Current best answer

Closest Pair = (4,10)
Difference = 1

Current sum

14 < 15

Move

left += 1

Now

left = 3
right = 4

Pointers

1   3   4   7   10
            L   R
Iteration 4

Values

7
10

Current sum

7 + 10
17

Difference

abs(15-17)
2

Compare

2 < 1

False

Do not update.

Current best pair remains

(4,10)

Now

17 > 15

Current sum is too large.

Need a smaller sum.

Move

right -= 1

Now

left = 3
right = 3
Loop Condition

Check

while left < right

becomes

3 < 3

False

Loop stops.

Return
return pair

Returns

(4,10)

Output

Closest Pair = (4,10)