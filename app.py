import dash
from dash import Dash, html, dcc

# สร้างแอปและเปิดใช้งานระบบ multi-page ด้วย Dash Pages
app = Dash(__name__, use_pages=True)
server = app.server

links = {
    '/w1p1': 'Overall Participants info.',
    '/w1p2-p1': 'Assumptions check : Sankey',
    '/w1p2-p2': 'Assumtion check : Job field by level',
    '/w1p3-p1': 'Add performance Rating into data : Job list VS Total score',
    '/w1p3-p2': 'Add performance Rating into data : Interview round'
    
}

# เพิ่มลิงก์สำหรับ Workshop 2
link_w2 = {
    '/w2p1': 'Distribution Analysis'  # ชื่อที่คุณต้องการแสดงสำหรับ w2p1
}

# Layout หลักของแอป
app.layout = html.Div(
    style={'backgroundColor': '#f5f5f5', 'padding': '2px'},  # พื้นหลังเป็นสีเทาอ่อน
    children=[
        # Header สีดำพร้อมโลโก้
        html.Div(
            style={
                'backgroundColor': '#002248',
                'padding': '10px',
                'display': 'flex',
                'alignItems': 'center',
                'justifyContent': 'space-between',
                'border': '2px solid #001A3E',
                'borderRadius': '5px',
                'boxShadow': '0px 4px 8px rgba(0,0,0,0.2)',
                'marginBottom': '10px'
            },
            children=[
                html.Img(
                    src='/assets/PWG_Logo-FullColor-BlueBG_cut.jpg',  # เปลี่ยน URL ตรงนี้เป็นโลโก้ของคุณ
                    style={'height': '40px', 'marginRight': '20px'}
                )
            ]
        ),

        # div ใหญ่ ครอบ body
        html.Div(
            [
                # ส่วนหลักของหน้า
                html.Div([
                    html.H1('Elevating HR strategy with Data Analytics and AI'),
                    html.H3('For Adecco Client Event')
                ]),

                html.H3("Workshop1"),
                # แสดงลิงก์สำหรับทุกหน้าที่มีในแอป
                html.Div([
                    html.Div(
                        dcc.Link(links[page['relative_path']], href=page["relative_path"]),
                        style={'margin': '10px'}
                    ) for page in dash.page_registry.values() if page['relative_path'].startswith('/w1p')
                ]),

                html.H3('Workshop2'),
                # แสดงลิงก์สำหรับหน้า w2p1
                html.Div([
                    html.Div(
                        dcc.Link(link_w2[page['relative_path']], href=page["relative_path"]),
                        style={'margin': '10px'}
                    ) for page in dash.page_registry.values() if page['relative_path'].startswith('/w2p')
                ]),

                # แสดงเนื้อหาของหน้า
                dash.page_container
            ],
            style={
                'margin': '20px',
                'backgroundColor': 'white',  # พื้นหลังใน body div เป็นสีขาว
                'border': '2px solid #faf7f7',
                'borderRadius': '5px',
                'boxShadow': '0px 4px 8px rgba(0,0,0,0.2)',
                'marginBottom': '20px',
                'padding': '30px'
            }
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
