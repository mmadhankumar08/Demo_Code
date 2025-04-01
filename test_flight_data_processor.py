import unittest
from flight_data_processor import FlightDataProcessor


class TestFlightDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = FlightDataProcessor()
        self.sample_data = {
            "flight_number": "AZ001",
            "departure_time": "2025-02-19 15:30",
            "arrival_time": "2025-02-20 03:45",
            "status": "ON_TIME"
        }
        self.processor.add_flight(self.sample_data)

    def test_add_flight(self):
        new_flight = {
            "flight_number": "AZ002",
            "departure_time": "2025-02-21 11:00",
            "arrival_time": "2025-02-21 16:00",
            "status": "DELAYED"
        }

        self.processor.add_flight(new_flight)
        self.assertIn(new_flight, self.processor.flights)

    def test_add_duplicate_flight(self):
        duplicate_flight = {
            "flight_number": "AZ001",
            "departure_time": "2025-02-19 15:30",
            "arrival_time": "2025-02-20 03:45",
            "status": "ON_TIME"
        }
        self.processor.add_flight(duplicate_flight)
        self.assertEqual(len(self.processor.flights), 1)

    def test_remove_flight(self):
        self.processor.remove_flight("AZ001")
        self.assertEqual(len(self.processor.flights), 0)

    def test_flights_by_status(self):
        flights = self.processor.flights_by_status("ON_TIME")
        self.assertEqual(len(flights), 1)
        self.assertEqual(flights[0]['flight_number'], "AZ001")

    def test_get_longest_flight(self):
        new_flight = {
            "flight_number": "AZ003",
            "departure_time": "2025-02-22 10:00",
            "arrival_time": "2025-02-23 18:00",
            "status": "ON_TIME"
        }
        self.processor.add_flight(new_flight)
        longest_flight = self.processor.get_longest_flight()
        self.assertEqual(longest_flight['flight_number'], "AZ003")

    def test_update_flight_status(self):
        self.processor.update_flight_status("AZ001", "CANCELLED")
        self.assertEqual(self.processor.flights[0]['status'], "CANCELLED")


if __name__ == '__main__':
    unittest.main()
