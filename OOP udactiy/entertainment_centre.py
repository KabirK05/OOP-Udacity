import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy that comes to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")


menace_II_society = media.Movie("Menace II Society",
                                "A young hustler on the street searches for a way out of the temptations of the ghetto",
                                "https://m.media-amazon.com/images/M/MV5BNGE3MGI0MzItNjJjNC00ZTUzLTlmZTctOGUyMDllMWM2OTcxXkEyXkFqcGdeQXVyMjQ1MjYzOTQ@._V1_.jpg",
                                "https://www.youtube.com/watch?v=XrMCRkTRmiY")
print(menace_II_society.storyline)
menace_II_society.show_trailer()

school_of_rock = media.Movie("School of Rock", "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PSUJFEBC74")

ratatouille = media.Movie("Ratatouille", "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=C3SBBRXDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxVU")

hunger_games = media.Movie("Hunger Games", "Storyline",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PA63a7H0bo")
movies = [toy_story, avatar, menace_II_society, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
                                
                                
                               
