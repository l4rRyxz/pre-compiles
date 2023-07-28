function LDAPSearch {
    param (
        [string]$LDAPQuery
    )

    $PDC = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain().PdcRoleOwner.Name
    $DistinguishedName = ([adsi]'').distinguishedName

    $DirectoryEntry = New-Object System.DirectoryServices.DirectoryEntry("LDAP://$PDC/$DistinguishedName")

    $DirectorySearcher = New-Object System.DirectoryServices.DirectorySearcher($DirectoryEntry, $LDAPQuery)

    return $DirectorySearcher.FindAll()

}

####
#### Usage:
####

# PS> Import-Module .\ad_enumeration.ps1
#
# PS> LDAPSearch -LDAPQuery "(samAccountType=805306368)"
#
# PS> LDAPSearch -LDAPQuery "(objectclass=group)"
#
#
# > foreach ($group in $(LDAPSearch -LDAPQuery "(objectCategory=group)")) {
# >> $group.properties | select {$_.cn}, {$_.member}
# >> }
