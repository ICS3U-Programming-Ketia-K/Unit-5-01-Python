# !/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 18, 2022
# This program calls function to convert the temperature
# from Celsius to Fahrenheit.

def fahrenheit():

    # get user temperature as string from the user
    temp_celsius = input("Enter temperature(°C): ")
    try:

        # convert user temperature from string to float
        temp_celsius_float = float(temp_celsius)
        # calculate the temperature from Celsius to Fahrenheit
        temp_fahrenheit = (9.0/5.0)*temp_celsius_float + 32
        # Display the temperature in Fahrenheit
        print("{}°C is equal to {:.1f}°F "
              .format(temp_celsius_float, temp_fahrenheit))
    except Exception:

        print("{} is not an integer.".format(temp_celsius))


def main():

    # This function calls other functions
    # call function
    fahrenheit()


if __name__ == "__main__":
    main()
