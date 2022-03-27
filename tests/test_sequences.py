'''Sequences tests'''

import unittest
from Sequences import seq_notify


class TestSequences(unittest.TestCase):
    '''Main test'''
    def test_seq_full(self):
        '''Tests full match'''
        vector = (0, 54, 17, -3, 1023)
        j = 0
        for i in seq_notify(vector, lambda x: isinstance(x, int), None, None):
            self.assertEqual(i, vector[j])
            j += 1
            
    def test_seq_full_callbacks(self):
        '''Tests full match with callbacks'''
        vector = (0, 54, 17, -3, 1023)
        expected = (54, 17, -3)
        # for assignment in callbacks
        vrs = {"start_called" : False, "end_called": False}
        def start_callback(x):
            vrs["start_called"] = True
            self.assertEqual(x, 0)
        def end_callback(x):
            vrs["end_called"] = True
            self.assertEqual(x, 1023)
        j = 0
        for i in seq_notify(vector, lambda x: isinstance(x, int),
                                    start_callback ,
                                    end_callback ):
            self.assertEqual(i, expected[j])
            j += 1
        self.assertTrue(vrs["start_called"])
        self.assertTrue(vrs["end_called"])
            
    def test_seq_full_start_callbacks(self):
        '''Tests full match with 1 callback'''
        vector = (0, 54, 17, -3, 1023)
        expected = (54, 17, -3, 1023)
        # for assignment in callbacks
        vrs = {"start_called" : False}

        def start_callback(x):
            vrs["start_called"] = True
            self.assertEqual(x, 0)

        j = 0
        for i in seq_notify(vector, lambda x: isinstance(x, int),
                                    start_callback,
                                    None):
            self.assertEqual(i, expected[j])
            j += 1
        self.assertTrue(vrs["start_called"])
            
    def test_seq_full_end_callbacks(self):
        '''Tests full match with 1 callback'''
        vector = (0, 54, 17, -3, 1023)
        expected = (0, 54, 17, -3)
        # for assignment in callbacks
        vrs = {"end_called": False}

        def end_callback(x):
            vrs["end_called"] = True
            self.assertEqual(x, 1023)

        j = 0
        for i in seq_notify(vector, lambda x: isinstance(x, int),
                                    None,
                                    end_callback):
            self.assertEqual(i, expected[j])
            j += 1
        self.assertTrue(vrs["end_called"])
            
    def test_seq_only_callbacks(self):
        '''Tests no iterations'''
        vector = (0, 1023)
        # for assignment in callbacks
        vrs = {"start_called" : False, "end_called": False}
        def start_callback(x):
            vrs["start_called"] = True
            self.assertEqual(x, 0)
        def end_callback(x):
            vrs["end_called"] = True
            self.assertEqual(x, 1023)
        isiterate = False
        for _ in seq_notify(vector, lambda x: isinstance(x, int),
                                    start_callback,
                                    end_callback):
            isiterate = True
        self.assertFalse(isiterate)
        self.assertTrue(vrs["start_called"])
        self.assertTrue(vrs["end_called"])

    def test_seq_sub_first(self):
        '''Tests part match'''
        vector = (0, 54, 17, 3, 1023)
        expected = (54, 17, 3, 1023)
        j = 0
        for i in seq_notify(vector, lambda x: x>0, None, None):
            self.assertEqual(i, expected[j])
            j += 1

    def test_seq_sub_last(self):
        '''Tests part match'''
        vector = (54, 17, 3, 1023, 0)
        expected = (54, 17, 3, 1023)
        j = 0
        for i in seq_notify(vector, lambda x: x>0, None, None):
            self.assertEqual(i, expected[j])
            j += 1

    def test_seq_sub_callbacks(self):
        '''Tests part match with callbacks'''
        vector = (0, 54, 17, 3, 1023, 0)
        expected = (17, 3)
        # for assignment in callbacks
        vrs = {"start_called" : False, "end_called": False}
        def start_callback(x):
            vrs["start_called"] = True
            self.assertEqual(x, 54)
        def end_callback(x):
            vrs["end_called"] = True
            self.assertEqual(x, 1023)
        j = 0
        for i in seq_notify(vector, lambda x: x>0,
                                    start_callback,
                                    end_callback):
            self.assertEqual(i, expected[j])
            j += 1
        self.assertTrue(vrs["start_called"])
        self.assertTrue(vrs["end_called"])

    def test_seq_sub_start_callbacks(self):
        '''Tests part match with 1 callback'''
        vector = (0, 54, 17, 3, 1023)
        expected = (17, 3, 1023)
        # for assignment in callbacks
        vrs = {"start_called" : False}

        def start_callback(x):
            vrs["start_called"] = True
            self.assertEqual(x, 54)

        j = 0
        for i in seq_notify(vector, lambda x: x>0,
                                    start_callback,
                                    None):
            self.assertEqual(i, expected[j])
            j += 1
        self.assertTrue(vrs["start_called"])

    def test_seq_sub_end_callbacks(self):
        '''Tests part match with 1 callback'''
        vector = (54, 17, 3, 1023, 0)
        expected = (54, 17, 3)
        # for assignment in callbacks
        vrs = {"end_called": False}

        def end_callback(x):
            vrs["end_called"] = True
            self.assertEqual(x, 1023)

        j = 0
        for i in seq_notify(vector, lambda x: x>0,
                                    None,
                                    end_callback):
            self.assertEqual(i, expected[j])
            j += 1
        self.assertTrue(vrs["end_called"])

    def test_seq_sub_both_callbacks(self):
        '''Tests part match callbacks without body'''
        vector = (0, 54, 1023, 0)
        # for assignment in callbacks
        vrs = {"start_called" : False, "end_called": False}
        def start_callback(x):
            vrs["start_called"] = True
            self.assertEqual(x, 54)
        def end_callback(x):
            vrs["end_called"] = True
            self.assertEqual(x, 1023)
        isiterate = False
        for _ in seq_notify(vector, lambda x: x>0,
                                    start_callback,
                                    end_callback):
            isiterate = True
        self.assertFalse(isiterate)
        self.assertTrue(vrs["start_called"])
        self.assertTrue(vrs["end_called"])

    def test_seq_sub_empty(self):
        '''Tests no match'''
        vector = (0, -54, -17, -3, -1023)
        # for assignment in callbacks
        vrs = {"start_called" : False, "end_called": False}
        isiterate = False
        def start_callback(x):
            vrs["start_called"] = True
        def end_callback(x):
            vrs["end_called"] = True
        for _ in seq_notify(vector, lambda x: x>0,
                                    start_callback,
                                    end_callback   ):
            isiterate = True
        self.assertFalse(isiterate)
        self.assertFalse(vrs["start_called"])
        self.assertFalse(vrs["end_called"])

    def test_seq_sub_oneitem(self):
        '''Tests one match'''
        vector = (0.0, 54, -1.7, 3.0, "1023")
        for i in seq_notify(vector, lambda x: isinstance(x, int),
                                    None,
                                    None):
            self.assertEqual(i, 54)

    def test_seq_sub_oneitem_callbacks(self):
        '''Tests one match callbacks'''
        vector = (0.0, 54, -1.7, 3.0, "1023")
        # for assignment in callbacks
        vrs = {"start_called" : False, "end_called": False}
        def start_callback(x):
            vrs["start_called"] = True
            self.assertEqual(x, 54)
        def end_callback(x):
            vrs["end_called"] = True
            self.assertEqual(x, 54)
        isiterate = False
        for _ in seq_notify(vector, lambda x: isinstance(x, int),
                                    start_callback,
                                    end_callback):
            isiterate = True
        self.assertTrue(vrs["start_called"])
        self.assertTrue(vrs["end_called"])
        self.assertFalse(isiterate)

    def test_seq_sub_oneitem_start_callback(self):
        '''Tests one match first callback'''
        vector = (0.0, 54, -1.7, 3.0, "1023")
        vrs = {"start_called" : False}

        def start_callback(x):
            vrs["start_called"] = True
            self.assertEqual(x, 54)

        isiterate = False
        for _ in seq_notify(vector, lambda x: isinstance(x, int),
                                    start_callback,
                                    None):
            isiterate = True
        self.assertTrue(vrs["start_called"])
        self.assertFalse(isiterate)

    def test_seq_sub_oneitem_end_callback(self):
        '''Tests one match second callback'''
        vector = (0.0, 54, -1.7, 3.0, "1023")
        # for assignment in callbacks
        vrs = {"end_called": False}

        def end_callback(x):
            vrs["end_called"] = True
            self.assertEqual(x, 54)

        isiterate = False
        for _ in seq_notify(vector, lambda x: isinstance(x, int),
                                    None,
                                    end_callback ):
            isiterate = True
        self.assertTrue(vrs["end_called"])
        self.assertFalse(isiterate)

    def test_seq_sub_oneitem_end_callback_2(self):
        '''Tests one match second callback'''
        vector = (0, 1, 2, 3, 4)
        # for assignment in callbacks
        vrs = {"end_called": False}

        def end_callback(x):
            vrs["end_called"] = True
            self.assertEqual(x, 4)

        for _ in seq_notify(vector, lambda x: x*x >= 16,
                                    None,
                                    end_callback ):
            pass
        self.assertTrue(vrs["end_called"])


    def test_seq_valid_condition(self):
        '''Tests of predicate'''
        vector = (0.0, 54, -1.7, 3.0, "1023")

        with self.assertRaises(ValueError):
            next(seq_notify(vector, lambda x: x*x, None, None))


