import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from backend.chat_bot import flirt_respond
def test_chat_bot():
    message = 'Hey what\'s up?'
    if len(sys.argv) > 1:
        message = sys.argv[1]
    try:
        print(flirt_respond(message))
    except Exception as e:
        print(f'Flirt failed: {e}')

def main():
    test_chat_bot()

if __name__ == '__main__':
    main()