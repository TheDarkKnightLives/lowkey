import re
import operator as op
import sys

class LowKey:
    def __init__(self, sentence=""):
        self.sentence = sentence
        self.words = sentence.split()  # Store the list of words
        self.variables = {}

    def extract_quoted(self, word):
        pattern = r'"([^"]*)"'
        quoted_segment = re.search(pattern, word)
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
        if len(self.words) > 3 and self.words[0] == "the" and self.words[2] == "is" or self.words[3].isdigit():
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
        elif not self.words[3].isdigit() and not isinstance(self.variables.get(self.words[3]), bool):
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
                if (self.words[5] in self.variables and
                        not isinstance(self.variables[self.words[5]], bool) and
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
        message = ""
        for word in self.words:
            if word == "say":
                continue

            if '"' in word:
                word = word.replace('"', "")
                value = type(self.variables.get(word))

                if value == int:
                    message += str(self.variables[word]) 
                elif value == bool:
                    message += str(self.variables[word])
                elif value == str:
                    message += str(self.variables[word])
            
            else:
                message += word 

            message += " "

        print(message.strip())

    def ask(self):
        varname = ""
        for word in self.words:
            if word == self.words[1]:
                varname = word
            elif word == "ask":
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
            else:
                print("something is wrong with this syntax")
                print("ex: ask varname type ")
                print("there are only three types available: str, int, bool")

        print("varname is " + varname)

    def extract(self, start, end):
        words = self.sentence.split()
        operator = {
                "is greater than": ">",
                "is lesser than": "<",
                "is greater than or equal to": ">=",
                "is lesser than or equal to": "<=",
                "is equal to": "==",
                "is not equal to": "!="
        }

        if start in words and end in words:
            stind = words.index(start) + 2  # start index of the start word
            enind = words.index(end) - 1  # end index of the end word 

            if stind < enind:
                extr = words[stind:enind]  # extracting the keys from the dictionary as tuple 
                result = ' '.join(extr)  # the tuple to a string 
                varextr = self.sentence.replace(result, "")  # taken out string from original for variable extraction 
                resswords = varextr.split()  # again splitting to tuples for easy access of variables
                var1 = resswords[1]
                var2 = resswords[2]
                varornot = 0  # 0 when no var, 1 when 1 var, 2 when 2 variables 

                if result in operator:
                    oper = operator[result]

                    if var1 in self.variables.keys() and var2 not in self.variables.keys():
                        varornot = 1
                        return var1, oper, var2, varornot 
                    elif var1 in self.variables.keys() and var2 in self.variables.keys():
                        varornot = 2
                        return var1, oper, var2, varornot    
                    else:
                        return var1, oper, var2, varornot
                else:
                    return None, None, None, None
            else:
                print("the words are misplaced, do it in the right order")
        else:
            print("u do not have the do keyword ...")

    def ifcond(self):
        var1, oper, var2, von = self.extract("if", "do")

        ops = {
            ">": op.gt,
            "<": op.lt,
            ">=": op.ge,
            "<=": op.le,
            "==": op.eq,
            "!=": op.ne
        }

        if von == 2:
            if ops[oper](self.variables[var1], self.variables[var2]):
                print("True condition executed")
            else:
                print("False condition executed")
        elif von == 1:
            print("you did not provide enough variables for the condition")
        else:
            print("you did not provide any variables for the condition")
                
    def process_command(self, command):
        self.sentence = command
        self.words = command.split()

        # Handle commands
        if "the" in self.words and "is" in self.words:
            self.varass(command)
        elif "say" in self.words:
            self.say()
        elif "ask" in self.words:
            self.ask()
        elif "if" in self.words and "do" in self.words:
            self.ifcond()
        else:
            print("Unrecognized command. Please try again.")

# Main Functionality
if __name__ == "__main__":
    print("Welcome to LowKey, your simple variable processor!")
    lowkey_instance = LowKey()

    if len(sys.argv) != 2:
        print("Usage: python lowkey.py <filename.lkey>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line in file:
                lowkey_instance.process_command(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    while True:
        user_input = input("Enter your command: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting LowKey...")
            break

        # Process user input
        lowkey_instance.process_command(user_input)

