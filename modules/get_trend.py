
import pandas
import numpy
import time
from .pytrends.request import TrendReq
from datetime import datetime
from dateutil.parser import parse

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('epobrien', 'lBBarMv2rGTe2Dqg7YnL')


def get_term(kw, start_date, end_date):
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list=kw

    s = str(start_date).split(' ')[0]
    e = str(end_date).split(' ')[0]
    pytrends.build_payload(kw_list, cat=0, timeframe=s+' '+e, geo='', gprop='')
    int_over_time_df = pytrends.interest_over_time()
    date_list = int_over_time_df.index.tolist()

    return int_over_time_df, date_list

def get_scatter(df, title, separate_y_axis=False, y_axis_label='', scale='linear', initial_hide=False):
    '''Generate a scatter plot of the entire dataframe'''
    label_arr = list(df)
    series_arr = list(map(lambda col: df[col], label_arr))

    layout = go.Layout(
        title=title,
        legend=dict(orientation="h"),
        xaxis=dict(type='date'),
        yaxis=dict(
            title=y_axis_label,
            showticklabels=not separate_y_axis,
            type=scale
        )
    )

    y_axis_config = dict(
        overlaying='y',
        showticklabels=False,
        type=scale)

    # Form Trace For Each Series
    trace_arr = []
    for index, series in enumerate(series_arr):
        if (label_arr[index]=='isPartial'):
            continue
        print('name: ', label_arr[index])
        trace = go.Scatter(
            x=series.index,
            y=series,
            name=label_arr[index],
            visible=True
        )

        # Add separate axis for the series
        if separate_y_axis:
            trace['yaxis'] = 'y{}'.format(index + 1)
            layout['yaxis{}'.format(index + 1)] = y_axis_config
        trace_arr.append(trace)

    print('get_trend: layout: ', layout)
    fig = go.Figure(data=trace_arr, layout=layout)
    return fig
