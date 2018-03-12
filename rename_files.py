import os


def rename_files():
    # get file names from a folder
    file_list = os.listdir("/Users/neerajdeshpande/Desktop/Python/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " +saved_path)

    os.chdir("/Users/neerajdeshpande/Desktop/Python/prank/")
    print("directory has been changed")
    new_dir=os.getcwd()
    print("now we are in " +new_dir)

    # for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate("0123456789"))
        print("we completed for loop ")

    os.chdir(saved_path)


rename_files()
