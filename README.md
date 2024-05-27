# Multithreaded News Client/Server Information System

## Project Description
The project aims to develop a Python-based client-server system for real-time news exchange. The server component handles multiple client connections and retrieves news updates from NewsAPI.org, while the client script provides a user-friendly interface for querying the server and displaying news content.

## Semester
Second 2024

## Group
- **Group Name:** B14
- **Course Code:** ITNE352
- **Section:** 2
- **Members:**
  - Mahmood Alaa (ID: 202107304)
  - Husain Nabeel (ID: 202108591)

## Table of Contents
1. [Requirements](#requirements)
2. [How to Run the System](#how-to-run-the-system)
3. [Scripts Description](#scripts-description)
4. [Additional Concepts](#additional-concepts)
5. [Acknowledgments](#acknowledgments)
6. [Conclusion](#conclusion)

## Requirements
- **Dependencies:** Python 3, Tkinter, newsapi-python
- **Installation:**
  - Install Python 3 from [python.org](https://www.python.org/)
  - Install required libraries:
  ```
    pip install newsapi-python
    pip install tkinter
  ```
## How to Run the System
### 1. Server Setup
1. Open a terminal window.
2. Navigate to the directory containing the server script.
3. Run the server script:
```
   python server.py
```
### 2. Client Setup
1. Open a new terminal window.
2. Navigate to the directory containing the client script.
3. Run the client script:
```
   python client.py
```
### 2. Client GUI setup (to run client with GUI)
1. Open a new terminal window
2. Navigate to the directory containing the clientgui script
3. Run the client script:
```
  python clientgui.py
```

## Scripts Description
### Server Script
- **Main Functionalities:** Handles client connections, interacts with NewsAPI, and serves news data to clients.
- **Utilized Packages:** socket, threading, json, requests, newsapi.NewsApiClient
- **Key Functions:** start_server, client_handling, response_handling

### Client Script
- **Main Functionalities:** Provides a GUI for user interaction, communicates with the server, and displays news content.
- **Utilized Packages:** socket, json, tkinter
- **Class:** NewsClientApp

## Additional Concepts
- **Error Handling:** Implemented on both server and client sides to manage exceptions and provide user feedback.
- **Multithreading:** Enables the server to handle multiple client connections concurrently.

## Acknowledgments
- We extend our gratitude to Dr. Mohammed Abdulaziz Almeer for his guidance and support.
- Special thanks to NewsAPI.org for providing valuable resources.

## Conclusion
- The Multithreaded News Client/Server Information System showcases proficiency in network programming, API integration, and user interface design, contributing to a practical understanding of modern software development principles.
