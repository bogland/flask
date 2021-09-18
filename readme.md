#prettier 이슈일때  
플러그인 설치

1. Django Baptiste Darthenay
2. Unibeautify - Universal Formatter

[project경로]/.vscode/settings.json

```
{
  "files.associations": {
    "**/*.html": "html",
    "**/templates/*/*.html": "django-html",
    "**/templates/*": "django-html",
    "**/requirements{/**,*}.{txt,in}": "pip-requirements"
  },
  "unibeautify.enabled": true,
  "[django-html]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "Glavin001.unibeautify-vscode"
  }
}

```
