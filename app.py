import dash
from dash import Dash, html, dcc, Input, Output

# สร้างแอปและเปิดใช้งานระบบ multi-page ด้วย Dash Pages
app = Dash(__name__, use_pages=True)

links = {
    '/w1p1': '1',
    '/w1p2-p1': '2',
    '/w1p2-p2': '3',
    '/w1p3-p1': '4',
    '/w1p3-p2': '5'
}

# Layout หลักของแอป
app.layout = html.Div(
    style={'backgroundColor': '#f5f5f5', 'padding': '2px'},
    children=[
        dcc.Location(id='url', refresh=False),  # เพิ่ม component dcc.Location เพื่อติดตาม URL

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

        # div สำหรับปุ่ม
        html.Div(
            style={
                'display': 'flex', 
                'justifyContent': 'center', 
                'gap': '10px',  # ช่องว่างระหว่างปุ่ม
                'flexWrap': 'wrap',  # ทำให้ปุ่มล้นลงมาในบรรทัดใหม่เมื่อไม่พอ
                'margin': '20px'
            },
            children=[
                dcc.Link(
                    html.Button(
                        links[page], 
                        style={
                            'padding': '10px 20px', 
                            'backgroundColor': '#F1A03A', 
                            'color': 'white', 
                            'border': 'none', 
                            'borderRadius': '5px',
                            'cursor': 'pointer'
                        }
                    ),
                    href=page
                ) for page in links
            ]
        ),

        # div ใหญ่ ครอบ body
        html.Div(
            [
                html.H1('Elevating HR strategy with Data Analytics and AI'),
                # html.H3('For Adecco Client Event'),

                dash.page_container
            ],
            style={
                'margin': '20px',
                'backgroundColor': 'white',
                'border': '2px solid #faf7f7',
                'borderRadius': '5px',
                'boxShadow': '0px 4px 8px rgba(0,0,0,0.2)',
                'padding': '30px'
            }
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)