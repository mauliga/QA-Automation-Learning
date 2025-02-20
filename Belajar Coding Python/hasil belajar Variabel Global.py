x = "Penyejuknate"

def myfunc():
    print("Mauliga " + x)

myfunc()

x = "Penyejuknate"
def myfunc():
    x = "nate"
    print ("Mauliga " + x)
myfunc()
print ("Mauliga " + x)

def myfunc():
    global x
    x = "Penyejuknate"

myfunc()
print ("Mauliga " +x)

x = "Penyejuknate"
def myfunc():
    global x
    x = "Nate"
myfunc()
print ("Mauliga " + x)

x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
    