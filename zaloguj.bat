@echo off

SET /A %seconds=60
SET /A %minutes=%4%*%seconds%

FOR /L %%X IN (0, 1, %3) DO (
    python source/login.py %1 %2
    timeout /t %minutes
)
