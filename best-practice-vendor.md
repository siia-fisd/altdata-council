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


