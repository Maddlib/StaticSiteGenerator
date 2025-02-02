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

    def test_leaf_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_link(self):
        node = LeafNode("p", "val", {"href":"https://www.google.com"})
        self.assertEqual(
            "<p href = \"https://www.google.com\">val</p>", node.to_html()
        )

    def test_parent_no_tag_error(self):
        leaves = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        with self.assertRaises(ValueError):
            ParentNode(None, leaves).to_html()

    def test_parent_no_leaves_error(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None).to_html()

    def test_parent_to_html(self):
        leaves = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode("p", leaves)
        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html()
        )
    
    def test_parent_to_html_props(self):
        leaves = [
            LeafNode("b", "Bold text", {"href":"https://www.google.com"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text", {"href":"https://www.google.com"}),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode("p", leaves, {"href":"https://www.google.com"})
        self.assertEqual(
            "<p href = \"https://www.google.com\"><b href = \"https://www.google.com\">Bold text</b>Normal text<i href = \"https://www.google.com\">italic text</i>Normal text</p>", node.to_html()
        )
    
    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()