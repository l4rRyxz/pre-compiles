# Collection of pre-compiled binaries for different situations.


- #### [BackupOperatorToDA](https://github.com/l4rRyxz/pre-compiles/blob/main/windows/BackupOperatorToDA.exe)
A tool to abuse the privileges of the group "Backup Operator". Let's you copy SAM, SYSTEM, SECURITY for local extraction.

- #### [Mimikatz v.2.1.1](https://github.com/l4rRyxz/pre-compiles/blob/main/windows/mimikatz_2.1.1.exe)
Mimikatz compiled in 2.1.1 instead of 2.2.0, which avoids some already encountered issues.

- #### [PrintSpoofer64](https://github.com/l4rRyxz/pre-compiles/blob/main/windows/PrintSpoofer64.exe)
From LOCAL/NETWORK SERVICE to SYSTEM by abusing `SeImpersonatePrivilege` on Windows 10 and Server 2016/2019.

- #### [JuicyPotato](https://github.com/l4rRyxz/pre-compiles/blob/main/windows/JuicyPotato/)
A sugared version of RottenPotatoNG, with a bit of juice, i.e. another Local Privilege Escalation tool, from a Windows Service Accounts to NT AUTHORITY\SYSTEM
The folder also contains a script `GetCLSID.ps1` this may be necessary to gather working CLSID's for the exploitation.
!!! -> JuicyPotato doesn't work on Windows Server 2019 and Windows 10 build 1809 onwards.

- #### [SweetPotato](https://github.com/l4rRyxz/pre-compiles/blob/main/windows/SweetPotato.exe)
	- Works on Windows 7 up to the latest version of Windows 10 and Server 2019
	- Compatible with execute-assembly from Cobalt Strike an other C2 projects that support in memory execution of .NET executables
	- Works on 32 bit and 64 bit operating systems.
	- Can be compiled for for .NET 2 and 4 depending on target OS.
	- Automatically attempts the correct exploit to execute.

- #### [RoguePotato]()
