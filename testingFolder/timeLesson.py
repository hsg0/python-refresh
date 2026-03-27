from time import *

# print("Current time in seconds since the epoch:", time())

# stopGo = int(input("'1' to GO, '0' to STOP: "))

# while stopGo != 0:
#     print("Press '4' to Start, '6' to Stop.")
#     while True:
#         userInput = int(input("Enter '4' to Start, '6' to Stop: "))
#         if userInput == 4:
#             startTime = time()
#             print("Timer started at:", startTime)
#         elif userInput == 6:
#             stopTime = time()
#             print("Timer stopped at:", stopTime)
#             elapsedTime = stopTime - startTime
#             print("Elapsed time in seconds:", elapsedTime)
#             break
#         else:
#             print("Invalid input. Please enter '4' to Start or '6' to Stop.")
#     stopGo = int(input("'1' to GO, '0' to STOP: "))

# timer = int(input("Enter '1' to Begin, '0' to End: "))  
# while timer != 0:
#     print("Press '4' to Start, '6' to Stop.")
#     while True:
#         userInput = int(input("Enter '4' to Start, '6' to Stop: "))
#         if userInput == 4:
#             startTime = time()
#             print("Timer started at:", startTime)
#         elif userInput == 6:
#             stopTime = time()
#             print("Timer stopped at:", stopTime)
#             elapsedTime = stopTime - startTime
#             print("Elapsed time in seconds:", elapsedTime)
#             break
#         else:
#             print("Invalid input. Please enter '4' to Start or '6' to Stop.")
#     timer = int(input("Enter '1' to Begin, '0' to End: "))

# countDown = int(input("Enter a countdown time in seconds: "))
# while countDown > 0:
#     print("Time remaining:", countDown, "seconds")
#     sleep(1)
#     countDown -= 1
# print("Countdown complete!")

fileSize = int(input("Enter the file size in bytes: "))
downloadSpeed = int(input("Enter the download speed in bytes per second: "))
estimatedTime = fileSize / downloadSpeed
print("Estimated download time in seconds:", estimatedTime)
countDown = int(estimatedTime)
while countDown > 0:
    print("Time remaining:", countDown, "seconds")
    sleep(1)
    countDown -= 1
print("Download complete!")