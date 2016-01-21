
@ECHO OFF

:: This program tracks it's execution folder's WAV files and converts them to FLAC
:: Requires the FLAC binary to be within the the scripts execution folder.

IF NOT EXIST "flac.exe" (
  ECHO Please make sure that the flac binary is included in this script's folder.
  PAUSE
  GOTO End
  )

ECHO Starting tracker. Files will only be encoded if there is no FLAC equivalent.
ECHO Use Ctrl-C to stop the execution of this script.

:Loop
FOR /r %%i IN (*) DO (
  IF "%%~xi%" == ".wav" (
    IF NOT EXIST "%%~ni%.flac" (
      ECHO.
      ECHO Found uncoverted file %%~ni%. Starting conversion..
      flac.exe -s "%%i%" > NUL
      ECHO Conversion completed.
      )
    )
  )

ECHO.
ECHO Sleeping for 30 seconds...
timeout /t 30 /nobreak > NUL

GOTO Loop

:End
