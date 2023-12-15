# pdf class 

from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, **kwargs):
        super(PDF, self).__init__(**kwargs)
        self.add_page()
        self.add_font('Roboto-Bold', '', r'C:\Users\ynur4\Documents\incident_report_app\website\fonts\Roboto-Bold.ttf', uni=True)
        self.add_font('Roboto-Medium', '', r'C:\Users\ynur4\Documents\incident_report_app\website\fonts\Roboto-Medium.ttf', uni=True)
    def make_header(self):
        # image_file = 'fs_pic.png'
        # self.image(name=image_file, x=2, y=9, w=64.4, h=14.61, type='PNG')
        self.set_x(self.w / 2 - 17)
        self.set_font('Roboto-Bold', '', 20)
        self.cell(w=30, h=10, txt='Incident Report', border=0)
        
    def make_title(self, text, x, y, size):
        self.set_xy(x, y)
        self.set_font('Roboto-Bold', '', size)
        self.cell(w=30, h=10, txt=text, border=3)

    def text_box_single_line(self, x, y, w, h, text):
        self.set_fill_color(235, 235, 235)
        # self.rect(x, y, w, 12, 'DF')
        self.set_xy(x, y)
        self.set_font(family='Roboto-Medium', style='', size= 12)
        self.cell(w=w, h=h, txt=text, fill=True, border=1)

    def text_multiple_line(self, x, y, w, h, text):
        self.set_fill_color(235, 235, 235)
        # self.rect(x, y, w, 12, 'DF')
        self.set_xy(x, y)
        self.set_font(family='Roboto-Medium', style='', size=10)
        self.multi_cell(w=w, h=h, txt=text, fill=True, border=1)
        
        
# make pdf function 

def make_pdf():
    pdf = PDF()
    pdf.make_header()
    
    pdf.make_title(text='Site Name/Address', x=17, y=30, size=12)
    pdf.text_box_single_line(x=65, y=30, w=120, h=12, text=f'My Real Adress 21')
    
    pdf.make_title(text='Incident Type', x=17, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=65, y=pdf.get_y(), w=120, h=12, text=f'My Real Adress 21')
    
    pdf.make_title(text='Event Details', x=88, y=pdf.get_y() + 20, size=18)
    
    pdf.make_title(text='Date of Incident:', x=17, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=pdf.get_x() + 12, y=pdf.get_y(), w=40, h=12, text=f'Janurary 27 2023')
    
    pdf.make_title(text='Time of Incident:', x=17, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=pdf.get_x() + 12, y=pdf.get_y(), w=40, h=12, text=f'6:43 PM')
    
    pdf.make_title(text='Incident Resolved:', x=17, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=pdf.get_x() + 12, y=pdf.get_y(), w=40, h=12, text=f'Yes, at 6:26PM')
    
    pdf.make_title(text='People Involved', x=84, y=pdf.get_y() + 20, size=18)
    pdf.text_multiple_line(x=17, y=pdf.get_y() + 20, w=178, h=12, text='')
    
    pdf.output('output.pdf')
    
    
make_pdf()


    
    
