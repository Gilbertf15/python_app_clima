import requests

from tkinter import PhotoImage
import customtkinter as ctk

#ctk.set_appearance_mode('dark')
class Main_climate:

    def __init__(self, loop):
        self.loop = loop
        self.loop.title("App")
        self.loop.geometry("1000x1000")
        self.loop.resizable(False, False)
        self.label1 = ctk.CTkLabel(self.loop,text="Weather Forecast App", font=("Times New Roman", 15))
        self.label1.pack()
        
        self.bg = PhotoImage(file='img_climate/background.png')
        self.label_bg = ctk.CTkLabel(self.loop, text='',image=self.bg)
        self.label_bg.place(x=0, y=50)
        self.entry1 = ctk.CTkEntry(self.loop, placeholder_text='City_name,Us', font=('  Times New Roman', 10), width=200)
        self.entry1.place(x=400, y=200)
        self.butao1 = ctk.CTkButton(self.loop, text="Acessar", font=("Arial", 10), width=15, command=self.main_time)
        self.butao1.place(x=470, y=350)
        
    def main_time(self):
        try:
            global acess_main
            var1 = str(self.entry1.get())
            url = f"https://api.hgbrasil.com/weather?key=a99754ac&city_name={var1}"
        
            requests_acess = requests.get(url)  
            acess_main = requests_acess.json()

            #time = acess_main['results'] ['time']
            #temp = acess_main['results'] ['temp']
            #date = acess_main['results'] ['date']
            #description = acess_main['results'] ['description']
            #city = acess_main['results'] ['city']
            #forecast = acess_main['results'] ['forecast']

            currently = acess_main['results'] ['currently']
            condition = acess_main['results'] ['condition_slug']

            self.entry1.destroy()
            self.butao1.destroy()
            self.label_bg.destroy()

        except:
            self.label_erro = ctk.CTkLabel(self.loop, text='Erro, nome da cidade invalido ou erro de conexão', font=('Times New Roman', 15))
            self.label_erro.pack()
            
        
        if currently == 'dia':
            ctk.set_appearance_mode('light')
            match condition:
                case 'clear_day':
                    print('dia limpo')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/sol-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)    
                    label_nublado.place(x=220, y=60)
                    
                case 'storm' :
                    print('tempestade')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/chuva-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)
                    
                    
                case 'snow':
                    print('neve')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/neve-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)

                case 'hail':
                    print('granizo')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/neve-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)

                case 'cloudly_day':
                    print('nublado dia ')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/sol_nublado-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)
                    
                   

                case 'rain':
                    print('chuva')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/chuva-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)

                case 'cloud':
                    print('nublado di')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/sol_nublado-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None, image=imagem_p)
                    label_nublado.place(x=220, y=60)

                    
                case 'none_day':
                    label_nublado = ctk.CTkLabel(self.loop, text="erro ao obter clima do dia, tente depois", font=('Arial', 10))
                    label_nublado.pack()
                    print('erro ao obter')
           
    

        if currently == 'noite':
              ctk.set_appearance_mode('dark')
              match condition:
                case 'clear_night':
                    print('noite limpo')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/lua-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)

                case 'storm' :
                    print('tempestade')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/chuva-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)
                    
                case 'snow':
                    print('neve')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/neve-removebg-preview.png")      
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)

                case 'hail':
                    print('granizo')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/neve-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)

                case 'cloudly_night':
                    print('nublado noite ')
                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/lua_nublado-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)

                    
                case 'rain':
                    print('chuva')
                    imagem_p = PhotoImage(file="img_climate/chuva-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)

                case 'cloud':
                    print('nublado n')

                    self.acess_weather()
                    imagem_p = PhotoImage(file="img_climate/nublado-removebg-preview.png")
                    label_nublado = ctk.CTkLabel(self.loop, text=None,image=imagem_p)
                    label_nublado.place(x=220, y=60)
                    
                case 'none_night':
                    print('erro ao obter')
                    label_nublado = ctk.CTkLabel(self.loop, text="erro ao obter clima do noite, tente depois", font=('Arial', 10)) 
                    label_nublado.pack()

    def acess_weather(self):
        label_time =  ctk.CTkLabel(self.loop, text=f'Data Atual : {acess_main['results'] ['time']} : {acess_main['results'] ['date']} ', font=('Times NeW Roman', 10))
        label_time.place(x=15, y=5)

        label_weekday =  ctk.CTkLabel(self.loop, text=f'{acess_main['results']['forecast'][0]['weekday']}', font=('Arial', 15))
        label_weekday.place(x=600, y=100)


        label_temp =  ctk.CTkLabel(self.loop, text=f'{acess_main['results'] ['temp']} °C', font=('Arial', 25))
        label_temp.place(x=600, y=160)

        label_description =  ctk.CTkLabel(self.loop, text=f'{acess_main['results'] ['description']}', font=('Arial', 15))
        label_description.place(x=600, y=210)

        label_city =  ctk.CTkLabel(self.loop, text=f'{acess_main['results'] ['city']}', font=('Arial', 15))
        label_city.place(x=600, y=130)

        label_max =  ctk.CTkLabel(self.loop, text=f'Max: {acess_main['results']['forecast'][0]['max']} °C', font=('Arial', 15))
        label_max.place(x=600, y=245)

        label_min =  ctk.CTkLabel(self.loop, text=f'Min: {acess_main['results']['forecast'][0]['min']} °C', font=('Arial', 15))
        label_min.place(x=600, y=290)

        label_forecast1 =  ctk.CTkLabel(self.loop, text=f'{acess_main['results']['forecast'][1]['weekday']} | {acess_main['results']['forecast'][1]['description']} | Max: {acess_main['results']['forecast'][1]['max']}C° | Min: {acess_main['results']['forecast'][1]['min']}C°', font=('Arial', 20))
        label_forecast1.place(x=10, y=400)

        label_forecast2 =  ctk.CTkLabel(self.loop, text=f'{acess_main['results']['forecast'][2]['weekday']} | {acess_main['results']['forecast'][2]['description']} | Max: {acess_main['results']['forecast'][2]['max']}C° | Min: {acess_main['results']['forecast'][2]['min']}C°', font=('Arial', 20))
        label_forecast2.place(x=10, y=450)

        label_forecast3 =  ctk.CTkLabel(self.loop, text=f'{acess_main['results']['forecast'][3]['weekday']} | {acess_main['results']['forecast'][3]['description']} | Max: {acess_main['results']['forecast'][3]['max']}C° | Min: {acess_main['results']['forecast'][3]['min']}C°', font=('Arial', 20))
        label_forecast3.place(x=10, y=500)

        label_forecast4 =  ctk.CTkLabel(self.loop, text=f'{acess_main['results']['forecast'][4]['weekday']} | {acess_main['results']['forecast'][4]['description']} | Max: {acess_main['results']['forecast'][4]['max']}C° | Min: {acess_main['results']['forecast'][4]['min']}C°', font=('Arial', 20))
        label_forecast4.place(x=10, y=550)

        label_forecast5 =  ctk.CTkLabel(self.loop, text=f'{acess_main['results']['forecast'][5]['weekday']} | {acess_main['results']['forecast'][5]['description']} | Max: {acess_main['results']['forecast'][5]['max']}C° | Min: {acess_main['results']['forecast'][5]['min']}C°', font=('Arial', 20))
        label_forecast5.place(x=10, y=600)

        label_forecast2 =  ctk.CTkLabel(self.loop, text=f'{acess_main['results']['forecast'][6]['weekday']} | {acess_main['results']['forecast'][6]['description']} | Max: {acess_main['results']['forecast'][6]['max']}C° | Min: {acess_main['results']['forecast'][6]['min']}C°', font=('Arial', 20))
        label_forecast2.place(x=10, y=650)

if __name__ == '__main__':
    loop= ctk.CTk()
    app_obj = Main_climate(loop)
                
    loop.mainloop()

        

    

