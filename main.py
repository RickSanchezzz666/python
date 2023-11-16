import tkinter as tk
import server
import client
import threading

root = tk.Tk()

root.geometry('800x600')
root.configure(bg='#343541')
root.title("Чат")

def get_message():
    message = messageInput.get()
    if(len(message) > 0):
        # client.send_message(message)
        print('Text:', message)
        messages_listbox.insert(tk.END, message)
        messageInput.delete(0, tk.END)
        messages_listbox.yview(tk.END)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

messages_listbox = tk.Listbox(root, bg='#343541', fg='white')
scrollbar = tk.Scrollbar(root, command=messages_listbox.yview)

messages_listbox.config(yscrollcommand=scrollbar.set)

messages_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

messages_listbox.insert(tk.END, 'Your messages: ')

messageLabel = tk.Label(root, text='Input your message!', bg='#343541', fg='white')
messageLabel.pack(pady=(10, 0))

messageInput = tk.Entry(root, width=40)
messageInput.pack(pady=10)

sendButton = tk.Button(root, text='Send Message', command=get_message)
sendButton.pack()

# def start():
#     server.start_server()

def start_server():
    # server_thread = threading.Thread(target=start)
    # server_thread.start()
    root.mainloop()

start_server()