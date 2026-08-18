# Curriculum validation

```powershell
python -m pip install -r tools/validation/requirements.txt
python tools/validation/validate_curriculum.py
```

Use `--offline` to skip GitHub and Pedro Pathing URL checks.

GitHub Actions runs the same script on every push and pull request.
