
@ECHO OFF

:: Setup the Windows WiFi virtual adapter. Requires administrator privileges.
SET /p HOTSPOTSSID = "Enter your hotspot's name: "
SET /p PASSWORD = "Enter your hotspot's login password: "
netsh wlan set hostednetwork mode=allow ssid=%HOTSPOTSSID% key=%PASSWORD% keyUsage=persistent
ECHO Don't forget to enable WiFi sharing on your main adapter and have it redirect to the new hotspot.
