# Movie Recommendation System

This Django project is a movie recommendation system that suggests movies to users based on their preferences and viewing history. It leverages collaborative filtering and content-based filtering techniques to provide personalized recommendations, aligning with the growing demand for AI-driven personalization in the entertainment industry (as highlighted in the IBM job description for "Student Data and AI Developer").

## Features

*   **User Profiles:** Users can create profiles to track their movie ratings and watch history.
*   **Movie Database:** The system includes a database of movies with details like title, genre, director, actors, and plot summaries.
*   **Recommendation Algorithms:**
    *   **Collaborative Filtering:** Recommends movies based on the ratings of similar users.
    *   **Content-Based Filtering:** Recommends movies based on the characteristics of movies a user has previously rated highly.
*   **Search and Filtering:** Users can search for movies by title, genre, or actor.
*   **Ratings and Reviews:** Users can rate and review movies.
*   **User Interface:** A user-friendly interface for browsing movies, viewing recommendations, and managing profiles.

## Technologies Used

*   **Django:** A high-level Python web framework for rapid development and clean design.
*   **Python:** A versatile programming language widely used in data science and machine learning.
*   **PostgreSQL:** A powerful open-source relational database management system.
*   **HTML, CSS, JavaScript:** Front-end technologies for building the user interface.
*   **Scikit-learn (Optional):** A machine learning library for implementing recommendation algorithms.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone [invalid URL removed]
    ```

2.  **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up the database:**
    *   Create a PostgreSQL database.
    *   Update the `DATABASES` settings in `settings.py` with your database credentials.
    ```bash
    python manage.py migrate
    ```
5.  **Load initial movie data (Optional):**
    You can use a script to load movie data into the database.
    ```bash
    python manage.py loaddata movies.json 
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License.
