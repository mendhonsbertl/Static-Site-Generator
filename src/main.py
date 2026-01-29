import os
import shutil


from copy_static_public import copy_files_recursive
from generate_page import generat_page_recursive




dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"



def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    # generate_page("content/index.md", "template.html", "public/index.html")
    generat_page_recursive(dir_path_content,"template.html", dir_path_public)


main()


