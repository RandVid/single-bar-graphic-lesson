## Single Bar Graphic Visualisation

### Introduction

Welcome to this brief lesson on data visualization created by *Ilya Plisko*.

In this lesson, you'll learn how to use the `seaborn` library to create a **single bar chart**, 
a common visualization for counting and comparing categories. 
By the end of this lesson, 
you'll be able to recreate the following chart that shows the distribution of *game genres* across different *gaming platforms*:

![Example Chart](example.png)

### Step 1: Importing Data

To create a **meaningful graphic**, we need a dataset. In this lesson, 
we'll use a file named `dataset.csv` containing information on gaming platforms and genres.

To create a dataframe (`df`), we'll use the `pandas` library:

``` python
import pandas as pd
df = pd.read_csv("filepath/filename.csv")
```

**Exercise**: Try importing the file yourself. If the file is in the same directory as your Python script, 
you only need to specify its name *("dataset.csv")*. 
If it's in a different location, provide the full path to the file.

### Step 2: Filtering Data

Our chart shows data broken down by **platform** and **genre**. 
Let's filter the dataset to include only the platforms the original graph focuses on: 
**'PS4'**, **'XOne'**, **'PC'**, and **'WiiU'**.

We can filter specific platforms using the `isin(array)` method in `pandas`:

``` python
platforms = ['platform1', 'platform2', ...]
df = df[df['platform'].isin(platforms)]
```

**Exercise**: Implement this code to filter the dataset by the selected platforms.

### Step 3: Sorting Data

To improve readability, we can sort the data by **genre** so that genres appear in alphabetical order or in a specific order of interest.

To sort data in `pandas`, use the `sort_values` method:

``` python
df.sort_values('parameter', inplace=True)
```

This code sorts genres alphabetically and ensures consistent ordering in the plot. 
*inplace=True* is not mandatory, but it should be used if you want to change the same dataframe and not to create the new one.

**Exercise**: Try implementing this sorting step in your `task.py` file.
