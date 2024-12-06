
from .models import Animal, ShelterLocation

def update_shelter_occupancy():
    # Get all shelter locations
    shelters = ShelterLocation.objects.all()

    for shelter in shelters:
        # Count the number of animals in this shelter with adoptedOrNot = 0
        occupancy_count = Animal.objects.filter(locationID=shelter.locationID, adoptedOrNot=0).count()
        
        # Update the currentOccupancy for the shelter
        shelter.currentOccupancy = occupancy_count
        shelter.save()  # Save the updated shelter
        
update_shelter_occupancy()