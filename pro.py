import tkinter as tk #for the UI
import openmeteo_requests   #imports the used API


openmeteo = openmeteo_requests.Client()

#builds the initial window
window = tk.Tk()                         
window.title("weather app")
window.geometry("1000x600")




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
	        "current": "temperature_2m",
                                            }
        responses = openmeteo.weather_api(url1, params=params)
        response = responses[0]
        print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation: {response.Elevation()} m asl")
        print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()
        label1 = tk.Label(new_window, text=f"Current temperature of Athens: {current_temperature_2m:.1f}°C",height= 20,width= 40)
        label1.pack()
        print(f"Current temperature_2m: {current_temperature_2m}")

        
      

    
def thessaloniki():
                window.destroy()   #closes the old window to open another
                new_window = tk.Tk()   #initialization of the new window
                new_window.title('WEATHER APP')
                new_window.geometry('1000x600')
                url1 = "https://api.open-meteo.com/v1/forecast"
                #taking into account that we have a response of 200
                params = {
                    "latitude": 37.9838,
                    "longitude": 23.7278,
                    "current": "temperature_2m",
                                                    }
                responses = openmeteo.weather_api(url1, params=params)
                response = responses[0]
                print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
                print(f"Elevation: {response.Elevation()} m asl")
                print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
        
                current = response.Current()
                current_temperature_2m = current.Variables(0).Value()
                label1 = tk.Label(new_window, text=f"Current temperature of Thessaloniki: {current_temperature_2m:.1f}°C",height= 20,width= 40)
                label1.pack()
                print(f"Current temperature_2m: {current_temperature_2m}")
    
def patras():
               window.destroy()
               new_window = tk.Tk()
               new_window.title('WEATHER APP')
               new_window.geometry('1000x600')
               url1 = "https://api.open-meteo.com/v1/forecast"
               params = {
                "latitude": 37.9838,
                "longitude": 23.7278,
                "current": "temperature_2m",
                                                   }
               responses = openmeteo.weather_api(url1, params=params)
               response = responses[0]
               print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
               print(f"Elevation: {response.Elevation()} m asl")
               print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
       
               current = response.Current()
               current_temperature_2m = current.Variables(0).Value()
               label1 = tk.Label(new_window, text=f"Current temperature of PATRAS: {current_temperature_2m:.1f}°C",height= 20,width= 40)
               label1.pack()
               print(f"Current temperature_2m: {current_temperature_2m}")
    
#creates the buttons of the first window
button1 = tk.Button(window, text = 'Athens', command= athens,width= 20, height= 3)
button2 = tk.Button(window, text = 'Thessaloniki', command= thessaloniki,width= 20, height= 3)
button3 = tk.Button(window, text = 'Patra', command= patras,width= 20, height= 3)

button1.pack(pady=20)
button2.pack(pady=50)
button3.pack(pady=50)


window.mainloop()