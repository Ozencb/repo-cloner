import json
import requests
import argparse
import os
import sys
from git import Repo

def main():
    desc = "This program is used to clone starred or created repositories of a user"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-u", "--user", help="User Name", dest='target', required=True)
    parser.add_argument("-m", "--mode", help="Enter 'repos' or 'stars'", dest='mode', required=True)
    parser.add_argument("-o", "--output", help="Output Directory", dest='output', required=False)
    args = parser.parse_args()
    target = args.target
    output = args.output
    mode = args.mode
    
    if not output:
        output = os.path.curdir + "/" + mode
    
    if mode != "repos" and mode != "stars":
        print('Enter "repos" or "stars" as --mode argument')
        print('\nExiting...')
        exit(0)
    
    if mode == "stars":
        mode_append = "starred"
    elif mode == "repos":
        mode_append = "repos"

    url = "https://api.github.com/users/" + target + "/" + mode_append + "?page=&per_page=10000"
    r = requests.get(url)
    data = json.loads(r.content)
    
    if len(data) == 0:
        print ("Found no repos")
    else:
        if  "message" in data and "API rate limit exceeded" in data["message"]:
            print ("Rate limit reached")
        else:
            for i in data:
                star_url = i["clone_url"]
                output_name = os.path.join(output, i["name"])
                if os.path.isdir(output_name):
                    print (star_url + ": Directory already exists. Pulling updates")
                    repo = Repo(output_name)
                    repo.remotes.origin.pull()
                else:
                    print (star_url)
                    Repo.clone_from(star_url, output_name)
            print ("Succesfully cloned all repos.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
            print('\nKeyboardInterrupt Detected.')
            print('\nExiting...')
            exit(0)