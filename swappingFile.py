while True:
    print("---------- Swap Files Data -----------")
    user_input_file_1 = input("Enter file name: ")
    user_input_file_2 = input(f"Enter file to swap with {user_input_file_1}: ")

    def swapping_files(file_1, file_2):
        file1_content = ""
        file2_content = ""
        with open(file_1, "r") as file1:
            file1_content = file1.read()
        with open(file_2, "r") as file2:
            file2_content = file2.read()
        with open(file_1, "w") as file1:
            file1.write(file2_content)
        with open(file_2, "w") as file2:
            file2.write(file1_content)
        print(f"File 1 content: {file1_content}")
        print(f"File 2 content: {file2_content}")
        print("---------- Successfully compeleted -----------")

    swapping_files(user_input_file_1, user_input_file_2)
