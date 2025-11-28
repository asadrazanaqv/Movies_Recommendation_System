# Movie Recommendation System

This is a **Movie Recommendation System** web app built using Python and Streamlit. The app recommends movies based on the similarity of movie titles and descriptions.

## Features

- Recommends movies based on user input.
- Uses **TF-IDF Vectorizer** and **Cosine Similarity** to find similar movies.
- Interactive web app built with **Streamlit**.
- Easy to run locally with pickle files.

## Technologies Used

- Python
- Streamlit
- Numpy
- Pandas
- Scikit-learn
- Pickle
- Requests

## How It Works

The app uses the following approach:

1. Movie data is loaded into a Pandas DataFrame.
2. Text features from the movies are transformed using **TfidfVectorizer**.
3. **Cosine Similarity** is computed to find similar movies.
4. When a user selects a movie, the app recommends similar movies based on the similarity scores.

## Important Notes

- The model's **similarity.pkl** file is large (over 100 MB), so it cannot be uploaded to GitHub directly.  
- To run this app on your local machine:

  1. Download the `Movie_Recommendation_System.ipynb` file.
  2. At the end of the notebook, the model and movie list are saved using pickle:

     ```python
     import pickle
     pickle.dump(similarity, open('similarity.pkl', 'wb'))
     pickle.dump(list_of_all_titles, open('movies_list.pkl', 'wb'))
     ```

  3. Make sure `similarity.pkl` and `movies_list.pkl` are in the same folder as the Streamlit app (`app.py` or `Movie_Recommendation_System.py`).
  4. Run the app locally:

     ```bash
     streamlit run Movie_Recommendation_System.py
     ```

- Once the pickle files are in place, the app will run smoothly and you can explore movie recommendations.

## Usage

1. Enter a movie title in the app.
2. Click on "Recommend".
3. See a list of recommended movies based on similarity.

---

This README ensures that anyone with the project files can set up and run the **Movie Recommendation System** locally even if the large pickle file is not uploaded to GitHub.
