def compute_square_footage(length, width, height):
    return 2 * length * width + 2 * length * height + 2 * width * height
def gallons_needed(square_footage):
    return square_footage / 50
while True:
    decision = input("Do you want to continue? (Yes or No): ")
    if decision.lower() == 'no':
        break
    length = float(input("Enter room length: "))
    width = float(input("Enter room width: "))
    height = float(input("Enter room height: "))
    square_footage = compute_square_footage(length, width, height)
    gallons = gallons_needed(square_footage)
    print(f"Gallons of paint needed to paint the room: {gallons:.2f}")