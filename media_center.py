# coding=utf-8
import fresh_tomatoes
from media import Movie

# make instance of Movie class for "Mad Max" film
m_max = Movie(movie_title="Mad Max: Fury Road",
              movie_poster_image_url="https://upload.wikimedia.org"
                                     "/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
              movie_story_line="Following a nuclear holocaust, the world has"
                               " become a desert wasteland and civilization has"
                               " collapsed. Max Rockatansky, a survivor, is"
                               " captured by the War Boys, the army of the "
                               "tyrannical Immortan Joe, and taken to Joe's "
                               "Citadel. Designated a universal blood donor, "
                               "Max is imprisoned and used as a blood bag for a"
                               " sick War Boy called Nux. Meanwhile, Imperator "
                               "Furiosa, one of Joe's lieutenants, is sent in "
                               "her armoured semi-truck, the War Rig, to "
                               "collect gasoline. When she drives off-route, "
                               "Joe realizes that his five wives—women selected"
                               " for breeding—are missing. Joe leads his entire"
                               " army in pursuit of Furiosa, calling on the aid"
                               " of nearby Gas Town and the Bullet Farm.",
              movie_trailer_youtube_url="https://www.youtube.com/watch?v="
                                        "hEJnMQG9ev8")

# make instance of Movie class for "Once Upon a Time in America" film
once_in_america = Movie(movie_title="Once Upon a Time in America",
                        movie_poster_image_url="https://upload.wikimedia.org/"
                                               "wikipedia/en/d/d8/Once_Upon_A"
                                               "_Time_In_America1.jpg",
                        movie_story_line="The film explores themes of childhood"
                                         " friendships, love, lust, greed, "
                                         "betrayal, loss, broken relationships,"
                                         " and the rise of mobsters in American"
                                         " society.",
                        movie_trailer_youtube_url="https://www.youtube.com/"
                                                  "watch?v=mzhX2PD6Srw")

# inflate list by movie instances
movies = [m_max, once_in_america, ]

# invoke open_movies_page to start website
fresh_tomatoes.open_movies_page(movies)
