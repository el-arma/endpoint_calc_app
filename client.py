"""Module for testing API requests to a calculation service."""

import requests

# URL to send the GET request to
url_root: str = 'http://127.0.0.1:5000/'

test_cases: list = [
    # test main route:
    '',
    # test /calculate:
    'calculate?op=sum&arg1=2&arg2=5',
    'calculate?op=sub&arg1=99&arg2=101',
    'calculate?op=sum&arg1=2&arg2=5',
    'calculate?op=mul&arg1=4&arg2=5',
    'calculate?op=div&arg1=30&arg2=5',
    'calculate?op=dggdfggdftggtgh&arg1=2&arg2=5',
    'calculate?op=div&arg1=2&arg2=0']

def my_req_test(url_endpoint: str):
    """This is a valid doc string"""

    # Send GET request (timeout 5s)
    response = requests.get(url_endpoint, timeout = 5)

    # Check if the request was successful
    if response.status_code == 200:

        # Print the content of the response (text)
        captured_data = response.text

        print(captured_data)

    else:

        print(f"Failed to retrieve content. Status code: {response.status_code}")


def main():
    """This is a valid doc string"""
    for test_case in test_cases:
        full_url_case = f'{url_root}{test_case}'
        print(f'For: {full_url_case}')
        my_req_test(full_url_case)


if __name__ == "__main__":
    main()
