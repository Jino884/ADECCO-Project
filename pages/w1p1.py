import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd

# # ลงทะเบียนหน้าใน Dash Pages
# dash.register_page(__name__, suppress_callback_exceptions=True)

# layout = html.Div([
#     dcc.Store(id='auto-refresh-mode', data=False),  # เก็บสถานะเปิด/ปิด
#     html.Div([
#         html.Button(id='toggle-refresh-button', n_clicks=0, children='Refresh Stopped', style={'background-color': 'red'}),
#     ], style={'display': 'flex', 'justify-content': 'flex-end'}),  # จัดปุ่มไปทางขวาสุด
    
#     html.Div([
#         html.H4('Industry Portion on Pie'),
#         dcc.Loading(dcc.Graph(id="pie-chart-1"), type="cube")
#     ]),
#     html.Div([
#         html.H4('Level Portion on Pie'),
#         dcc.Loading(dcc.Graph(id="pie-chart-2"), type="cube")
#     ]),
#     html.Div([
#         html.H4('Current Job Portion on Pie'),
#         dcc.Loading(dcc.Graph(id="pie-chart-3"), type="cube")
#     ]),
#     dcc.Interval(id='interval-component', interval=5*1000, n_intervals=0, disabled=True)  # Interval ทุกๆ 5 วินาที แต่เริ่มต้นปิดไว้
# ])

# # Callback สำหรับสลับสถานะ refresh mode และ fetch ข้อมูลทันที
# @dash.callback(
#     [Output('auto-refresh-mode', 'data'),
#      Output('toggle-refresh-button', 'children'),
#      Output('toggle-refresh-button', 'style'),
#      Output('interval-component', 'disabled'),
#      Output('interval-component', 'n_intervals')],
#     [Input('toggle-refresh-button', 'n_clicks')],
#     [State('auto-refresh-mode', 'data')]
# )
# def toggle_auto_refresh(n_clicks, auto_refresh_mode):
#     if n_clicks > 0:
#         # สลับสถานะ refresh mode
#         new_mode = not auto_refresh_mode
        
#         # อัปเดตข้อความและสีของปุ่มตามสถานะ
#         button_text = 'Refresh Running' if new_mode else 'Refresh Stopped'
#         button_color = 'green' if new_mode else 'red'
        
#         # อัปเดต interval ให้ทำงานหรือหยุด และ reset `n_intervals` เป็น 0 เพื่อให้ fetch ข้อมูลทันที
#         interval_disabled = not new_mode
        
#         return new_mode, button_text, {'background-color': button_color}, interval_disabled, 0
#     return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

# # Callback สำหรับกราฟ pie chart 1
# @dash.callback(
#     Output('pie-chart-1', 'figure'),
#     Input('interval-component', 'n_intervals'),  # trigger เมื่อ interval เกิดขึ้น
#     State('auto-refresh-mode', 'data')  # รับค่า State จาก dcc.Store
# )


# def plot_pie_chart_1(n_intervals, auto_refresh_mode):
#     if auto_refresh_mode:
#         url = "https://docs.google.com/spreadsheets/d/1d4BYCMKsZ8py4DukV5rLfRh6BXkPqrL-Z2pUAzeqTvs/gviz/tq?tqx=out:csv"
#         data = pd.read_csv(url)
#         df = pd.DataFrame(data)
        
#         fig = px.pie(df, names='what was your current industry & year of experience : industry', title='Industry Portion on Pie')
        
#         fig.update_traces(
#             textposition='outside',
#             textinfo='percent+label',
#             textfont=dict(size=16)
#         )
        
#         fig.update_layout(title_text='Industry Portion on Pie')
        
#         return fig
#     return dash.no_update

# # Callback สำหรับกราฟ pie chart 2
# @dash.callback(
#     Output('pie-chart-2', 'figure'),
#     Input('interval-component', 'n_intervals'),  # ใช้ interval-component เป็นตัว trigger
#     State('auto-refresh-mode', 'data')  # รับค่า State จาก dcc.Store
# )
# def plot_pie_chart_2(n_intervals, auto_refresh_mode):
#     if auto_refresh_mode:
#         url = "https://docs.google.com/spreadsheets/d/1d4BYCMKsZ8py4DukV5rLfRh6BXkPqrL-Z2pUAzeqTvs/gviz/tq?tqx=out:csv"
#         data = pd.read_csv(url)
#         df = pd.DataFrame(data)
        
#         fig = px.pie(df, names='Level', title='Level Portion on Pie')
        
#         fig.update_traces(
#             textposition='outside',
#             textinfo='percent+label',
#             textfont=dict(size=16)
#         )
        
#         fig.update_layout(title_text='Level Portion on Pie')
        
#         return fig
#     return dash.no_update

# # Callback สำหรับกราฟ pie chart 3
# @dash.callback(
#     Output('pie-chart-3', 'figure'),
#     Input('interval-component', 'n_intervals'),  # ใช้ interval-component เป็นตัว trigger
#     State('auto-refresh-mode', 'data')  # รับค่า State จาก dcc.Store
# )
# def plot_pie_chart_3(n_intervals, auto_refresh_mode):
#     if auto_refresh_mode:
#         url = "https://docs.google.com/spreadsheets/d/1d4BYCMKsZ8py4DukV5rLfRh6BXkPqrL-Z2pUAzeqTvs/gviz/tq?tqx=out:csv"
#         data = pd.read_csv(url)
#         df = pd.DataFrame(data)
        
#         fig = px.pie(df, names='what was your first job field & year of experience : role', title='Current Job Portion on Pie')
        
#         fig.update_traces(
#             textposition='outside',
#             textinfo='percent+label',
#             textfont=dict(size=16)
#         )
        
#         fig.update_layout(title_text='Current Job Portion on Pie')
        
#         return fig
#     return dash.no_update


# ลงทะเบียนหน้าใน Dash Pages
dash.register_page(__name__, suppress_callback_exceptions=True)

layout = html.Div([
    html.Div([
        html.H4('Industry Portion on Pie'),
        dcc.Loading(dcc.Graph(id="pie-chart-1"), type="cube")
    ]),
    html.Div([
        html.H4('Level Portion on Pie'),
        dcc.Loading(dcc.Graph(id="pie-chart-2"), type="cube")
    ]),
    html.Div([
        html.H4('Current Job Portion on Pie'),
        dcc.Loading(dcc.Graph(id="pie-chart-3"), type="cube")
    ])
])

# Callback สำหรับกราฟ pie chart 1
@dash.callback(
    Output('pie-chart-1', 'figure'),
    Input('pie-chart-1', 'id')  # ใช้ Input ที่จะถูกเรียกเมื่อหน้าโหลด
)
def plot_pie_chart_1(_):
    url = "https://docs.google.com/spreadsheets/d/1d4BYCMKsZ8py4DukV5rLfRh6BXkPqrL-Z2pUAzeqTvs/gviz/tq?tqx=out:csv"
    data = pd.read_csv(url)
    df = pd.DataFrame(data)

    fig = px.pie(df, names='what was your current industry & year of experience : industry', title='Industry Portion on Pie')

    fig.update_traces(
        textposition='outside',
        textinfo='percent+label',
        textfont=dict(size=16)
    )

    fig.update_layout(title_text='Industry Portion on Pie')

    return fig

# Callback สำหรับกราฟ pie chart 2
@dash.callback(
    Output('pie-chart-2', 'figure'),
    Input('pie-chart-2', 'id')  # ใช้ Input เดียวกัน
)
def plot_pie_chart_2(_):
    url = "https://docs.google.com/spreadsheets/d/1d4BYCMKsZ8py4DukV5rLfRh6BXkPqrL-Z2pUAzeqTvs/gviz/tq?tqx=out:csv"
    data = pd.read_csv(url)
    df = pd.DataFrame(data)

    fig = px.pie(df, names='Level', title='Level Portion on Pie')

    fig.update_traces(
        textposition='outside',
        textinfo='percent+label',
        textfont=dict(size=16)
    )

    fig.update_layout(title_text='Level Portion on Pie')

    return fig

# Callback สำหรับกราฟ pie chart 3
@dash.callback(
    Output('pie-chart-3', 'figure'),
    Input('pie-chart-3', 'id')  # ใช้ Input เดียวกัน
)
def plot_pie_chart_3(_):
    url = "https://docs.google.com/spreadsheets/d/1d4BYCMKsZ8py4DukV5rLfRh6BXkPqrL-Z2pUAzeqTvs/gviz/tq?tqx=out:csv"
    data = pd.read_csv(url)
    df = pd.DataFrame(data)

    fig = px.pie(df, names='what was your first job field & year of experience : role', title='Current Job Portion on Pie')

    fig.update_traces(
        textposition='outside',
        textinfo='percent+label',
        textfont=dict(size=16)
    )

    fig.update_layout(title_text='Current Job Portion on Pie')

    return fig
