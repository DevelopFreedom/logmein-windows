#!/usr/bin/env python

from __future__ import print_function

import os
import sys

try:
    import unittest
    import unittest.mock
    from unittest.mock import patch
    from unittest.mock import call
except ImportError as e:
    import mock
    from mock import patch
    from mock import call


class TestMain(unittest.TestCase):
    def setUp(self):
        self.argv_backup = sys.argv

    def tearDown(self):
        sys.argv = self.argv_backup

    def test_should_pass(self):
        pass


class AnyStringContaining(str):
    def __eq__(self, other):
        return self in other


if __name__ == '__main__':
    unittest.main()
