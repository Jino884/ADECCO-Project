import dash
from dash import dcc, html

# ลงทะเบียนหน้าใน Dash Pages
dash.register_page(__name__, suppress_callback_exceptions=True)

# layout สำหรับหน้า Home
layout = html.Div([
    html.H1("Welcome to the Home Page"),
    html.Div([
        html.Img(
            src='/assets/main-fig-event.jpg',  # เปลี่ยนเป็นชื่อไฟล์รูปภาพของคุณ
            style={
                'width': '80%',  # ปรับขนาดตามต้องการ
                'height': 'auto',
                'margin': 'auto',
                'display': 'block'  # จัดให้อยู่กลางหน้า
            }
        )
    ])
])
