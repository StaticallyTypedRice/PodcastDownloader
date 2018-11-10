@echo off

pyinstaller .\src\startup.py ^
--onefile ^
--nosonsole ^
--log-level=DEBUG ^
--specpath=.\build\ ^
--name="PodcastDownloader" ^
--icon=.\src\icon\icon.ico

pyinstaller .\src\startup_cli.py ^
--onefile ^
--log-level=DEBUG ^
--specpath=.\build\ ^
--name="PodcastDownloaderCLI" ^
--icon=.\src\icon\icon.ico
