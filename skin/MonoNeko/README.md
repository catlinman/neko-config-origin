
# MonoNeko MonoDevelop skin#

This is a syntax highlighting and interface theme for MonoDevelop. The GTK theme is formatted for Windows and might not work as intended on other operating systems. However, it should be fairly simple to change the interface themes on OSs other than Windows since mainly due to the fact that the Windows version of MonoDevelop does not contain a theme selection menu while the version for other operating systems does. Don't ask me what's up with that - I'm just sitting here skinning the Windows version. At the same time the Windows version of MonoDevelop has a horrible time getting along with custom GTK settings. This means that certain portions of the application remain white even when edited and so create a completely unreadable mess. At this point I have not found a good way to create a dark theme so I've simply modified the base theme to be a little more gray and less code-cluttered.

![](https://github.com/catlinman/nekoconfig/blob/master/screenshots/mononeko.png)

## Installation ##

To install the theme head over to your MonoDevelop installation folder and copy the *gtkrc.win32* file into your *bin* folder. I suggest you make a copy of the original just in case you wish to revert to the original.

To install the syntax highlighting scheme, open up MonoDevelop and navigate to *"Tools -> Options -> Text Editor .> Syntax Highlighting"*. There you will find a new menu where you can select the different syntax schemes. Add a new one by pressing the *Add* button and navigate to the *MonoNeko.xml*. From there you can select it in the context menu.