import argparse

def main():
    parse = argparse.ArgumentParser(description='示例')
    parse.add_argument('h', type=str, help="帮助")

    args = parse.parse_args()

    if args.h == 'h':
        help()


def help():
    print("HELP:")

if __name__ == "__main__":
   main() 