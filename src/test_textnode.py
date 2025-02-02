import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        node = TextNode("This is a text node", TextType.NORMAL, None)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, link, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_textnode_to_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_textnode_to_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_textnode_to_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<a href = \"https://www.boot.dev\">This is a link node</a>")

    def test_textnode_to_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<img src = \"https://www.boot.dev\" alt = \"This is an image node\"></img>")

if __name__ == "__main__":
    unittest.main()