
devices = open("devices.txt", "a")
while True:
  newItem = input("Enter a device (exit if you finished): ")
  if newItem == "exit":
    print("All done!")
    break
  else:
    devices.write(newItem + "\n")
devices.close()
