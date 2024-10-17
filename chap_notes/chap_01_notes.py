# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Chapter 01: Getting Started
#
# ## 1.1 What can we forecast?
#
# * Forecasting is required in many situations but some things are easier to forecast than others.
# * Factors that influence the predictability of an event or quantity include:
#     - How well we understand the factors that contribute to it
#     - How much data is available
#     - How similar the future is to the past
#     - Whether the forecasts can affect the thing we are trying to forecast
#    
# * Good forecasts capture the actual patterns and relationships in the historical data but don't replicate historical events that will not occur again. 
# * Good forecasts are possible in a changing environment. 
#     - Forecasts rarely assume that environment is unchanging
#     - Good forecasts will capture the way in which the environment is changing. What is normally assumed is that the way the environment is changing will continue into the future. e.g. highly volative environment will continue to be highly volatile in the future.
#     
# * Many forecasting methods exist. Forecasting methods can be extremely simple such as the **naive forecast** or as complex as deep learning methods
#     - The Naive forecast uses the most recent observation as the forecast.
#     
# ## 1.2 Forecasting, goals, planning
# * Forecasting is often confused with goals and planning in a business setting.
# * **Forecasting** is predicting the future given all the information available whereas **goals** are what we would like to have happen. Lastly, **planning** is a response to forecasts and goals.
# * Businesses and organizations need to have forecasts at a variety of time horizons:
#     - Short-term forecasts: Forecasts over a short time horizon (~1 month or less) are needed to schedule personel, production, and the placement of inventory.
#     - Medium-term forecasts: Needed to determine future resource requirements (>1 month to ~1 year)
#     - Long-term forecasts: Long time horizon of >1 year needed for strategic planning.
#
# ## 1.3 Determining what to forecast
# * Key things to determine at the beginning of a forecasting project
#     - what should be forecasted (e.g. every product line, or groups of products?)
#     - need to determine the forecasting horizon (how many time steps in the future need to be predicted)
#     - how often do the forecasts need to be produced (refreshed)
# * Spend time talking with the people who will be using the forecasts to make sure you understand their needs
#
# ## 1.4 Forecasting data and methods
# * Choice of the appropriate forecasting methods depends primarily on what data is available.
# * If there's no data available or the data available isn't relevant to the forecasts, **qualitative forecasting** must be done. This is more than guesswork and structured approaches are possible with well known methods.
# * **Quantitative forecasting** using statistical approaches can be employed when two conditions are met:
#     1. Numerical information about the past is available
#     2. It is reasonable to assume that some aspects of the past patterns will continue into the future.
# * Many time series forecasting methods available often developed with a specific purpose. Each methods had pros/cons.
# * A **time series** is anything that is observed sequentially over time. These observations may be at regular time intervals or at irregular time intervals (will only cover regular time intervals in this book)
# ### Predictor variables, model types, and time series forecasting
# * Some models use only the information in the times series itself and project the patterns in history into the future while other models may use additional predictors that explain the variation in history.
# * Two general extremes for model types (using electricity demand as the response variable as an example case):
#     1. Explanatory models: Uses additional variables that explain the variation in electricity demand but doesn't take into account the history of electricity demand. For example an explanatory model might be:
#     $$D = f(CurrentTemperature, StrengthOfEconomy, Population, TimeOfDay, DayOfWeek, Error) $$
# where the error term represents random variation as well the the effects of relevant variables not included in the model
#     2. Time series model: Uses history of the time series itself as a set of predictors to forecast the response variable, electricity demand, but does not include any additional external variables that may impact the system. For example:
#     $$D_{t+1}=f(D_t, D_{t-1}, D_{t-2}, D_{t-3}, ..., error)$$
#     where $t+1$ is one hour in the future, $t$ is the present hour, $t-1$ is the previous hour, $t-2$ is two hours ago, etc.
#     
# * Dynamic Regression models are models that incorporate features of both explanatory models and time series. Dynamic regression models are also called longitudinal models, or transfer function models. Related to Dynamic Regression models are Distributed Lag regression models that only include lag. Example of Dynamic Regression model:
#     $$D_{t+1}=f(D_t, CurrentTemperature, TimeOfDay, DayOfWeek, error)$$
#     
# ## 1.5, 1.6 - no notes since very high level remarks
#
# ## 1.7 The statistical forecasting perspective
# * The thing we are trying to forecast is unknown and can be considered as a random variable thus it could take a range of possible values
# * When we obtain a forecast, in most cases, we are estimating the middle of the distribution of possible values of the randome variable could take. Thus, we are estimating the expected value of the random variable.
#     * This forecasted value which is the expected value of the forecast distribution is the **point forecast**
# * Often a prediction interval, a range of possible values about the point forecast, where the actual value will fall with a given level of confidence is provided along with the point forecast. 
#     * The width of the prediction interval reflects the uncertainty in the forecasted value
#     * Typically, there is more uncertainty in the forecast as the time horizon increases. Thus, the width of the prediction interval typically increase with forecast horizon.
#     
