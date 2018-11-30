# Alternative Data Council

The ADC is a working group within the [FISD](
http://www.siia.net/Divisions/FISD-Financial-Information-Services-Association). We are focused on establishing best practices and standards for the delivery of alternative data to the investment industry.

## Goals

The primary goals of establishing alternative data standards is to:

* lower cost for the benefit of end clients 
* facilitate growth of the industry
* drive adoption of alternative data in the investment process

Specifically this will be achieved by:

* improving data documentation
* raising data quality standards
* unifying data pipeline management
* reduce time spent on data delivery and ingestion
* easier permissions management and authentication

## Principles

The industry is best served by having standards which are:

* open and shared, instead of proprietary and centralized
* community enabled, instead of relying on a single party
* developer friendly, instead of primarily for non-technical users

## Who benefits and how?

From data consumer perspective:

* investors: reduced cost for investment management services
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

## Who participates?

Initially the working group will consist of mostly buy-side institutions. Membership will then be extended to sell-side institutions and data vendors.

## What do the standards cover?

To achieve the goals, the following should be available:

* **Vendor best practices**: guiding vendors on how to best deliver data
* **Documentation standards**: consistent data documentation, similar to [API Blueprint](https://github.com/apiaryio/api-blueprint/blob/master/API%20Blueprint%20Specification.md#i-api-blueprint-language-1)
* **Data definition language**: covering data schema, file attributes and quality tests, similar to [Frictionless](https://frictionlessdata.io/specs/data-package/), [Intake](https://intake.readthedocs.io/en/latest/data-packages.html#defining-a-package), [Quilt](https://docs.quiltdata.com/api/buildyml)
* **Issue tracker**: transparent tracking of problems and improvement requests
* **Knowledge base**: containing answers/solutions (including code) to commonly asked questions/problems
* **Authentication provider**: defining data access permissions and providing authentication

## Tools

To help with adoption of standards, participants benefit from an ecosystem of tools and services compliant with the standards.

* [d6t-pyton](https://github.com/d6t/d6t-python): libraries for data ingestion and data pipes
* [intake](https://intake.readthedocs.io/en/latest): library for data packages
* [marbles](https://github.com/twosigma/marbles): library for data unit testing
* [Crux](https://www.cruxinformatics.com/): managed data operations service
* [BEAM](https://antenna.bamfunds.com/): common csv data evaluation

Other examples [Frictionless](https://frictionlessdata.io/software/), [API Blueprint](https://apiblueprint.org/tools.html).

## License and Access

Free and open sourced under the MIT license. The documents will be publicly accessible on Github and in FISD documents.

## Roadmap

TBD

## Procedures

TBD. Covering:

* how often to meet?
* who works on what?
* contributing, [RFC](https://github.com/apiaryio/api-blueprint-rfcs/blob/master/rfcs/0001-rfc-process.md), voting?
* [issue tracking](https://guides.github.com/features/issues/) and [enhancement requests](https://github.com/django/deps/blob/master/final/0001-dep-process.rst)?
