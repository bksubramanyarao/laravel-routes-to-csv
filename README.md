# how to use

## option 1

1. need to have python installed
2. copy the laravel-routes-to-csv.py to laravel routes folder
3. run by double click on laravel-routes-to-csv.py or
4. run python laravel-routes-to-csv.py from cli

## option 2

1. add the below code to routes(web.php)

2. ```php
   Route::get('/laravel-routes-to-csv', function() {
   	header('Content-Type: application/excel');
   	header('Content-Disposition: attachment; filename="routes.csv"');
   
   	$routes = Route::getRoutes();
   	$fp = fopen('php://output', 'w');
   	fputcsv($fp, ['METHOD', 'URI', 'NAME', 'ACTION']);
   	foreach ($routes as $route) {
   		if (strpos($route->uri(), '_') === false) {
   			fputcsv($fp, [head($route->methods()) , $route->uri(), $route->getName(), $route->getActionName()]);
   		}
   	}
   	fclose($fp);
   });
   ```
   
3. run php artisan serve

4. go to http://127.0.0.1:8000/laravel-routes-to-csv

5. original source https://www.terrymatula.com/development/2014/laravel-routes-generating-a-csv/

















