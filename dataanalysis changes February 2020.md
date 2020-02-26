Changes : 

Stage 1: Repository Structure
Remove:
- [x] 3_Reshaping_Groupby.ipynb (commit into 3_Reshaping_Groupby.ipynb)
- [x] 4_Visualization_SQL.ipynb (commit into 4_SQL_Query_Proposal.ipynb)
- [x] Add '.ipynb_checkpoints' to gitignore
- [x] Add `requirements.txt` to standardize packages in future developments.

Stage 2:
Adjustment for pandas v1

- [x] Slightly add `np.nan` alternatives,  `pd.NA`. Pandas v1 now support `NA`.
- [x] Introducing `DataFrame.convert_dtypes` and `Series.convert_dtypes` for automatically find best possible data type. Pandas now also support "String" types (previously written as 'object')
- [x] Add new feature: `df.to_markdown()` in linear with `df.to_csv()` or `df.to_json()`
- [x] `Series.dt.weekday_name` is deprecated, changed into `Series.dt.day_name()`

Stage 3: 
Adjustment for python 3.8.1
- [ ] Walrus operator. There's no operation that need walrus operator
- [x] Self documenting f-strings variable. GIve an example of output formatting in python


Stage 4: Material enhancement:
- [x] Change Chinook.db schema image into its official one from sqlite
- [x] Import unimported dependencies


requirements:
use `pip install 'package version' --force-reinstall`
pandas >= 1.0.0 
pandas-datareader
matplotlib
___
Later : standardize env in environment.md


___
issues :


use df['column_name'] instead of df.column_name for consitency




