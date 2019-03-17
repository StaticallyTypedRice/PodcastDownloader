# Podcast Downloader

![Podcast Downloader Icon](./src/icon/icon.svg)

Podcast Downloader is a simple utility for automatically downloading all podcasts listed in a given RSS file. The program is writen in Python and can be ran as-is or built into standalone Windows, Mac or Linux executables.

## Usage

The startup files are in the `src` folder. Simply run one of the following commands (on either Windows, Mac or Linux).

For a graphical interface (**currently still in development**):

    cd src
    python3 startup.py

For a command line interface:

    cd src
    python3 startup_cli.py

No command line arguments are required.

You may need to install dependencies first:

    pip install -r requirements.txt

## Building

Podcast Downloader can be built using PyInstaller. First, install PyInstaller if you don't have it:

    pip install pyinstaller

Next, install the Python dependencies:

    pip install -r requirements.txt

On Linux, you may also need to install tkinter.

To build exectuables for Windows, run the `build.cmd` file.

For Mac or Linux, run the `build.sh` file.

The executables can be found in the `dist` folder.

Optionally, if you want to use UPX, download it from https://upx.github.io/ and extract it to the `upx` folder, such that the UPX executable is in the folder root.

You can also build the project manually using PyInstaller using whatever arguments you like:

    cd src
    pyinstaller startup.py
    pyinstaller startup_cli.py
