# CHANGELOG - Scylla

## Unreleased

***Added***:

* Add new ScyllaDB metrics ([#15592](https://github.com/DataDog/integrations-core/pull/15592))

***Fixed***:

* Update datadog-checks-base dependency version to 32.6.0 ([#15604](https://github.com/DataDog/integrations-core/pull/15604))
* Add config for new metrics groups ([#15614](https://github.com/DataDog/integrations-core/pull/15614))

## 2.4.0 / 2023-08-10

***Added***:

* Update generated config models ([#15212](https://github.com/DataDog/integrations-core/pull/15212))

***Fixed***:

* Fix types for generated config models ([#15334](https://github.com/DataDog/integrations-core/pull/15334))

## 2.3.1 / 2023-07-10

***Fixed***:

* Bump Python version from py3.8 to py3.9 ([#14701](https://github.com/DataDog/integrations-core/pull/14701))

## 2.3.0 / 2022-09-16 / Agent 7.40.0

***Added***:

* Update HTTP config spec templates ([#12890](https://github.com/DataDog/integrations-core/pull/12890))

## 2.2.0 / 2022-05-15 / Agent 7.37.0

***Added***:

* Support dynamic bearer tokens (Bound Service Account Token Volume) ([#11915](https://github.com/DataDog/integrations-core/pull/11915))

## 2.1.0 / 2022-04-05 / Agent 7.36.0

***Added***:

* Add metric_patterns options to filter all metric submission by a list of regexes ([#11695](https://github.com/DataDog/integrations-core/pull/11695))

***Fixed***:

* Remove outdated warning in the description for the `tls_ignore_warning` option ([#11591](https://github.com/DataDog/integrations-core/pull/11591))

## 2.0.0 / 2022-02-19 / Agent 7.35.0

***Changed***:

* Add tls_protocols_allowed option documentation ([#11251](https://github.com/DataDog/integrations-core/pull/11251))

***Added***:

* Add `pyproject.toml` file ([#11429](https://github.com/DataDog/integrations-core/pull/11429))

***Fixed***:

* Fix namespace packaging on Python 2 ([#11532](https://github.com/DataDog/integrations-core/pull/11532))

## 1.6.3 / 2022-01-21 / Agent 7.34.0

***Fixed***:

* Fix license header dates in autogenerated files ([#11187](https://github.com/DataDog/integrations-core/pull/11187))

## 1.6.2 / 2022-01-18

***Fixed***:

* Fix the type of `bearer_token_auth` ([#11144](https://github.com/DataDog/integrations-core/pull/11144))

## 1.6.1 / 2022-01-08

***Fixed***:

* Add comment to autogenerated model files ([#10945](https://github.com/DataDog/integrations-core/pull/10945))

## 1.6.0 / 2021-11-13 / Agent 7.33.0

***Added***:

* Document new include_labels option ([#10617](https://github.com/DataDog/integrations-core/pull/10617))
* Document new use_process_start_time option ([#10601](https://github.com/DataDog/integrations-core/pull/10601))

## 1.5.0 / 2021-10-04 / Agent 7.32.0

***Added***:

* Add HTTP option to control the size of streaming responses ([#10183](https://github.com/DataDog/integrations-core/pull/10183))
* Add runtime configuration validation ([#8982](https://github.com/DataDog/integrations-core/pull/8982))
* Add allow_redirect option ([#10160](https://github.com/DataDog/integrations-core/pull/10160))

***Fixed***:

* Fix the description of the `allow_redirects` HTTP option ([#10195](https://github.com/DataDog/integrations-core/pull/10195))

## 1.4.0 / 2021-05-28 / Agent 7.29.0

***Added***:

* Support "ignore_tags" configuration ([#9392](https://github.com/DataDog/integrations-core/pull/9392))

## 1.3.2 / 2021-03-07 / Agent 7.27.0

***Fixed***:

* Fix logs section placement in example config ([#8605](https://github.com/DataDog/integrations-core/pull/8605))

## 1.3.1 / 2021-01-25 / Agent 7.26.0

***Fixed***:

* Update prometheus_metrics_prefix documentation ([#8236](https://github.com/DataDog/integrations-core/pull/8236))

## 1.3.0 / 2020-10-31 / Agent 7.24.0

***Added***:

* Sync openmetrics config specs with new option ignore_metrics_by_labels ([#7823](https://github.com/DataDog/integrations-core/pull/7823))
* Add ability to dynamically get authentication information ([#7660](https://github.com/DataDog/integrations-core/pull/7660))
* Add config spec ([#7735](https://github.com/DataDog/integrations-core/pull/7735))

## 1.2.1 / 2020-09-21 / Agent 7.23.0

***Fixed***:

* Fix style for the latest release of Black ([#7438](https://github.com/DataDog/integrations-core/pull/7438))

## 1.2.0 / 2020-06-29 / Agent 7.21.0

***Added***:

* Add note about warning concurrency ([#6967](https://github.com/DataDog/integrations-core/pull/6967))

## 1.1.0 / 2020-05-17 / Agent 7.20.0

***Added***:

* Allow optional dependency installation for all checks ([#6589](https://github.com/DataDog/integrations-core/pull/6589))

## 1.0.3 / 2020-04-04 / Agent 7.19.0

***Fixed***:

* Remove logs sourcecategory ([#6121](https://github.com/DataDog/integrations-core/pull/6121))

## 1.0.2 / 2020-02-26 / Agent 7.18.0

***Fixed***:

* Fix discrepancies in `batchlog_manager`, `execution_stages`, `io_queue` and `query_processor` metric group names ([#5885](https://github.com/DataDog/integrations-core/pull/5885))

## 1.0.1 / 2020-02-25

***Fixed***:

* Fix typo in explicit send_histograms_buckets option ([#5867](https://github.com/DataDog/integrations-core/pull/5867))

## 1.0.0 / 2020-02-21

***Added***:

* Scylla new integration ([#5440](https://github.com/DataDog/integrations-core/pull/5440))