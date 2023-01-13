1) using django-restframework, paged with default pagesize = 1
	.a (GET,POST) 
		example : http://127.0.0.1:8000/api/municipalities/
		
	.b (GET,PUT,DELETE) detailed
		example : http://127.0.0.1:8000/api/municipalities/5
		
	.c (GET,POST) using django-restframework-gis, input/output one feature
		      at the time in GeoJSON format, such as provided in "municipilities_nl.geojson" file.
		      
		example : http://127.0.0.1:8000/api/municipalitieslocation/
		      
		
	
2) using djangorestframework-gis, filtering using bounding box, paged (limited to 100 features/page) 
	.a) spatial query
		example : http://127.0.0.1:8000/api/filter/?in_bbox=4.222,51.781,5.5,52.5
		

3) python script, named "post_municipalities.py" to automatically post "municipilities_nl.geojson"
	.a) run the script 
		example : python post_municipalities.py
		
		
=============================================================================================================
4) docker and setup from github follow (README.MD)
==============================================================================================================
5) jwt autorization:
	.a) create user http://127.0.0.1:8000/api/register/
	.b) login (top right) or http://127.0.0.1:8000/api/login/
	.c) use end points of section (1)
