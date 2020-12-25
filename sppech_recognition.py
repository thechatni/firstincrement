import speech_recognition as sr
from time import sleep
loading = ['You are crossing a bridge on cold rainy night when suddenly a black Jeep pulls up beside you. Two guys get out from the car carrying a large bag on their shoulders. One man is wearing a red hoodie with a light green face mask covering his face. The other guy is wearing a white and black checkered shirt with a blue paterrned bandana on his face. They throw the bag over the bridge into the river below. Both of them quickly jump back into the Jeep and drive off. You watch the Jeep drive off, its number plate reads, DEF 1962. You look over the bridge to see what they threw. You are shocked to see a body floating in the water. Just as you are looking over, a Police car pulls up beside you.', '\n','The police found the dead body and are suspecting you to be the killer since you were the only one found around the crime scene. To prove your innocence, you must correctly answer the following questions by recalling details of the incident.']
for i in range(len(loading)):
    print(loading[i], flush=True); sleep(15)

r = sr.Recognizer()

story ="You are crossing a bridge on cold rainy night when suddenly a black Jeep pulls up beside you. Two guys get out from the car carrying a large bag on their shoulders. One man is wearing a red hoodie with a light green face mask covering his face. The other guy is wearing a white and black checkered shirt with a blue paterrned bandana on his face. They throw the bag over the bridge into the river below. Both of them quickly jump back into the Jeep and drive off. You watch the Jeep drive off, it's number plate reads, 'DEF 1962'. You look over the bridge to see what they threw. You are shocked to see a body floating in the water. Just as you are looking over, a Police car pulls up beside you."

preface ="The police found the dead body and are suspecting you to be the killer since you were the only one found around the crime scene. To prove your innocence, you must correctly answer the following questions by recalling details of the incident."

det_preface ="The interrogator asks: So, if you're not the culprit, then tell me about what really happened that night. "

correct = 0
wrong =0

q2 = "Describe the first guy's outfit."

q3 = "Describe the second guy's outfit."

q4 = "What was the number plate of the car?"

word1="Jeep"
word2="red"
word3="blue"
word4="1962"

print("\nInvestigator: What type of car were the two driving?")
with sr.Microphone() as source:
    print("Speak Now:")
    audio = r.listen(source)
    while True:
        try:
            text1 = r.recognize_google(audio) 
            print("You said : {}".format(text1))
            if word1 in text1: 
               print ('Okay')
               correct=correct+1
               sleep(1)
            else:
                print ('Hmm, not sure about that.')
                wrong=wrong+1
                sleep(1)
            break
        except:
            print("Sorry, couldn't get that")
            print("\nInvestigator: What type of car were the two driving?")
            with sr.Microphone() as source:
                print("Speak Now:")
                audio = r.listen(source)

            

print("\nInvestigator: Describe the first guy's outfit.")     
with sr.Microphone() as source:
    print("Speak Now:")
    audio = r.listen(source)
    while True:
        try:
            text2 = r.recognize_google(audio) 
            print("You said : {}".format(text2))
            if word2 in text2: 
               print ('Hmmm. Okay.')
               correct=correct+1
               sleep(1)
            else:
                print ('I see')
                wrong=wrong+1
                sleep(1)
            break
        except:
            print("Sorry, couldn't get that")
            print("\nInvestigator: Describe the first guy's outfit.")
            with sr.Microphone() as source:
                print("Speak Now:")
                audio = r.listen(source)
            

print("\nInvestigator: What color bandana was the second guy wearing.")     
with sr.Microphone() as source:
    print("Speak Now:")
    audio = r.listen(source)
    while True:
        try:
            text3 = r.recognize_google(audio) 
            print("You said : {}".format(text3))
            if word3 in text3: 
               print ('Okay. Got it.')
               correct=correct+1
               sleep(1)
            else:
                print ('Okay.')
                wrong=wrong+1
                sleep(1)
            break
        except:
            print("Sorry, couldn't get that")
            print("\nInvestigator: What color bandana was the second guy wearing.")
            with sr.Microphone() as source:
                print("Speak Now:")
                audio = r.listen(source)
        

print("\nInvestigator: What was the number plate of the car?")     
with sr.Microphone() as source:
    print("Speak Now:")
    audio = r.listen(source)
    while True:
        try:
            text4 = r.recognize_google(audio) 
            print("You: {}".format(text4))
            if word4 in text4: 
               print ('I see.')
               correct=correct+1
               sleep(1)
            else:
                print ('Hmm, interesting.')
                wrong=wrong+1
                sleep(1)
            break
        except:
            print("Sorry couldn't get that")
            print("\nInvestigator: What was the number plate of the car?")
            with sr.Microphone() as source:
                print("Speak Now:")
                audio = r.listen(source)

if (wrong>=2):
    print("I don't believe you are telling the truth. You are now a prime suspect!")
else:
    print("Yep, your answers check out. Sorry for disturbing you. You're free to go")
