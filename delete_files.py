import os

with open("files_to_keep.txt", "r") as not_delete:
    names_list = [l for l in (line.strip() for line in not_delete) if l]
    arr = os.listdir()
    for i in names_list:
        arr.remove(i)
    counter = 1
    for file in arr:
        print(f"Deleted FILE: '{file}' on {counter}th line")
        counter += 1
        os.remove(file)