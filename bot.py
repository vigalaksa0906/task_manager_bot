from features import run_bot
from database import create_table

if __name__ == '__main__':
    # Ensure the 'tasks' table exists before running the bot
    create_table()

    TOKEN = 'ENTER YOUR TOKEN HERE'
    run_bot(TOKEN)
