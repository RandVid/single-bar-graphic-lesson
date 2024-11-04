Single Bar Graphic Visualization
--------------------------------

### Style the Graph

The function `sns.set_style("style")` allows you to change the visual style of Seaborn plots. In this lesson, we will utilize the `"darkgrid"` style, which is consistent with the style used in the original graph.

### Plot the Graph

Seaborn provides several functions for creating plots, but we will focus on `sns.catplot()` for this lesson:

```python
import seaborn as sns

plot = sns.catplot(
    data=df,
    x=df.column1,
    hue=df.column2,
    kind='count',
    order=list,
    height=float,
    aspect=float
)
```

The `sns.catplot()` function is versatile, capable of drawing various types of graphs. You can find more information on its capabilities in the [official documentation](https://seaborn.pydata.org/generated/seaborn.catplot.html). For this lesson, we will use the `'count'` type to display the frequency of categories.

#### Let's Explore Each Parameter of `sns.catplot()`

1.  **`data=df`**

    This parameter specifies the DataFrame from which the graph will pull its data.

2.  **`x=df.column1`**

    This parameter defines what data is plotted on the x-axis. In our case, it is `df.platform`. Note that there is also a `y=` parameter for specifying the y-axis data.

3.  **`hue=df.column2`**

    The `hue` parameter determines the coloring of the bars based on the values from another column. Here, it is set to `df.genre`, allowing for a visual distinction between genres.

4.  **`kind='count'`**

    As mentioned earlier, this parameter specifies the type of graph to be drawn. We are using `'count'` to represent the frequency of occurrences.

5.  **`order=list`**

    The `order` parameter instructs Seaborn to display the categories in the specified order. To match the example graph, we will pass the list `platform_order`, which contains:

    **`'PS4', 'XOne', 'PC', 'WiiU'`**

    in that exact order.

6.  **`height=float` and `aspect=float`**

    These parameters control the dimensions of the graph. While you can specify any values, I recommend setting `height=5` and `aspect=16/10` to closely resemble the original graph's proportions.

### Save the Graph

You can **save the graph** using the `plot.savefig('name')` function. Save it as *'graph.png'* so that its existence can be verified during testing.
You also can add the parameter `dpi=float` with any value you want, but I would recommend use 500 to be as close to the example as possible
