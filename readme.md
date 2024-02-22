# Flask exercises

This project was made to support tutorials and talks about introducing html templates rendering with Flask.

# Pipenv

To run the project, you can first load the pip env

```
pipenv shell
```

To exit from virtual environment:

```
deactivate
```

# Run

Inside the virtual environment, you can run your project:

```
flask run
```

# Use

Then visit http://127.0.0.1:5000/home

# Concepts

To understand the concepts presented on the code:

## Basic returning (no rendering template)

/examplePage

It is not rendering any html template

## Rendering with parameters

/page1/<username>

Basic html renerization sending one parameter from URL

Same concept than /hello/<user_id> but, in this case, is hard returning, not rendering template.

## Macros

/people/<username> and /new_people/<username>

These pages are importing a macro created in an external .jinja2 file.

Using same code in different pages

## Extend pages

/home, /extendedPage and /form

All of them are pages extended base.html. They are using macros too.

## Forms

/form page is using native (not wtf) forms to work

## WTF forms

Pending