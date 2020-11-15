class FiniteAutomata:
    states = []
    alphabet = []
    initial = ''
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
            self.initial = file.readline().strip()
            self.final = file.readline().strip().split(' ')
            for line in file:
                transition = line.strip().split(' ')
                if (transition[0], transition[1]) not in self.transitions.keys():
                    self.transitions[(transition[0], transition[1])] = [transition[2]]
                else:
                    self.transitions[(transition[0], transition[1])].append(transition[2])
        file.close()

    def print_states(self):
        print(self.states)

    def print_alphabet(self):
        print(self.alphabet)

    def print_transitions(self):
        print(self.transitions)

    def print_final_states(self):
        print(self.final)

    def is_DFA(self):
        for path in self.transitions.keys():
            if len(self.transitions[path]) > 1:
                return False
        return True

    def check_sequence(self, sequence):
        current_state = self.initial
        while len(sequence) > 0:
            transition = (current_state, sequence.pop(0))
            current_state = self.transitions[transition][0] if transition in self.transitions.keys() else None
            if current_state is None:
                return False
        return current_state in self.final

    def check_sequence_wrapper(self):
        sequence = input("Give a sequence: ").strip().split(' ')
        if len(sequence) == 0:
            print("Empty sequence not allowed")
            return

        if self.check_sequence(sequence):
            print("Sequence is accepted")
        else:
            print("Sequence is not accepted")


    def print_menu(self):
        print("Menu:\n1. Print states\n2. Print alphabet\n3. Print transitions\n4. Print final states")
        if self.is_DFA():
            print("5. Check sequence\n6. Exit\n")
        else:
            print("5. Exit\n")

    def run(self):
        cmds = {1: self.print_states, 2: self.print_alphabet,
                3: self.print_transitions, 4: self.print_final_states}

        # the choice to verify a sequence will only appear if the fa is deterministic
        if self.is_DFA():
            cmds[5] = self.check_sequence_wrapper

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
