# Hackville 2024 Project
Team: [Daniel](https://github.com/danomar13), [Dean](https://github.com/DeanGhassemi), [David](https://github.com/DavidHTwastaken), [Anreet](https://github.com/anreetka)

Our submission for Hackville 2024 is a web application that helps people who are new to flirting by providing lessons and a chatbot for practice.

Click here to [check out the website](https://flirtlearn.co)!

## Installing and Using Locally
The deployed application currently doesn't work properly (we only had 36 hours to be fair 😆).

If you want to check it out locally, just clone this repository and follow the instructions.

### Requirements
* [Python 3.11.5]([url](https://www.python.org/downloads/))
* [MongoDB]([url](https://www.mongodb.com/docs/manual/administration/install-community/))
* [npm]([url](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm))
* Ports 5713 and 5000

### Frontend
The frontend and backend are run separately, using two different terminals.

For the frontend, open a terminal in the ```frontend/hackathon2024/``` directory. Use the command ```npm run dev```.

Open your browser and go to ```http://localhost:5713```.

Website is now running locally!

### Backend
In order for the chat bot and login systems to work, you need to start the backend.

Open a terminal in the ```backend/``` directory. Use the command ```python -m pip install -r requirements``` to install the necessary packages. Then run ```python -m flask --app main run``` to start the Flask server (should start running on port 5000).

### Environment
You will also need to add a ```.env``` file in the ```backend/``` directory for the environment variables.
Each of the following values need to be in the ```.env``` file:
* In order to use the chat bot, you'll need an [OpenAI API key]([url](https://openai.com/product)). Write it in the file like ```OPENAI_API_KEY=<your key>```.
* Make sure that MongoDB is running on your computer and make note of the port it's running on (probably 21017). Write the URL in the file like ```MONGO_URI="mongodb://localhost:<your port>/hackville2024"```.
* Make a string containing 32 characters for the JWT secret key. Write it in the file like ```JWT_SECRET_KEY=<your key>```.

Now you're ready to try out the demo!
