from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.boywtnsbssunyyyasxud',
        'PASSWORD': 'ZHJ-vrj*cwh8pnu7hpn',
        'HOST': 'aws-0-eu-west-2.pooler.supabase.com',
        'PORT': '5432',
    }
}

# Security settings
SECRET_KEY = 'ChickenTikkaMasalaIsTheBestFoodInTheWorld'
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1','oddsmatcha.uk']
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'tools',
    #'tailwind',
    'theme',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.discord',
]

TAILWIND_APP_NAME = 'theme'
TAILWIND_CSS_ARGUMENTS = [
    '--output', 'theme/static/css/dist/styles.css'
]
# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # <-- Add this line
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1  # or your actual site ID

SOCIALACCOUNT_PROVIDERS = {
    "discord": {
        "SCOPE": [
            "identify",
            "email"
        ]
    }
}
SOCIALACCOUNT_LOGIN_ON_GET = True

# URL configuration
ROOT_URLCONF = 'odds-matcha.urls'

SUPABASE_JWT_SECRET = 'H3fncEtvTlJUfByii+juyPC2QpU4sp05aXcSdoQLeGih/3iwjK5jKKOI/R66Y9fEi7/SHgWm38NDM1m3GAv17Q=='
SUPABASE_URL = "https://boywtnsbssunyyyasxud.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJveXd0bnNic3N1bnl5eWFzeHVkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc5ODY0NDQsImV4cCI6MjA2MzU2MjQ0NH0.ewgUMeJ8zLpnt6yJKoOWEFpn-RiipNwBqZTuuExTwcU"
SUPABASE_SERVICE_ROLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJveXd0bnNic3N1bnl5eWFzeHVkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0Nzk4NjQ0NCwiZXhwIjoyMDYzNTYyNDQ0fQ.3mvEm5CMpbQyXuA7oB4NKXvksQVwzsjFLjNg3yzXUoM"

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "theme" / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'tools.context_processors.user_tools',  # <-- Add this line
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'odds-matcha.wsgi.application'

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

LOGIN_REDIRECT_URL = '/'