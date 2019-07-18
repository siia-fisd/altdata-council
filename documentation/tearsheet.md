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
* Principal vendor contact:
* Description of vendor:
* Value-add/uniqueness: [100 characters]
   * Attach pitch deck

### Data

* Data Description: [100 characters]
* Metrics provided: 
    * Attach data dictionary if possible
 * Asset class (circle one): Equity, commodity, Credit, Rates, FX, Real Estate, Crypto
* Geographic coverage: (country or region)
* Sector Coverage (use GICs L2/3):
* Stock coverage: give a number
* Cap coverage: (small, mid, large)
* Style(dividend, earnings, emerging, equity, growth, leverage, liquidity, momentum, other, profit, quality, reversal, sentiment, size, smallcap, value, volatility, yield)
* Frequency: observations | delivery
* Delays: collection vs publication
* History of data: (How many years back does it go + free text for notes)
* Quality metrics: (eg panel size, number of sdks)

### Methodology

* How is data collected?
* How is data processed?
    * Ticker/entity mapping?
            * Security identifiers mapped to? (ISIN/CUSIP/SEDOL/Tickers)
    * Fiscal quarter mapping?
    * Taxonomy? Eg sector / country / kpi mapping?
* Point in Time: true or backfilled?
* Forecasts made?

### Case study

* Summarize common use cases
* 1 detailed case study (can be attached)

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
* Full size including history:
* Monthly size growth:

### Support
* support hours: 
* support timezones:
* support contact via email only or phone too?:
* Type of support provided: technical/business/investor
* SLA for delivery issues:
* SLA for outage:
* SLA for quality metrics:

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
