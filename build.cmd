@echo off

pyinstaller startup_cli.py ^
--onefile ^
--log-level=DEBUG ^
--specpath=.\build\ ^
--name="PodcastDownloaderCLI" ^
--icon=.\icon\icon.ico
