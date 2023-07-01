from langchain import OpenAI
from langchain.text_splitter import  RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import TextLoader

class LangChainSummariser:
    def __init__(self, openai_api_key, filepath):
        self.openai_api_key  = openai_api_key
        self.llm = OpenAI(model_name="text-davinci-003", temperature=0, openai_api_key=openai_api_key)
        self.filepath = filepath
        self.documents = []
        self.texts = []
        self.chain = {}
        self.results = ""
    def load(self):
        loader = TextLoader(self.filepath)
        self.documents = loader.load()
        return self.documents

    def split(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=50)
        self.texts = text_splitter.split_documents(self.documents)
        return self.texts
    def initChain(self):
        self.chain = load_summarize_chain(self.llm, chain_type="map_reduce", verbose=False)
    def summarize(self):
        self.results =   self.chain.run(self.texts)
        return self.results