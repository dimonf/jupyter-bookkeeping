# jupyter-bookkeeping 

Jupyter notebook interface for working with financial double entry data. Originally,
financial records were obtained by importing [Beancount](https://beancount.github.io/)
data into pandas. However, the only real dependency of this module is pandas, 
as long as dataframe has columns:
- date
- account

## Modules list:
- tb_interactive, interactive Trial Balance, generated from double-entry transactions

## Installation
`pip3 install jupyter-bookkeeping`

Or to install the bleeding edge version from git:

`pip3 install git+https://github.com/dimonf/jupyter-bookkeeping`

## Usage

```python
records_file_path = "/home/user/data/my-records.bean"
dt = bn.query2pd('select account,date,position,description,convert(position,"USD",date) as usd')
box = tb_interactive(dt, acc_delimiter=':')
display(box)
```
