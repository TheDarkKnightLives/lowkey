#include <iostream>
#include <string>
#include <sstream>
#include <cctype>
#include <unordered_map>

using namespace std;

// Variable storage
unordered_map<string, string> variables;

// Function to handle variable assignment when the statement starts with "the"
void variable_ass(istringstream& iss) {
    string var_name, equals_word, value;

    // Get variable name
    iss >> var_name;

    // Read "equals"
    iss >> equals_word;
    if (equals_word != "equals") {
        cout << "Syntax error: Expected 'equals' after variable name." << endl;
        return;
    }

    // Read value (the rest of the line)
    getline(iss, value);
    value = value.substr(1); // Remove leading space

    // Determine the type of the value
    if (isdigit(value[0]) || (value[0] == '-' && isdigit(value[1]))) {
        bool is_digit = true;
        for (char c : value) {
            if (!isdigit(c) && c != '-') {
                is_digit = false;
                break;
            }
        }
        if (is_digit) {
            variables[var_name] = to_string(stoi(value)); // Store as string
            cout << "Variable name: " << var_name << " (int)" << endl;
            cout << "Assigned value: " << stoi(value) << endl; // Convert to int
        } else {
            cout << "Syntax error: Invalid integer value." << endl;
        }
    } else if (value == "True" || value == "False") {
        variables[var_name] = (value == "True") ? "true" : "false"; // Store as string
        cout << "Variable name: " << var_name << " (bool)" << endl;
        cout << "Assigned value: " << variables[var_name] << endl; // Output as boolean
    } else if (value.front() == '"' && value.back() == '"') {
        variables[var_name] = value; // Store as string
        cout << "Variable name: " << var_name << " (string)" << endl;
        cout << "Assigned value: " << value << endl; // Output as string
    } else {
        cout << "Syntax error: Unrecognized value type." << endl;
    }
}

// Function to handle the "say" command
void say(const string& content) {
    // Check if the content is a variable
    if (variables.find(content) != variables.end()) {
        cout << variables[content] << endl; // Print variable value
    } else {
        cout << content << endl; // Print the direct content
    }
}

// Main interpreter function
void interpret(const string& line) {
    istringstream iss(line);
    string keyword;

    // Check if the line starts with "the" for variable assignment
    iss >> keyword;
    if (keyword == "the") {
        variable_ass(iss);
    } else if (keyword == "say") {
        string content;
        getline(iss, content);

        // Check if the content is empty or doesn't have parentheses
        if (content.empty() || content.front() != '(' || content.back() != ')') {
            cout << "Syntax error: Expected content inside parentheses." << endl;
            return;
        }

        // Remove the surrounding parentheses
        content = content.substr(1, content.length() - 2); // Remove parentheses
        content = content.substr(1); // Remove leading space

        if (content.empty()) {
            cout << "Syntax error: No content provided." << endl;
        } else {
            say(content); // Call the say function
        }
    } else {
        // Check if the first word is a variable name for say
        if (variables.find(keyword) != variables.end()) {
            say(keyword); // If it's a variable, say its value
        } else {
            cout << "Syntax error: Unrecognized command." << endl;
        }
    }
}

int main() {
    string line;

    cout << "Enter your statements. Type 'exit' to quit." << endl;

    // Main interpreter loop
    while (true) {
        cout << ">> ";
        getline(cin, line);

        if (line == "exit") break; // Exit condition

        interpret(line); // Interpret the entered line
    }

    return 0;
}

