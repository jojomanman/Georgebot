# Georgebot

Georgebot is a versatile Telegram bot designed to facilitate various interactions, from echoing messages to executing Python scripts and handling location sharing. It provides a foundational platform for extending its capabilities with advanced features like AI integration.

### Features
-   `/start` command: Initiates interaction and sends a welcome message to the user.
-   Text Message Echo: The bot echoes back any text message it receives, demonstrating basic message handling.
-   `/run_script <script_name.py>`: Executes Python scripts located in the `scripts/` directory. For example, `/run_script sample.py` will run the `sample.py` script.
-   `/share_location`: Prompts the user to share their location. Once shared, the bot echoes back the received location data.

### Getting Started

To set up and run Georgebot, follow these steps:

**Prerequisites**:
-   Python 3.x
-   pip

**Installation**:
1.  **Clone the repository**: If you haven't already, clone the Georgebot repository to your local machine.
    ```bash
    git clone https://github.com/your-username/georgebot.git
    cd georgebot
    ```
    (Replace `https://github.com/your-username/georgebot.git` with the actual repository URL if available, or remove this step if not applicable for a new user starting from a provided codebase.)
2.  **Navigate to the project root**: Ensure you are in the main `georgebot` directory.
3.  **Create a `.env` file**: In the project root, create a file named `.env` and add your Telegram bot token:
    ```
    BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    ```
    Replace `YOUR_TELEGRAM_BOT_TOKEN` with the actual token obtained from BotFather on Telegram.
    
    **Important**: Make sure to add `.env` to your `.gitignore` file to prevent sensitive information from being committed to version control.
4.  **Install dependencies**: Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Bot

To start the bot, execute the `bot.py` script:
```bash
python bot.py
```
Expected output will include messages indicating successful database connection and that the application has started polling for updates, similar to:
```
Database connected successfully.
Application started, polling for updates...
```

### Database

Georgebot uses SQLite for data storage. The database file, `bot_database.db`, is created in the project root. It contains the following tables:
-   `messages`: Stores user messages and the bot's corresponding responses.
-   `locations`: Stores data related to shared user locations.

### Extensibility

The bot's message handling logic, particularly the echo functionality, is implemented in [`handlers/messages.py`](handlers/messages.py). This file is a key point for integration with Artificial Intelligence (AI) models. You can replace the current echo logic with calls to a Large Language Model (LLM) API or other AI services to enable more sophisticated conversational capabilities.

### Future Enhancements (Optional)

Potential future improvements based on user feedback and advanced features could include:
-   **Automatic Location Sharing**: Implementing a mechanism for the bot to automatically request and receive location updates.
-   **Command Autocomplete**: Providing autocomplete suggestions for bot commands to enhance user experience.

These enhancements are not currently implemented but represent areas for future development.