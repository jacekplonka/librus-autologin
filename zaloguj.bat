@echo off

SET /A minutes = %4 * 60

FOR /L %%X IN (0, 1, %3) DO (
    python source/login.py %1 %2
    timeout /t %minutes%
)
