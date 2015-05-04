
# Fetch the parameters. If they are not supplied, ask the user to enter them. We make sure that Get-Date does not receive extra quotes.

# Keep in mind that the formatting of the DateTime can vary. The date needs to be listed but the actual time is optional and can be formatted
# in different ways. Example: 04/20/1999 13:42:32 or 11/27/1996 6PM. Datetime also for some reason wants the American date format when constructing
# from a parameter but asks for the user's system date format when it receive the date via Get-Date. Not sure what's up with that.

Param(
	[string]$path = $(Read-Host "Enter the path to the file you'd like to edit").Replace("`"",""),
	[Datetime]$date = $(Get-Date((Read-Host "Enter the date you'd like to apply [Format: MM/DD/YYYY HH:MM:SS AM/PM]").Replace("`"",""))),
	[string]$entry = $(Read-Host "Which entry do you want to edit [create, edit, access, all]").Replace("`"","")
)

# Check if the path is valid.
If(Test-Path($path.Replace("`"",""))) {
	# Make sure that one of our options was actually selected. If valid, apply the selected date to the given file's entry.
	If(($entry -eq "create") -or ($entry -eq "edit") -or ($entry -eq "access") -or ($entry -eq "all")){
		If($entry -eq "create") {
			$(Get-Item($path)).creationtime=$($date)

		} ElseIf($entry -eq "edit") {
			$(Get-Item($path)).lastwritetime=$($date)

		} ElseIf($entry -eq "access") {
			$(Get-Item($path)).lastaccesstime=$($date)

		} ElseIf($entry -eq "all") {
			$(Get-Item($path)).creationtime=$($date)
			$(Get-Item($path)).lastwritetime=$($date)
			$(Get-Item($path)).lastaccesstime=$($date)
		}
	} Else {
		throw "The supplied entry string ($($entry)) is not valid. It must be one of the following: create, edit, access, all"
	}
} Else {
	throw "The path ($($path)) supplied is not valid."
}