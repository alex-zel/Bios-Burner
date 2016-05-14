@echo off

REM		Batch installer for "one-click bios"

start	/wait	xcopy	/Y	<YOUR_SHARE_PATH>	"C:\OneClick_Bios\"		/D /E /Q
reg	import "C:\OneClick_Bios\oneclickbios.reg"
