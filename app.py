from pathlib import Path

import streamlit as st
from PIL import Image

#---PATH SETTING---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "headshot.png"


#---GENERAL SETTING---
PAGE_TITLE = "Digital Resume | Jesse Aseoff"
PAGE_ICON = ":wave:"
NAME = "Jesse Aseoff"
DESCRIPTION = """
I am a senior at Chapman University who is passionate about data and its potential to help businesses make more informed decisions. After graduation, I am looking for a position where I can use my skills to help a company grow and succeed.
"""
EMAIL = "jesse.aseoff@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jaseoff/",
    "GitHub": "https://github.com/aseoff",
}

PROJECT_1 = {
    "🏠 **Zillow Algorithm ('Zestimate')**": "https://github.com/aseoff/zestimate"
}

PROJECT_2 = {
    "🦠 **'The Game of Life' - Data Structures Project**": "https://github.com/aseoff/The-Game-of-Life/"
}

PROJECT_3 = {
    "🚗 **Founder | Dashathon**": "https://dashathon2020.wixsite.com/dashathon/home"
}


PROJECT_4 = {
    "🚗 **Founder | Dashathon**": "https://dashathon2020.wixsite.com/dashathon/home"
}

OTHER_PROJECTS = {
    "National Student Advertising Competition (NSAC) Campaign": "https://drive.google.com/drive/folders/1WgF1OzM-127P_eVPe12oXsM9kSu4alzq",
    "Dashathon (National Fundraiser)": "https://dashathon2020.wixsite.com/dashathon/home"
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#st.title("Hello there!")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)


with col2:
    st.title(NAME)
    st.write(
"""
**BS Data Science | 3.83 GPA**
"""
    )
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



##---------------SKILLS AND COURSES FUNCTION------------------
def showSkillsAndCourses():
    col1_sk, col2_sk = st.columns(2, gap="large")
    # --- SKILLS ---
    with col1_sk:
        st.write('\n')
        st.subheader("Hard Skills")
        st.write(
            """
        - 👨‍💻️ **Languages:** Python, R, SQL, Java, C++
        
        - ⚙️ **Machine Learning:** Supervised (SVM, KNN, NNs, GLM, Decision Trees) and Unsupervised (K-Means, Hierarchial, PCA)
        
        - 🗃 **Soft Skills:** Collaboration, Problem-solving, Storytelling 
        """
        )

    #Courses--------------
    with col2_sk:
        st.write('\n')
        st.subheader("Relevant Courses")
        st.write(
            """
        - 📊 Introduction to Data Science
        - 🧮 Machine Learning
        - 📉 Statistical Models in Business Analytics
        - 📚 Database Management
        - 📈 Data Structures and Algorithms
        - 📶 Data Communications and Computer Networks

        """
        )
##------------------------------------
##----------------RELEVANT EXPERIENCE FUNCTION------------------------
def showRelevantExperience():
    # --- RELEVANT EXPERIENCE ---
    st.write('\n')
    st.subheader("Experience")
    st.write("---")

    # --- EXPERIENCE 1
    st.write("🍎", "**Computer Science Teacher | Far Horizons Montessori School**")
    st.write("August 2021 - December 2021")
    st.write(
        """
    - ► Taught age-appropriate computer skills to K-8 students
    - ► Developed written instructions and handouts to supplement course lectures.
    - ► Created tests and assignments to assess student knowledge of presented coursework and lecture materials.
    """
    )
    # --- EXPERIENCE 2
    st.write('\n')
    st.write("♟️", "**Strategy Specialist | Circle Advertising**")
    st.write("August 2020 - May 2021")
    st.write(
        """
    - ► Created and analyzed a Qualtrics survey to uncover meaningful findings for our client - Tinder
    - ► Produced data sheets, graphics and presentations using Excel and PowerPoint
    - ► Competed in the American Advertising Federation National Student Advertising Competition
    """
    )

    # --- EXPERIENCE 3
    st.write('\n')
    st.write("📊", "**Data Analyst Intern | Tech Education Start-Up**")
    st.write("May 2020 - September 2020")
    st.write(
        """
    - ► Utilized statistical software including Excel and R to compile and analyze data
    - ► Developed clear visualizations with ggplot to simplify complex data findings
    - ► Created a company website using Wordpress and basic HTML skills
    - ► Maintained a database with competitor information and other potentially valuable information
    """
    )
##---------------------------------
##----------------RELEVANT PROJECTS FUNCTION------------------------
def showRelevantProjects():
    # --- Relevant Projects ---
    st.write('\n')
    st.subheader("Projects")
    st.write("---")

 

    # --- PROJECT 1
    for project, link in PROJECT_2.items():
        st.write(f"[{project}]({link})")
    st.write("March 2021")
    st.write(
        """
    - ► Created a C++ program of the 1970s game designed by mathematician J.H. Conway
    - ► The simulation utilizes object oriented programming in Java to model the life cycle of bacteria
    - ► The project incorporated two-dimensional arrays and compiled and ran successfully
    """
    )

       # --- PROJECT 2
    st.write('\n')
    for project, link in PROJECT_1.items():
        st.write(f"[{project}]({link})")
    st.write("July 2020")
    st.write(
        """
    - ► Worked in a team of 3 to clean and analyze a large California housing dataset using R
    - ► Using R, we implemented data visualizations, supervised learning algorithms (linear regression, decision trees) and unsupervised learning algorithms (K-means, PCA) to help create our simplified “Zestimate”
    - ► Created an interactive R Shiny program that took in various parameters from the user to return a “Zestimate” value with the machine learning methods applied in the project
    """
    )

    # --- PROJECT 3
    st.write('\n')
    for project, link in PROJECT_3.items():
        st.write(f"[{project}]({link})")    
    st.write("April 2020 - June 2020")
    st.write(
        """
- ► Founded a philanthropy event which brought together 40+ DoorDash drivers who donated earnings the night of May 30th, 2020
- ► All donations went to worthwhile causes including Colorado COVID relief and Food Bank of the Rockies
- ► Led a team of eight board members
- ► Received media coverage from local NBC and FOX affiliates
- ► Raised and donated over $20,000 in less than two weeks
    """
    )

def showMoreWorkExperience():
        # --- MORE WORK EXPERIENCE ---
    st.subheader("Further Work Experience")
    st.write("---")

    # --- EXPERIENCE 1
    st.write("👨‍🏫️", "**Academic Tutor | Orange, CA**")
    st.write("March 2020 - Present")
    st.write(
        """
    - ► Worked with first generation students at local high school, helping them reach their goal of attending college
    - ► Hosted 100+ private tutoring sessions with 100% satisfaction rate
    - ► Develop handouts, study materials and quizzes.
    - ► Create and implement individual lesson plans based on student learning styles.
    """
    )

        # --- EXPERIENCE 2
    st.write('\n')
    st.write("🛶", "**Camp Group Leader | Camp Equinunk**")
    st.write("May 2021 - Present")
    st.write(
        """
    - ► Responsible for the health, safety and well-being of forty 11-year old campers during summer sleep away camp
    - ► Train and manage staff team of 12-15 counselors, upholding health and child safety standards.
    - ►Communicate and maintain personal contact with parents or guardians to discuss achievements and behavior concerns.
    """
    )

        # --- EXPERIENCE 3
    st.write('\n')
    st.write("🏫", "**Tour Guide and Office Assistant | Chapman University**")
    st.write("December 2020 - Present")
    st.write(
        """
   - ► Deliver guided tours to groups of up to 25, presenting scripted information and answering questions.
   - ► Host brief one on one interviews with prospective students
   - ► Handle incoming calls and directed callers to appropriate department or employee.
    """
    )

def showLeadership():
        # --- EXTRA CURRICULARS ---
    st.subheader("Leadership and Academic Activities")
    st.write("---")

    # --- EXPERIENCE 1
    st.write("👨‍🎓️", "**Presidential Scholaship Recipient | Chapman University**")
    st.write("August 2019 - Present")

    # --- EXPERIENCE 2
    st.write('\n')
    st.write("🎒", "**Dean's List | Chapman University**")
    st.write("December 2019 - Present")

    # --- EXPERIENCE 3
    st.write('\n')
    st.write("👔", "**Recruitment Chair | Alpha Epsilon Pi Fraternity**")
    st.write("January 2021 - Present")

    # --- EXPERIENCE 4
    st.write('\n')
    st.write("🇳🇱", "**Semester Abroad | Vrije Universiteit Amsterdam**")
    st.write("January 2022 - June 2022")

    # --- EXPERIENCE 5
    st.write('\n')
    st.write("🎗️", "**Board Member | B+ Foundation of Chapman University**")
    st.write("August 2019 - December 2021")



    
##----------------------------------------
##SHOW OTHER PROJECTS IF NECESSARY!
# def showOtherProjects():
#     st.write('\n')
#     st.subheader("Other Projects")
#     st.write("---")
#     for project, link in OTHER_PROJECTS.items():
#         st.write(f"[{project}]({link})")


##-------------DISPLAY MENU---------------
#ADD  'Leadership', 'Academic Activities', 'Community Projects'
# display = st.multiselect('Display', ['Relevant Skills and Courses', 'Relevant Experience', 'Relevant Projects', 'Other Projects'])
# print(display)
# if 'Relevant Skills and Courses' in display:
#     showSkillsAndCourses()
# if 'Relevant Experience' in display:
#     showRelevantExperience()
# if 'Relevant Projects' in display:
#     showRelevantProjects()
# if 'Other Projects' in display:
#     showOtherProjects()

#---------------SITE LAYOUT----------------
with st.expander("Relevant Skills and Courses"):
    showSkillsAndCourses()
with st.expander("Relevant Experience"):
    showRelevantExperience()
with st.expander("Relevant Projects"):
    showRelevantProjects()
with st.expander("More Work Experience"):
    showMoreWorkExperience()
with st.expander("Leadership and Academic Activities"):
    showLeadership()

