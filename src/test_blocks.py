import unittest
from blocks import block_to_block_type, BlockType

class TestBlocks(unittest.TestCase):
    def test_block_to_block_type(self):
        block = "hello world"
        block2 = "### Hello World"
        block3 = "```Hello \n World\n```"
        block4 = "- Hello\n- World"

        
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(block2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block3), BlockType.CODE)
        self.assertEqual(block_to_block_type(block4), BlockType.ULIST)
        


if __name__ == "__main__":
    unittest.main()