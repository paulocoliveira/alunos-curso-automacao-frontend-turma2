from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WebDriverSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            chrome_options = Options()
            chrome_options.add_argument("--disable-search-engine-choice-screen")
            my_service = Service(ChromeDriverManager().install())
            cls._instance = webdriver.Chrome(service=my_service, options=chrome_options)
        
        return cls._instance

    @classmethod
    def quit_instance(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None