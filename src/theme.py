import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ece9e6, #ffffff);
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        border-radius: 10px;
        background-color: #007BFF;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #cccccc;
        padding: 15px;
        font-size: 16px;
    }
    .card {
        background: #ffffff;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 20px 0;
    }
    a {
        color: #007BFF;
        font-weight: bold;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)


# Define the main menu buttons
def main_menu():
    st.title("Punjab Safe City Authority Services")
    if st.button("Emergency 15 🚨"):
        emergency_15()
    elif st.button("Virtual Women Police Station 👮‍♀️"):
        virtual_women_police_station()
    elif st.button("Virtual Center for Child Safety 🛡️"):
        virtual_center_for_child_safety()
    elif st.button("Traffic E-Challan 🚗"):
        traffic_echallan()
    elif st.button("Crime Stoppers 🕵️"):
        crime_stoppers()
    elif st.button("Free Wi-Fi Services 📶"):
        free_wifi_services()
    elif st.button("Panic Button 🚨"):
        panic_button()
    elif st.button("Download Women's Safety & Punjab Police App 📱"):
        download_women_safety_app()
    elif st.button("Internship Program 💼"):
        internship_program()
    elif st.button("Raasta FM 88.6 🎙️"):
        raasta_fm()
    elif st.button("Electronic Data Analysis Center 💻"):
        electronic_data_analysis_center()
    elif st.button("Other Services 🛠️"):
        other_services()


def emergency_15():
    hide_main_menu()
    st.markdown("""
    <div class="card">
        <h3>Emergency 15 🚨</h3>
        <p>کسی بھی ہنگامی صورتحال میں فوری مدد کے لیے 15 پر کال کریں۔</p>
        <p>اپنی شکایت آن لائن درج کرنے کے لیے، براہ مہربانی وزٹ کریں: 
        <a href="https://psca.gop.pk/onefive/" target="_blank">https://psca.gop.pk/onefive/</a></p>
        <p>For any emergency please call 15 immediately.</p>
        <p>To register your online complaint, please visit:
        <a href="https://psca.gop.pk/onefive/" target="_blank">https://psca.gop.pk/onefive/</a></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Main Menu"):
        main_menu()

def virtual_women_police_station():
    hide_main_menu()
    st.markdown("""
    <div class="card">
        <h3>Virtual Women Police Station 👮‍♀️</h3>
        <p>ورچوئل ویمنز پولیس اسٹیشن پر اپنی شکایت درج کرانے کے لیے براہ مہربانی وزٹ کریں:
        <a href="https://psca.gop.pk/virtual-women-police-station" target="_blank">https://psca.gop.pk/virtual-women-police-station</a></p>
        <p>To register your complaint on Virtual Women's Police Station please visit:
        <a href="https://psca.gop.pk/virtual-women-police-station" target="_blank">https://psca.gop.pk/virtual-women-police-station</a></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Main Menu"):
        main_menu()

# Define the other functions similarlydef hide_main_menu():
    st.markdown("""
    <style>
    .stButton button {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.image(r"C:\Users\jalal\Downloads\PSCA.jpg",width=200)


st.title("Welcome to Punjab Safe City Authority")

# Define a session state to handle the selected button
if "selected_button" not in st.session_state:
    st.session_state.selected_button = None

# Function to reset to main menu
def go_to_main_menu():
    st.session_state.selected_button = None

# Main menu buttons
if st.session_state.selected_button is None:
    st.markdown("### Hello Engineer Jalal, Salam! How can we help you today?")
    st.markdown("Please choose an option below:")

    if st.button("Emergency 15 🚨"):
        st.session_state.selected_button = "Emergency 15"
    
    if st.button("Virtual Women Police Station 👮‍♀️"):
        st.session_state.selected_button = "Virtual Women Police Station"
    
    if st.button("Virtual Center for Child Safety 🛡️"):
        st.session_state.selected_button = "Virtual Center for Child Safety"
    
    if st.button("Traffic E-Challan 🚗"):
        st.session_state.selected_button = "Traffic E-Challan"
    
    if st.button("Crime Stoppers 🕵️"):
        st.session_state.selected_button = "Crime Stoppers"
    
    if st.button("Free Wi-Fi Services 📶"):
        st.session_state.selected_button = "Free Wi-Fi Services"
    
    if st.button("Panic Button 🚨"):
        st.session_state.selected_button = "Panic Button"
    
    if st.button("Download Women's Safety & Punjab Police App 📱"):
        st.session_state.selected_button = "Download Women's Safety App"
    
    if st.button("Internship Program 💼"):
        st.session_state.selected_button = "Internship Program"
    
    if st.button("Rasta FM88.6 📻"):
        st.session_state.selected_button = "Rasta FM88.6"
    
    if st.button("Electronic Data Analysis Center 💻"):
        st.session_state.selected_button = "Electronic Data Analysis Center"
    
    if st.button("Other Services 🛠️"):
        st.session_state.selected_button = "Other Services"

# Display corresponding text area based on button pressed
if st.session_state.selected_button == "Emergency 15":
    st.markdown("### Emergency 15 🚨")
    st.markdown("""
    **کسی بھی ہنگامی صورتحال میں فوری مدد کے لیے  15 پر کال کریں۔**

    اپنی شکایت آن لائن درج کرنے کے لیے، براہ مہربانی وزٹ کریں:
    [https://psca.gop.pk/onefive/](https://psca.gop.pk/onefive/)

    **For any emergency, please call 15 immediately.**

    To register your online complaint, please visit:
    [https://psca.gop.pk/onefive/](https://psca.gop.pk/onefive/)
    """)
    if st.button("Go to Main Menu"):
        go_to_main_menu()

elif st.session_state.selected_button == "Virtual Women Police Station":
    st.markdown("### Virtual Women Police Station 👮‍♀️")
    st.markdown("""
    **ورچوئل ویمنز پولیس اسٹیشن پر اپنی شکایت درج کرانے کے لیے براہ مہربانی وزٹ کریں:**
    [https://psca.gop.pk/virtual-women-police-station](https://psca.gop.pk/virtual-women-police-station)

    **To register your complaint on Virtual Women's Police Station please visit:**
    [https://psca.gop.pk/virtual-women-police-station](https://psca.gop.pk/virtual-women-police-station)
    """)
    if st.button("Go to Main Menu"):
        go_to_main_menu()

elif st.session_state.selected_button == "Virtual Center for Child Safety":
    st.markdown("### Virtual Center for Child Safety 🛡️")
    st.markdown("""
    **ورچوئل سینٹر فار چائلڈ سیفٹی صوبہ پنجاب میں بچوں کے تحفظ کو یقینی بنانے کے لیے اپنی نوعیت کا واحد مرکز ہے۔**
    بچوں کے بارے میں شکایات یہاں درج کی جا سکتی ہیں:
    [https://psca.gop.pk/vccs/](https://psca.gop.pk/vccs/)

    **The pioneering Virtual Center for Child Safety provides a physical hub dedicated to safeguarding children, ensuring their well-being and protection in the province of Punjab.**

    Complaints about children can be lodged here:
    [https://psca.gop.pk/vccs/](https://psca.gop.pk/vccs/)
    """)
    if st.button("Go to Main Menu"):
        go_to_main_menu()

elif st.session_state.selected_button == "Traffic E-Challan":
    st.markdown("### Traffic E-Challan 🚗")
    st.markdown("""
    **اپنا ای چالان ڈاؤن لوڈ کرنے کے لیے، براہ مہانی وزٹ کریں:**
    [https://echallan.psca.gop.pk](https://echallan.psca.gop.pk)

    **To download your e-challan, please visit:**
    [https://echallan.psca.gop.pk](https://echallan.psca.gop.pk)

    You need to provide:
    - Plate Number
    - CNIC or Vehicle Chassis Number
    """)
    if st.button("Go to Main Menu"):
        go_to_main_menu()

elif st.session_state.selected_button == "Crime Stoppers":
    st.markdown("### Crime Stoppers 🕵️")
    st.markdown("""
    **کرائم سٹاپرز جرائم کی اطلاع دینے کے لیے ایک خفیہ سروس ہے جو 100 فیصد صیغہ راز کی ضمانت دیتی ہے۔**
    
    اپنی شکایت درج کرنے کے لیے براہ مہربانی وزٹ کریں:
    [https://crimestoppers.psca.gop.pk:1787/PublicComplaint](https://crimestoppers.psca.gop.pk:1787/PublicComplaint)
    
    **Crime Stoppers is an anonymous crime reporting service that guarantees 100% anonymity.**

    To register your complaint, please visit:
    [https://crimestoppers.psca.gop.pk:1787/PublicComplaint](https://crimestoppers.psca.gop.pk:1787/PublicComplaint)
    """)
    if st.button("Go to Main Menu"):
        go_to_main_menu()

elif st.session_state.selected_button == "Free Wi-Fi Services":
    st.markdown("### Free Wi-Fi Services 📶")
    st.markdown("""
    **وزیرِ اعلیٰ پنجاب مریم نواز شریف کی ہدایت پر سیف سٹی ایمرجنسی میں شہریوں کی سہولت کیلئے فری وائی فائی سروس فراہم کر رہی ہے۔**

    Please visit for nearby free Wi-Fi:
    [https://psca.gop.pk/free-wifi-service/](https://psca.gop.pk/free-wifi-service/)
    """)
    if st.button("Go to Main Menu"):
        go_to_main_menu()

elif st.session_state.selected_button == "Panic Button":
    st.markdown("### Panic Button 🚨")
    st.markdown("""
    **پینک بٹن شہریوں کے لئے ایک سیفٹی زون ہے۔ کسی بھی ایمرجنسی کی صورت میں پینک بٹن دبانے سے شہری سیف سٹی نمائندے سے بات کرسکتے ہیں۔**

    Panic buttons are installed on the following locations:
    [https://psca.gop.pk/panic-buttons/](https://psca.gop.pk/panic-buttons/)
    """)
    if st.button("Go to Main Menu"):
        go_to_main_menu()

elif st.session_state.selected_button == "Download Women's Safety App":
    st.markdown("### Download Women's Safety & Punjab Police App 📱")
    st.markdown("""
    **ویمن سیفٹی ایپ ڈاؤن لوڈ کریں**
    [Android](https://play.google.com/store/apps/details?id=com.psca.ppic3.womensafety&hl=ur)
    [iOS](https://apps.apple.com/pk/app/punjab-police-women-safety-app/id1487787591)
    """)
    if st.button("Go to Main Menu"):
        go_to_main_menu()
        
        
elif st.session_state.selected_button == "Internship Program":
    st.markdown("### Internship Program 💼")
    st.markdown("""
                شپ کی سہولت بھی فراہم کرتا ہے تاکہ وہ عملی زندگی میں قدم رکھنے سے پہلے تیار ہو سکیں. آرٹیفیشل انٹیلیجنس، مشین لرننگ، نیٹ ورکنگ، سافٹ ویئر ڈویلپمنٹ، ڈیٹا بیس ایڈمنسٹریشن، سسٹم ایڈمنسٹریشن یا دیگر متعلقہ شعبہ جات میں طلباء و طالبات سیف سٹی کی اس سروس سے فائدہ اٹھا سکتے ہیں تاکہ وہ اپنے آپ کو دورِ حاضر کے جدید تقاضوں سے ہم آہنگ کر سکیں۔
آپ اس لنک پر انٹرن شپ کے لیے اپلائی کر سکتے ہیں۔
https://psca.gop.pk/apply-for-internship

Internship Program
Safe City offers internship programs to fresh graduates to prepare them for the professional world. Whether it is Artificial Intelligence, Machine Learning, Networking, Software Development, Database Administration, System Administration or any other field related to Safe City services, fresh graduates can take advantage of our services to learn and prepare for the professional life.

Please apply for internship:
https://psca.gop.pk/apply-for-internship/""")
    if st.button("Go to Main Menu"):
        go_to_main_menu()
        
elif st.session_state.selected_button == "Rasta FM88.6":
    st.markdown("### Rasta FM88.6 📻")
    st.markdown("""
                
راستہ ایف ایم 88.6 ایک اور عوامی خدمت ہے جسے سیف سٹی نے عام لوگوں کے لیے متعارف کروایا ہے۔ راستہ ایف ایم شہریوں کو ٹریفک جام، احتجاج، سڑکوں کی بندش یا کسی دوسری رکاوٹ کے بارے میں رہنمائی فراہم کرتا ہے۔ اس کے استعمال سے وہ آسانی اور محفوظ طریقے سے اپنی منزل تک پہنچ سکتے ہیں۔ ایف ایم 88.6 پر ٹیون ان کریں اور ٹریفک ایڈوائزری کے ساتھ میوزک اور ٹاک شوز سے لطف اندوز بھی ہوں۔

Raasta FM 88.6
Raasta FM 88.6 is another public service introduced by Safe City for general public. Raasta FM guides the citizens about traffic jams, protests, road closures or any other hindrance which they can avoid to reach their destination easily and safely. Tune in to FM 88.6 and enjoy music and talk shows along with traffic advisory.""")
    if st.button("Go to Main Menu"):
        go_to_main_menu()


elif st.session_state.selected_button == "Electronic Data Analysis Center":
    st.markdown("### Electronic Data Analysis Center 💻")
    st.markdown("""الیکٹرانک ڈیٹا انیلیسز سینٹر
سیف سٹی عوام اور قانون نافذ کرنے والے اداروں کو فوٹیج یا ویڈیو شہادت فراہم کرنے کی سہولت بھی دیتا ہے. شہری اپنے کیس کے تفتیشی افسر کے ساتھ آ کر اور قانونی تقاضے پورے کرنے کے بعد متعلقہ ویڈیو دیکھ سکتے ہیں اور حاصل بھی کر سکتے ہیں۔

Electronic Data Analysis Center
Safe City provides services for the general public as well as Law Enforcement Agencies to watch video footage of any incident and get the required video evidence from Safe City after due process. Citizens can come with the relevant Investigation Officer (IO) of the case and watch / get the required footage after fulfilling the legal requirements.""")
    if st.button("Go to Main Menu"):
        go_to_main_menu()


elif st.session_state.selected_button == "Other Services":
    st.markdown("### Other Services 🛠️")
    st.markdown("""سیف سٹی سے متعلق مزید تازہ ترین معلومات کے لئے ہمیں فالو کریں:
Please follow us for latest updates:

Whatsapp Channel
https://whatsapp.com/channel/0029VajDNCx60eBgBtTwy61O

Facebook
https://www.facebook.com/punjabsafecities

Youtube
https://www.youtube.com/@PunjabSafeCitiesAuthority

Instagram
https://www.instagram.com/punjabsafecities/

Twitter
https://x.com/PSCAsafecities

LinkedIn
https://www.linkedin.com/company/punjabsafecities

Tiktok
https://www.tiktok.com/@safecitiesofficial
پنجاب سیف سٹیز اتھارٹی""")
    if st.button("Go to Main Menu"):
        go_to_main_menu()




if __name__ == "__main__":
    main_menu()
