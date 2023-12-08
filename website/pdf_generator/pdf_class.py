from fpdf import FPDF



# class PDF(FPDF):
#     def __init__(self, **kwargs):
#         super(PDF, self).__init__(**kwargs)
#         self.add_page()
#         self.add_font('Roboto-Bold', '', r'Roboto-Bold.ttf', uni=True)
#         self.add_font('Roboto-Medium', '', r'Roboto-Medium.ttf', uni=True)

#     def make_header(self):
#         image_file = 'fs_pic.png'
#         self.image(name=image_file, x=2, y=9, w=64.4, h=14.61, type='PNG')
#         self.set_x(self.w / 2 - 17)
#         self.set_font('Roboto-Bold', '', 20)
#         self.cell(w=30, h=10, txt='Port Royal', border=0)

#     def make_title(self, text, x, y, size):
#         self.set_xy(x, y)
#         self.set_font('Roboto-Bold', '', size)
#         self.cell(w=30, h=10, txt=text, border=3)

#     def text_box_single_line(self, x, y, w, h, text):
#         self.set_fill_color(235, 235, 235)
#         # self.rect(x, y, w, 12, 'DF')
#         self.set_xy(x, y)
#         self.set_font(family='Roboto-Medium', style='', size= 12)
#         self.cell(w=w, h=h, txt=text, fill=True, border=1)

#     def text_multiple_line(self, x, y, w, h, text):
#         self.set_fill_color(235, 235, 235)
#         # self.rect(x, y, w, 12, 'DF')
#         self.set_xy(x, y)
#         self.set_font(family='Roboto-Medium', style='', size=10)
#         self.multi_cell(w=w, h=h, txt=text, fill=True, border=1)


