# 1. Library imports
#pip install requests

# 2. Introduce the application
print("\t\t歡迎進入旅遊地點天氣預測!\n\n")
print("本次要旅遊城市及地點是歐洲克羅埃西亞，輸入完後請按下按鈕! Let's Go!\n\n")

# 3. input of the city name from the user using the code
#city_name = input("輸入旅遊城市名稱 : (例如 Tokyo) ")
city_name1 = 'Vienna'
city_name2 = 'Zadar'
city_name3 = 'Omis'
city_name4 = 'Dubrovnik'
city_name5 = 'Kotor'
city_name6 = 'Mostar'
city_name7 = 'Hvr'
city_name8 = 'Split'
city_name9 = 'Plitvica'

# 4. importing the requests module
import requests

# 5. We will create a function that will take the name of the city the user enters and prints the report for us. Look at the code of the function below.
def Gen_report(C):
    print("旅遊城市 : " + C)
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
#Gen_report(city_name)
Gen_report(city_name1)
Gen_report(city_name2)
Gen_report(city_name3)
Gen_report(city_name4)
Gen_report(city_name5)
Gen_report(city_name6)
Gen_report(city_name7)
Gen_report(city_name8)
Gen_report(city_name9)
