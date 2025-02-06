from decouple import config, Csv
ALLOWED_HOSTS = ['127.0.0.1','.vercel.app']
DEBUG = True
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": config("POSTGRES__POSTGRES_HOST"),
        "PORT": 5432,
        "NAME": config("POSTGRES__POSTGRES_DATABASE"),
        "USER": config("POSTGRES__POSTGRES_USER"),
        "PASSWORD": config("POSTGRES__POSTGRES_PASSWORD")
    }
}
