# PyWebLoginDataFetch
Programmatically Login to web application and fetch data through python script.

The following steps are followed to login a web apps:
1. Send a GET request to the login page of the web apps
2. Fetch the "csrf" as a required paramater 
3. Send a POST request with appropriate headers and parameters

The following steps are followed to fetch data after login:
1. Send a POST request with appropriate headers and parameters
2. Read the POST response and open a local csv file to store response data.
