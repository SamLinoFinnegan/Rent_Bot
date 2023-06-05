# Rental Bot

This project is a script that uses Selenium to search a rental site and automatically send requests for ads that meet the required parameters.

## Installation

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running the following command:

pip install -r requirements.txt


## Usage

1. Modify the `user_input.py` file and define your search parameters and user data.
2. Add your credentials to the '.env' file (your email and password that you will use to log into Daft.ie)
3. Run the `user_input.py` script to start the rental bot.


## Configuration

The `user_input.py` file contains the following configuration options:

- `MY_SEARCHES`: List of URLs for the rental site search queries.
- `full_name`: Your full name.
- `your_email`: Your email address.
- `your_phone`: Your phone number.
- `message`: The message you would like to send to homeowners.
- `params`: Dictionary containing various search parameters:
- `Bedrooms Available`: Number of bedrooms available.
- `Single Bedroom`: Specify if a single bedroom is required.
- `Double Bedroom`: Specify if a double bedroom is required.
- `Available From`: Maximum number of days in the future to consider for availability.
- `Lease`: Specify lease details.
- `Sharing with`: Specify if sharing with others is acceptable.
- `Furnished`: Specify if a furnished property is required.
- `Bathroom`: Specify bathroom requirements.
- `Owner Occupied`: Specify if owner-occupied properties are acceptable.
- `Preferences`: Specify gender preferences.
- `max_price`: Maximum price limit.
- `ignore`: List of parameters to ignore in the search.

## Dependencies

- Selenium
- Python Dotenv

