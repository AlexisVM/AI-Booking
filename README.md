# AI-Booking Using Linear Regression

## A Brief overview
When traveling, a main factor in hotel selection is the price, since it fluctuates and changes depending on different factors, but maily people do their comparisons between other hotels in the area to obtain the price, and that is not the reality. Price depends on the room, the service, the attention, the location, the amenities and other factors that people usually doesn't consider and that represent most of it.

To successfully know how the price of a hotel will behave based on it's characteristics, a model is missing to really find correlations that let to a proper result.

Many websites nowadays allow hotel comparison, but not many ones let the user know what to expect based on requested characteristics. With this approach the final user, aka. the traveler, will have an idea of what price to expect for a hotel based in data from other hotels in the region, other cities and with different characteristics.

Traveling, according to a study conducted by Tourism Review International, is an activity that brings an incredible amount of benefits to the traveler, including physical and emotional. The study mainly obtained that traveling was more important to people that travel more, and people than doesn't travel is mainly because of resources like time and money. This also tells us that the lack of visibility in the origin of prices cause that the people prefer to do other thing instead of traveling.

Many websites and applications are now very popular to compare prices between hotels, they use many complex algorithms to analyze prices published in different locations, filter data and give the final user the "best" result according to their requests, but this results really just compare known data, they doesn't predict or give relevant information to the user to make decisions.

When airbnb enter the lodging market, many people faced the problem that they didn't really knew how to set their prices, because they tried to compete with the houses around them without paying attention to other details, and the same occurs with hotels (but in a bigger scale). 

AI is present (or could be present) in many of the most common activities that we do in a daily basis, and that is because of everything we do, did or will do represents data, data that could be studied and create information that make Artificial Intelligence possible. 

AI in price forecasting is incredibly popular since recent years in many subjects, from food price prediction to stock market price prediction. Many frameworks exist to help in the development of  Artificial Intelligence models and they had made an amazing improvement in data analysis to make decisions.

Data analysis for predicting properties prices has also been popular since recent years. A model using an AI framework was created by Sayed Huzaif to analyze and predict prices in real estate and also will be used as base to this model, with the difference of the approach in the calculus.

## Dataset

The dataset is composed by 120 rows containing data from hotels in bosnia:
- ID
- Name of the hotel
- Price (In Bosnian currency)
- Hotel star rating
- Distance from the hotel to midtown
- Customer ratings
- Amount of rooms per booking
- Size of the room in square meters
- City where the hotel is located

With that information we can see relations between attributes to help obtain a proper price.

![Dataset](https://github.com/AlexisVM/AI-Booking/blob/main/Media/dataset.jpg)

## Model

When analizing the data by an initial visual representation, there are present some relations between the attributes, same that can help to get a result.

![Scatter plot](https://github.com/AlexisVM/AI-Booking/blob/main/Media/relations.jpg)
![Heatmap plot](https://github.com/AlexisVM/AI-Booking/blob/main/Media/heatmap.jpg)

The results are on the pdf document within this repo, the results demonstrate a solid model that can be used to obtain great results.

## Usage

To run the model clone the repo and follow some steps:

### Regression using a framework
1. Run the file `HotelPriceRegression.py` 
2. See the model results
3. Wait for an input field and enter requested data
4. See the final result using the model

### Manual regression
1. Run the file `HotelPriceManualRegression.py` 
2. See the model results
3. Wait for an input field and enter requested data
4. See the final result using the model

We use two models to compare a manual approach and one established by a framework.

> The characteristics for the data are the following
> - Hotel rating must be from 1 to 5
> - Distance from the hotel to midtown should be in meters
> - The rating from the customers can be obtained from rating agencies and must be from 1 to 10, if it uses another scale, a conversion should be done.
> - The size of the room must be in square meters


The final result will be a hotel's price prediction using the given attributes.
