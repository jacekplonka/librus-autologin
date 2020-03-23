@echo off

SET %minutes = %4% * 60

FOR /L %%X IN (1, 1, %3) DO (
    python3 source/login.py %1 %2
    timeout /t %minutes
)