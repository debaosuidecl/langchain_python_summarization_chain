
from classes import KeywordScaleSerp as KSSModule, LangChainSummariser as LCSModule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values


def main(keyword, link_count):
    env_vars = dotenv_values()
    #env variables
    openai_api_key = env_vars["openai_api_key"]
    serp_api_key = env_vars["serp_api_key"]
    chromedriver_path = env_vars["chromedriver_path"]
    # INITIALISE WEB DRIVER
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    # get the keyword items in the array
    keywordScaleSerp = KSSModule.KeywordScaleSerp(keyword, serp_api_key, link_count=link_count)
    res = keywordScaleSerp.get_keyword_scaleserp()
    if res == False : return print("Could not find key word array")
    # Load the web pages
    file_path = "data/output_final.txt"
    with open(file_path, 'w') as file:
    # Append the string to the file
        file.write("")
    # index = 0
    for index,x in enumerate(res):
        link = x['link']
        print(f"{index+1}. processing this link now {link}")
        try:
            driver.get(link)  
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            # Find all elements that contain text
            texts =  driver.find_element(By.XPATH, "/html/body").text
            file_path = "data/output_final.txt"
            with open(file_path, 'a') as file:
            # Append the string to the file
                file.write(texts+ "\n")
            print("done")
        except Exception as e:
            print(e)
    driver.quit()
    summarizer = LCSModule.LangChainSummariser(openai_api_key=openai_api_key,  filepath="data/output_final.txt" )
    print("summarizing")
    summarizer.load().split().initChain().summarize()
    print(summarizer.results)
    return summarizer.results
    
main(keyword="BBQ", link_count= 10)
