@echo off

pyinstaller podcast_downloader.py ^
--onefile ^
--log-level=DEBUG ^
--specpath=.\build\ ^
--name="PodcastDownloader" ^
--icon=.\icon\icon.ico
