#!/usr/bin/env python3
"""
Sample Python code with security and style issues for testing
This file contains intentional violations for bandit, pylint, and flake8
"""

import os
import subprocess
import pickle
import hashlib
import sqlite3
import random
import sys

# Global variable (bad practice)
global_var = "This should not be global"

def insecure_function():
    """Function with security issues"""
    # Bandit: Hardcoded password
    password = "super_secret_password_123"
    
    # Bandit: Use of eval() (dangerous)
    user_input = "print('hello')"
    eval(user_input)
    
    # Bandit: Use of exec() (dangerous)
    exec("import os; os.system('ls')")
    
    # Bandit: Insecure tempfile usage
    import tempfile
    temp_file = tempfile.mktemp()
    with open(temp_file, 'w') as f:
        f.write("sensitive data")
    
    # Bandit: SQL injection vulnerability
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    user_id = "1 OR 1=1"
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    
    # Bandit: Insecure hash usage
    hash_obj = hashlib.md5()
    hash_obj.update(b"sensitive data")
    
    # Bandit: Use of pickle (insecure deserialization)
    data = pickle.dumps({"key": "value"})
    unpickled = pickle.loads(data)
    
    return password

def poorly_formatted_function(    arg1,    arg2    ,    arg3    ):
    """Function with formatting issues"""
    # Flake8: Multiple spaces around operators
    x = 5  *  2
    y = x +  10
    
    # Flake8: Line too long
    very_long_variable_name_that_exceeds_the_line_length_limit_and_should_be_shortened = "This is a very long string"
    
    # Flake8: Missing whitespace after comma
    items = [1,2,3,4,5]
    
    # Flake8: Extra whitespace
    result = ( x + y )
    
    # Flake8: Unused import (sys is imported but not used)
    # Flake8: Import not at top (subprocess imported above but used here)
    subprocess.run(["ls", "-la"])
    
    # Pylint: Missing docstring for variable
    bad_var = 42
    
    # Pylint: Invalid variable name
    invalid_name_123 = "bad naming"
    
    # Pylint: Too many local variables
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = range(16)
    
    # Pylint: Unreachable code
    return True
    print("This will never execute")
    
def another_bad_function():
    """Function with various code quality issues"""
    # Pylint: Missing return type annotation
    # Pylint: Too many statements in function
    x = 1
    y = 2
    z = 3
    result = x + y + z
    print(result)
    
    # Pylint: Magic number
    if result == 6:
        print("Result is 6")
    
    # Pylint: Consider using enumerate
    items = ['a', 'b', 'c']
    for i in range(len(items)):
        print(f"Item {i}: {items[i]}")
    
    # Pylint: Redundant parenthesis
    return (result)

class BadClass:
    """Class with various issues"""
    
    def __init__(self):
        # Pylint: Invalid name
        self.BAD_ATTRIBUTE = "should be lowercase"
        
    def bad_method(self, x, y):
        # Pylint: Missing docstring
        # Pylint: Argument name doesn't follow snake_case
        return x + Y  # Pylint: Undefined variable Y
    
    def another_method(self):
        # Pylint: No return
        pass

def function_with_exceptions():
    """Function with exception handling issues"""
    try:
        # Bandit: Try-except without specific exception
        risky_operation()
    except:
        # Pylint: Bare except
        pass
    
    try:
        another_operation()
    except Exception as e:
        # Pylint: Exception variable not used
        pass
    
    # Pylint: Too broad exception
    try:
        yet_another_operation()
    except BaseException:
        pass

def risky_operation():
    """Simulate risky operation"""
    # Bandit: Use of os.system() (command injection)
    os.system("rm -rf /")
    
    # Bandit: Use of subprocess with shell=True
    subprocess.run("ls -la", shell=True)

def another_operation():
    """Another operation"""
    pass

def yet_another_operation():
    """Yet another operation"""
    pass

# Bandit: Code running at module level
if __name__ == "__main__":
    # Pylint: Too many statements in module level
    print("Starting execution")
    insecure_function()
    poorly_formatted_function(1, 2, 3)
    another_bad_function()
    
    # Pylint: Unused variable
    unused_var = "This is never used"
    
    # Bandit: Debug print with sensitive data
    print(f"Password: {insecure_function()}")
