import unittest
from src.university_management import UniversityManagement
import os
import json

class TestUniversityManagement(unittest.TestCase):
    def setUp(self):
        # Set up a temporary database file for testing
        self.test_db = 'test_database.json'
        self.um = UniversityManagement()
        self.um.data = {"personnel": [], "professeurs": [], "étudiants": []}
        save_data(self.um.data)

    def tearDown(self):
        # Remove the temporary database file after tests
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_person(self):
        self.um.add_person("personnel", "John Doe")
        self.assertIn("John Doe", self.um.data["personnel"])

    def test_display_all(self):
        self.um.add_person("étudiant", "Jane Doe")
        with self.assertLogs(level='INFO') as log:
            self.um.display_all()
            self.assertIn("Jane Doe", log.output[0])

if __name__ == '__main__':
    unittest.main()
