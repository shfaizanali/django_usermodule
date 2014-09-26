
USE_I18N = True

USE_L10N = True

USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'customdb',
        'USER': 'customuser',
        'PASSWORD': 'custompassword',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}