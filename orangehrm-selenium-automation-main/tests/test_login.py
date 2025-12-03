import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage
from utilities.config import Config

def test_successful_login():
    """Test login with correct credentials - BUG-OHRM-007 verification"""
    print("🧪 Setting up browser...")
    
    # Setup browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Initialize pages
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        config = Config()
        
        print("🧪 Testing successful login...")
        
        # Navigate and login
        login_page.navigate_to_login()
        login_page.login(config.USERNAME, config.PASSWORD)
        
        # Verify login was successful
        assert dashboard_page.is_dashboard_loaded(), "Login failed with correct credentials!"
        print("✅ Login successful with correct credentials!")
        
    finally:
        # Always close the browser
        driver.quit()

def test_username_case_insensitivity():
    """Test BUG-OHRM-007: Username field case insensitivity"""
    print("🧪 Setting up browser for case sensitivity test...")
    
    # Setup browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Initialize pages
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        config = Config()
        
        print("🧪 Testing username case insensitivity bug...")
        
        # Navigate and login with lowercase username
        login_page.navigate_to_login()
        login_page.login("admin", config.PASSWORD)  # lowercase username
        
        # Verify login worked with wrong case (confirming the bug)
        assert dashboard_page.is_dashboard_loaded(), "Login failed with lowercase username!"
        print("✅ Username case insensitivity bug confirmed! (BUG-OHRM-007)")
        print("✅ Both 'Admin' and 'admin' work as usernames - Security issue found!")
        
    finally:
        # Always close the browser
        driver.quit()

def test_login_with_invalid_credentials():
    """Test login failure with wrong password"""
    print("🧪 Setting up browser for invalid credentials test...")
    
    # Setup browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Initialize pages
        login_page = LoginPage(driver)
        config = Config()
        
        print("🧪 Testing login with invalid credentials...")
        
        # Navigate and login with wrong password
        login_page.navigate_to_login()
        login_page.login(config.USERNAME, "wrongpassword")
        
        # Verify login failed (should not see dashboard)
        dashboard_page = DashboardPage(driver)
        login_successful = dashboard_page.is_dashboard_loaded()
        
        assert not login_successful, "Login should have failed with wrong password!"
        print("✅ Login correctly failed with invalid credentials!")
        
    finally:
        driver.quit()

def test_forgot_password_link_missing_bug():
    """Test BUG-OHRM-002: Forgot Password link is missing or not working"""
    print("🧪 Testing BUG-OHRM-002: Forgot Password link bug...")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        
        # Check if forgot password link exists
        forgot_password_present = login_page.is_element_present(login_page.FORGOT_PASSWORD_LINK)
        
        # This test DOCUMENTS the bug - the link should be present but isn't
        if not forgot_password_present:
            print("✅ BUG CONFIRMED: Forgot password link is MISSING! (BUG-OHRM-002)")
            print("✅ This is a security and usability issue!")
            # We expect this to "fail" because the bug exists - but we document it properly
            pytest.fail("BUG-OHRM-002 CONFIRMED: Forgot password link is missing from login page")
        else:
            print("✅ Forgot password link is present and working")
            assert True
            
    finally:
        driver.quit()

def test_background_color_consistency():
    """Test BUG-OHRM-006: Background color consistency"""
    print("🧪 Testing BUG-OHRM-006: Background color check...")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        
        # Get background color for documentation
        body = driver.find_element(By.TAG_NAME, "body")
        background_color = body.value_of_css_property("background-color")
        
        print(f"🎨 Current background color: {background_color}")
        print("📝 Note: Manual observation needed for color inconsistency across sessions")
        
        # This test passes but documents the potential issue
        assert True, "Background color documented - manual verification needed for BUG-OHRM-006"
        
    finally:
        driver.quit()

def test_leave_application_form_bug():
    """
    Test BUG-OHRM-001: Apply Leave functionality form submission
    This demonstrates actual form submission and detects form issues
    """
    print("🧪 Testing Leave Application Form Submission...")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Initialize pages
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        leave_page = LeavePage(driver)
        config = Config()
        
        # Login first
        print("🔐 Logging in to access Leave module...")
        login_page.navigate_to_login()
        login_page.login(config.USERNAME, config.PASSWORD)
        
        # Verify login successful
        assert dashboard_page.is_dashboard_loaded(), "Login failed!"
        print("✅ Login successful, navigating to Leave module...")
        
        # Navigate to Leave section
        print("📋 Navigating to Leave module...")
        dashboard_page.navigate_to_leave()
        leave_page.navigate_to_apply_leave()
        
        # Wait for page to load completely
        import time
        time.sleep(3)
        
        # Check for the original bug - "No Leave Types with Leave Balance"
        print("🔍 Checking for form submission issues...")
        original_bug_detected = leave_page.is_no_leave_balance_displayed()
        
        if original_bug_detected:
            print("✅ BUG-OHRM-001 CONFIRMED: 'No Leave Types with Leave Balance' message displayed!")
            print("✅ This prevents users from submitting leave application forms!")
            
            # Demonstrate form interaction attempt
            print("📝 Demonstrating form submission attempt despite the bug...")
            form_interaction_possible = leave_page.attempt_leave_application(
                from_date="2025-01-01",
                to_date="2025-01-02",
                comment="Test leave application - Automated test"
            )
            
            # This test "fails" intentionally to document the bug
            pytest.fail("BUG-OHRM-001 CONFIRMED: Cannot submit leave application form due to no leave balance")
        
        else:
            print("ℹ️  Original BUG-OHRM-001 not detected - testing form submission functionality...")
            
            # Test actual form submission
            print("📝 Testing actual form submission...")
            form_interaction_possible = leave_page.attempt_leave_application(
                from_date="2025-01-01",
                to_date="2025-01-02",
                comment="Test leave application - Automated test"
            )
            
            # Check if leave type dropdown is available
            dropdown_available = leave_page.is_leave_type_dropdown_available()
            print(f"📊 Leave type dropdown available: {dropdown_available}")
            print(f"📊 Form interaction possible: {form_interaction_possible}")
            
            if not form_interaction_possible:
                print("✅ FORM SUBMISSION ISSUE DETECTED: Apply button not available!")
                print("✅ This demonstrates form submission testing - even though original bug is fixed, there are still form issues!")
                # Document the form submission issue
                pytest.fail("FORM SUBMISSION ISSUE: Apply button not available for leave application")
            else:
                print("✅ Form submission elements are accessible")
                # If form is accessible, we could add more form submission tests here
                assert True, "Form submission testing completed"
            
    except Exception as e:
        print(f"❌ Test error: {str(e)}")
        raise
    finally:
        driver.quit()

