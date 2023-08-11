# CHANGELOG - Crio

## Unreleased

## 2.4.0 / 2023-08-10

***Added***:

* Update generated config models. See [#15212](https://github.com/DataDog/integrations-core/pull/15212).

***Fixed***:

* Fix types for generated config models. See [#15334](https://github.com/DataDog/integrations-core/pull/15334).

## 2.3.1 / 2023-07-10

***Fixed***:

* Bump Python version from py3.8 to py3.9. See [#14701](https://github.com/DataDog/integrations-core/pull/14701).

## 2.3.0 / 2022-09-16 / Agent 7.40.0

***Added***:

* Update HTTP config spec templates. See [#12890](https://github.com/DataDog/integrations-core/pull/12890).

## 2.2.0 / 2022-05-15 / Agent 7.37.0

***Added***:

* Support dynamic bearer tokens (Bound Service Account Token Volume). See [#11915](https://github.com/DataDog/integrations-core/pull/11915).

## 2.1.0 / 2022-04-05 / Agent 7.36.0

***Added***:

* Add metric_patterns options to filter all metric submission by a list of regexes. See [#11695](https://github.com/DataDog/integrations-core/pull/11695).

***Fixed***:

* Remove outdated warning in the description for the `tls_ignore_warning` option. See [#11591](https://github.com/DataDog/integrations-core/pull/11591).

## 2.0.0 / 2022-02-19 / Agent 7.35.0

***Changed***:

* Add tls_protocols_allowed option documentation. See [#11251](https://github.com/DataDog/integrations-core/pull/11251).

***Added***:

* Add `pyproject.toml` file. See [#11335](https://github.com/DataDog/integrations-core/pull/11335).

***Fixed***:

* Fix namespace packaging on Python 2. See [#11532](https://github.com/DataDog/integrations-core/pull/11532).

## 1.8.3 / 2022-01-21 / Agent 7.34.0

***Fixed***:

* Fix license header dates in autogenerated files. See [#11187](https://github.com/DataDog/integrations-core/pull/11187).

## 1.8.2 / 2022-01-18

***Fixed***:

* Fix the type of `bearer_token_auth`. See [#11144](https://github.com/DataDog/integrations-core/pull/11144).

## 1.8.1 / 2022-01-08

***Fixed***:

* Add comment to autogenerated model files. See [#10945](https://github.com/DataDog/integrations-core/pull/10945).

## 1.8.0 / 2021-11-13 / Agent 7.33.0

***Added***:

* Document new include_labels option. See [#10617](https://github.com/DataDog/integrations-core/pull/10617).
* Add runtime configuration validation. See [#8903](https://github.com/DataDog/integrations-core/pull/8903).

## 1.7.0 / 2021-10-04 / Agent 7.32.0

***Added***:

* Add HTTP option to control the size of streaming responses. See [#10183](https://github.com/DataDog/integrations-core/pull/10183).
* Add allow_redirect option. See [#10160](https://github.com/DataDog/integrations-core/pull/10160).

***Fixed***:

* Fix the description of the `allow_redirects` HTTP option. See [#10195](https://github.com/DataDog/integrations-core/pull/10195).

## 1.6.0 / 2021-05-28 / Agent 7.29.0

***Added***:

* Support "ignore_tags" configuration. See [#9392](https://github.com/DataDog/integrations-core/pull/9392).

## 1.5.1 / 2021-01-25 / Agent 7.26.0

***Fixed***:

* Update prometheus_metrics_prefix documentation. See [#8236](https://github.com/DataDog/integrations-core/pull/8236).

## 1.5.0 / 2020-10-31 / Agent 7.24.0

***Added***:

* Sync openmetrics config specs with new option ignore_metrics_by_labels. See [#7823](https://github.com/DataDog/integrations-core/pull/7823).
* Add config specs. See [#7848](https://github.com/DataDog/integrations-core/pull/7848).

## 1.4.0 / 2020-05-17 / Agent 7.20.0

***Added***:

* Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.3.2 / 2020-04-04 / Agent 7.19.0

***Fixed***:

* Update deprecated imports. See [#6088](https://github.com/DataDog/integrations-core/pull/6088).

## 1.3.1 / 2020-02-22 / Agent 7.18.0

***Fixed***:

* Fix metric validation. See [#5581](https://github.com/DataDog/integrations-core/pull/5581).

## 1.3.0 / 2020-01-13 / Agent 7.17.0

***Added***:

* Make OpenMetrics use the RequestsWrapper. See [#5414](https://github.com/DataDog/integrations-core/pull/5414).

## 1.2.0 / 2019-05-14 / Agent 6.12.0

***Added***:

* Adhere to code style. See [#3495](https://github.com/DataDog/integrations-core/pull/3495).

## 1.1.0 / 2019-01-04 / Agent 6.9.0

***Added***:

* Add nginx ingress controller integration. See [#2853][1].

## 1.0.0 / 2018-10-13 / Agent 6.6.0

***Added***:

* Add a CRI-O check. See [#2231][2].

[1]: https://github.com/DataDog/integrations-core/pull/2853
[2]: https://github.com/DataDog/integrations-core/pull/2231