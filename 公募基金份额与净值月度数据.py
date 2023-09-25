# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 01:05:27 2023

@author: PHCadmin
"""

from pyecharts import options as opts
from pyecharts.charts import Line, Bar
import pandas as pd
import numpy as np
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot

from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server

file_path = r'C:\Users\Administrator\OneDrive - Panoramic Hills Capital\General - Panoramic Hills Capital\BBU\A股宏观资金面数据\A股宏观资金面数据集.xlsx'
# 准备数据
df = pd.read_excel(file_path,"公募基金(Wind)",header=0)
df['月份'] = df['月份'].dt.strftime('%Y-%m-%d')
x_data = df['月份'].tolist()
y_data1 = df['公募混合型基金份额（月频）'].tolist()
y_data2 = df['公募股票型基金份额（月频）'].tolist()
y_data3 = df['份额SUM MoM Change'].tolist()














# 创建堆叠柱状图对象1
bar1 = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("公募混合型基金份额（月频）", y_data1, stack="stack1")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)

# 创建堆叠柱状图对象2
bar2 = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("公募股票型基金份额（月频）", y_data2, stack="stack1")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)

# 创建折线图对象
line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis("份额SUM MoM Change", y_data3, yaxis_index=1,z=3)
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
    )
 
)

# 合并堆叠柱状图和折线图
combined_chart = bar1.overlap(bar2).overlap(line)

# 设置全局选项
combined_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="公募基金份额与净值月度数据",pos_top="5%",pos_left="center"),
    xaxis_opts=opts.AxisOpts(
        name="           日期",
        axislabel_opts=opts.LabelOpts(rotate=45,interval=3),  # 设置X轴标签旋转角度
    ),
    datazoom_opts=[opts.DataZoomOpts()],  # 增加底部滑动条
)

# 设置Y轴选项
combined_chart.extend_axis(
    yaxis=opts.AxisOpts(
        name="MoM",
        type_="value",
        position="right",
        axislabel_opts=opts.LabelOpts(formatter="{value}"),  # 右侧Y轴数值格式
    )
)

combined_chart.extend_axis(
    yaxis=opts.AxisOpts(
        name="份额",
        type_="value",
        position="left",
        axislabel_opts=opts.LabelOpts(formatter="{value}"),  # 右侧Y轴数值格式
    )
)

# 设置鼠标悬浮时显示对应数据
combined_chart.set_series_opts(
    tooltip_opts=opts.TooltipOpts(trigger="item", axis_pointer_type="cross")
)

combined_chart.render(r"C:\Users\Administrator\OneDrive - Panoramic Hills Capital\General - Panoramic Hills Capital\BBU\A股宏观资金面数据\公募基金份额与净值月度数据.html")


put_html(line.render_notebook())
