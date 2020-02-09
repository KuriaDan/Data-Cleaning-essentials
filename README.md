# Data-Cleaning-essentials

A python module for doing the repetitive data cleaning tasks.
contains four functions:
    1. initial eda checks - checks for missing values per column, returns a dataframe with each column name and the responding missing values percentage
    2. view columns with many Nans - this function accepts a dataframe and a missing values threshold percentage. It returns the columns that have missing values greater than the percentage specified
    3. drop columns with many Nans - this function drops columns whose percentage of missing values exceed the specified threshold.
    4. cleaning column names - this function removes spaces and replaces them with an underscore and lowers their cases.


## Getting Started

paste it in your current working directory or paste the py file to "C:\Users\USER\Anaconda3\Lib\site-packages\"


### Using

To use the module, import it as you would regular python modules i.e

```
import data_cleaning
```

from data_cleaning import initial_eda_checks

```

