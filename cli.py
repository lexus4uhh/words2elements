from tool import main

try:
    print(main(input()))
except Exception as e:
    print(f'error: {e}')