import numpy as np
import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

INTERVAL_1 = list(range(1961, 2006))
INTERVAL_2 = list(range(2006, 2016))

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a numpy 1-d array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]



"""
End helper code
"""

# Problem 1
import numpy as np

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    
    Args:
        x: a list or array-like with length N, representing the x-coords of N sample points
        y: a list or array-like with length N, representing the y-coords of N sample points
        degs: a list of integers, representing the degrees of the fitting polynomials
    
    Returns:
        A list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial.
    """
    models = []
    for deg in degs:
        # Fit a polynomial of degree 'deg' to the points (x, y)
        coeffs = np.polyfit(x, y, deg)
        models.append(coeffs)
    return models


# Problem 2
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: list or array-like with length N, representing the y-coords of N sample points
        estimated: list or array-like with length N, representing the estimated values by the regression model
    
    Returns:
        A float representing the R-squared error term.
    """
    # Calculate the mean of the actual y values
    mean_y = sum(y) / len(y)
    
    # Total sum of squares (variance of actual y values)
    total_variance = sum((yi - mean_y) ** 2 for yi in y)
    
    # Residual sum of squares (variance of the errors)
    residual_variance = sum((yi - esti) ** 2 for yi, esti in zip(y, estimated))
    
    # Calculate R-squared
    r2 = 1 - (residual_variance / total_variance)
    return r2


# Problem 3
def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-square for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.
    Args:
        x: a list of length N, representing the x-coords of N sample points
        y: a list of length N, representing the y-coords of N sample points
        models: a list containing the regression models you want to apply to
                your data. Each model is a numpy array storing the coefficients of
                a polynomial.
    Returns:
        None
    """
    x = np.array(x)
    y = np.array(y)
    
    for model in models:
        degree = len(model) - 1
        # Generate predictions
        predictions = np.polyval(model, x)
        
        # Compute R-squared value
        ss_total = np.sum((y - np.mean(y))**2)
        ss_residual = np.sum((y - predictions)**2)
        r_squared = 1 - (ss_residual / ss_total)
        
        # Calculate standard error of the slope for linear models
        if degree == 1:
            slope = model[0]
            residuals = y - predictions
            standard_error = np.sqrt(np.sum(residuals**2) / (len(x) - 2)) / np.sqrt(np.sum((x - np.mean(x))**2))
            print(f"Linear model: Slope = {slope}, Standard Error = {standard_error:.4f}")
        
        # Plot the data and the model
        pylab.figure()
        pylab.plot(x, y, 'bo', label='Data Points')  # Blue dots for data
        pylab.plot(x, predictions, 'r-', label=f'Degree {degree} Model')  # Red line for model
        pylab.xlabel('x')
        pylab.ylabel('y')
        pylab.title(f"Degree {degree} Model\nR-squared = {r_squared:.4f}")
        pylab.legend()
        pylab.show()



### Begining of program
raw_data = Climate('/workspaces/6.0002/edX/UNIT_4/problem_set_4/data.csv')

# Problem 3
y = []
x = INTERVAL_1
for year in INTERVAL_1:
    y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
models = generate_models(x, y, [1])
evaluate_models_on_training(x, y, models)


# Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
# MISSING LINES
models = generate_models(x, y, [1])    
evaluate_models_on_training(x, y, models)
