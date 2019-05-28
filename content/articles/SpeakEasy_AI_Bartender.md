Title: Speakeasy, the AI Bartender
Author: Scott Butters
Date: 2019-05-27 17:00
Modified: 2019-05-27 17:00
Category: blog
Tags: Python, Data Science, NLP, SVD, LSA, Cocktails, Recommender, Flask, App, Robots, AI, The Singularity
Slug: Speakeasy-AI-Bartender
Summary: You know that thing where you're hanging out in a schmancy speakeasy and the bartender asks you what you'd like to have—not in terms of a specific cocktail, or even the base spirit, but in terms of the flavor profile? And then just sets to work grabbing one bottle after another until before you know it you've got a little bit of magic in your mouth and you don't even know how? That. That right there is the epitome of mixology, as far as I'm concerned. That's "[the speakeasy experience](http://speakeasy-ai-bartender.herokuapp.com/)." That's what I've sought to recreate with this app.
Status: published

You know that thing where you're hanging out in a schmancy speakeasy and the bartender asks you what you'd like to have—not in terms of a specific cocktail, or even the base spirit, but in terms of the flavor profile? And then just sets to work grabbing one bottle after another until before you know it you've got a little bit of magic in your mouth and you don't even know how? That. That right there is the epitome of mixology, as far as I'm concerned. That's "[the speakeasy experience](http://speakeasy-ai-bartender.herokuapp.com/)." That's what I've sought to recreate with this app.

<figure>
  <img src="{static}/img/bar.jpg" alt="speakeasy-bar" style="width:100%">
  <figcaption>My home bar, soon to be tended by my personal AI assistant.</figcaption>
</figure>

# Abstract

[The SpeakEasy app](http://speakeasy-ai-bartender.herokuapp.com/) is a cocktail recommendation engine that's built to transform plain English requests from a user into a suggested cocktail that best matches the request. The functionality of this system rests on three systems:

* A database of cocktails, containing recipes, descriptions, and metadata for each.
* A model trained to vectorize and transform text describing a cocktail into an appropriate topic space.
* An app that uses the model trained on the cocktail database to make new predictions based on user's request.

The first production version of the app is making use of cocktail data scraped from [Difford's Guide](https://www.diffordsguide.com/cocktails). The text data from each cocktail is processed into a document-term matrix using a TF-IDF vectorizer, then factored into a document (cocktail)-topic matrix using latent semantic analysis (LSA). Finally, the data, vectorizer and LSA transformation matrix are packaged into a Flask app and hosted on Heroku so all the world can get the drink they're itching for.

The code for both the [SpeakEasy modeling](https://github.com/BotScutters/SpeakEasy) and [SpeakEasy app](https://github.com/BotScutters/speakeasy-app) are available on my [GitHub](https://github.com/BotScutters).

# Data Sources

Data! As much as with any other project, building this app demonstrated to me the value of high quality data, though this time with a particular flavor. That is, I started out using a dataset of cocktail recipes that were mostly terrible concoctions of flavored vodka and fruit juice. As they say, garbage juice in, garbage juice out. It wasn't until late in the model development that I decided I really ought to revisit step one and collect all new data. More on that later. 

In principle, though, in order for the recommendation algorithm to make decent suggestions given a variety of input types (i.e. the user might ask for a type of cocktail ("Manhattan variation"), a taste profile ("sweet and sour"), a combination ("spicy margarita"), or really any other thing) I needed a data source with not just a large number of high quality drinks, but also a substantial amount of text dedicated to describing the various qualities of the cocktails.

## [Drizly](https://drizly.com/recipes#all-recipes)

They've got a decent collection of about 600 cocktails, mostly pretty well described. I actually started out working with this dataset as my primary source. It's got two main downfalls, though: the formatting is somewhat inconsistent, making it impractical to extract recipes in a meaningful way, and more importantly, the cocktail list is padded with recipes that I'll snobbishly call garbage juice and seemed to give SpeakEasy a bias towards suggesting drinks that might glow under a blacklight, give you cancer, or both. No thanks. 

## [Difford's Guide](https://www.diffordsguide.com/cocktails)

Difford's Guide was my gold mine. Every cocktail on the site has been sampled, reviewed and rated by Mr. Difford himself, and from what I can tell the man's got standards. The drinks are good and interesting, the descriptions are generally decent for a NLP analysis, the website is laid out in a way that's relatively easy to scrape—a beautifully balanced data source for what I was looking for in this project. But the garnish that really tied the site together was that the recipe ingredients are all presented with consistent units and in a table format, making it exceedingly easy to extract the information and process it on the modeling end. Standardized units are the things of an engineer's dreams!

## Future Data Sources

In the course of preparing this app I flagged a number of resources for cocktail recipes that would be fantastic to incorporate down the line. One of the biggest challenges in integrating them is simply the variations in website formatting and different types of available information (which could also be viewed as a strength, through a certain lens).

* [Kindred Cocktails](https://kindredcocktails.com/cocktail?scope=0) - a strong cocktail database with lots of metadata to back it up. I briefly spoke with Dan, their Chief Swizzlestick, about a collaboration, but that seems to have fizzled out for now. Nonetheless, they're doing great work. Perhaps a relationship will be rekindled when I pick this back up.
* [Spruce Eats](https://www.thespruceeats.com/a-to-z-cocktail-recipes-3962886) - They've got a strong showing of about 1000 cocktails with pretty verbose descriptions. Just a matter of doing the work to incorporate.
* [Imbibe + PDT Cocktails](https://docs.google.com/spreadsheets/d/1W59zl7F534rHhRhzxxAH0EMqbe4H7qGz646srCpRnXw/pub?single=true&gid=0&output=html) - a Reddit user put together this spreadsheet of cocktails. Lots of fantastic drinks, but sorely lacking in good descriptions. Would require a strong ingredient description library to cross reference and build-up the descriptions.

## Tools

##### Code

- Python
- Jupyter notebook

##### Data exploration and cleaning

- Regex
- Numpy
- Pandas

##### Feature Preparation and NLP Modeling

* Gensim Doc2Vec
* Sklearn
  * TfidfVectorizer
  * TruncatedSVD
  * cosine_similarity

##### Visualization

- Matplotlib
- Hvplot
- SkLearn TSNE

##### Workflow management

- DataScienceMVP
- Cookiecutter

## Data Acquisition

Scraping the cocktail data from Difford's Guide took two main steps: putting together a list of all of the cocktails I wanted to get data on (as well as URLs to each cocktail's page), and then actually going to the pages and getting the cocktail data.

### Getting the List of Cocktails

To get my list of cocktails to scrape, I made use of the advanced search feature of the site. I found that if I conducted an advanced search to show me all cocktails with a rating of 3 stars or higher (gotta set the bar somewhere…), the page returned a total of well over 4,000 cocktails spread across over 100 pages. After a bit of investigation, I found that the URL carried all of the parameters and sending them through an internal API, including an offset parameter indicating which page to load. Jackpot! I wrote a function that generated URLs for each page, then proceeded to pull the source html from each page using Python's requests library and then parse the html with BeautifulSoup to extract the names and URLs of all displayed cocktails.

Side note: an interesting hiccup I ran into while doing this is that I kept on coming up short of the expected number of cocktails I'd scrape from the page. After a bit of puzzling, I found that the cocktails were being displayed sorted by rating…but! Turns out that when cocktails had an identical rating, i.e. 100 different cocktails might have a 3.5 star rating, the order *within* that rating group is (apparently) random. What's worse, the order seems to be calculated on every page load, since duplicates were regularly found on the following page. I ended up resolving this by having the list render sorted by name rather than rating.

### Getting Data on Each Cocktail

I used two methods to get each individual cocktail's data. I started out by pulling the source html into BeautifulSoup and parsing it for various desired attributes, similar to above. However, one fun trick I employed was using the Pandas read_html function to do a lot of the parsing. The first table I pulled was the one containing each cocktail's recipe. I converted this directly into a DataFrame so I could easily extract different elements from the table, then converted the table *back* into html using the to_html function. With only a little bit of clean-up and modification, this table is what I ultimately fed directly into the app later on to show a user the recipe! The other table I pulled is what contained the bulk of the text I used for each cocktail, i.e. description, garnish, instructions, etc. Because each cocktail might actually have a different number of entries in the table, pulling the table wholesale like this made the process much simpler to parse.

## Data Preparation

Coming out of the acquisition stage I had all of my cocktail data effectively stored in JSON format. Before I could properly vectorize each cocktail, I needed to clean and combine the text for each cocktail into a single "document" or "bag of words". Basically what this meant was stepping through the data for each individual cocktail and appending all of the entries that seemed like they might be useful (descriptions, ingredients, etc.) into a single long string. Finally, I fed each string through a text cleaning function to remove extraneous html tags and unicode characters that managed to sneak their way in.

## Modeling: LSA or Doc2Vec?

Oh, I spent a long time on this one, and frankly, I bet I'll spend more, as there's still more data to add and more algorithms to try out. But as of this writing I can say that I have fiercely pitted latent semantic analysis (LSA) against a Doc2Vec embedding and thus far LSA is winning. I'll come back to this.

But from a high level, SpeakEasy behaves the same regardless of which method is in use:

To train the model:

1. Feed text from all cocktails in dataset into model and have model learn the overall vocabulary as well as various word frequencies within each cocktail description. The model is trained on this.
2. Convert text of each cocktail description into a numerical vector representation.

To make a suggestion:

1. Receive user input in the form of a string.
2. Using trained model, transform string into numerical vector.
3. Suggest cocktail exhibiting the highest cosine similarity to this new vector.

Note that this method is making the assumption that (a) training data is robust, and that (b) our user input text contains relevant words that were represented in the original data. A bit obvious, but significant. A nonsense request will yield a nonsense suggestion. A request for a rare ingredient or unusual descriptor may well fall on deaf ears and, again, yield a nonsense suggestion.

But now to the nitty gritty: how do we convert a string of text into numbers? The potential methods are many and the choice has a significant impact on what comes out the other side.

### Latent Semantic Analysis

There are two main steps for implementing LSA: converting the text data to a numerical representation using [Sklearn's term frequency-inverse document frequency (TF-IDF) vectorization](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html), and reducing the dimensionality of the newly created document-term matrix into a document-topic space using [Sklearn's TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html) function. This yields a topic-document matrix, which is what we ultimately compare the vector generated from user input against.

There are a few choices to be made in tuning this model. 

For the vectorizer, I'm pre-processing the text by stripping all unicode accents, lowercasing all uppercase characters, and removing stop words (common words that contribute no meaning, such as "the", "and", etc.). I'm also creating additional tokens by including in my document-term matrix not just individual words, but also bigrams (all sets of two consecutive words from the processed text). There certainly exist further steps I could take that may improve model performance even further, including: stemming or lemmatizing tokens down to base forms, adding to or modifying the stock stop words than come built in to the library, adjusting frequency thresholds for which words make it into the model, and experimenting further with which ngrams to include.

For the TruncatedSVD model, the primary choice to make was the number of vectors to reduce the document-term matrix down to. Evaluating this was tricky, but the method I ended up settling on was choosing a few test phrases to simulate user input and manually/subjectively measuring how good the suggestions were. Test phrases I tried were:

* "Give me something sweet and smoky, like a margarita with mezcal"
* "can you make me a bitter manhattan variation with fernet?"

From there I looked at the different drinks suggested depending on the number of dimensions I was reducing to, and what types of features appeared to be captured by the algorithm.

Ultimately what I found is that over approximately 100 dimensional vectors, though I was only capturing about 25% of the variance in the documents, there seemed to be diminishing returns and little change in the suggestions. I ended up settling at 128 dimensions per vector, though I fully expect that number to shift a bit as/when I add additional data to the model.

### Doc2Vec

[Doc2Vec](https://radimrehurek.com/gensim/models/doc2vec.html) is a paragraph embedding model built on top of Word2Vec to give a numeric representation of an entire paragraph based on a continuous-bag-of-words model and a skip gram model. Effectively, Doc2Vec extends the functionality of Word2Vec from looking just at individual words and the few that surround them to looking at all of the words that make up a document and then producing a vector representation of that entire document.

With this project, that means that Doc2Vec can potentially be a drop-in replacement for TF-IDF and Truncated SVD as described above. To train the model, we:

1. Preprocess each document, similar to how we did with LSA
2. Instantiate a model with some hyperparameters
3. Build a vocabulary of all tokens in document
4. Train model on corpus 

To make suggestions, we run the user input through the same processing engine, infer a vector for the new document, and return the cocktail with highest cosine similarity.

But, I hear you asking, *what about those hyperparameters?*

Ah yes, the hyperparameters.

So I wrote a grid search algorithm. Starting coarse and working my way toward an optimal configuration, I adjusted the values for number of dimensions per vector, number of epochs to train the model over, and the number of steps (epochs) to use for inferring the vector for test data. After much iteration, I landed on parameters of a vectorsize of 100, 400 epochs, and 3 steps. That should raise two big questions: wait, how'd you even decide what to call "good" in order to tune the model? And that aside, how'd you end up at 400 epochs when all the literature suggests you should be well below 100? 

I know. And it was a headache that I'm sure I'm not over with. But let's step through one at a time.

For measuring goodness of fit, I decided to test how well the model would do at matching the text description of a cocktail *to itself*. This is actually a pretty reasonable test with Doc2Vec, as the way it constructs the document vector is non-deterministic. That is to say, even after setting random seeds anywhere I could and even my Python hash seed, the model would *still* infer a different (albeit similar) document vector for each document every time I ran it through. Though in practice I won't be feeding long description documents into the model, in theory I do want it to be fit well enough that when making a cocktail suggestion based on a document the model has been trained on, the correct answer is at least *close* to the best match.

So that was my parameter. For every configuration of hyperparameters that I tested, I ran each cocktail through the prediction function and took the average of all the rankings where I found the cocktail the test description had come from to be the error I wanted to minimize. This harrowing journey brought me to the parameters mentioned above, at which each cocktail would *on average* be the predicted as the 6th best match with itself.

As for the parameters: from what I've reae about Doc2Vec, I expected epochs to be happier closer to 20, and that I shouldn't need to specify the steps parameter at all—but these made a huge difference in performance. The vector size actually ended up around a reasonable value. A theory I have for *why* the epochs seem so far off from what I'd expect is that my data may not actually fit the idea of a continuous bag of words all that well, given that adjacent words may sometimes be unrelated, if it's just a list of ingredients, and the topics jump around due to the way I combined the different fields from the website into a single document. Each document is not actually a continuous set of words so much as several groups of words bunched together.

### Comparing the Two Methods

Gripes about Doc2Vec parameters aside, how'd they perform? For a final test, I basically replicated the procedure I used to tune the LSA model (though in hindsight I really should have tried manually tuning the Doc2Vec model this way; in the future I will). When comparing the output of each model to the same input, it was clear that LSA made suggestions that were far more relevant to the input request than what Doc2Vec was spitting out. So disappointing.

## Packaging and Serving as an App

After finalizing the model I'd work with, it was time to package it all up and serve it in an app. To do this, I wrote an app using the Python's [Flask](http://flask.pocoo.org/) library along with Bootstrap for the templates and web styling and an API to pass the data back and forth between Javascript and Python. The app is now hosted [here](http://speakeasy-ai-bartender.herokuapp.com/) using [Heroku](www.heroku.com).

An interesting (and ongoing) challenge I ran into while deploying the app was due to the file size. The upon pickling, the LSA model ends up being well over 100 MB, meaning that it can't be stored to and pulled from Github like the rest of the app. I resolved this by storing all of my pickled model files on Amazon S3, and adding a step to the app's startup sequence to download all of the models from AWS. While technically I could get away with compressing the LSA model to under 100 MB and then unzipping it upon loading the program, I think I will stick with the S3 method, as this will allow me to scale my dataset larger in the future.

An additional problem, however, is that Heroku only grants 500 MB of RAM to an app unless you upgrade all the way to the third price tier. Not that that's an insane thing to do…but for a prototype? Not yet. So as of now, my app has been averaging a load of about 590 MB RAM, which means I'm receiving constant warnings that I'm above their threshhold. Fortunately, they're friendly enough to allow the app to keep running without erroring out completely. That said, I recognize SpeakEasy is in treacherous waters here and that I really ought to spend some time figuring out how to reduce the memory requirements of the app.

## Conclusion

I've been dreaming about this app for a long time, and it's been hard work and a ton of fun bringing it to fruition. But…is SpeakEasy done? If you haven't picked up on it by now: SpeakEasy is a work in progress. There are bugs, sure, and I can see some flaws in the first steps I took. But also, I've got a ton of ideas about how I want to *improve* SpeakEasy. On the laundry list:

* More data, always more data. Incorporate more cocktails from additional sources.
* Build a database of ingredients with descriptions of each of those. Cross-reference cocktail recipes with ingredient database to pad cocktail descriptions.
* Experiment with more methods of text preprocessing, primarily trying out stemming vs lemmatizing and doing some cross-sectional analysis to identify additional stop words to add. 
* An additional interesting approach could be taking the text input and actually padding it with synonyms of the entered words. Could help to handle words that are similar but still different. 
* Could also do some level of hierarchically classifying ingredients.
* Modeling methods! How well would the model perform if I used a probabilistic Latent Semantic Analysis (PSLA)? Or Latent Dirichlet Allocation (LDA) or Nonnegative Matrix Factorization (NMF)? What about going deeper down the embedding hole and trying lda2vec? Okay, but what if I go even deeper, all the way down the deep learning rabbit hole and implement some [neural net magickry as described in this paper](https://arxiv.org/pdf/1707.07435.pdf)? Okay, I'm done now. Except not, I'll definitely obviously try all of these just as soon as I find all the time. I want to, at least.
* Develop a better testing method for evaluating goodness of model fit. Because you know what didn't feel good? My testing method, both for tuning hyperparameters and choosing a model. A better method and more quantifiable scoring metric would do worlds of good. Ideas? Let's talk!
* Improve user interface of app. Currently it's not exactly reliable in terms of uptime, rendering on different devices, and even predictions. 
* Improve memory management of app. Even if I don't make drastic changes to the models, I could still switch to Gensim's implementation of Latent Semantic Indexing, which utilizes better memory management (constant size, not impacted by size of corpus) as well as the ability to update the model with streaming data (bonus!).
* Add logging for user requests and suggested matches (believe it or not, I'm not tracking you), and provide user with the ability to up or downvote the recommendation they received. Long term it would be awesome to incorporate that into the suggestions, but short term I could even use it for guiding choices about model development.
* Build sister app, the AI Budtender. I've already done a bunch of the legwork, as described in my previous blog about scraping dispensary data off of [Leafly.com](http://localhost:8000/articles/2019/04/29/scraping-leafy/). Extending the code I wrote there to get data on all of the different strains wouldn't be a very big stretch, and SpeakEasy would pretty happily train on that dataset without so much as a "No way, man." 
* Thirteenth but not last, INVENT COCKTAILS! This is the problem I'm most excited to work on, but it's…bigger. I want to develop the algorithm that won't just suggest a cocktail near to a description but actually invent the recipe that matches it best—and to it well. There are a lot of problems baked into that question, but man do I want to figure out how to answer them.
* This isn't over.

Thanks for reading and feel free to reach out with questions or comments!