# Exploratory Data Analysis

## First 30 mins
- Set up your environment
- Import libraries
- Acquire your data
- Peek at your data
    - head, tail
    - shape
    - dtypes
    - describe
    - astype
    - value_counts
    - sort_values

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
- Tips
    - Very often, you need to combine EDA with conditional indexing (boolean indexing)
    - If you normalize, you can optionally apply a `* 100` multiplier to the resulting DataFrame so you can interpret in percentages
        - Can also combine with `round(,2)`
    - If you use `sum` as the aggregating function, your values may become very huge. Use the opposite: ` / 1000000` and interpret the resulting DataFrame in the unit of millions

