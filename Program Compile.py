#Program Compile

"""
Enter how many states do you want to add: 4
States must Start with 0 --> 4

Enter State Name: 0
Enter Path: a
Enter finall state that connect to state 0 with path a.
0 1

Enter Path: b
Enter finall state that connect to state 0 with path b.
0

Enter State Name: 1
Enter Path: a
Enter finall state that connect to state 1 with path a.
2

Enter Path: b
Enter finall state that connect to state 1 with path b.
2

Enter State Name: 2
Enter Path: a
Enter finall state that connect to state 2 with path a.
3

Enter Path: b
Enter finall state that connect to state 2 with path b.
3

Enter State Name: 3
Enter Path: a
Enter finall state that connect to state 3 with path a.


Enter Path: b
Enter finall state that connect to state 3 with path b.


Enter finall state: 
3

NFA is: 
 {'0': {'a': ['0', '1'], 'b': ['0']}, '1': {'a': ['2'], 'b': ['2']}, '2': {'a': ['3'], 'b': ['3']}, '3': {'a': [], 'b': []}} 

NFA Table is: 
+--------+----+----+
| States | a  | b  |
+--------+----+----+
|   0    | 01 | 0  |
|   1    | 2  | 2  |
|   2    | 3  | 3  |
|   3    | [] | [] |
+--------+----+----+ 


DFA is: 
 {'0': {'a': '01', 'b': '0'}, '01': {'a': '012', 'b': '02'}, '012': {'a': '0123', 'b': '023'}, '02': {'a': '013', 'b': '03'}, '0123': {'a': '0123', 'b': '023'}, '023': {'a': '013', 'b': '03'}, '013': {'a': '012', 'b': '02'}, '03': {'a': '01', 'b': '0'}} 

DFA Table is: 
+--------+------+-----+
| States |  a   |  b  |
+--------+------+-----+
|   0    |  01  |  0  |
|   01   | 012  |  02 |
|  012   | 0123 | 023 |
|   02   | 013  |  03 |
|  0123  | 0123 | 023 |
|  023   | 013  |  03 |
|  013   | 012  |  02 |
|   03   |  01  |  0  |
+--------+------+-----+ 

DFA Finall states are:  ['0123', '023', '013', '03'] 

Press Enter To Exit Program.
"""
