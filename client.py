import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

#if server is online so provide public ip add here
host='127.0.0.1'
port=9000

#clients will be objects
class client:
    def __init__(self, host, port):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,port))

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring("Nickname", "please choose a nickname", parent=msg)

        self.gui_done = False

        self.running = True
        #thread runs and maintains the gui
        gui_thread = threading.Thread(target=self.gui_loop)
        #thread deals with the server connection
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        #chat label
        self.win = tkinter.Tk()
        self.win.configure(bg="lightblue")

        #box with previous chat
        self.chat_label = tkinter.Label(self.win, text="Chat: ", bg="lightblue")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        #text box to enter chat
        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.win, text="Message: ", bg="lightblue")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)


        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done=True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    def write(self):
        message=f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0','end')
        #get message from message box and send it to the server then clear message box

    def stop(self):
        self.running=False
        self.win.destroy()
        self.sock.close()
        exit(0)
    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("error")
                self.sock.close()
                break

client = client(host, port)
