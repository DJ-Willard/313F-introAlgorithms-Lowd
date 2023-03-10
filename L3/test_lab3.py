import lab3
import unittest



class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        #The following check is without using tree as an iterator (which uses inorder traversal)
        #So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")




class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data
        test = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)
        self.assertEqual(test, 8)

        print("\n")


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]



        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

class T6_KeyError_FS(unittest.TestCase):
    def find_successor(self):
        print("\n")
        print("successor for an empty tree")
        with self.assertRaises(KeyError):
            t = lab3.Tree()
            t.find_successor(1)
        print("\n")


class T6_KeyError_del(unittest.TestCase):
    def delete(self):
        print("\n")
        print("Delete for an empty tree")
        with self.assertRaises(KeyError):
            t = lab3.Tree()
            t.delete(1)
        print("\n")

class T7_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(10)
        t.insert(5)
        t.insert(3)
        t.insert(7)
        t.insert(2)
        t.insert(4)
        t.insert(6)
        t.insert(8)
        t.insert(15)
        t.insert(13)
        t.insert(20)
        t.insert(12)
        t.insert(14)
        t.insert(17)
        t.insert(22)

        l1 = [node for node in t]
        t.delete(10)
        l2 = [node for node in t]
        t.delete(22)
        l3 = [node for node in t]
        t.delete(15)
        l4 = [node for node in t]
        t.delete(8)
        l5 = [node for node in t]



        self.assertEqual(l1, [2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 17, 20, 22])
        self.assertEqual(l2, [2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 15, 17, 20, 22])
        self.assertEqual(l3, [2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 15, 17, 20])
        self.assertEqual(l4, [2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 17, 20])
        self.assertEqual(l5, [2, 3, 4, 5, 6, 7, 12, 13, 14, 17, 20])


class T8_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(10)
        t.insert(5)
        t.insert(3)
        t.insert(7)
        t.insert(2)
        t.insert(4)
        t.insert(6)
        t.insert(8)
        t.insert(15)
        t.insert(13)
        t.insert(20)
        t.insert(12)
        t.insert(14)
        t.insert(17)
        t.insert(22)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        postorder = [node for node in t.postorder()]

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator,[2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 17, 20, 22])
        print("inorder traversal")
        self.assertEqual(inorder, [2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 17, 20, 22])
        print("preorder traversal")
        self.assertEqual(preorder, [10, 5, 3, 2, 4, 7, 6, 8, 15, 13, 12, 14, 20, 17, 22])
        print("postorder traversal")
        self.assertEqual(postorder, [2, 4, 3, 6, 8, 7, 5, 12, 14, 13, 17, 22, 20, 15, 10])
        print("\n")

#note test _find node as well
class T10_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        print("\n")
        print("find node function")
        t = lab3.Tree()
        t.insert(10)
        t.insert(5)
        t.insert(3)
        t.insert(7)
        t.insert(2)
        t.insert(4)
        t.insert(6)
        t.insert(8)
        t.insert(15)
        t.insert(13)
        t.insert(20)
        t.insert(12)
        t.insert(14)
        t.insert(17)
        t.insert(22)

        self.assertEqual(t.contains(22), True)
        self.assertEqual(t.contains(120), False)
        print("\n")

class T11_testFSfind(unittest.TestCase):

    def test_find_successor(self):
        print("\n")
        t = lab3.Tree()
        t.insert(10)
        t.insert(5)
        t.insert(3)
        t.insert(7)
        t.insert(2)
        t.insert(4)
        t.insert(6)
        t.insert(8)
        t.insert(15)
        t.insert(13)
        t.insert(20)
        t.insert(12)
        t.insert(14)
        t.insert(17)
        t.insert(22)

        succ1 = t.find_successor(22)
        succ2 = t.find_successor(10)
        succ3 = t.find_successor(5)

        self.assertEqual(succ1, None)
        self.assertEqual(succ2.data, 12)
        self.assertEqual(succ3.data, 6)
        print("\n")


class T12_tree__insert(unittest.TestCase):

    def test_insert(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(5)
        t.insert(3)
        t.insert(7)
        t.insert(2)
        t.insert(3)
        t.insert(6)
        t.insert(8)



        self.assertEqual(t.root.data, 5)
        self.assertEqual(t.root.left.data, 3)
        self.assertEqual(t.root.left.left.data, 2)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 7)
        self.assertEqual(t.root.right.left.data, 6)
        self.assertEqual(t.root.right.right.data, 8)

        print("\n")

if __name__ == '__main__' :
    unittest.main()