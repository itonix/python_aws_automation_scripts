data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]


file_to_write = "plants.txt"

# # with open(file_to_write, "w") as file:
# #     for item in data:
# #         file.write(item + "\n")

# with open(file_to_write, "a") as myfile:
#     for item in data:
#         print(item, file=myfile)

with open("plants.txt", "a") as myfile:
    for line in data:
        myfile.write(line + "\n")
        
# Writing plant data to a text file
with open(file_to_write, "a") as myfile:
    for line in data:
        print(line, file=myfile)