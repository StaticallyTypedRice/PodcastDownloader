@echo off

pyinstaller startup.py ^
--onefile ^
--log-level=DEBUG ^
--specpath=.\build\ ^
--name="PodcastDownloader" ^
--icon=.\icon\icon.ico

pyinstaller startup_cli.py ^
--onefile ^
--log-level=DEBUG ^
--specpath=.\build\ ^
--name="PodcastDownloaderCLI" ^
--icon=.\icon\icon.ico
