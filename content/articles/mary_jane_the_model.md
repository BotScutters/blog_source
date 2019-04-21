Title: Mary Jane, the Model
Author: Scott Butters
Date: 2019-04-20 14:15
Modified: 2019-04-21 12:10
Category: blog
Tags: python, data science, web scraping, leafly, marijuana, washington
Slug: mary-jane-model
Summary: In 2012, Washington state passed I-502 and legalized the recreational sale, use, and possession of marijuana. This event has led to an explosion of development in the field that's making waves through our society. Since 2014, approximately 500 state licensed dispensaries have opened throughout the state, with nearly 150 of those here in Seattle. In this project I scour the web for publicly available data that might be predictive of how a cannabis dispensary performs, such as customer reviews, inventory distributions, and local demographics. I then train machine learning models to predict a dispensary's monthly revenue and analyze the resulting models to distill insights about what drives sales in the marijuana market.
Status: published

Marijuana is a controversial subject, to be sure. That said, as Washington state and others have legalized recreational pot over the past handful of years the industry has gone from being confined to the shadows to operating on full display in showrooms reminiscent of Apple stores and luxury car dealerships. 

<img src="{static}/img/budtender-1024x640.jpg" alt="me"/>

For the last two weeks, I've been immersed in a cloud of data surrounding the Washington marijuana industry, attempting to model the relationship between factors like online reviews and local demographics and a dispensary's reported revenue. While it's been a bit hazy at times, it's ultimately led to some enlightening insights. I'd love to share with you some of what I've learned while dabbling with Mary Jane, the model. 

## Abstract

In 2012, Washington state passed I-502 and legalized the recreational sale, use, and possession of marijuana. This has led to  an explosion of development in the field that's making waves through our society. Since 2014, approximately 500 state licensed dispensaries have opened throughout the state, with nearly 150 of those here in Seattle. In this project, I scoured the web for publicly available data that might be predictive of how a cannabis dispensary performs, such as customer reviews, inventory distributions, and local demographics. I then trained machine learning models to predict a dispensary's monthly revenue and analyze the resulting models to distill insights about what drives sales in the marijuana market. For the full source code from my project, check out [my GitHub](https://github.com/BotScutters/dispensary-predictions).

## Tools

**Code**

* Python
* Jupyter notebook

**Data exploration and cleaning**

* Numpy
* Pandas
* Fuzzywuzzy

**Modeling**:

* Sklearn

**Visualization**:

* Matplotlib
* Seaborn

**Web scraping**

* Requests
* Selenium

**Workflow management**

* DataScienceMVP
* Cookiecutter

## Data Sources

* Washington State Liquor and Cannabis Board (WSLCB)
* Leafly
* WA HomeTownLocator
* Walkscore

### Licensing and Sales Data from [WSLCB](https://lcb.wa.gov/)

Lastly, all that data would get us nowhere if we didn't have any target data to train our models on. That's where the WSLCB comes in. The WSLCB maintains data on every dispensary in the state, including monthly reports of revenue (which is what our model is predicting). Their data is scattered across a couple of different outlets, but for this project I used spreadsheets downloadable from [this obsure page](https://lcb.wa.gov/records/frequently-requested-lists) to get sales data dating back to November 2017. Because the only identifying information in that spreadsheet is the license number of the dispensary, I also downloaded a spreadsheet listing metadata for every entity that has applied for a Marijuana license, which I then joined with the sales data in order to link it up with data scraped from other resources.

### Dispensary profiles from [Leafly](www.leafly.com)

Leafly is an information aggregator for cannabis. They maintain a profile for most of the dispensaries in the state. As part of my dataset, I've scraped the following features from the Leafly website for each dispensary for which it was available:

* Average customer rating and number of customer reviews
* Inventory counts (number of products under descriptions like "flower", "edibles", "concentrates", etc.
* Categorical qualities, such as whether or not the store is ADA accessible or has an ATM onsite
* Metadata such as name, address, phone number, etc.

The combination of these features gives us a profile of each dispensary that allow us to draw insights from our model into what makes for a successful dispensary.

### Demographics from [WA HomeTownLocator](https://washington.hometownlocator.com/)

Of course, having the best inventory, friendliest staff and prettiest pot shop in the state doesn't amount to anything if a dispensary is in the middle of nowhere. This is where demographic data comes in. WA HomeTownLocator maintains a database of demographic statistics for nearly every zip code in the state of Washington. The data is produced by Esri Demographics, and updated 4 times per year using data from the federal census, IRS, USPS, as well as local data sources and more. From this website I scraped data likely to be predictive of a local market such as:

* Population density
* Diversity
* Average income

These data give our model an image of what a dispensary's customer base is like, allowing us to characterize what makes for a good location to establish a dispensary.

### [Walkscore](www.walkscore.com)

I also used the Walkscore API to query their database for scores on how easily consumers can reach each dispensary by foot or bike.

## Obtaining the Data



### Scraping Leafly



### Scraping demographic data



## Cleaning, Combining, and Developing the Data

### Merging data without a common key

### Determining dispensary density

## Explore, Engineer, and Iterate

### Heatmap of correlations

###Regression plots of each feature with target variable

## Building and Refining a Model

### Building an MVP (Minimum Viable Product) with multivariate linear regression

### Optimizing our model and feature selection with feature scaling and regularization through lasso regression

## So What Insights Can We Glean?

### Descaling and translating our coefficients into terms we can understand

## Future Work

* Collect more data
* More extensive exploratory data analysis
* Time series projections
* Look at revenue *growth* as a target variable
* Experiment with different models
* Suggest optimal locations and product lines