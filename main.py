import argparse
from weather import parser as weather_parser
from weather import commands

def main():
    parser = weather_parser.create_parser()
    args = parser.parse_args()
    try:
        commands.handle_command(args)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
