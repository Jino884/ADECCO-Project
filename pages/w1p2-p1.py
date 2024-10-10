import pandas as pd
from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import dash

# ลงทะเบียนหน้าใน Dash Pages
dash.register_page(__name__, suppress_callback_exceptions=True)

# โหลดข้อมูลจาก Google Sheets
url = "https://docs.google.com/spreadsheets/d/1d4BYCMKsZ8py4DukV5rLfRh6BXkPqrL-Z2pUAzeqTvs/gviz/tq?tqx=out:csv"
df = pd.read_csv(url)

# เพิ่ม (F) และ (C) เพื่อแยกงาน
df['what was your first job field & year of experience : role'] += ' (F)'
df['what was your current job field & year of experience : role'] += ' (C)'
df['number_of_jobs'] = df['list all job field that you had been work on till now'].str.split(', ').str.len()

df_hr = df.loc[df['what was your current job field & year of experience : role'] == 'HR (C)']

# ฟังก์ชันสร้างข้อมูล Sankey
def create_sankey_data(df):
    nodes = list(set(df['field of your degree']).union(
        df['what was your first job field & year of experience : role'],
        df['what was your current job field & year of experience : role']
    ))

    links = []
    for _, row in df.iterrows():
        source_index = nodes.index(row['field of your degree'])
        target_index = nodes.index(row['what was your first job field & year of experience : role'])
        links.append({'source': source_index, 'target': target_index, 'value': 1})

        source_index = nodes.index(row['what was your first job field & year of experience : role'])
        target_index = nodes.index(row['what was your current job field & year of experience : role'])
        links.append({'source': source_index, 'target': target_index, 'value': 1})

    return nodes, links

# สร้าง nodes และ links
nodes, links = create_sankey_data(df)

# แปลง links เป็นรูปแบบที่ Plotly ต้องการ
link_dict = {
    'source': [link['source'] for link in links],
    'target': [link['target'] for link in links],
    'value': [link['value'] for link in links]
}

# กำหนด layout ของหน้า w1p2
layout = html.Div([
    html.Div([
        html.H4('Sankey Diagram'),
        # dcc.Graph(id='sankey-graph'),
        dcc.Loading(dcc.Graph(id="sankey-graph"), type="cube")
    ], style={'marginBottom': '25px'}),

    # html.Div([
    #     html.H4('Industry Distribution'),
    #     # dcc.Graph(id='industry-pie-chart')
    #     dcc.Loading(dcc.Graph(id="industry-pie-chart"), type="cube")
    # ],style={'marginBottom': '25px'}),

    # html.Div([
    #     html.H4('BarChart of Year of Service (HR)'),
    #     # dcc.Graph(id='bar-chart-YOS'),
    #     dcc.Loading(dcc.Graph(id="bar-chart-YOS"), type="cube")
    # ],style={'marginBottom': '25px'}),

    # html.Div([
    #     html.H4('List all job field that you had been work on till now'),
    #     # dcc.Graph(id='bar-chart-listalljob'),
    #     dcc.Loading(dcc.Graph(id="bar-chart-listalljob"), type="cube")
    # ],style={'marginBottom': '25px'})
])

# Callback สำหรับ Sankey Diagram
@dash.callback(
    dash.Output('sankey-graph', 'figure'),
    dash.Input('sankey-graph', 'id')
)
def update_sankey(_):
    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=nodes,
        ),
        link=dict(
            source=link_dict['source'],
            target=link_dict['target'],
            value=link_dict['value'],
        )
    ))
    fig.update_layout(title_text="Sankey Diagram", font_size=15)
    return fig

# # Callback สำหรับ Pie Chart
# @dash.callback(
#     dash.Output('industry-pie-chart', 'figure'),
#     dash.Input('industry-pie-chart', 'id')
# )
# def update_pie_chart(_):
#     fig = px.pie(df, names='field of your degree', title='Distribution of Industries')

#     fig.update_traces(
#         textposition='outside', 
#         textinfo='percent+label', 
#         textfont=dict(size=16))  # กำหนดขนาดฟอนต์ของ data label

#     fig.update_layout(
#         title_text='Distribution of Industries')
#     return fig

# # Callback สำหรับ Bar Chart (HR)
# @dash.callback(
#     dash.Output('bar-chart-YOS', 'figure'),
#     dash.Input('bar-chart-YOS', 'id')
# )
# def update_bar_chart(_):
#     bar_data = df_hr.groupby("what was your current job field & year of experience : year of service").size().reset_index(name='participant_count')

#     fig = go.Figure([go.Bar(
#         x=bar_data['what was your current job field & year of experience : year of service'],
#         y=bar_data['participant_count'],
#         text=bar_data['participant_count'],
#         textposition='auto',
#         textfont=dict(size=16),
#         width=0.5

#     )])

#     fig.update_layout(
#         title_text="Participants by Year of Service for only HR", 
#         xaxis_title="Year of Service", 
#         yaxis_title="Number of Participants",
#         bargap = 0.2,
#         bargroupgap=0.1
        
#         )
#     return fig

# Callback สำหรับ Bar Chart (list of job field)
# @dash.callback(
#     dash.Output('bar-chart-listalljob', 'figure'),
#     dash.Input('bar-chart-listalljob', 'id')
# )
# def update_bar_chart_laj(_):
#     # สร้างข้อมูลใหม่โดยจัดกลุ่มตาม number_of_jobs และ Level
#     bar_data = df.groupby(['number_of_jobs', 'Level']).size().reset_index(name='participant_count')

#     # สร้างกราฟแท่งซ้อน
#     fig = go.Figure()

#     # เพิ่มแท่งสำหรับแต่ละ Level
#     for level in bar_data['Level'].unique():
#         level_data = bar_data[bar_data['Level'] == level]
#         fig.add_trace(go.Bar(
#             x=level_data['number_of_jobs'],
#             y=level_data['participant_count'],
#             name=level,
#             text=level_data['participant_count'],
#             textposition='auto',
#             width=0.5,
#             textfont=dict(size=16)
#         ))

#     fig.update_layout(
#         title_text="List of Job Field by Level", 
#         xaxis_title="Number of Job Field", 
#         yaxis_title="Number of Participants",
#         barmode='stack',  # เปลี่ยนให้เป็นแบบ stacked
#         bargap=0.2,  # ปรับระยะห่างระหว่างแท่ง
#         bargroupgap=0.1  # ปรับระยะห่างระหว่างกลุ่มแท่ง (ถ้ามีหลายกลุ่ม)
#     )
#     return fig