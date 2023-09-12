import re
import pandas as pd
from ipywidgets import widgets

def tb_interactive(dt, acc_delimiter=":", pd_disp_width=200):
    dtg = ""
    t_years = sorted(dt['date'].dt.year.unique())
    w_years = widgets.Dropdown(
            options = t_years,
            value = [t_years[-1]],
            description = 'years',
            disabled = False)
    del t_years
    acc_level_max = max([acc.count(':') for acc in dt['account'].unique()]) + 1
    w_account_level = widgets.IntSlider(
        value = 9,
        min = 0,
        max = acc_level_max,
        step = 1,
        continuous_update = True,
        orientation = 'horizontal',
        readout = True,
        readout_format = 'd',
        description = 'acc. depth')
        
    def get_gr_obj(period, account_level):
        nonlocal dtg
        #period: a year (e.g. 1996)
        date_begin, date_end = [pd.Timestamp(d) for d in f'{period}-01-01 {period}-12-31'.split()]
        r_acc = re.compile(rf'((?:[^{acc_delimiter}]+{acc_delimiter}?){{,{account_level}}})(?:{acc_delimiter}|$)')
        def chk_cols(df, col_set):
            return [col for col in col_set if col in df.columns]
        def map_tb(i):
            #s - series for each raw in a dataframe
            s = dt.loc[i]
            if s['date'] < date_begin:
                return 'bf'
            elif s['date'] > date_end:
                return 'after'
            elif s['usd'] > 0:
                return 'dt'
            else:
                return 'ct'
        def acc_level(i):
            #returns root account of acc_level
            if account_level == 0:
                return ''
            return r_acc.match(dt.loc[i]['account']).group(1)
        def prn(self):
          #return standard Trial Balance DataFrame with extra 'after' column for total of records after period of interest
          df = self['usd'].sum().unstack(1)
          df['cf'] = df.loc[:,chk_cols(df,['bf','dt','ct'])].sum(axis=1)  #add 'cf' columnt for Trial Balance
          return df[chk_cols(df,['bf','dt','ct','cf','after'])]
        def curr(self):
          #return TB DataFrame with only totals relevant for period of choice.
          df = prn(self)
          return df[df[chk_cols(['bf','dt','ct'])].any(axis=1)]
        dtg = dt.groupby(by=[acc_level,map_tb])  #keep order of index labels! Second level will form column names, after `unstack(1)`
        dtg.prn = prn.__get__(dtg)
        dtg.curr = curr.__get__(dtg)
        with pd.option_context('display.max_colwidth',90,'display.width',pd_disp_width):
            print(dtg.prn())
    
    out = widgets.interactive_output(get_gr_obj,{'period':w_years, 'account_level':w_account_level})
    h_box = widgets.HBox([w_years, w_account_level])
    v_box = widgets.VBox([h_box, out])
    return v_box, dtg
