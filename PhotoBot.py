from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech

def bot(myTextNew):
    chrome_options = webdriver.ChromeOptions()
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    chrome_options.add_experimental_option("detach", True)
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(r'C:\\Users\\Amit\\Documents\\Academics\\NCI\\Semester_3\\chromedriver.exe',
                              chrome_options=chrome_options)

    driver.get('https://www.facebook.com')

    driver.implicitly_wait(10)

    crack_cookies = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[1]')
    crack_cookies.click()

    # Below code is for logging into the account

    user_name = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')

    user_name.send_keys('username@email.com')

    pwd = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')

    pwd.send_keys('EnterTheRelevantPassword')

    login = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

    login.click()

    fb_search = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/label/input")

    fb_search.send_keys(myTextNew)
    fb_search.send_keys(Keys.RETURN)

    # Passing the white screen

    #time.sleep(7)

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak

import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

while True:
    with sr.Microphone() as source:
        print("Talk")
        SpeakText("What will you like to search on Facebook?")
        audio_text = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            text_recognize = r.recognize_google(audio_text)
            print("Text: " + text_recognize)
            SpeakText("Did you say {}".format(text_recognize))
            with sr.Microphone() as newSource:
                print("Please confirm")
                audio_text_confirmation = r.listen(newSource)
                try:
                    text_recognize_confirmation = r.recognize_google(audio_text_confirmation)
                    print(text_recognize_confirmation)
                    if text_recognize_confirmation == "yes":
                        bot(text_recognize)
                        break

                except:
                    print("Error")

        except:
            print("Sorry, I did not get that")