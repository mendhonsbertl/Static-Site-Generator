from textnode import TextNode, TextType
import re
from markdown_to_blocks import markdown_to_blocks


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches



def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        for alt, link in images:
            sections = original_text.split(f"![{alt}]({link})", 1)
            if sections[0] !="":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, link))
            original_text = sections[1]
        if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        for alt, link in links:
            sections = original_text.split(f"[{alt}]({link})", 1)
            if sections[0] !="":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, link))
            original_text = sections[1]
        if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



    
def text_to_textnodes(text):
    
    node = [TextNode(text, TextType.TEXT)]
    new_node = split_nodes_delimiter(node, "**", TextType.BOLD)
    new_node = split_nodes_delimiter(new_node, "_", TextType.ITALIC)
    new_node = split_nodes_delimiter(new_node, "`", TextType.CODE)
    new_node = split_nodes_images(new_node)
    new_node = split_nodes_links(new_node)
    return new_node
    
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        lines = block.split("\n")
        for line in lines:
            if line.startswith("# "):
                return line.strip("# ")
    raise Exception("no header h1")


            


