from decouple import config, Csv
ALLOWED_HOSTS = ['.vercel.app']
DEBUG = False
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": "ep-purple-poetry-a2c68m2j-pooler.eu-central-1.aws.neon.tech",
        "PORT": 5432,
        "NAME": ,
        "USER": "neondb",
        "PASSWORD": "npg_mjDnbxXiI06z",
    }
}
