import os

os.environ.setdefault("IP", "0.0.0.0.")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "hushhush")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DB_URL", "postgressql:///taskmanager")