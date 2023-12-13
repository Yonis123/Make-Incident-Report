from flask import Blueprint, render_template, request
from .pdf_gen import *


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
        
        
        
        
    return render_template('questions.html')
   
        
        
        
        
