
import os
import subprocess
import json
import csv
from pathlib import Path



laravel_project_root = str(Path(os.getcwd()).parents[0])
print(laravel_project_root)

laravel_project_routes = subprocess.Popen(f'cd {laravel_project_root} & php artisan route:list --json', shell=True, stdout=subprocess.PIPE)

routes_json = json.loads(laravel_project_routes.stdout.read().decode("utf-8"))


with open('laravel-routes.csv', 'w', newline='') as file:
	wr = csv.writer(file, quoting=csv.QUOTE_ALL)
	wr.writerow(['METHOD', 'URI', 'NAME', 'ACTION'])
	for route in routes_json:
		wr.writerow([route['method'], route['uri'], route['name'], route['action']])

