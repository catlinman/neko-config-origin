FOR /F "tokens=*" %%G IN ('dir /b *.flac') DO ffmpeg -i "%%G" -map_metadata 0 "%%~nG.wav"
