import unittest

import numpy as np
import pandas as pd
from task import import_dataset


# todo: replace this with an actual test
class TestCase(unittest.TestCase):

    def test_import(self):
        df = pd.read_csv('dataset.csv')
        df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
        df.sort_values(by='genre', inplace=True)
        returned_df = import_dataset()
        self.assertTrue(
            np.array_equal(df.genre.unique(), returned_df.genre.unique()),
            msg="Genres are not sorted in alphabetical order"
        )
        self.assertEqual(
            list(df.platform.unique()),
            list(returned_df.platform.unique()),
            msg="Platforms are different"
        )
        diff = df.compare(returned_df)
        self.assertTrue(diff.empty, msg="DataFrames have differences:\n" + str(diff))
