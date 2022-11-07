# Python exercises

## Windows
### Change Powershell execution policy

Demo of setting up the Execution Policy.
https://youtu.be/R11kUjafVEo?list=PLtgJR0xD2TPdBfg5oIKseNuN0tX_DgPkH&t=1738

Open a Powershell window as administrator and type the following:
```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```
Then respond y to any questions.

You need to use create virtual environment as you should not corrupt your Python in Windows.
```
python -m venv .venv
.venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

## macOS

Follow the above demo of Windows version, but you don't need to open Powershell to type that Execution Policy command. The same thing you have to do is to create virtual environment as you should not corrupt your Python in macOS. The code will be a bit different.
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Codespace
It is fine to use the Linus Python interpreter directly, as you can delete Codepace and create new one if there is any problem easily.
```
pip install -r requirements.txt
```

![Open in Codespaces](https://classroom.github.com/assets/open-in-codespaces-abfff4d4e15f9e1bd8274d9a39a0befe03a0632bb0f153d0ec72ff541cedbe34.svg)
