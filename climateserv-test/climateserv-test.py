import climateserv.api

GeometryCoords = [[-16.85, 13.85], [-16.85, 13.05], [-13.78, 13.05], [-13.78, 13.85], [-16.85, 13.85]] # Gambia
                  
DatasetType = 'IMERG'
OperationType = 'Average'
EarliestDate = '01/01/2015'
LatestDate = '12/31/2022'
SeasonalEnsemble = '' # only used for Seasonal_Forecast
SeasonalVariable = '' # only used for Seasonal_Forecast
Outfile = 'climateserv-test/gambia-imerg-average.csv'

climateserv.api.request_data(DatasetType, OperationType, 
             EarliestDate, LatestDate,GeometryCoords, 
             SeasonalEnsemble, SeasonalVariable,Outfile)