@echo off 
cd /d %~dp0 
setlocal enabledelayedexpansion

python ../lstm.py param.yaml

cd ..