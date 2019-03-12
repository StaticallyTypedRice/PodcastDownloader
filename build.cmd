@echo off

pyinstaller .\src\startup.py ^
--onefile ^
--noconsole ^
--log-level=DEBUG ^
--specpath=.\build\ ^
--name="PodcastDownloader" ^
--upx-dir=.\upx ^
--icon=.\src\icon\icon.ico

pyinstaller .\src\startup_cli.py ^
--onefile ^
--log-level=DEBUG ^
--specpath=.\build\ ^
--name="PodcastDownloaderCLI" ^
--upx-dir=.\upx ^
--icon=.\src\icon\icon.ico
