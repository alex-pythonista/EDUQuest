#!/bin/bash

echo "EDUQuest APP SERVER RUN"

python manage.py runserver --settings=$DJANGO_SETTINGS_MODULE 0.0.0.0:8000