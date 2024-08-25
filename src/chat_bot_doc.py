import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.schema import Document
api_key = "sk-proj-IY4k2UUbxBt4dUWyfp85T3BlbkFJLyjumT9QPCrybc6Ta1jd"
pdf_path = r'D:\PSCA\Chat Bot\resources\text.pdf'  # Path to your pre-trained PDF file

def get_pdf_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        chunk_size=500, chunk_overlap=50, separator="\n"
    )
    chunks = text_splitter.split_text(text)
    return chunks
def init_faiss_index():
    index_path = "/content/drive/MyDrive/PSCA/faiss_index"
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=api_key)
    
    if os.path.exists(index_path):
        try:
            vector_store = FAISS.load_local(index_path, embeddings)
            print("FAISS index loaded successfully.")
            return vector_store
        except Exception as e:
            print(f"Error loading FAISS index: {e}")
    
    print("Creating new FAISS index...")
    pdf_text = get_pdf_text(pdf_path)
    text_chunks = get_text_chunks(pdf_text)
    vector_store = get_vector_store(text_chunks)
    
    if vector_store:
        vector_store.save_local(index_path)
        print("New FAISS index saved successfully.")
    
    return vector_store
def get_vector_store(text_chunks):
    try:
        embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=api_key)
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        print("FAISS index created successfully.")
        return vector_store
    except Exception as e:
        print(f"Error while creating vectors: {str(e)}")
        return None

def create_faiss_index():
    pdf_text = get_pdf_text(pdf_path)
    text_chunks = get_text_chunks(pdf_text)
    get_vector_store(text_chunks)

# Call this function at the beginning of your main() function
def get_conversational_chain(temperature=0.8):
    prompt_template = """
    Please act as a Correspondent for the Punjab Safe City Authority, which is a law enforcement agency responsible to provide immidiate response in any emergency.
    Your role is to provide accurate and detailed information to users based on the provided context Answer should be in same language in which user ask the question.
    like for example:"user":"mujhe pakistan k bary me batao", output:"Pakistan South Asia mein ek mulk hai, jiska hadood India, Afghanistan, Iran, aur China se lagti hai, aur iska samundari kinaara Arabian Sea ke saath hai. Iski ek bohat hi purani tareekh aur mukhtalif culture hai. Qaumi zubaan Urdu hai, aur Islam qaumi mazhab hai. Iska darul hukoomat Islamabad hai, jabkay Karachi sab se bara sheher hai."
    Provide detailed and correct answers using the information from the given context.
    If the relevant information is not found in the context,or If the answer cannot be found from either source, respond with: "Sorry, I am unable to process this query."
    the provided context Answer should be in same language in which user ask the question.
    Answer the query always concise and short.
    You must be able to answer the query if the query is like a situation.
    Do not give any irrelevant information, always try to give answer according to the query, and always give answer in which the user asks.....
    Title each response with the user’s query.
    Use bullet points to clearly list relevant information whenever possible.
    the provided context Answer should be in same language in which user ask the question.
    Do not guess or provide incorrect answers.
    the provided context Answer should be in same language in which user ask the question.
    Context: \n {context} \n
    Question: \n {question} \n

    Answer:
    """

    llm = OpenAI(api_key=api_key,temperature=temperature)
    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=api_key)
    try:
        new_db = FAISS.load_local(
            "/content/drive/MyDrive/PSCA/faiss_index", embeddings, allow_dangerous_deserialization=True
        )
        print("FAISS index loaded successfully.")
    except ValueError as e:
        print(f"Error loading FAISS index: {e}")
        st.write("Error loading FAISS index.")
        return
    
    # ... rest of the function remains the same

    docs = new_db.similarity_search(user_question)
    print(f"Similar Chunk: {docs}")

    max_context_length = 4097
    total_tokens = 0
    chunks = []
    for doc in docs:
        chunk = doc.page_content
        chunk_tokens = len(chunk.split())
        if total_tokens + chunk_tokens <= max_context_length:
            # Create a Document instance for each chunk
            document = Document(page_content=chunk, metadata={})
            chunks.append(document)
            total_tokens += chunk_tokens
        else:
            break

    chain = get_conversational_chain()
    response = chain({"input_documents": chunks, "question": user_question})
    print(response)
    st.write(response["output_text"])

def main():
    import os
    if not os.path.exists("/content/drive/MyDrive/PSCA/faiss_index"):
        create_faiss_index()
    st.set_page_config(page_title="Punjab Safe City Authority", page_icon=":shield:", layout="wide")
    vector_store = init_faiss_index()
    if not vector_store:
        st.error("Failed to initialize FAISS index. Please check your setup and try again.")
        return
    # Sidebar
    st.sidebar.image(r"D:\PSCA\Chat Bot\resources\PSCA-logo.png", use_column_width=True)
    st.sidebar.title("Quick Access")

    # Group buttons in the sidebar
    button_groups = {
        "Emergency Services": ["Emergency 15", "Panic Button"],
        "Traffic & Transportation": ["Traffic E-Challan", "Rasta FM88.6", "Free Wi-Fi Services"],
        "Safety & Security": ["Crime Stoppers", "Virtual Women Police Station", "Virtual Center for Child Safety"],
        "Other Services": ["Internship Program", "Electronic Data Analysis Center", "Download Women's Safety & Punjab Police App"]
    }

    selected_service = None
    for group, buttons in button_groups.items():
        st.sidebar.subheader(group)
        for button in buttons:
            if st.sidebar.button(button, key=button):
                selected_service = button

    # Main content area
    st.title("Punjab Safe City Authority Chat Assistant")
    st.markdown("Welcome to the Punjab Safe City Authority chatbot. Ask any question or use the quick access buttons on the left.")

    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What would you like to know about Punjab Safe City Authority?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            docs = vector_store.similarity_search(prompt)
            
            max_context_length = 4097
            total_tokens = 0
            chunks = []
            for doc in docs:
                chunk = doc.page_content
                chunk_tokens = len(chunk.split())
                if total_tokens + chunk_tokens <= max_context_length:
                    document = Document(page_content=chunk, metadata={})
                    chunks.append(document)
                    total_tokens += chunk_tokens
                else:
                    break

            chain = get_conversational_chain()
            response = chain({"input_documents": chunks, "question": prompt})
            full_response = response["output_text"]
            
            message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    # Display information for selected service
    if selected_service:
        # Display corresponding text area based on button pressed
        st.subheader(f"Information about {selected_service}")
        if selected_service== "Emergency 15":
            st.markdown("### Emergency 15 🚨")
            st.markdown("""
            **کسی بھی ہنگامی صورتحال میں فوری مدد کے لیے  15 پر کال کریں۔**

            اپنی شکایت آن لائن درج کرنے کے لیے، براہ مہربانی وزٹ کریں:
            [https://psca.gop.pk/onefive/](https://psca.gop.pk/onefive/)

            **For any emergency, please call 15 immediately.**

            To register your online complaint, please visit:
            [https://psca.gop.pk/onefive/](https://psca.gop.pk/onefive/)
            """)
            

        elif selected_service== "Virtual Women Police Station":
            st.markdown("### Virtual Women Police Station 👮‍♀️")
            st.markdown("""
            **ورچوئل ویمنز پولیس اسٹیشن پر اپنی شکایت درج کرانے کے لیے براہ مہربانی وزٹ کریں:**
            [https://psca.gop.pk/virtual-women-police-station](https://psca.gop.pk/virtual-women-police-station)

            **To register your complaint on Virtual Women's Police Station please visit:**
            [https://psca.gop.pk/virtual-women-police-station](https://psca.gop.pk/virtual-women-police-station)
            """)
            

        elif selected_service== "Virtual Center for Child Safety":
            st.markdown("### Virtual Center for Child Safety 🛡️")
            st.markdown("""
            **ورچوئل سینٹر فار چائلڈ سیفٹی صوبہ پنجاب میں بچوں کے تحفظ کو یقینی بنانے کے لیے اپنی نوعیت کا واحد مرکز ہے۔**
            بچوں کے بارے میں شکایات یہاں درج کی جا سکتی ہیں:
            [https://psca.gop.pk/vccs/](https://psca.gop.pk/vccs/)

            **The pioneering Virtual Center for Child Safety provides a physical hub dedicated to safeguarding children, ensuring their well-being and protection in the province of Punjab.**

            Complaints about children can be lodged here:
            [https://psca.gop.pk/vccs/](https://psca.gop.pk/vccs/)
            """)
            

        elif selected_service== "Traffic E-Challan":
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
            

        elif selected_service== "Crime Stoppers":
            st.markdown("### Crime Stoppers 🕵️")
            st.markdown("""
            **کرائم سٹاپرز جرائم کی اطلاع دینے کے لیے ایک خفیہ سروس ہے جو 100 فیصد صیغہ راز کی ضمانت دیتی ہے۔**
            
            اپنی شکایت درج کرنے کے لیے براہ مہربانی وزٹ کریں:
            [https://crimestoppers.psca.gop.pk:1787/PublicComplaint](https://crimestoppers.psca.gop.pk:1787/PublicComplaint)
            
            **Crime Stoppers is an anonymous crime reporting service that guarantees 100% anonymity.**

            To register your complaint, please visit:
            [https://crimestoppers.psca.gop.pk:1787/PublicComplaint](https://crimestoppers.psca.gop.pk:1787/PublicComplaint)
            """)
            

        elif selected_service== "Free Wi-Fi Services":
            st.markdown("### Free Wi-Fi Services 📶")
            st.markdown("""
            **وزیرِ اعلیٰ پنجاب مریم نواز شریف کی ہدایت پر سیف سٹی ایمرجنسی میں شہریوں کی سہولت کیلئے فری وائی فائی سروس فراہم کر رہی ہے۔**

            Please visit for nearby free Wi-Fi:
            [https://psca.gop.pk/free-wifi-service/](https://psca.gop.pk/free-wifi-service/)
            """)
            

        elif selected_service== "Panic Button":
            st.markdown("### Panic Button 🚨")
            st.markdown("""
            **پینک بٹن شہریوں کے لئے ایک سیفٹی زون ہے۔ کسی بھی ایمرجنسی کی صورت میں پینک بٹن دبانے سے شہری سیف سٹی نمائندے سے بات کرسکتے ہیں۔**

            Panic buttons are installed on the following locations:
            [https://psca.gop.pk/panic-buttons/](https://psca.gop.pk/panic-buttons/)
            """)
            

        elif selected_service== "Download Women's Safety App":
            st.markdown("### Download Women's Safety & Punjab Police App 📱")
            st.markdown("""
            **ویمن سیفٹی ایپ ڈاؤن لوڈ کریں**
            [Android](https://play.google.com/store/apps/details?id=com.psca.ppic3.womensafety&hl=ur)
            [iOS](https://apps.apple.com/pk/app/punjab-police-women-safety-app/id1487787591)
            """)
            
                
                
        elif selected_service== "Internship Program":
            st.markdown("### Internship Program 💼")
            st.markdown("""
                        شپ کی سہولت بھی فراہم کرتا ہے تاکہ وہ عملی زندگی میں قدم رکھنے سے پہلے تیار ہو سکیں. آرٹیفیشل انٹیلیجنس، مشین لرننگ، نیٹ ورکنگ، سافٹ ویئر ڈویلپمنٹ، ڈیٹا بیس ایڈمنسٹریشن، سسٹم ایڈمنسٹریشن یا دیگر متعلقہ شعبہ جات میں طلباء و طالبات سیف سٹی کی اس سروس سے فائدہ اٹھا سکتے ہیں تاکہ وہ اپنے آپ کو دورِ حاضر کے جدید تقاضوں سے ہم آہنگ کر سکیں۔
        آپ اس لنک پر انٹرن شپ کے لیے اپلائی کر سکتے ہیں۔
        https://psca.gop.pk/apply-for-internship

        Internship Program
        Safe City offers internship programs to fresh graduates to prepare them for the professional world. Whether it is Artificial Intelligence, Machine Learning, Networking, Software Development, Database Administration, System Administration or any other field related to Safe City services, fresh graduates can take advantage of our services to learn and prepare for the professional life.

        Please apply for internship:
        https://psca.gop.pk/apply-for-internship/""")
            
                
        elif selected_service== "Rasta FM88.6":
            st.markdown("### Rasta FM88.6 📻")
            st.markdown("""
                        
        راستہ ایف ایم 88.6 ایک اور عوامی خدمت ہے جسے سیف سٹی نے عام لوگوں کے لیے متعارف کروایا ہے۔ راستہ ایف ایم شہریوں کو ٹریفک جام، احتجاج، سڑکوں کی بندش یا کسی دوسری رکاوٹ کے بارے میں رہنمائی فراہم کرتا ہے۔ اس کے استعمال سے وہ آسانی اور محفوظ طریقے سے اپنی منزل تک پہنچ سکتے ہیں۔ ایف ایم 88.6 پر ٹیون ان کریں اور ٹریفک ایڈوائزری کے ساتھ میوزک اور ٹاک شوز سے لطف اندوز بھی ہوں۔

        Raasta FM 88.6
        Raasta FM 88.6 is another public service introduced by Safe City for general public. Raasta FM guides the citizens about traffic jams, protests, road closures or any other hindrance which they can avoid to reach their destination easily and safely. Tune in to FM 88.6 and enjoy music and talk shows along with traffic advisory.""")
            


        elif selected_service== "Electronic Data Analysis Center":
            st.markdown("### Electronic Data Analysis Center 💻")
            st.markdown("""الیکٹرانک ڈیٹا انیلیسز سینٹر
        سیف سٹی عوام اور قانون نافذ کرنے والے اداروں کو فوٹیج یا ویڈیو شہادت فراہم کرنے کی سہولت بھی دیتا ہے. شہری اپنے کیس کے تفتیشی افسر کے ساتھ آ کر اور قانونی تقاضے پورے کرنے کے بعد متعلقہ ویڈیو دیکھ سکتے ہیں اور حاصل بھی کر سکتے ہیں۔

        Electronic Data Analysis Center
        Safe City provides services for the general public as well as Law Enforcement Agencies to watch video footage of any incident and get the required video evidence from Safe City after due process. Citizens can come with the relevant Investigation Officer (IO) of the case and watch / get the required footage after fulfilling the legal requirements.""")
            


        elif selected_service== "Other Services":
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
         

if __name__ == "__main__":
    main()
