#!/bin/bash
set -e
gunicorn project.wsgi --reload --log-file - --access-logfile -