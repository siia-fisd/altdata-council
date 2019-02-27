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

* Summary
* Case study
* Methodology
* Legal & Compliance
* Backtests
* Technical information

### Summary

* Vendor name
* Vendor contact
* Description: [100 characters]
* Value-add/uniqueness: [100 characters]
* Data source: [100 characters]
* Category: 
* Asset class: Equity, commodity, Credit, Rates, FX, Real Estate, Crypto
* Application: Macro, Sector specific, Stock specific, Risk indicator, Quant signal
* Coverage: Geographic, Asset Class, breadth
    * Stock coverage: Very high ( > 500), High ( > 100), Middle ( > 20), Low (<=20)
* Delivery: Raw, semi processed, processed, trading signal, alerts, GUI, reports, research analysts
* Support: technical, analysts, research
* History: [Notes: 100 characters]
* Frequency: observations | delivery 
* Licensing structure: 
* Pricing model: flat annual, per user, by AUM

### Case study

* Summarize common use cases
* 1 detailed case study
* List of additional case studies

### Methodology

* How is data collected?
* How is data processed?
    * Ticker mapping?
    * Fiscal quarter mapping?
    * Taxonomy? Eg sector / country / kpi mapping?
* Forecasts made?

### Legal & Compliance

* Trial policy: length? paid? NDA required?
* PII level
* Indemnification
* FISD standard contract compliant?
* What else?

### Backtests 

* Available: yes/no
* Type: kpis, forecasts, trading
* Methodology?
* Results?

### Technical 

* Delivery:
    * Location: SFTP/FTP,  S3, API, Web UI, email
    * Format: CSV, Excel, Parquet, JSON
    * Authentiation: 
* Historically consistency (Y/N), missing values (Y/N), methodology transparency (Y/N), outliers (Y/N), Mapped to financial instrument (Y/N), back tested (Y/N)
    * Notes: 
* Historical size:
* Monthly size growth:
* Outages / recovery: Any delivery failures? How were they addressed?
