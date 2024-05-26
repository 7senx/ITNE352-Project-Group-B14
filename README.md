#  ITNE 352 Project

## Prepped by
- Mahmood Alaa (ID: 202107304)
- Husain Nabeel (ID: 202108591)

## Introduction

Within the ever-changing context of modern education at the University of Bahrain, the ITNE352 course is essential to developing proficiency with contemporary technology. A key project that falls under the purview of this course is the Multithreaded News Client/Server Information System, which stands out as a shining example of inventive teamwork and real-world application. Fundamentally, the goal of this project is to provide a smooth platform that will enable people to easily share and obtain breaking news updates with the highest level of efficiency and ease.

Starting this development path requires a multipronged strategy that incorporates several technical aspects like network connectivity, multithreading, APIs, and client/server architecture. By closely following industry best practices, students are not only taught how to code features but also gain a deep comprehension of the underlying rules that control reliable software development.

This thorough examination of the Multithreaded News Client/Server Information System includes insightful information about the nuances of client-side and server-side implementations. Through analyzing brief segments of code and clarifying their importance in the larger project context, students gain the ability to confidently and accurately negotiate the challenges of developing real-world applications.

In addition, an extensive synopsis of the project's goals, approaches, and expected results acts as a beacon of hope for budding technologists, providing a path to becoming proficient in modern software engineering paradigms. As a result, the Multithreaded News Client/Server Information System is evidence of the University of Bahrain's dedication to promoting innovation and quality in technology education, in addition to being an educational project.

## Project Description

This project's goal is to use Python scripts to create a client-server system. The server component is in charge of handling several client connections, replying to requests from clients, and utilizing the proper APIs to retrieve news updates from the NewsAPI.org service. The client script, on the other hand, establishes a connection with the server, opens a menu that is easy to use, queries the server, and shows the responses that the server returns.

### Client Code

The basis for a flexible client interface to communicate with a server-based news retrieval system is laid by a Python script. In the field of modern technology, where instantaneous information availability and seamless connectivity are critical, your script is the epitome of efficiency and pragmatism.

Fundamentally, the script makes use of the stability of the socket module in Python to enable smooth communication between the client and server objects. Users are able to navigate through a variety of alternatives, from searching headlines to exploring news sources, all contained within an easy user interface, thanks to a number of carefully designed functions and logical paths.

The script is noteworthy for adhering to structured data transmission; it uses JSON encoding to make information transfer between the client and server components easier. This establishes the foundation for scalability and interoperability across many technology ecosystems in addition to guaranteeing data integrity.

Moreover, the modular architecture of the script facilitates extensibility and ease of maintenance, enabling the smooth incorporation of new features and improvements in response to changing user needs and technology paradigms.

### Server Code

Our code looks like your code is configuring a server to accept connections from the outside world, respond to requests from clients, and communicate with an API interface to obtain data in response to requests from clients. Let's dissect the functions of each component:

1. **Server Setup (start_server function):**
   - Creates a socket, binds it to a specific IP address and port, and listens for incoming connections.
   - Once a client connects, it starts a new thread (client_handling) to handle that client's requests concurrently.
   
2. **Client Handling (client_handling function):**
   - Accepts a client socket and address as arguments.
   - Receives the client's name and acknowledges the connection.
   - Enters a loop to continuously receive messages from the client.
   - Parses the received message into option and criteria.
   - Depending on the option, it calls functions from API_interface to retrieve data (headlines or sources) based on the criteria.
   - Sends the response back to the client.
   - Catches any exceptions that occur during processing and closes the client socket.
   
3. **Response Handling (response function):**
   - Constructs the file path based on the client's name and the options provided.
   - Opens the corresponding JSON file and sends its contents back to the client.
   - This function is responsible for sending the requested data back to the client.
   
4. **Main Block:**
   - Starts the server when the script is executed.

### GUI Code

Our code looks like a solid foundation for a News Client application with a GUI built using Tkinter. Here's a summary of its functionalities and structure:

1. **Client Initialization:**
   - The NewsClientApp class initializes the client application window using Tkinter.
   - It establishes a connection to the server using a socket.
   
2. **Frame Navigation:**
   - The show_frame method allows switching between different frames (screens) within the application.
   - Each frame corresponds to a different section of the application, such as entering the user's name, the main menu, searching headlines, etc.
   
3. **User Interface:**
   - Frames such as EnterName, MainMenu, SearchHeadlines, ListSources, etc., are responsible for displaying specific sections of the user interface.
   - Buttons are used to trigger actions like submitting user input, navigating between frames, and initiating searches.
   
4. **Data Communication:**
   - Communication with the server is handled through the send and receive methods, which send messages to the server and receive responses.
   - Messages are encoded in a specific format (e.g., "1.1\n" for searching headlines by keyword) to convey the user's request to the server.
   
5. **Functionality:**
   - Users can perform various actions, including searching headlines by keyword, category, or country, listing all headlines, listing news sources, etc.
   - Each action triggers a specific request to the server, and the received data is displayed to the user.
   
6. **Displaying Data:**
   - Frames such as DisplayHeadlines and DisplaySources are responsible for presenting the received data (headlines or news sources) to the user in a readable format.
   - Message boxes are used to display detailed information about selected headlines or news sources.
   
7. **Error Handling:**
   - Basic error handling is implemented to handle cases such as empty user input and closing the client socket upon quitting the application.

## Additional Concepts

### JSON Code

Our code appears to be generally well-organized and structured. However, in order to handle any exceptions that might arise during API calls or file operations, you might want to think about including error handling. You might also include some logging to monitor the execution flow and any potential issues.

### Recommended Design Guidelines

The project description offers suggested design principles for putting the system in place. It recommends beginning with a basic Python server that has the ability to echo data and accept TCP connections. It then suggests putting the API integration into practice in order to get data from the internet source and extract the necessary information. Lastly, the standards suggest adding threads to the networking code to handle numerous connections.

## Acknowledgments

We would like to express our gratitude to Dr
