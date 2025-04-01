from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime


class FlightStatus(Enum):
    ON_TIME = "ON_TIME"
    DELAYED = "DELAYED"
    CANCELLED = "CANCELLED"


class FlightDataProcessor:
    def __init__(self) -> None:
        # Initializing an empty list for list of flights
        self.flights: List[Dict] = []

    def add_flight(self, data: Dict) -> None:
        """
        Function to add new flight to the existing flights, If flight number already exists then it will not the data

        :param data: Dictionary that will have flight_number, departure_time, arrival_time and status
        :return: None
        """

        # Checking whether flight already exist in the flights list by comparing the flight number.
        flight_already_exist = False
        for each_flight in self.flights:
            if data['flight_number'] in each_flight['flight_number']:
                flight_already_exist = True

        # Based on the flight_already_exist flag, If flight does not exist
        # then we are adding the flight data to the flight list
        if not flight_already_exist:
            data["duration_minutes"] = self.calculate_duration(data["departure_time"], data["arrival_time"])
            self.flights.append(data)

    @staticmethod
    def calculate_duration(departure_time: str, arrival_time: str) -> int:
        """
        Method to calculate duration of flight in minutes using departure and arrival time.
        :param departure_time: Departure time of the flight
        :param arrival_time: Arrival time of flight
        :return: Duration in minutes
        """
        time_format = "%Y-%m-%d %H:%M"
        # Changing the datetime sting to the specified format
        departure = datetime.strptime(departure_time, time_format)
        arrival = datetime.strptime(arrival_time, time_format)
        duration = (arrival - departure).total_seconds() / 60  # Convert seconds to minutes
        return int(duration)

    def remove_flight(self, flight_number: str) -> None:
        """
        Method to remove the given flight from the existing list of flights by comparing the given number.

        :param flight_number: Flight number to remove from the existing flight list if exist
        :return: None
        """
        self.flights = [flight for flight in self.flights if flight['flight_number'] != flight_number]

    def flights_by_status(self, status: str) -> List[Dict]:
        """
        Method to get all the flight by the given status.
        :param status: Flight status to be filtered
        :return: List of dict containing flights with the given status
        """
        return [flight for flight in self.flights if flight['status'] == status]

    def get_longest_flight(self) -> Optional[Dict]:
        """
        Method to get the flight information which is having the longest duration in minutes.
        :return: None if flight list is empty else flight with the longest duration will be returned
        """
        if not self.flights:
            return None
        return max(self.flights, key=lambda flight: flight.get('duration_minutes', 0))

    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        """
        Method to update the status of the flight using given number.
        :param flight_number: Flight number to which the flight status will be updated.
        :param new_status: New status that need to be updated.
        :return: None
        """
        for flight in self.flights:
            if flight['flight_number'] == flight_number:
                flight['status'] = new_status
                break
