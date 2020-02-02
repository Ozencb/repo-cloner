import json
import requests
import argparse
import os
import sys
import re
from git import Repo

class Cloner:
    # Constructor
    def __init__(self, args):
        self.args = args
        return

    # Argument validation
    def __validate_args(self):
        args = self.args

        user = args.user
        mode = args.mode

        # Set output directory
        if args.output:
            os.makedirs(args.output, exist_ok=True)
            directory = os.path.curdir + '/' + args.output + '/' + mode.title()
        else:
            os.makedirs("RepoCloner", exist_ok=True)
            directory = os.path.curdir + '/RepoCloner/' + mode.title()

        self.directory = directory
        self.user = user
        self.mode = mode

    def __get_api_data(self):

        url = 'https://api.github.com/users/{user}/{mode}?per_page=30&page='.format(
            user = self.user,
            mode = self.mode
        )


        # Exception handling for connection errors
        try:
            r = requests.get(url,timeout=5)
            h = requests.head(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:",errh)
            msg = json.loads(r.content)
            if 'message' in msg:
                print(msg['message'])
            exit(0)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:",errc)
            exit(0)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:",errt)
            exit(0)
        except requests.exceptions.RequestException as err:
            print("There was an error.",err)
            exit(0)

        # Exception handling for JSON decoding errors
        try:
            data = r.json()
        except json.decoder.JSONDecodeError:
            print("Could not decode JSON")


        # Extract number of pages from link headers
        if 'link' in h.headers:
            links_header = h.headers['Link']
            last_page_substr = re.search('rel="next"(.*)>; rel="last"', links_header).group(1)
            total_pages = int(last_page_substr.split('&page=', 1)[1])
        else:
            total_pages = 2
            self.single_page = True


        if len(data) is not 0:
            self.total_pages = total_pages
            self.url = url
        else:
            print("No repos found. Exiting...\n")
            exit(0)


    def __initialize_download(self):
        range_ = range(1, self.total_pages)

        for page in range_:
            url = self.url + str(page)

            r = requests.get(url)
            data = json.loads(r.content)

            if 'message' in data and 'API rate limit exceeded' in data['message']: 
                print(data['message'])
            else:
                for repo in data:
                    repo_url = repo['clone_url']
                    repo_name = repo['name']
                    output_path = os.path.join(self.directory, repo_name)
                    
                    if os.path.isdir(output_path):
                        print("Directory already exists for repo. Pulling updates:" + repo_name)
                        repo = Repo(output_path)
                        repo.remotes.origin.pull()
                    else:
                        print("Cloning repo:" + repo_name)
                        Repo.clone_from(repo_url, output_path)
            
            if self.single_page:
                break
                    
        
        print("Successfully cloned all repos.")

    def clone(self):
        self.__validate_args()
        self.__get_api_data()
        self.__initialize_download()


'''
    def things():

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

'''