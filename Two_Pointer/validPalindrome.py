#This is one of the most frequently asked Two Pointer interview questions.
#Problem Statement
#Given a string, return True if it is a palindrome after:
#Ignoring spaces
#Ignoring punctuation/special characters
#Ignoring uppercase/lowercase

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (ignore case)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Input

s = "A man, a plan, a canal: Panama"

print(is_palindrome(s))


Here is the end-to-end tracing for:

s = "A man, a plan, a canal: Panama"

Only letters are compared. Spaces, comma ,, and colon : are skipped.

Index positions
Index:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Char:   A   m a n ,   a     p  l  a  n  ,     a     c  a  n  a  l  :     P  a  n  a  m  a
Initial values
left = 0
right = 29
Iteration 1
left = 0  → s[left] = 'A'
right = 29 → s[right] = 'a'

Compare:

'A'.lower() == 'a'.lower()
'a' == 'a'

Match.

Move both pointers:

left = 1
right = 28
Iteration 2
left = 1 → s[left] = ' '

Space is not alphanumeric, so skip:

left = 2

Now:

left = 2 → s[left] = 'm'
right = 28 → s[right] = 'm'

Compare:

'm' == 'm'

Match.

Move:

left = 3
right = 27
Iteration 3
left = 3 → 'a'
right = 27 → 'a'

Compare:

'a' == 'a'

Match.

Move:

left = 4
right = 26
Iteration 4
left = 4 → 'n'
right = 26 → 'n'

Compare:

'n' == 'n'

Match.

Move:

left = 5
right = 25
Iteration 5
left = 5 → ','

Comma is not alphanumeric, so skip:

left = 6

Now:

left = 6 → ' '

Space is not alphanumeric, so skip:

left = 7

Now:

left = 7 → 'a'
right = 25 → 'a'

Compare:

'a' == 'a'

Match.

Move:

left = 8
right = 24
Iteration 6
left = 8 → ' '

Space is not alphanumeric, so skip:

left = 9

Now:

left = 9 → 'p'
right = 24 → 'P'

Compare after lowercase:

'p'.lower() == 'P'.lower()
'p' == 'p'

Match.

Move:

left = 10
right = 23
Iteration 7
left = 10 → 'l'
right = 23 → ' '

Right side is space, so skip:

right = 22

Now:

right = 22 → ':'

Colon is not alphanumeric, so skip:

right = 21

Now:

left = 10 → 'l'
right = 21 → 'l'

Compare:

'l' == 'l'

Match.

Move:

left = 11
right = 20
Iteration 8
left = 11 → 'a'
right = 20 → 'a'

Compare:

'a' == 'a'

Match.

Move:

left = 12
right = 19
Iteration 9
left = 12 → 'n'
right = 19 → 'n'

Compare:

'n' == 'n'

Match.

Move:

left = 13
right = 18
Iteration 10
left = 13 → ','

Comma is not alphanumeric, so skip:

left = 14

Now:

left = 14 → ' '

Space is not alphanumeric, so skip:

left = 15

Now:

left = 15 → 'a'
right = 18 → 'a'

Compare:

'a' == 'a'

Match.

Move:

left = 16
right = 17
Iteration 11
left = 16 → ' '

Space is not alphanumeric, so skip:

left = 17

Now:

left = 17
right = 17

Condition:

left < right
17 < 17

False.

So the loop stops.

Final answer

No mismatch was found, so:

return True

Output:

True

Main idea: the code compares only valid characters from both ends:

A m a n a p l a n a c a n a l P a n a m a

After ignoring spaces and symbols, it becomes:

amanaplanacanalpanama

This reads the same forward and backward, so it is a palindrome.