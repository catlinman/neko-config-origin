
@ECHO OFF

:: Run this if you don't want to get nagged to upgrade to Windows 10 all the time.
:: The script gets the pid of GWX.exe and kills it. Not much more to say really.
FOR /F "TOKENS=1,2,*" %%a IN ('tasklist /FI "IMAGENAME eq GWX.exe"') DO (
  SET GWXPID=%%b
  )

ECHO Killing GWX Process (PID: %GWXPID%) ...
TASKKILL /PID %GWXPID% /T /F
