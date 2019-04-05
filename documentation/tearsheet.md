# Dataset Documentation Guidelines - Dataset Tear Sheet

## Introduction

### Goals

* Guide vendors on how to describe their datasets at a high level
* Allow buyers to quickly understand and assess dataset
* Seller and buyer speak same language
    * Define common taxonomy 
    * Standardize naming and semantics of metadata fields
* Make description available in machine readable format
    * Enable better indexing on a data catalog
    * Make it easier to integrate data catalogs

### Target Users

* **Vendors**: produce marketing materials
* **Market places**: provide summary descriptions of vendors
* **Data management/scout teams**: maintain a data catalog
* **Data engineering teams**: build a data catalog  
* **Analysts / PMs**: decide if dataset relevant to investment process

### Design Principles

* Prioritize important attributes
* Be flexible and extendable for future new datasets
* Provided in human and machine readable format (HTML / PDF / JSON)

## Contents

### Table Of Contents

* Vendor
* Data
* Methodology
* Case Study
* Backtests
* Technical information
* Support information
* Contract and Trials
* Legal and compliance

### Vendor

* Vendor name:
* Vendor website:
* Attach pitch deck
* Principal vendor contact:
* Description of vendor:
* Value-add/uniqueness: [100 characters]

### Data

* Data Description: [100 characters]
* Asset class (circle one): Equity, commodity, Credit, Rates, FX, Real Estate, Crypto
* Geographic coverage: (country or region)
* Sector Coverage (use GICs L2/3):
* Stock coverage: give a number
* cap coverage: (small, mid, large)
* Style(dividend, earnings, emerging, equity, growth, leverage, liquidity, momentum, other, profit, quality, reversal, sentiment, size, smallcap, value, volatility, yield)

### Methodology

* How is data collected?
* How is data processed?
    * Ticker mapping?
    * Fiscal quarter mapping?
    * Taxonomy? Eg sector / country / kpi mapping?
* How long after data collection is data available to client:
* Point in Time or updated:
* Forecasts made?

### Case study

* Summarize common use cases
* 1 detailed case study (can be attached)
* List of additional case studies< repeats first point

### Backtests 
We tend to like to do our own so I don't think this is something we want
* Available: yes/no
* Type: kpis, forecasts, trading
* Methodology?
* Results?

### Technical 

* Delivery:
    * Location: SFTP/FTP,  S3, GCP, Azzure, API, Web UI, email, if API, state type of API (REST/POST etc)
    * Format: CSV, TSV, Excel, Parquet, JSON, pdf, other (state)
    * State of data on delivery: Raw, semi processed, processed, trading signal, alerts, GUI, reports, research analysts reports 
    * Authentiation: ????
* Historically consistency (Y/N), missing values (Y/N), methodology transparency (Y/N), outliers (Y/N), Mapped to financial instrument (Y/N), back tested (Y/N) < I think this is overkill?
    * Notes: 
* Historical size: << too hard to define, does it matter?
* Monthly size growth:
* History of data: (How many years back does it go + free text for notes)
* Frequency: observations | delivery ??

### Support
* support hours: 
* support timezones:
* support contact via email only or phone too?:
* Type of support provided: technical/business/investor
* SLA for delivery issues:
* SLA for outage:

### Contract and Trials

* Licensing structure: 
* Pricing model: flat annual, per user, by AUM
* Contract lengths
* Trial cost?:Y/N if Y how much?
* Trial time period: (1 week, 1 month, 2 months, 3 months, flexible)
* Other trial notes:

### Legal & Compliance

* NDA required? 
* PII level
* MNPI level
* Indemnification
* FISD standard contract compliant?
* What else?
