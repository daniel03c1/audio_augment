import numpy as np
import os
import unittest
from models import *


class ModelsTest(unittest.TestCase):
    def test_controller(self):
        output_size = 10
        n_subpolicies = 5
        controller = Controller(output_size=output_size,
                                n_subpolicies=n_subpolicies)

        policy = controller()
        self.assertEqual([*policy.size()], [n_subpolicies*4, output_size])


if __name__ == '__main__':
    os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    unittest.main()
