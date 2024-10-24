import sys
import basic

def run_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            return basic.run(filename, contents)
    except Exception as e:
        return None, e

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Check if the provided file has .lk extension
        filename = sys.argv[1]
        if filename.endswith('.lk'):
            result, error = run_file(filename)

            if error:
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))
        else:
            print("Error: The file must have a .lk extension.")
    else:
        # Interactive shell
        while True:
            text = input('basic > ')
            if text.strip() == "":
                continue
            result, error = basic.run('<stdin>', text)

            if error:
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))

