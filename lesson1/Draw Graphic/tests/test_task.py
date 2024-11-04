import os
import unittest

from task import draw_graph


class TestCase(unittest.TestCase):
    def test_draw_graph(self):
        # Call the draw_graph function
        plot = draw_graph()

        # Check the order of the x-axis (platforms) and hue (genres)
        x_order = plot.ax.get_xticklabels()  # Get x-axis tick labels
        hue_order = plot.ax.get_legend_handles_labels()[1]  # Get hue legend labels

        platform_order = ['PS4', 'XOne', 'PC', 'WiiU']
        genre_order = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle', 'Racing', 'Role-Playing',
                       'Shooter', 'Simulation', 'Sports', 'Strategy']

        # Test if the x-axis order is correct
        self.assertEqual([label.get_text() for label in x_order], platform_order, msg='Wrong platform order!')

        # Test if the hue (legend) order is correct
        self.assertEqual(hue_order, genre_order, msg='Wrong genre order!')

    def test_plot_file_created(self):
        if os.path.exists('plot.png'):
            os.remove('plot.png')

        # Call the draw_graph function
        draw_graph()

        # Check if the plot file exists
        self.assertTrue(os.path.exists('plot.png'))
