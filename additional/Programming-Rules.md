# Programming Rules for Django Project

## 1. General Rules
- Commit messages must be clear and follow this format: `[type]: short description` (e.g., `fix: corrected typo in model`).
- Code should be thoroughly tested before pushing to the repository.
- Any push that does not follow these rules will be reverted.

## 2. Rules for Models
- Every model must inherit from `django.db.models.Model`.
- Field names must be in `camelCase`.
- Use `Meta` class to specify ordering and verbose names.
- Each model should have a `__str__()` method for a readable string representation.
- Related fields must use `related_name` in ForeignKey or ManyToMany fields for reverse relationships.
  
## 3. Rules for Views
- All views must be associated with a URL pattern in the `urls.py` file.
- Views should be named appropriately to reflect their purpose.
- All views returning HTML content must extend from a base template like `base.html`.

## 4. Rules for Templates
- All templates must be written in HTML.
- Templates must be placed inside the `templates/` directory.
- Templates should extend a base template (e.g., `base.html`).
- Template variable names must be descriptive and use `snake_case`.
- Use Django template tags and filters appropriately; avoid inline Python logic.

## 5. Rules for URLs
- Every route must be mapped to a view in the `urls.py` file.
- Use the `path()` function for URL routing.
- All routes must have descriptive names using the `name` argument in `path()` (e.g., `path('dashboard/', views.DashboardView.as_view(), name='dashboard')`).
- URL patterns must be defined in their respective `app_name/urls.py` file and included in the project's `urls.py`.

## 6. Rules for Static and Media Files
- Static files (CSS, JS, images) must be placed inside the `static/` directory.
- Media files (uploads) must be placed inside the `media/` directory.
- Use Django’s `{% static %}` and `{% media %}` template tags to reference files.

## 7. Rules for Forms
- Use Django’s built-in form classes (e.g., `forms.ModelForm`) for validation and processing.
- All form fields must be explicitly defined in the form class.
  
## 8. Rules for Migrations
- Migrations should be run and committed every time a model is changed.
- Always ensure migrations are synced between team members before deploying to production.



