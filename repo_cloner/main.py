import argparse
import traceback
from repo_cloner.cloner import Cloner

def main():
    desc = "This program is used to clone starred or created repositories of a user"
    
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-u', '--user', 
                        help='User Name',
                        dest='user',
                        type=str,
                        required=True)
    parser.add_argument('-m', '--mode',
                        help='Enter "repos" or "starred"',
                        dest='mode',
                        type=str,
                        required=True,
                        choices=['repos', 'starred'])
    parser.add_argument('-o', '--output',
                        help='Output Directory',
                        dest='output',
                        type=str,
                        required=False)
    try:
        args = parser.parse_args()
        cloner = Cloner(args)
        cloner.clone()

    except KeyboardInterrupt:
        print('\nKeypress Detected. Exiting...\n')
    except Exception:
        traceback.print_exc()
    exit(0)

if __name__ == '__main__':
    main()