import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo,showerror

def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params = {
        'authorization':'P9UaZmC12tngWViqwBHsQOcKd6pvJFou54krTNXyjSl0Lh78MbJuywkNx8b79GOKhgpCzAcvVLD236S1',
        'sender_id':'TXTIND',
        'message': message,
        'language':'english',
        'route':'v3',
        'numbers':number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


#send_sms("9752543478","Chacha petty kha rahe ho")

def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    if r == True:
        showinfo("Send Success","Successfully Sent")
    else:
        showerror("Error", " Something went wrong")


# creating GUI
root = Tk()
root.title("Message Sender ")
root.geometry("400x500")
font = ("Helvetica", 22, "bold")

textNumber = Entry(root, font=font)
textNumber.pack(fill = X,pady = 20)

textMsg = Text(root)
textMsg.pack(fill = X)

sendBtn = Button(root, text = "Send SMS", command = btn_click )
sendBtn.pack()

root.mainloop()
