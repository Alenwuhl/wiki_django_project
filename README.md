# CS50W Wiki Project - Harvard University

## Project Overview

This project was developed as part of the **CS50 Web Programming with Python and JavaScript** course at Harvard University. The goal of this assignment is to create a **Wikipedia-like online encyclopedia** where users can view, search, create, and edit articles written in **Markdown**. The project involves the use of **Django**, a Python-based web framework, and focuses on implementing key functionalities required to build a fully functional, user-editable encyclopedia.

## Features

1. **Entry Page**:
   - Users can visit a URL corresponding to a specific article and view the contents of the article, which are stored in **Markdown** format. The contents are converted to **HTML** before rendering the page.
   - If an article does not exist, an error page is displayed to the user.

2. **Index Page**:
   - The homepage lists all available encyclopedia entries. Each entry name is clickable and redirects the user to the corresponding article page.

3. **Search Functionality**:
   - Users can search for encyclopedia entries.
   - If the search query matches exactly with an entry title, the user is redirected to that entry.
   - If the query does not match any title exactly, the user is shown a list of articles that contain the search term as a substring.

4. **Create New Page**:
   - Users can create a new encyclopedia entry by providing a title and writing content in **Markdown** format.
   - If an entry with the given title already exists, an error message is shown, and the user is prompted to choose a different title.

5. **Edit Page**:
   - Each article page contains an "Edit" button that allows users to modify the content of the entry.
   - The content is pre-filled in a form and editable in **Markdown** format. Upon submission, the updated content is saved, and the user is redirected back to the article page.

6. **Random Page**:
   - Users can click on a link to view a randomly selected article from the encyclopedia.

7. **Markdown to HTML Conversion**:
   - All encyclopedia articles are stored in **Markdown** format. Using the `markdown2` package, the Markdown content is converted into **HTML** for display.

## How to Run the Project

1. Clone this repository.
2. Install the required dependencies (Django, markdown2) by running:

   ```bash
   pip install -r requirements.txt
3. Run the Django development server:
   ```bash
   python3 manage.py runserver
4. Access the project on your browser at http://127.0.0.1:8000/.

## Video Demo
A video demonstrating the functionality of the project can be found here: 

## Acknowledgements
This project was completed as part of the CS50 Web Programming with Python and JavaScript course at Harvard University.

**Note:** This project is for educational purposes only, and its development follows the guidelines and requirements provided by the CS50W course.
