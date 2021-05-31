import os

query = input("Give Shutdown Timer(TIP: Don't use characters and large numbers. It'll be dangerous): ")

print("Initiating Your Request!")

os.system(f"SHUTDOWN /S /F /T {query}")


