# 1. Library imports
#pip install requests

# 2. Introduce the application
print("\t\t歡迎進入旅遊地點天氣預測!\n\n")
print("請輸入旅遊城市名稱，輸入完後請按下按鈕! Let's Go!\n\n")

# 3. input of the city name from the user using the code
city_name = input("輸入旅遊城市名稱 : (例如 Tokyo) ")

# 4. importing the requests module
import requests

# 5. We will create a function that will take the name of the city the user enters and prints the report for us. Look at the code of the function below.
def Gen_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
Gen_report(city_name)
