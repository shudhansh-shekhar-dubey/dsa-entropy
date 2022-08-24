"""

BITWISE OPERATIONS

| = 0, _ = 1

AND: (&)
If a room has two consecutive doors, one can only enter iff both doors are open

0 0 : 0
0 1 : 0
1 0 : 0
1 1 : 1

OR: (|)
If a room has two seperate doors, one can enter if any or both door are open

0 0 : 0
0 1 : 1
1 0 : 1
1 1 : 1

XOR: (^)
If a room has a revolving door, one can only enter from one door iff other
door is closed
If both doors are partially open, one can also never enter

0 0 : 0
0 1 : 1
1 0 : 1
1 1 : 0



"""