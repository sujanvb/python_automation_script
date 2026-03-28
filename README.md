# Selenium Python Automation Framework

This repository contains a Selenium-based test automation framework built using Python.  
The framework is designed to execute UI automation tests and generate HTML reports with screenshots for each test step.

## Features

- Selenium WebDriver based automation
- Automatic screenshot capture for test steps
- Timestamp-based report folder creation
- HTML test execution report
- Modular framework structure
- Easy test execution

## Prerequisites

Make sure the following software is installed:

- Python 3.x
- Google Chrome browser

## Installation

Clone the repository:

git clone https://github.com/sujanvb/adnabu-qa-assignment.git
cd adnabu-qa-assignment

Install required dependencies:

pip install -r requirements.txt

## Running the Test

To execute the automation test, run the following command from the project root directory:

python SearchAddToCartTest.py

This will:
- Launch the browser
- Execute the test steps
- Capture screenshots for each step
- Generate an HTML execution report

## Reports

After execution, reports will be generated inside the `reports` folder with a timestamp-based directory.

## Author

Sujan V B