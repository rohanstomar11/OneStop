# One Stop Backend

Welcome to the One Stop Backend  
Pre-Requisite: Python

## 1. Set up Django

### 1.1 Virtual Environment

Setup a Virtual Environment.
Example. To create a virtual environment using venv (ONE TIME)

```bash
python -m venv env 
```

Activate the virtual Environment

```bash
source env/bin/activate
```

### 1.2 Install Django (ONE TIME)

```bash
pip install django djangorestframework
```

Next, let’s start a new Django project:

```bash
django-admin startproject {{projectname}}
```

In `{{projectname}}/settings.py`:

```python
INSTALLED_APPS = [
    # All your installed apps stay the same
    ...
    'rest_framework',
]
```

Test run the Django server:

```bash
cd {{projectname}}/
python manage.py runserver
```

Go to http://localhost:8000 to see if it works!

### 1.3 Create API app

```bash
python manage.py startapp {{appname}}
```

### 1.4 Register the {{appname}} app with the {{projectname}} project

Edit `{{projectname}}/settings.py`

```python
INSTALLED_APPS = [
    '{{appname}}.apps.{{Appname}}Config',
    ... # Leave all the other INSTALLED_APPS
]
```

### 1.5 Migrate the database

```bash
python manage.py migrate
```

### 1.6 Create Super User

```
python manage.py createsuperuser
```

Follow the prompts to create a superuser.

Check that it works:

```
python manage.py runserver
```

Go to http://localhost:8000/admin & log in.

## 2. Create a model in the database that Django ORM will manage

We’ll build it in `{{appname}}/models.py`, so open up that file.

### 2.1 Create model

```python
# {{appname}}/models.py
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)    
    
    def __str__(self):
        return self.name
```

### 2.2 Make migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### 2.3 Register Profile with the admin site

Open `{{appname}}/admin.py`:

```python
# {{appname}}/admin.py
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
```

Check that it worked:

```bash
python manage.py runserver
```

Visit http://localhost:8000/admin and see the new model

### 2.4 Create some new profiles

In the admin site, click "Add" to create some new model instances for testing

## 3. Serialize the Profile model

Create a new file - `{{appname}}/serializers.py`:

```python
# {{appname}}/serializers.py

from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (‘id’, ‘name’, ‘email’)
```

## 4. Display the data

We need to create Views & URLs so we can access the data from the browser.

### 4.1 Views

In `{{appname}}/views.py`:

```python
# {{appname}}/views.py

from rest_framework import viewsets

from .serializers import ProfileSerializer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('name')
    serializer_class = ProfileSerializer
```

### 4.2 Site-wide URLs

Head to the project level URLs file - `{{projectname}}/urls.py`:

```python
# {{projectname}}/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('{{appname}}.urls')),
]
```

### 4.3 API URLs

Now create the API-specific routes in `{{appname}}/urls.py`:

```python
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

## Test it!

```bash
python manage.py runserver
```

## 5. Allow CORS

```bash
pip install django-cors-headers
```

Add these in `{{projectname}}/settings.py`

```python
# {{projectname}}/settings.py

INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)
```

```python
# {{projectname}}/settings.py

MIDDLEWARE = [
    ...,
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...,
]
```

```python
# {{projectname}}/settings.py

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
```

- Go to http://localhost:8000 & see the API root.
- Go to http://localhost:8000/profiles & see the Profiles listed.
- Go to http://localhost:8000/profiles/1/ & see a specific Profile instance.
- POST a payload to http://localhost:8000/profiles to add a new Profile.
- PUT/PATCH a payload to http://localhost:8000/profiles/1/ to update a Profile instance.
