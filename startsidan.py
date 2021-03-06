# -*- coding: utf-8 -*-
import tkinter
from getWeather import getWeather
from tkinter import messagebox
import webbrowser
import planLosning

class startsida:

    def __init__(self):
        pass
        self.weather = ''

        #self.nyplan = planLosning.plan()


    def sida(self):
        nyplan = planLosning.plan()
        top = tkinter.Tk()
        top.geometry("1920x1080")
        top.attributes('-fullscreen', True)
        vasttrafik1 = tkinter.PhotoImage(file="bilder//vasttrafik1.gif")
        ljus = tkinter.PhotoImage(file="bilder//lampa.gif")
        ljud = tkinter.PhotoImage(file="bilder//spotify.gif")
        smhi = tkinter.PhotoImage(file="bilder//smhi.gif")
        leaving = tkinter.PhotoImage(file="bilder//exit.gif")
        calendar = tkinter.PhotoImage(file="bilder//calendar.gif")
        settings = tkinter.PhotoImage(file="bilder//settings.gif")
        home = tkinter.PhotoImage(file="bilder//home.gif")
        #Event, fixa allt som händer
        def trafficCallBack():
            webbrowser.open_new('http://sebastiannilsson.com/vasttrafik-widget/next_trips/results?from=Smaragdgatan&to=Lantmilsgatan&max_results=4&weather_image=&no_refresh=0&no_refresh=1')


        def weatherCallBack():
            self.weather = getWeather()
            toplevel = tkinter.Toplevel()
            label1 = tkinter.Label(toplevel, text=self.weather, height=0, width=50)
            label1.pack()
            #webbrowser.open_new('http://www.wunderground.com/cgi-bin/findweather/getForecast?brand=wxmap&query=57.64436,11.89600&lat=57.64436&lon=11.89600&zoom=11&type=terrain&units=metric&rad=0&sat=0&svr=0&cams=0&tor=0&wxsn=1&wxsn.mode=temp&wxsn.opa=50&wxsn.bcdgtemp=0&wxsn.rf=0')

            #lägg in kalender
        def calendarCallBack():
            webbrowser.open_new('https://calendar.google.com/calendar/render?tab=wc#main_7%7Cweek')

            #Lägg till listan med ESP
        def lightCallBack():
            top.destroy()
            nyplan.plan()
                #send("Computer on")
                #messagebox.showinfo("Ljus", "Ljussidan")

            #Ljud öppna spotify och koppla till högtalare
        def soundCallBack():
            messagebox.showinfo( "Ljud", "Spotify")

            #Kommando för ett visst ljusschema
        def homeCallBack():
            messagebox.showinfo("Hemma", "Tänd hemma")

            #Kommando för att släcka aktivt ljus
        def leavingCallBack():
            messagebox.showinfo("Går", "Släck hemma")

            #Kom på inställningar
        def propertiesCallBack():
            quit()


            #Knapparna
        B1 = tkinter.Button( image = vasttrafik1,command = trafficCallBack)
        B2 = tkinter.Button( image = smhi, command = weatherCallBack)
        B3 = tkinter.Button( image = calendar, command = calendarCallBack)
        B4 = tkinter.Button( image = ljus, command = lightCallBack)
        B5 = tkinter.Button( image = ljud, command = soundCallBack)
        B6 = tkinter.Button( image = home, command = homeCallBack)
        B7 = tkinter.Button( image = leaving, command = leavingCallBack)
        B8 = tkinter.Button( image = settings, command = propertiesCallBack)

            #Placering knappar
        B1.place(x=0,y=0)
        B2.place(x=480,y=0)
        B3.place(x=960,y=0)
        B4.place(x=1440,y=0)
        B5.place(x=0,y=540)
        B6.place(x=480,y=540)
        B7.place(x=960,y=540)
        B8.place(x=1440,y=540)

        top.mainloop()
