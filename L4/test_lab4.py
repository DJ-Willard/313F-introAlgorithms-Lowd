from rb_tree import Node, rb_tree
import unittest
 
class T0_tree_left_rotation(unittest.TestCase):

    def test_tree_left_rotation_1(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [3,2,1])
        tree.print_tree()
        print("tree after left rotation about root  in prorder")
        print("\n")
    
    def test_tree_left_rotation_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [9,7,5,3,1,2,6,8,10])
        tree.print_tree()
        print("tree after left rotation about root  in prorder")
        print("\n")
    


class T1_tree_right_rotation(unittest.TestCase):

    def test_tree_right_rotation_1(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)

        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [1,2,3])
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")
    
    def test_tree_right_rotation_2(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [5,3,1,2,7,6,9,8,10])
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")
    

class T2_tree_insert_color(unittest.TestCase):


    def test_tree_insert_color_0(self):
        print("\n")
        print("tree_color_check")
        
        tree = rb_tree()

        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.insert(4)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 3, 4])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black', 'red'])
        print("\n")


    def test_tree_insert_color_1(self):
        print("\n")
        print("tree_color_check")
        
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 4, 3, 6, 5, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black', 'red', 'red'])
        print("\n")

class T3_tree_delete(unittest.TestCase):


    def test_tree_delete_0(self):
        print("\n")
        print("tree_insert")
        #print("checking in order, preorder and post order")
        tree = rb_tree()

        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 6, 9])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black'])
        tree.delete(9)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [6, 5, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black'])
        print("\n")

    def test_tree_delete_1(self):
        print("\n")
        print("tree_insert")
        print("checking in order, preorder and post order")
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.delete(5)
        tree.delete(4)
        # tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 6, 3, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black'])
        print("\n")
    
    def test_tree_delete_color_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(3)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(1)
        tree.insert(2)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 2, 1, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'])
        tree.delete(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 2, 1, 5, 3, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red', 'red'])
        tree.delete(7)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [8, 2, 1, 5, 3, 9, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red'])
        print("\n")

class T4_tree_Rotations(unittest.TestCase):

    def test_rotate_left(self):
        print("\n")
        print("tree_left_rotate 9")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        tree.left_rotate(tree.root.right)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 1, 2, 6, 10, 9, 8])
        print("node 9 right rotate back")
        tree.right_rotate(tree.root.right)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 1, 2, 6, 9, 8, 10])
        tree.print_tree()
        print("\n")

class T5_tree_Color_insert(unittest.TestCase):

    def test_insert(self):
        print("/n")
        print("testing insert")
        tree = rb_tree()
        tree.insert(7)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7])
        self.assertEqual(tree_preorder_color, ['black'])
        tree.insert(5)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5])
        self.assertEqual(tree_preorder_color, ['black', 'red'])
        tree.insert(9)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 9])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'red'])
        tree.insert(3)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 9])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black'])
        tree.insert(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 6, 9])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'red', 'black'])
        tree.insert(8)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 6, 9, 8])
        self.assertEqual(tree_preorder_color, ['black','black', 'red', 'red', 'black', 'red'])
        tree.insert(10)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'red', 'black', 'red', 'red'])
        tree.insert(1)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 1, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'black', 'black', 'red', 'red'])
        tree.insert(2)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 2, 1, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'])
        print("\n")

class T6_tree_Rotate_emtpyL(unittest.TestCase):

    def test_emptyRotateL(self):
        print("\n")
        print("rotating left a for an empty node")
        with self.assertRaises(KeyError):
            tree = rb_tree()
            tree.bst_insert(10)
            tree.bst_insert(5)
            tree.left_rotate(tree.root)
        print("\n")

class T7_tree_rotate_emtpyR(unittest.TestCase):

    def test_emptyRotateR(self):
        print("\n")
        print("rotating right a for an empty node")
        with self.assertRaises(KeyError):
            tree = rb_tree()
            tree.bst_insert(10)
            tree.bst_insert(15)
            tree.right_rotate(tree.root)
        print("\n")

class T8_rbtree_insert_fixup(unittest.TestCase):

    def test_rbtree_insert(self):
        print("\n")
        print("check insert fixup")
        tree = rb_tree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(3)
        tree.insert(6)
        tree.insert(9)
        tree.insert(13)
        tree.insert(17)
        tree.insert(12)
        tree.insert(14)
        tree.insert(16)
        tree.insert(19)
        tree.insert(1)
        tree.insert(0)
        tree.print_tree()
        print('\n')
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [10, 5, 3, 1, 0, 2, 3, 7, 6, 9, 15, 13, 12, 14, 17, 16, 19])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red', 'red', 'black','red', 'red', 'black', 'red', 'red'])
        print("\n")

class T9_rbtree_delete_fixup(unittest.TestCase):

    def test_rbtree_delete_fixup(self):
        print("\n")
        print("check delete fix up")
        tree = rb_tree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(3)
        tree.insert(6)
        tree.insert(9)
        tree.insert(13)
        tree.insert(17)
        tree.insert(12)
        tree.insert(14)
        tree.insert(16)
        tree.insert(19)
        tree.insert(1)
        tree.insert(0)
        tree.print_tree()
        print('\n')
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [10, 5, 3, 1, 0, 2, 3, 7, 6, 9, 15, 13, 12, 14, 17, 16, 19])
        self.assertEqual(tree_preorder_color, ['black','red','red','black','red','red','black','black','red','red','red','black','red','red','black','red','red'])
        tree.delete(1)
        print("deleting 1")
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [10, 5, 3, 2, 0, 3, 7, 6, 9, 15, 13, 12, 14, 17, 16, 19])
        self.assertEqual(tree_preorder_color, ['black','red','red','black','red','black','black','red','red','red','black','red','red','black','red','red'])
        print("\n")

class T10_delete_emptryTree(unittest.TestCase):

    def test_delete_isempty(self):
        print("\n")
        print("Delete for an empty tree")
        with self.assertRaises(KeyError):
            tree = rb_tree()
            tree.delete(1)
        print("\n")

class T11_tree_insert_delete(unittest.TestCase):

    def test_insert(self):
        print("/n")
        print("testing insert")
        tree = rb_tree()
        tree.insert(7)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7])
        self.assertEqual(tree_preorder_color, ['black'])
        tree.insert(5)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5])
        self.assertEqual(tree_preorder_color, ['black', 'red'])
        tree.insert(9)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 9])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'red'])
        tree.insert(3)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 9])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black'])
        tree.insert(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 6, 9])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'red', 'black'])
        tree.insert(8)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 6, 9, 8])
        self.assertEqual(tree_preorder_color, ['black','black', 'red', 'red', 'black', 'red'])
        tree.insert(10)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'red', 'black', 'red', 'red'])
        tree.insert(1)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 3, 1, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'black', 'black', 'red', 'red'])
        tree.insert(2)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 2, 1, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'])
        print("\n")
        print("delete 6")
        tree.delete(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 2, 1, 5, 3, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red', 'red'])
        print("\n")
        print("insert 4")
        tree.insert(4)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 2, 1, 4, 3, 5, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'red', 'black', 'red', 'red'])
        print("\n")
        print("delete 7")
        tree.delete(7)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [8, 2, 1, 4, 3, 5, 9, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'red','black', 'red'])

        print("\n")

if __name__ == "__main__":
    unittest.main()
