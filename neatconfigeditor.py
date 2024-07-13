import os
import asyncio
import subprocess

PYTHON_INTERPRETER = os.path.join(os.getcwd(), 'venv', 'Scripts', 'python.exe')


async def start_flask_server():
    subprocess.Popen([PYTHON_INTERPRETER, 'app.py'])


async def open_browser():
    await asyncio.sleep(2)
    url = 'http://127.0.0.1:5000/NEAT-Config-Editor/'
    if os.name == 'nt':  # Windows
        os.system(f'start {url}')
    elif os.name == 'posix':  # Linux or macOS
        subprocess.Popen(['xdg-open', url])


async def main():
    task1 = asyncio.create_task(start_flask_server())
    task2 = asyncio.create_task(open_browser())

    await asyncio.gather(task1, task2)


asyncio.run(main())
