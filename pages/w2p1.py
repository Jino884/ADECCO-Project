import pandas as pd
from dash import html, dcc, Output, Input, callback
import plotly.express as px
import dash
import dash_cytoscape as cyto

# URL ของ Google Sheets
url = "https://docs.google.com/spreadsheets/d/1d4BYCMKsZ8py4DukV5rLfRh6BXkPqrL-Z2pUAzeqTvs/gviz/tq?tqx=out:csv&sheet=Span%20of%20control"

# โหลดข้อมูลจาก Google Sheets
df = pd.read_csv(url)

# ข้อมูลโครงสร้างสำหรับ Cytoscape
elements = [
    # โหนด
    {'data': {'id': 'A', 'label': 'Manager A'}},
    {'data': {'id': 'B', 'label': 'Employee B'}},
    {'data': {'id': 'C', 'label': 'Employee C'}},
    {'data': {'id': 'D', 'label': 'Employee D'}},
    {'data': {'id': 'E', 'label': 'Manager B'}},
    {'data': {'id': 'F', 'label': 'Employee F'}},
    {'data': {'id': 'G', 'label': 'Employee G'}},
    
    # ขอบ
    {'data': {'source': 'A', 'target': 'B'}},
    {'data': {'source': 'A', 'target': 'C'}},
    {'data': {'source': 'A', 'target': 'D'}},
    {'data': {'source': 'E', 'target': 'F'}},
    {'data': {'source': 'E', 'target': 'G'}}
]

# สร้าง layout สำหรับหน้า w2p1
layout = html.Div([
    html.Div([
        html.H1("Age Distribution"),
        dcc.Graph(id='age-histogram')
    ], style={'margin-bottom': '40px'}),  # เพิ่ม margin เพื่อแยกแต่ละกราฟ

    html.Div([
        html.H1("Year of Service Distribution"),
        dcc.Graph(id='year-of-service-histogram')
    ], style={'margin-bottom': '40px'}),  # เพิ่ม margin เพื่อแยกแต่ละกราฟ

    html.Div([
        html.H1("Span of Control Diagram"),
        cyto.Cytoscape(
            id='cyto-graph',
            elements=elements,
            layout={'name': 'circle'},  # รูปแบบการจัดเรียง
            style={'width': '100%', 'height': '600px'},
            stylesheet=[
                {'selector': 'node', 'style': {'label': 'data(label)', 'text-wrap': 'wrap', 'text-max-width': '80px'}},
                {'selector': 'edge', 'style': {'width': 2, 'line-color': '#888'}},
                {'selector': ':hover', 'style': {'background-color': '#f00', 'line-color': '#f00'}}
            ]
        )
    ])
])

# ลงทะเบียนหน้า w2p1 โดยไม่กำหนด layout ที่นี่
dash.register_page(__name__, suppress_callback_exceptions=True)

# Callback สำหรับสร้างกราฟ Age Distribution
@callback(
    Output('age-histogram', 'figure'),
    Input('age-histogram', 'id')  # ใช้ input dummy เพื่อให้ callback ทำงานเมื่อโหลดหน้า
)
def update_age_histogram(_):
    # สร้าง histogram ของ age
    fig_age = px.histogram(df, x='age', title='Age Distribution',
                            category_orders={'age': list(range(df['age'].min(), df['age'].max() + 1))})

    # ปรับแกน x ของ age histogram
    fig_age.update_layout(
        xaxis=dict(
            tickmode='linear',
            tick0=min(df['age']),
            dtick=1,
            title='Age'
        ),
        yaxis_title='Number of participant',
        bargap=0.2
    )

    # เพิ่ม border ให้กับแท่ง histogram ของ age
    fig_age.update_traces(marker=dict(line=dict(width=1, color='black')))
    
    return fig_age

# Callback สำหรับสร้างกราฟ Year of Service Distribution
@callback(
    Output('year-of-service-histogram', 'figure'),
    Input('year-of-service-histogram', 'id')  # ใช้ input dummy เพื่อให้ callback ทำงานเมื่อโหลดหน้า
)
def update_year_of_service_histogram(_):
    # สร้าง histogram ของ yearOfService
    fig_year_of_service = px.histogram(df, x='yearOfService', title='Year of Service Distribution',
                                        category_orders={'yearOfService': list(range(df['yearOfService'].min(), df['yearOfService'].max() + 1))})

    # ปรับแกน x ของ yearOfService histogram
    fig_year_of_service.update_layout(
        xaxis=dict(
            tickmode='linear',
            tick0=min(df['yearOfService']),
            dtick=1,
            title='Year of Service'
        ),
        yaxis_title='Number of participant',
        bargap=0.2
    )

    # เพิ่ม border ให้กับแท่ง histogram ของ yearOfService
    fig_year_of_service.update_traces(marker=dict(line=dict(width=1, color='black')))
    
    return fig_year_of_service

