from .base import *
from config.env import  env

DEBUG = env.bool("DJANGO_DEBUG",default=False)

