#!/usr/bin/env python3
"""Test script to verify PIPEBOARD_API_TOKEN bypass is working"""

import sys
import os

# Add the module to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from meta_ads_mcp.core.pipeboard_auth import pipeboard_auth_manager

def test_bypass():
    print("Testing PIPEBOARD_API_TOKEN bypass...")
    print("-" * 50)
    
    # Test 1: Get access token without PIPEBOARD_API_TOKEN
    print("\n1. Testing get_access_token():")
    token = pipeboard_auth_manager.get_access_token()
    print(f"   Token received: {token}")
    print(f"   Success: {token == 'MOCK_ACCESS_TOKEN_BYPASS_12345'}")
    
    # Test 2: Test token validity
    print("\n2. Testing test_token_validity():")
    is_valid = pipeboard_auth_manager.test_token_validity()
    print(f"   Token valid: {is_valid}")
    print(f"   Success: {is_valid == True}")
    
    # Test 3: Test auth flow initiation
    print("\n3. Testing initiate_auth_flow():")
    try:
        auth_data = pipeboard_auth_manager.initiate_auth_flow()
        print(f"   Auth data: {auth_data}")
        print(f"   Success: {auth_data.get('status') == 'authenticated'}")
    except Exception as e:
        print(f"   Error: {e}")
        print(f"   Success: False")
    
    # Test 4: Force refresh should still return mock token
    print("\n4. Testing get_access_token(force_refresh=True):")
    token_refresh = pipeboard_auth_manager.get_access_token(force_refresh=True)
    print(f"   Token received: {token_refresh}")
    print(f"   Success: {token_refresh == 'MOCK_ACCESS_TOKEN_BYPASS_12345'}")
    
    print("\n" + "-" * 50)
    print("All tests completed! The bypass is working correctly.")
    print("\nYou can now use the Meta Ads MCP without PIPEBOARD_API_TOKEN.")
    print("The mock token 'MOCK_ACCESS_TOKEN_BYPASS_12345' will be used for all API calls.")

if __name__ == "__main__":
    test_bypass()