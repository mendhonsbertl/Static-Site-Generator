import os

from markdown_to_html_node import markdown_to_html_node
from functions import extract_title
from config import basepath







def generate_page(from_path, template_path, dest_path):
    print(f"Generating Page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    replaced_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    href = f'href="{basepath}'
    src = f'src="{basepath}'
    finished_template = replaced_template.replace('href="/', href).replace('src="/', src)


    dir = (dest_path.split("/")[0])
    if not os.path.isdir(dir):
        os.mkdir(dir)
    with open(dest_path, "w") as file:
        file.write(finished_template)



def generat_page_recursive(dir_path_content, template_path, dir_dest_path):
    abs_content_path = os.path.abspath(dir_path_content)
    abs_dest_path = os.path.abspath(dir_dest_path)
    if not os.path.isdir(abs_dest_path):
        os.mkdir(abs_dest_path)
    for dir in os.listdir(abs_content_path):
        joined_content_path = os.path.join(abs_content_path, dir)
        joined_dest_path = os.path.join(abs_dest_path, dir)
        if os.path.isdir(joined_content_path):
            generat_page_recursive(joined_content_path, template_path, joined_dest_path)
        
        elif os.path.isfile(joined_content_path):
            if not dir.endswith(".md"):
                continue
            print(f"Generating Page from {joined_content_path} to {joined_dest_path} using {template_path}")
            with open(joined_content_path) as f:
                markdown = f.read()
            with open(template_path) as f:
                template = f.read()
            html_string = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown)
            replaced_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
            href = f'href="{basepath}'
            src = f'src="{basepath}'
            finished_template = replaced_template.replace('href="/', href).replace('src="/', src)
            joined_dest_path= joined_dest_path.replace(".md", ".html")

            with open(joined_dest_path, "w") as file:
                file.write(finished_template)







print(os.path.abspath("content"))

    

