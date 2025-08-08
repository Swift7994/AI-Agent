# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
# from functions.run_python_file import run_python_file



# print(run_python_file("calculator", "main.py"))  # (should print the calculator's usage instructions)
# print(run_python_file("calculator", "main.py", ["3 + 5"]))  # (should run the calculator... which gives a kind of nasty rendered result)
# print(run_python_file("calculator", "tests.py"))
# print(run_python_file("calculator", "../main.py"))  # (this should return an error)
# print(run_python_file("calculator", "nonexistent.py")) # (this should return an error)


# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


# print(get_file_content("calculator", "lorem.txt")) # (should return the content of the lorem.txt file)
# print(get_file_content("calculator", "main.py")) # (should return the content of the main.py file)
# print(get_file_content("calculator", "pkg/calculator.py")) # (should return the content of the calculator.py file)
# print(get_file_content("calculator", "/bin/cat"))  # (this should return an error string)
# print(get_file_content("calculator", "pkg/does_not_exist.py")) (this should return an error string)


# print(get_files_info("calculator", ".")) # (should return info about the files in the current directory)
# print(get_files_info("calculator", "pkg"))  # (should return info about the files in the pkg directory)
# print(get_files_info("calculator", "/bin")) # (should return an error string)
# print(get_files_info("calculator", "../")) # (should return an error string)