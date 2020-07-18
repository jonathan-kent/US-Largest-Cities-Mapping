from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class lat_long_searcher:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        #add chrome webdriver file path
        self.driver = webdriver.Chrome('C:/Users/Jonathan/bin/chromedriver.exe',chrome_options=chrome_options)
        self.driver.get("https://www.google.com")

    def get_coords(self, city):
        city = city.replace(" ", "+")
        self.driver.get("https://www.google.com/search?q="+city+"+latitude+and+longitude")
        coords = self.driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[1]").text
        return coords

def format_coords(coords, city):
    coords = coords.replace("°", "")
    coords = coords.replace("N", "")
    coords = coords.replace("W", "")
    coords = coords.replace(" ", "")
    coords = coords.replace(",", ";-")
    return city+";"+coords
    
def colect_coords():
    searcher = lat_long_searcher()

    for i in range(1820,2020,10):
        print(i)
        year = str(i)
        file = open(year+".txt", "r")
        entries = file.readlines()
        file.close()
        for entry in entries:
            entry = entry.replace("\n", "")
            parsed = entry.split(";")
            file = open("coords.txt", "r")
            lines = file.readlines()
            file.close()
            total = ""
            for line in lines:
                total = total + line
            if parsed[1] not in total:
                coords = format_coords(searcher.get_coords(parsed[1]), parsed[1])
                file = open("coords.txt", "a")
                file.writelines([coords+"\n"])
                file.close()

def add_coords():
    file = open("coords.txt", "r")
    coords_lines = file.readlines()
    file.close()
    for i in range(1790,2020,10):
        print(i)
        year = str(i)
        file = open(year+".txt", "r")
        entries = file.readlines()
        file.close()
        file = open(year+".txt", "w")
        for entry in entries:
            entry = entry.replace("\n", "")
            parsed = entry.split(";")
            for coords in coords_lines:
                if parsed[1] in coords:
                    coords_split = coords.split(";")
                    print("entry: "+entry+" coords: "+coords_split[1]+" "+coords_split[2])
                    file.writelines(entry+";"+coords_split[1]+";"+coords_split[2]+"\n")
        file.close()
        


