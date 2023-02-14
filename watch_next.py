# import spacy
import spacy

# load library
nlp = spacy.load("en_core_web_md")


# read movies file
movies = open("movies.txt", "r")
movies_read = movies.read()
# split each line
movies_read_list = movies_read.split("\n")
# remove empty string at the end of the list
movies_read_list.pop()
# split the movie titles from their descriptions
movie_descriptions = []
for movie in movies_read_list:
  a = movie.split(" :")
  movie_descriptions.append(a)


# create Hulk movie description
hulk_movie = ["Planet Hulk", "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."]
hulk_movie_nlp = nlp(hulk_movie[1])


# function to compare the Hulk movie to movies in the list
def watch_after_hulk():
  similarity_score1 = 0
  
  # iterate over the movie list to measure the similarity between each movie and the hulk movie
  for description in range(len(movie_descriptions)):
    description_nlp = nlp(movie_descriptions[description][1])
    title = movie_descriptions[description][0]
    similarity_score2 = hulk_movie_nlp.similarity(description_nlp)
    
    # if this iteration produces a higher similarity score, save the movie
    if similarity_score2 > similarity_score1:
      similarity_score1 = similarity_score2
      next_title = title
  
  print(f"As you've watched Planet Hulk, you might like {next_title}")

