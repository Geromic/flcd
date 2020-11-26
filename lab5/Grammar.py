
class Grammar:
    def __init__(self, filepath):
        '''
        Structure:
            -1st line: space separated non-terminals (N)
            -2nd line: space separated terminals ()
            -3rd line: start (S)
            -next n lines: productions
        '''
        self.nonTerminals = []
        self.terminals = []
        self.productions = {}
        self.start = None
        self.__readFromFile(filepath)
        pass

    def print_terminals(self):
        print(self.terminals)

    def print_non_terminals(self):
        print(self.nonTerminals)

    def print_productions(self):
        print(self.productions)

    def print_production_for_non_terminal(self, nonTerm):
        print(self.productions[nonTerm])

    def __readFromFile(self, filepath):
        with open(filepath, 'r') as file:
            self.nonTerminals = file.readline().strip().split('\\')
            self.terminals = file.readline().strip().split('\\')
            self.start = file.readline().strip()
            for line in file:
                production = line.strip().split('\\')
                key = production[0].strip()
                values = list(production[1].strip().split('|'))
                self.productions[key] = values
        file.close()


grammarParser = Grammar("../resources/grammars/g1.txt")
grammarParser.print_non_terminals()
grammarParser.print_terminals()
grammarParser.print_productions()
grammarParser.print_production_for_non_terminal("S")
