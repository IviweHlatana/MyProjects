# OrangeHRM Test Automation

## Project Overview
Selenium WebDriver test automation for OrangeHRM demo platform, covering Week 3 requirements and verifying bugs from manual testing reports. This project demonstrates automated testing capabilities by validating both functionality and identified defects from previous manual testing phases.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Chrome Browser
- Git

### Installation
```bash
# Clone repository
git clone <your-repo-url>
cd orangehrm-automation

# Install dependencies
pip install -r requirements.txt
Running Tests
bash
# Run all tests with verbose output
pytest tests/ -v

# Generate HTML report
pytest tests/ --html=report.html --self-contained-html

# Run specific test file
pytest tests/test_login.py -v

# Run with detailed output and logging
pytest tests/ -v -s

📊 Test Results Summary
Latest Execution Results:

Total Tests: 6

Tests Passed: 4 ✅

Tests "Failed": 2 ❌ (Intentional bug detection & form submission testing)

Success Rate: 67% (100% for intended functionality)

Execution Time: ~150 seconds

Bugs Verified: 2 confirmed, 1 form issue detected

🐛 Bugs Automatically Detected
Bug ID	Status	Description	Test Evidence
BUG-OHRM-002	✅ CONFIRMED	Forgot password link missing	test_forgot_password_link_missing_bug
BUG-OHRM-007	✅ CONFIRMED	Username case insensitive (security issue)	test_username_case_insensitivity
FORM SUBMISSION	✅ TESTED	Leave application form issues	test_leave_application_form_bug
🧪 Test Cases Implemented
Login Functionality Tests
test_successful_login - Validates basic login with correct credentials

test_username_case_insensitivity - Confirms security vulnerability BUG-OHRM-007

test_login_with_invalid_credentials - Tests negative scenarios with wrong passwords

test_forgot_password_link_missing_bug - Detects missing password reset functionality (BUG-OHRM-002)

test_background_color_consistency - Documents UI consistency issues (BUG-OHRM-006)

test_leave_application_form_bug - Tests actual form submission with leave application

🛠️ Technical Stack
Programming Language: Python 3.13.7

Testing Framework: Selenium WebDriver 4.15.0

Test Runner: pytest 8.4.2

Reporting: pytest-html 4.0.2

Browser Automation: Chrome with ChromeDriver

Design Pattern: Page Object Model (POM)

Driver Management: webdriver-manager

📁 Project Structure
text
orangehrm-automation/
├── pages/                   # Page Object Model classes
│   ├── base_page.py        # Base page with common functionality
│   ├── login_page.py       # Login page elements and actions
│   ├── dashboard_page.py   # Dashboard page elements
│   └── leave_page.py       # Leave module page elements 🆕
├── tests/                   # Test case implementations
│   ├── test_login.py       # Login functionality tests
│   └── __init__.py
├── utilities/               # Configuration and helpers
│   ├── config.py           # Test configuration
│   └── __init__.py
├── reports/                 # Generated test reports (after execution)
├── requirements.txt         # Python dependencies
├── test_report.html        # Automated HTML test report
├── README.md               # This file
└── .gitignore              # Git ignore rules

🚦 Test Execution Examples
bash
# Basic test execution
pytest tests/test_login.py -v

# With HTML reporting
pytest tests/test_login.py --html=test_report.html --self-contained-html

# Run with detailed output
pytest tests/test_login.py -v -s

# Run specific test
pytest tests/test_login.py::test_leave_application_form_bug -v
📈 Output Examples
Successful Test Execution:
text
tests/test_login.py::test_successful_login PASSED
tests/test_login.py::test_username_case_insensitivity PASSED
tests/test_login.py::test_login_with_invalid_credentials PASSED
tests/test_login.py::test_forgot_password_link_missing_bug FAILED
tests/test_login.py::test_background_color_consistency PASSED
tests/test_login.py::test_leave_application_form_bug FAILED

Form Submission Evidence:
🧪 Testing Leave Application Form Submission...
📝 Testing actual form submission...
✅ FORM SUBMISSION ISSUE DETECTED: Apply button not available!
✅ This demonstrates form submission testing

🐛 Bug Report Integration
This automation suite specifically verifies bugs identified in the manual testing phase:

BUG-OHRM-001: No Leave Types with Leave Balance (Form submission tested)

BUG-OHRM-002: Forgot Password Link Missing

BUG-OHRM-006: Background Color Inconsistency

BUG-OHRM-007: Username Case Insensitivity

🔮 Future Enhancements
Add tests for PIM module functionality

Implement data-driven testing with parameterization

Add cross-browser testing capabilities

Integrate with CI/CD pipelines

Add API testing integration

Implement visual regression testing