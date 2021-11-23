import streamlit as st
import base64
from PIL import Image



def app():
    st.title(' ')
    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)

    set_background('Front.jpg')

    new_title = '<p style="font-family:Fjord One; color:Black; font-size: 42px;"><b>One Stop solution for all the diseases</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:Fjord One; color:Red; font-size: 43px;"><b>About Cordial Care.AI:</b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:Sans One; color:Black; font-size: 32px;"><b>Online Cancer consultancy System(cordial care) is a complete web portal for managing the interactive session of an patient and the corresponding doctor for consultancy online. It is a system designed specifically for the common people as to this pandemic situation, instead of going to the hospital the patient can upload a picture of the effected area and get to know what type of cancer they are harbouring and will be directed to the corresponding doctor for consultancy with the means of virtual interaction making it less likely for the patient to travel to a hospital. <b></p>'
    new_title = '<p style="font-family:Sans One; color:Black; font-size: 32px;"><b>The programs interface is designed to be simple and its use can be grasped in minutes even by inexperienced computer users and elderly patients.The system is developed using machine learning language and asp.net to increase the accuracy of the system in finding out the type cancer the particular patient has and referring the patient to the respective doctor for consultation.<b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:Sans One; color:Black; font-size: 32px;"><b>Cordial care.AI is a website that Predicts the type of cancer and provide the result as a possibility. It acts as a one stop solution where people can find the result without waiting in long queue for the result and it also has extended features where you can interact with doctors with any delay and can find solutions to be cured before any fatality happens.<b></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    
    
    st.write(" ")
    result = st.button ("Video Calling")
    if result:
       st.components.v1.html(
"""<head>
  <script src='https://meet.jit.si/external_api.js'></script>
</head>
<body>
 
<button id="start" type="button">Start</button>
<div id="jitsi-container">
</div>
 
<script>
var button = document.querySelector('#start');
var container = document.querySelector('#jitsi-container');
var api = null;
 
button.addEventListener('click', () => {
    var possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var stringLength = 30;
 
    function pickRandom() {
    return possible[Math.floor(Math.random() * possible.length)];
    }
 
var randomString = Array.apply(null, Array(stringLength)).map(pickRandom).join('');
 
    var domain = "meet.jit.si";
    var options = {
        "roomName": randomString,
        "parentNode": container,
        "width": 600,
        "height": 600,
    };
    api = new JitsiMeetExternalAPI(domain, options);
});
 
</script>
</body>
</html>"""
,
    height=600
)   
    
