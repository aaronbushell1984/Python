# ***LESSON***
import io

def write_text_file(file_name, write_text, write_or_append):
    """open file write_or_append is w or r flag"""
    file = open(file_name, write_or_append)
    file.write(write_text)
    file.close()
    return

def read_text_file(file_name):
    success = False
    file = io.StringIO() # Declared so finally block can see file
    try:   # prevents an error from this example - read_text_file("xyz")
        file = open(file_name)
        text = file.read()
        print(text)
        success = True
    except FileNotFoundError: # error/ exception handling
        print(f"File not found: {file_name}")
    except OSError:
        print(OSError)
    except:
        print("Some other error") # final catch all. #NB EXCEPT MUST BE IN ORDER OF SPECIFICITY
    finally: # always executes
        file.close()
    return success

filename = "todolist.txt"
todo = "1. Go to shops \n2. Exercise \n3. Walk the dog\n"

write_text_file(filename, todo, "a")
read_text_file(filename)

# produces crash
read_text_file("xyz")

