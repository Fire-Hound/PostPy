
class Postify:
    def __init__(self, data):

        self.expression = []
        self.stack = []
        self.operators = ['+', '-', '/', '*', '^', '(', ')']
        data = "".join(data.split()) # Removing whitespace
        self.postify(data)


    def POP(self):
        return self.stack.pop()

    def PUSH(self, item):
        self.stack.append(item)

    def postify(self, data):
        self.PUSH('(')

        data = data + ')'
        for d in data:
            if d in self.operators:
                if d == ')':
                    self.POP_until_Lbracket()
                elif self.is_of_high_presidence(d):

                    self.PUSH(d)


                elif self.is_of_same_presidence(d):
                    self.PUSH(d)

                else:
                    if self.stack[-1] == '(': # ignoring left bracket or else it will be added to our expression
                        self.PUSH(d)
                        continue
                    item = self.POP()
                    self.expression.append(item)
                    self.PUSH(d)
            else:
                self.expression.append(d)
                
    def is_of_same_presidence(self, operator):
        if operator in ['(', ')'] and self.stack[-1] in ['(', ')']:
            return True
        elif operator in ['*', '/'] and self.stack[-1] in ['*', '/']:
            return True
        elif operator in ['+', '-'] and self.stack[-1] in ['+', '-']:
            return True
        elif operator == '^' and self.stack[-1] == '^':
            return True
        else:
            return False
        
    def is_of_high_presidence(self, operator):
        presidence = ['(',')','^','/','*','+','-']
        presidence_index = [4,4,3,2,2,1,1]
        o = presidence.index(operator)  #Operator's index
        s = presidence.index(self.stack[-1]) #Operator in stack index
        if presidence_index[o] > presidence_index[s]:
            return True
        else:
            return False
        
    def POP_until_Lbracket(self):
            while True:
                item = self.POP()

                if item == '(':
                    break
                self.expression.append(item)
#-------USAGE---------
#expr = "(a+b)*d"
#a = Postify(expr)
#print(a.expression)
#print(a.stack)
