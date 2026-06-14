# Weather App using OpenWeatherMap API

## Overview

This project is a simple Weather Application built using Python. It fetches real-time weather information from the OpenWeatherMap API and displays it in the terminal.

## Features

* Get current weather by city name
* Display temperature in Celsius
* Display humidity percentage
* Display weather conditions
* Secure API key management using `.env`
* Error handling for:

  * Invalid city names
  * Invalid API keys
  * No internet connection
  * Request timeout

## Technologies Used

* Python
* Requests
* Python Dotenv
* OpenWeatherMap API

## Project Structure

.
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── Weather_app.py
└── screenshots/

## Installation

1. Clone the repository

```bash
git clone <your-repository-url>
cd weather-app
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```env
API_KEY=your_api_key_here
```

4. Run the application

```bash
python Weather_app.py
```

## Example

Input:

```text
Enter city name: Delhi
```

Output:

```text
Weather Information
-------------------
City: Delhi
Temperature: 34 °C
Humidity: 52 %
Weather: Clear Sky
```

## Error Handling

### Invalid City

```text
City Not Found
```

### Invalid API Key

```text
Invalid API Key
```

### No Internet Connection

```text
No Internet Connection
```

### Request Timeout

```text
Request Timed Out
```

## Author

Shivam Choudhary
