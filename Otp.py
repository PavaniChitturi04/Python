import random

# Generate a random 6-digit OTP
otp = random.randint(100000, 999999)

# Print the OTP
print("Your OTP is:", otp)

# Prompt the user to enter the OTP
user_otp = int(input("Enter the OTP you received: "))

# Compare the OTP entered by the user with the generated OTP
if user_otp == otp:

    print("OTP verification successful!")
else:
    print("OTP verification failed.")