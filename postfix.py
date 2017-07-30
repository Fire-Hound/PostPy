
class Postify:
    def __init__(self, data):
        data = "".join(data.split())
        self.expression = []
        self.stack = []
        self.operators = ['+', '-', '/', '*', '^', '(', ')']
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
                elif d == '(':
                    self.PUSH(d)
                elif self.is_of_high_presidence(d):

                    self.PUSH(d)


                elif self.is_of_same_presidence(d):
                    item = self.POP()
                    self.expression.append(item)
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
#--------------------------Usage-----------------------------------
# expr1 = "a*b+(c+d)-(e+f)+g*h/k^2"
# expr2 = "b+c*d-e+(e^2*f)"
# expr3 = "(a*b*c^2+d)+(c/d+c)"
# expr4 = "a*b+c/d"
# expr5 = "a + b * c + (d*e+f)*g"
# expr6 = "a-b-c"
# expr7 = "12-4*5^3"
# expr8 = "((12-4)*5)^3"
# expr9 = "1+(2*3-(4/5*6)*7)*8"
# expr10 = "((a+b) *c-(d-e)^(f+g))"
# for expr in [expr1,expr2,expr3,expr4,expr5,expr6,expr7,expr8,expr9,expr10]:
#     a = Postify(expr)
#     print(a.expression)
