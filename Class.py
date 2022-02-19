from prettytable import PrettyTable

class conversion(object):
    def __init__(self,n):
        self.nfa = {}
        self.n = n
        self.finall_state = []
        self.dfa_states = []
        self.dfa = {}
        self.keys = ['0']
        self.path = ['a','b']
        self.nfa_table = []
        self.dfa_table = []
        self.dfa_finall_states = []
        
    def input_state_path(self):
        print("States must Start with 0 --> {}\n".format(self.n))
        for i in range(self.n):  
            state = input("Enter State Name: ")
            self.nfa[state] = {}
            for j in range(2):
                path = input("Enter Path: ")
                print("Enter finall state that connect to state {} with path {}.".format(state,path))
                conection_state = [x for x in input().split()]
                print()
                self.nfa[state][path] = conection_state

        print("Enter finall state: ")
        self.finall_state = [x for x in input().split()]

        print("\nNFA is: \n",self.nfa,"\n")

    def nfa_table_(self):
        conversion.input_state_path(self)
        states = [x for x in range(self.n)]

        path_a = []
        for i in range(self.n):
            s = "".join(self.nfa[str(i)]['a'])
            if s == '':
                path_a.append('[]')
            else:
                path_a.append(s)

        path_b = []
        for i in range(self.n):
            s = "".join(self.nfa[str(i)]['b'])
            if s == '':
                path_b.append('[]')
            else:
                path_b.append(s)

        self.nfa_table = PrettyTable(['States','a','b'])
        for i in range(self.n):
            self.nfa_table.add_row([states[i],path_a[i],path_b[i]])

        print("NFA Table is: ")
        print(self.nfa_table,"\n")

    def dfa_first_row(self):
        self.dfa['0'] = {}
        
        for i in range(2):
            s = "".join(self.nfa['0'][self.path[i]])
            self.dfa['0'][self.path[i]] = s
            if s not in self.keys: 
                self.dfa_states.append(s)
                self.keys.append(s)

    def dfa_other_rows(self):
        conversion.dfa_first_row(self)
        
        while len(self.dfa_states) != 0:
            self.dfa[self.dfa_states[0]] = {}
            for _ in range(len(self.dfa_states[0])):
                for i in range(len(self.path)):
                    t = []
                    for j in range(len(self.dfa_states[0])):
                        t += self.nfa[self.dfa_states[0][j]][self.path[i]]
                    s = "".join(t)
                    if s not in self.keys:
                        self.dfa_states.append(s)
                        self.keys.append(s)
                    self.dfa[self.dfa_states[0]][self.path[i]] = s
                
            self.dfa_states.remove(self.dfa_states[0])

        print("\nDFA is: \n",self.dfa,"\n")

    def dfa_table_(self):
        conversion.dfa_other_rows(self)

        states = list(self.dfa.keys())
        
        
        path_a = []
        for i in states:
            s = "".join(self.dfa[str(i)]['a'])
            path_a.append(s)

        path_b = []
        for i in states:
            s = "".join(self.dfa[str(i)]['b'])
            path_b.append(s)

        self.dfa_table = PrettyTable(['States','a','b'])
        for i in range(len(states)):
            self.dfa_table.add_row([states[i],path_a[i],path_b[i]])

        print("DFA Table is: ")
        print(self.dfa_table,"\n")

        for i in states:
            for j in i:
                if j in self.finall_state:
                    self.dfa_finall_states.append(i)
                    break

        print("DFA Finall states are: ",self.dfa_finall_states,"\n")
