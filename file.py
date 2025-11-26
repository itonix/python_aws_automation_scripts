# input_file = r'D:\python\TextFiles\country_info.txt'  # Use raw string for Windows paths

# fullcountry_dict = {}

# with open(input_file, "r") as countryfile:
#     countryfile.readline()   # Skip header
#     for line in countryfile:
#         country, capital, cc, cc3, IAC, TimeZone, currency = line.strip().split('|')

#         count_dict = {
#             "country_name": country,
#             "capital": capital,
#             "cc": cc,
#             "cc3": cc3,
#             "IAC": IAC,
#             "TimeZone": TimeZone,
#             "currency": currency
#         }

#         # Use lowercase to make lookup case-insensitive
#         fullcountry_dict[country.lower()] = count_dict

# checkcountry = input("Enter the country for details: ").lower()

# if checkcountry in fullcountry_dict:
#     print(fullcountry_dict[checkcountry])
# else:
#     print("Enter a valid country")

   