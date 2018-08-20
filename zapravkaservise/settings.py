import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'dji$y(z^87_+0so=438urqe&sj-+gp0yhui))@ebylxeo)pxrd'

DEBUG = False

DEV_MODE = False

#ALLOWED_HOSTS = ['.zapravkaservice.ru', 'tehniks-it.ru', 'www.zapravkaservice.ru',]

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.kartridji_zapravka',
    'main.mainpage',
    'main.main_content',
    'main.devices',
    'main.STS',
    'main.skup',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zapravkaservise.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static'
            ],
        },
    },
]

WSGI_APPLICATION = 'zapravkaservise.wsgi.application'

if DEV_MODE == True and DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'my_local_db',
            'USER': 'vlad',
            'PASSWORD': '321',
            'HOST' : 'localhost',
            'PORT' : ''
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'my_db',
            'USER': 'vlad',
            'PASSWORD': 'vlad0717',
            'HOST' : 'localhost',
            'PORT' : ''
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


if DEV_MODE == True and DEBUG == True:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static_web"),
        os.path.join(BASE_DIR, "media_web"),

    ]  
else:
    STATICFILES_DIRS = [
        '/opt/djangoEnv/zapravkaservise/static',
    	'/opt/djangoEnv/zapravkaservise/media',
    	

    ]     


    STATIC_ROOT = os.path.join(BASE_DIR, "static_web")
    MEDIA_ROOT = os.path.join(BASE_DIR, "media_web")





