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
