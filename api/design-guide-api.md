
# Guide to Designing Data REST APIs

This guide provides best practices for designing delightful data REST APIs. It is provided by the [Alternative Data Council](https://www.siia.net/Divisions/FISD-Financial-Information-Services-Association/Programs/Alternative-Data-Council) 

It is aimed at data providers who want to delight their data consumer with a user-friendly interface to consume data such that their users can extract value from the information as efficiently as possible. The primary audience are api developers but this guide is also relevant for sales, product and legal & compliance teams.

## Why you should read this guide

This guide aims to address important user pain points and business goals.

* **pain points**: 
    * supplying and consuming data via apis is time-consuming and expensive
    * lack of clear guidelines to build and interact with data apis
    * lack of tools for making internal data easily but securely accessible to third parties
    * writing and reading api documentation is time-consuming and expensive

* **business goals**: 
    * shorten sales and onboarding cycles for exchanging data via rest apis
    * provide user-friendly guidelines and tools to build and interact with data apis 
    * improve documentation and getting started guides

## Why you should/should not build a data APIs

* alternatives: d6tpipe, crux, aws rds, snowlflake

* Why API vs db/files: a survey a data consumer showed 2/3 prefer having a data dump vs   
Return data in api vs return file link?  

Benefits of APIs vs db/flat files:  
* dynamic: Except for price, I would only expect to do incremental calls each day if my end user adds new bonds. Otherwise I would maintain the static data on my server for their existing portfolios.
* light-weight maintenance: prefer to use API calls to a database that I do not maintain. It is possible that the portfolio will become some large that I will need a copy of your whole database locally
* tracking access and usage: 
    * pricing: which user has access to what?
    * usage: allows usage-based pricing

Downsides of API
* difficult to download all data
* users get tracked: creates privacy issues
* schema-less by default: standard apis return json or csv which are difficult to onboard for consumers

* questions to ask:
Who is the end user?  
    * How want to query? Just filters or also calculations? Types of Queries -- Do you envision sending requests to the API to return data based on some filter (e.g. return Maturity Date for the bond with CUSIP 123456789)?  Or do you envision more complex requests that entail the system doing calculations and returning the results of the calculations?

* **tradeoffs**:
    * real-time vs delayed results: unlike rest apis, querying data apis can result in long load times. This often exceeds 30 sec maximum set by rest apis.
    * result format: schema-less eg csv or json vs schema-rich eg parquet

* **special considerations**
    * multi-product apis: often providers are offering multiple feeds
    * point-in-time data: data consumers want to avoid look-ahead bias
    * reference data: easily join data from different end points

## Help users learn how to use the API

Documentation is part of the product
Use Swagger if possible.  Excel data dictionaries for detailed insights.  Return the API schema when user want quick navigation on the fly

### API Documentation

swagger /docs endpoint

### Getting started resources

[Postman Collections](https://www.postman.com/collection/)

### Schema

/schema endpoint: returns schema
    product: for multi-product feeds
        [how granular will this be?]

Include brief field description in schema

### Data dictionary

[returned by api?]

### How to build documentation

[other api documentation tools]


## How users requests data

### Protecting data assets: authentication



### Versioning

* API version
* data/model version

### Parameters

POST, no GET

### Endpoints

#### Common Endpoints

/data/reference => request static reference data

    [multiple attributes each requiring a different query format…] => hierarchy: /data/reference/id/tickers

/data/latest => get latest data

    params
        id: security identifer 
            list of ids eg ['abc','def']   
            default: [bbg ticker]
        idtype: 'ticker', 'permid', 'figi'
        fields: data field requested, can be found in data dictionary
        product: optional for multi-product feeds

/data/history => get history

    params
        id: security identifer 
            list of ids eg ['abc','def']   
            default: [bbg ticker]
        idtype: 'ticker', 'permid', 'figi'
        dates:
            single date 
            date range  
            list of dates   
            [point in time] 
                default: rolling point in time
        fields: data field requested, can be found in data dictionary
        product: optional for multi-product feeds


#### Custom Endpoints

/data/[vendor-specific]/

    vendor-specific end points, primarily to speed up querying

    Do NOT create lots of endpoints each answering a mini use-case.   
    2 is the desired number of endpoints but allowing for vendor specific variations, try not to exceed 5



## How data should be structured

### Security identifiers

Tickers should be optional, figi or permid type stable ids should be the norm.

### Data Fields

use from data dictionary

### Security Identifiers


### Dates and Times

Use common date formats.  Return properly formatted timestamps with timezone

date formats: iso dates YYYY-MM-DD
fiscal quarter convention: F[N]QYYYY, C[N]QYYYY
fiscal/calendar year convention: CYYYY, FYYYY


## How data is returned to users

### Return data vs return link to data

For long-running queries, send link to where data will be

User needs to long-poll... while data is processing, need a way to check status of the running task

### Format

direct from api: csv vs json vs xml
delayed form link: parquet, csv

Do NOT put arbitrary limits to the user requests
If user wants large amounts of data, send a file instead. Limits should be mindfully designed to optimize performance for a common use case and explicitly communicated. 


## Handling Point-in-Time

PIT: need to address 2 dimensions, ie 4 choices         
        data-version    
    model-version       

## Python Implementation

d6tflow


## Managing Change

See FISD guilde on [Service Level and Communications](https://www.siia.net/Divisions/FISD-Financial-Information-Services-Association/Programs/Working-Groups/Service-Level-and-Communications)

## Additional Resources

* [Apigee Web API Design](https://cloud.google.com/files/apigee/apigee-web-api-design-the-missing-link-ebook.pdf)
* [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/)
* [Postman](https://www.postman.com/)
    * [Postman Collections](https://www.postman.com/collection/)
* [Swagger OpenAPI Specification](https://swagger.io/specification/)


