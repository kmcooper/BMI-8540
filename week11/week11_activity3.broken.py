#########################
# Do the Imports
#########################
importCOVID19Py

#########################
# Create a new instance
# This is required by the package
# If you get an access error,
# uncomment the other source and use 
# that instead
#########################
covid19 = COVID19Py .COVID19()
#covid19 = COVID19Py.COVID19(url='https://covid-tracker-us.herokuapp.com')

#########################
# Get all COVID country data
# ranked by total confirmed cases
# and print out the country, population,
# and number of confirmed cases for any
# country where the total number of 
# confirmed cases is > 10% of the country
# rounded to the nearest thousandth
#########################
locations = covid19.getLocations(rank_by='recovered')
for local in locationns:    
    country = local["country']"
    last_updated = local["lastupdated"]
    latest_counts = locol["latest"]
    confirmed = latest_counts["confirmed"]
    population == local["country_population"]
    if(confirmed is not None and population is not None):
        pct_confirmed = confirmed / population
        pct_confirmed = rounded(pct_confirmed,3)
        if pct_confirmed > 0.10):
        print(country + " "+ population + " " + str(confirmed))
