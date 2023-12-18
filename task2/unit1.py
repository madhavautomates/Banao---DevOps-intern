import unittest
import requests

class TestWebsiteLoading(unittest.TestCase):

    def test_website_loading(self):
        url = "https://atg.world"

        # Step 1: Log that the test is starting
        print("Step 1: Starting the website loading test")

        try:
            # Step 2: Log that the request is being made
            print(f"Step 2: Making a request to {url}")
            
            # Make the HTTP request
            response = requests.get(url)

            # Step 3: Log the status code received
            print(f"Step 3: Received response with status code {response.status_code}")

            # Step 4: Check if the website loaded successfully
            self.assertEqual(response.status_code, 200, "Website did not load successfully")

            # Step 5: Log that the website loaded successfully
            print("Step 5: Website loaded successfully")

        except requests.ConnectionError:
            # Step 6: Log that there was a connection error
            print("Step 6: Connection error - Website did not load")

            # Fail the test if there was a connection error
            self.fail("Connection error - Website did not load")

if __name__ == '__main__':
    unittest.main()
