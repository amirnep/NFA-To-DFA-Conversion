import Class as c

n = int(input("Enter how many states do you want to add: "))

if __name__ == '__main__': #Run Program.
    a = c.conversion(n)
    a.nfa_table_()
    a.dfa_table_()

quit = input("Press Enter To Exit Program.")
