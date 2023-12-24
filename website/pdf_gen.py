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
        self.set_x(84)
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

def make_pdf(address=None, date_incident=None, time_start=None, resolved=None, time_resolved=None, people_involved=None, person_1_name=None, person_1_contact=None, person_1_type=None, person_1_extra=None, person_2_name=None, person_2_contact=None, 
             person_2_type=None, person_2_extra=None, person_3_name=None, person_3_contact=None, person_3_type=None, person_3_extra=None, event_description=None, arrived=None):
    pdf = PDF()
    pdf.make_header()
    
    pdf.make_title(text='Site Name/Address', x=17, y=30, size=12)
    pdf.text_box_single_line(x=65, y=30, w=120, h=12, text=address)
    
    # pdf.make_title(text='Incident Type', x=17, y=pdf.get_y() + 20, size=12)
    # pdf.text_box_single_line(x=65, y=pdf.get_y(), w=120, h=12, text=f'Gen Incident Type Based on Description')
    
    # pdf.make_title(text='Event Details', x=88, y=pdf.get_y() + 20, size=18)
    
    # pdf.make_title(text='Date of Incident:', x=17, y=pdf.get_y() + 20, size=12)
    # pdf.text_box_single_line(x=pdf.get_x() + 12, y=pdf.get_y(), w=40, h=12, text=date_incident)
    
    # pdf.make_title(text='Time of Incident:', x=17, y=pdf.get_y() + 20, size=12)
    # pdf.text_box_single_line(x=pdf.get_x() + 12, y=pdf.get_y(), w=40, h=12, text=time_start)
    
    # def resolvedMessage(resolved):
    #     if resolved == 'yes':
    #         text = f'Yes, at {time_resolved}'
    #         return text
    #     else:
    #         return 'No'
        
    # pdf.make_title(text='Incident Resolved:', x=17, y=pdf.get_y() + 20, size=12)
    # pdf.text_box_single_line(x=pdf.get_x() + 12, y=pdf.get_y(), w=40, h=12, text=resolvedMessage(resolved))
    
    # pdf.make_title(text='People Involved', x=84, y=pdf.get_y() + 20, size=18)
    
    # # make an if statement where I pass in the amount of people and make a list of the people
    # # according to the amount of people but for now I will include all 3 people 
    # def person_format(name, type, extra, contact):
    #     return f'{name} they are a {type}, and they can be contacted at {contact}. {extra}'
        
    # if people_involved == '1':
    #     pdf.make_title(text='Person 1:', x=17, y=pdf.get_y() + 20, size=12)
    #     pdf.text_multiple_line(x=pdf.get_x(), y=pdf.get_y(), w=140, h=12, text=person_format(person_1_name, person_1_type, person_1_extra, person_1_contact))
    
    # elif people_involved == '2':
   
    #     pdf.make_title(text='Person 1:', x=17, y=pdf.get_y() + 20, size=12)
    #     pdf.text_multiple_line(x=pdf.get_x(), y=pdf.get_y(), w=140, h=12, text=person_format(person_1_name, person_1_type, person_1_extra, person_1_contact))
        
    #     pdf.make_title(text='Person 2:', x=17, y=pdf.get_y() + 12, size=12)
    #     pdf.text_multiple_line(x=pdf.get_x(), y=pdf.get_y(), w=140, h=12, text=person_format(person_2_name, person_2_type, person_2_extra, person_2_contact))
    # elif people_involved == '3':
    #     pdf.make_title(text='Person 1:', x=17, y=pdf.get_y() + 20, size=12)
    #     pdf.text_multiple_line(x=pdf.get_x(), y=pdf.get_y(), w=140, h=12, text=person_format(person_1_name, person_1_type, person_1_extra, person_1_contact))
        
    #     pdf.make_title(text='Person 2:', x=17, y=pdf.get_y() + 12, size=12)
    #     pdf.text_multiple_line(x=pdf.get_x(), y=pdf.get_y(), w=140, h=12, text=person_format(person_2_name, person_2_type, person_2_extra, person_2_contact))
        
    #     pdf.make_title(text='Person 3:', x=17, y=pdf.get_y() + 12, size=12)
    #     pdf.text_multiple_line(x=pdf.get_x(), y=pdf.get_y(), w=140, h=12, text=person_format(person_3_name, person_3_type, person_3_extra, person_3_contact))

    
    # pdf.make_title(text='Event Description', x=84, y=pdf.get_y() + 20, size=18)
    # pdf.text_multiple_line(x=19, y=pdf.get_y() + 15, w=173, h=12, text=event_description)
    
    # def format_arrived(arrived):
    #     string = ' ,'.join(arrived)
        
            
        

    # pdf.make_title(text='Emergency Response', x=79, y=pdf.get_y() + 20, size=18)
    # # include if statement if any of them are selected and make it so if multiple of the emergency response types are selected I can add an and at the end and make it more of a complete sentence
    # pdf.text_multiple_line(x=19, y=pdf.get_y() + 15, w=173, h=12, text=f'{format_arrived(arrived)}')

    # pdf.make_title(text='Comments:', x=87, y=pdf.get_y() + 20, size=18)
    # # include if statement if any of them are selected and make it so if multiple of the emergency response types are selected I can add an and at the end and make it more of a complete sentence
    # pdf.text_multiple_line(x=19, y=pdf.get_y() + 15, w=173, h=12, text=f'Here are my final comments for you and my freind liets goooooo we shall unite one day')
    
    
    # pdf.make_title(text='Reported By:', x=87, y=pdf.get_y() + 20, size=18)
    
    # # include if statement if any of them are selected and make it so if multiple of the emergency response types are selected I can add an and at the end and make it more of a complete sentence
    # pdf.make_title(text='Name:', x=17, y=pdf.get_y() + 20, size=12)
    # pdf.text_box_single_line(x=45, y=pdf.get_y(), w=120, h=12, text=f'Yonis TheJoe')
    
    # pdf.make_title(text='Position:', x=17, y=pdf.get_y() + 20, size=12)
    # pdf.text_box_single_line(x=45, y=pdf.get_y(), w=120, h=12, text=f'Security Guard')
    
    # pdf.make_title(text='Contact:', x=17, y=pdf.get_y() + 20, size=12)
    # pdf.text_box_single_line(x=45, y=pdf.get_y(), w=120, h=12, text=f'647-599-4930')
    
    # pdf.make_title(text='Reported on:', x=17, y=pdf.get_y() + 20, size=12)
    # pdf.text_box_single_line(x=45, y=pdf.get_y(), w=120, h=12, text=f'Janurary 7th, 2023')
    


    
    
    
    

    pdf.output('output.pdf')
    
    # return pdf
    
    



    
    
