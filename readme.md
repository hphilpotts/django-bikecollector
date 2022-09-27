26/09/22:       

### Beginning project:      
`django-admin startproject` run, local and remote repos established, `python3 manage.py startapp` run.       
`main_app` inserted into `settings.py`, tested working ok on `localhost:8000`.      

Database `bikecollector` created in _pgAdmin4_, connected in `settings.py`. Migrations sent.        

`urls.py` created in app folder, `urls.py` updated in project folder, `'home'` added to app `views.py`.     
- tested working ok using simple HTML.      

`base.html` created in `main_app/templates/` for DTL inheritance, 'about' template also created.        
`main_app/static/css/style.css` added.      

- issues seen where _localhost:8000/about/_ not triggering error but nothing rendering.     
- _issue found_: I had used `HttpResponse` instead of `render` in `views.py`, now working ok.       

### Index functionality:        
- hardcoding sample data into `views.py` in order to implement and test index data.
- added link w/path to `base.html`, updated `urls.py` with path, updated `views.py` request API.        
- `main_app/templates/bikes/index.html` created.
- _Largely working fine, with the exception of when I have tried to concatenate multiple values, workaround like so:_     
    - `<span class="card-title"> {{ bike.make  }} {{ bike.model }} </span>`       
    - started looking at templatetags etc. but have been advised that the above is acceptable!      
- _Also had issues with accessing list by index, later realised that I should be using_ `.index` _rather than_ `[index]`.      
- reversed list using `{% for bike in bikes reversed %}` - `bikes.reverse()` of course did not work!        
- also able to capitalise `bike.material.0` using `{{bike.material.0 |title }}`.        

27/09/22        

### Creating Bike Model:        
- creating Bike class in `models.py`, ran `makemigrations` and `migrate` without issue.            
    - avoiding needing to establish a second table for `bike.material` (currently a list):
    - therefore separated out into two properties: `bike.material` and `bike.material_info    
- commented out hard-coded Bike model and dictionaries in `views.py`, imported `Bike` from `.models`.       
- updated `bikes_index` API with `bikes = Bike.objects.all()` - Django ORM.     
- updated `bikes/index.html` to reflect changes to Bike objects.        
- directly inserted test data into _pgAdmin4_, tested working ok.       

### Creating superuser:     
- created superuser 'hphilpotts` for admin, logged in ok.       
- registered `Bike` model in `main_app/admin.py`, successfully added as admin.      

### Adding images:       
- updated `Bike` model to include `image` property. Chose URL as string over upload using `ImageField` to reduce storage and make for simpler implementation. Migrated successfully.        
- `index.html` updated and images added. Some images do not work - image type is important.     
- CSS added to improve appearance:      

![basic formatting work with images added]('readme_screenshots/Screenshot 2022-09-27 at 16.41.39.png')      

### Detail view:        
- making images clickable for details view. Added `<a></a>` tags around images in `index.html`, path added in `urls.py`, `views.py` updated.        
- `/bikes/detail.html` created, CSS added.   

- Also, hardcoded urls in `base.html` and `home.html` switched out for _Django_ `{% url %}`.        




