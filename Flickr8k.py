import time
from selenium import webdriver
import os
import glob
import zipfile
import  shutil


def zipExtract(dataset_name):
    working_directory = r"C:\Users\Amit\Documents\Academics\NCI\Semester_3\Research_project"
    #print(working_directory)
    username = os.environ.get("USERNAME")
    downloads_folder = "C:/Users/{0}/Downloads/*".format(username)
    #print(downloads_folder)
    # Checking the latest file downloaded
    list_of_files = glob.glob(downloads_folder)
    latest_file = max(list_of_files, key=os.path.getmtime)
    #print(latest_file)
    # unzipping the file to the Python working directory
    try:
        with zipfile.ZipFile(latest_file, 'r') as zip_ref:
                zip_ref.extractall(working_directory)
                print("Files - {} unzipped successfully in the working directory!".format(dataset_name))
        os.remove("C:/Users/{0}/Downloads/{1}".format(username, dataset_name + ".zip"))
    except NameError:
        print("Unable to locate the file to unzip")


driver = webdriver.Chrome(r'C:\Users\Amit\Documents\Academics\NCI\Semester_3\chromedriver.exe')

driver.get("https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip")
time.sleep(5)
zipExtract("Flickr8k_text")

# Downloading Flickr8k Dataset

working_directory = os.getcwd()
username = os.environ.get("USERNAME")
downloads_folder = "C:/Users/{0}/Downloads/*".format(username)

driver.get("https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip")
counter = 1


def create_file():
    file = open(r"C:\Users\Amit\Documents\Academics\NCI\Semester_3\Research_project\Flickr8k.lemma.token.txt", "r")
    counter_file = 1
    with open(r'C:\Users\Amit\Documents\Academics\NCI\Semester_3\Research_project\newfile.text', 'wt') as f:
        for words in file.readlines():
            if counter_file == 1:
                f.write("image,caption")
                f.write("\n")
                counter_file += 1
            line = words.split("#")
            line[1] = line[1].replace("\t", "")
            line[1] = line[1].replace(line[1][0], "")
            line1 = ",".join(line)
            f.write(line1)

    f.close()
    file.close()
    os.rename(r'C:\Users\Amit\Documents\Academics\NCI\Semester_3\Research_project\newfile.text',
              r'C:\Users\Amit\Documents\Academics\NCI\Semester_3\Research_project\captions.txt')
    os.remove(r'C:\Users\Amit\Documents\Academics\NCI\Semester_3\Research_project\Flickr8k.lemma.token.txt')


def killfile():
    del_files = ['CrowdFlowerAnnotations.txt', 'ExpertAnnotations.txt', 'Flickr_8k.devImages.txt', 'Flickr_8k.testImages.txt', 'Flickr_8k.trainImages.txt', 'Flickr8k.token.txt', 'readme.txt']
    for file in del_files:
        os.remove(r'C:\Users\Amit\Documents\Academics\NCI\Semester_3\Research_project\{}'.format(file))
    shutil.rmtree(r'C:\Users\Amit\Documents\Academics\NCI\Semester_3\Research_project\__MACOSX')
    # os.rmdir(r'C:\Users\Amit\Documents\Academics\NCI\Semester_3\Research_project\__MACOSX')


while True:
    list_of_files = glob.glob(downloads_folder)
    latest_file = max(list_of_files, key=os.path.getctime)
    if latest_file == r"C:/Users/{0}/Downloads\Flickr8k_Dataset.zip".format(username):
        print("File Found")
        zipExtract("Flickr8k_Dataset")
        driver.close()
        driver.quit()
        killfile()
        create_file()
        break
    else:
        time.sleep(10)
        print("Checked attempt #{}".format(counter))
        counter += 1
