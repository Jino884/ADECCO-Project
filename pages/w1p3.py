import pandas as pd
from dash import dcc, html, Input, Output, Dash
import plotly.graph_objects as go
import plotly.express as px
import dash

# ลงทะเบียนหน้าใน Dash Pages
dash.register_page(__name__, suppress_callback_exceptions=True)

# ดึงข้อมูลจาก Google Sheets
url = "https://docs.google.com/spreadsheets/d/1d4BYCMKsZ8py4DukV5rLfRh6BXkPqrL-Z2pUAzeqTvs/gviz/tq?tqx=out:csv"
data = pd.read_csv(url)
df = pd.DataFrame(data)

# คำนวณจำนวนงานทั้งหมด
df['number_of_jobs'] = df['list all job field that you had been work on till now'].str.split(',').str.len()

# layout สำหรับหน้า w1p3
layout = html.Div([
    # html.Div([
    #     html.H4('Scatter Year of Service'),
    #     # dcc.Graph(id='scatter-yos')
    #     dcc.Loading(dcc.Graph(id="scatter-yos"), type="cube")
    # ],style={'marginBottom': '25px'}),

    html.Div([
        html.H4('Scatter Number of field'),
        # dcc.Graph(id='scatter-list-of-job')
        dcc.Loading(dcc.Graph(id="scatter-list-of-job"), type="cube")
    ],style={'marginBottom': '25px'}),
    html.Div([
        html.H4('Interview round VS Number of participant'),
        # dcc.Graph(id='interview')
        dcc.Loading(dcc.Graph(id="interview"), type="cube")
    ],style={'marginBottom': '25px'})
])

# # Callback สำหรับ scatter plot สำหรับ Year of Service
# @dash.callback(
#     Output('scatter-yos', 'figure'),
#     Input('scatter-yos', 'id')
# )
# def create_scatter_plot_yos(_):
#     fig = go.Figure(data=go.Scatter(
#         x=df['what was your first job field & year of experience : year of service'],
#         y=df['Score'],
#         mode='markers',  # ทำให้เป็น scatter plot
#         marker=dict(size=10, color='rgba(152, 0, 0, .8)', line=dict(width=2, color='DarkSlateGrey'))
#     ))
#     fig.update_layout(title="Scatter Plot of Year of Service vs Total Score",
#                       xaxis_title="Year of Service",
#                       yaxis_title="Total Score")
#     return fig

@dash.callback(
    Output('scatter-list-of-job', 'figure'),
    Input('scatter-list-of-job', 'id')
)
def create_scatter_plot_loj(_):
    fig = go.Figure()

    # ดึงระดับที่ไม่ซ้ำกันจากคอลัมน์ Level
    levels = df['Level'].unique()

    # สร้าง scatter plot สำหรับแต่ละ Level
    for level in levels:
        level_data = df[df['Level'] == level]
        fig.add_trace(go.Scatter(
            x=level_data['number_of_jobs'],
            y=level_data['Score'],
            mode='markers',
            name=level,  # ชื่อสำหรับ legend
            marker=dict(
                size=10,
                color=px.colors.qualitative.Plotly[levels.tolist().index(level)],  # ใช้สีจาก Plotly
                line=dict(width=2, color='DarkSlateGrey')
            )
        ))

    fig.update_layout(
        title="Scatter Plot of Number of Job List vs Total Score",
        xaxis_title="Number of Job List",
        yaxis_title="Total Score",
        legend_title="Level"  # ชื่อ legend
    )
    
    return fig

@dash.callback(
    Output('interview', 'figure'),  # ต้องมี ID ที่ตรงกันใน layout
    Input('interview', 'id')  # แก้ไขที่นี่
)
def bar_interview_round(_):
    # สร้าง DataFrame ที่เก็บข้อมูลการนับผู้เข้าร่วมตามกระบวนการสัมภาษณ์และระดับ
    bar_data = df.groupby(
        ["Please list all the process you have been through along the application of your current position : Interview", "Level"]
    ).size().reset_index(name='participant_count')

    # สร้างกราฟ Bar โดยใช้ Plotly
    fig = go.Figure()

    # เพิ่ม bar แต่ละ Level ลงใน fig
    for level in bar_data['Level'].unique():
        filtered_data = bar_data[bar_data['Level'] == level]
        fig.add_trace(go.Bar(
            x=filtered_data["Please list all the process you have been through along the application of your current position : Interview"],
            y=filtered_data['participant_count'],
            name=level,  # ใช้ชื่อ Level เป็นชื่อของ bar
            text=filtered_data['participant_count'],
            textposition='auto'
        ))

    # ปรับแต่ง layout ของกราฟ
    fig.update_layout(
        title_text="Interview Round",
        xaxis_title='Number of Interview',
        yaxis_title="Number of Participant",
        barmode='stack'  # ตั้งค่าให้เป็น stacked bar
    )
    fig.update_xaxes(type='linear')  # กำหนดแกน x เป็น linear
    return fig