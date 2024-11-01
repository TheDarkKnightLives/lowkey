import re
import sys
import operator as op 
import os

class LowKey:
    def __init__(self, sentence=""):
        self.sentence = sentence
        self.words = sentence.split()  # Store the list of words
        self.variables = {}
    
    def extract_quoted(self, word):
       #weird ass pattern shit ...  
        pattern = r'"([^"]*)"'
        # Search for the quoted segment
        quoted_segment = re.search(pattern, word)
        # Check if a quoted segment was found and return it
        if quoted_segment:
            return quoted_segment.group(1)  # Return the captured content (without quotes)
        else:
            return None      

    def extract_quoted_segment(self, sentence):
        pattern = r'"([^"]*)"'
        quoted_segment = re.search(pattern, sentence)
        if quoted_segment:
            return quoted_segment.group(1)  # Return the captured content (without quotes)
        else:
            return None      

    
    def varass(self, sen):
        variable_name = self.words[1]
        print("3rd : " + self.words[3])
    # Check for assignment
        if len(self.words) > 3 and self.words[0] == "the" and self.words[2] == "is"   or self.words[3].isdigit():

            variable_value = self.words[3]
            errorno = True

        # Check for boolean assignment
            if variable_value in ["true", "false"]:
                self.variables[variable_name] = variable_value == "true"  # Convert to boolean
                print(f"variable name: {variable_name}\nvariable value: {self.variables[variable_name]} type: boolean")
                print("Boolean assignment successful...")
                errorno = False

        # Check for integer assignment
            elif variable_value.isdigit():
                self.variables[variable_name] = int(variable_value)
                print(f"variable name: {variable_name}\nvariable value: {self.variables[variable_name]} type: integer")
                print("Integer assignment successful...")
                errorno = False

        # Check for quoted string assignment
            quoted_string = self.extract_quoted_segment(sen)
            if quoted_string:
                self.variables[variable_name] = quoted_string
                print(f"variable name: {variable_name}\nvariable value: {self.variables[variable_name]} type: string")
                print("String assignment successful...")
                errorno = False

            if errorno:
                print("No datatype found, recheck your input...")

         # Reassignment with operation
        elif len(self.words) > 5 and self.words[3].isdigit() and self.words[5].isdigit() and self.words[4] == "equals":

            num1 = int(self.words[3])
            num2 = int(self.words[5])
            operation = self.words[4]

            if operation == "plus":
                self.variables[variable_name] = num1 + num2
            elif operation == "minus":
                self.variables[variable_name] = num1 - num2
            elif operation == "into":
                self.variables[variable_name] = num1 * num2
            elif operation == "div":
                self.variables[variable_name] = num1 / num2
            elif operation == "remainder":
                self.variables[variable_name] = num1 % num2
            else:
                print("Invalid operation.")

            print(f"variable name: {variable_name}\nvalue: {self.variables[variable_name]}")

    # Variable to number operations

        elif not self.words[3].isdigit() and not isinstance(self.variables[self.words[3]], bool) :
        # Handle integer operations with existing variable
            if self.words[5].isdigit():
                num2 = int(self.words[5])
                operation = self.words[4]
                var_value = self.variables[self.words[3]]

                if operation == "plus":
                    self.variables[variable_name] = var_value + num2
                elif operation == "minus":
                    self.variables[variable_name] = var_value - num2
                elif operation == "into":
                    self.variables[variable_name] = var_value * num2
                elif operation == "div":
                    self.variables[variable_name] = var_value / num2
                elif operation == "remainder":
                    self.variables[variable_name] = var_value % num2
                else:
                    print("Invalid keyword: " + operation)

                print(f"variable name: {variable_name}\nvalue: {self.variables[variable_name]}")
            else:
            # Handle operations between two variables
                if (not isinstance(self.variables[self.words[5]], bool) and
                        not isinstance(self.variables[self.words[5]], str)):
                    var_value1 = self.variables[self.words[3]]
                    var_value2 = self.variables[self.words[5]]
                    operation = self.words[4]

                    if operation == "plus":
                        self.variables[variable_name] = var_value1 + var_value2
                    elif operation == "minus":
                        self.variables[variable_name] = var_value1 - var_value2
                    elif operation == "into":
                        self.variables[variable_name] = var_value1 * var_value2
                    elif operation == "div":
                        self.variables[variable_name] = var_value1 / var_value2
                    elif operation == "remainder":
                        self.variables[variable_name] = var_value1 % var_value2
                    else:
                        print("Invalid keyword: " + operation)

                    print(f"variable name: {variable_name}\nvalue: {self.variables[variable_name]}")
                else:
                    print("One of the variables you provided is not an integer...")

        else:
            print("I think you forgot something... (equals)")
    def say(self):
        #stringuu = self.extract_quoted_segment(sen)
        #string = stringuu.replace('"',"")
        #print("string:" +string)
        message = ""
        for word in self.words:
            if word == "say":
                continue

            if '"' in word :
                word = word.replace('"',"")
                value = type(self.variables[word])

                if value == int:
                    message += str(self.variables[word]) 
                elif value == bool:
                    message += str(self.variables[word])
                elif value == str:
                    message += str(self.variables[word])
            
            else:
            #print(stringuu)
                #print("quote seg after say ")

                #word = self.extract_quoted(word)
                #print(word)
                message +=word 

            message+= " "
            #print(message)

                
        print(message)

    def ask(self):
        varname = ""
        for word in self.words:
            if word == self.words[1]:
                varname = word;
            elif  word == "ask":
                pass
            elif word == "int":
                print("asking for int")
                x = int(input(""))
                self.variables[varname] = x
            elif word == "bool":
                x = input("").lower()

                if x == "true":
                    self.variables[varname] = True

                elif x == "false":
                    self.variables[varname] = False



                print("asking for bool")

            elif word == "str":
                x = input("")
                self.variables[varname] = x

                print("asking for str")
            else :
                print("something is wrong with this syntax")
                print("ex:ask varname type ")
                print("there are only three types available str int bool ")



        print("varname is " + varname)
    def extract( self , start , end ):
        words = self.sentence.split()
        operator = {
                "is greater than" : ">",
                "is lesser than" : "<",
                "is greater than or equal to" : ">=",
                "is lesser than or equal to " :"<=",
                "is equal to" : "==",
                "is not equal to":"!="
                }



        if start in words and end in words:
            stind = words.index(start) + 2 #stind is the start index of the start word
            enind = words.index(end) - 1#enind is the end index of the end word 

            if stind < enind:
                extr = words[stind:enind]#extracting the keys from the dictionary as tuple 
                result = ' '.join(extr)#the tuple to a string 
                varextr = self.sentence.replace(result,"")#taken out string from original for varextraction 
                resswords = varextr.split()#again spitting em to tuples to easy acces of var
                #print(varextr)
                #print(resswords)
                var1 = resswords[1]
                var2 = resswords[2]
                varornot = 0# 0 when no var , 1 when 1 var , 2 when 2 variables ... 
                #print("var1 :" + var1)
                #print("var2 :" + var2)

                print("operator :" + operator[result])
                if  result in operator:
                    oper = operator[result]
                    #print("the statement is :" + oper)
                    #print("result is :"+ result)
                    #return var1 , oper, var2

                    if var1 in self.variables.keys()  and var2 not in self.variables.keys():
                        print("var1 is a variable ")
                        varornot = 1
                        return var1 , oper , var2 ,varornot 
                    elif var1 in self.variables.keys() and var2 in self.variables.keys():
                        print("var1 and var2 are variables  ")
                        varornot = 2
                        return var1 , oper , var2 , varornot    
                        
                    else:
                        print("no variablessss ")
                        return var1 , oper , var2 , varornot

                
                        


                

                    

                else:
                    print("this is not a keyword :" + result)

                    return None, None ,None ,None 





            else:
                print("the words are misplaced ,do it in the right order  ")

        else:
            print("u do not have the do keyword ...")

    def ifcond(self):
        var1 , oper , var2 , von = self.extract("if" , "do")

        print("the var1 is " + var1)
        print("the var2 is " + var2)
        print("the operator is " + oper)
        print("variable or not thing " + str(von))#von has 0 1 2 variables . determine all that with this numbers for comparison u nigga 
        print("got the if the thing ... ")       
        
        ops = {
                "<":op.lt,
                ">":op.gt,
                "==":op.eq,
                "!=":op.ne,
                "<=":op.le,
                ">=":op.ge
                }
        expression = " "
        expression += var1 + oper + var2
        print("the expression to evaluate is :: " + expression)
        result = None 
        if von == 0 :
            try:
                number1 = int(var1)
                number2 = int(var2)
                result = eval(expression)

                
                if result:
                    line = LowKey()
                    while True:
                        sentence = input(">>>>")
        # Create an instance of LowKey with the list of words
        # Call the method to display the words
                        try:
                            line.sentence  = sentence
                            line.words = sentence.split()
                            line.tokens()

                            if sentence == "thasall":
                                print("end of the condition detected ...")
                                break
                        except Exception as e :
                            print("some compiler based error occured ... ")
                            print(e)
                            pass



                else:
                    print("the given condition is false ...")


            except ValueError:
                print("the var names that u gave are not declared ...")
            


            #print("no var detected ...")
            # print("this is good ..")
            #result = eval(expression) dont worry this is given in the top inside the try method 
#            print(result)#u need to add the not equal to operator thingy . u forgot that ...
            

            
        elif von == 1:
            print("1 var detected ...")
            
        elif von == 2:
            print("2 var detected ...")

        else:
            print("None detected , recheck ur shitty code ...")
    def ifnotcond(self):
        pass

    def tokens(self):
        if self.words:
            word = self.words[0] 
            if word == "the":
                self.varass(self.sentence)
            elif word == "lsvar":
                if not self.variables:
                    print("No variables assigned yet.")
                else:
                    print("Current variables:", self.variables)
            elif word == "if":
                self.ifcond()
            elif word == "ifnot":
                self.ifnotcond()
            elif word == "say":
                self.say()
            elif word == "ask":
                self.ask()
            elif word == "exit":
                pass
            elif word == "clear":
                os.system("clear")
            else :
                print("no keyword matches ur shit ... ")


def shell():
        line = LowKey()

        while True:
            sentence = input(">> ")
        # Create an instance of LowKey with the list of words
        # Call the method to display the words
            try:
                line.sentence  = sentence
                line.words = sentence.split()
                line.tokens()

                if sentence == "exit":
                    print("bye ...")
                    break
            except Exception as e :
                print("some compiler based error occured ... ")
                print(e)
                pass


def withfile(filename):
    line = LowKey()
    print("parsing the file " + filename)
    with open(filename , 'r' ) as file :
        sentence = file.readline()
        while sentence:
            try:

                
                line.sentence = sentence 
                line.words = sentence.split()
                line.tokens()
                sentence = file.readline()
            except Exception as e :
                print("some compiler based error ...")
                print(e)
                break
            

def main():
    # Take input from the user
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        if filename.endswith('.lkey'):
            try:
                withfile(filename)
            except FileNotFoundError:
                print("file not found ")

        else:
            print("the file does not end with .lkey extension ")

    else:
        shell()


# This ensures that main() runs when the script is executed directly
if __name__ == "__main__":
    main()

