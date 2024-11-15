import discord
from discord.ext import commands
from discord import Intents
from database import add_task, delete_task, show_tasks, complete_task

intents = Intents.default()  # Set default intents
intents.message_content = True  # Ensure the bot can read message content

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='add_task')
async def add_task_command(ctx, *, description: str):
    """Add a new task"""
    add_task(description)
    await ctx.send(f"Task '{description}' has been added.")

@bot.command(name='delete_task')
async def delete_task_command(ctx, task_id: int):
    """Delete a task by its ID"""
    delete_task(task_id)
    await ctx.send(f"Task with ID {task_id} has been deleted.")

@bot.command(name='show_tasks')
async def show_tasks_command(ctx):
    """Show all tasks"""
    tasks = show_tasks()
    if tasks:
        task_list = "\n".join([f"{task[0]}. {task[1]} {'(Completed)' if task[2] else '(Not completed)'}" for task in tasks])
        await ctx.send(f"Task List:\n{task_list}")
    else:
        await ctx.send("There are no tasks currently.")

@bot.command(name='complete_task')
async def complete_task_command(ctx, task_id: int):
    """Mark a task as completed"""
    complete_task(task_id)
    await ctx.send(f"Task with ID {task_id} has been marked as completed.")

def run_bot(token):
    """Run the Discord bot"""
    bot.run(token)
