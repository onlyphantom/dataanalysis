# Exploratory Data Analysis

## First 30 mins
- Set up your environment
- Import libraries
- Acquire your data
    - `pd.read_csv(comment='#', skiprows=10)`
- Peek at your data
    - head, tail
    - shape
    - dtypes
    - describe
    - astype
    - value_counts
    - sort_values
    - fillna(0) 
        - Replaces all `NaN` with 0. If you pass in a string, it replaces with that string

## Next 1 hour
- Exploratory Data Analysis
- Frequency table / Contingency table
    - Can be one-dimensional
        - Output is consistent with values from `.value_counts()`
    - Can be two-dimensional
- Minimal Syntax: `pd.crosstab(index='', columns='')`
    - For one-dimensional:
        - `pd.crosstab(index='bank.branches', columns='count')`
    - For two-dimensional:
        - `pd.crosstab(index='bank.branches', columns='bank.division')`
- Full Suntax:
- ```py
    pd.crosstab(index='',
                columns='', 
                values='', 
                aggfunc='', 
                margins='', 
                margins_name='', 
                normalize='')`
    ```
    - If you use `values`, you need to pass in `aggfunc` so it know which function to use to aggregate
    - `margins` add a row / column at the end that totals across the respective dimension
    - `margins_name` allow usb to overwrite the default, which is `All`
    - `normalize` takes one of **three** values:
        - `index`, `columns`, `True`
    - You can pass in multiple values for `index` and `columns` to create a multi-index. You need to use a list
    - Default function of a crosstab function is `len`

- Pivot Table
    - Default function of a pivot table is `mean`
    - Remember that mean is sensitive to outlier; `median` on the other hand is more robust
    - Require the `data` parameter, which is the name you give to your dataframe
    - Every other parameter is the same
    - If a `values` parameter is not provided explicitly
        - Implictly: It takes all numeric columns **not used as index or columns** and implictly treat them as a list of `values`
    - To avoid that implicit behavior:
        - Explictly provide the `values`
        - Use `.astype` to do an extra step of preprocessing so all non-numeric columns are not numeric types
        - Use column indexing before passing that into the `data` parameter

- Datetimes
    - `pd.to_datetime(sales['ReportDate'])`
    - Once it's a datetime, you gain access to `dt`'s attributes and methods
        - `dt.month`, `dt.week`, `dt.day`...
    - You can use methods like `dt.to_period('M')`
    - Practical: Create new features / columns

- Tips
    - Very often, you need to combine EDA with conditional indexing (boolean indexing)
    - If you normalize, you can optionally apply a `* 100` multiplier to the resulting DataFrame so you can interpret in percentages
        - Can also combine with `round(,2)`
    - If you use `sum` as the aggregating function, your values may become very huge. Use the opposite: ` / 1000000` and interpret the resulting DataFrame in the unit of millions
    - Very often, you need to combine your EDA with string matching
        - `.str.startswith('PT.')`
        - `.str.endswith('Zimmerman')`
        - `.str.contains('New York City')`

