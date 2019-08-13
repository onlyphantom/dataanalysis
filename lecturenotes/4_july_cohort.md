# Day 1
Reference: github.com/google/python-fire
Template: github.com/onlyphantom/stockmonitor

`pd.DataFrame.plot()`
- Two parameters
    - `subplots` default False
    - `kind` is the kind of plot you want
        - default is `kind="line"`
        - Options are `hist` for histogram, `bar` for bar plot

# One-dimensional
- apple['price']
- Numeric? Categorical? Time Series?
    - Numeric: Box or Histogram for distribution; Line is temporal / series / sequence of values
    - Categorical: Bar
    - Time Series: Line type

## Two-dimensional
- X axis and Y axis
    - If X (age) and Y (premium) are both numeric: Scatterplot
    - If X (gender) is categorical and Y is numeric: Boxplot
    - If X and Y are both categorical: Bar

## Altair Visualization
```py
import altair as alt
alt.Chart(dat).encode(
    x='recruitment_date',
    y='employee_age',
    color='division'
).mark_bar()
```
- mark_bar(), mark_line(), mark_point(), mark_area()
- Use the example gallery

Later on add .brush, .interactive()

## SQL Queries
- Structured Query Language
```sql
SELECT c.name, c.bank_acc, c.savings_bal, cs.name, b.name
FROM customers as c
LEFT JOIN customersupport as cs ON cs.id = c.customerrep.id
LEFT JOIN branch as b ON b.id = c.branchid
WHERE b.name = 'kemang'
ORDER BY c.savings_bal DESC
LIMIT 20
```