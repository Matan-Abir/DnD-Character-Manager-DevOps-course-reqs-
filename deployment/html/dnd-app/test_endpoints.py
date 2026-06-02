#!/usr/bin/env python3
"""Quick endpoint test"""
import requests
import time

BASE_URL = "http://localhost:5000"

# Give server time to start
time.sleep(2)

print("Testing endpoints...")

# Test dice roll
try:
    response = requests.post(f"{BASE_URL}/api/roll-dice")
    print(f"✓ Dice roll: {response.status_code} - {response.json()}")
except Exception as e:
    print(f"✗ Dice roll failed: {e}")

# Test get characters
try:
    response = requests.get(f"{BASE_URL}/api/characters")
    print(f"✓ Get characters: {response.status_code} - {len(response.json())} characters")
except Exception as e:
    print(f"✗ Get characters failed: {e}")

print("\nAll endpoints working!")
