# Python Selenium Automation Framework

A Selenium WebDriver test automation framework in Python, built with the **Page Object Model**. It runs an end-to-end UI test against a demo Shopify storefront and produces an **HTML execution report with a screenshot for every step**.

> Personal project, created as a small demo of framework design in Python.

## Test Scenario

`SearchAddToCartTest.py` covers a basic shopping flow:

1. Launch the store and unlock it on the password page
2. Verify the Home page is loaded
3. Search for a product (`Snowboards`)
4. Verify the Search Results page and pick the first **in-stock** product
5. Verify the Product page shows the same product name
6. Click **Add to Cart**
7. Verify the cart contains exactly one item, with the correct name and quantity of 1

## Features

- Page Object Model, with a shared `MasterPage` base class
- Reusable action layer (explicit waits, click, set/clear text, get text/attributes, multi-element text)
- Driver management through a single `DriverScript` class (Chrome via `webdriver-manager`, incognito, cache disabled)
- Self-contained HTML reports with a timestamped folder per run
- Step-level PASS/FAIL logging with a screenshot per step
- Test case documentation in `TestCaseDoc.xlsx`

## Project Structure

```
python_automation_script/
├── SearchAddToCartTest.py        # Test script (entry point)
├── pageClasses/                  # Page Objects
│   ├── MasterPage.py             # Base page
│   ├── LoginPage.py
│   ├── HomePage.py
│   ├── ApplicationHeader.py
│   ├── SearchResultsPage.py
│   ├── ProductPage.py
│   └── YourCartSection.py
├── utilityClasses/
│   ├── DriverScript.py           # Browser setup / teardown
│   ├── ReusableActionClass.py    # Wrapped Selenium actions with waits
│   └── ReportManager.py          # HTML report + screenshots
├── TestCaseDoc.xlsx              # Test case documentation
└── requirements.txt
```

## Prerequisites

- Python 3.8+
- Google Chrome (the matching driver is downloaded automatically by `webdriver-manager`)

## Setup

```bash
git clone https://github.com/sujanvb/python_automation_script.git
cd python_automation_script
pip install -r requirements.txt
```

## Run the Test

```bash
python SearchAddToCartTest.py
```

## Reports

Each run creates, inside the `reports/` folder:

- `TestReport_<timestamp>.html`: the execution report
- `screenshots/<timestamp>/step_<n>.png`: one screenshot per logged step

Open the HTML file in any browser to review the results.

## Tech Stack

Python · Selenium WebDriver · webdriver-manager · HTML reporting

## Author

**Sujan V B**
