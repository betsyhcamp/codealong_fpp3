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
# * If there's no data available or the data available isn't relevant to the forecasts, **qualitative forecasting** must be done. This is more than guesswork and structured approaches are possible.
# * **Quantitative forecasting** using statistical approaches can be employed when two conditions are met;
#     1. Numerical information about the past is available
#     2. It is reasonable to assume that some aspects of the past patterns will continue into the future.
# * Many time series forecasting methods available often developed with a specific purpose. Each methods had pros/cons.
# * A **time series** is anything that is observed sequentially over time. These observations may be at regular time intervals or at irregular time intervals (will only cover regular time intervals in this book)
#

# %%
