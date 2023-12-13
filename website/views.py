from flask import Blueprint, render_template, request
from .pdf_gen import *
from datetime import datetime


views = Blueprint('views', __name__)

@views.route('/')
def home():
    
    # return render_template('questions.html')
    return 'this is the home page'
        
        
@views.route('/make_report', methods=['GET', 'POST'])
def make_report():
    if request.method == 'POST':
        incident_report_data = request.form
        # now I want to use this data to generate an incident report, and save that pdf. Once I have it I want
        # to save that pdf, send and send off the email with the pdf and then also i need to do db stuff for that pdf 
        
        make_pdf(site_name=incident_report_data['address'], incident_type='USE AI FOR THIS',
                 date=incident_report_data['date'], reported_name=incident_report_data['full_name'],
                 description_of_event=incident_report_data['event_description'], 
                 type_of_emergency_response='something', supervisory_staff_responder='some', 
                 people_involved='N/A', action_taken='ss', reported_title='Security', reported_date='2000', 
                 reported_contact='someone444', comments='sss', weather=22, time='2:22PM', outside_service_responder='something')
        
        
        
        
    return render_template('questions.html')
   
        
        
        
        
