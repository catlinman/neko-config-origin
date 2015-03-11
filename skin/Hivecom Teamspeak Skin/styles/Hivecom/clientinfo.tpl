<!--
Predefined values have to be inside the html comment-tag to make sure that they will be parsed
before the replacing begins! Remove the "#" to enable.

#%%CLIENT_SERVER_SHOW_MAX_GROUPS%%5
-->

<style type="text/css">
@import url('Styles/Hivecom/style.css');
</style>
   
<tr><td>&nbsp;</td></tr>
            
<table id="header">
	<tr><td class="header"><span></span>%%?CLIENT_NAME%% <img src="%%?CLIENT_COUNTRY_IMAGE%%" alt="" title="%%CLIENT_COUNTRY_TOOLTIP%%"/></td></tr>
	<tr><td class="headersub"><span></span>%%?CLIENT_CUSTOM_NICK_NAME%%</td></tr>
</table>
</table>

<table id="container">
	<td><table id="info">    
		<tr><td class="user"><table>
			<tr><td class="infoheader"><span class="red">CLIENT INFO</span> </td></tr> 
			<tr><td class="infotext">Away Message:</td><td class="infotext">%%?CLIENT_AWAY_MESSAGE%%</td></tr>
			<tr><td class="infotext">Description:</td><td class="infotext">%%?CLIENT_DESCRIPTION%%</td></tr>
			<tr><td class="infotext">Total Connections:</td><td class="infotext">%%CLIENT_TOTALCONNECTIONS%%</td></tr>
			<tr><td class="infotext">Online since:</td><td class="infotext">%%CLIENT_CONNECTED_SINCE%%</td></tr> 	
			<tr><td class="infotext">Version:</td><td class="infotext">%%CLIENT_VERSION_SHORT%% %%CLIENT_VERSION_STATE%% on %%CLIENT_PLATFORM%%</td></tr>
			<tr><td class="infotext">Client / Database ID:</td><td class="infotext">%%CLIENT_ID%%&nbsp;/&nbsp;%%CLIENT_DATABASE_ID%%</td></tr>
			<tr><td class="infotext">Unique ID:</td><td class="infotext">%%CLIENT_UNIQUE_ID%%</td></tr>
			<tr><td class="infotext">Volume Modifier:</td><td class="infotext">%%?CLIENT_VOLUME_MODIFIER%% dB</td></tr>
		</table></td></tr>
		<tr><td>&nbsp;</td></tr>
		<tr><td class="scanner"><table><tr><td class="infoheader">RUNNING APPLICATIONS</td><tr><td class="infotext">%%?CLIENT_META_DATA%%</td></tr></table></td></tr>
		<tr><td class="scanner"><tr><td class="infotext"><br />*** Client requested talk power at: <b>%%?CLIENT_TALK_REQUEST_TIME%%</b></td></tr><tr><td class="infotext">&nbsp;&nbsp;&nbsp;&nbsp;[ %%?CLIENT_TALK_REQUEST_MSG%% ]</td></tr></table></td></tr>        
	</table></td>
    
	<tr><td class="server"><table>
		<tr><td class="infoheader">SERVER GROUPS</td> </tr>
		<tr><td class="grouptext">%%CLIENT_SERVER_GROUP_NAME%%</td></tr>
		<tr><td class="infoheader">CHANNEL GROUPS</td></tr>
		<tr><td class="grouptext">%%CLIENT_CHANNEL_GROUP_NAME%%</td></tr>
		<tr><td>&nbsp;</td></tr>
		<tr><td class="infoheader">AVATAR</td> </tr>
	</table></td></tr>      
</table>
