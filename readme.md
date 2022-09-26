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



