# Discord Task Management Bot

This is a simple Discord bot that helps manage tasks within a small team. The bot allows users to:
- Add tasks
- Delete tasks
- Mark tasks as completed
- View a list of all tasks

The tasks are stored in a SQLite database, and the bot interacts with users through Discord commands.

## Features
- **`!add_task <description>`**: Adds a new task with a given description.
- **`!delete_task <task_id>`**: Deletes a task based on its ID.
- **`!show_tasks`**: Displays all tasks, showing whether they are completed or not.
- **`!complete_task <task_id>`**: Marks a task as completed.

## Requirements

Before running the bot, ensure you have Python 3.8 or higher installed. You also need to install the required dependencies. The bot uses the following libraries:

- `discord.py` - for interacting with the Discord API.
- `pytest` - for running unit tests.

## Installation

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running The Bot 
Once everything is set up, you can run the bot with the following command:
```bash
python bot.py
```
This will start the bot, and it will begin listening for commands in the Discord server where it has been invited.

## Testing
You can test the bot's functionality by running unit tests. The tests cover basic operations like adding, deleting, and completing tasks.

To run tests with `unittest`:
```bash
python -m unittest discover -s tests
```
