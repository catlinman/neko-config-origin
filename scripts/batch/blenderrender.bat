
@ECHO OFF

:: The given paths need to be setup within this file before further execution.
SET SCENEPATH 	= "C:\[SCENE PATH]\[NAME].blend"
SET OUTPUTPATH 	= "C:\[OUTPUT PATH]"

SET /p BEGIN = "Enter the starting keyframe: "
SET /p END = "Enter the end keyframe: "

"C:\[INSTALL PATH]\blender.exe" -b %SCENEPATH% -x 1 -o %OUTPUTPATH% -s %BEGIN% -e %END% -a

ECHO The render was either cancelled or has finished.
PAUSE
