import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_props(self):
        node = HTMLNode("<p>", "val", None, {"href":"https://www.google.com"})
        self.assertEqual(
            " href = \"https://www.google.com\"", node.props_to_html()
        )

    def test_props_mult(self):
        node = HTMLNode("<p>", "val", None, {"href":"https://www.google.com", "target": "_blank"})
        self.assertEqual(
            " href = \"https://www.google.com\" target = \"_blank\"", node.props_to_html()
        )

    def test_htmlnode_repr(self):
        node = HTMLNode("<p>", "val", None, {"href":"https://www.google.com"})
        self.assertEqual(
            "HTMLNode(<p>, val, None, {'href': 'https://www.google.com'})", repr(node)
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_link(self):
        node = LeafNode("p", "val", {"href":"https://www.google.com"})
        self.assertEqual(
            "<p href = \"https://www.google.com\">val</p>", node.to_html()
        )

if __name__ == "__main__":
    unittest.main()