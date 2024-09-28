"""
    Student Name: Dan Shaw w0190983
    Program Name: Imperial to Metric Conversion
    Program Description: A console program that converts a weight given in imperial tons, stones, pounds and ounces to the metric equivalent in metric tons, kilograms and grams
"""

def main():
    # Output program title and greeting
    greeting = "IMPERIAL TO METRIC CONVERTER"
    print(greeting)
    print("-" * len(greeting))

    # Get the following values from the user: imperial tons, stone, pounds, ounces
    while (imperialTons := validateFloat(input("\tEnter the number of tons: "))) == None:
        pass

    while (stone := validateFloat(input("\tEnter the number of stone: "))) == None:
        pass

    while (pounds := validateFloat(input("\tEnter the number of pounds: "))) == None:
        pass

    while (ounces := validateFloat(input("\tEnter the number of ounces: "))) == None:
        pass

    # Perform imperial to metric calculations
    totalOunces = (35840 * imperialTons) + (224 * stone) + (16 * pounds) + ounces
    totalKilos = totalOunces / 35.274
    metricTons = int(totalKilos / 1000)
    remainderKilos = totalKilos % 1000
    remainderGrams = (remainderKilos - int(remainderKilos)) * 1000

    # Output results to user
    print("The metric weight is {0} metric tons, {1} kilos and {2:.1f} grams.".format(metricTons, int(remainderKilos), remainderGrams))

# Validates whether inputQuery is a valid number by trying to convert to a float
# Returns the converted float if successfull and None if fails
def validateFloat(inputQuery):
    try:
        return float(inputQuery)
    except:
        errorString = "Please enter a valid number"
        print("-" * len(errorString))
        print(errorString)
        print("-" * len(errorString))
        return None

if __name__ == "__main__":
    main() 