import openai
from tkinter import *
import customtkinter
import os
import pickle

# Genel Ayarlar

root = customtkinter.CTk()
root.title("ChatGpt Bot")
root.geometry('600x500')
# İcon Sayfası https://www.vecteezy.com/free-vector/ai-logo

root.iconbitmap("logo.png")

# Renklendirme Özellikleri dark/light

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Fonksiyonlar

def speak():
    if chat_entry.get():
        filename="api_key"
        try:

            if os.path.isfile(filename):
                input_file=open(filename,'rb')
                api_sifre=pickle.load(input_file)

                openai.api_key=api_sifre
                openai.Model.list()


                cevap=openai.Completion.create(
                    model="text-davinci-003",
                    prompt=chat_entry.get(),
                    temperature=0,
                    max_tokens=4000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
                my_text.insert(END,(cevap["choices"][0]["text"]).strip())
                my_text.insert(END,"\n\n")
            else:
                input_file=open(filename,'wb')
                input_file.close()
                my_text.insert(END, "\n\n API KEY Almayı Unuttun! Lütfen Aşağıdaki Buton'dan Temin et \n https://platform.openai.com/account/api-keys")
        except Exception as e:
            my_text.insert(END,f"\n Bir Hata oluştu: {e}")
    else:
        my_text.insert(END,"\\n Hey Dostum Soru Sormayı Unuttun")

def clear():
    my_text.delete(1.0, END)
    chat_entry.delete(0, END)
    
def key():
    filename="api_key"
    try:

        if os.path.isfile(filename):
            input_file=open(filename,'rb')
            api_sifre=pickle.load(input_file)
            api_entry.insert(END,api_sifre)
        else:
            input_file=open(filename,'wb')
            input_file.close()
        root.geometry('600x600')
        api_frame.pack(pady=10)
    except Exception as e:
        my_text.insert(END,f"\n Bir Hata oluştu: {e}")

def save_key():
    filename="api_key"
    try:
        output_file=open(filename,"wb")
        pickle.dump(api_entry.get(),output_file)
        api_entry.delete(0,END)
        api_frame.pack_forget()
    except Exception as e:
        my_text.insert(END,f"\n Bir Hata oluştu: {e}")
    root.geometry('600x500')
    
#Text Frame

text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)


my_text = Text(text_frame,bg="#343638",width=65,bd=1,relief="flat",wrap=WORD,selectbackground="#1f538d")
my_text.grid(row=0,column=0)

#ScrollBar

text_scroll = customtkinter.CTkScrollbar(text_frame,command=my_text.yview)
text_scroll.grid(row=0,column=1,sticky="ns")

my_text.configure(yscrollcommand=text_scroll.set)

# Entry

chat_entry = customtkinter.CTkEntry(root,
placeholder_text="Chat GPT''ye ne sormak istersin?",
    width=495,
    height=50,
    border_width=1)
chat_entry.pack(pady=10)

# Buton Frame

button_frame = customtkinter.CTkFrame(root, fg_color="#242424")

button_frame.pack(pady=10)

#Submit Button

submit_button = customtkinter.CTkButton(button_frame,
    text="ChatGpt'ye Sor",
    command=speak)

submit_button.grid(row=0,column=0,padx=20)

#Clear Button

clear_button = customtkinter.CTkButton(button_frame,
    text="Cevapları Temizle",
    command=clear)

clear_button.grid(row=0,column=1,padx=20)

#API KEY Button

apı_button = customtkinter.CTkButton(button_frame,
    text="API Key Güncelle",
    command=key)

apı_button.grid(row=0,column=2,padx=20)

#API Key Frame İ

api_frame = customtkinter.CTkFrame(root,border_width=1)
api_frame.pack(pady=10)

api_entry = customtkinter.CTkEntry(api_frame,placeholder_text="Yeni API Key Giriniz",width=300,height=50,border_width=1)

api_entry.grid(row=0,column=0, padx=20,pady=20)

api_save_button = customtkinter.CTkButton(api_frame,text="Key Kaydet",command=save_key)

api_save_button.grid(row=0,column=1,padx=10)


root.mainloop()