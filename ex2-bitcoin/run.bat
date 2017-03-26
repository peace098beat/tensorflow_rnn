rem @echo off 
cd /d %~dp0 
setlocal enabledelayedexpansion

del /s initial.npy
del /s output.npy
del /s losses.npy
del /s *.png

cd /d %~dp0 
call .\lstm_basic/run.bat
cd /d %~dp0 
call .\lstm_batch50/run.bat
cd /d %~dp0 
call .\lstm_batch200/run.bat
cd /d %~dp0 
call .\lstm_epoch1000/run.bat
cd /d %~dp0 
call .\lstm_epoch3000/run.bat
cd /d %~dp0 
call .\lstm_forget0.25/run.bat
cd /d %~dp0 
call .\lstm_forget0.5/run.bat
cd /d %~dp0 
call .\lstm_learning0.02/run.bat
cd /d %~dp0 
call .\lstm_learning0.5/run.bat
cd /d %~dp0 
call .\lstm_seq30/run.bat
cd /d %~dp0 
call .\lstm_seq40/run.bat
cd /d %~dp0 
call .\lstm_seq60/run.bat
cd /d %~dp0 
call .\lstm_seq70/run.bat
cd /d %~dp0 
call .\lstm_hidden1/run.bat
cd /d %~dp0 
call .\lstm_hidden4/run.bat

rem start runipy output_batch.ipynb
rem start runipy output_epoch.ipynb
rem start runipy output_forget.ipynb
rem start runipy output_learning.ipynb
rem start runipy output_seq.ipynb
rem start runipy output_hidden.ipynb
