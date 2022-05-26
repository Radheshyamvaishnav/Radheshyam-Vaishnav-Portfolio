import time
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import requests
import re
import io

st.set_page_config(page_title='Mr. Vaishnav\'s portfolio' ,layout="wide",page_icon='👨‍🔬')

#hide menu hamburger icon , Reduce padding & remove footer & header
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
with st.sidebar:
        # Profile image
        _, col2, _ = st.columns([1, 4, 1])

        col2.image('Profile.png', use_column_width=True)
        
        # Name
        _ , _, col2, _ , _= st.columns([1, 1, 20, 1, 1])

        with col2:
                st.title('Radheshyam Vaishnav')

        st.text("")

        # Role
        _, col2, _= st.columns([1, 100, 1])

        with col2:
                st.text("Software Developer | Ex-Wipro")
                st.text("Java | Python | Javascript")
                st.text("AI ML Enthusiast | Quantum Curious")
                st.text("Learner")
                



        st.text("")
        

        # Links
        col ,col1, col2, col3, _ = st.columns([1, 1, 3, 1, 1])
        col2.caption('Wish to connect?')


        _ ,col1, col2, col3, _ = st.columns([0.5, 1, 1, 1, 0.5])
        col1.markdown("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/circled-envelope.png)](mailto:rdscode.py@gmail.com)")
        col2.markdown("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/linkedin-circled--v1.png)](https://www.linkedin.com/in/radheshyam-vaishnav/)")
        col3.markdown("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Radheshyamvaishnav)")

        st.text("")

        # Resume Button
        col ,col1, col2, col3, _ = st.columns([1, 2, 8, 2, 1])
        pdfFileObj = open('pdf/resume.pdf', 'rb')
        col2.download_button('Download Resume',pdfFileObj,file_name='Radheshyam Vaishnav\'s Resume.pdf',mime='pdf')
               
col ,col1, col2, col3, _ = st.columns([1, 2, 8, 4, 1])
col3.header("_नमस्कार🙏🏻_")



st.subheader("About Me")
st.write('''_I am a self-taught, passionate Software developer who enjoys connecting the dots: be it ideas 
from different disciplines, people from different teams, or applications from different industries. 
I have strong technical skills and an academic background in Computer Science._

_My passion lies in solving business problems with tailored data and algorithms and communicating complex 
ideas to non-technical stakeholders. I am able to jump across verticals to deliver high-performing solutions._

_While working as a Trainee Automation Engineer at Wipro, I increased the delivery rate of a project by 20%, 
for which I received a 150% bonus on top of my salary._

_During my graduate studies, I found it difficult to study whole pdf books and revise them before exams, 
therefore as a final year project, I designed an ML project called Automatic Text Summarization to overcome this 
problem. It is a tool that summaries paragraphs to help students revise more quickly and effectively before exams._''')

st.write("__________________________________________________________________________________________________________")

st.text("")
st.subheader("Skills")
col0 ,col1, col2, col3, col4 = st.columns([0.2, 0.2, 0.2, 0.2, 0.2])
col0.button("Python")
col1.button("Java")
col2.button("Javascript")
col3.button("C/C++")
col4.button("ASP.NET")
col0.button("R")
col1.button("MYSQL")
col2.button("MongoDB")
col3.button("Firebase")
col4.button("JSON")
col0.button("NLP")
col1.button("Spacy")
col2.button("Keras")
col3.button("Tricentis  Tosca")
col4.button("Vision AI")
st.text("")

st.write("__________________________________________________________________________________________________________")

st.subheader("Education")
st.text("")
st.markdown("**● Bachelors Of Science in Information Technology**")
st.text('''
-> Kishinchand Chellaram College, Mumbai                                         2018 - 2021
-> University Of Mumbai
-> CGPA 8.08
        ''')

st.text("")
st.markdown("**● Introduction to Quantum Computing**")
st.text('''
-> The Coding School, Los Angeles                                                2020 - 2021
-> 2018
        ''')


st.text("")
st.markdown("**● Higher Secondry Education**")
st.text('''
-> Utkarsha Vidyalaya & Junior College                                           2016 - 2018
-> Science
-> 63%
        ''')


st.text("")
st.markdown("**● Secondry School Education**")
st.text('''
-> Adarsh Education Society                                                       2018
-> 83%
        ''')


st.write("__________________________________________________________________________________________________________")

st.text("")


st.subheader("Work Experiance")

st.text("")
st.code(''' 
● Scholar Trainee
| Wipro  
| Full-time
| Aug 2021 - May 2022 
| Bengaluru, Karnataka, India

• As a trainee, I got the chance to work on a real-world project connect with the business team and work on their requirements.
• Worked on Tosca, Vision AI, Oracle Fusion(SCM, Finance, OFA, Sourcing), Java, Python etc technologies.

''')



st.text("")
st.code(''' 
● Sofware Development Intern
| Curaksha Company
| Internship 
| Jul 2020 - Oct 2020
| Mumbai, India

• Researched various topics such as AI, ML, DL, VR, and others.
• Contributed to the Magento project.
• Developed a project called Stock Analysis Using Machine Learning.
• Worked with the MySQL database.
''' )

st.text("")
st.code(''' 
● Freelancer
| Full-time
| March 2020
| Mumbai, India

''')

st.write("__________________________________________________________________________________________________________")

st.subheader("Projects")

st.text("")
st.write("___● Automatic Text Summarization Website___")
st.code('''-> Automatic Text Summarization Website created using Python, Flask, and Spacy. 
-> Spacy is a free, open-source library for advanced Natural Language Processing (NLP) in Python. 
-> For designing purpose I have used HTML, CSS, and JavaScript 
-> And, Lastly for Database I have used Firebase.
''')
st.write("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Radheshyamvaishnav/Automatic-Text-Summarization)")
st.text("")

st.text("")
st.write("___● Automatic-Face-Mask-Detector___")
st.code('''-> This is a ML sequential model in which I have used nearly 1500 images to train,test and validate this model. 
-> For training purpose i have used tensorflow'Keras library. 
-> This model gives us 96% accuracy.
''')
st.write("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Radheshyamvaishnav/Automatic-Face-Mask-Detector)")
st.text("")

st.text("")
st.write("___● WhatsApp Automation___")
st.code('''-> It is a program for sending Whatsaap messages automatically.
-> It is created using python and selenium.
''')
st.write("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Radheshyamvaishnav/Whatsaap-Automation)")
st.text("")


st.text("")
st.write("___● Stock-Analysis-With-ML___")
st.code('''-> This is a ML Sequential model created using Machine learning libraries like LSTM,Tensorflow  Keras.
-> This model is used to predict the the Company Stock Prices.
''')
st.write("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Radheshyamvaishnav/Stock-Analysis-With-ML)")
st.text("")

st.text("")
st.write("___● Java Programs___")
st.code('''-> This Repositery contains various Mini Projects Of java.
''')
st.write("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Radheshyamvaishnav/Java-programs-3)")
st.text("")



st.text("")
st.write("___● NGO Website___")
st.code('''-> This is simple Bootstrap website where i have used Python FLask for backend.
''')
st.write("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Radheshyamvaishnav/Vikas-NGO)")
st.text("")


st.text("")

st.write("And Many More projects @ [![Foo](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Radheshyamvaishnav/)")




st.write("__________________________________________________________________________________________________________")

st.subheader("Certificates")
st.text("")

st.text("● Software Engineering Virtual Experience, JPMorgan Chase & Co")
st.text("● Python Core & Advanced, Udemy")
st.text("● Cloud Computing Basics, Coursera")
st.text("● NDG Linux Unhatched, Cisco Networking Academy")
st.text("● Database Design using MySql, UpGrad")
st.text("● Database For Developers: Foundations, Oracle")
st.text("● Machine Learning Operations Fundamentals - Coursera")
st.text("● Automation Specialist Level 1 & Level 2 - Tricentis Academy")

st.write("__________________________________________________________________________________________________________")
       
st.text("")

col1, col2, col3 = st.columns([ 0.5, 0.5,10])
col3.text('''Please feel free to connectt with me @ rdscode.py@gmail.com''')
#col2.markdown("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/circled-envelope.png)](mailto:rdscode.py@gmail.com)***Rdscode.py@gmail.com***")
# col2.markdown("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/linkedin-circled--v1.png)](https://www.linkedin.com/in/radheshyam-vaishnav/)***Radheshyam Vaishnav's Linkedin***")
# col3.markdown("[![Foo](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Radheshyamvaishnav)***Radheshyam Vaishnav's Github***")


st.text("")
st.text("")
st.text("")
col1,col2,col3 = st.columns([10, 10, 10])

if col2.button("सुदिनमस्तु 😊", help="Have a Good Day !! 😊"):
       st.balloons()

#st.markdown("[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yourGitHubName/yourRepo/yourApp/)")
