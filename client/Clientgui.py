import socket
import json
import tkinter as tk
from tkinter import messagebox

SERVER_IP = "127.0.0.1"
SERVER_PORT = 6900
CATEGORIES = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
COUNTRIES = ["au", "nz", "ca", "ae", "sa", "gb", "us", "eg", "ma"]
LANGUAGES = ["ar", "en"]

class NewsClientApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("News Client")
        self.geometry("600x400")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_IP, SERVER_PORT))
        self.current_frame = None
        self.show_frame(EnterName)

    def show_frame(self, frame_class, *args):
        new_frame = frame_class(self, *args)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    def send(self, msg):
        self.client_socket.send(msg.encode())

    def receive(self):
        return self.client_socket.recv(100000).decode()

class EnterName(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Enter Your Name", font=("Helvetica", 18)).pack(pady=20)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        tk.Button(self, text="Submit", command=self.submit_name).pack(pady=10)

    def submit_name(self):
        name = self.entry.get()
        if name:
            self.master.send(name)
            self.master.show_frame(MainMenu)
        else:
            messagebox.showwarning("Input Error", "Name cannot be empty")

class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Main Menu", font=("Helvetica", 18)).pack(pady=20)

        tk.Button(self, text="Search Headlines", command=lambda: master.show_frame(SearchHeadlines)).pack(pady=10)
        tk.Button(self, text="List of Sources", command=lambda: master.show_frame(ListSources)).pack(pady=10)
        tk.Button(self, text="Quit", command=self.quit_program).pack(pady=10)

    def quit_program(self):
        self.master.client_socket.close()
        self.master.destroy()

class SearchHeadlines(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Search Headlines", font=("Helvetica", 18)).pack(pady=20)

        tk.Button(self, text="Search for Keywords", command=lambda: master.show_frame(SearchByKeywords)).pack(pady=10)
        tk.Button(self, text="Search by Category", command=lambda: master.show_frame(SearchByCategory)).pack(pady=10)
        tk.Button(self, text="Search by Country", command=lambda: master.show_frame(SearchByCountry)).pack(pady=10)
        tk.Button(self, text="List all New Headlines", command=self.list_all_headlines).pack(pady=10)
        tk.Button(self, text="Back to Main Menu", command=lambda: master.show_frame(MainMenu)).pack(pady=10)

    def list_all_headlines(self):
        self.master.send("1.4:null")
        headlines_data = self.master.receive()
        headlines_list = json.loads(headlines_data)
        self.master.show_frame(DisplayHeadlines, headlines_list)

class ListSources(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="List of Sources", font=("Helvetica", 18)).pack(pady=20)

        tk.Button(self, text="Search by Category", command=lambda: master.show_frame(SearchSourceByCategory)).pack(pady=10)
        tk.Button(self, text="Search by Country", command=lambda: master.show_frame(SearchSourceByCountry)).pack(pady=10)
        tk.Button(self, text="Search by Language", command=lambda: master.show_frame(SearchSourceByLanguage)).pack(pady=10)
        tk.Button(self, text="List all Sources", command=self.list_all_sources).pack(pady=10)
        tk.Button(self, text="Back to Main Menu", command=lambda: master.show_frame(MainMenu)).pack(pady=10)

    def list_all_sources(self):
        self.master.send("2.4:x")
        sources_data = self.master.receive()
        sources_list = json.loads(sources_data)
        self.master.show_frame(DisplaySources, sources_list)

class SearchByKeywords(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Search by Keywords", font=("Helvetica", 18)).pack(pady=20)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)
        
        tk.Button(self, text="Search", command=self.search).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: master.show_frame(SearchHeadlines)).pack(pady=10)

    def search(self):
        keyword = self.entry.get()
        msg = f"1.1:{keyword}"
        self.master.send(msg)
        headlines_data = self.master.receive()
        headlines_list = json.loads(headlines_data)
        self.master.show_frame(DisplayHeadlines, headlines_list)

class SearchByCategory(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Search by Category", font=("Helvetica", 18)).pack(pady=20)

        for category in CATEGORIES:
            tk.Button(self, text=category, command=lambda c=category: self.search(c)).pack(pady=5)

        tk.Button(self, text="Back", command=lambda: master.show_frame(SearchHeadlines)).pack(pady=10)

    def search(self, category):
        msg = f"1.2:{category}"
        self.master.send(msg)
        headlines_data = self.master.receive()
        headlines_list = json.loads(headlines_data)
        self.master.show_frame(DisplayHeadlines, headlines_list)

class SearchByCountry(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Search by Country", font=("Helvetica", 18)).pack(pady=20)

        for country in COUNTRIES:
            tk.Button(self, text=country, command=lambda c=country: self.search(c)).pack(pady=5)

        tk.Button(self, text="Back", command=lambda: master.show_frame(SearchHeadlines)).pack(pady=10)

    def search(self, country):
        msg = f"1.3:{country}"
        self.master.send(msg)
        headlines_data = self.master.receive()
        headlines_list = json.loads(headlines_data)
        self.master.show_frame(DisplayHeadlines, headlines_list)

class SearchSourceByCategory(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Search Source by Category", font=("Helvetica", 18)).pack(pady=20)

        for category in CATEGORIES:
            tk.Button(self, text=category, command=lambda c=category: self.search(c)).pack(pady=5)

        tk.Button(self, text="Back", command=lambda: master.show_frame(ListSources)).pack(pady=10)

    def search(self, category):
        msg = f"2.1:{category}"
        self.master.send(msg)
        sources_data = self.master.receive()
        sources_list = json.loads(sources_data)
        self.master.show_frame(DisplaySources, sources_list)

class SearchSourceByCountry(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Search Source by Country", font=("Helvetica", 18)).pack(pady=20)

        for country in COUNTRIES:
            tk.Button(self, text=country, command=lambda c=country: self.search(c)).pack(pady=5)

        tk.Button(self, text="Back", command=lambda: master.show_frame(ListSources)).pack(pady=10)

    def search(self, country):
        msg = f"2.2:{country}"
        self.master.send(msg)
        sources_data = self.master.receive()
        sources_list = json.loads(sources_data)
        self.master.show_frame(DisplaySources, sources_list)

class SearchSourceByLanguage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Search Source by Language", font=("Helvetica", 18)).pack(pady=20)

        for language in LANGUAGES:
            tk.Button(self, text=language, command=lambda l=language: self.search(l)).pack(pady=5)

        tk.Button(self, text="Back", command=lambda: master.show_frame(ListSources)).pack(pady=10)

    def search(self, language):
        msg = f"2.3:{language}"
        self.master.send(msg)
        sources_data = self.master.receive()
        sources_list = json.loads(sources_data)
        self.master.show_frame(DisplaySources, sources_list)

class DisplayHeadlines(tk.Frame):
    def __init__(self, master, headlines_list):
        super().__init__(master)
        tk.Label(self, text="Headlines", font=("Helvetica", 18)).pack(pady=20)

        for index, item in enumerate(headlines_list['articles']):
            tk.Button(self, text=f"{index + 1}. {item['title']}", command=lambda i=index: self.show_details(i, headlines_list)).pack(pady=5)

        tk.Button(self, text="Back", command=lambda: master.show_frame(SearchHeadlines)).pack(pady=10)

    def show_details(self, index, headlines_list):
        selected_headline = headlines_list['articles'][index]
        messagebox.showinfo("Article Details", f"Title: {selected_headline['title']}\n"
                                               f"Author: {selected_headline['author']}\n"
                                               f"Source: {selected_headline['source']['name']}\n"
                                               f"Description: {selected_headline['description']}\n"
                                               f"URL: {selected_headline['url']}\n"
                                               f"Published At: {selected_headline['publishedAt']}")

class DisplaySources(tk.Frame):
    def __init__(self, master, sources_list):
        super().__init__(master)
        tk.Label(self, text="Sources", font=("Helvetica", 18)).pack(pady=20)

        for index, item in enumerate(sources_list['sources']):
            tk.Button(self, text=f"{index + 1}. {item['name']}", command=lambda i=index: self.show_details(i, sources_list)).pack(pady=5)

        tk.Button(self, text="Back", command=lambda: master.show_frame(ListSources)).pack(pady=10)

    def show_details(self, index, sources_list):
        selected_source = sources_list['sources'][index]
        messagebox.showinfo("Source Details", f"Name: {selected_source['name']}\n"
                                              f"Country: {selected_source['country']}\n"
                                              f"Description: {selected_source['description']}\n"
                                              f"URL: {selected_source['url']}\n"
                                              f"Category: {selected_source['category']}\n"
                                              f"Language: {selected_source['language']}")

if __name__ == "__main__":
    app = NewsClientApp()
    app.mainloop()
