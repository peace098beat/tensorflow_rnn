rem @echo off 
cd /d %~dp0 
setlocal enabledelayedexpansion

del /s initial.npy
del /s output.npy
del /s losses.npy
del /s *.png