# Alternative Investment Data Standards

## Goals

The primary goal of establishing alternative data standards is to help drive the adoption of alternative data in the investment process and facilite growth of the industry as well as lowering cost for the benefit of end clients. Specifically this will be achieved by:

* unifying data pipeline management
* reduce time spent on data delivery and ingestion
* secure permissions management and authentication
* raising data quality standards
* increasing knowledge transfer between participants

## Principles

The industry is best served by having standards which are:

* open and shared, instead of proprietary and centralized
* community enabled, instead of relying on a single party
* developer friendly, instead of primarily for non-technical users

## Who benefits and how

From data consumer perspective:

* fundamental analyst: faster data insights, automate tasks, easier slice+dice
* fundamental pms: increased idea generation, scalability, data roi
* quantitative analyst / data scientist: better data quality, easier to assess predictive value and build strategies
* quantitative pm: reduced research time, increased data roi
* data engineering: cheaper, faster and better data pipelines
* IT: improved security and scalability

From data vendor perspective:

* C suite: happier clients, shorter sales cycle, secure distribution
* product manager: better user experience, usage analytics
* engineering: easier to build data pipelines, less infrastructure to manage

## Architecture

To achieve the standards goals, the following technology should be available to participants:

* Meta database: covering file attributes, column definitions and quality tests
* Authentication provider: defining data access permissions and providing authentication
* Knowledge base: containing answers/soutions to commonly asked questions/problems

Additionally, there should be open source tools for:

* data push and pull to/from various data sources
* data ingestion of varied data
* data quality testing
* data joining

## Data Vendor Best Practices

* enable data download without having to change firewall and proxy settings
	* enable http redirect
* provide data in machine readable format
* provide meta data that defines how data should be ingested
	* parquet files with built in schema
	* if schema changes, show which columns were added/removed/renamed
* store all historic predictions for point-in-time analysis
	* at minimum don't overwrite old data with current data
	* if methodology changes, keep old methodolgy data and provide
* provide pre-cleaned test data
* provide replicable case studies

[look at fds docs]

