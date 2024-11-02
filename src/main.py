from textnode import TextNode, TextType

def main():
    node = TextNode("text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
main()