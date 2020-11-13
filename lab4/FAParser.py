class FiniteAutomata:
    states = []
    alphabet = []
    start = ''
    final = []
    transitions = {}

    def __init__(self, filename):
        self.__read_file(filename)

    def __read_file(self, filename):
        '''
        input file structure:
        1st line - alphabet
        2nd line - states
        3rd line - initial state
        4th line - final states
        next n lines - transitions (n - no. of transitions)
        '''
        with open(filename, 'r') as file:
            self.alphabet = file.readline().strip().split(' ')
            self.states = file.readline().strip().split(' ')
            self.start = file.readline().strip()
            self.final = file.readline().strip().split(' ')
            for line in file:
                transition = line.strip().split(' ')
                self.transitions[(transition[0], transition[1])] = transition[2]
        file.close()

    def print_states(self):
        print(self.states)

    def print_alphabet(self):
        print(self.alphabet)

    def print_transitions(self):
        print(self.transitions)

    def print_final_states(self):
        print(self.final)

    def print_menu(self):
        print("Menu:\n1. Print states\n2. Print alphabet\n3. Print transitions\n4. Print final states\n5. Exit\n")

    def run(self):
        cmds = {1: self.print_states, 2: self.print_alphabet, 3: self.print_transitions, 4: self.print_final_states}

        self.print_menu()

        while True:
            try:
                cmd = int(input("Give command: "))
                if cmd in cmds.keys():
                    cmds[cmd]()
                else:
                    break
            except ValueError:
                print("Invalid format!")


fa = FiniteAutomata("FA.in")
fa.run()
