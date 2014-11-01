@echo off

REM Put out tips

:restart
cls
color 3f
@echo ===================================================
@echo =          vscleanerV0.1 				   			=
@echo =   vs studio temporary file remover     			=
@echo =                                        			=
@echo =    mail : yokyo.young@gmail.com       	 		=
@echo =    site : https://github.com/yokyo/vscleaner 	=
@echo ===================================================
@echo/
@echo.
@echo 1,Remove 'Debug' directories
@echo 2,Remove 'Release' directories
@echo 3,Remove all temporary files
@echo 4,quit
@echo/

REM Define sorts of temporary file type
set temp_files=(*.ncb *.pch *.plg *.obj *.opt *.pdb *.exp *.sbr *.ilk *.bsc *.idb *.res *.aps *.manifest .lastbuildstate *.cache *.dep *.sdf *.filters *.log *.tlog *.user *_i.c *_p.c *.tlb *.tlh )

REM Make choice
choice /c 1234 /m "what do you want to do ?(1,2,3,4)" /n
if errorlevel 4 call :remove_quit
if errorlevel 3 call :remove_temp_files
if errorlevel 2 call :remove_folder Release
if errorlevel 1 call :remove_folder Debug

@echo/
@echo/
@echo/
@echo done.
pause>nul
goto restart
call :restart

REM Function @ delete temporary files 
:remove_temp_files
for /R %%i in %temp_files% do (
	del /f /q %%i>nul 2>nul
)
REM remove ipch directory
call :remove_folder ipch
exit /b 0

REM function
REM @param :folder to be removed
:remove_folder
for /R %%i in (.) do (
 if exist %%i\%1 rd /q /s %%i\%1>nul 2>nul
)
exit /b 0

:remove_quit
exit 0