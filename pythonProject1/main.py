import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import wolframalpha
import requests
import playsound
import os
from gtts import gTTS
import cv2
import random
import pyautogui
from bruteForce import *
import speedtest
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import os
import psutil
from volumeHandControl import *
from WhMessage import *

# Inizializiamo il microfono
r = sr.Recognizer()
mic = sr.Microphone(1)
print(mic.list_microphone_names())
#settiamo la lingua di wikipedia a italiano
wikipedia.set_lang('it')

# funzione che converte da testo a parlato
def speak(text):
    print(text)
    tts = gTTS(text=text, lang='it')

    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


# una volta riconosciuta la frase, elabora il comando

def parse_command(statement):
    if not statement:
        parse_command(take_command())

    print("Comando: " + statement)

    #comandi di presentazione:

    if "ciao" in statement or "presentati" in statement:
        speak('Ciao sono Jarvis!')

    elif "come va" in statement:
        speak("Io tutto bene tu?")
        risposta = take_command()
        if "non bene" in risposta or (not "bene" in risposta):
            speak("Oh mi dispiace, cosa è successo?")
            risposta = take_command()
            speak("Mi piacerebbe aiutarti ma sono solo un assistente vocale")
        else:
            speak("Mi fa piacere")

    elif "arrivederci" in statement or "spegniti" in statement or "stop" in statement:
        speak('è stato un piacere. Ciao.')
        exit()



    #comandi di ricerca e apertura:

    elif 'wikipedia' in statement:
        # Usiamo le API di wikipedia per trarre informazioni su una questione
        try:
            speak('Cerco su Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("Secondo Wikipedia")
            for s in results.split("."):
                speak(s)
        except:
            speak("Non ho capito")
            print("Non ho capitoooo!")

    elif 'cerca su google' in statement:
        statement = statement.replace("cerca su google", "")
        webbrowser.open_new("https://www.google.it/search?q=" + statement)
        speak('Cerco su google' + statement)
        time.sleep(5)

    elif 'cerca su youtube' in statement:
        statement = statement.replace("cerca su youtube", "")
        webbrowser.open_new("https://www.youtube.com/results?search_query=" + statement)
        speak('Cerco su youtube' + statement)
        time.sleep(5)


    elif 'apri youtube' in statement:
        webbrowser.open_new("https://www.youtube.com")
        speak("youtube è aperto")
        time.sleep(5)

    elif 'apri google' in statement:
        webbrowser.open_new("https://www.google.com")
        speak("Google chrome è aperto")
        time.sleep(5)

    elif 'apri gmail' in statement:
        webbrowser.open_new("https://www.gmail.com")
        speak("Gmail è aperto")
        time.sleep(5)

    elif 'apri spotify' in statement:
        webbrowser.open_new("https://open.spotify.com/")
        speak("Spotify è aperto")
        time.sleep(5)

    elif "meteo" in statement:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("Di quale città desideri il meteo")
        city_name = take_command()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        print("Cerco meteo in città: " + city_name)
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"] - 273.15
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" La temperature è di " +
                  str(f"{current_temperature:.2f}") + " \n gradi \n"
                                                      "\n La percentuale di  umidità è" +
                  str(current_humidiy))
        else:
            speak(" Città non trovata ")

    elif 'notizie' in statement:
        news = webbrowser.open_new("https://www.ilmattino.it")
        speak('Ecco le ultime notizie')
        time.sleep(6)




    #comandi di sistema

    elif 'ora' in statement:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sono le {strTime}")

    elif 'scatta una foto' in statement:
        cam = cv2.VideoCapture(0)
        img_counter = 0
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:

                print("Escape hit, closing...")
                break
            elif k % 256 == 32:

                img_name = "cattura{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

            if cv2.waitKey(1) & 0XFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()

    elif 'calcola' in statement:
        speak('Dimmi cosa ti devo calcolare')
        try:
            question = take_command()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        except:
            speak('Non ho capito')
            print("Non ho capitoooo!")





    #comandi di svago:

    elif 'raccontami una barzelletta' in statement:
        barzelletteDef = (  #barzellette di default
        "Dal medico. Dottore non capisco mia moglie è incinta le assicuro, sono stato attentissimo Com’è possibile??? Vede signore è come nel traffico, non basta stare attenti per sè occorre che lo siano anche gli altri",
        "Qual è il colmo per una disoccupata. Chiamarsi Assunta ",
        "Qual è il colmo per un eschimese. Prendere delle decisioni a caldo",
        "Qual è il colmo per un cosmonauta. Avere gli occhi fuori dalle orbite",
        "Qual è il colmo per un pompiere indeciso. Trovarsi tra due fuochi ")

        random_number = random.randint(0, 4)
        risposta = barzelletteDef[random_number]
        speak(risposta)

    elif 'posso raccontarti una barzelletta' in statement:
            speak("Certo, basta che sia divertente")
            barzelletta = take_command() #trovare un modo per salvarla
            speak("Molto divertente ma le mie sono meglio. Chiedimi di raccontarti una barzelletta")
            print()






    #funzionalità aggiuntive:

    elif 'bruteforce' in statement:
        speak("Immettere una password di max 6 caratteri")
        password = pyautogui.password("Inserisci un pin: ")
        start_time = time.time()
        pin = bruteforce(password)
        speak("Il tuo pin per caso è: "+str(pin)) #. Ci ho impiegato solo "+"--- %s secondi ---" % (time.time() - start_time))


    elif 'speed test' in statement:
        speak("Cosa vuoi che faccia? 1= Download 2= Upload 3= Ping.  Indicarne uno dei 3")
        option = take_command()
        st = speedtest.Speedtest()
        if "uno" in option:
            speak("Sto eseguendo il calcolo")
            vel = int(st.download())
            velmb = vel / 1000000
            print(velmb , "mb/s")

        elif "due" in option:
            speak("Sto eseguendo il calcolo")
            vel = int(st.download())
            velmb = vel / 1000000
            print(velmb , "mb/s")

        elif "tre" in option:
            speak("Sto eseguendo il calcolo")
            servernames = []
            st.get_servers(servernames)
            print(st.results.ping)
        else:
            print("Inserire un codice corretto")


    elif 'numero cellulare' in statement:
        speak("Inserire un numero di telefono con Country code")
        mobileNo = input("Inserire un numero di telefono con Country code")
        mobileNo = phonenumbers.parse(mobileNo)

        #timezone del numero
        print(timezone.time_zones_for_number(mobileNo))
        #carrier del numero
        print(carrier.name_for_number(mobileNo, "en"))
        #posizione del numero
        print(geocoder.description_for_number(mobileNo, "en"))
        #validazione del numero
        print("Numero di telefono valido: ",phonenumbers.is_valid_number(mobileNo))
        #se è possibile chiamarlo immagino
        print("Accertamento possibilità del numero: ", phonenumbers.is_possible_number(mobileNo))

    elif 'uso nucleo ' in statement: #nucleo sta per cpu ma il coglione del microfono non lo capisce
        speak("L'utilizzo della cpu è: ")
        load1,load5,load15 = psutil.getloadavg()

        cpu_usage = (load15/os.cpu_count()) * 100
        print(cpu_usage)

    elif 'controllo volume' in statement:
        volumeControl()

    elif 'manda messaggio' in statement:
        speak("Inserire le varie disposizioni richieste")
        numero = input("Inserire il numero di telefono a cui mandare il mess (con prefisso): ")
        mes = input("Inserire il messaggio da mandare")
        ora = input("Inserire l'ora a cui mandarlo")
        min = input("Inserire il minuto in cui mandarlo")
        message(numero,mes,ora,min)



    else:
        speak('Non ho capito')
        print("Non ho capito")

    parse_command(take_command())


# In ascolto per un comando vocale
def take_command():

    print("Ti ascolto")
    try:
        with mic as source:
            audio = r.listen(source)
        return r.recognize_google(audio, language="it-IT").lower()
    except Exception as e:
        print(e)


parse_command(take_command())



