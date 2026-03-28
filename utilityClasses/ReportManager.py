import os
from datetime import datetime


class Status:
    PASS = "PASS"
    FAIL = "FAIL"


class ReportManager:

    report_file = None
    driver = None
    step_counter = 1
    report_initialized = False

    base_path = os.getcwd()
    screenshot_execution_folder = None


    @staticmethod
    def set_driver(driver):
        ReportManager.driver = driver


    @staticmethod
    def initialize_report():

        if ReportManager.report_initialized:
            return

        execution_time = datetime.now().strftime("%Y%m%d_%H%M%S")

        reports_dir = os.path.join(ReportManager.base_path, "reports")
        os.makedirs(reports_dir, exist_ok=True)

        ReportManager.screenshot_execution_folder = os.path.join(
            reports_dir, "screenshots", execution_time
        )

        os.makedirs(ReportManager.screenshot_execution_folder, exist_ok=True)

        report_path = os.path.join(reports_dir, f"TestReport_{execution_time}.html")

        ReportManager.report_file = open(report_path, "w", encoding="utf-8")

        ReportManager.report_file.write("""
        <html>
        <head>
        <title>Automation Report</title>

        <style>

        body {font-family: Arial; background:#fafafa;}

        table {border-collapse: collapse; width: 100%;}

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }

        th {background:#f2f2f2;}

        .PASS {color: green; font-weight:bold;}
        .FAIL {color: red; font-weight:bold;}

        img {
            width:120px;
            border:1px solid #ccc;
        }

        </style>

        </head>

        <body>

        <h2>Automation Execution Report</h2>

        <table>

        <tr>
        <th>Sl. No</th>
        <th>Step</th>
        <th>Description</th>
        <th>Status</th>
        <th>Date & Time</th>
        <th>Screenshot</th>
        </tr>
        """)

        ReportManager.report_initialized = True


    @staticmethod
    def updateTestLog(step, description, status):

        if not ReportManager.report_initialized:
            ReportManager.initialize_report()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        screenshot_name = f"step_{ReportManager.step_counter}.png"

        screenshot_absolute = os.path.join(
            ReportManager.screenshot_execution_folder,
            screenshot_name
        )

        relative_folder = os.path.basename(ReportManager.screenshot_execution_folder)

        screenshot_relative = f"screenshots/{relative_folder}/{screenshot_name}"

        if ReportManager.driver is not None:
            ReportManager.driver.save_screenshot(screenshot_absolute)

        status_class = "PASS" if status == Status.PASS else "FAIL"

        ReportManager.report_file.write(f"""
        <tr>
        <td>{ReportManager.step_counter}</td>
        <td>{step}</td>
        <td>{description}</td>
        <td class="{status_class}">{status}</td>
        <td>{timestamp}</td>
        <td>
        <a href="{screenshot_relative}" target="_blank">
        <img src="{screenshot_relative}">
        </a>
        </td>
        </tr>
        """)

        ReportManager.step_counter += 1


    @staticmethod
    def close_report():

        if ReportManager.report_file:

            ReportManager.report_file.write("""
            </table>
            </body>
            </html>
            """)

            ReportManager.report_file.close()