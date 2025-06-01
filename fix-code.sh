#!/bin/bash
echo "🔧 Running auto-fixes..."

ruff check naboopay test setup.py --fix
ruff format naboopay test setup.py

isort naboopay test setup.py
black naboopay test setup.py

pre-commit run --all-files

echo "✅ Code fixes complete!"