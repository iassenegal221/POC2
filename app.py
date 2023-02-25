import streamlit as st 

#Necessary NLP Packaages 
import nltk
from textblob import TextBlob

#Sumy Packages 
import sumy
## pip install -U sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer
import spacy as sp
#import en_core_web_sm


st.set_page_config(page_title="KeyText")

def summarizer(text , sentences):
   
    """Summarize the text."""
    nltk.download('punkt')
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

def sentiment(text):
    """Sentiment Analysis of the text."""
    blob = TextBlob(text)
    return blob.sentiment
from keybert import KeyBERT
def keywords(text,num):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text,keyphrase_ngram_range=(1, num))
    return keywords
## Entity extraction
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import spacy
#pip3 install https://github.com/explosion/spacy-models/releases/download/fr_core_news_sm-2.2.0/fr_core_news_sm-2.2.0.tar.gz

def entity_extractor(text):
    spacy.cli.download("fr_core_news_sm")
    final_stopwords_list = stopwords.words('english') + stopwords.words('french')
    nlp = sp.load('fr_core_news_sm')##sp.load('en_core_web_sm')
    docs = nlp(text)
    tokens = [token.text for token in docs]
    tokens = [i for i in tokens if i.lower() not in final_stopwords_list]
    entities = [(ent.text, ent.label_) for ent in docs.ents]
    finaldata = [entities]#['"Tokens":{},\n"Entities":{}'.format(tokens,entities)]
    return finaldata

def main():
    st.image('logo.jpeg')
    import pdf
    pdf.f()

   # st.set_page_config(
   #  page_title="NLP APP",
   #  page_icon=":computer:",
   #  layout="centered",
   #  initial_sidebar_state="collapsed",
   #  menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is an *extremely* cool app!"
   #  }
# )
    
    ############################################################

    ########################################################
    #st.markdown("<h1 style='text-align: center; color: black;'>Mon tableau de bord</h1>", unsafe_allow_html=True)
    #uploaded_file = st.file_uploader("Choisir un fichier au bon format", type="pdf")
    #from PyPDF2 import PdfReader

    #if uploaded_file is not None:
      ## st.text_area(label ="tet",value=reader, height =100)



 
    st.title("Multi NLP task Web App") 
    with st.expander("About the application",expanded=False):
     st.write("""
        This is an application that integrates different use case applications of Natural Language Processing (NLP) that are the summarization of long passages into just few sentences and then detection of the sentiment in the text.
     """)
     
    
    #Getting the text from the user
    task =  st.selectbox("Select An Action You Want To Perform ",("None","Summarize Text","Detect Sentiment","Extract keywords","Extract entity"))
        #Text Summarizer 
    if task == "Summarize Text":
        InputText = st.text_area( "Paste the text that you want to summarize here.", "")
        sentencesCount= st.slider('Select sentence count', 1, 10 , value = 1)
        st.write("The above text will be summarized into {sentencesCount} sentences.".format(sentencesCount=sentencesCount))
        if st.button("Okay, Generate Summary"):
                st.caption("Using the sumy automatic summarizer module........")
                st.success("The summary result is:")
                st.write(summarizer(InputText , sentencesCount))

    #Sentiment Analysis
    elif task == "Detect Sentiment":
        InputText = st.text_area("Paste the message that you want to analyze here.", "")
        if st.button("Detect Sentiment"):
            st.success("The sentiment results of the above message is:")
            st.write(sentiment(InputText))
    #Keywords Extraction
    elif task == "Extract keywords":
        InputText = st.text_area("Paste the text that you want to analyze here.", "")
        keywordsCount= st.slider('Select number of keywords', 1, 10 , value = 1)#########
        st.write("Keywords will be extracted {keywordsCount} here.".format(keywordsCount=keywordsCount))
       # top_n = st.selectbox("select a stopwords", (2,3,4,5,6,7))
        if st.button("Extract keywords"):
            st.success("The most relevant of the above text is:")
            st.write(keywords(InputText,keywordsCount))
    ## Entity extraction
    elif task == "Extract entity":
        InputText = st.text_area("Paste the text that you want to analyze here.", "")
        
        if st.button("Extract entity"):
            st.success("The extracted entities of the above text is:")
            st.write(entity_extractor(InputText))
    
    else:
        st.subheader("Nothing to do here!")
        st.write("Please select an action from the dropdown menu.")


    st.sidebar.subheader("Developed happily by")
    st.sidebar.text("Ndiaye Dia ")
    st.sidebar.write("Visit me on :")
    st.sidebar.write("[Github](https://ias.sn)")
    st.sidebar.info("Happy Streamlit-ing!")

   
    # with st.container():  
    #     if st.button("Refresh Page"):
    #         pyautogui.hotkey("ctrl","F5")
           # st.legacy_caching.clear_cache()
           
           

if __name__ == '__main__':
    main()





