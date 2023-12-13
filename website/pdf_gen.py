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
        self.cell(w=30, h=10, txt='Port Royal', border=0)
        
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

def make_pdf(site_name, incident_type, date, time, weather, description_of_event, type_of_emergency_response,
             supervisory_staff_responder, outside_service_responder, people_involved, action_taken, reported_name,
             reported_title, reported_date, reported_contact, comments):
    pdf = PDF()

    pdf.make_header()
    pdf.make_title('Incident Report', pdf.w / 2 - 30, 31, 25)

    pdf.make_title(text='Site Name/Address', x=17, y=60, size=12)
    pdf.text_box_single_line(x=65, y=60, w=120, h=12, text=f'{site_name}')

    pdf.make_title(text='Incident', x=17, y=80, size=12)
    pdf.text_box_single_line(x=65, y=80, w=120, h=12, text=f'{incident_type}')

    pdf.make_title(text='Event Details', x=88, y=100, size=18)
    pdf.make_title(text='Date', x=17, y=120, size=12)
    pdf.make_title(text='Time', x=17, y=140, size=12)
    pdf.make_title(text='Weather', x=17, y=160, size=12)
    pdf.text_box_single_line(x=45, y=120, w=40, h=12, text=f'{date}')
    pdf.text_box_single_line(x=45, y=140, w=40, h=12, text=f'{time}')
    pdf.text_box_single_line(x=45, y=160, w=40, h=12, text=f'{weather}')

    pdf.make_title(text='Description of Events', x=78, y=180, size=18)

    text = description_of_event

    def formatted_text(text):
        new_text = text.replace('.', '\n')
        return new_text

    pdf.text_multiple_line(x=17, y=200, w=178, h=12, text=formatted_text(text))

    pdf.make_title(text='Event Details', x=88, y=pdf.get_y() + 10, size=18)
    pdf.make_title(text='Type of Emergency Response:', x=17, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=85, y=pdf.get_y(), w=110, h=12, text=f'{type_of_emergency_response}')
    pdf.make_title(text='Supervisory Staff Responder:', x=17, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=85, y=pdf.get_y(), w=110, h=12, text=f'{supervisory_staff_responder}')
    pdf.make_title(text='Outside Service Responder:', x=17, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=85, y=pdf.get_y(), w=110, h=12, text=f'{outside_service_responder}')

    pdf.make_title(text='People Involved', x=84, y=pdf.get_y() + 20, size=18)
    # people_involved = (f'NAME: Yonis Nur, PHONE NUMBER: 000-000-000, RESIDENT/VISITOR: Resident, EMAIL CONTACT: '
    #                    f'hello_my_friend@gmail.com, UNIT NUMBER INVOLVED:N/A\n\n'
    #                    f'NAME: Yonis Nur, PHONE NUMBER:000-000-000, RESIDENT/VISITOR: Resident, EMAIL CONTACT: hello_my_friend@gmail.com, UNIT NUMBER INVOLVED:N/A\n\n')
    people_invo = people_involved
    pdf.text_multiple_line(x=17, y=pdf.get_y() + 20, w=178, h=12, text=people_invo)

    pdf.make_title(text='Action Taken', x=84, y=pdf.get_y() + 10, size=18)
    # action_taken = ('I did some stuff, then some more, then some more, then some more,then some more,then some more,'
    #                 'then some more,then some more,then some more,then some more,then some more,')
    action_taken = action_taken
    pdf.text_multiple_line(x=17, y=pdf.get_y() + 20, w=178, h=12, text=action_taken)

    pdf.make_title(text='Comments', x=84, y=pdf.get_y() + 10, size=18)
    comments = 'kllkdlkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
    pdf.text_multiple_line(x=17, y=pdf.get_y() + 20, w=178, h=12, text=comments)

    pdf.make_title(text='Reported By', x=84, y=pdf.get_y() + 10, size=18)
    pdf.make_title(text='Name', x=17 + 45, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=45 + 45, y=pdf.get_y(), w=60, h=12, text=f'{reported_name}')
    pdf.make_title(text='Title', x=17 + 45, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=45 + 45, y=pdf.get_y(), w=60, h=12, text=f'{reported_title}')
    pdf.make_title(text='Date', x=17 + 45, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=45 + 45, y=pdf.get_y(), w=60, h=12, text=f'{reported_date}')
    pdf.make_title(text='Contact#', x=17 + 45, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=45 + 45, y=pdf.get_y(), w=60, h=12, text=f'{reported_contact}')

    pdf.make_title(text='Reviewed By', x=84, y=pdf.get_y() + 20, size=18)
    pdf.make_title(text='Name', x=17 + 45, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=45 + 45, y=pdf.get_y(), w=60, h=12, text=f'')
    pdf.make_title(text='Title', x=17 + 45, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=45 + 45, y=pdf.get_y(), w=60, h=12, text=f'')
    pdf.make_title(text='Date', x=17 + 45, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=45 + 45, y=pdf.get_y(), w=60, h=12, text='')
    pdf.make_title(text='Contact#', x=17 + 45, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=45 + 45, y=pdf.get_y(), w=60, h=12, text='')
    pdf.make_title(text='Signature', x=17 + 45, y=pdf.get_y() + 20, size=12)
    pdf.text_box_single_line(x=45 + 45, y=pdf.get_y(), w=60, h=12, text='')
    
    pdf.output("output.pdf")
    
site = input('What is the site of the address?')
incident = input('What was the incident')
date = input('What was the date of the incident?')
time = input('What was the time of the incident')
weather = input('What was the weather when the incident occured?')
DOE = input('What happened in the incident (provide full description)?')
TER = input('What was the emergency response?')
SSR = input('who was the supervisory staff responder?')
OSR = input('Who was the outside service responder')
PI = input('Who was involved?')
AT = input('What did you do?')
RN = input('What is your name?')
RT = input('What is your title?')
RD = input('What is the date today?')
RC = input('What is your phone number')
comment = input('Any other information that would be helpful for the property managers to know?')

make_pdf(site_name=site, incident_type=incident, date=date, time=time, weather=weather, description_of_event=DOE, type_of_emergency_response=TER,
             supervisory_staff_responder=SSR, outside_service_responder=OSR, people_involved=PI, action_taken=AT, reported_name=RN,
             reported_title=RT, reported_date=RD, reported_contact=RC, comments=comment)