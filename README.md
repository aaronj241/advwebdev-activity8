# advwebdev-activity8
Activity 8 for Advanced Web Development



Issues:

Had to add a developer setting to my github account to allow git pushes for workflow stuff.

Had to update codeql-analysis with uses: github/codeql-action/init@v3 as v1 was causing errors testing

Had to remove from flask import json, from test_app.py, because it was unsed and causing errors with the flake8 lint test.