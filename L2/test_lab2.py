import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")


class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")


class myT1_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [128, 4, 1, 2, 16, 8, 32, 64]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [1, 2, 4, 8, 16, 32, 64, 128])
        print("\n")

class myT2_pq_empty(unittest.TestCase):

    def test_pq_empty(self):
        print("\n")
        pq = pqueue.pqueue(5)
        with self.assertRaises(KeyError):
            pq.extract_max()
        print("\n")

class myT3_insert_full_pq(unittest.TestCase):

    def test_full_pq(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(4)
        pq.insert(8)
        pq.insert(16)
        with self.assertRaises(IndexError):
            pq.insert(32)
        print("\n")

class myT4_insert_extract(unittest.TestCase):
    def test_insert_extract(self):
        print("\n")
        mh = mheap.max_heap(5)
        mh.insert(1)
        mh.insert(2)
        mh.insert(3)
        mh.insert(4)
        mh.insert(5)
        self.assertEqual(mh.__str__(), "[5|4|2|1|3]")
        print("\n")

class myT5_build_heap(unittest.TestCase):

    def test_build_heap(self):
        print("\n")
        list = [128, 4, 1, 2, 16]

        mh = mheap.max_heap(len(list), list)
        mh.build_heap()
        self.assertEqual(mh.get_heap(), [128, 16, 1, 2, 4])
        print("\n")


class myT6_is_empty(unittest.TestCase):
    def test_empty(self):
        print("\n")
        pq = pqueue.pqueue(5)
        value = pq.is_empty()
        self.assertEqual(value, True)
        print("\n")

class myT7_peak_empty_pq(unittest.TestCase):
    def test_peak_empty(self):
        print("\n")
        pq = pqueue.pqueue(5)
        value = pq.peek()
        self.assertEqual(value, None)
        print("\n")

class myT8_peak_mh(unittest.TestCase):
    def test_peak_mh(self):
        print("\n")
        mh = mheap.max_heap(5)
        mh.insert(1)
        mh.insert(2)
        mh.insert(3)
        mh.insert(4)
        mh.insert(5)
        value = mh.peek()
        self.assertEqual(value, 5)
        print("\n")

class myT9_peak_empty_mh(unittest.TestCase):
    def test_peak_empty(self):
        print("\n")
        mh = mheap.max_heap(5)
        value = mh.peek()
        self.assertEqual(value, None)
        print("\n")

class myT10_get_heap_equal(unittest.TestCase):
    def test_is_equal(self):
        print("\n")
        mh = mheap.max_heap(3)
        mh.insert(1)
        mh.insert(2)
        mh.insert(3)
        self.assertEqual(mh.get_heap(), mh.heap)


    
if __name__ == '__main__':
    unittest.main()