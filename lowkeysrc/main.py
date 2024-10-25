import re
import os

class LowKey:
    def __init__(self, sentence=""):
        self.sentence = sentence
        self.words = sentence.split()  # Store the list of words
        self.variables = {}
    
    def extract_quoted(self, word):
        # Regular expression pattern to find the first quoted segment
        pattern = r'"([^"]*)"'
        # Search for the quoted segment
        quoted_segment = re.search(pattern, word)
        # Check if a quoted segment was found and return it
        if quoted_segment:
            return quoted_segment.group(1)  # Return the captured content (without quotes)
        else:
            return None      

    def extract_quoted_segment(self, sentence):
        # Regular expression pattern to find the first quoted segment
        pattern = r'"([^"]*)"'
        # Search for the quoted segment
        quoted_segment = re.search(pattern, sentence)
        # Check if a quoted segment was found and return it
        if quoted_segment:
            return quoted_segment.group(1)  # Return the captured content (without quotes)
        else:
            return None      

    def varass(self, sen):
        # Working with assignment 
        variable_name = self.words[1]
     
        if  len(self.words) > 3 and self.words[0] == "the" and self.words[2] == "equals":
            variable_name = self.words[1]
            variable_value = self.words[3]
            errorno = True 
            # Check for boolean assignment
            if variable_value in ["true", "false"]:
                self.variables[variable_name] = variable_value == "true"
                print(f"variable name: {variable_name}\nvariable value: {self.variables[variable_name]} type: boolean")
                print("Boolean assignment successful...")
                errorno = False 

            # Check for integer assignment
            if variable_value.isdigit():
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
                print("no datatype found , recheck ur shit ...")
            
##############################
#reassignment with operation 
        elif self.words[3].isdigit() and self.words[5].isdigit():
            if self.words[4] == "plus":
                self.variables[variable_name] = int(self.words[3]) + int(self.words[5])
                print(f"variable name : {variable_name} \n value : {self.variables[variable_name]}" )
                    
            elif self.words[4] == "minus":
                self.variables[variable_name] = int(self.words[3]) - int(self.words[5])
                print(f"variable name : {variable_name} \n value : {self.variables[variable_name]}" )
                
            elif self.words[4] == "into":
                self.variables[variable_name] = int(self.words[3]) * int(self.words[5])
                print(f"variable name : {variable_name} \n value : {self.variables[variable_name]}" )
            elif self.words[4] == "div":
                self.variables[variable_name] = int(self.words[3]) / int(self.words[5])
                print(f"variable name : {variable_name} \n value : {self.variables[variable_name]}" )
            elif self.words[4] == "remainder":
                self.variables[variable_name] = int(self.words[3]) % int(self.words[5])
                print(f"variable name : {variable_name} \n value : {self.variables[variable_name]}" )
            elif self.words[4] == "incr":
                self.variables[variable_name] = int(self.words[3]) + 1
                print(f"variable name : {variable_name} \n value : {self.variables[variable_name]}" )

            elif self.words[4] == "decr":
                self.variables[variable_name] = int(self.words[3]) + 1
                print(f"variable name : {variable_name} \n value : {self.variables[variable_name]}" )


        else:
            print("I think you forgot something... (equals)")

    def sayorask(self):
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


    def ifcond(self, sen):
        print(sen)

    def ifnotcond(self, sen):
        print(sen)

    def notifcond(self, sen):
        print(sen)

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
                self.ifcond(self.sentence)
            elif word == "ifnot":
                self.ifnotcond(self.sentence)
            elif word == "notif":
                self.notifcond(self.sentence)
            elif word == "say" or word == "ask":
                self.sayorask()
            elif word == "exit":
                pass
            elif word == "clear":
                os.system("clear")
            else :
                print("no keyword matches ur shit ... ")
def main():
    # Take input from the user
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
            pass

# This ensures that main() runs when the script is executed directly
if __name__ == "__main__":
    main()

