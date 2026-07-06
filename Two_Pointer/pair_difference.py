def pair_difference(arr, k):
    left = 0
    right = 1

    while right < len(arr):

        # Avoid comparing the same element
        if left == right:
            right += 1
            continue

        diff = arr[right] - arr[left]

        if diff == k:
            print(f"Pair Found: ({arr[left]}, {arr[right]})")
            left += 1
            right += 1

        elif diff < k:
            right += 1

        else:
            left += 1

============================================================================================
# Input
arr = [1, 2, 3, 5, 7, 8]
k = 3

pair_difference(arr, k)



Input
arr = [1, 2, 3, 5, 7, 8]
k = 3

We need to find pairs whose difference is 3.

Initial State
left = 0
right = 1

Array with indices:

Index : 0  1  2  3  4  5
Value : 1  2  3  5  7  8

Pointers:

Index : 0  1  2  3  4  5
Value : 1  2  3  5  7  8
        L  R
Iteration 1

Condition:

while right < len(arr)
1 < 6

✔ True

Check
if left == right
0 == 1

False

Calculate difference

diff = arr[right] - arr[left]
diff = 2 - 1
diff = 1

Compare

if diff == k
1 == 3

False

Next

elif diff < k
1 < 3

✔ True

Since the difference is too small, we need a larger difference.

Move the right pointer:

right += 1

Now

left = 0
right = 2

Pointers

1  2  3  5  7  8
L     R
Iteration 2

Difference

3 - 1
2

Compare

2 == 3

False

2 < 3

✔ True

Difference is still small.

Move

right += 1

Now

left = 0
right = 3

Pointers

1  2  3  5  7  8
L        R
Iteration 3

Difference

5 - 1
4

Compare

4 == 3

False

4 < 3

False

Go to

else:

Difference is too large.

To reduce it, move the left pointer.

left += 1

Now

left = 1
right = 3

Pointers

1  2  3  5  7  8
   L     R
Iteration 4

Difference

5 - 2
3

Compare

3 == 3

✔ True

Pair found

(2,5)

Print

Pair Found: (2,5)

Move both

left += 1
right += 1

Now

left = 2
right = 4

Pointers

1  2  3  5  7  8
      L     R
Iteration 5

Difference

7 - 3
4

Compare

4 == 3

False

4 < 3

False

Go to

else

Move

left += 1

Now

left = 3
right = 4

Pointers

1  2  3  5  7  8
         L  R
Iteration 6

Difference

7 - 5
2

Compare

2 == 3

False

2 < 3

✔ True

Difference is too small.

Move

right += 1

Now

left = 3
right = 5

Pointers

1  2  3  5  7  8
         L     R
Iteration 7

Difference

8 - 5
3

Compare

3 == 3

✔ True

Pair found

(5,8)

Move both

left += 1
right += 1

Now

left = 4
right = 6
Loop Condition
while right < len(arr)

becomes

6 < 6

False

Loop ends.

Final Output
Pair Found: (2, 5)
Pair Found: (5, 8)