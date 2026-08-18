"""
# Low-Level Design: Multi-Level Parking Lot System

## Requirements
- Multi-level parking lot with various Spot types (Motorcycle, Compact/Car, Large/Truck, Electric).
- Vehicles of different types (Motorcycle, Car, Truck, EV) parking in compatible spot sizes.
- Flexible pricing strategy (Hourly rate based on vehicle type).
- Ticket generation on entry, fee calculation & spot release on exit.
"""

from enum import Enum
from typing import List, Dict, Optional
import time


class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    TRUCK = 3


class SpotType(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3


class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.current_vehicle: Optional[Vehicle] = None

    def is_available(self) -> bool:
        return self.current_vehicle is None

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        if self.spot_type == SpotType.LARGE:
            return True
        if self.spot_type == SpotType.COMPACT:
            return vehicle.vehicle_type in (VehicleType.CAR, VehicleType.MOTORCYCLE)
        if self.spot_type == SpotType.MOTORCYCLE:
            return vehicle.vehicle_type == VehicleType.MOTORCYCLE
        return False

    def park(self, vehicle: Vehicle):
        self.current_vehicle = vehicle

    def unpark(self):
        self.current_vehicle = None


class ParkingTicket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = time.time()
        self.exit_time: Optional[float] = None
        self.fee: float = 0.0


class ParkingLotLevel:
    def __init__(self, level_number: int, spots: List[ParkingSpot]):
        self.level_number = level_number
        self.spots = spots

    def find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        for spot in self.spots:
            if spot.is_available() and spot.can_fit_vehicle(vehicle):
                return spot
        return None


class ParkingLot:
    def __init__(self, name: str, levels: List[ParkingLotLevel]):
        self.name = name
        self.levels = levels
        self.active_tickets: Dict[str, ParkingTicket] = {}
        self._ticket_counter = 1000

    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        for level in self.levels:
            spot = level.find_available_spot(vehicle)
            if spot:
                spot.park(vehicle)
                self._ticket_counter += 1
                ticket_id = f"TCK-{self._ticket_counter}"
                ticket = ParkingTicket(ticket_id, vehicle, spot)
                self.active_tickets[ticket_id] = ticket
                return ticket
        return None  # Parking full

    def unpark_vehicle(self, ticket_id: str, hourly_rate: float = 5.0) -> float:
        if ticket_id not in self.active_tickets:
            raise KeyError("Invalid ticket ID")

        ticket = self.active_tickets.pop(ticket_id)
        ticket.spot.unpark()
        ticket.exit_time = time.time()

        # Compute fee (minimum 1 hour)
        duration_hours = max(1.0, (ticket.exit_time - ticket.entry_time) / 3600)
        fee = round(duration_hours * hourly_rate, 2)
        ticket.fee = fee
        return fee


# =====================================================================
# Tests
# =====================================================================
def test_parking_lot():
    spots = [
        ParkingSpot("L1-S1", SpotType.MOTORCYCLE),
        ParkingSpot("L1-S2", SpotType.COMPACT),
        ParkingSpot("L1-S3", SpotType.LARGE),
    ]
    level1 = ParkingLotLevel(1, spots)
    lot = ParkingLot("Downtown Mall Garage", [level1])

    # 1. Park car
    car = Vehicle("ABC-123", VehicleType.CAR)
    ticket_car = lot.park_vehicle(car)
    assert ticket_car is not None
    assert ticket_car.spot.spot_id == "L1-S2"

    # 2. Park truck
    truck = Vehicle("TRK-999", VehicleType.TRUCK)
    ticket_truck = lot.park_vehicle(truck)
    assert ticket_truck is not None
    assert ticket_truck.spot.spot_id == "L1-S3"

    # 3. Another car cannot park because compact & large are occupied
    car2 = Vehicle("XYZ-789", VehicleType.CAR)
    assert lot.park_vehicle(car2) is None

    # 4. Unpark car
    fee = lot.unpark_vehicle(ticket_car.ticket_id, hourly_rate=10.0)
    assert fee == 10.0
    assert spots[1].is_available() is True


if __name__ == "__main__":
    test_parking_lot()
    print("Parking Lot LLD tests passed successfully! [OK]")
