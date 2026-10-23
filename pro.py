import tkinter as tk #for the UI
import openmeteo_requests   #imports the used API


openmeteo = openmeteo_requests.Client()

#builds the initial window
window = tk.Tk()                         
window.title("weather app")
window.geometry("1000x600")

label2 = tk.Label(window, text = "Linked in and Github: Theofilos Papathanasiou",height= 50,width=50)
label2.place(x = 0, y = - 300)






# for each button i want to create i need one function for the command
def athens():
        window.destroy()
        new_window = tk.Tk()
        new_window.title('WEATHER APP')
        new_window.geometry('1000x600')
        url1 = "https://api.open-meteo.com/v1/forecast"
        params = {
	        "latitude": 37.9838,
                "longitude": 23.7278,
	        "current": [
                "temperature_2m",
                "rain",
                "relative_humidity_2m"
                                         ]

                                            }
        responses = openmeteo.weather_api(url1, params=params)
        response = responses[0]

        print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation: {response.Elevation()} m asl")
        print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

        current = response.Current()

        current_temperature_2m = current.Variables(0).Value()
        current_rain = current.Variables(1).Value()
        current_relative_humidity_2m = current.Variables(2).Value()

        label1 = tk.Label(new_window, text=f"Current temperature of Athens: {current_temperature_2m:.1f}°C",height= 20,width= 40)
        label3 = tk.Label(new_window, text=f"Rain: {current_rain}",height= 20,width= 40)
        label4 = tk.Label(new_window, text=f"Relative Humidity: {current_relative_humidity_2m}",height= 20,width= 40)
        label1.pack()
        label3.pack()
        label4.pack()
        print(f"Current temperature_2m: {current_temperature_2m}")
        print(f"Current rain: {current_rain}")
        print(f"current_relative_humidity_2m{current_relative_humidity_2m}")
        
      

    
def thessaloniki():
                window.destroy()   #closes the old window to open another
                new_window = tk.Tk()   #initialization of the new window
                new_window.title('WEATHER APP')
                new_window.geometry('1000x600')
                url1 = "https://api.open-meteo.com/v1/forecast"
                params = {
                    "latitude": 40.6407,
                    "longitude": 22.9349,
                    "current":["temperature_2m",
                                    "rain",
                                    "relative_humidity_2m"] 
                                                    }
                responses = openmeteo.weather_api(url1, params=params)
                response = responses[0]
                #taking into account that we have a response of 200
                print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
                print(f"Elevation: {response.Elevation()} m asl")
                print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
                
                current = response.Current()
        
                current_temperature_2m = current.Variables(0).Value()
                current_rain = current.Variables(1).Value()
                current_relative_humidity_2m = current.Variables(2).Value()

                label1 = tk.Label(new_window, text=f"Current temperature of Thessaloniki: {current_temperature_2m:.1f}°C",height= 20,width= 40)
                label3 = tk.Label(new_window, text=f"Rain: {current_rain}",height= 20,width= 40)
                label4 = tk.Label(new_window, text=f"Relative Humidity: {current_relative_humidity_2m}",height= 20,width= 40)
                label1.pack()
                label3.pack()
                label4.pack()
                print(f"Current temperature_2m: {current_temperature_2m}")
                print(f"Current rain: {current_rain}")
                print(f"current_relative_humidity_2m{current_relative_humidity_2m}")
    
def patras():
               window.destroy()
               new_window = tk.Tk()
               new_window.title('WEATHER APP')
               new_window.geometry('1000x600')
               url1 = "https://api.open-meteo.com/v1/forecast"
               params = {
                "latitude": 38.2462,
                "longitude": 21.7351,
                "current": ["temperature_2m",
                                "rain",
                                "relative_humidity_2m" ]
                                                   }
               responses = openmeteo.weather_api(url1, params=params)
               response = responses[0]
               print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
               print(f"Elevation: {response.Elevation()} m asl")
               print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
       
               current = response.Current()
               current_temperature_2m = current.Variables(0).Value()
               current_rain = current.Variables(1).Value()
               current_relative_humidity_2m = current.Variables(2).Value()

               label1 = tk.Label(new_window, text=f"Current temperature of Patras: {current_temperature_2m:.1f}°C",height= 20,width= 40)
               label3 = tk.Label(new_window, text=f"Rain: {current_rain}",height= 20,width= 40)
               label4 = tk.Label(new_window, text=f"Relative Humidity: {current_relative_humidity_2m}",height= 20,width= 40)
               label1.pack()
               label3.pack()
               label4.pack()
               print(f"Current temperature_2m: {current_temperature_2m}")
               print(f"Current rain: {current_rain}")
               print(f"current_relative_humidity_2m{current_relative_humidity_2m}")
                   
    
#creates the buttons of the first window
button1 = tk.Button(window, text = 'Athens', command= athens,width= 20, height= 3)
button2 = tk.Button(window, text = 'Thessaloniki', command= thessaloniki,width= 20, height= 3)
button3 = tk.Button(window, text = 'Patra', command= patras,width= 20, height= 3)

button1.pack(pady = 50)
button2.pack(pady=50)
button3.pack(pady=50)


window.mainloop()
