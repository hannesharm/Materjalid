"""
Given a csv file of city names and their state codes,
script must be able to write 2 new files based on the given file:
    first file: first column is the code, second column is the number of cities with that code;
    second file: first column is the city name, second column is the number of letters in that city name.

input file exaple:
    Youngstown, OH
    Wilmington, NC
    Waterloo, IA
    Victoria, TX
    Tyler, TX
    Texarkana, TX
    Springfield, OH
    Sioux City, IA
    Schenectady, NY
    Santa Barbara, CA
    Ravenna, OH

first file exaple:
    OH, 3
    NC, 1
    IA, 2
    TX, 3
    NY, 1
    CA, 1

second file example:
    Youngstown, 10
    Wilmington, 10
    Waterloo, 8
    Victoria, 8
    Tyler, 5
    Texarkana, 9
    Springfield, 11
    Sioux City, 10
    Schenectady, 11
    Santa Barbara, 13
    Ravenna, 7
"""