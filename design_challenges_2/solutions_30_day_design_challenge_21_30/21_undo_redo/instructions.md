## Parse dictionary response as custom object to simplify weather app code

While dictionaries are very useful data structures, their main drawback is that you need to know the exact
spelling of their keys to access their values. Automatic editor code completion features and direct overview of
their keys becomes somehow tricky, and you need to write more code in order to get the values you are actually 
looking for.


## Challenge

For this challenge, you will have to cast the api response of the OpenWeatherMap service into a custom object
so that you can simplify the code used to access the response data. You need to do it in the following fashion.
Assuming you have a response who looks like this:

`data = {
    'coord': {'lon': 5.25, 'lat': 52},
    'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}],
    'base': 'stations',
    'main': {'temp': 279.8, 'feels_like': 277.87, 'temp_min': 277.63, 'temp_max': 281.49, 'pressure': 1021, 'humidity': 73},
    'visibility': 10000,
    'wind': {'speed': 2.68, 'deg': 309, 'gust': 7.6},
    'clouds': {'all': 62},
    'dt': 1679914909,
    'sys': {'type': 2, 'id': 2009768, 'country': 'NL', 'sunrise': 1679894779, 'sunset': 1679940148},
    'timezone': 7200,
    'id': 2745909,
    'name': 'Provincie Utrecht',
    'cod': 200
}`

The object should be able to access every value as an attribute. For example, if you want to access the temperature 
value you should use `object_name.main.temp`etc. 

HINT: Dataclasses can be quite useful in this process.

## Solution (this should be sent afterwards with your explanation video (if applicable)

To achieve this we created a function `dict_to_dataclass` that creates a dataclass automatically from a dictionary.
We then create subclasses for every nested dictionary and list inside the response dictionary,
that we define the key names as attributes with their respective types. 

As long as this is done the only thing we need to change in our app code is to simply create an
extra function `convert_forecast_to_custom_object` in the `WeatherApi` class that passes the response 
dictionary to the `dict_to_dataclass` function, which returns the object that contains all the dictionary values
as attributes. 

- Notice, how this could have been done in one function, the already existing `get_complete_forecast` method of the 
`WeatherApi` class but for demonstration purposes we do it in a separate one.

We can then simplify both the `WeatherApi` and the `WeatherService` classes by removing the `get_current_temperature`, 
`get_current_humidity` and `get_current_wind`. That is because now we don't need a 'wrapper' functions to 
get those values since we have the custom object. Notice how easier we can access those values in the 
`run.py` script. Plus, we don't have to be aware of the data that is accessible since it can all be explored, by
accessing the members of the custom object we created (aka using the '.') 

One last advantage is that the mapping of the data into classes allows faster understanding of the data
structures and types of the original response itself. In addition, if the api service changes the data structure
of the response, we can very easily change the code to adapt to it. With the previous approach that would be
way more cumbersome.










