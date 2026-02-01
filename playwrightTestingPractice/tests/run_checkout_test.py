#!/usr/bin/env python3
"""
Quick test script to verify checkout_click navigates to the correct page
"""
import subprocess
import sys

print("=" * 70)
print("Running test_click_back to verify checkout navigation...")
print("=" * 70)

result = subprocess.run(
    ["python", "-m", "pytest", "test_06_order.py::test_click_back", "-v", "-s"],
    cwd=r"c:\Users\86885\Testing\PlaywrightAutomationstore\playwrightTestingPractice\tests",
    capture_output=True,
    text=True,
    timeout=180
)

print(result.stdout)
print(result.stderr)

# Check if test passed
if "PASSED" in result.stdout or result.returncode == 0:
    print("\n" + "=" * 70)
    print("✓ TEST PASSED - Checkout navigation is working correctly!")
    print("=" * 70)
    sys.exit(0)
else:
    print("\n" + "=" * 70)
    print("✗ TEST FAILED - Check the output above for details")
    print("=" * 70)
    sys.exit(1)
