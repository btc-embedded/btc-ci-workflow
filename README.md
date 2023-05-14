![test_ec](https://github.com/thabok/btc-ci-workflow/actions/workflows/test_ec.yml/badge.svg)

---
title: BTC Embedded Platform - RESTful API documentation v23.1p0
language_tabs:
  - http: HTTP
language_clients:
  - shell: curl
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="btc-embedded-platform-restful-api-documentation">BTC Embedded Platform REST API v23.1p0</h1>

> Scroll down for code samples, example requests and responses.

Email: <a href="mailto:support@btc-embedded.com">Support</a> 

<h1 id="btc-embedded-platform-restful-api-documentation-back-to-back-tests">Back-to-Back tests</h1>

Create and retrieve Back-to-Back tests.

## getTestByUID

<a id="opIdgetTestByUID"></a>

> Code samples

```http
GET /ep/b2b/{b2b__uid} HTTP/1.1

Accept: application/json

```

`GET /ep/b2b/{b2b__uid}`

*Get a B2B test*

Get a Back-to-Back test with the provided UID.

<h3 id="gettestbyuid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|b2b-uid|path|string|true|The UID of the Back-to-Back test to be returned.|

> Example responses

> 200 Response

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL",
  "stimuliFolderUIDs": 231,
  "stimuliScopeUIDs": 231
}
```

> 404 Response

```
"No Back-to-Back tests were found."
```

<h3 id="gettestbyuid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[RestBackToBackTest](#schemarestbacktobacktest)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## changeComparisonVerdictStatus

<a id="opIdchangeComparisonVerdictStatus"></a>

> Code samples

```http
PATCH /ep/b2b/{b2b__uid} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`PATCH /ep/b2b/{b2b__uid}`

*Change a verdict status for a comparison*

Changes verdict status for a comparison. If accept is true, the comparison verdict status is changed from 'failed' to 'failed (accepted)'. If accept is false, the comparison verdict status is changed from 'failed (accepted)'to 'failed'.

> Body parameter

```json
{
  "comparisonUID": "a3v",
  "accept": false
}
```

<h3 id="changecomparisonverdictstatus-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|b2b-uid|path|string|true|The Back-to-Back test UID for which to change the comparison verdict.|
|body|body|[ComparisonAcceptanceData](#schemacomparisonacceptancedata)|true|Provide the comparison and the acceptance flag.|

> Example responses

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="changecomparisonverdictstatus-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="changecomparisonverdictstatus-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## executeBackToBackTestOnFolder

<a id="opIdexecuteBackToBackTestOnFolder"></a>

> Code samples

```http
POST /ep/folders/{folder__uid}/b2b HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/{folder__uid}/b2b`

*Create a B2B test on a folder*

<b>Long running task </b>Generates a Back-to-Back test on a given folder UID for the specified reference and comparison execution kinds. Optionally, the execution can be forced to simulate all contained requirements-based test cases/stimuli-vectors. Optionally, only stimuli vectors can be set to be executed if force execution is activated. Otherwise if there are requirements-based test cases with comparison verdicts, the verdicts will be deleted in order to run the Back-to-Back test.

> Body parameter

```json
{
  "refMode": "TL MIL",
  "compMode": "SIL",
  "forceExecute": false,
  "simulateStimuliVectorsOnly": false
}
```

<h3 id="executebacktobacktestonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The folder UID for which the Back-to-Back test is generated.|
|body|body|[BackToBackTestExecutionData](#schemabacktobacktestexecutiondata)|true|Provides the reference and comparison execution kinds for which the Back-to-Back test will be generated. Optionally, the execution can be forced to simulate all contained test cases/stimuli-vectors. Optionally, only stimuli vectors can be set to be executed if force execution is activated. Otherwise if there are Requirements-based Test Cases with comparison verdicts, the verdicts will be deleted in order to run the Back-to-Back test.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executebacktobacktestonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeBackToBackTestOnFolder

> Code samples

```http
POST /ep/folders/{folder__uid}/b2b HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/b2b`

The long running task status and result will be transmitted.

<h3 id="executebacktobacktestonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL",
  "stimuliFolderUIDs": 231,
  "stimuliScopeUIDs": 231
}
```

> 404 Response

```
"Job ID does not exist."
```

<h3 id="executebacktobacktestonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RestBackToBackTest](#schemarestbacktobacktest)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeBackToBackTestOnFolderList

<a id="opIdexecuteBackToBackTestOnFolderList"></a>

> Code samples

```http
POST /ep/folders/b2b HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/b2b`

*Create a B2B test on a list of folders*

<b>Long running task </b>Generates a Back-to-Back test on a given list of folder UIDs for the specified reference and comparison execution kinds. Optionally, the execution can be forced to simulate all contained requirements-based test cases/stimuli-vectors. Optionally, only stimuli vectors can be set to be executed if force execution is activated. Otherwise if there are requirements-based test cases with comparison verdicts, the verdicts will be deleted in order to run the Back-to-Back test.

> Body parameter

```json
{
  "refMode": "TL MIL",
  "compMode": "SIL",
  "forceExecute": false,
  "simulateStimuliVectorsOnly": false,
  "UIDs": "2UPb"
}
```

<h3 id="executebacktobacktestonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BackToBackTestExecutionSourceData](#schemabacktobacktestexecutionsourcedata)|true|Provides a list of folder UIDs, reference and comparison execution kinds for which the Back-to-Back test will be generated. Optionally, the execution can be forced to simulate all contained test cases/stimuli-vectors.Optionally, only stimuli vectors can be set to be executed if force execution is activated. Otherwise if there are requirements-based test cases with comparison verdicts, the verdicts will be deleted in order to run the Back-to-Back test.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executebacktobacktestonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeBackToBackTestOnFolderList

> Code samples

```http
POST /ep/folders/b2b HTTP/1.1

Accept: application/json

```

`POST /ep/folders/b2b`

The long running task status and result will be transmitted.

<h3 id="executebacktobacktestonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL",
  "stimuliFolderUIDs": 231,
  "stimuliScopeUIDs": 231
}
```

> 404 Response

```
"Job ID does not exist."
```

<h3 id="executebacktobacktestonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RestBackToBackTest](#schemarestbacktobacktest)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeBackToBackTestOnScope

<a id="opIdexecuteBackToBackTestOnScope"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/b2b HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/scopes/{scope__uid}/b2b`

*Create a B2B test on a scope*

<b>Long running task </b>Generates a Back-to-Back test on a given scope UID for the specified reference and comparison execution kinds. Optionally, the execution can be forced to simulate all contained requirements-based test cases/stimuli-vectors. Optionally, only stimuli vectors can be set to be executed if force execution is activated. Otherwise if there are requirements-based test cases with comparison verdicts, the verdicts will be deleted in order to run the Back-to-Back test.

> Body parameter

```json
{
  "refMode": "TL MIL",
  "compMode": "SIL",
  "forceExecute": false,
  "simulateStimuliVectorsOnly": false
}
```

<h3 id="executebacktobacktestonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The scope UID for which the Back-to-Back test is generated.|
|body|body|[BackToBackTestExecutionData](#schemabacktobacktestexecutiondata)|true|Provides the reference and comparison execution kinds for which the Back-to-Back test will be generated. Optionally, the execution can be forced to simulate all contained test cases/stimuli-vectors.Optionally, only stimuli vectors can be set to be executed if force execution is activated. Otherwise if there are requirements-based test cases with comparison verdicts, the verdicts will be deleted in order to run the Back-to-Back test.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executebacktobacktestonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeBackToBackTestOnScope

> Code samples

```http
POST /ep/scopes/{scope__uid}/b2b HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/b2b`

The long running task status and result will be transmitted.

<h3 id="executebacktobacktestonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL",
  "stimuliFolderUIDs": 231,
  "stimuliScopeUIDs": 231
}
```

> 404 Response

```
"Job ID does not exist."
```

<h3 id="executebacktobacktestonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RestBackToBackTest](#schemarestbacktobacktest)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeBackToBackTestOnScopeList

<a id="opIdexecuteBackToBackTestOnScopeList"></a>

> Code samples

```http
POST /ep/scopes/b2b HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/scopes/b2b`

*Create a B2B test on a list of scopes*

<b>Long running task </b>Generates a Back-to-Back test on a given list of scope UIDs for the specified reference and comparison execution kinds. Optionally, the execution can be forced to simulate all contained requirements-based test cases/stimuli-vectors. Optionally, only stimuli vectors can be set to be executed if force execution is activated. Otherwise if there are requirements-based test cases with comparison verdicts, the verdicts will be deleted in order to run the Back-to-Back test.

> Body parameter

```json
{
  "refMode": "TL MIL",
  "compMode": "SIL",
  "forceExecute": false,
  "simulateStimuliVectorsOnly": false,
  "UIDs": "2UPb"
}
```

<h3 id="executebacktobacktestonscopelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BackToBackTestExecutionSourceData](#schemabacktobacktestexecutionsourcedata)|true|Provides a list of scope UIDs, the reference and comparison execution kinds for which the Back-to-Back test will be generated. Optionally, the execution can be forced to simulate all contained test cases/stimuli-vectors.Optionally, only stimuli vectors can be set to be executed if force execution is activated. Otherwise if there are Requirements-based Test Cases with comparison verdicts, the verdicts will be deleted in order to run the Back-to-Back test.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executebacktobacktestonscopelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeBackToBackTestOnScopeList

> Code samples

```http
POST /ep/scopes/b2b HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/b2b`

The long running task status and result will be transmitted.

<h3 id="executebacktobacktestonscopelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL",
  "stimuliFolderUIDs": 231,
  "stimuliScopeUIDs": 231
}
```

> 404 Response

```
"Job ID does not exist."
```

<h3 id="executebacktobacktestonscopelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RestBackToBackTest](#schemarestbacktobacktest)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getAllTests

<a id="opIdgetAllTests"></a>

> Code samples

```http
GET /ep/b2b HTTP/1.1

Accept: application/json

```

`GET /ep/b2b`

*Get all B2B tests*

Get all Back-to-Back tests from active profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "referenceMode": "TL MIL",
    "comparisonMode": "SIL",
    "referenceFolderUIDs": 231,
    "comparisonFolderUID": "231",
    "executionDate": "10/15/20, 8:34 AM",
    "verdictStatus": "PASSED",
    "verdictState": "VALID",
    "failed": 4,
    "failedAccepted": 0,
    "passed": 21,
    "error": 0,
    "total": 25,
    "comparisons": [
      {
        "uid": "yak7s7",
        "name": "SV_ATG_26",
        "verdictStatus": "PASSED",
        "referenceExecutionRecordUID": "abs3",
        "comparisonExecutionRecordUID": "zz61",
        "comment": "<Comment text>"
      }
    ],
    "name": "TL MIL vs SIL",
    "stimuliFolderUIDs": 231,
    "stimuliScopeUIDs": 231
  }
]
```

> 404 Response

```
"No Back-to-Back tests were found."
```

<h3 id="getalltests-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getalltests-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RestBackToBackTest](#schemarestbacktobacktest)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» referenceMode|string|false|none|The reference execution config type.|
|» comparisonMode|string|false|none|The comparison execution config type.|
|» referenceFolderUIDs|[string]|false|none|Reference folder UIDs|
|» comparisonFolderUID|string|false|none|Comparison folder UID|
|» executionDate|string|false|none|Execution Date|
|» verdictStatus|string|false|none|The verdict status|
|» verdictState|string|false|none|Verdict State|
|» failed|integer(int32)|false|none|Number of failed comparisons.|
|» failedAccepted|integer(int32)|false|none|Number of failed accepted comparisons.|
|» passed|integer(int32)|false|none|Number of passed comparisons.|
|» error|integer(int32)|false|none|Number of comparisons with error.|
|» total|integer(int32)|false|none|Total number of comparisons.|
|» comparisons|[[RestComparison](#schemarestcomparison)]|false|none|[All comparisons.]|
|»» uid|string|false|read-only|The unique identifier (UID) of this object.|
|»» name|string|false|none|The name of Test Case / Stimuli Vector used in Comparison.|
|»» verdictStatus|string|false|none|The verdict status|
|»» referenceExecutionRecordUID|string|false|none|UID of reference execution record.|
|»» comparisonExecutionRecordUID|string|false|none|UID of compared to execution record.|
|»» comment|string|false|none|Added comment for Comparison.|
|» name|string|false|none|The name of the Back-To-Back Test.|
|» stimuliFolderUIDs|[string]|false|none|Folder UIDs for which Back-To-Back Test was generated.|
|» stimuliScopeUIDs|[string]|false|none|Scope UIDs for which Back-To-Back Test was generated.|

#### Enumerated Values

|Property|Value|
|---|---|
|verdictStatus|PASSED|
|verdictStatus|FAILED|
|verdictStatus|ERROR|
|verdictStatus|FAILED_ACCEPTED|
|verdictState|VALID|
|verdictState|OUTDATED_TOLERANCE_UPDATE|
|verdictState|OUTDATED_MISSING_EXECUTIONS|
|verdictStatus|PASSED|
|verdictStatus|FAILED|
|verdictStatus|ERROR|
|verdictStatus|FAILED_ACCEPTED|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-regression-test-reports">Regression Test Reports</h1>

Creates a Regression Test Report for a given Regression Test. Retrieves all existing Regression Test reports from the profile.

## createRegressionReport

<a id="opIdcreateRegressionReport"></a>

> Code samples

```http
POST /ep/regression-tests/{regression__test__uid}/regression-test-reports HTTP/1.1

Accept: application/json

```

`POST /ep/regression-tests/{regression__test__uid}/regression-test-reports`

*Create a report for a regression test*

Creates a Regression Test Report on a regression test.

<h3 id="createregressionreport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|regression-test-uid|path|string|true|The Regression test UID for which the Regression Report is created.|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 404 Response

```
"No Regression test was found for the given test UID."
```

<h3 id="createregressionreport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Report](#schemareport)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## getReports_1

<a id="opIdgetReports_1"></a>

> Code samples

```http
GET /ep/regression-test-reports HTTP/1.1

Accept: application/json

```

`GET /ep/regression-test-reports`

*Get all reports*

Retrieve all the Regression Test reports from the profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "reportName": "Report 9/27/20 07:43 AM",
    "reportType": "<Report Type>"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getreports_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getreports_1-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Report](#schemareport)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» reportName|string|false|none|Name of the report.|
|» reportType|string|false|none|Type of the report.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-regression-tests">Regression Tests</h1>

Creates regression tests.

## getTestByUID_1

<a id="opIdgetTestByUID_1"></a>

> Code samples

```http
GET /ep/regression-tests/{regression__test__uid} HTTP/1.1

Accept: application/json

```

`GET /ep/regression-tests/{regression__test__uid}`

*Get a test*

Get the Regression Test with the provided UID.

<h3 id="gettestbyuid_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|regression-test-uid|path|string|true|The UID of the Regression Test to be returned.|

> Example responses

> 200 Response

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL"
}
```

> 404 Response

```
"No regression tests were found."
```

<h3 id="gettestbyuid_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[RegressionTest](#schemaregressiontest)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## changeComparisonVerdictStatus_1

<a id="opIdchangeComparisonVerdictStatus_1"></a>

> Code samples

```http
PATCH /ep/regression-tests/{regression__test__uid} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`PATCH /ep/regression-tests/{regression__test__uid}`

*Update verdict status for a comparison*

Changes verdict status for a Comparison.If accept is true, the comparison verdict status is changed from 'failed' to 'failed (accepted)'. If accept is false, the comparison verdict status is changed from 'failed (accepted)'to 'failed'

> Body parameter

```json
{
  "comparisonUID": "a3v",
  "accept": false
}
```

<h3 id="changecomparisonverdictstatus_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|regression-test-uid|path|string|true|The Regression Test UID for which to change the Comparison verdict.|
|body|body|[ComparisonAcceptanceData](#schemacomparisonacceptancedata)|true|Provide the Comparison and the acceptance flag.|

> Example responses

> 400 Response

```
"No Regression Test was found for UID."
```

<h3 id="changecomparisonverdictstatus_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="changecomparisonverdictstatus_1-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## executeRegressionTestOnFolder

<a id="opIdexecuteRegressionTestOnFolder"></a>

> Code samples

```http
POST /ep/folders/{folder__uid}/regression-tests HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/{folder__uid}/regression-tests`

*Generate a test on a folder*

<b>Long running task </b>Generates a Regression Test on a given folder UID for the specified comparison execution kind. Optionally, the folder where to save the simulated execution records can be provided. If this property is not provided, the execution records are not saved.

> Body parameter

```json
{
  "compMode": "SIL",
  "compFolderUID": "asV1"
}
```

<h3 id="executeregressiontestonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The folder UID for which the Regression Test is generated.|
|body|body|[RegressionTestExecutionData](#schemaregressiontestexecutiondata)|true|Provides the comparison execution kind for which the Regression Test will be generated. Optionally, the folder where to save the simulated execution records can be provided. If this property is not provided, the execution records are not saved.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executeregressiontestonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRegressionTestOnFolder

> Code samples

```http
POST /ep/folders/{folder__uid}/regression-tests HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/regression-tests`

The long running task status and result will be transmitted.

<h3 id="executeregressiontestonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executeregressiontestonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RegressionTest](#schemaregressiontest)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not Acceptable|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeRegressionTestOnFolderList

<a id="opIdexecuteRegressionTestOnFolderList"></a>

> Code samples

```http
POST /ep/folders/regression-tests HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/regression-tests`

*Generate a test on a list of folders*

<b>Long running task </b>Generates a Regression Test on a given list of folder UIDs for the specified comparison execution kind. Optionally, the folder where to save the simulated execution records can be provided. If this property is not provided, the execution records are not saved.

> Body parameter

```json
{
  "compMode": "SIL",
  "compFolderUID": "asV1",
  "UIDs": "2UPb"
}
```

<h3 id="executeregressiontestonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RegressionTestExecutionSourceData](#schemaregressiontestexecutionsourcedata)|true|Provides a list of folder UIDs and the comparison execution kind for which the Regression Test will be generated. Optionally, the folder where to save the simulated execution records can be provided. If this property is not provided, the execution records are not saved.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executeregressiontestonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRegressionTestOnFolderList

> Code samples

```http
POST /ep/folders/regression-tests HTTP/1.1

Accept: application/json

```

`POST /ep/folders/regression-tests`

The long running task status and result will be transmitted.

<h3 id="executeregressiontestonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL"
}
```

> 404 Response

```
"Job ID does not exist."
```

<h3 id="executeregressiontestonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RegressionTest](#schemaregressiontest)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not Acceptable|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getAllTests_1

<a id="opIdgetAllTests_1"></a>

> Code samples

```http
GET /ep/regression-tests HTTP/1.1

Accept: application/json

```

`GET /ep/regression-tests`

*Get all tests*

Get all Regression Tests from active profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "referenceMode": "TL MIL",
    "comparisonMode": "SIL",
    "referenceFolderUIDs": 231,
    "comparisonFolderUID": "231",
    "executionDate": "10/15/20, 8:34 AM",
    "verdictStatus": "PASSED",
    "verdictState": "VALID",
    "failed": 4,
    "failedAccepted": 0,
    "passed": 21,
    "error": 0,
    "total": 25,
    "comparisons": [
      {
        "uid": "yak7s7",
        "name": "SV_ATG_26",
        "verdictStatus": "PASSED",
        "referenceExecutionRecordUID": "abs3",
        "comparisonExecutionRecordUID": "zz61",
        "comment": "<Comment text>"
      }
    ],
    "name": "TL MIL vs SIL"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getalltests_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getalltests_1-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RegressionTest](#schemaregressiontest)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» referenceMode|string|false|none|The reference execution config type.|
|» comparisonMode|string|false|none|The comparison execution config type.|
|» referenceFolderUIDs|[string]|false|none|Reference folder UIDs|
|» comparisonFolderUID|string|false|none|Comparison folder UID|
|» executionDate|string|false|none|Execution Date|
|» verdictStatus|string|false|none|The verdict status|
|» verdictState|string|false|none|Verdict State|
|» failed|integer(int32)|false|none|Number of failed comparisons.|
|» failedAccepted|integer(int32)|false|none|Number of failed accepted comparisons.|
|» passed|integer(int32)|false|none|Number of passed comparisons.|
|» error|integer(int32)|false|none|Number of comparisons with error.|
|» total|integer(int32)|false|none|Total number of comparisons.|
|» comparisons|[[RestComparison](#schemarestcomparison)]|false|none|[All comparisons.]|
|»» uid|string|false|read-only|The unique identifier (UID) of this object.|
|»» name|string|false|none|The name of Test Case / Stimuli Vector used in Comparison.|
|»» verdictStatus|string|false|none|The verdict status|
|»» referenceExecutionRecordUID|string|false|none|UID of reference execution record.|
|»» comparisonExecutionRecordUID|string|false|none|UID of compared to execution record.|
|»» comment|string|false|none|Added comment for Comparison.|
|» name|string|false|none|The name of the RegresionTest Test.|

#### Enumerated Values

|Property|Value|
|---|---|
|verdictStatus|PASSED|
|verdictStatus|FAILED|
|verdictStatus|ERROR|
|verdictStatus|FAILED_ACCEPTED|
|verdictState|VALID|
|verdictState|OUTDATED_TOLERANCE_UPDATE|
|verdictState|OUTDATED_MISSING_EXECUTIONS|
|verdictStatus|PASSED|
|verdictStatus|FAILED|
|verdictStatus|ERROR|
|verdictStatus|FAILED_ACCEPTED|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-stimuli-vectors">Stimuli Vectors</h1>

Handle stimuli vectors.

## getStimuliVectorByUID

<a id="opIdgetStimuliVectorByUID"></a>

> Code samples

```http
GET /ep/stimuli-vectors/{stimuli__vector__uid} HTTP/1.1

Accept: application/json

```

`GET /ep/stimuli-vectors/{stimuli__vector__uid}`

*Get a stimuli vector*

Get a specific stimuli vector by UID.

<h3 id="getstimulivectorbyuid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|stimuli-vector-uid|path|string|true|The UID of the stimuli vector to be returned.|

> Example responses

> 200 Response

```json
{
  "uid": "yak7s7",
  "name": "ExampleName",
  "length": 42,
  "folderUID": "12",
  "scopeUID": "24a"
}
```

> 404 Response

```
"No stimuli vector was found."
```

<h3 id="getstimulivectorbyuid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[B2BStimuliVector](#schemab2bstimulivector)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## deleteStimuliVector

<a id="opIddeleteStimuliVector"></a>

> Code samples

```http
DELETE /ep/stimuli-vectors/{stimuli__vector__uid} HTTP/1.1

Accept: text/plain

```

`DELETE /ep/stimuli-vectors/{stimuli__vector__uid}`

*Delete a stimuli vector*

Delete a stimuli vector by its UID.

<h3 id="deletestimulivector-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|stimuli-vector-uid|path|string|true|The UID of the stimuli vector to be deleted.|

> Example responses

> 404 Response

```
"No stimuli vector was found. UID = {VALUE}"
```

<h3 id="deletestimulivector-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## exportStimuliVectors

<a id="opIdexportStimuliVectors"></a>

> Code samples

```http
POST /ep/stimuli-vectors-export HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/stimuli-vectors-export`

*Export Stimuli Vectors*

<b>Long running task</b> Export single or multiple Stimuli Vector(s) by providing the list of the stimuli vectors which will be exported, the export directory, the export format and a list of additional options for export.

> Body parameter

```json
{
  "UIDs": "2UPb",
  "exportDirectory": "C:/RestProfiles/VectorExport",
  "exportFormat": "EXCEL",
  "additionalOptions": {
    "csvDelimiter": "SEMICOLON",
    "singleFile": true,
    "architectureUid": "2Ai7"
  },
  "overwritePolicy": "OVERWRITE"
}
```

<h3 id="exportstimulivectors-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RestStimuliVectorExportInfo](#schemareststimulivectorexportinfo)|true|All necessary information for exporting a stimuli vectors.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exportstimulivectors-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="exportstimulivectors-responseschema">Response Schema</h3>

### Callbacks

#### Progress

**/ep/progress**

## exportStimuliVectors

> Code samples

```http
POST /ep/stimuli-vectors-export HTTP/1.1

Accept: application/json

```

`POST /ep/stimuli-vectors-export`

The long running task status and result will be transmitted.

<h3 id="exportstimulivectors-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "exportStatus": [
    {
      "name": "Artifact_1_2",
      "uid": "2my",
      "warnings": "{Cause}",
      "errors": "Export failed for file {file location}. {Cause}."
    }
  ]
}
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exportstimulivectors-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[ExportResult](#schemaexportresult)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getStimuliVectors

<a id="opIdgetStimuliVectors"></a>

> Code samples

```http
GET /ep/stimuli-vectors HTTP/1.1

Accept: application/json

```

`GET /ep/stimuli-vectors`

*Get all stimuli vectors*

Get all stimuli vectors.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "ExampleName",
    "length": 42,
    "folderUID": "12",
    "scopeUID": "24a"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getstimulivectors-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getstimulivectors-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[B2BStimuliVector](#schemab2bstimulivector)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|false|none|The name of the StimuliVector.|
|» length|integer(int64)|false|none|The length of the vector.|
|» folderUID|string|false|none|The unique identifier of the folder the StimuliVector belongs to.|
|» scopeUID|string|false|none|The unique identifier of the scope the StimuliVector belongs to.|

<aside class="success">
This operation does not require authentication
</aside>

## importStimuliVectors

<a id="opIdimportStimuliVectors"></a>

> Code samples

```http
PUT /ep/stimuli-vectors HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`PUT /ep/stimuli-vectors`

*Import stimuli vectors*

<b>Long running task</b> Import multiple stimuli vectors from external files into a Folder by providing their path and the Folders UID. Can either overwrite or skip stimuli vectors that are already imported.

> Body parameter

```json
{
  "paths": [
    "C:/RestProfiles/VectorExport/stimVetor.csv"
  ],
  "vectorKind": "TC",
  "folderUID": "13",
  "delimiter": "SEMICOLON",
  "overwritePolicy": "SKIP"
}
```

<h3 id="importstimulivectors-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RestStimuliVectorImportInfo](#schemareststimulivectorimportinfo)|true|All necessary information for importing a stimuli vector into the EP.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"The request cannot be processed. Please verify that the provided input has a valid format."
```

<h3 id="importstimulivectors-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## importStimuliVectors

> Code samples

```http
PUT /ep/stimuli-vectors HTTP/1.1

Accept: application/json

```

`PUT /ep/stimuli-vectors`

The long running task status and result will be transmitted.

<h3 id="importstimulivectors-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "importStatus": [
    {
      "UIDs": "15Lx",
      "warnings": "Undefined value detected for signal {signal name}. A default value will be set.",
      "errors": "Invalid format in file {file location}. {Cause}."
    }
  ]
}
```

> 400 Response

```
"File {NAME} can't be imported. {CAUSE}"
```

<h3 id="importstimulivectors-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[ImportResult](#schemaimportresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getStimuliVectorsFromFolder

<a id="opIdgetStimuliVectorsFromFolder"></a>

> Code samples

```http
GET /ep/folders/{folder__uid}/stimuli-vectors HTTP/1.1

Accept: application/json

```

`GET /ep/folders/{folder__uid}/stimuli-vectors`

*Get all stimuli vectors from a folder*

Get all stimuli vectors from the specified folder.

<h3 id="getstimulivectorsfromfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The UID of the folder from which to get stimuli vectors.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "ExampleName",
    "length": 42,
    "folderUID": "12",
    "scopeUID": "24a"
  }
]
```

> 404 Response

```
"No stimuli vectors were found."
```

<h3 id="getstimulivectorsfromfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getstimulivectorsfromfolder-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[B2BStimuliVector](#schemab2bstimulivector)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|false|none|The name of the StimuliVector.|
|» length|integer(int64)|false|none|The length of the vector.|
|» folderUID|string|false|none|The unique identifier of the folder the StimuliVector belongs to.|
|» scopeUID|string|false|none|The unique identifier of the scope the StimuliVector belongs to.|

<aside class="success">
This operation does not require authentication
</aside>

## getStimuliVectorsFromScope

<a id="opIdgetStimuliVectorsFromScope"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/stimuli-vectors HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/stimuli-vectors`

*Get all stimuli vectors from a scope*

Get all stimuli vectors from the specified scope.

<h3 id="getstimulivectorsfromscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope from which to get stimuli vectors.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "ExampleName",
    "length": 42,
    "folderUID": "12",
    "scopeUID": "24a"
  }
]
```

> 404 Response

```
"No stimuli vectors were found."
```

<h3 id="getstimulivectorsfromscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getstimulivectorsfromscope-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[B2BStimuliVector](#schemab2bstimulivector)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|false|none|The name of the StimuliVector.|
|» length|integer(int64)|false|none|The length of the vector.|
|» folderUID|string|false|none|The unique identifier of the folder the StimuliVector belongs to.|
|» scopeUID|string|false|none|The unique identifier of the scope the StimuliVector belongs to.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-tolerances">Tolerances</h1>

Import, reset and retrieve global and local tolerances.

## exportGlobalTolerances

<a id="opIdexportGlobalTolerances"></a>

> Code samples

```http
POST /ep/profiles/export-global-tolerances HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/profiles/export-global-tolerances`

*Export global tolerances*

Use this command to export the global tolerances per usecase.

> Body parameter

```json
{
  "path": "C:/Rest/tolerances.xml",
  "toleranceUseCase": "RBT"
}
```

<h3 id="exportglobaltolerances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TolerancesIOConfig](#schematolerancesioconfig)|true|All necessary information for exporting tolerances.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"The request cannot be processed. Please verify that the provided input has a valid format."
```

<h3 id="exportglobaltolerances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## exportGlobalTolerances

> Code samples

```http
POST /ep/profiles/export-global-tolerances HTTP/1.1

Accept: text/plain

```

`POST /ep/profiles/export-global-tolerances`

The long running task status and result will be transmitted.

<h3 id="exportglobaltolerances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 400 Response

```
"The request cannot be processed. Invalid value 'X' provided for enumeration 'toleranceUseCase'."
```

<h3 id="exportglobaltolerances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Exported. When the long running task is finished, the operation result will be available.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getGlobalTolerances

<a id="opIdgetGlobalTolerances"></a>

> Code samples

```http
GET /ep/scopes/{scope__id}/global-tolerances?kind=RBT HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__id}/global-tolerances`

*Get the global tolerances*

Use this command to retrieve the global tolerances. A valid scope uid and use case must be specified. The lead-lag-unit can be either Seconds or Steps.

<h3 id="getglobaltolerances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-id|path|string|true|The scope from which to retrieve the global tolerances.|
|kind|query|string|true|The use case kind. Can be either RBT or B2B.|
|lead-lag-unit|query|string|false|For existing tolerances, lead and lag values should be displayed as either SECONDS or STEPS. Default is STEPS.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|kind|B2B|
|kind|RBT|
|lead-lag-unit|SECONDS|
|lead-lag-unit|STEPS|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "detection_endstop_bottom",
    "lead": "0.0",
    "lag": "0.0",
    "absTol": "0.0",
    "relTol": "1",
    "kind": "Local"
  }
]
```

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="getglobaltolerances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Global tolerances retrieved.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request.|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found.|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getglobaltolerances-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ToleranceDefinition](#schematolerancedefinition)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|false|none|none|
|» lead|string|false|none|none|
|» lag|string|false|none|none|
|» absTol|string|false|none|none|
|» relTol|string|false|none|none|
|» kind|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## setGlobalTolerances

<a id="opIdsetGlobalTolerances"></a>

> Code samples

```http
PUT /ep/profiles/global-tolerances HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`PUT /ep/profiles/global-tolerances`

*Import the global tolerances*

Use this command to import the global tolerances.

> Body parameter

```json
{
  "path": "C:/Rest/tolerances.xml",
  "toleranceUseCase": "RBT"
}
```

<h3 id="setglobaltolerances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TolerancesIOConfig](#schematolerancesioconfig)|true|All necessary information for importing tolerances.|

> Example responses

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="setglobaltolerances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Global tolerances imported.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request.|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## resetGlobalTolerances

<a id="opIdresetGlobalTolerances"></a>

> Code samples

```http
DELETE /ep/profiles/global-tolerances?kind=RBT HTTP/1.1

Accept: text/plain

```

`DELETE /ep/profiles/global-tolerances`

*Reset the global tolerances*

Use this command to reset the global tolerances for the profile.

<h3 id="resetglobaltolerances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|kind|query|string|true|The use case kind. Can be either RBT or B2B.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|kind|B2B|
|kind|RBT|

> Example responses

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="resetglobaltolerances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Global tolerances reset.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request.|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## getLocalTolerances

<a id="opIdgetLocalTolerances"></a>

> Code samples

```http
GET /ep/test-cases/{test__case__id}/local-tolerances HTTP/1.1

Accept: application/json

```

`GET /ep/test-cases/{test__case__id}/local-tolerances`

*Get the local tolerances*

Use this command to retrieve the local tolerances. A valid test case uid must be specified. The lead-lag-unit can be either Seconds or Steps. Setting the create-if-missing to true will create local tolerances from the global tolerances.

<h3 id="getlocaltolerances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|test-case-id|path|string|true|The UID of the test case for which local tolerances will be retrieved.|
|lead-lag-unit|query|string|false|For existing tolerances, lead and lag values should be displayed as either SECONDS or STEPS. Default is STEPS.|
|create-if-missing|query|boolean|false|If true, the local tolerances will be created if they do not exist yet. Default is: false.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|lead-lag-unit|SECONDS|
|lead-lag-unit|STEPS|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "detection_endstop_bottom",
    "lead": "0.0",
    "lag": "0.0",
    "absTol": "0.0",
    "relTol": "1",
    "kind": "Local"
  }
]
```

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="getlocaltolerances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Local tolerances retrieved.|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request.|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Test case not found.|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getlocaltolerances-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ToleranceDefinition](#schematolerancedefinition)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|false|none|none|
|» lead|string|false|none|none|
|» lag|string|false|none|none|
|» absTol|string|false|none|none|
|» relTol|string|false|none|none|
|» kind|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## importLocalTolerances

<a id="opIdimportLocalTolerances"></a>

> Code samples

```http
PUT /ep/test-cases/{test__case__id}/local-tolerances HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`PUT /ep/test-cases/{test__case__id}/local-tolerances`

*Import the local tolerances*

Import local tolerances for a given test case.

> Body parameter

```json
{
  "path": "C:/Rest/tolerances.xml"
}
```

<h3 id="importlocaltolerances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|test-case-id|path|string|true|The UID of the test case for which local tolerances will be imported.|
|body|body|[RBTTolerancesIOConfig](#schemarbttolerancesioconfig)|true|All necessary information for importing tolerances.|

> Example responses

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="importlocaltolerances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Local tolerances imported.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request.|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Test case not found.|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## exportLocalTolerances

<a id="opIdexportLocalTolerances"></a>

> Code samples

```http
POST /ep/test-cases/{test__case__id}/local-tolerances HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/test-cases/{test__case__id}/local-tolerances`

*Export local tolerances*

Export local tolerances for a given test case.

> Body parameter

```json
{
  "path": "C:/Rest/tolerances.xml"
}
```

<h3 id="exportlocaltolerances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|test-case-id|path|string|true|The UID of the requirement-based Test Case to export the local tolerances for.|
|body|body|[RBTTolerancesIOConfig](#schemarbttolerancesioconfig)|true|All necessary information for exporting tolerances.|

> Example responses

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="exportlocaltolerances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Local tolerances exported.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request.|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Test case not found.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## removeLocalTolerances

<a id="opIdremoveLocalTolerances"></a>

> Code samples

```http
DELETE /ep/test-cases/{test__case__id}/local-tolerances HTTP/1.1

Accept: text/plain

```

`DELETE /ep/test-cases/{test__case__id}/local-tolerances`

*Reset the local tolerances*

Remove the local tolerances for a test case.

<h3 id="removelocaltolerances-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|test-case-id|path|string|true|The UID of the test case for which local tolerances will be removed.|

> Example responses

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="removelocaltolerances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Local tolerances removed.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request.|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Test case not found.|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-requirement-based-test-execution-reports">Requirement-based Test Execution Reports</h1>

Creates requirement-based Test Execution Reports.

## createRBTExecutionReportOnFolder

<a id="opIdcreateRBTExecutionReportOnFolder"></a>

> Code samples

```http
POST /ep/folders/{folder__uid}/test-execution-reports-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/{folder__uid}/test-execution-reports-rbt`

*Create a report on a folder*

Create a requirement-based Test Execution Report on a given folder.

> Body parameter

```json
{
  "execConfigName": "TL MIL"
}
```

<h3 id="createrbtexecutionreportonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The folder UID for which the Test Execution Report is created.|
|body|body|[RBTExecutionReportCreationInfoData](#schemarbtexecutionreportcreationinfodata)|true|Provide the execution kind for which to create the Test Execution Report (example: SIL, TL MIL, SL MIL, etc.).|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createrbtexecutionreportonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createRBTExecutionReportOnFolder

> Code samples

```http
POST /ep/folders/{folder__uid}/test-execution-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/test-execution-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createrbtexecutionreportonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 404 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createrbtexecutionreportonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Report](#schemareport)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createRBTExecutionReportOnFolderList

<a id="opIdcreateRBTExecutionReportOnFolderList"></a>

> Code samples

```http
POST /ep/folders/test-execution-reports-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/test-execution-reports-rbt`

*Create a report on a list of folders*

Create a requirement-based Test Execution Report on a given list of folders.

> Body parameter

```json
{
  "execConfigName": "TL MIL",
  "UIDs": [
    "22a",
    "22c"
  ]
}
```

<h3 id="createrbtexecutionreportonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RBTExecutionReportCreationInfo](#schemarbtexecutionreportcreationinfo)|true|Provide the execution config name  (example: SIL, TL MIL, SL MIL, etc.) and the list of folder UIDs for which to create the Test Execution Report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createrbtexecutionreportonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createRBTExecutionReportOnFolderList

> Code samples

```http
POST /ep/folders/test-execution-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/folders/test-execution-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createrbtexecutionreportonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createrbtexecutionreportonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createRBTExecutionReportOnRequirementsSource

<a id="opIdcreateRBTExecutionReportOnRequirementsSource"></a>

> Code samples

```http
POST /ep/requirements-sources/{requirements__source__uid}/test-execution-reports-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/requirements-sources/{requirements__source__uid}/test-execution-reports-rbt`

*Create a report on a requirements source*

Create a requirement-based Test Execution Report on a given requirements source.

> Body parameter

```json
{
  "execConfigName": "TL MIL"
}
```

<h3 id="createrbtexecutionreportonrequirementssource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|requirements-source-uid|path|string|true|The requirements source UID for which the Test Execution Report is created.|
|body|body|[RBTExecutionReportCreationInfoData](#schemarbtexecutionreportcreationinfodata)|true|Provide the execution kind for which to create the Test Execution Report  (example: SIL, TL MIL, SL MIL, etc.).|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createrbtexecutionreportonrequirementssource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createRBTExecutionReportOnRequirementsSource

> Code samples

```http
POST /ep/requirements-sources/{requirements__source__uid}/test-execution-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/requirements-sources/{requirements__source__uid}/test-execution-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createrbtexecutionreportonrequirementssource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 404 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createrbtexecutionreportonrequirementssource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Report](#schemareport)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createRBTExecutionReportOnRequirementsSourceList

<a id="opIdcreateRBTExecutionReportOnRequirementsSourceList"></a>

> Code samples

```http
POST /ep/requirements-sources/test-execution-reports-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/requirements-sources/test-execution-reports-rbt`

*Create a report on a list of requirements sources*

Create a requirement-based Test Execution Report on a given list of requirements sources.

> Body parameter

```json
{
  "execConfigName": "TL MIL",
  "UIDs": [
    "22a",
    "22c"
  ]
}
```

<h3 id="createrbtexecutionreportonrequirementssourcelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RBTExecutionReportCreationInfo](#schemarbtexecutionreportcreationinfo)|true|Provide the execution kind  (example: SIL, TL MIL, SL MIL, etc.) and list of requirements sources UIDs for which to create the Test Execution Report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createrbtexecutionreportonrequirementssourcelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createRBTExecutionReportOnRequirementsSourceList

> Code samples

```http
POST /ep/requirements-sources/test-execution-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/requirements-sources/test-execution-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createrbtexecutionreportonrequirementssourcelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createrbtexecutionreportonrequirementssourcelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createRBTExecutionReportOnScope

<a id="opIdcreateRBTExecutionReportOnScope"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/test-execution-reports-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/scopes/{scope__uid}/test-execution-reports-rbt`

*Create a report on a scope*

Create a requirement-based Test Execution Report on a given scope.

> Body parameter

```json
{
  "execConfigName": "TL MIL"
}
```

<h3 id="createrbtexecutionreportonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The Scope UID for which the Test Execution Report is created.|
|body|body|[RBTExecutionReportCreationInfoData](#schemarbtexecutionreportcreationinfodata)|true|Provide the execution kind for which to create the Test Execution Report  (example: SIL, TL MIL, SL MIL, etc.).|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createrbtexecutionreportonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createRBTExecutionReportOnScope

> Code samples

```http
POST /ep/scopes/{scope__uid}/test-execution-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/test-execution-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createrbtexecutionreportonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"No scope was found for scope UID {scopeUID}."
```

<h3 id="createrbtexecutionreportonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Not found|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createRBTExecutionReportOnScopeList

<a id="opIdcreateRBTExecutionReportOnScopeList"></a>

> Code samples

```http
POST /ep/scopes/test-execution-reports-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/scopes/test-execution-reports-rbt`

*Create a report on a list of scopes*

Create a requirement-based Test Execution Report on a given list of scopes.

> Body parameter

```json
{
  "execConfigName": "TL MIL",
  "UIDs": [
    "22a",
    "22c"
  ]
}
```

<h3 id="createrbtexecutionreportonscopelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RBTExecutionReportCreationInfo](#schemarbtexecutionreportcreationinfo)|true|Provide the execution config name  (example: SIL, TL MIL, SL MIL, etc.) and the list of scope UIDs for which to create the Test Execution Report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createrbtexecutionreportonscopelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createRBTExecutionReportOnScopeList

> Code samples

```http
POST /ep/scopes/test-execution-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/test-execution-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createrbtexecutionreportonscopelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createrbtexecutionreportonscopelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getReports_2

<a id="opIdgetReports_2"></a>

> Code samples

```http
GET /ep/test-execution-reports-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/test-execution-reports-rbt`

*Get all reports*

Retrieve all the requirement-based Test Execution reports from the profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "reportName": "Report 9/27/20 07:43 AM",
    "reportType": "<Report Type>"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getreports_2-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getreports_2-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Report](#schemareport)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» reportName|string|false|none|Name of the report.|
|» reportType|string|false|none|Type of the report.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-requirement-based-test-execution">Requirement-based Test Execution</h1>

Executes requirement-based Testing.

## executeRBTOnFolder

<a id="opIdexecuteRBTOnFolder"></a>

> Code samples

```http
POST /ep/folders/{folder__uid}/test-execution-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/{folder__uid}/test-execution-rbt`

*Execute all test cases from a folder*

<b>Long running task </b>Executes a requirement-based Test on all Test Cases from a given folder for the specified execution kinds. Optionally, also the model coverage report can be generated or the test execution can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "generateModelCoverageReport": false,
  "forceExecute": false
}
```

<h3 id="executerbtonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The folder UID for which the requirement-based Test is executed.|
|body|body|[RBTExecutionData](#schemarbtexecutiondata)|true|Provide the list of execution kinds  (example: SIL, TL MIL, SL MIL, etc.) for which to execute the Test Cases. Optionally, you can choose to also generate a model coverage report for each execution kind (by default they will not be generated) or set the test execution to forced, so to not re-use any previous execution results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRBTOnFolder

> Code samples

```http
POST /ep/folders/{folder__uid}/test-execution-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/test-execution-rbt`

The long running task status and result will be transmitted.

<h3 id="executerbtonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "...",
  "reportUIDs": "4fg6"
}
```

> 404 Response

```
"No folder was found for folder UID {folder__uid}."
```

<h3 id="executerbtonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RBTestCaseExecutionResultMapData](#schemarbtestcaseexecutionresultmapdata)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeRBTOnFolderList

<a id="opIdexecuteRBTOnFolderList"></a>

> Code samples

```http
POST /ep/folders/test-execution-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/test-execution-rbt`

*Execute all test cases from a list of folders*

<b>Long running task </b>Executes a requirement-based Test on all Test Cases from a given list of folders for the specified execution kinds. Optionally, also the model coverage report can be generated or the test execution can be forced to not re-use any previous results.

> Body parameter

```json
{
  "UIDs": "2UPb",
  "data": {
    "execConfigNames": "SIL",
    "generateModelCoverageReport": false,
    "forceExecute": false
  }
}
```

<h3 id="executerbtonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RBTExecutionDataExtended](#schemarbtexecutiondataextended)|true|Provide the list of folder UIDs and a list of execution kinds (example: SIL, TL MIL, SL MIL, etc.) for which to execute the Test Cases. Optionally, you can choose to also generate a model coverage report for each execution kind (by default they will not be generated) or set the test execution to forced, so to not re-use any previous execution results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRBTOnFolderList

> Code samples

```http
POST /ep/folders/test-execution-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/folders/test-execution-rbt`

The long running task status and result will be transmitted.

<h3 id="executerbtonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "...",
  "reportUIDs": "4fg6"
}
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RBTestCaseExecutionResultMapData](#schemarbtestcaseexecutionresultmapdata)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeRBTOnRBTestCase

<a id="opIdexecuteRBTOnRBTestCase"></a>

> Code samples

```http
POST /ep/test-cases-rbt/{testcase__uid}/test-execution-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/test-cases-rbt/{testcase__uid}/test-execution-rbt`

*Execute a test case*

<b>Long running task </b>Executes a requirement-based Test on a requirement-based Test Case for the specified execution kinds. Optionally, also the test execution can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false
}
```

<h3 id="executerbtonrbtestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|testcase-uid|path|string|true|The requirement-based Test Case UID for which the RBT is executed.|
|body|body|[RBTExecutionDataNoReport](#schemarbtexecutiondatanoreport)|true|Provide the execution configs (example: SIL, TL MIL, SL MIL, etc.) for which to execute the requirement-based Test. Optionally, you can choose to set the test execution to forced, so to not re-use any previous execution results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonrbtestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRBTOnRBTestCase

> Code samples

```http
POST /ep/test-cases-rbt/{testcase__uid}/test-execution-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/test-cases-rbt/{testcase__uid}/test-execution-rbt`

The long running task status and result will be transmitted.

<h3 id="executerbtonrbtestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "...",
  "reportUIDs": "4fg6"
}
```

> 404 Response

```
"Not all RB Test Cases specified have valid UIDs."
```

<h3 id="executerbtonrbtestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RBTestCaseExecutionResultMapData](#schemarbtestcaseexecutionresultmapdata)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeRBTOnRBTestCasesList

<a id="opIdexecuteRBTOnRBTestCasesList"></a>

> Code samples

```http
POST /ep/test-cases-rbt/test-execution-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/test-cases-rbt/test-execution-rbt`

*Execute a list of test cases*

<b>Long running task </b>Executes a requirement-based Test on a list of requirement-based Test Cases for the specified execution kinds. Optionally, also the test execution can be forced to not re-use any previous results.

> Body parameter

```json
{
  "UIDs": "2UPb",
  "data": {
    "execConfigNames": "SIL",
    "forceExecute": false
  }
}
```

<h3 id="executerbtonrbtestcaseslist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RBTExecutionDataExtendedNoReport](#schemarbtexecutiondataextendednoreport)|true|Provide the list of execution config  (example: SIL, TL MIL, SL MIL, etc.) and the list of requirement-based Test Case UIDs for which to execute the requirement-based Test. Optionally, you can choose to set the test execution to forced, so to not re-use any previous execution results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonrbtestcaseslist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRBTOnRBTestCasesList

> Code samples

```http
POST /ep/test-cases-rbt/test-execution-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/test-cases-rbt/test-execution-rbt`

The long running task status and result will be transmitted.

<h3 id="executerbtonrbtestcaseslist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "...",
  "reportUIDs": "4fg6"
}
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonrbtestcaseslist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RBTestCaseExecutionResultMapData](#schemarbtestcaseexecutionresultmapdata)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeRBTOnReqSource

<a id="opIdexecuteRBTOnReqSource"></a>

> Code samples

```http
POST /ep/requirements-sources/{requirements__source__uid}/test-execution-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/requirements-sources/{requirements__source__uid}/test-execution-rbt`

*Execute all test cases linked to a requirements source*

<b>Long running task </b>Executes a requirement-based Test on all Test Cases linked to the requirements of the given requirements source for the specified execution kinds. Optionally, also the model coverage report can be generated or the test execution can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "generateModelCoverageReport": false,
  "forceExecute": false
}
```

<h3 id="executerbtonreqsource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|requirements-source-uid|path|string|true|The requirements source UID for which the RBT is executed.|
|body|body|[RBTExecutionData](#schemarbtexecutiondata)|true|Provide the list of execution kinds  (example: SIL, TL MIL, SL MIL, etc.) for which to execute the Test Cases. Optionally, you can choose to also generate a model coverage report for each execution kind (by default they will not be generated) or set the test execution to forced, so to not re-use any previous execution results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonreqsource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRBTOnReqSource

> Code samples

```http
POST /ep/requirements-sources/{requirements__source__uid}/test-execution-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/requirements-sources/{requirements__source__uid}/test-execution-rbt`

The long running task status and result will be transmitted.

<h3 id="executerbtonreqsource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "...",
  "reportUIDs": "4fg6"
}
```

> 404 Response

```
"No requirements source was found for UID {requirements__source__uid}."
```

<h3 id="executerbtonreqsource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RBTestCaseExecutionResultMapData](#schemarbtestcaseexecutionresultmapdata)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeRBTOnReqSourceList

<a id="opIdexecuteRBTOnReqSourceList"></a>

> Code samples

```http
POST /ep/requirements-sources/test-execution-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/requirements-sources/test-execution-rbt`

*Execute all test cases linked to a list of requirements sources*

<b>Long running task </b>Executes a requirement-based Test on all Test Cases linked to the requirements of the given requirements sources for the specified execution kinds. Optionally, also the model coverage report can be generated or the test execution can be forced to not re-use any previous results.

> Body parameter

```json
{
  "UIDs": "2UPb",
  "data": {
    "execConfigNames": "SIL",
    "generateModelCoverageReport": false,
    "forceExecute": false
  }
}
```

<h3 id="executerbtonreqsourcelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RBTExecutionDataExtended](#schemarbtexecutiondataextended)|true|Provide the list of requirement source UIDs and the list of execution kinds (example: SIL, TL MIL, SL MIL, etc.) for which to execute the Test Cases. Optionally, you can choose to also generate a model coverage report for each execution kind (by default they will not be generated) or set the test execution to forced, so to not re-use any previous execution results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonreqsourcelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRBTOnReqSourceList

> Code samples

```http
POST /ep/requirements-sources/test-execution-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/requirements-sources/test-execution-rbt`

The long running task status and result will be transmitted.

<h3 id="executerbtonreqsourcelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "...",
  "reportUIDs": "4fg6"
}
```

> 400 Response

```
"Not all requirements source UIDs are valid."
```

<h3 id="executerbtonreqsourcelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RBTestCaseExecutionResultMapData](#schemarbtestcaseexecutionresultmapdata)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeRBTOnScope

<a id="opIdexecuteRBTOnScope"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/test-execution-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/scopes/{scope__uid}/test-execution-rbt`

*Execute all test cases from a scope*

<b>Long running task </b>Executes a requirement-based Test on all Test Cases from a given scope for the specified execution kinds. Optionally, also the model coverage report can be generated or the test execution can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "generateModelCoverageReport": false,
  "forceExecute": false
}
```

<h3 id="executerbtonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The scope UID for which the requirement-based Test is executed.|
|body|body|[RBTExecutionData](#schemarbtexecutiondata)|true|Provide the list of execution kinds  (example: SIL, TL MIL, SL MIL, etc.) for which to execute the Test Cases. Optionally, you can choose to also generate a model coverage report for each execution kind (by default they will not be generated) or set the test execution to forced, so to not re-use any previous execution results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRBTOnScope

> Code samples

```http
POST /ep/scopes/{scope__uid}/test-execution-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/test-execution-rbt`

The long running task status and result will be transmitted.

<h3 id="executerbtonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "...",
  "reportUIDs": "4fg6"
}
```

> 404 Response

```
"No scope was found for UID {scope__uid}."
```

<h3 id="executerbtonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RBTestCaseExecutionResultMapData](#schemarbtestcaseexecutionresultmapdata)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeRBTOnScopeList

<a id="opIdexecuteRBTOnScopeList"></a>

> Code samples

```http
POST /ep/scopes/test-execution-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/scopes/test-execution-rbt`

*Execute all test cases from a list of scopes*

<b>Long running task </b>Executes a requirement-based Test on all Test Cases from a given list of scopes for the specified execution kinds. Optionally, also the model coverage report can be generated or the test execution can be forced to not re-use any previous results.

> Body parameter

```json
{
  "UIDs": "2UPb",
  "data": {
    "execConfigNames": "SIL",
    "generateModelCoverageReport": false,
    "forceExecute": false
  }
}
```

<h3 id="executerbtonscopelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RBTExecutionDataExtended](#schemarbtexecutiondataextended)|true|Provide the list of scope UIDs and the list of execution kinds (example: SIL, TL MIL, SL MIL, etc.) for which to execute the Test Cases. Optionally, you can choose to also generate a model coverage report for each execution kind (by default they will not be generated) or set the test execution to forced, so to not re-use any previous execution results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executerbtonscopelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeRBTOnScopeList

> Code samples

```http
POST /ep/scopes/test-execution-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/test-execution-rbt`

The long running task status and result will be transmitted.

<h3 id="executerbtonscopelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "...",
  "reportUIDs": "4fg6"
}
```

> 400 Response

```
"Not all scope UIDs are valid."
```

<h3 id="executerbtonscopelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[RBTestCaseExecutionResultMapData](#schemarbtestcaseexecutionresultmapdata)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-requirement-based-test-cases">Requirement-based Test Cases</h1>

Handle requirement-based Test Cases.

## getRBTestCase

<a id="opIdgetRBTestCase"></a>

> Code samples

```http
GET /ep/test-cases-rbt/{testcase__uid} HTTP/1.1

Accept: application/json

```

`GET /ep/test-cases-rbt/{testcase__uid}`

*Get a test case*

Get a requirement-based Test Case by providing its UID.

<h3 id="getrbtestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|testcase-uid|path|string|true|The UID of the requirement-based Test Case to be returned.|

> Example responses

> 200 Response

```json
{
  "uid": "yak7s7",
  "name": "ExampleName",
  "description": "This is a description.",
  "kind": "TC",
  "length": 42,
  "draft": false,
  "lastModifiedDate": "01-Jan-2020 12:00:00",
  "folderUID": "12",
  "scopeUID": "24a",
  "requirementUIDs": [
    "121a"
  ]
}
```

> 404 Response

```
"No requirement-based Test Case was found. UID = {VALUE}"
```

<h3 id="getrbtestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[RequirementBasedTestCase](#schemarequirementbasedtestcase)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## deleteRBTestCase

<a id="opIddeleteRBTestCase"></a>

> Code samples

```http
DELETE /ep/test-cases-rbt/{testcase__uid} HTTP/1.1

Accept: text/plain

```

`DELETE /ep/test-cases-rbt/{testcase__uid}`

*Delete a test case*

Delete a requirement-based Test Case by providing its UID.

<h3 id="deleterbtestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|testcase-uid|path|string|true|The UID of the requirement-based Test Case to be deleted.|

> Example responses

> 404 Response

```
"No requirement-based Test Case was found. UID = {VALUE}"
```

<h3 id="deleterbtestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## exportRBTestCases

<a id="opIdexportRBTestCases"></a>

> Code samples

```http
POST /ep/test-cases-rbt-export HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/test-cases-rbt-export`

*Export test cases*

<b>Long running task</b> Export single or multiple requirement-based Test Case(s) by providing the list of the test cases which will be exported, the export directory, the export format and a list of additional options for export.

> Body parameter

```json
{
  "UIDs": "2UPb",
  "exportDirectory": "C:/RestProfiles/VectorExport",
  "exportFormat": "EXCEL",
  "additionalOptions": {
    "csvDelimiter": "SEMICOLON",
    "singleFile": true,
    "architectureUid": "2Ai7"
  },
  "overwritePolicy": "OVERWRITE"
}
```

<h3 id="exportrbtestcases-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RestRBTestCaseExportInfo](#schemarestrbtestcaseexportinfo)|true|All necessary information for exporting test cases.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exportrbtestcases-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## exportRBTestCases

> Code samples

```http
POST /ep/test-cases-rbt-export HTTP/1.1

Accept: application/json

```

`POST /ep/test-cases-rbt-export`

The long running task status and result will be transmitted.

<h3 id="exportrbtestcases-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "exportStatus": [
    {
      "name": "Artifact_1_2",
      "uid": "2my",
      "warnings": "{Cause}",
      "errors": "Export failed for file {file location}. {Cause}."
    }
  ]
}
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exportrbtestcases-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[ExportResult](#schemaexportresult)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getAllRBTestCases

<a id="opIdgetAllRBTestCases"></a>

> Code samples

```http
GET /ep/test-cases-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/test-cases-rbt`

*Get all test cases*

Get all requirement-based Test Cases.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "ExampleName",
    "description": "This is a description.",
    "kind": "TC",
    "length": 42,
    "draft": false,
    "lastModifiedDate": "01-Jan-2020 12:00:00",
    "folderUID": "12",
    "scopeUID": "24a",
    "requirementUIDs": [
      "121a"
    ]
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getallrbtestcases-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getallrbtestcases-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequirementBasedTestCase](#schemarequirementbasedtestcase)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|false|none|The name of the RBTestCase.|
|» description|string|false|none|An optional description of the RBTestCase|
|» kind|string|false|none|The datatype or kind of the RBTestCase. Usually "tc" or "csv".|
|» length|integer(int64)|false|none|The length of the vector.|
|» draft|boolean|false|none|States whether or not the RBTestCase is in Draft-Mode.|
|» lastModifiedDate|string|false|none|The date of the last modification to the RBTestCase|
|» folderUID|string|false|none|The unique identifier of the folder the RBTestCase belongs to.|
|» scopeUID|string|false|none|The unique identifier of the scope the RBTestCase belongs to.|
|» requirementUIDs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## importRBTestCase

<a id="opIdimportRBTestCase"></a>

> Code samples

```http
PUT /ep/test-cases-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`PUT /ep/test-cases-rbt`

*Import test cases*

<b>LONG RUNNING TASK</b>  Import multiple requirement-based Test Cases from external files by providing their Path and an Overwrite Policy.

> Body parameter

```json
{
  "paths": [
    "C:/RestProfiles/testCase.tc"
  ],
  "folderUID": "exampleUID123",
  "overwritePolicy": "SKIP",
  "draft": false,
  "csvDelimiter": "SEMICOLON",
  "importKind": "TC"
}
```

<h3 id="importrbtestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RestRBTestCaseImportInfo](#schemarestrbtestcaseimportinfo)|true|All necessary information for importing a Test Case into the EP.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"The request cannot be processed. Please verify that the provided input has a valid format."
```

<h3 id="importrbtestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## importRBTestCase

> Code samples

```http
PUT /ep/test-cases-rbt HTTP/1.1

Accept: application/json

```

`PUT /ep/test-cases-rbt`

The long running task status and result will be transmitted.

<h3 id="importrbtestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "importStatus": [
    {
      "UIDs": "15Lx",
      "warnings": "Undefined value detected for signal {signal name}. A default value will be set.",
      "errors": "Invalid format in file {file location}. {Cause}."
    }
  ]
}
```

> 400 Response

```
"File {NAME} can't be imported. {CAUSE}"
```

<h3 id="importrbtestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[ImportResult](#schemaimportresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getRBTestCasesByFolder

<a id="opIdgetRBTestCasesByFolder"></a>

> Code samples

```http
GET /ep/folders/{folder__uid}/test-cases-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/folders/{folder__uid}/test-cases-rbt`

*Get a list of test cases from a folder*

Get all requirement-based Test Cases from a certain Folder by providing its UID.

<h3 id="getrbtestcasesbyfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The UID of the Folder containing the requirement based Test Cases.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "ExampleName",
    "description": "This is a description.",
    "kind": "TC",
    "length": 42,
    "draft": false,
    "lastModifiedDate": "01-Jan-2020 12:00:00",
    "folderUID": "12",
    "scopeUID": "24a",
    "requirementUIDs": [
      "121a"
    ]
  }
]
```

> 404 Response

```
"No requirement-based Test Cases were found for this Folder. folder-uid = {VALUE}"
```

<h3 id="getrbtestcasesbyfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getrbtestcasesbyfolder-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequirementBasedTestCase](#schemarequirementbasedtestcase)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|false|none|The name of the RBTestCase.|
|» description|string|false|none|An optional description of the RBTestCase|
|» kind|string|false|none|The datatype or kind of the RBTestCase. Usually "tc" or "csv".|
|» length|integer(int64)|false|none|The length of the vector.|
|» draft|boolean|false|none|States whether or not the RBTestCase is in Draft-Mode.|
|» lastModifiedDate|string|false|none|The date of the last modification to the RBTestCase|
|» folderUID|string|false|none|The unique identifier of the folder the RBTestCase belongs to.|
|» scopeUID|string|false|none|The unique identifier of the scope the RBTestCase belongs to.|
|» requirementUIDs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## getRBTestCasesByScope

<a id="opIdgetRBTestCasesByScope"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/test-cases-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/test-cases-rbt`

*Get a list of test cases from a scope*

Get all requirement-based Test Cases from a certain Scope by providing its UID.

<h3 id="getrbtestcasesbyscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the Scope containing the requirement based Test Cases.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "ExampleName",
    "description": "This is a description.",
    "kind": "TC",
    "length": 42,
    "draft": false,
    "lastModifiedDate": "01-Jan-2020 12:00:00",
    "folderUID": "12",
    "scopeUID": "24a",
    "requirementUIDs": [
      "121a"
    ]
  }
]
```

> 404 Response

```
"No requirement-based Test Cases were found for this Scope. scope-uid = {VALUE}"
```

<h3 id="getrbtestcasesbyscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getrbtestcasesbyscope-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequirementBasedTestCase](#schemarequirementbasedtestcase)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|false|none|The name of the RBTestCase.|
|» description|string|false|none|An optional description of the RBTestCase|
|» kind|string|false|none|The datatype or kind of the RBTestCase. Usually "tc" or "csv".|
|» length|integer(int64)|false|none|The length of the vector.|
|» draft|boolean|false|none|States whether or not the RBTestCase is in Draft-Mode.|
|» lastModifiedDate|string|false|none|The date of the last modification to the RBTestCase|
|» folderUID|string|false|none|The unique identifier of the folder the RBTestCase belongs to.|
|» scopeUID|string|false|none|The unique identifier of the scope the RBTestCase belongs to.|
|» requirementUIDs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## getTestCasesByRequirementId

<a id="opIdgetTestCasesByRequirementId"></a>

> Code samples

```http
GET /ep/requirements/{requirement__uid}/test-cases-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/requirements/{requirement__uid}/test-cases-rbt`

*Get a list of test cases linked to a requirement*

Use this command to retrieve the test cases linked to a given requirement uid.

<h3 id="gettestcasesbyrequirementid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|requirement-uid|path|string|true|The uid of the requirement for which all linked test cases should be returned.|
|only-indirect-testcases|query|boolean|false|The flag used to specify whether to retrieve only test cases which are indirectly linked to a given requirement. This flag has an effect only on non-leaves requirements. If no value is specified, this flag will be set to false.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "ExampleName",
    "description": "This is a description.",
    "kind": "TC",
    "length": 42,
    "draft": false,
    "lastModifiedDate": "01-Jan-2020 12:00:00",
    "folderUID": "12",
    "scopeUID": "24a",
    "requirementUIDs": [
      "121a"
    ]
  }
]
```

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="gettestcasesbyrequirementid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="gettestcasesbyrequirementid-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequirementBasedTestCase](#schemarequirementbasedtestcase)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|false|none|The name of the RBTestCase.|
|» description|string|false|none|An optional description of the RBTestCase|
|» kind|string|false|none|The datatype or kind of the RBTestCase. Usually "tc" or "csv".|
|» length|integer(int64)|false|none|The length of the vector.|
|» draft|boolean|false|none|States whether or not the RBTestCase is in Draft-Mode.|
|» lastModifiedDate|string|false|none|The date of the last modification to the RBTestCase|
|» folderUID|string|false|none|The unique identifier of the folder the RBTestCase belongs to.|
|» scopeUID|string|false|none|The unique identifier of the scope the RBTestCase belongs to.|
|» requirementUIDs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## unlinkRequirementToTestCase

<a id="opIdunlinkRequirementToTestCase"></a>

> Code samples

```http
PUT /ep/requirements/test-cases-rbt HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`PUT /ep/requirements/test-cases-rbt`

*Unlink requirements from test cases*

Use this command to unlink requirements from test cases. Only their uids must be specified.

> Body parameter

```json
{
  "requirementUIDs": [
    "284"
  ],
  "testCaseUIDs": [
    "27m"
  ]
}
```

<h3 id="unlinkrequirementtotestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RBTestCaseRequirementsInfo](#schemarbtestcaserequirementsinfo)|true|Provide the configuration for the unlinking. The uids of the requirements and test cases must be specified.|

> Example responses

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="unlinkrequirementtotestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Requirements unlinked from test cases.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## linkRequirementToTestCase

<a id="opIdlinkRequirementToTestCase"></a>

> Code samples

```http
POST /ep/requirements/test-cases-rbt HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/requirements/test-cases-rbt`

*Link requirements to test cases*

Use this command to link requirements to test cases. Only their uids must be specified.

> Body parameter

```json
{
  "requirementUIDs": [
    "284"
  ],
  "testCaseUIDs": [
    "27m"
  ]
}
```

<h3 id="linkrequirementtotestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RBTestCaseRequirementsInfo](#schemarbtestcaserequirementsinfo)|true|Provide the configuration for the linking. The uids of the requirements and test cases must be specified.|

> Example responses

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="linkrequirementtotestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Requirements linked to test cases.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-interface-reports">Interface Reports</h1>

Handle interface reports.

## createInterfaceReportOnScope

<a id="opIdcreateInterfaceReportOnScope"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/interface-reports HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/interface-reports`

*Create a report on a scope*

Create an interface report on given scope. The interface report will use the interface of the architecture of the provided scope.

<h3 id="createinterfacereportonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The scope on which the interface report should be created. The interface report will use the interface of the architecture of the provide scope.|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"Cannot create an interface report on scope."
```

<h3 id="createinterfacereportonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## getReports_3

<a id="opIdgetReports_3"></a>

> Code samples

```http
GET /ep/interface-reports HTTP/1.1

Accept: application/json

```

`GET /ep/interface-reports`

*Get all reports*

Retrieve all interface reports from the profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "reportName": "Report 9/27/20 07:43 AM",
    "reportType": "<Report Type>"
  }
]
```

> 404 Response

```
"No reports were found."
```

<h3 id="getreports_3-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getreports_3-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Report](#schemareport)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» reportName|string|false|none|Name of the report.|
|» reportType|string|false|none|Type of the report.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-project-reports">Project Reports</h1>

Create and retrieve project reports.

## createProjectReport

<a id="opIdcreateProjectReport"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/project-report HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/project-report`

*Create a project report*

Create a project report.

<h3 id="createprojectreport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope for which the report shall be created.|
|template-name|query|string|false|The name of the template to use for report creation. <br>This can be either the full path and filename of a template file to use, or the name of a template that was provided to EP by setting the template folder via the preference REPORT_TEMPLATE_FOLDER <br> If no template is given, all available data will be included.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createprojectreport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createProjectReport

> Code samples

```http
POST /ep/scopes/{scope__uid}/project-report HTTP/1.1

Accept: text/plain

```

`POST /ep/scopes/{scope__uid}/project-report`

The long running task status and result will be transmitted.

<h3 id="createprojectreport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 406 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createprojectreport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the full path and file name of the created report is returned.|None|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getAllProjectReports

<a id="opIdgetAllProjectReports"></a>

> Code samples

```http
GET /ep/project-reports HTTP/1.1

Accept: application/json

```

`GET /ep/project-reports`

*Get all project reports*

Retrieve all project reports from the profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "reportName": "Report 9/27/20 07:43 AM",
    "reportType": "<Report Type>"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getallprojectreports-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getallprojectreports-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Report](#schemareport)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» reportName|string|false|none|Name of the report.|
|» reportType|string|false|none|Type of the report.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-scopes">Scopes</h1>

Handle Scopes.

## getScope

<a id="opIdgetScope"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid} HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}`

*Get a scope*

Get a specific scope by providing its UID.

<h3 id="getscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope to be returned.|

> Example responses

> 200 Response

```json
{
  "uid": "k25pq",
  "name": "string",
  "topLevel": true,
  "kind": "SUT",
  "path": "string",
  "architecture": "string",
  "sampleTime": {
    "uid": "s567k",
    "seconds": "0.01"
  }
}
```

> 404 Response

```
"No Scope was found."
```

<h3 id="getscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[Scope](#schemascope)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## getScopesByQuery

<a id="opIdgetScopesByQuery"></a>

> Code samples

```http
GET /ep/scopes HTTP/1.1

Accept: application/json

```

`GET /ep/scopes`

*Get a list of scopes*

Get a list of scopes by a query which filters by path and top-level.

<h3 id="getscopesbyquery-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|path|query|string|false|Enter the path of the scope you would like to search for. If null, then all scopes will be returned.|
|top-level|query|boolean|false|Specifies, if only top level scopes shall be returned. <br>If set to 'true', only top level scopes will be returned. <br>If set to 'false', all scopes will be returned, including the top level. <br>If not specified, then the default value is 'false'.|
|architecture-uid|query|string|false|Specifies from which architecture the scopes are being collected. If null, then the first imported architecture will be used.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "k25pq",
    "name": "string",
    "topLevel": true,
    "kind": "SUT",
    "path": "string",
    "architecture": "string",
    "sampleTime": {
      "uid": "s567k",
      "seconds": "0.01"
    }
  }
]
```

> 404 Response

```
"No scopes found for this query."
```

<h3 id="getscopesbyquery-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getscopesbyquery-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Scope](#schemascope)]|false|none|none|
|» uid|string|false|none|The unique identifier (UID) of this object.|
|» name|string|false|none|The scope name.|
|» topLevel|boolean|false|none|True if scope is a toplevel scope.|
|» kind|string|false|none|Scope kind.|
|» path|string|false|none|Scope path.|
|» architecture|string|false|none|The corresponding architecture of the scope.|
|» sampleTime|[SampleTime](#schemasampletime)|false|none|The sample time of the scope.|
|»» uid|string|false|none|The unique identifier (UID) of this object.|
|»» seconds|string|false|none|The sample time as a value given in seconds.|

#### Enumerated Values

|Property|Value|
|---|---|
|kind|SUT|
|kind|DUMMY|
|kind|ENVIRONMENT|
|kind|HIDDEN_INTERNAL|
|kind|VIRTUAL|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-signals">Signals</h1>

Handle signals' operations.

## getSignals

<a id="opIdgetSignals"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/signals HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/signals`

*Get all signals from a scope*

Get all signals from the given scope

<h3 id="getsignals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The scope for which to get the signals.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "identifier": "INPUT:driver_up:var"
  }
]
```

> 404 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getsignals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getsignals-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RestSignal](#schemarestsignal)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» identifier|string|false|read-only|The signal identifier.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-coverage-generation">Coverage generation</h1>

For a C-Code function, create stimuli vectors which cover the code function, or mark coverage properties that are unreachable.

## execute

<a id="opIdexecute"></a>

> Code samples

```http
POST /ep/coverage-generation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/coverage-generation`

*Execute coverage generation*

<b>Long running task</b> Using the provided configuration, execute the coverage generation / stimuli vector generation.

> Body parameter

```json
{
  "isSubscopesGoalsConsidered": false,
  "targetDefinitions": [
    {
      "label": "Statement"
    }
  ],
  "folderName": "myFolder",
  "checkUnreachableProperties": false,
  "pllString": "STM;D;CDC",
  "engineSettings": {
    "timeoutSeconds": 500,
    "handlingRateThreshold": 50,
    "analyseSubScopesHierarchically": true,
    "engineAtg": {
      "name": "ATG",
      "searchDepthSteps": 10,
      "executionMode": "TOP_DOWN",
      "mutateExistingVectors": false,
      "timeoutSecondsPerSubsystem": 500
    },
    "engineCv": {
      "name": "CV",
      "searchDepthSteps": 10,
      "timeoutSecondsPerSubsystem": 500,
      "timeoutSecondsPerProperty": 500,
      "memoryLimitMb": 500,
      "loopUnroll": 50,
      "coreEngines": [
        {
          "name": "SMIBMC"
        }
      ],
      "assumptionCheckEnabled": true,
      "searchFocus": "BALANCED",
      "parallelExecutionMode": "BALANCED",
      "maximumNumberOfThreads": 1
    },
    "allowDenormalizedFloats": true
  },
  "scopeUid": "string",
  "assumptions": [
    {
      "id": "uisc23"
    }
  ],
  "drivers": [
    {
      "id": "uisc23"
    }
  ],
  "initializationVectorUID": "exampleUID123"
}
```

<h3 id="execute-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Config](#schemaconfig)|true|The configuration to use for the coverage generation run.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"Cannot execute on this profile."
```

<h3 id="execute-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Accepted|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## execute

> Code samples

```http
POST /ep/coverage-generation HTTP/1.1

Accept: text/plain

```

`POST /ep/coverage-generation`

The long running task status and result will be transmitted.

<h3 id="execute-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="execute-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Executed. When the long running task is finished, the operation result will be available.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-code-analysis-reports-b2b">Code Analysis Reports B2B</h1>

Handle Back-To-Back code analysis reports.

## createCodeAnalysisReportOnFolder

<a id="opIdcreateCodeAnalysisReportOnFolder"></a>

> Code samples

```http
POST /ep/folders/{folder__uid}/code-analysis-reports-b2b HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/code-analysis-reports-b2b`

*Create a report on a folder*

Create a B2B code analysis report on given folder.

<h3 id="createcodeanalysisreportonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The folder UID for which to create the B2B code analysis report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createcodeanalysisreportonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createCodeAnalysisReportOnFolder

> Code samples

```http
POST /ep/folders/{folder__uid}/code-analysis-reports-b2b HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/code-analysis-reports-b2b`

The long running task status and result will be transmitted.

<h3 id="createcodeanalysisreportonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"All folders need to be of kind: Requirement-based Test Case or Stimuli Vector."
```

<h3 id="createcodeanalysisreportonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is available in the 'result' field of the response object.|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createCodeAnalysisReportOnFolders

<a id="opIdcreateCodeAnalysisReportOnFolders"></a>

> Code samples

```http
POST /ep/folders/code-analysis-reports-b2b HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/code-analysis-reports-b2b`

*Create a report on a list of folders*

Create B2B Code Analysis Report on given folders.

> Body parameter

```json
{
  "UIDs": [
    "2UPb",
    "3rH8"
  ]
}
```

<h3 id="createcodeanalysisreportonfolders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ReportCreationInfo](#schemareportcreationinfo)|true|Provide the list of folder UIDs for which to create the B2B code analysis report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createcodeanalysisreportonfolders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createCodeAnalysisReportOnFolders

> Code samples

```http
POST /ep/folders/code-analysis-reports-b2b HTTP/1.1

Accept: application/json

```

`POST /ep/folders/code-analysis-reports-b2b`

The long running task status and result will be transmitted.

<h3 id="createcodeanalysisreportonfolders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"All folders need to be of kind: Requirement-based Test Case or Stimuli Vector."
```

<h3 id="createcodeanalysisreportonfolders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is available in the 'result' field of the response object.|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createCodeAnalysisReportOnScope

<a id="opIdcreateCodeAnalysisReportOnScope"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/code-analysis-reports-b2b HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/code-analysis-reports-b2b`

*Create a report on a scope*

Create a B2B code analysis report on given scope.

<h3 id="createcodeanalysisreportonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The scope UID for which to create the B2B code analysis report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createcodeanalysisreportonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createCodeAnalysisReportOnScope

> Code samples

```http
POST /ep/scopes/{scope__uid}/code-analysis-reports-b2b HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/code-analysis-reports-b2b`

The long running task status and result will be transmitted.

<h3 id="createcodeanalysisreportonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 404 Response

```
"No scope was found for the given UID."
```

<h3 id="createcodeanalysisreportonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is available in the 'result' field of the response object.|[Report](#schemareport)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getReports_4

<a id="opIdgetReports_4"></a>

> Code samples

```http
GET /ep/code-analysis-reports-b2b HTTP/1.1

Accept: application/json

```

`GET /ep/code-analysis-reports-b2b`

*Get all reports*

Retrieve all B2B code analysis reports from profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "reportName": "Report 9/27/20 07:43 AM",
    "reportType": "<Report Type>"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getreports_4-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getreports_4-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Report](#schemareport)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» reportName|string|false|none|Name of the report.|
|» reportType|string|false|none|Type of the report.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-code-coverage-robustness-check-b2b">Code Coverage/Robustness Check B2B</h1>

Retrieve code coverage/robustness checks details and results in B2B.

## getCodeCoverageGoalsByScope

<a id="opIdgetCodeCoverageGoalsByScope"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/coverage-details-b2b HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/coverage-details-b2b`

*Get coverage details for a scope*

Get all code coverage/robustness checks details for a scope. Some filters can be applied.

<h3 id="getcodecoveragegoalsbyscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope|
|statuses|query|array[string]|false|The status filter for code coverage/robustness check goals. Possible values: COVERED, UNKNOWN, UNREACHABLE_INF, UNREACHABLE_N, INCONSISTENT, UNKNOWN_JUSTIFIED, UNREACHABLE_INF_JUSTIFIED, UNREACHABLE_N_JUSTIFIED. Can also specify multiple options. <br>Can also be empty, in which case the results are shown for all statuses.|
|goal-types|query|array[string]|false|The goal type filter for code coverage/robustness check goals. Possible values for code coverage goals: STM(Statement), C(Condition), D(Decision/Branch), CDC(C/DC), MCDC(C/DC and MC/DC), F(Function), SC(Switch-Case), RO(Relational Operator),  FC(Function Call). <br>Possible values for robustness check goals are: DZ(Division by Zero), CA(Downcast). Can also specify multiple options. Can also be empty, in which case the results are shown for all goal types.|
|files|query|array[string]|false|List of file filters for code coverage/robustness check goals. If list is empty the results are shown for all files.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|statuses|COVERED|
|statuses|UNKNOWN|
|statuses|UNREACHABLE_INF|
|statuses|UNREACHABLE_N|
|statuses|INCONSISTENT|
|statuses|UNKNOWN_JUSTIFIED|
|statuses|UNREACHABLE_N_JUSTIFIED|
|statuses|UNREACHABLE_INF_JUSTIFIED|
|goal-types|STM|
|goal-types|D|
|goal-types|C|
|goal-types|MCDC|
|goal-types|F|
|goal-types|FC|
|goal-types|SC|
|goal-types|RO|
|goal-types|CDC|
|goal-types|DZ|
|goal-types|CA|

> Example responses

> 200 Response

```json
[
  {
    "pll": "STM:1",
    "type": "Statement",
    "line": 390,
    "file": "power_widow_control.c",
    "properties": [
      {
        "pll": "STM:76:0",
        "status": "Unknown",
        "coveringVectors": [
          "testCase"
        ]
      }
    ],
    "expression": "(obstacle_position!=0)",
    "blocks": [
      "string"
    ],
    "comment": "Comment",
    "justified": true
  }
]
```

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="getcodecoveragegoalsbyscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getcodecoveragegoalsbyscope-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CodeCoverageGoal](#schemacodecoveragegoal)]|false|none|none|
|» pll|string|false|none|PLL string of the coverage goal.|
|» type|string|false|none|Goal type of the coverage goal.|
|» line|integer(int32)|false|none|The line number of the location where the coverage goal is located in the file.|
|» file|string|false|none|The file name where the coverage property can be located.|
|» properties|[[CodeCoverageProperty](#schemacodecoverageproperty)]|false|none|[A list with coverage goal properties.]|
|»» pll|string|false|none|PLL string of the coverage property.|
|»» status|string|false|none|Status of the coverage property.|
|»» coveringVectors|[string]|false|none|none|
|» expression|string|false|none|Expression of the coverage goal.|
|» blocks|[string]|false|none|none|
|» comment|string|false|none|The comment.|
|» justified|boolean|false|none|If this goal is justified|

<aside class="success">
This operation does not require authentication
</aside>

## getCodeCoverageResultByScope

<a id="opIdgetCodeCoverageResultByScope"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/coverage-results-b2b HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/coverage-results-b2b`

*Get coverage results for a scope*

Get the code coverage and robustness checks results for a scope. Goal type filters can be applied.

<h3 id="getcodecoverageresultbyscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope|
|goal-types|query|array[string]|false|The goal type filter for code coverage/robustness check goals. Possible values for code coverage goals: STM(Statement), C(Condition), D(Decision/Branch), CDC(C/DC), MCDC(C/DC and MC/DC), F(Function), SC(Switch-Case), RO(Relational Operator),  FC(Function Call). Possible values for robustness check goals are: DZ(Division by Zero), CA(Downcast). Can also specify multiple options. Can also be empty, in which case the results are shown for all goal types.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|goal-types|STM|
|goal-types|D|
|goal-types|C|
|goal-types|MCDC|
|goal-types|F|
|goal-types|FC|
|goal-types|SC|
|goal-types|RO|
|goal-types|CDC|
|goal-types|DZ|
|goal-types|CA|

> Example responses

> 200 Response

```json
{
  "CDCCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "CDCPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "ConditionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "ConditionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DecisionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DecisionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "FunctionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "FunctionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "FunctionCallCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "FunctionCallPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "MCDCCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "MCDCPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "RelationalOperatorCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "RelationalOperatorPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "StatementCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "StatementPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "SwitchCaseCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "SwitchCasePropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DivisionByZeroCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DivisionByZeroPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DownCastCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DownCastPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "codeCoverageComment": "My code coverage overview comment.",
  "robustnessCoverageComment": "My robustness checks overview comment."
}
```

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="getcodecoverageresultbyscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[CodeCoverageResult](#schemacodecoverageresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## setGoalComment

<a id="opIdsetGoalComment"></a>

> Code samples

```http
POST /ep/coverage-goals/set-comment-b2b HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/coverage-goals/set-comment-b2b`

*Set goal comments*

Set comments of code coverage and robustness check goals.

> Body parameter

```json
[
  {
    "pll": "F:0",
    "comment": "MyComment"
  }
]
```

<h3 id="setgoalcomment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[GoalComment](#schemagoalcomment)|true|none|

> Example responses

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="setgoalcomment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## setGoalJustified

<a id="opIdsetGoalJustified"></a>

> Code samples

```http
POST /ep/coverage-goals/set-justified-b2b HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/coverage-goals/set-justified-b2b`

*Set goal justified status*

Set justified status of code coverage and robustness check goals.

> Body parameter

```json
{
  "justified": true,
  "plls": [
    "2fa"
  ]
}
```

<h3 id="setgoaljustified-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CodeCoverageJustify](#schemacodecoveragejustify)|true|none|

> Example responses

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="setgoaljustified-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## setScopeOverviewComment

<a id="opIdsetScopeOverviewComment"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/set-coverage-overview-comment-b2b HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/scopes/{scope__uid}/set-coverage-overview-comment-b2b`

*Set overview comments*

Set the comments of code coverage overview sections.

> Body parameter

```json
[
  {
    "type": "CC_STAT",
    "comment": "myComment"
  }
]
```

<h3 id="setscopeoverviewcomment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope|
|body|body|[OverviewComment](#schemaoverviewcomment)|true|none|

> Example responses

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="setscopeoverviewcomment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-messages">Messages</h1>

Handle messages and message markers.

## createMessageMarker

<a id="opIdcreateMessageMarker"></a>

> Code samples

```http
POST /ep/message-markers HTTP/1.1

Accept: application/json

```

`POST /ep/message-markers`

*Create a message marker*

Use this command to create a new message marker at the current time. The response will contain the created message marker time stamp as java Timestamp

> Example responses

> 201 Response

```json
{
  "date": "string"
}
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createmessagemarker-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[MessageMarker](#schemamessagemarker)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## getMessages

<a id="opIdgetMessages"></a>

> Code samples

```http
GET /ep/message-markers/{marker__date}/messages HTTP/1.1

Accept: application/json

```

`GET /ep/message-markers/{marker__date}/messages`

*Get a list of messages from a message marker*

Search for messages created after a given message marker.

<h3 id="getmessages-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|marker-date|path|string|true|The message marker after which the messages should be queried from the Database.|
|search-string|query|string|false|Enter the beginning of the messages you would like to search for. If null, then all messages will be returned.|
|severity|query|string|false|Choose any severity you would like to search for. If null, then all severities will be returned.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|severity|INFO|
|severity|WARNING|
|severity|ERROR|
|severity|CRITICAL|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "date": "01-Jan-2020 12:00:00",
    "message": "This is a message. ",
    "hint": "This is a hint.",
    "severity": "INFO"
  }
]
```

> 404 Response

```
"No message found for the given query."
```

<h3 id="getmessages-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getmessages-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Message](#schemamessage)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» date|string|false|read-only|The creation-date of the message.|
|» message|string|true|none|The message itself.|
|» hint|string|false|none|An additional hint.|
|» severity|string|true|none|The severity of the message.|

#### Enumerated Values

|Property|Value|
|---|---|
|severity|INFO|
|severity|WARNING|
|severity|ERROR|
|severity|CRITICAL|

<aside class="success">
This operation does not require authentication
</aside>

## getMessagesByQuery

<a id="opIdgetMessagesByQuery"></a>

> Code samples

```http
GET /ep/messages HTTP/1.1

Accept: application/json

```

`GET /ep/messages`

*Get a list of messages*

Search for past messages up until a certain amount you can set yourself.

<h3 id="getmessagesbyquery-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|search-string|query|string|false|Enter the beginning of the messages you would like to search for. If null, then all messages will be returned. |
|severity|query|string|false|Choose any severity you would like to search for. If null, then all severities will be returned.|
|max-messages|query|integer(int32)|false|The maximum number of messages returned. Cannot be > 1000. |

#### Detailed descriptions

**search-string**: Enter the beginning of the messages you would like to search for. If null, then all messages will be returned. 
Furthermore, you may use the following wildcards: '*' for any string, '?' for any single character.

**max-messages**: The maximum number of messages returned. Cannot be > 1000. 
If > 1000, negative, or null, at most 1000 messages will be returned.

#### Enumerated Values

|Parameter|Value|
|---|---|
|severity|INFO|
|severity|WARNING|
|severity|ERROR|
|severity|CRITICAL|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "date": "01-Jan-2020 12:00:00",
    "message": "This is a message. ",
    "hint": "This is a hint.",
    "severity": "INFO"
  }
]
```

> 400 Response

```
"Illegal argument. maxMessages = {VALUE}"
```

<h3 id="getmessagesbyquery-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getmessagesbyquery-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Message](#schemamessage)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» date|string|false|read-only|The creation-date of the message.|
|» message|string|true|none|The message itself.|
|» hint|string|false|none|An additional hint.|
|» severity|string|true|none|The severity of the message.|

#### Enumerated Values

|Property|Value|
|---|---|
|severity|INFO|
|severity|WARNING|
|severity|ERROR|
|severity|CRITICAL|

<aside class="success">
This operation does not require authentication
</aside>

## addMessage

<a id="opIdaddMessage"></a>

> Code samples

```http
POST /ep/messages HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/messages`

*Create a message*

Add a message by providing a Message. Note that a new UID will be assigned.

> Body parameter

```json
{
  "message": "This is a message. ",
  "hint": "This is a hint.",
  "severity": "INFO"
}
```

<h3 id="addmessage-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Message](#schemamessage)|true|Provide any message you would like to add. A new UID will be assigned.|

> Example responses

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="addmessage-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## deleteMessagesByQuery

<a id="opIddeleteMessagesByQuery"></a>

> Code samples

```http
DELETE /ep/messages HTTP/1.1

Accept: text/plain

```

`DELETE /ep/messages`

*Delete a list of messages*

Search for past messages up until a certain amount you can set yourself and delete them.

<h3 id="deletemessagesbyquery-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|search-string|query|string|false|Enter the beginning of the messages you would like to search for. If null, then all messages will be deleted.|
|severity|query|string|false|Choose any severity you would like to search for. If null, then all severities will be deleted.|
|max-messages|query|integer(int32)|false|The max number of messages deleted. If negative or null, all messages will be deleted.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|severity|INFO|
|severity|WARNING|
|severity|ERROR|
|severity|CRITICAL|

> Example responses

> 400 Response

```
"Illegal argument. maxMessages = {VALUE}"
```

<h3 id="deletemessagesbyquery-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## getMessage

<a id="opIdgetMessage"></a>

> Code samples

```http
GET /ep/messages/{message__uid} HTTP/1.1

Accept: application/json

```

`GET /ep/messages/{message__uid}`

*Get a message*

Get the message with the provided UID.

<h3 id="getmessage-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|message-uid|path|string|true|The UID of the message to be returned.|

> Example responses

> 200 Response

```json
{
  "uid": "yak7s7",
  "date": "01-Jan-2020 12:00:00",
  "message": "This is a message. ",
  "hint": "This is a hint.",
  "severity": "INFO"
}
```

> 404 Response

```
"No message was found. UID = {VALUE}"
```

<h3 id="getmessage-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[Message](#schemamessage)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## deleteMessage

<a id="opIddeleteMessage"></a>

> Code samples

```http
DELETE /ep/messages/{message__uid} HTTP/1.1

Accept: text/plain

```

`DELETE /ep/messages/{message__uid}`

*Delete a message*

Delete a message by providing its UID.

<h3 id="deletemessage-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|message-uid|path|string|true|Enter the UID of the message you would like to delete.|

> Example responses

> 404 Response

```
"No message was found. UID = {VALUE}"
```

<h3 id="deletemessage-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## exportMessages

<a id="opIdexportMessages"></a>

> Code samples

```http
POST /ep/messages/message-report?file%2Dname=C%3A%2Fprofiles%2Fmessage_report.html HTTP/1.1

Accept: text/plain

```

`POST /ep/messages/message-report`

*Export messages*

Export all messages to the specified report file (in HTML format). 
If a <a href='#post-/ep/message-markers'>Message Marker</a> is provided, all messages starting from the marker will be exported.

<h3 id="exportmessages-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|file-name|query|string|true|The path and file name of the message report file to create.|
|marker-date|query|string|false|If specified, only messages that were posted after this <a href='#post-/ep/message-markers'>Message Marker</a> was created will be exported.|

#### Detailed descriptions

**file-name**: The path and file name of the message report file to create.
Note: An existing file will be overwritten!

> Example responses

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exportmessages-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Exported Succesfully. Returns exported report location.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-preferences">Preferences</h1>

Set and retrieve preferences.

## getPreference

<a id="opIdgetPreference"></a>

> Code samples

```http
GET /ep/preferences/{preference__name} HTTP/1.1

Accept: application/json

```

`GET /ep/preferences/{preference__name}`

*Get a preference*

Get the preference with a given name. If the retrieved value is empty, the preference might have its default value.

<h3 id="getpreference-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|preference-name|path|string|true|Enter the name of the preference that you want retrieved.|

> Example responses

> 200 Response

```json
{
  "preferenceName": "ARCHITECTURE_DEFAULT_VIEW",
  "preferenceValue": "C-Code"
}
```

> 404 Response

```
"No preference found for this name."
```

<h3 id="getpreference-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[Preference](#schemapreference)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## setPreferences

<a id="opIdsetPreferences"></a>

> Code samples

```http
PUT /ep/preferences HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`PUT /ep/preferences`

*Set a list of preferences*

Set new values for a list of given preferences. The preference name and new value must be provided for each of them.

> Body parameter

```json
[
  {
    "preferenceName": "ARCHITECTURE_DEFAULT_VIEW",
    "preferenceValue": "C-Code"
  }
]
```

<h3 id="setpreferences-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Preference](#schemapreference)|false|none|

> Example responses

> 200 Response

```json
{
  "messages": [
    "string"
  ]
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="setpreferences-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Preferences set|[PreferenceImportResult](#schemapreferenceimportresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-profiles">Profiles</h1>

Create and handle EP Profiles.

## getCurrentProfile

<a id="opIdgetCurrentProfile"></a>

> Code samples

```http
GET /ep/profiles HTTP/1.1

Accept: application/json

```

`GET /ep/profiles`

*Get the active profile*

Use this command to get the currently active profile.

> Example responses

> 200 Response

```json
{
  "uid": "yak7s7",
  "metadata": {
    "Profile Creator": "developer",
    "Profile Creation Date": "14-Sep-2020 14:01:43",
    "Profile Modifier": "",
    "Profile Modification Date": "",
    "Profile Creation Tool Version": "2.8p0"
  },
  "profilePath": {
    "path": "C:/RestProfiles/test.epp"
  }
}
```

> 404 Response

```
"No active profile found."
```

<h3 id="getcurrentprofile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[Profile](#schemaprofile)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## saveProfile

<a id="opIdsaveProfile"></a>

> Code samples

```http
PUT /ep/profiles HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`PUT /ep/profiles`

*Save the profile*

Use this command to save your active profile at a given location. Keep in mind to use only legal profile paths.

> Body parameter

```json
{
  "path": "C:/RestProfiles/test.epp"
}
```

<h3 id="saveprofile-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ProfilePath](#schemaprofilepath)|true|The path where the profile will be saved.|

> Example responses

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="saveprofile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## createProfile

<a id="opIdcreateProfile"></a>

> Code samples

```http
POST /ep/profiles HTTP/1.1

Accept: application/json

```

`POST /ep/profiles`

*Create a profile*

Use this command to create a new empty profile. It won't contain a path, since it's not stored anywhere yet.

<h3 id="createprofile-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|discardCurrentProfile|query|boolean|false|If 'true' the current profile is discarded and a new profile will be created. Otherwise a new profile will only be created when the current profile is not in a dirty state.Default is 'false'|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "metadata": {
    "Profile Creator": "developer",
    "Profile Creation Date": "14-Sep-2020 14:01:43",
    "Profile Modifier": "",
    "Profile Modification Date": "",
    "Profile Creation Tool Version": "2.8p0"
  },
  "profilePath": {
    "path": "C:/RestProfiles/test.epp"
  }
}
```

> 428 Response

```
"Current profile is dirty."
```

<h3 id="createprofile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Profile](#schemaprofile)|
|428|[Precondition Required](https://tools.ietf.org/html/rfc6585#section-3)|Precondition Required|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## discardProfile

<a id="opIddiscardProfile"></a>

> Code samples

```http
DELETE /ep/profiles HTTP/1.1

Accept: text/plain

```

`DELETE /ep/profiles`

*Discard a profile*

Use this command to discard a profile, even if it is dirty. Changes will not be saved!

> Example responses

> 404 Response

```
"No active profile found."
```

<h3 id="discardprofile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## openProfile

<a id="opIdopenProfile"></a>

> Code samples

```http
GET /ep/profiles/{profile__path} HTTP/1.1

Accept: application/json

```

`GET /ep/profiles/{profile__path}`

*Open a profile*

Use this command to open an existing profile. Specifiy the path to the profile with a name of your choice. Keep in mind to only use legal profile paths of already existing profiles.

<h3 id="openprofile-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|profile-path|path|string|true|The path to the existing profile.|
|discardCurrentProfile|query|boolean|false|If 'true' the current profile is discarded and a new profile will be created. Otherwise a new profile will only be created when the current profile is not in a dirty state.Default is 'false'|

> Example responses

> 200 Response

```json
{
  "uid": "yak7s7",
  "metadata": {
    "Profile Creator": "developer",
    "Profile Creation Date": "14-Sep-2020 14:01:43",
    "Profile Modifier": "",
    "Profile Modification Date": "",
    "Profile Creation Tool Version": "2.8p0"
  },
  "profilePath": {
    "path": "C:/RestProfiles/test.epp"
  }
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="openprofile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[Profile](#schemaprofile)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|428|[Precondition Required](https://tools.ietf.org/html/rfc6585#section-3)|Precondition Required|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-progress">Progress</h1>

Get the current status of long-running operations.

## getProgress

<a id="opIdgetProgress"></a>

> Code samples

```http
GET /ep/progress HTTP/1.1

Accept: application/json

```

`GET /ep/progress`

*Get the status of a long running operation*

Get the status of a long running operation. If the operation is on-going, the current progress will be returned. If the operation is complete, the resulted object will be returned if there is one.  An error will be returned if it occured during the long-running operation.

<h3 id="getprogress-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|The progress id. Can be retrieved by starting a long-running operation.|

#### Detailed descriptions

**progress-id**: The progress id. Can be retrieved by starting a long-running operation.
If not specified then last long running operation result will be returned. 

> Example responses

> 200 Response

```json
{
  "message": "string",
  "progress": 0,
  "result": {}
}
```

> 400 Response

```
"There is a problem with the request that started the long running operation."
```

<h3 id="getprogress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Operation is complete. No resulting object is returned.|[LongRunningResponse](#schemalongrunningresponse)|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Operation is complete. Resulting object is returned as JSON.|[LongRunningResponse](#schemalongrunningresponse)|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Operation is currently in progress|[LongRunningResponse](#schemalongrunningresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-reports">Reports</h1>

Retrieve and export Reports.

## getReport

<a id="opIdgetReport"></a>

> Code samples

```http
GET /ep/reports/{report__uid} HTTP/1.1

Accept: application/json

```

`GET /ep/reports/{report__uid}`

*Get a report*

Get the report with the provided UID.

<h3 id="getreport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|report-uid|path|string|true|The UID of the report to be returned.|

> Example responses

> 200 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 404 Response

```
"No report was found. UID = {VALUE}"
```

<h3 id="getreport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[Report](#schemareport)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## exportReport

<a id="opIdexportReport"></a>

> Code samples

```http
POST /ep/reports/{report__uid} HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/reports/{report__uid}`

*Export a report*

Use this command export a report to a given location. The exported report corresponds to the given UID inside the command. New name can be set for file. If file exists, will be overwritten. Keep in mind to use only legal profile paths.

> Body parameter

```json
{
  "exportPath": "C:/Program Files/BTC/reports",
  "newName": "New Report"
}
```

<h3 id="exportreport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|report-uid|path|string|true|The UID of the report to be returned.|
|body|body|[ReportExportInfo](#schemareportexportinfo)|true|Provide the location where to export the report. (Optional) Report can be given a new name.|

> Example responses

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exportreport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Exported Succesfully. Returns exported report location.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-matlab-script-execution">MATLAB script Execution</h1>

Execute a MATLAB script.

## executeMatlabScriptLong

<a id="opIdexecuteMatlabScriptLong"></a>

> Code samples

```http
POST /ep/execute-long-matlab-script HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/execute-long-matlab-script`

*Execute long-running MATLAB script*

Execute a long-running MATLAB script using the given parameters. Should be used when the time it takes for the script to end is longer than the request timeout of your REST client. Otherwise, for ease of use, the <b>Execute a short-running MATLAB script</b> method should be utilized.

> Body parameter

```json
{
  "scriptName": "my_script",
  "outArgs": 3,
  "inArgs": [
    true,
    1,
    1.2,
    "myString",
    [
      false,
      2
    ],
    {
      "field1": 3,
      "field2": [
        4,
        "myString"
      ],
      "field3": {
        "childField": 5
      }
    }
  ]
}
```

<h3 id="executematlabscriptlong-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[MatlabScriptInput](#schemamatlabscriptinput)|true|Information needed to execute the MATLAB script|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executematlabscriptlong-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeMatlabScriptLong

> Code samples

```http
POST /ep/execute-long-matlab-script HTTP/1.1

Accept: application/json

```

`POST /ep/execute-long-matlab-script`

The long running task status and result will be transmitted.

<h3 id="executematlabscriptlong-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "outArgs": [
    true,
    1,
    1.2,
    "myString",
    [
      false,
      2
    ],
    {
      "field1": 3,
      "field2": [
        4,
        "myString"
      ],
      "field3": {
        "childField": 5
      }
    }
  ]
}
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="executematlabscriptlong-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[MatlabScriptOutput](#schemamatlabscriptoutput)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## executeMatlabScriptShort

<a id="opIdexecuteMatlabScriptShort"></a>

> Code samples

```http
POST /ep/execute-short-matlab-script HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/execute-short-matlab-script`

*Execute short-running MATLAB script*

Execute a short-running MATLAB script using the given parameters. If the time it takes for the script to end is longer than the request timeout of your REST client, this request may fail. In this scenario the <b>Execute a long-running MATLAB script</b> method should be used.

> Body parameter

```json
{
  "scriptName": "my_script",
  "outArgs": 3,
  "inArgs": [
    true,
    1,
    1.2,
    "myString",
    [
      false,
      2
    ],
    {
      "field1": 3,
      "field2": [
        4,
        "myString"
      ],
      "field3": {
        "childField": 5
      }
    }
  ]
}
```

<h3 id="executematlabscriptshort-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[MatlabScriptInput](#schemamatlabscriptinput)|true|Information needed to execute the MATLAB script|

> Example responses

> 200 Response

```json
{
  "outArgs": [
    true,
    1,
    1.2,
    "myString",
    [
      false,
      2
    ],
    {
      "field1": 3,
      "field2": [
        4,
        "myString"
      ],
      "field3": {
        "childField": 5
      }
    }
  ]
}
```

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="executematlabscriptshort-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[MatlabScriptOutput](#schemamatlabscriptoutput)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-model-coverage-reports">Model Coverage Reports</h1>

Creates RBT or B2B model coverage reports.

## createModelCoverageReportOnFolder

<a id="opIdcreateModelCoverageReportOnFolder"></a>

> Code samples

```http
POST /ep/folders/{folder__uid}/model-coverage-reports HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/{folder__uid}/model-coverage-reports`

*Create a report for a folder*

<b>Long running task</b> Create RBT or B2B model coverage report for given folder.

> Body parameter

```json
{
  "type": "B2B",
  "simulationKind": "SL MIL",
  "useShortCircuitLogic": true
}
```

<h3 id="createmodelcoveragereportonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The folder UID for which to create the model coverage report.|
|body|body|[ModelCoverageReportInfo](#schemamodelcoveragereportinfo)|true|The model coverage report info object containing all parameter.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"Cannot start a new long-running operation: Previous operation is not finished, yet!"
```

<h3 id="createmodelcoveragereportonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createModelCoverageReportOnFolder

> Code samples

```http
POST /ep/folders/{folder__uid}/model-coverage-reports HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/model-coverage-reports`

The long running task status and result will be transmitted.

<h3 id="createmodelcoveragereportonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createmodelcoveragereportonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createModelCoverageReportOnFolders

<a id="opIdcreateModelCoverageReportOnFolders"></a>

> Code samples

```http
POST /ep/folders/model-coverage-reports HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/model-coverage-reports`

*Create a report for a list of folders*

<b>Long running task</b> Create RBT or B2B model coverage report for a list of folders. <br>In the RBT use-case, RBTestCases from the folders will be used to generate the report. <br>In the B2B use-case, RBTestCases and Stimuli-Vectors from the folders will be used to generate the report.

> Body parameter

```json
{
  "type": "B2B",
  "simulationKind": "SL MIL",
  "folderUIDs": "21L",
  "useShortCircuitLogic": true
}
```

<h3 id="createmodelcoveragereportonfolders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ModelCoverageReportOnFoldersInfo](#schemamodelcoveragereportonfoldersinfo)|true|The model coverage report info object containing all parameter.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"Cannot start a new long-running operation: Previous operation is not finished, yet!"
```

<h3 id="createmodelcoveragereportonfolders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createModelCoverageReportOnFolders

> Code samples

```http
POST /ep/folders/model-coverage-reports HTTP/1.1

Accept: application/json

```

`POST /ep/folders/model-coverage-reports`

The long running task status and result will be transmitted.

<h3 id="createmodelcoveragereportonfolders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createmodelcoveragereportonfolders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createModelCoverageReportOnScope

<a id="opIdcreateModelCoverageReportOnScope"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/model-coverage-reports HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/scopes/{scope__uid}/model-coverage-reports`

*Create a report for a scope*

<b>Long running task</b> Create RBT or B2B model coverage report on given scope.

> Body parameter

```json
{
  "type": "B2B",
  "simulationKind": "SL MIL",
  "useShortCircuitLogic": true
}
```

<h3 id="createmodelcoveragereportonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The scope UID for which to create the model coverage report.|
|body|body|[ModelCoverageReportInfo](#schemamodelcoveragereportinfo)|true|The model coverage report info object containing all parameter.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createmodelcoveragereportonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createModelCoverageReportOnScope

> Code samples

```http
POST /ep/scopes/{scope__uid}/model-coverage-reports HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/model-coverage-reports`

The long running task status and result will be transmitted.

<h3 id="createmodelcoveragereportonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createmodelcoveragereportonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getReports_5

<a id="opIdgetReports_5"></a>

> Code samples

```http
GET /ep/model-coverage-reports HTTP/1.1

Accept: application/json

```

`GET /ep/model-coverage-reports`

*Get a list of reports*

Retrieve all model coverage reports of the specified testing use-case from the profile.

<h3 id="getreports_5-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|coverage-type|query|string|false|The model coverage testing use-case.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|coverage-type|RBT|
|coverage-type|B2B|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "reportName": "Report 9/27/20 07:43 AM",
    "reportType": "<Report Type>"
  }
]
```

> 404 Response

```
"No reports were found."
```

<h3 id="getreports_5-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getreports_5-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Report](#schemareport)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» reportName|string|false|none|Name of the report.|
|» reportType|string|false|none|Type of the report.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-formal-specification-reports">Formal Specification Reports</h1>

Formal Specification Reports

## getAllFormalSpecificationReports

<a id="opIdgetAllFormalSpecificationReports"></a>

> Code samples

```http
GET /ep/formal-specification-reports HTTP/1.1

Accept: application/json

```

`GET /ep/formal-specification-reports`

*Get all reports*

Get all formal specification reports from the profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "reportName": "Report 9/27/20 07:43 AM",
    "reportType": "<Report Type>"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getallformalspecificationreports-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getallformalspecificationreports-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Report](#schemareport)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» reportName|string|false|none|Name of the report.|
|» reportType|string|false|none|Type of the report.|

<aside class="success">
This operation does not require authentication
</aside>

## createFormalSpecificationReport

<a id="opIdcreateFormalSpecificationReport"></a>

> Code samples

```http
POST /ep/formal-specification-reports HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/formal-specification-reports`

*Create a formal specification report*

Create a formal specification report on a list of formal specification UID's.

> Body parameter

```json
{
  "UIDs": [
    "2UPb",
    "3rH8"
  ]
}
```

<h3 id="createformalspecificationreport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ReportCreationInfo](#schemareportcreationinfo)|true|Provide the list of formal specification UIDs for which to create the formal specification report. These UIDs should be from the same instance, for example all should be formal requirement UIDs.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createformalspecificationreport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createFormalSpecificationReport

> Code samples

```http
POST /ep/formal-specification-reports HTTP/1.1

Accept: application/json

```

`POST /ep/formal-specification-reports`

The long running task status and result will be transmitted.

<h3 id="createformalspecificationreport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createformalspecificationreport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-formal-specifications">Formal Specifications</h1>

Handle Formal Specifications.

## getAllEnvironmentalAssumption

<a id="opIdgetAllEnvironmentalAssumption"></a>

> Code samples

```http
GET /ep/environmental-assumptions HTTP/1.1

Accept: application/json

```

`GET /ep/environmental-assumptions`

*Get all environmental assumptions*

Get all environmental assumptions present on active profile, or from the specified scope-uid.

<h3 id="getallenvironmentalassumption-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|query|string|false|The UID of scope from which to get the environmental assumptions.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "EA_FR1",
    "description": "Environmental assumption description",
    "scopeUID": "u378",
    "draft": "false",
    "errors": "There is an empty place in the Universal Pattern."
  }
]
```

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="getallenvironmentalassumption-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getallenvironmentalassumption-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[EnvironmentalAssumption](#schemaenvironmentalassumption)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|true|none|The name of the environmental assumption.|
|» description|string|true|none|The description of the environmental assumption.|
|» scopeUID|string|true|none|The unique identifier (UID) of the scope this object belongs to.|
|» draft|string|false|none|States whether or not the FormalRequirement is in Draft-Mode.|
|» errors|[string]|false|none|List of errors|

<aside class="success">
This operation does not require authentication
</aside>

## getAllFormalRequirements

<a id="opIdgetAllFormalRequirements"></a>

> Code samples

```http
GET /ep/formal-requirements HTTP/1.1

Accept: application/json

```

`GET /ep/formal-requirements`

*Get all formal requirements*

Get all formal requirements from the profile, or from the specified scope-uid.

<h3 id="getallformalrequirements-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|query|string|false|The UID of scope from which to get the formal requirements.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "FR_1",
    "description": "Formal requirement description",
    "scopeUID": "u378",
    "draft": "false",
    "errors": "There is an empty place in the Universal Pattern."
  }
]
```

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="getallformalrequirements-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getallformalrequirements-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[FormalSpecification](#schemaformalspecification)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|true|none|The name of the formal requirement.|
|» description|string|true|none|The description of the formal requirement.|
|» scopeUID|string|true|none|The unique identifier (UID) of the scope this object belongs to.|
|» draft|string|false|none|States whether or not the FormalRequirement is in Draft-Mode.|
|» errors|[string]|false|none|List of errors|

<aside class="success">
This operation does not require authentication
</aside>

## getEnvironmentalAssumptionsForFormalRequirement

<a id="opIdgetEnvironmentalAssumptionsForFormalRequirement"></a>

> Code samples

```http
GET /ep/formal-requirements/{formal__requirement__uid}/environmental-assumptions HTTP/1.1

Accept: application/json

```

`GET /ep/formal-requirements/{formal__requirement__uid}/environmental-assumptions`

*Get all environmental assumptions from a formal requirement*

Use this command to retrieve the environmental assumptions from a formal requirement.

<h3 id="getenvironmentalassumptionsforformalrequirement-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|formal-requirement-uid|path|string|true|The uid of the formal requirement for which all environmental assumptions should be returned.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "EA_FR1",
    "description": "Environmental assumption description",
    "scopeUID": "u378",
    "draft": "false",
    "errors": "There is an empty place in the Universal Pattern."
  }
]
```

> 400 Response

```
"Illegal argument. path = {VALUE}"
```

<h3 id="getenvironmentalassumptionsforformalrequirement-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getenvironmentalassumptionsforformalrequirement-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[EnvironmentalAssumption](#schemaenvironmentalassumption)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|true|none|The name of the environmental assumption.|
|» description|string|true|none|The description of the environmental assumption.|
|» scopeUID|string|true|none|The unique identifier (UID) of the scope this object belongs to.|
|» draft|string|false|none|States whether or not the FormalRequirement is in Draft-Mode.|
|» errors|[string]|false|none|List of errors|

<aside class="success">
This operation does not require authentication
</aside>

## exportSpec

<a id="opIdexportSpec"></a>

> Code samples

```http
POST /ep/specifications-export HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/specifications-export`

*Export a SPEC file*

<b>Long running task</b> Exports the given formal specifications belonging to the same scope to the specified SPEC file.

> Body parameter

```json
{
  "specFile": "C:/Desktop/mySpecFile.spec",
  "archUid": "A1b",
  "formalSpecificationUids": "2yy"
}
```

<h3 id="exportspec-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SpecExport](#schemaspecexport)|true|The configuration to use for exporting a SPEC file.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exportspec-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## exportSpec

> Code samples

```http
POST /ep/specifications-export HTTP/1.1

Accept: text/plain

```

`POST /ep/specifications-export`

The long running task status and result will be transmitted.

<h3 id="exportspec-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```
"{Formal specifications successfully exported to SPEC file.}"
```

<h3 id="exportspec-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## importSpecFromScope

<a id="opIdimportSpecFromScope"></a>

> Code samples

```http
POST /ep/specifications-import HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/specifications-import`

*Import a SPEC file*

Imports formal specifications from the specified SPEC file.<br><b>Long running task</b> Specify artifact existing policy, one of EXTEND_NAME, OVERWRITE, or SKIP. By default it will be used 'EXTEND_NAME'.

> Body parameter

```json
{
  "specPath": "C:/Desktop/mySpecFile.spec",
  "scopeId": "27Y",
  "isDraft": false,
  "optionParam": "EXTEND_NAME"
}
```

<h3 id="importspecfromscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SpecImport](#schemaspecimport)|true|The configuration to use for importing a SPEC file.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importspecfromscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## importSpecFromScope

> Code samples

```http
POST /ep/specifications-import HTTP/1.1

Accept: text/plain

```

`POST /ep/specifications-import`

The long running task status and result will be transmitted.

<h3 id="importspecfromscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importspecfromscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Imported. When the long running task is finished, the operation result will be available.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-requirements-import">Requirements Import</h1>

Import Requirements.

## executeImport

<a id="opIdexecuteImport"></a>

> Code samples

```http
POST /ep/requirements-import HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/requirements-import`

*Import requirements*

Import requirements by specifying the kind of requirements.

> Body parameter

```json
{
  "kind": "One of EXCEL or DOORS",
  "nameAttribute": "REQ_ID",
  "descriptionAttribute": "Description",
  "additionalAttributes": [
    "string"
  ],
  "settings": [
    {
      "key": "projectName_attr",
      "value": "InformalRequirements"
    }
  ]
}
```

<h3 id="executeimport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RequirementImportRestConfig](#schemarequirementimportrestconfig)|true|The configuration used for importing requirements.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="executeimport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## executeImport

> Code samples

```http
POST /ep/requirements-import HTTP/1.1

Accept: application/json

```

`POST /ep/requirements-import`

The long running task status and result will be transmitted.

<h3 id="executeimport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
"Object containing info about RequirementSource"
```

> 400 Response

```
"Import failed. Exception: {EXCEPTION MESSAGE}"
```

<h3 id="executeimport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is available in the 'result' field of the response object.|[RequirementSource](#schemarequirementsource)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Import failed.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getDoorsRequirementImportConfig

<a id="opIdgetDoorsRequirementImportConfig"></a>

> Code samples

```http
GET /ep/requirements-import/doors HTTP/1.1

Accept: application/json

```

`GET /ep/requirements-import/doors`

*Get the DOORS™ configuration template*

Get the configuration with default settings for importing different kinds of requirements.

> Example responses

> 200 Response

```json
{
  "kind": "One of EXCEL or DOORS",
  "nameAttribute": "REQ_ID",
  "descriptionAttribute": "Description",
  "additionalAttributes": [
    "string"
  ],
  "settings": [
    {
      "key": "projectName_attr",
      "value": "InformalRequirements"
    }
  ]
}
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getdoorsrequirementimportconfig-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[RequirementImportRestConfig](#schemarequirementimportrestconfig)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## getExcelRequirementImportConfig

<a id="opIdgetExcelRequirementImportConfig"></a>

> Code samples

```http
GET /ep/requirements-import/excel HTTP/1.1

Accept: application/json

```

`GET /ep/requirements-import/excel`

*Get the Excel™ configuration template*

Get the configuration with default settings for importing different kinds of requirements.

> Example responses

> 200 Response

```json
{
  "kind": "One of EXCEL or DOORS",
  "nameAttribute": "REQ_ID",
  "descriptionAttribute": "Description",
  "additionalAttributes": [
    "string"
  ],
  "settings": [
    {
      "key": "projectName_attr",
      "value": "InformalRequirements"
    }
  ]
}
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getexcelrequirementimportconfig-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[RequirementImportRestConfig](#schemarequirementimportrestconfig)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-requirements">Requirements</h1>

Retrieve Requirements, Linked Requirements, or Requirement Sources.

## getAllRequirementSources

<a id="opIdgetAllRequirementSources"></a>

> Code samples

```http
GET /ep/requirements-sources HTTP/1.1

Accept: application/json

```

`GET /ep/requirements-sources`

*Get all requirement sources*

Get all requirement sources found on the opened profile.

> Example responses

> 200 Response

```json
[
  "Object containing info about RequirementSource"
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getallrequirementsources-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getallrequirementsources-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequirementSource](#schemarequirementsource)]|false|none|none|
|» kind|string|true|none|The kind of this requirement source. The kind identifies this source to be from a specific requirement management tool.|
|» settings|[[RequirementSetting](#schemarequirementsetting)]|true|none|[A list with requirement settings.For EXCEL requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, excel_file_path, projectName_attr (or excel_sheet_name), excel_id_attr, excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, projectName_attr, doors_module_qualifier, doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.]|
|»» key|string|true|none|For EXCEL requirement kind, the following keys are mandatory: excel_file_path, projectName_attr, excel_id_attr. The optional setting keys are: excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys are mandatory: projectName_attr, doors_module_qualifier. The optional setting keys are: doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.|
|»» value|string|true|none|Setting value|
|» definedAdditionalAttributes|[string]|false|none|none|
|» externalUUID|string|true|none|The unique ID identifying the external requirement source.|
|» name|string|true|none|The requirement source name.|
|» uid|string|true|none|The universally unique identifier of this requirement source.|

<aside class="success">
This operation does not require authentication
</aside>

## getAllRequirementsOfRequirementSource

<a id="opIdgetAllRequirementsOfRequirementSource"></a>

> Code samples

```http
GET /ep/requirements/{requirement__source__id} HTTP/1.1

Accept: application/json

```

`GET /ep/requirements/{requirement__source__id}`

*Get all requirements of a requirement source*

Get the requirements of the given requirement source id.

<h3 id="getallrequirementsofrequirementsource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|requirement-source-id|path|string|true|The UID of the requirement source.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "27T",
    "identifier": "1",
    "isRemoved": true,
    "additionalAttributes": {
      "property1": "string",
      "property2": "string"
    },
    "scopeId": "27T",
    "description": "Requirement description.",
    "name": "REQ_PW_1_1",
    "dateOfLastUpdate": "01-Jan-2020 12:00:00",
    "requirementSource": "Object containing info about RequirementSource"
  }
]
```

> 404 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getallrequirementsofrequirementsource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getallrequirementsofrequirementsource-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Requirement](#schemarequirement)]|false|none|none|
|» uid|string|true|none|The universally unique identifier.|
|» identifier|string|true|none|The requirement identifier (e.g. a chapter number within DOORS).|
|» isRemoved|boolean|false|none|Value meaning whether this requirement has been removed within the requirement management tool.|
|» additionalAttributes|object|false|none|Map containing all additional attributes.|
|»» **additionalProperties**|string|false|none|Map containing all additional attributes.|
|» scopeId|string|true|none|The scope id this requirement is directly linked to.|
|» description|string|true|none|The requirement description.|
|» name|string|true|none|The requirement name.|
|» dateOfLastUpdate|string|true|none|The requirement last update date.|
|» requirementSource|[RequirementSource](#schemarequirementsource)|true|none|none|
|»» kind|string|true|none|The kind of this requirement source. The kind identifies this source to be from a specific requirement management tool.|
|»» settings|[[RequirementSetting](#schemarequirementsetting)]|true|none|[A list with requirement settings.For EXCEL requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, excel_file_path, projectName_attr (or excel_sheet_name), excel_id_attr, excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, projectName_attr, doors_module_qualifier, doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.]|
|»»» key|string|true|none|For EXCEL requirement kind, the following keys are mandatory: excel_file_path, projectName_attr, excel_id_attr. The optional setting keys are: excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys are mandatory: projectName_attr, doors_module_qualifier. The optional setting keys are: doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.|
|»»» value|string|true|none|Setting value|
|»» definedAdditionalAttributes|[string]|false|none|none|
|»» externalUUID|string|true|none|The unique ID identifying the external requirement source.|
|»» name|string|true|none|The requirement source name.|
|»» uid|string|true|none|The universally unique identifier of this requirement source.|

<aside class="success">
This operation does not require authentication
</aside>

## getLinkedRequirementsOnScope

<a id="opIdgetLinkedRequirementsOnScope"></a>

> Code samples

```http
GET /ep/scopes/{scope__id}/linked-requirements HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__id}/linked-requirements`

*Get all requirements for a scope*

Get the linked requirements of this given scope id.

<h3 id="getlinkedrequirementsonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-id|path|string|true|The UID of the scope id.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "27T",
    "identifier": "1",
    "isRemoved": true,
    "additionalAttributes": {
      "property1": "string",
      "property2": "string"
    },
    "scopeId": "27T",
    "description": "Requirement description.",
    "name": "REQ_PW_1_1",
    "dateOfLastUpdate": "01-Jan-2020 12:00:00",
    "requirementSource": "Object containing info about RequirementSource"
  }
]
```

> 404 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getlinkedrequirementsonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getlinkedrequirementsonscope-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Requirement](#schemarequirement)]|false|none|none|
|» uid|string|true|none|The universally unique identifier.|
|» identifier|string|true|none|The requirement identifier (e.g. a chapter number within DOORS).|
|» isRemoved|boolean|false|none|Value meaning whether this requirement has been removed within the requirement management tool.|
|» additionalAttributes|object|false|none|Map containing all additional attributes.|
|»» **additionalProperties**|string|false|none|Map containing all additional attributes.|
|» scopeId|string|true|none|The scope id this requirement is directly linked to.|
|» description|string|true|none|The requirement description.|
|» name|string|true|none|The requirement name.|
|» dateOfLastUpdate|string|true|none|The requirement last update date.|
|» requirementSource|[RequirementSource](#schemarequirementsource)|true|none|none|
|»» kind|string|true|none|The kind of this requirement source. The kind identifies this source to be from a specific requirement management tool.|
|»» settings|[[RequirementSetting](#schemarequirementsetting)]|true|none|[A list with requirement settings.For EXCEL requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, excel_file_path, projectName_attr (or excel_sheet_name), excel_id_attr, excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, projectName_attr, doors_module_qualifier, doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.]|
|»»» key|string|true|none|For EXCEL requirement kind, the following keys are mandatory: excel_file_path, projectName_attr, excel_id_attr. The optional setting keys are: excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys are mandatory: projectName_attr, doors_module_qualifier. The optional setting keys are: doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.|
|»»» value|string|true|none|Setting value|
|»» definedAdditionalAttributes|[string]|false|none|none|
|»» externalUUID|string|true|none|The unique ID identifying the external requirement source.|
|»» name|string|true|none|The requirement source name.|
|»» uid|string|true|none|The universally unique identifier of this requirement source.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-code-analysis-reports-rbt">Code Analysis Reports RBT</h1>

Creates requirement-based code analysis reports.

## createCodeAnalysisReportOnFolder_1

<a id="opIdcreateCodeAnalysisReportOnFolder_1"></a>

> Code samples

```http
POST /ep/folders/{folder__uid}/code-analysis-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/code-analysis-reports-rbt`

*Create a report on a folder*

<b>Long running task</b> Create an RBT code analysis report on a given folder.

<h3 id="createcodeanalysisreportonfolder_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The folder UID for which to create an RBT code analysis report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createcodeanalysisreportonfolder_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createCodeAnalysisReportOnFolder_1

> Code samples

```http
POST /ep/folders/{folder__uid}/code-analysis-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/code-analysis-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createcodeanalysisreportonfolder_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"All folders need to be of kind: Requirement-based Test Case."
```

<h3 id="createcodeanalysisreportonfolder_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is available in the 'result' field of the response object.|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createCodeAnalysisReportOnFolders_1

<a id="opIdcreateCodeAnalysisReportOnFolders_1"></a>

> Code samples

```http
POST /ep/folders/code-analysis-reports-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/code-analysis-reports-rbt`

*Create a report on a list of folders*

Create an RBT code analysis report on given folders.

> Body parameter

```json
{
  "UIDs": [
    "2UPb",
    "3rH8"
  ]
}
```

<h3 id="createcodeanalysisreportonfolders_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ReportCreationInfo](#schemareportcreationinfo)|true|Provide the list of folder UIDs for which to create the RBT code analysis report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createcodeanalysisreportonfolders_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createCodeAnalysisReportOnFolders_1

> Code samples

```http
POST /ep/folders/code-analysis-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/folders/code-analysis-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createcodeanalysisreportonfolders_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"All folders need to be of kind: Requirement-based Test Case."
```

<h3 id="createcodeanalysisreportonfolders_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is available in the 'result' field of the response object.|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createCodeAnalysisReportOnRequirementsSource

<a id="opIdcreateCodeAnalysisReportOnRequirementsSource"></a>

> Code samples

```http
POST /ep/requirements-sources/{requirements__source__uid}/code-analysis-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/requirements-sources/{requirements__source__uid}/code-analysis-reports-rbt`

*Create a report on a requirements source*

Create an RBT code analysis report on a given requirements source UID.

<h3 id="createcodeanalysisreportonrequirementssource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|requirements-source-uid|path|string|true|The requirements source UID for which to create RBT code analysis report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createcodeanalysisreportonrequirementssource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createCodeAnalysisReportOnRequirementsSource

> Code samples

```http
POST /ep/requirements-sources/{requirements__source__uid}/code-analysis-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/requirements-sources/{requirements__source__uid}/code-analysis-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createcodeanalysisreportonrequirementssource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 404 Response

```
"No requirements source was found for the given UID."
```

<h3 id="createcodeanalysisreportonrequirementssource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is available in the 'result' field of the response object.|[Report](#schemareport)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createCodeAnalysisReportOnRequirementsSources

<a id="opIdcreateCodeAnalysisReportOnRequirementsSources"></a>

> Code samples

```http
POST /ep/requirements-sources/code-analysis-reports-rbt HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/requirements-sources/code-analysis-reports-rbt`

*Create a report on requirements sources*

Create an RBT code analysis report on given requirements sources.

> Body parameter

```json
{
  "UIDs": [
    "2UPb",
    "3rH8"
  ]
}
```

<h3 id="createcodeanalysisreportonrequirementssources-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ReportCreationInfo](#schemareportcreationinfo)|true|Provide the list of requirements sources UIDs for which to create the RBT code analysis report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createcodeanalysisreportonrequirementssources-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createCodeAnalysisReportOnRequirementsSources

> Code samples

```http
POST /ep/requirements-sources/code-analysis-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/requirements-sources/code-analysis-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createcodeanalysisreportonrequirementssources-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 400 Response

```
"No requirements sources were found for the given UID."
```

<h3 id="createcodeanalysisreportonrequirementssources-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is available in the 'result' field of the response object.|[Report](#schemareport)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createCodeAnalysisReportOnScope_1

<a id="opIdcreateCodeAnalysisReportOnScope_1"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/code-analysis-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/code-analysis-reports-rbt`

*Create a report on scope*

Create an RBT code analysis report on a given scope.

<h3 id="createcodeanalysisreportonscope_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The scope UID for which to create RBT code analysis report.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createcodeanalysisreportonscope_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createCodeAnalysisReportOnScope_1

> Code samples

```http
POST /ep/scopes/{scope__uid}/code-analysis-reports-rbt HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/code-analysis-reports-rbt`

The long running task status and result will be transmitted.

<h3 id="createcodeanalysisreportonscope_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 404 Response

```
"No scope was found for the given UID."
```

<h3 id="createcodeanalysisreportonscope_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is available in the 'result' field of the response object.|[Report](#schemareport)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getReports_6

<a id="opIdgetReports_6"></a>

> Code samples

```http
GET /ep/code-analysis-reports-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/code-analysis-reports-rbt`

*Get all reports*

Retrieve all RBT code analysis reports from the profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "reportName": "Report 9/27/20 07:43 AM",
    "reportType": "<Report Type>"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getreports_6-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getreports_6-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Report](#schemareport)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» reportName|string|false|none|Name of the report.|
|» reportType|string|false|none|Type of the report.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-code-coverage-robustness-check-rbt">Code Coverage/Robustness Check RBT</h1>

Retrieve code coverage/robustness checks details and results in RBT.

## getCodeCoverageGoalsByRequirementSource

<a id="opIdgetCodeCoverageGoalsByRequirementSource"></a>

> Code samples

```http
GET /ep/requirements-sources/{requirement__source__uid}/coverage-details-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/requirements-sources/{requirement__source__uid}/coverage-details-rbt`

*Get coverage details for a requirement source*

Get code coverage/robustness checks details for a requirement source. Some filters can be applied.

<h3 id="getcodecoveragegoalsbyrequirementsource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|requirement-source-uid|path|string|true|The UID of the requirement source|
|statuses|query|array[string]|false|The status filter for code coverage/robustness check goals. Possible values: COVERED, UNKNOWN, UNREACHABLE_INF, UNREACHABLE_N, INCONSISTENT, UNKNOWN_JUSTIFIED, UNREACHABLE_INF_JUSTIFIED, UNREACHABLE_N_JUSTIFIED. Can also specify multiple options. Can also be empty, in which case the results are shown for all statuses.|
|goal-types|query|array[string]|false|The goal type filter for code coverage/robustness check goals. Possible values for code coverage goals: STM(Statement), C(Condition), D(Decision/Branch), CDC(C/DC), MCDC(C/DC and MC/DC), F(Function), SC(Switch-Case), RO(Relational Operator),  FC(Function Call). Possible values for robustness check goals are: DZ(Division by Zero), CA(Downcast). Can also specify multiple options. Can also be empty, in which case the results are shown for all goal types.|
|files|query|array[string]|false|List of file filters for code coverage/robustness check goals. If list is empty the results are shown for all files.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|statuses|COVERED|
|statuses|UNKNOWN|
|statuses|UNREACHABLE_INF|
|statuses|UNREACHABLE_N|
|statuses|INCONSISTENT|
|statuses|UNKNOWN_JUSTIFIED|
|statuses|UNREACHABLE_N_JUSTIFIED|
|statuses|UNREACHABLE_INF_JUSTIFIED|
|goal-types|STM|
|goal-types|D|
|goal-types|C|
|goal-types|MCDC|
|goal-types|F|
|goal-types|FC|
|goal-types|SC|
|goal-types|RO|
|goal-types|CDC|
|goal-types|DZ|
|goal-types|CA|

> Example responses

> 200 Response

```json
[
  {
    "pll": "STM:1",
    "type": "Statement",
    "line": 390,
    "file": "power_widow_control.c",
    "properties": [
      {
        "pll": "STM:76:0",
        "status": "Unknown",
        "coveringVectors": [
          "testCase"
        ]
      }
    ],
    "expression": "(obstacle_position!=0)",
    "blocks": [
      "string"
    ],
    "comment": "Comment",
    "justified": true
  }
]
```

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="getcodecoveragegoalsbyrequirementsource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getcodecoveragegoalsbyrequirementsource-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CodeCoverageGoal](#schemacodecoveragegoal)]|false|none|none|
|» pll|string|false|none|PLL string of the coverage goal.|
|» type|string|false|none|Goal type of the coverage goal.|
|» line|integer(int32)|false|none|The line number of the location where the coverage goal is located in the file.|
|» file|string|false|none|The file name where the coverage property can be located.|
|» properties|[[CodeCoverageProperty](#schemacodecoverageproperty)]|false|none|[A list with coverage goal properties.]|
|»» pll|string|false|none|PLL string of the coverage property.|
|»» status|string|false|none|Status of the coverage property.|
|»» coveringVectors|[string]|false|none|none|
|» expression|string|false|none|Expression of the coverage goal.|
|» blocks|[string]|false|none|none|
|» comment|string|false|none|The comment.|
|» justified|boolean|false|none|If this goal is justified|

<aside class="success">
This operation does not require authentication
</aside>

## getCodeCoverageGoalsByScope_1

<a id="opIdgetCodeCoverageGoalsByScope_1"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/coverage-details-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/coverage-details-rbt`

*Get coverage details for a scope*

Get all code coverage/robustness checks details for a scope. Some filters can be applied.

<h3 id="getcodecoveragegoalsbyscope_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope|
|statuses|query|array[string]|false|The status filter for code coverage/robustness check goals. Possible values: COVERED, UNKNOWN, UNREACHABLE_INF, UNREACHABLE_N, INCONSISTENT, UNKNOWN_JUSTIFIED, UNREACHABLE_INF_JUSTIFIED, UNREACHABLE_N_JUSTIFIED. Can also specify multiple options. <br>Can also be empty, in which case the results are shown for all statuses.|
|goal-types|query|array[string]|false|The goal type filter for code coverage/robustness check goals. Possible values for code coverage goals: STM(Statement), C(Condition), D(Decision/Branch), CDC(C/DC), MCDC(C/DC and MC/DC), F(Function), SC(Switch-Case), RO(Relational Operator),  FC(Function Call).<br>Possible values for robustness check goals are: DZ(Division by Zero), CA(Downcast). Can also specify multiple options. Can also be empty, in which case the results are shown for all goal types.|
|files|query|array[string]|false|List of file filters for code coverage/robustness check goals. If list is empty the results are shown for all files.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|statuses|COVERED|
|statuses|UNKNOWN|
|statuses|UNREACHABLE_INF|
|statuses|UNREACHABLE_N|
|statuses|INCONSISTENT|
|statuses|UNKNOWN_JUSTIFIED|
|statuses|UNREACHABLE_N_JUSTIFIED|
|statuses|UNREACHABLE_INF_JUSTIFIED|
|goal-types|STM|
|goal-types|D|
|goal-types|C|
|goal-types|MCDC|
|goal-types|F|
|goal-types|FC|
|goal-types|SC|
|goal-types|RO|
|goal-types|CDC|
|goal-types|DZ|
|goal-types|CA|

> Example responses

> 200 Response

```json
[
  {
    "pll": "STM:1",
    "type": "Statement",
    "line": 390,
    "file": "power_widow_control.c",
    "properties": [
      {
        "pll": "STM:76:0",
        "status": "Unknown",
        "coveringVectors": [
          "testCase"
        ]
      }
    ],
    "expression": "(obstacle_position!=0)",
    "blocks": [
      "string"
    ],
    "comment": "Comment",
    "justified": true
  }
]
```

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="getcodecoveragegoalsbyscope_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getcodecoveragegoalsbyscope_1-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CodeCoverageGoal](#schemacodecoveragegoal)]|false|none|none|
|» pll|string|false|none|PLL string of the coverage goal.|
|» type|string|false|none|Goal type of the coverage goal.|
|» line|integer(int32)|false|none|The line number of the location where the coverage goal is located in the file.|
|» file|string|false|none|The file name where the coverage property can be located.|
|» properties|[[CodeCoverageProperty](#schemacodecoverageproperty)]|false|none|[A list with coverage goal properties.]|
|»» pll|string|false|none|PLL string of the coverage property.|
|»» status|string|false|none|Status of the coverage property.|
|»» coveringVectors|[string]|false|none|none|
|» expression|string|false|none|Expression of the coverage goal.|
|» blocks|[string]|false|none|none|
|» comment|string|false|none|The comment.|
|» justified|boolean|false|none|If this goal is justified|

<aside class="success">
This operation does not require authentication
</aside>

## getCodeCoverageResultByRequirementSource

<a id="opIdgetCodeCoverageResultByRequirementSource"></a>

> Code samples

```http
GET /ep/requirements-sources/{requirements__source__uid}/coverage-results-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/requirements-sources/{requirements__source__uid}/coverage-results-rbt`

*Get coverage results for a requirement source*

Get the code coverage and robustness checks results for a requirement source. Goal type filters can be applied.

<h3 id="getcodecoverageresultbyrequirementsource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|requirements-source-uid|path|string|true|The UID of the requirement source|
|goal-types|query|array[string]|false|The goal type filter for code coverage/robustness check goals. Possible values for code coverage goals: STM(Statement), C(Condition), D(Decision/Branch), CDC(C/DC), MCDC(C/DC and MC/DC), F(Function), SC(Switch-Case), RO(Relational Operator),  FC(Function Call). Possible values for robustness check goals are: DZ(Division by Zero), CA(Downcast). Can also specify multiple options. Can also be empty, in which case the results are shown for all goal types.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|goal-types|STM|
|goal-types|D|
|goal-types|C|
|goal-types|MCDC|
|goal-types|F|
|goal-types|FC|
|goal-types|SC|
|goal-types|RO|
|goal-types|CDC|
|goal-types|DZ|
|goal-types|CA|

> Example responses

> 200 Response

```json
{
  "CDCCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "CDCPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "ConditionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "ConditionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DecisionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DecisionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "FunctionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "FunctionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "FunctionCallCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "FunctionCallPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "MCDCCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "MCDCPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "RelationalOperatorCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "RelationalOperatorPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "StatementCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "StatementPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "SwitchCaseCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "SwitchCasePropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DivisionByZeroCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DivisionByZeroPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DownCastCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DownCastPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "codeCoverageComment": "My code coverage overview comment.",
  "robustnessCoverageComment": "My robustness checks overview comment."
}
```

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="getcodecoverageresultbyrequirementsource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[CodeCoverageResult](#schemacodecoverageresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## getCodeCoverageResultByScope_1

<a id="opIdgetCodeCoverageResultByScope_1"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/coverage-results-rbt HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/coverage-results-rbt`

*Get coverage results for a scope*

Get the code coverage and robustness checks results for a scope. Goal type filters can be applied.

<h3 id="getcodecoverageresultbyscope_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope|
|goal-types|query|array[string]|false|The goal type filter for code coverage/robustness check goals. Possible values for code coverage goals: STM(Statement), C(Condition), D(Decision/Branch), CDC(C/DC), MCDC(C/DC and MC/DC), F(Function), SC(Switch-Case), RO(Relational Operator),  FC(Function Call). Possible values for robustness check goals are: DZ(Division by Zero), CA(Downcast). Can also specify multiple options. Can also be empty, in which case the results are shown for all goal types.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|goal-types|STM|
|goal-types|D|
|goal-types|C|
|goal-types|MCDC|
|goal-types|F|
|goal-types|FC|
|goal-types|SC|
|goal-types|RO|
|goal-types|CDC|
|goal-types|DZ|
|goal-types|CA|

> Example responses

> 200 Response

```json
{
  "CDCCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "CDCPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "ConditionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "ConditionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DecisionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DecisionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "FunctionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "FunctionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "FunctionCallCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "FunctionCallPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "MCDCCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "MCDCPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "RelationalOperatorCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "RelationalOperatorPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "StatementCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "StatementPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "SwitchCaseCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "SwitchCasePropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DivisionByZeroCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DivisionByZeroPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DownCastCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DownCastPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "codeCoverageComment": "My code coverage overview comment.",
  "robustnessCoverageComment": "My robustness checks overview comment."
}
```

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="getcodecoverageresultbyscope_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[CodeCoverageResult](#schemacodecoverageresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## setGoalComment_1

<a id="opIdsetGoalComment_1"></a>

> Code samples

```http
POST /ep/coverage-goals/set-comment-rbt HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/coverage-goals/set-comment-rbt`

*Set goal comments*

Set comments of code coverage and robustness check goals.

> Body parameter

```json
[
  {
    "pll": "F:0",
    "comment": "MyComment"
  }
]
```

<h3 id="setgoalcomment_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[GoalComment](#schemagoalcomment)|true|none|

> Example responses

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="setgoalcomment_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## setGoalJustified_1

<a id="opIdsetGoalJustified_1"></a>

> Code samples

```http
POST /ep/coverage-goals/set-justified-rbt HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/coverage-goals/set-justified-rbt`

*Set goal justified status*

Set justified status of code coverage and robustness check goals.

> Body parameter

```json
{
  "justified": true,
  "plls": [
    "2fa"
  ]
}
```

<h3 id="setgoaljustified_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CodeCoverageJustify](#schemacodecoveragejustify)|true|none|

> Example responses

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="setgoaljustified_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## setScopeOverviewComment_1

<a id="opIdsetScopeOverviewComment_1"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/set-coverage-overview-comment-rbt HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/scopes/{scope__uid}/set-coverage-overview-comment-rbt`

*Set overview comments*

Set the comments of code coverage overview sections.

> Body parameter

```json
[
  {
    "type": "CC_STAT",
    "comment": "myComment"
  }
]
```

<h3 id="setscopeoverviewcomment_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope|
|body|body|[OverviewComment](#schemaoverviewcomment)|true|none|

> Example responses

> 400 Response

```
"The provided input data is invalid."
```

<h3 id="setscopeoverviewcomment_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-execution-records">Execution records</h1>

Handle execution records.

## getExecutionRecords_1

<a id="opIdgetExecutionRecords_1"></a>

> Code samples

```http
GET /ep/execution-records/{execution__record__uid} HTTP/1.1

Accept: application/json

```

`GET /ep/execution-records/{execution__record__uid}`

*Get an execution record*

Get the requested execution record by UID.

<h3 id="getexecutionrecords_1-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|execution-record-uid|path|string|true|Execution record UID|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "executionConfig": "SIL",
    "name": "SIL_TestCase",
    "status": "OK",
    "folderName": "SIL simulations",
    "length": 2,
    "scopeName": "power_window_controller",
    "sourceName": "TestCase"
  }
]
```

> 404 Response

```
"No execution record was found."
```

<h3 id="getexecutionrecords_1-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getexecutionrecords_1-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ExecutionRecord](#schemaexecutionrecord)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» executionConfig|string|true|none|The execution config name|
|» name|string|true|none|The execution record name|
|» status|string|false|none|The status of execution record.Possible options: OK, WARNING, or ERROR.|
|» folderName|string|true|none|The folder name on which this execution record can be found.|
|» length|integer(int64)|true|none|The length of execution record source|
|» scopeName|string|true|none|The scope name of execution record|
|» sourceName|string|true|none|The name of execution record source|

#### Enumerated Values

|Property|Value|
|---|---|
|status|OK|
|status|WARNING|
|status|ERROR|

<aside class="success">
This operation does not require authentication
</aside>

## deleteExecutionRecord

<a id="opIddeleteExecutionRecord"></a>

> Code samples

```http
DELETE /ep/execution-records/{execution__record__uid} HTTP/1.1

Accept: application/json

```

`DELETE /ep/execution-records/{execution__record__uid}`

*Delete an execution record*

Deletes the specified execution record.

<h3 id="deleteexecutionrecord-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|execution-record-uid|path|string|true|The UID of the execution record to be deleted.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 403 Response

```
"Cannot start a new long-running operation: Previous operation is not finished, yet!"
```

<h3 id="deleteexecutionrecord-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

### Callbacks

#### Progress

**/ep/progress**

## deleteExecutionRecord

> Code samples

```http
DELETE /ep/execution-records/{execution__record__uid} HTTP/1.1

Accept: text/plain

```

`DELETE /ep/execution-records/{execution__record__uid}`

The long running task status and result will be transmitted.

<h3 id="deleteexecutionrecord-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 400 Response

```
"No execution record was found. UID = {VALUE}"
```

<h3 id="deleteexecutionrecord-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Deleted. When the long running task is finished, the operation result will be available.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## exportExecutionRecords

<a id="opIdexportExecutionRecords"></a>

> Code samples

```http
POST /ep/execution-records-export HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/execution-records-export`

*Export execution records*

<b>LONG RUNNING TASK</b> Export single or multiple execution record(s) by providing the list of the execution records which will be exported, the export directory, the export format and a list of additional options for export.

> Body parameter

```json
{
  "UIDs": "2UPb",
  "exportDirectory": "C:/RestProfiles/VectorExport",
  "exportFormat": "MDF"
}
```

<h3 id="exportexecutionrecords-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RestExecutionRecordExportInfo](#schemarestexecutionrecordexportinfo)|true|All necessary information for exporting execution records.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"The request cannot be processed. Please verify that the provided input has a valid format."
```

<h3 id="exportexecutionrecords-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## exportExecutionRecords

> Code samples

```http
POST /ep/execution-records-export HTTP/1.1

Accept: text/plain

```

`POST /ep/execution-records-export`

The long running task status and result will be transmitted.

<h3 id="exportexecutionrecords-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 200 Response

```
["exampleUID123"]
```

<h3 id="exportexecutionrecords-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Exported. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="exportexecutionrecords-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getExecutionRecords

<a id="opIdgetExecutionRecords"></a>

> Code samples

```http
GET /ep/execution-records HTTP/1.1

Accept: application/json

```

`GET /ep/execution-records`

*Get all execution records*

Get all execution records available in the profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "executionConfig": "SIL",
    "name": "SIL_TestCase",
    "status": "OK",
    "folderName": "SIL simulations",
    "length": 2,
    "scopeName": "power_window_controller",
    "sourceName": "TestCase"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getexecutionrecords-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getexecutionrecords-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ExecutionRecord](#schemaexecutionrecord)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» executionConfig|string|true|none|The execution config name|
|» name|string|true|none|The execution record name|
|» status|string|false|none|The status of execution record.Possible options: OK, WARNING, or ERROR.|
|» folderName|string|true|none|The folder name on which this execution record can be found.|
|» length|integer(int64)|true|none|The length of execution record source|
|» scopeName|string|true|none|The scope name of execution record|
|» sourceName|string|true|none|The name of execution record source|

#### Enumerated Values

|Property|Value|
|---|---|
|status|OK|
|status|WARNING|
|status|ERROR|

<aside class="success">
This operation does not require authentication
</aside>

## importExecutionRecord

<a id="opIdimportExecutionRecord"></a>

> Code samples

```http
POST /ep/execution-records HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/execution-records`

*Import execution records*

Import multiple execution records by providing the path for each file.

> Body parameter

```json
{
  "paths": [
    "C:/RestProfiles/VectorExport/executionRecord.mdf"
  ],
  "kind": "SIL",
  "folderName": "New Records",
  "folderUID": "X34",
  "referenceExternalFile": true,
  "csvDelimiter": "SEMICOLON"
}
```

<h3 id="importexecutionrecord-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RestExecutionRecordImportInfo](#schemarestexecutionrecordimportinfo)|true|All necessary information for importing an execution record to the profile.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importexecutionrecord-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/EP/progress**

## importExecutionRecord

> Code samples

```http
POST /ep/execution-records HTTP/1.1

Accept: application/json

```

`POST /ep/execution-records`

The long running task status and result will be transmitted.

<h3 id="importexecutionrecord-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "importStatus": [
    {
      "UIDs": "15Lx",
      "warnings": "Undefined value detected for signal {signal name}. A default value will be set.",
      "errors": "Invalid format in file {file location}. {Cause}."
    }
  ]
}
```

> 400 Response

```
"File {NAME} can't be imported. {CAUSE}"
```

<h3 id="importexecutionrecord-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[ImportResult](#schemaimportresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getExecutionRecordsByFolder

<a id="opIdgetExecutionRecordsByFolder"></a>

> Code samples

```http
GET /ep/folders/{folder__uid}/execution-records HTTP/1.1

Accept: application/json

```

`GET /ep/folders/{folder__uid}/execution-records`

*Get all execution records for a folder*

Get all the execution records for a given folder UID.

<h3 id="getexecutionrecordsbyfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The folder UID from which to retrieve all execution records.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "executionConfig": "SIL",
    "name": "SIL_TestCase",
    "status": "OK",
    "folderName": "SIL simulations",
    "length": 2,
    "scopeName": "power_window_controller",
    "sourceName": "TestCase"
  }
]
```

> 404 Response

```
"No Folder found with UID: {VALUE}"
```

<h3 id="getexecutionrecordsbyfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getexecutionrecordsbyfolder-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ExecutionRecord](#schemaexecutionrecord)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» executionConfig|string|true|none|The execution config name|
|» name|string|true|none|The execution record name|
|» status|string|false|none|The status of execution record.Possible options: OK, WARNING, or ERROR.|
|» folderName|string|true|none|The folder name on which this execution record can be found.|
|» length|integer(int64)|true|none|The length of execution record source|
|» scopeName|string|true|none|The scope name of execution record|
|» sourceName|string|true|none|The name of execution record source|

#### Enumerated Values

|Property|Value|
|---|---|
|status|OK|
|status|WARNING|
|status|ERROR|

<aside class="success">
This operation does not require authentication
</aside>

## moveExecutionRecords

<a id="opIdmoveExecutionRecords"></a>

> Code samples

```http
PUT /ep/folders/{folder__uid}/execution-records HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`PUT /ep/folders/{folder__uid}/execution-records`

*Move a list of execution records to a folder*

Moves the list of execution records to the requested user-defined execution record folder.

> Body parameter

```json
{
  "UIDs": "2UPb"
}
```

<h3 id="moveexecutionrecords-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The UID of user-defined execution record folder.|
|body|body|[ExecutionRecordsMoveData](#schemaexecutionrecordsmovedata)|true|Provide a list of execution record UIDs to be moved.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "executionConfig": "SIL",
    "name": "SIL_TestCase",
    "status": "OK",
    "folderName": "SIL simulations",
    "length": 2,
    "scopeName": "power_window_controller",
    "sourceName": "TestCase"
  }
]
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="moveexecutionrecords-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="moveexecutionrecords-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ExecutionRecord](#schemaexecutionrecord)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» executionConfig|string|true|none|The execution config name|
|» name|string|true|none|The execution record name|
|» status|string|false|none|The status of execution record.Possible options: OK, WARNING, or ERROR.|
|» folderName|string|true|none|The folder name on which this execution record can be found.|
|» length|integer(int64)|true|none|The length of execution record source|
|» scopeName|string|true|none|The scope name of execution record|
|» sourceName|string|true|none|The name of execution record source|

#### Enumerated Values

|Property|Value|
|---|---|
|status|OK|
|status|WARNING|
|status|ERROR|

<aside class="success">
This operation does not require authentication
</aside>

## getExecutionRecordsByScope

<a id="opIdgetExecutionRecordsByScope"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/execution-records HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/execution-records`

*Get all execution records for a scope*

Get all the execution records for the given scope UID.

<h3 id="getexecutionrecordsbyscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The scope UID from which to retrieve all execution records.|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "executionConfig": "SIL",
    "name": "SIL_TestCase",
    "status": "OK",
    "folderName": "SIL simulations",
    "length": 2,
    "scopeName": "power_window_controller",
    "sourceName": "TestCase"
  }
]
```

> 404 Response

```
"No Scope found with UID: {VALUE}"
```

<h3 id="getexecutionrecordsbyscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getexecutionrecordsbyscope-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ExecutionRecord](#schemaexecutionrecord)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» executionConfig|string|true|none|The execution config name|
|» name|string|true|none|The execution record name|
|» status|string|false|none|The status of execution record.Possible options: OK, WARNING, or ERROR.|
|» folderName|string|true|none|The folder name on which this execution record can be found.|
|» length|integer(int64)|true|none|The length of execution record source|
|» scopeName|string|true|none|The scope name of execution record|
|» sourceName|string|true|none|The name of execution record source|

#### Enumerated Values

|Property|Value|
|---|---|
|status|OK|
|status|WARNING|
|status|ERROR|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-test-case-stimuli-vector-simulation">Test Case/Stimuli Vector Simulation</h1>

Simulate TestCases.

## simulateOnFolder

<a id="opIdsimulateOnFolder"></a>

> Code samples

```http
POST /ep/folders/{folder__uid}/testcase-simulation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/{folder__uid}/testcase-simulation`

*Simulates all Test Cases/StimuliVectors from a folder*

<b>Long running task </b>Simulates all Test Cases/StimuliVectors from a given folder for the specified execution kinds. Optionally,  simulation can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false
}
```

<h3 id="simulateonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|The Folder UID for which the Test Cases/Stimuli Vectors are simulated.|
|body|body|[TestCaseSimulationParams](#schematestcasesimulationparams)|true|Provide the list of execution kinds  (example: SIL, TL MIL, SL MIL, etc.) on  which to simulate. Optionally, set the simulation to forced, so to not re-use any previous simulation results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="simulateonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## simulateOnFolder

> Code samples

```http
POST /ep/folders/{folder__uid}/testcase-simulation HTTP/1.1

Accept: application/json

```

`POST /ep/folders/{folder__uid}/testcase-simulation`

The long running task status and result will be transmitted.

<h3 id="simulateonfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "..."
}
```

> 404 Response

```
"No folder was found for folder UID {folder__uid}."
```

<h3 id="simulateonfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Simulated. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[TestCaseSimulationResultMap](#schematestcasesimulationresultmap)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## simulateOnFolderList

<a id="opIdsimulateOnFolderList"></a>

> Code samples

```http
POST /ep/folders/testcase-simulation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders/testcase-simulation`

*Simulates all Test Cases/StimuliVectors from a list of folders*

<b>Long running task </b>Simulates all Test Cases/StimuliVectors from a given list of folders for the specified execution kinds. Optionally,  simulation can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false,
  "UIDs": "2UPb"
}
```

<h3 id="simulateonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TestCaseSimulationOnListParams](#schematestcasesimulationonlistparams)|true|Provide the list of folder UIDs and a list of execution kinds (example: SIL, TL MIL, SL MIL, etc.) for which to simulate. Optionally, set the simulation to forced, so to not re-use any previous simulation results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="simulateonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## simulateOnFolderList

> Code samples

```http
POST /ep/folders/testcase-simulation HTTP/1.1

Accept: application/json

```

`POST /ep/folders/testcase-simulation`

The long running task status and result will be transmitted.

<h3 id="simulateonfolderlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "..."
}
```

> 404 Response

```
"Not all folder UIDs are valid."
```

<h3 id="simulateonfolderlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Simulated. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[TestCaseSimulationResultMap](#schematestcasesimulationresultmap)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## simulateOnScope

<a id="opIdsimulateOnScope"></a>

> Code samples

```http
POST /ep/scopes/{scope__uid}/testcase-simulation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/scopes/{scope__uid}/testcase-simulation`

*Simulates all Test Cases/StimuliVectors from a scope*

<b>Long running task </b>Simulates all Test Cases/StimuliVectors from a given scope for the specified execution kinds. Optionally,  simulation can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false
}
```

<h3 id="simulateonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The Scope UID for which the Test Cases/Stimuli Vectors are simulated.|
|body|body|[TestCaseSimulationParams](#schematestcasesimulationparams)|true|Provide the list of execution kinds  (example: SIL, TL MIL, SL MIL, etc.) on  which to simulate. Optionally, set the simulation to forced, so to not re-use any previous simulation results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="simulateonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## simulateOnScope

> Code samples

```http
POST /ep/scopes/{scope__uid}/testcase-simulation HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/{scope__uid}/testcase-simulation`

The long running task status and result will be transmitted.

<h3 id="simulateonscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "..."
}
```

> 404 Response

```
"No scope was found for UID {scope__uid}."
```

<h3 id="simulateonscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Sumilated. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[TestCaseSimulationResultMap](#schematestcasesimulationresultmap)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## simulateOnScopeList

<a id="opIdsimulateOnScopeList"></a>

> Code samples

```http
POST /ep/scopes/testcase-simulation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/scopes/testcase-simulation`

*Simulates all Test Cases/StimuliVectors from a list of scopes*

<b>Long running task </b>Simulates all Test Cases/StimuliVectors from a given list of scopes for the specified execution kinds. Optionally, simulation can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false,
  "UIDs": "2UPb"
}
```

<h3 id="simulateonscopelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TestCaseSimulationOnListParams](#schematestcasesimulationonlistparams)|true|Provide the list of scope UIDs and the list of execution kinds (example: SIL, TL MIL, SL MIL, etc.) on  which to simulate. Optionally, set the simulation to forced, so to not re-use any previous simulation results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="simulateonscopelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## simulateOnScopeList

> Code samples

```http
POST /ep/scopes/testcase-simulation HTTP/1.1

Accept: application/json

```

`POST /ep/scopes/testcase-simulation`

The long running task status and result will be transmitted.

<h3 id="simulateonscopelist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "..."
}
```

> 404 Response

```
"Not all scope UIDs are valid."
```

<h3 id="simulateonscopelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Sumilated. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[TestCaseSimulationResultMap](#schematestcasesimulationresultmap)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## simulateTestCase

<a id="opIdsimulateTestCase"></a>

> Code samples

```http
POST /ep/test-cases/{testcase__uid}/testcase-simulation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/test-cases/{testcase__uid}/testcase-simulation`

*Simulates a Test Case/Stimuli Vector*

<b>Long running task </b>Simulates a Test Case/Stimuli Vector for the specified execution kinds. Optionally, also the test execution can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false
}
```

<h3 id="simulatetestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|testcase-uid|path|string|true|The Test Case/Stimuli VectorUID to simulate.|
|body|body|[TestCaseSimulationParams](#schematestcasesimulationparams)|true|Provide the execution configs (example: SIL, TL MIL, SL MIL, etc.) on which to simulate. Optionally, you can choose to set the test execution to forced, so to not re-use any previous execution results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="simulatetestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## simulateTestCase

> Code samples

```http
POST /ep/test-cases/{testcase__uid}/testcase-simulation HTTP/1.1

Accept: application/json

```

`POST /ep/test-cases/{testcase__uid}/testcase-simulation`

The long running task status and result will be transmitted.

<h3 id="simulatetestcase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "..."
}
```

> 404 Response

```
"Not all RB Test Cases specified have valid UIDs."
```

<h3 id="simulatetestcase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Executed. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[TestCaseSimulationResultMap](#schematestcasesimulationresultmap)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## simulateTestCases

<a id="opIdsimulateTestCases"></a>

> Code samples

```http
POST /ep/test-cases/testcase-simulation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/test-cases/testcase-simulation`

*Simulates all Test Cases/StimuliVectors*

<b>Long running task </b>Simulates all Test Cases/StimuliVectors on the specified execution kinds. Optionally,  simulation can be forced to not re-use any previous results.

> Body parameter

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false,
  "UIDs": "2UPb"
}
```

<h3 id="simulatetestcases-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TestCaseSimulationOnListParams](#schematestcasesimulationonlistparams)|true|Provide the list of Test Case UIDs and a list of execution kinds (example: SIL, TL MIL, SL MIL, etc.) for which to simulate. Optionally, set the simulation to forced, so to not re-use any previous simulation results.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="simulatetestcases-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## simulateTestCases

> Code samples

```http
POST /ep/test-cases/testcase-simulation HTTP/1.1

Accept: application/json

```

`POST /ep/test-cases/testcase-simulation`

The long running task status and result will be transmitted.

<h3 id="simulatetestcases-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "testResults": "..."
}
```

> 404 Response

```
"Not all folder UIDs are valid."
```

<h3 id="simulatetestcases-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Sumilated. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[TestCaseSimulationResultMap](#schematestcasesimulationresultmap)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-domain-checks">Domain Checks</h1>

Handle domain checks.

## createDomainChecksRanges

<a id="opIdcreateDomainChecksRanges"></a>

> Code samples

```http
POST /ep/domain-checks-ranges HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/domain-checks-ranges`

*Create domain checks ranges*

Create the domain checks ranges for a scope and a list of signals. If the list of signals is not given, ranges for all signals of the scope will be created by default. The ranges can be created with some convenience functions applied (partitioned by a percent, with boundaries checks included or with invalid ranges checks included). Please note ALL domain checks ranges created via this service will overwrite any existing ranges for the given list of signals or for all signals (if no signal is specified).

> Body parameter

```json
{
  "scopeUid": "27c",
  "signalUids": [
    "222"
  ],
  "applyBoundaryChecks": false,
  "applyInvalidRangesChecks": false,
  "percentage": 25
}
```

<h3 id="createdomainchecksranges-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DomainChecksRangesInput](#schemadomainchecksrangesinput)|true|The configuration to use for creating the domain checks ranges.|

> Example responses

> 200 Response

```
"Domain checks ranges created successfully."
```

<h3 id="createdomainchecksranges-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## exportDomainChecksGoals

<a id="opIdexportDomainChecksGoals"></a>

> Code samples

```http
POST /ep/domain-checks-export HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/domain-checks-export`

*Export domain check ranges*

Export domain check ranges of the given scopeUid.

> Body parameter

```json
{
  "scopeUid": "26u",
  "filePath": "C:/DomainChecks/goals.xml"
}
```

<h3 id="exportdomainchecksgoals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DomainChecksIOInfo](#schemadomainchecksioinfo)|true|All necessary information for exporting domain check ranges.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exportdomainchecksgoals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

### Callbacks

#### Progress

**/ep/progress**

## exportDomainChecksGoals

> Code samples

```http
POST /ep/domain-checks-export HTTP/1.1

Accept: text/plain

```

`POST /ep/domain-checks-export`

The long running task status and result will be transmitted.

<h3 id="exportdomainchecksgoals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exportdomainchecksgoals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Exported. When the long running task is finished, the operation result will be available.|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getDomainCheckGoalsByScope

<a id="opIdgetDomainCheckGoalsByScope"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/domain-check-details HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/domain-check-details`

*Get domain check details*

Get domain check details for a scope. Some filters can be applied.

<h3 id="getdomaincheckgoalsbyscope-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope, for which to retrieve the domain check details.|
|useCase|query|string|false|The use case for which to retrieve the domain check details. Possible values: B2B, RBT. If not provided, details are shown for B2B.|
|signalNames|query|array[string]|false|The names of the signals for which to retrieve the domain check details. If not provided, the details for all signals are shown.|
|signalKinds|query|array[string]|false|The kinds of the signals for which to retrieve the domain check details. Possible values: INPUT, OUTPUT, LOCAL, PARAMETER. If not provided, the details will be shown for all kinds.|
|goalStates|query|array[string]|false|The status filter for domain check details. Possible values: COVERED, UNKNOWN, UNREACHABLE, ERROR. If not provided, the details will be shown for all status.|
|goalTypes|query|array[string]|false|The goal type filter for domain check details. Possible values: VALID, INVALID. If not provided, the details will be shown for all types.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|useCase|B2B|
|useCase|RBT|
|signalKinds|INPUT|
|signalKinds|OUTPUT|
|signalKinds|LOCAL|
|signalKinds|PARAMETER|
|goalStates|COVERED|
|goalStates|UNREACHABLE|
|goalStates|UNKNOWN|
|goalStates|ERROR|
|goalStates|NOT_DEFINED|
|goalTypes|VALID|
|goalTypes|INVALID|

> Example responses

> 200 Response

```json
{
  "name": "Sa1_driver_down",
  "kind": "INPUT",
  "pll": "IDCG:1:0",
  "range": "[0 42]",
  "goalType": "VALID",
  "goalStatus": "UNREACHABLE",
  "comment": "The goal is unreachable because of... ",
  "coveringVectors": [
    "testCase"
  ]
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getdomaincheckgoalsbyscope-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[DomainCheckGoal](#schemadomaincheckgoal)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## getDomainChecksResults

<a id="opIdgetDomainChecksResults"></a>

> Code samples

```http
GET /ep/scopes/{scope__uid}/domain-checks-results HTTP/1.1

Accept: application/json

```

`GET /ep/scopes/{scope__uid}/domain-checks-results`

*Get domain checks results*

Get the domain checks results for a scope. Using the use case option will display the results for SVs and RBTest Cases if B2B is used or only for RBTest Cases if RBT option is used. Also, the results can be requested either only for the invalid goal types and for the valid ones, or for all goal types.

<h3 id="getdomainchecksresults-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scope-uid|path|string|true|The UID of the scope for which to get the domain checks results.|
|useCase|query|string|false|The use case for which to retrieve the domain check results. Possible values: B2B, RBT.Can be empty, in which case the results are shown for B2B use case.|
|goalTypes|query|array[string]|false|The goal type for which to retrieve the domain check results. Possible values: VALID, INVALID.Can be empty, in which case the results are shown for all goal types.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|useCase|B2B|
|useCase|RBT|
|goalTypes|VALID|
|goalTypes|INVALID|

> Example responses

> 200 Response

```json
{
  "totalCountValid": "100",
  "coveredCountValid": "100",
  "unreachableCountValid": "0",
  "errorCountValid": "0",
  "handledCountValid": "100",
  "unhandledCountValid": "0",
  "coveredPercValid": "100",
  "unreachablePercValid": "0",
  "errorPercValid": "0",
  "handledPercValid": "100",
  "unhandledPercValid": "0",
  "totalCountInvalid": "100",
  "coveredCountInvalid": "0",
  "unreachableCountInvalid": "100",
  "errorCountInvalid": "0",
  "handledCountInvalid": "100",
  "unhandledCountInvalid": "0",
  "coveredPercInvalid": "0",
  "unreachablePercInvalid": "100",
  "errorPercInvalid": "0",
  "handledPercInvalid": "100",
  "unhandledPercInvalid": "0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getdomainchecksresults-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[DomainChecksResults](#schemadomainchecksresults)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## importDomainChecksGoals

<a id="opIdimportDomainChecksGoals"></a>

> Code samples

```http
POST /ep/domain-checks HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/domain-checks`

*Import domain check ranges*

Import domain check ranges on the given scopeUid.

> Body parameter

```json
{
  "scopeUid": "26u",
  "filePath": "C:/DomainChecks/goals.xml"
}
```

<h3 id="importdomainchecksgoals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DomainChecksIOInfo](#schemadomainchecksioinfo)|true|All necessary information for importing domain check ranges. Range definitions which contains invalid identifier are not imported.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importdomainchecksgoals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

### Callbacks

#### Progress

**/ep/progress**

## importDomainChecksGoals

> Code samples

```http
POST /ep/domain-checks HTTP/1.1

Accept: text/plain

```

`POST /ep/domain-checks`

The long running task status and result will be transmitted.

<h3 id="importdomainchecksgoals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progressId|query|string|false|none|

> Example responses

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importdomainchecksgoals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Imported. When the long running task is finished, the operation result will be available.|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## setDomainChecksGoalsComments

<a id="opIdsetDomainChecksGoalsComments"></a>

> Code samples

```http
POST /ep/domain-check-comments HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`POST /ep/domain-check-comments`

*Set domain check comments*

Set the comments for the domain check ranges specified by the PLL of their corresponding domain check goal. To remove a comment for a given domain check goal, provide an empty string as a comment.

> Body parameter

```json
[
  {
    "pll": "VDCG:2:0",
    "comment": "MyComment"
  }
]
```

<h3 id="setdomainchecksgoalscomments-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DomainCheckGoalComment](#schemadomaincheckgoalcomment)|true|none|

> Example responses

> 200 Response

```
"Domain checks comments set successfully."
```

<h3 id="setdomainchecksgoalscomments-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-folders">Folders</h1>

Handle folders.

## getFoldersByQuery

<a id="opIdgetFoldersByQuery"></a>

> Code samples

```http
GET /ep/folders HTTP/1.1

Accept: application/json

```

`GET /ep/folders`

*Get a list of folders*

Get a list of folders by name and/or kind.

<h3 id="getfoldersbyquery-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|query|string|false|Enter the name of the folder you would like to search for. If null, then all folders will be returned.|
|kind|query|string|false|Enter the folder kind. If null, then all folder kinds will be returned.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|kind|RB_TEST_CASE|
|kind|EXECUTION_RECORD|
|kind|STIMULI_VECTOR|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "name": "Test Cases",
    "kind": "RB_TEST_CASE",
    "isDefault": true
  }
]
```

> 400 Response

```
"Illegal argument. {EXCEPTION MESSAGE}"
```

<h3 id="getfoldersbyquery-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<h3 id="getfoldersbyquery-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Folder](#schemafolder)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» name|string|true|none|The name of the folder.|
|» kind|string|true|none|The folder kind.|
|» isDefault|boolean|true|none|Set to 'true' if it is a default folder.|

<aside class="success">
This operation does not require authentication
</aside>

## addFolder

<a id="opIdaddFolder"></a>

> Code samples

```http
POST /ep/folders HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/folders`

*Create a folder*

Add a folder by providing a folder kind and optionally a folder name. Note that a new UID will be assigned.

> Body parameter

```json
{
  "folderKind": "RB_TEST_CASE",
  "folderName": "My folder"
}
```

<h3 id="addfolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[FolderTransmisionObject](#schemafoldertransmisionobject)|true|Provide any folder you would like to add. A new UID will be assigned.|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "name": "Test Cases",
  "kind": "RB_TEST_CASE",
  "isDefault": true
}
```

> 400 Response

```
"Illegal argument. {EXCEPTION MESSAGE}"
```

<h3 id="addfolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Folder](#schemafolder)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## deleteFolder

<a id="opIddeleteFolder"></a>

> Code samples

```http
DELETE /ep/folders/{folder__uid} HTTP/1.1

Accept: text/plain

```

`DELETE /ep/folders/{folder__uid}`

*Delete a folder*

Delete a folder by providing its UID.

<h3 id="deletefolder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder-uid|path|string|true|Enter the UID of the folder you would like to delete.|

> Example responses

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="deletefolder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-back-to-back-test-reports">Back-to-Back Test Reports</h1>

## createBackToBackReport

<a id="opIdcreateBackToBackReport"></a>

> Code samples

```http
POST /ep/b2b/{b2b__test__uid}/b2b-reports HTTP/1.1

Accept: application/json

```

`POST /ep/b2b/{b2b__test__uid}/b2b-reports`

*Create a B2B test report on a B2B test*

Creates a Back-to-Back test report on a Back-to-Back test by providing its UID.

<h3 id="createbacktobackreport-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|b2b-test-uid|path|string|true|The Back-to-Back test UID for which the Back-to-Back test report is created.|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}
```

> 404 Response

```
"No Back-to-Back test was found for the given test UID."
```

<h3 id="createbacktobackreport-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[Report](#schemareport)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## getReports

<a id="opIdgetReports"></a>

> Code samples

```http
GET /ep/b2b-reports HTTP/1.1

Accept: application/json

```

`GET /ep/b2b-reports`

*Get all B2B test reports*

Retrieve all the Back-to-Back test reports from the profile.

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "reportName": "Report 9/27/20 07:43 AM",
    "reportType": "<Report Type>"
  }
]
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getreports-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getreports-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Report](#schemareport)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» reportName|string|false|none|Name of the report.|
|» reportType|string|false|none|Type of the report.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-general">General</h1>

## importCCodeArchitecture

<a id="opIdimportCCodeArchitecture"></a>

> Code samples

```http
POST /ep/architectures/ccode HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/architectures/ccode`

*Import a C-Code architecture*

<b>Long running task</b> Import a C-Code architecture. Settings are provided as an import info object.

> Body parameter

```json
{
  "modelFile": "C:/Models/PowerWindow/CodeModel.xml",
  "mappingFile": "C:/Models/PowerWindow/mappingFile.xml"
}
```

<h3 id="importccodearchitecture-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CCodeImportInfo](#schemaccodeimportinfo)|true|The configuration to use for C-code architecture import.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importccodearchitecture-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## importCCodeArchitecture

> Code samples

```http
POST /ep/architectures/ccode HTTP/1.1

Accept: application/json

```

`POST /ep/architectures/ccode`

The long running task status and result will be transmitted.

<h3 id="importccodearchitecture-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "architectureKind": "C-Code",
  "name": "powerwindow_window_controller [C-Code]",
  "propList": "\"architectureProperties\": {\r\n      \"Test Mode\": \"GREY_BOX\",\r\n      \"Import Date\": \"Sep 18, 2020 1:19:43 PM\",\r\n       ....}"
}
```

> 400 Response

```
"The C-Code architecture import failed because no compiler is set. Please set the compiler and try again."
```

<h3 id="importccodearchitecture-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[Architecture](#schemaarchitecture)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## createEmbeddedCoderCWrapperModel

<a id="opIdcreateEmbeddedCoderCWrapperModel"></a>

> Code samples

```http
POST /ep/architectures/embedded-coder-wrapper-creation HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/architectures/embedded-coder-wrapper-creation`

*Create an EmbeddedCoder™ wrapper model*

<b>Long running task</b> Creating an EmbeddedCoder™ wrapper model. Settings are provided as an import wrapper info object.

> Body parameter

```json
{
  "ecModelFile": "C:/Model/powerwindow_ec.mdl",
  "ecInitScript": "C:/Model/start.m"
}
```

<h3 id="createembeddedcodercwrappermodel-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ECWrapperImportInfo](#schemaecwrapperimportinfo)|true|The EmbeddedCoder™ wrapper info containing the model file and the optional init script.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="createembeddedcodercwrappermodel-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## createEmbeddedCoderCWrapperModel

> Code samples

```http
POST /ep/architectures/embedded-coder-wrapper-creation HTTP/1.1

Accept: application/json

```

`POST /ep/architectures/embedded-coder-wrapper-creation`

The long running task status and result will be transmitted.

<h3 id="createembeddedcodercwrappermodel-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "ecModelFile": "C:/Model/powerwindow_ec.mdl",
  "ecInitScript": "C:/Model/start.m"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="createembeddedcodercwrappermodel-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[ECWrapperResultInfo](#schemaecwrapperresultinfo)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|406|[Not Acceptable](https://tools.ietf.org/html/rfc7231#section-6.5.6)|Not acceptable|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## importEmbeddedCoderArchitecture

<a id="opIdimportEmbeddedCoderArchitecture"></a>

> Code samples

```http
POST /ep/architectures/embedded-coder HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/architectures/embedded-coder`

*Import an EmbeddedCoder™ architecture*

<b>Long running task</b> Import an EmbeddedCoder™ architecture. Settings are provided as an import info object.

> Body parameter

```json
{
  "ecModelFile": "C:/Model/powerwindow_ec.mdl",
  "ecInitScript": "C:/Model/start.m",
  "parameterHandling": "OFF",
  "testMode": "BLACK_BOX",
  "fixedStepSolver": false,
  "inDepthCcodeAnalysis": false,
  "subsystemMatcher": "Model/SubsystemA.*|Model/SubsystemB",
  "parameterMatcher": "ParameterA|ParameterB|ParameterC"
}
```

<h3 id="importembeddedcoderarchitecture-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ECImportInfo](#schemaecimportinfo)|true|The EmbeddedCoder™ Import Info containing the model file and import parameters.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="importembeddedcoderarchitecture-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## importEmbeddedCoderArchitecture

> Code samples

```http
POST /ep/architectures/embedded-coder HTTP/1.1

Accept: application/json

```

`POST /ep/architectures/embedded-coder`

The long running task status and result will be transmitted.

<h3 id="importembeddedcoderarchitecture-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "architectureKind": "C-Code",
  "name": "powerwindow_window_controller [C-Code]",
  "propList": "\"architectureProperties\": {\r\n      \"Test Mode\": \"GREY_BOX\",\r\n      \"Import Date\": \"Sep 18, 2020 1:19:43 PM\",\r\n       ....}"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importembeddedcoderarchitecture-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[Architecture](#schemaarchitecture)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## getArchitecture

<a id="opIdgetArchitecture"></a>

> Code samples

```http
GET /ep/architectures/{architecture__uid} HTTP/1.1

Accept: application/json

```

`GET /ep/architectures/{architecture__uid}`

*Get a specific architecture*

Get an existing architecture by UID.

<h3 id="getarchitecture-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|architecture-uid|path|string|true|The UID of the architecture to be returned.|

> Example responses

> 200 Response

```json
{
  "uid": "yak7s7",
  "architectureKind": "C-Code",
  "name": "powerwindow_window_controller [C-Code]",
  "propList": "\"architectureProperties\": {\r\n      \"Test Mode\": \"GREY_BOX\",\r\n      \"Import Date\": \"Sep 18, 2020 1:19:43 PM\",\r\n       ....}"
}
```

> 404 Response

```
"No Architecture was found."
```

<h3 id="getarchitecture-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[Architecture](#schemaarchitecture)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

## getArchitectures

<a id="opIdgetArchitectures"></a>

> Code samples

```http
GET /ep/architectures HTTP/1.1

Accept: application/json

```

`GET /ep/architectures`

*Get all architectures*

Search for all open architectures.

<h3 id="getarchitectures-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|architecture-kind|query|string|false|Specifies the specific architecture kind to be queried. (e.g. 'Simulink', 'C-Code', 'TargetLink')|

> Example responses

> 200 Response

```json
[
  {
    "uid": "yak7s7",
    "architectureKind": "C-Code",
    "name": "powerwindow_window_controller [C-Code]",
    "propList": "\"architectureProperties\": {\r\n      \"Test Mode\": \"GREY_BOX\",\r\n      \"Import Date\": \"Sep 18, 2020 1:19:43 PM\",\r\n       ....}"
  }
]
```

> 404 Response

```
"No Architecture was found."
```

<h3 id="getarchitectures-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<h3 id="getarchitectures-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Architecture](#schemaarchitecture)]|false|none|none|
|» uid|string|false|read-only|The unique identifier (UID) of this object.|
|» architectureKind|string|false|read-only|The string representation of the concrete architecture<br>, e.g. 'Simulink', 'C-Code', 'TargetLink'.|
|» name|string|false|read-only|The architecture name as specified by the model.|
|» propList|object|false|read-only|The Architecture property List|
|»» **additionalProperties**|string|false|read-only|The Architecture property List|

<aside class="success">
This operation does not require authentication
</aside>

## architectureUpdate

<a id="opIdarchitectureUpdate"></a>

> Code samples

```http
PUT /ep/architectures HTTP/1.1

Accept: application/json

```

`PUT /ep/architectures`

*Update architectures*

<b>Long running task</b> Perform an architecture update.

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="architectureupdate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## architectureUpdate

> Code samples

```http
PUT /ep/architectures HTTP/1.1

Accept: application/json

```

`PUT /ep/architectures`

The long running task status and result will be transmitted.

<h3 id="architectureupdate-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "architectureKind": "C-Code",
  "name": "powerwindow_window_controller [C-Code]",
  "propList": "\"architectureProperties\": {\r\n      \"Test Mode\": \"GREY_BOX\",\r\n      \"Import Date\": \"Sep 18, 2020 1:19:43 PM\",\r\n       ....}"
}
```

> 400 Response

```
"parameters are not acceptable!"
```

<h3 id="architectureupdate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[Architecture](#schemaarchitecture)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## updateModelPaths

<a id="opIdupdateModelPaths"></a>

> Code samples

```http
PUT /ep/architectures/model-paths HTTP/1.1

Content-Type: application/json
Accept: text/plain

```

`PUT /ep/architectures/model-paths`

*Update model paths for architectures*

Update the paths for imported architectures. If the architecture-uid is not specified, the model paths will be updated for the master architecture.

> Body parameter

```json
{
  "slModelFile": "C:/Models/PowerWindow/ml2017b_tl50/powerwindow_sl_v01.mdl",
  "slInitScript": "C:/Models/PowerWindow/ml2017b_tl50/start.m",
  "addModelInfo": "C:/Models/PowerWindow/ml2017b_tl50/ModelInfoSl.xml",
  "tlModelFile": "C:/Models/PowerWindow/ml2017b_tl50/powerwindow_tl_v01.mdl",
  "tlInitScript": "C:/Models/PowerWindow/ml2017b_tl50/start.m",
  "environment": "C:/Models/PowerWindow/ml2017b_tl50/env.xml"
}
```

<h3 id="updatemodelpaths-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|architecture-uid|query|string|false|The UID of the architecture to be updated. If empty, the path will be updated for the master architecture.|
|body|body|[UpdateModelPath](#schemaupdatemodelpath)|false|The configuration to use for updating the model path.|

> Example responses

> 200 Response

```
"model paths updated."
```

<h3 id="updatemodelpaths-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

## importSimulinkArchitecture

<a id="opIdimportSimulinkArchitecture"></a>

> Code samples

```http
POST /ep/architectures/simulink HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/architectures/simulink`

*Import a Simulink™ architecture*

<b>Long running task</b> Import a Simulink™ architecture. Settings are provided as an import info object.

> Body parameter

```json
{
  "slModelFile": "C:/Models/PowerWindow/PowerWindow_SL.mdl",
  "slInitScriptFile": "C:/Models/PowerWindow/start.m",
  "parameterHandling": "EXPLICIT_PARAMETER",
  "testMode": "BLACK_BOX",
  "fixedStepSolver": true,
  "mappingFile": "C:/Models/PowerWindow/Mapping.xml",
  "subsystemMatcher": "Model|Model/SubsystemA.*|Model/SubsystemB/SubsystemBA",
  "parameterMatcher": "ParameterA|ParameterB|ParameterC"
}
```

<h3 id="importsimulinkarchitecture-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SLImportInfo](#schemaslimportinfo)|true|The Simulink™ Import Info containing the model file and import parameters.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importsimulinkarchitecture-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

### Callbacks

#### Progress

**/ep/progress**

## importSimulinkArchitecture

> Code samples

```http
POST /ep/architectures/simulink HTTP/1.1

Accept: application/json

```

`POST /ep/architectures/simulink`

The long running task status and result will be transmitted.

<h3 id="importsimulinkarchitecture-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "architectureKind": "C-Code",
  "name": "powerwindow_window_controller [C-Code]",
  "propList": "\"architectureProperties\": {\r\n      \"Test Mode\": \"GREY_BOX\",\r\n      \"Import Date\": \"Sep 18, 2020 1:19:43 PM\",\r\n       ....}"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importsimulinkarchitecture-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[Architecture](#schemaarchitecture)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## importTargetLinkArchitecture

<a id="opIdimportTargetLinkArchitecture"></a>

> Code samples

```http
POST /ep/architectures/targetlink HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/architectures/targetlink`

*Import a TargetLink™ architecture*

<b>Long running task</b> Import a TargetLink™ architecture. Settings are provided as an import info object.

> Body parameter

```json
{
  "tlModelFile": "C:/Model/PowerWindow_TL.mdl",
  "tlInitScript": "C:/Model/start.m",
  "slModelFile": "C:/Model/PowerWindow_SL.mdl",
  "slInitScript": "C:/Model/start.m",
  "environment": "C:/Model/environment.xml",
  "useExistingCode": true,
  "activateModelLinking": false,
  "closedLoopModel": false,
  "fixedStepSolver": false,
  "tlSubsystem": "PowerWindow",
  "calibrationHandling": "LIMITED_BLOCKSET",
  "testMode": "BLACK_BOX",
  "mappingFileForTLArch": "C:/Model/tlmapping.xml",
  "mappingFileForCCodeArch": "C:/Model/ccodemapping.xml",
  "mappingFileForSLArch": "C:/Model/slmapping.xml",
  "subsystemMatcher": "Model/RootSubsystem/Subsystem/RootSubsystem/SubsystemA.*|Model/RootSubsystem/Subsystem/RootSubsystem/SubsystemB",
  "calibrationMatcher": "CalibrationA|CalibrationB|CalibrationC",
  "cfileMatcher": "FilenameA\\.c|FilenameB\\.c"
}
```

<h3 id="importtargetlinkarchitecture-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TLImportInfo](#schematlimportinfo)|true|The TargetLink™ Import Info containing the model file and import parameters.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importtargetlinkarchitecture-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## importTargetLinkArchitecture

> Code samples

```http
POST /ep/architectures/targetlink HTTP/1.1

Accept: application/json

```

`POST /ep/architectures/targetlink`

The long running task status and result will be transmitted.

<h3 id="importtargetlinkarchitecture-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```json
{
  "uid": "yak7s7",
  "architectureKind": "C-Code",
  "name": "powerwindow_window_controller [C-Code]",
  "propList": "\"architectureProperties\": {\r\n      \"Test Mode\": \"GREY_BOX\",\r\n      \"Import Date\": \"Sep 18, 2020 1:19:43 PM\",\r\n       ....}"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importtargetlinkarchitecture-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|[Architecture](#schemaarchitecture)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## exitApplication

<a id="opIdexitApplication"></a>

> Code samples

```http
DELETE /ep/application HTTP/1.1

Accept: text/plain

```

`DELETE /ep/application`

*Exit EP and save the active profile*

After calling the exit method, the current active profile will be saved, if there is one. If the profile has no save path, one is created at a temporary directory and a response containing the path is returned.

<h3 id="exitapplication-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|force-quit|query|boolean|false|If set to 'true', the application will force quit without saving the active profile. <br>If set to 'false', the profile is saved at the given location, or at a temporary location if provided none. <br>Default is 'false'|

> Example responses

> 200 Response

```
"EmbeddedPlatform closed without saving active profile."
```

<h3 id="exitapplication-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|string|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-test">Test</h1>

## test

<a id="opIdtest"></a>

> Code samples

```http
GET /ep/test HTTP/1.1

Accept: text/plain

```

`GET /ep/test`

*Test the connection to the REST server*

> Example responses

> 200 Response

```
"Success message"
```

<h3 id="test-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Request successfully sent.|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

### Response Headers

|Status|Header|Type|Format|Description|
|---|---|---|---|---|
|200|X-Server-OS|undefined||The OS the REST API server is running on|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-input-restrictions">Input Restrictions</h1>

## exportToFile

<a id="opIdexportToFile"></a>

> Code samples

```http
POST /ep/input-restrictions-export HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/input-restrictions-export`

*Export input restrictions*

Export input restrictions to a file

> Body parameter

```json
{
  "filePath": "C:/path/to/file.xml"
}
```

<h3 id="exporttofile-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[InputRestrictionsFolderObject](#schemainputrestrictionsfolderobject)|true|The file into which to write the input restrictions.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="exporttofile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## exportToFile

> Code samples

```http
POST /ep/input-restrictions-export HTTP/1.1

Accept: text/plain

```

`POST /ep/input-restrictions-export`

The long running task status and result will be transmitted.

<h3 id="exporttofile-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 201 Response

```
"{Input restrictions exported.}"
```

<h3 id="exporttofile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created. When the long running task is finished, the following object is availabe in the 'result' field of the response object.|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

## importFromFile

<a id="opIdimportFromFile"></a>

> Code samples

```http
POST /ep/input-restrictions-import HTTP/1.1

Content-Type: application/json
Accept: application/json

```

`POST /ep/input-restrictions-import`

*Import input restrictions*

Import input restrictions from a file

> Body parameter

```json
{
  "filePath": "C:/path/to/file.xml"
}
```

<h3 id="importfromfile-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[InputRestrictionsFolderObject](#schemainputrestrictionsfolderobject)|true|The file that contains the input restrictions.|

> Example responses

> 202 Response

```json
{
  "jobID": "restJob_0"
}
```

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importfromfile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Long running operation started. The status of the operation can be reviewed by using the <a href='#get-/ep/progress'>Progress</a> i.e. GET '/ep/progress?progress-id={progress-id}' using the id received by this command.|[Job](#schemajob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

### Callbacks

#### Progress

**/ep/progress**

## importFromFile

> Code samples

```http
POST /ep/input-restrictions-import HTTP/1.1

Accept: text/plain

```

`POST /ep/input-restrictions-import`

The long running task status and result will be transmitted.

<h3 id="importfromfile-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|progress-id|query|string|false|none|

> Example responses

> 400 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="importfromfile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Imported. When the long running task is finished, the operation result will be available.|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|string|

<aside class="success">
This operation does not require authentication
</aside>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="btc-embedded-platform-restful-api-documentation-execution-configs">Execution configs</h1>

## getExecutionConfigs

<a id="opIdgetExecutionConfigs"></a>

> Code samples

```http
GET /ep/execution-configs HTTP/1.1

Accept: application/json

```

`GET /ep/execution-configs`

*Get all execution configs*

Get all execution configs available in the profile.

> Example responses

> 200 Response

```json
{
  "execConfigNames": "SIL"
}
```

> 500 Response

```
"{EXCEPTION MESSAGE}"
```

<h3 id="getexecutionconfigs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ExecutionConfigs](#schemaexecutionconfigs)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error.|string|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Report">Report</h2>
<!-- backwards compatibility -->
<a id="schemareport"></a>
<a id="schema_Report"></a>
<a id="tocSreport"></a>
<a id="tocsreport"></a>

```json
{
  "uid": "yak7s7",
  "reportName": "Report 9/27/20 07:43 AM",
  "reportType": "<Report Type>"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|reportName|string|false|none|Name of the report.|
|reportType|string|false|none|Type of the report.|

<h2 id="tocS_ComparisonAcceptanceData">ComparisonAcceptanceData</h2>
<!-- backwards compatibility -->
<a id="schemacomparisonacceptancedata"></a>
<a id="schema_ComparisonAcceptanceData"></a>
<a id="tocScomparisonacceptancedata"></a>
<a id="tocscomparisonacceptancedata"></a>

```json
{
  "comparisonUID": "a3v",
  "accept": false
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comparisonUID|string|true|none|UID of the Comparison|
|accept|boolean|true|none|If accept is true, the comparison verdict status is changed from 'failed' to 'failed (accepted)'. If accept is false, the comparison verdict status is changed from 'failed (accepted)'to 'failed'|

<h2 id="tocS_RestBackToBackTest">RestBackToBackTest</h2>
<!-- backwards compatibility -->
<a id="schemarestbacktobacktest"></a>
<a id="schema_RestBackToBackTest"></a>
<a id="tocSrestbacktobacktest"></a>
<a id="tocsrestbacktobacktest"></a>

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL",
  "stimuliFolderUIDs": 231,
  "stimuliScopeUIDs": 231
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|referenceMode|string|false|none|The reference execution config type.|
|comparisonMode|string|false|none|The comparison execution config type.|
|referenceFolderUIDs|[string]|false|none|Reference folder UIDs|
|comparisonFolderUID|string|false|none|Comparison folder UID|
|executionDate|string|false|none|Execution Date|
|verdictStatus|string|false|none|The verdict status|
|verdictState|string|false|none|Verdict State|
|failed|integer(int32)|false|none|Number of failed comparisons.|
|failedAccepted|integer(int32)|false|none|Number of failed accepted comparisons.|
|passed|integer(int32)|false|none|Number of passed comparisons.|
|error|integer(int32)|false|none|Number of comparisons with error.|
|total|integer(int32)|false|none|Total number of comparisons.|
|comparisons|[[RestComparison](#schemarestcomparison)]|false|none|[All comparisons.]|
|name|string|false|none|The name of the Back-To-Back Test.|
|stimuliFolderUIDs|[string]|false|none|Folder UIDs for which Back-To-Back Test was generated.|
|stimuliScopeUIDs|[string]|false|none|Scope UIDs for which Back-To-Back Test was generated.|

#### Enumerated Values

|Property|Value|
|---|---|
|verdictStatus|PASSED|
|verdictStatus|FAILED|
|verdictStatus|ERROR|
|verdictStatus|FAILED_ACCEPTED|
|verdictState|VALID|
|verdictState|OUTDATED_TOLERANCE_UPDATE|
|verdictState|OUTDATED_MISSING_EXECUTIONS|

<h2 id="tocS_RestComparison">RestComparison</h2>
<!-- backwards compatibility -->
<a id="schemarestcomparison"></a>
<a id="schema_RestComparison"></a>
<a id="tocSrestcomparison"></a>
<a id="tocsrestcomparison"></a>

```json
{
  "uid": "yak7s7",
  "name": "SV_ATG_26",
  "verdictStatus": "PASSED",
  "referenceExecutionRecordUID": "abs3",
  "comparisonExecutionRecordUID": "zz61",
  "comment": "<Comment text>"
}

```

All comparisons.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|name|string|false|none|The name of Test Case / Stimuli Vector used in Comparison.|
|verdictStatus|string|false|none|The verdict status|
|referenceExecutionRecordUID|string|false|none|UID of reference execution record.|
|comparisonExecutionRecordUID|string|false|none|UID of compared to execution record.|
|comment|string|false|none|Added comment for Comparison.|

#### Enumerated Values

|Property|Value|
|---|---|
|verdictStatus|PASSED|
|verdictStatus|FAILED|
|verdictStatus|ERROR|
|verdictStatus|FAILED_ACCEPTED|

<h2 id="tocS_Job">Job</h2>
<!-- backwards compatibility -->
<a id="schemajob"></a>
<a id="schema_Job"></a>
<a id="tocSjob"></a>
<a id="tocsjob"></a>

```json
{
  "jobID": "restJob_0"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|jobID|string|false|read-only|The ID of a job.|

<h2 id="tocS_BackToBackTestExecutionData">BackToBackTestExecutionData</h2>
<!-- backwards compatibility -->
<a id="schemabacktobacktestexecutiondata"></a>
<a id="schema_BackToBackTestExecutionData"></a>
<a id="tocSbacktobacktestexecutiondata"></a>
<a id="tocsbacktobacktestexecutiondata"></a>

```json
{
  "refMode": "TL MIL",
  "compMode": "SIL",
  "forceExecute": false,
  "simulateStimuliVectorsOnly": false
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|refMode|string|true|none|Reference execution mode (e.g. 'SL MIL', 'TL MIL', 'TL MIL (EV)', 'SIL', 'PIL', 'SL SIL'). Not case-sensitive.|
|compMode|string|true|none|Comparison execution mode (e.g. 'SL MIL', 'TL MIL', 'TL MIL (EV)', 'SIL', 'PIL', 'SL SIL'). Not case-sensitive.|
|forceExecute|boolean|false|none|(Optional) If true, simulates all contained test cases/stimuli-vectors, replacing existing execution records. Default is false.|
|simulateStimuliVectorsOnly|boolean|false|none|(Optional) This option can be used only when forceExecution is set to true. If true, simulates only stimuli-vectors. If false, and there are Requirements-based Test Cases with comparison verdicts, the verdicts will be deleted in order to run the Back-To-Back Test. Default value is false.|

<h2 id="tocS_BackToBackTestExecutionSourceData">BackToBackTestExecutionSourceData</h2>
<!-- backwards compatibility -->
<a id="schemabacktobacktestexecutionsourcedata"></a>
<a id="schema_BackToBackTestExecutionSourceData"></a>
<a id="tocSbacktobacktestexecutionsourcedata"></a>
<a id="tocsbacktobacktestexecutionsourcedata"></a>

```json
{
  "refMode": "TL MIL",
  "compMode": "SIL",
  "forceExecute": false,
  "simulateStimuliVectorsOnly": false,
  "UIDs": "2UPb"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|refMode|string|true|none|Reference execution mode (e.g. 'SL MIL', 'TL MIL', 'TL MIL (EV)', 'SIL', 'PIL', 'SL SIL'). Not case-sensitive.|
|compMode|string|true|none|Comparison execution mode (e.g. 'SL MIL', 'TL MIL', 'TL MIL (EV)', 'SIL', 'PIL', 'SL SIL'). Not case-sensitive.|
|forceExecute|boolean|false|none|(Optional) If true, simulates all contained test cases/stimuli-vectors, replacing existing execution records. Default is false.|
|simulateStimuliVectorsOnly|boolean|false|none|(Optional) This option can be used only when forceExecution is set to true. If true, simulates only stimuli-vectors. If false, and there are Requirements-based Test Cases with comparison verdicts, the verdicts will be deleted in order to run the Back-To-Back Test. Default value is false.|
|UIDs|[string]|true|none|UIDs list (e.g. scopes, folders)|

<h2 id="tocS_RegressionTest">RegressionTest</h2>
<!-- backwards compatibility -->
<a id="schemaregressiontest"></a>
<a id="schema_RegressionTest"></a>
<a id="tocSregressiontest"></a>
<a id="tocsregressiontest"></a>

```json
{
  "uid": "yak7s7",
  "referenceMode": "TL MIL",
  "comparisonMode": "SIL",
  "referenceFolderUIDs": 231,
  "comparisonFolderUID": "231",
  "executionDate": "10/15/20, 8:34 AM",
  "verdictStatus": "PASSED",
  "verdictState": "VALID",
  "failed": 4,
  "failedAccepted": 0,
  "passed": 21,
  "error": 0,
  "total": 25,
  "comparisons": [
    {
      "uid": "yak7s7",
      "name": "SV_ATG_26",
      "verdictStatus": "PASSED",
      "referenceExecutionRecordUID": "abs3",
      "comparisonExecutionRecordUID": "zz61",
      "comment": "<Comment text>"
    }
  ],
  "name": "TL MIL vs SIL"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|referenceMode|string|false|none|The reference execution config type.|
|comparisonMode|string|false|none|The comparison execution config type.|
|referenceFolderUIDs|[string]|false|none|Reference folder UIDs|
|comparisonFolderUID|string|false|none|Comparison folder UID|
|executionDate|string|false|none|Execution Date|
|verdictStatus|string|false|none|The verdict status|
|verdictState|string|false|none|Verdict State|
|failed|integer(int32)|false|none|Number of failed comparisons.|
|failedAccepted|integer(int32)|false|none|Number of failed accepted comparisons.|
|passed|integer(int32)|false|none|Number of passed comparisons.|
|error|integer(int32)|false|none|Number of comparisons with error.|
|total|integer(int32)|false|none|Total number of comparisons.|
|comparisons|[[RestComparison](#schemarestcomparison)]|false|none|[All comparisons.]|
|name|string|false|none|The name of the RegresionTest Test.|

#### Enumerated Values

|Property|Value|
|---|---|
|verdictStatus|PASSED|
|verdictStatus|FAILED|
|verdictStatus|ERROR|
|verdictStatus|FAILED_ACCEPTED|
|verdictState|VALID|
|verdictState|OUTDATED_TOLERANCE_UPDATE|
|verdictState|OUTDATED_MISSING_EXECUTIONS|

<h2 id="tocS_RegressionTestExecutionData">RegressionTestExecutionData</h2>
<!-- backwards compatibility -->
<a id="schemaregressiontestexecutiondata"></a>
<a id="schema_RegressionTestExecutionData"></a>
<a id="tocSregressiontestexecutiondata"></a>
<a id="tocsregressiontestexecutiondata"></a>

```json
{
  "compMode": "SIL",
  "compFolderUID": "asV1"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|compMode|string|true|none|Comparison execution mode (e.g. 'SL MIL', 'TL MIL', 'TL MIL (EV)', 'SIL', 'PIL', 'SL SIL')|
|compFolderUID|string|false|none|(Optional) The folder where to save the simulated ExecutionRecords. If this property is not provided, the ExecutionRecords are not saved.|

<h2 id="tocS_RegressionTestExecutionSourceData">RegressionTestExecutionSourceData</h2>
<!-- backwards compatibility -->
<a id="schemaregressiontestexecutionsourcedata"></a>
<a id="schema_RegressionTestExecutionSourceData"></a>
<a id="tocSregressiontestexecutionsourcedata"></a>
<a id="tocsregressiontestexecutionsourcedata"></a>

```json
{
  "compMode": "SIL",
  "compFolderUID": "asV1",
  "UIDs": "2UPb"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|compMode|string|true|none|Comparison execution mode (e.g. 'SL MIL', 'TL MIL', 'TL MIL (EV)', 'SIL', 'PIL', 'SL SIL')|
|compFolderUID|string|false|none|(Optional) The folder where to save the simulated ExecutionRecords. If this property is not provided, the ExecutionRecords are not saved.|
|UIDs|[string]|true|none|Folder UID list|

<h2 id="tocS_ExportResult">ExportResult</h2>
<!-- backwards compatibility -->
<a id="schemaexportresult"></a>
<a id="schema_ExportResult"></a>
<a id="tocSexportresult"></a>
<a id="tocsexportresult"></a>

```json
{
  "exportStatus": [
    {
      "name": "Artifact_1_2",
      "uid": "2my",
      "warnings": "{Cause}",
      "errors": "Export failed for file {file location}. {Cause}."
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|exportStatus|[[ExportStatus](#schemaexportstatus)]|false|none|[List of export status for each file.]|

<h2 id="tocS_ExportStatus">ExportStatus</h2>
<!-- backwards compatibility -->
<a id="schemaexportstatus"></a>
<a id="schema_ExportStatus"></a>
<a id="tocSexportstatus"></a>
<a id="tocsexportstatus"></a>

```json
{
  "name": "Artifact_1_2",
  "uid": "2my",
  "warnings": "{Cause}",
  "errors": "Export failed for file {file location}. {Cause}."
}

```

List of export status for each file.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|Exported element name.|
|uid|string|false|none|Exported elements uid.|
|warnings|[string]|false|none|List of warnings resulted during export of file.|
|errors|[string]|false|none|List of errors resulted during export of file.|

<h2 id="tocS_RestStimuliVectorExportInfo">RestStimuliVectorExportInfo</h2>
<!-- backwards compatibility -->
<a id="schemareststimulivectorexportinfo"></a>
<a id="schema_RestStimuliVectorExportInfo"></a>
<a id="tocSreststimulivectorexportinfo"></a>
<a id="tocsreststimulivectorexportinfo"></a>

```json
{
  "UIDs": "2UPb",
  "exportDirectory": "C:/RestProfiles/VectorExport",
  "exportFormat": "EXCEL",
  "additionalOptions": {
    "csvDelimiter": "SEMICOLON",
    "singleFile": true,
    "architectureUid": "2Ai7"
  },
  "overwritePolicy": "OVERWRITE"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UIDs|[string]|true|none|List with the UIDs of the elements which will be exported|
|exportDirectory|string|true|none|Directory where to export the elements|
|exportFormat|string|false|none|The format of the exported stimuli vectors. It can be: "EXCEL" or "CSV". Default value is EXCEL.|
|additionalOptions|[RestVectorExportDetails](#schemarestvectorexportdetails)|false|none|none|
|overwritePolicy|string|false|none|Overwrite policy: allowed values (not case-sensitive) are: EXTEND_NAME, in which case if the exported file exists on disk, its name will be extended and the original file on disk will be kept, OVERWRITE, in which case the original file on disk is overwritten, if it exists. Default value is EXTEND_NAME|

#### Enumerated Values

|Property|Value|
|---|---|
|exportFormat|EXCEL|
|exportFormat|CSV|
|overwritePolicy|EXTEND_NAME|
|overwritePolicy|OVERWRITE|
|overwritePolicy|SKIP|

<h2 id="tocS_RestVectorExportDetails">RestVectorExportDetails</h2>
<!-- backwards compatibility -->
<a id="schemarestvectorexportdetails"></a>
<a id="schema_RestVectorExportDetails"></a>
<a id="tocSrestvectorexportdetails"></a>
<a id="tocsrestvectorexportdetails"></a>

```json
{
  "csvDelimiter": "SEMICOLON",
  "singleFile": true,
  "architectureUid": "2Ai7"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|csvDelimiter|string|false|none|Relevant only for CSV export format. It can have one of the following values: "SEMICOLON", "COMMA", "COLON", "PIPE". Default value is "SEMICOLON".|
|singleFile|boolean|false|none|Relevant only for CSV export format: false  - each vector will be exported in it's own file; true - all vectors will be exported in same file. Default is 'false'|
|architectureUid|string|false|none|Relevant only for Excel export format. It specifies the UID of the architecture on which the interfaces of the vectors will be exported. Default is the master architecture|

#### Enumerated Values

|Property|Value|
|---|---|
|csvDelimiter|SEMICOLON|
|csvDelimiter|COMMA|
|csvDelimiter|COLON|
|csvDelimiter|PIPE|

<h2 id="tocS_B2BStimuliVector">B2BStimuliVector</h2>
<!-- backwards compatibility -->
<a id="schemab2bstimulivector"></a>
<a id="schema_B2BStimuliVector"></a>
<a id="tocSb2bstimulivector"></a>
<a id="tocsb2bstimulivector"></a>

```json
{
  "uid": "yak7s7",
  "name": "ExampleName",
  "length": 42,
  "folderUID": "12",
  "scopeUID": "24a"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|name|string|false|none|The name of the StimuliVector.|
|length|integer(int64)|false|none|The length of the vector.|
|folderUID|string|false|none|The unique identifier of the folder the StimuliVector belongs to.|
|scopeUID|string|false|none|The unique identifier of the scope the StimuliVector belongs to.|

<h2 id="tocS_ImportResult">ImportResult</h2>
<!-- backwards compatibility -->
<a id="schemaimportresult"></a>
<a id="schema_ImportResult"></a>
<a id="tocSimportresult"></a>
<a id="tocsimportresult"></a>

```json
{
  "importStatus": [
    {
      "UIDs": "15Lx",
      "warnings": "Undefined value detected for signal {signal name}. A default value will be set.",
      "errors": "Invalid format in file {file location}. {Cause}."
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|importStatus|[[ImportStatus](#schemaimportstatus)]|false|none|[List of import status for each file.]|

<h2 id="tocS_ImportStatus">ImportStatus</h2>
<!-- backwards compatibility -->
<a id="schemaimportstatus"></a>
<a id="schema_ImportStatus"></a>
<a id="tocSimportstatus"></a>
<a id="tocsimportstatus"></a>

```json
{
  "UIDs": "15Lx",
  "warnings": "Undefined value detected for signal {signal name}. A default value will be set.",
  "errors": "Invalid format in file {file location}. {Cause}."
}

```

List of import status for each file.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UIDs|[string]|false|none|List of UIDs for imported execution records.|
|warnings|[string]|false|none|List of warnings resulted during import of file.|
|errors|[string]|false|none|List of errors resulted during import of file.|

<h2 id="tocS_RestStimuliVectorImportInfo">RestStimuliVectorImportInfo</h2>
<!-- backwards compatibility -->
<a id="schemareststimulivectorimportinfo"></a>
<a id="schema_RestStimuliVectorImportInfo"></a>
<a id="tocSreststimulivectorimportinfo"></a>
<a id="tocsreststimulivectorimportinfo"></a>

```json
{
  "paths": [
    "C:/RestProfiles/VectorExport/stimVetor.csv"
  ],
  "vectorKind": "TC",
  "folderUID": "13",
  "delimiter": "SEMICOLON",
  "overwritePolicy": "SKIP"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|paths|[string]|true|none|none|
|vectorKind|string|false|none|The stimuli vector type. Default value is "TC"|
|folderUID|string|false|none|The UID of the folder you want to import into.|
|delimiter|string|false|none|The CSV file delimiter, can be: "SEMICOLON", "COMMA", "COLON", "PIPE". Default value is "SEMICOLON"|
|overwritePolicy|string|false|none|Decides what happens in case of duplicate names. Can be "EXTEND_NAME", "OVERWRITE" or "SKIP". Default is "SKIP".|

#### Enumerated Values

|Property|Value|
|---|---|
|vectorKind|TC|
|vectorKind|EXCEL|
|delimiter|SEMICOLON|
|delimiter|COMMA|
|delimiter|COLON|
|delimiter|PIPE|
|overwritePolicy|EXTEND_NAME|
|overwritePolicy|OVERWRITE|
|overwritePolicy|SKIP|

<h2 id="tocS_TolerancesIOConfig">TolerancesIOConfig</h2>
<!-- backwards compatibility -->
<a id="schematolerancesioconfig"></a>
<a id="schema_TolerancesIOConfig"></a>
<a id="tocStolerancesioconfig"></a>
<a id="tocstolerancesioconfig"></a>

```json
{
  "path": "C:/Rest/tolerances.xml",
  "toleranceUseCase": "RBT"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|path|string|true|none|The path to the xml file to use for import or export of tolerances.|
|toleranceUseCase|string|true|none|The use case of the tolerances for which tolerances should be applied. Allowed values are RBT and B2B.|

#### Enumerated Values

|Property|Value|
|---|---|
|toleranceUseCase|B2B|
|toleranceUseCase|RBT|

<h2 id="tocS_ToleranceDefinition">ToleranceDefinition</h2>
<!-- backwards compatibility -->
<a id="schematolerancedefinition"></a>
<a id="schema_ToleranceDefinition"></a>
<a id="tocStolerancedefinition"></a>
<a id="tocstolerancedefinition"></a>

```json
{
  "uid": "yak7s7",
  "name": "detection_endstop_bottom",
  "lead": "0.0",
  "lag": "0.0",
  "absTol": "0.0",
  "relTol": "1",
  "kind": "Local"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|name|string|false|none|none|
|lead|string|false|none|none|
|lag|string|false|none|none|
|absTol|string|false|none|none|
|relTol|string|false|none|none|
|kind|string|false|none|none|

<h2 id="tocS_RBTTolerancesIOConfig">RBTTolerancesIOConfig</h2>
<!-- backwards compatibility -->
<a id="schemarbttolerancesioconfig"></a>
<a id="schema_RBTTolerancesIOConfig"></a>
<a id="tocSrbttolerancesioconfig"></a>
<a id="tocsrbttolerancesioconfig"></a>

```json
{
  "path": "C:/Rest/tolerances.xml"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|path|string|true|none|The path to the xml file to use for import or export of local tolerances.|

<h2 id="tocS_RBTExecutionReportCreationInfoData">RBTExecutionReportCreationInfoData</h2>
<!-- backwards compatibility -->
<a id="schemarbtexecutionreportcreationinfodata"></a>
<a id="schema_RBTExecutionReportCreationInfoData"></a>
<a id="tocSrbtexecutionreportcreationinfodata"></a>
<a id="tocsrbtexecutionreportcreationinfodata"></a>

```json
{
  "execConfigName": "TL MIL"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|execConfigName|string|true|none|Execution kind (example: SIL, TL MIL, SL MIL, etc.). Not case-sensitive.|

<h2 id="tocS_RBTExecutionReportCreationInfo">RBTExecutionReportCreationInfo</h2>
<!-- backwards compatibility -->
<a id="schemarbtexecutionreportcreationinfo"></a>
<a id="schema_RBTExecutionReportCreationInfo"></a>
<a id="tocSrbtexecutionreportcreationinfo"></a>
<a id="tocsrbtexecutionreportcreationinfo"></a>

```json
{
  "execConfigName": "TL MIL",
  "UIDs": [
    "22a",
    "22c"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UIDs|[string]|true|none|List with unique identifiers of the objects.|
|execConfigName|string|true|none|Execution kind (example: SIL, TL MIL, SL MIL, etc.).|

<h2 id="tocS_ExecutionResultMessage">ExecutionResultMessage</h2>
<!-- backwards compatibility -->
<a id="schemaexecutionresultmessage"></a>
<a id="schema_ExecutionResultMessage"></a>
<a id="tocSexecutionresultmessage"></a>
<a id="tocsexecutionresultmessage"></a>

```json
"list of result messages..."

```

The execution result messages for the requirement based test execution.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|false|none|The test case execution result message.|
|execResultStatus|string|false|none|The execution result status for the test execution.|

<h2 id="tocS_RBTestCaseExecutionResultData">RBTestCaseExecutionResultData</h2>
<!-- backwards compatibility -->
<a id="schemarbtestcaseexecutionresultdata"></a>
<a id="schema_RBTestCaseExecutionResultData"></a>
<a id="tocSrbtestcaseexecutionresultdata"></a>
<a id="tocsrbtestcaseexecutionresultdata"></a>

```json
"..."

```

The detailed test results

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comment|string|false|none|The comment for the requirement based test execution.|
|verdictUID|string|false|none|The verdict UID for the requirement based test execution.|
|execRecordUID|string|false|none|The execution record UID for the requirement based test execution.|
|rbTestCaseUID|string|false|none|The test case UID for the requirement based test execution.|
|execResultStatus|string|false|none|The execution result status for the requirement based test execution.|
|execResultMessages|[[ExecutionResultMessage](#schemaexecutionresultmessage)]|false|none|The execution result messages for the requirement based test execution.|
|verdictStatus|string|false|none|The verdict status for the requirement based test execution.|

<h2 id="tocS_RBTestCaseExecutionResultMapData">RBTestCaseExecutionResultMapData</h2>
<!-- backwards compatibility -->
<a id="schemarbtestcaseexecutionresultmapdata"></a>
<a id="schema_RBTestCaseExecutionResultMapData"></a>
<a id="tocSrbtestcaseexecutionresultmapdata"></a>
<a id="tocsrbtestcaseexecutionresultmapdata"></a>

```json
{
  "testResults": "...",
  "reportUIDs": "4fg6"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|testResults|object|false|none|The detailed test results mapped by execution kind|
|» **additionalProperties**|[RBTestCaseExecutionResultSetData](#schemarbtestcaseexecutionresultsetdata)|false|none|The detailed test results mapped by execution kind|
|reportUIDs|[string]|false|none|The UID of the generated model coverage report|

<h2 id="tocS_RBTestCaseExecutionResultSetData">RBTestCaseExecutionResultSetData</h2>
<!-- backwards compatibility -->
<a id="schemarbtestcaseexecutionresultsetdata"></a>
<a id="schema_RBTestCaseExecutionResultSetData"></a>
<a id="tocSrbtestcaseexecutionresultsetdata"></a>
<a id="tocsrbtestcaseexecutionresultsetdata"></a>

```json
"..."

```

The detailed test results mapped by execution kind

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|totalTests|string|false|none|The number of total results of the test execution.|
|updatedTests|string|false|none|The number of updated test executions.|
|skippedTests|string|false|none|The number of skipped test executions.|
|executedTests|string|false|none|The number of new test executions.|
|passedTests|string|false|none|The number of passed tests in the test execution.|
|failedTests|string|false|none|The number of failed tests in the test execution.|
|noVerdictTests|string|false|none|The number of tests with no verdict results in the test execution.|
|errorneousTests|string|false|none|The number of tests with errorneous results in the test execution.|
|execConfigUID|string|false|none|The execution kind UID|
|testResults|[[RBTestCaseExecutionResultData](#schemarbtestcaseexecutionresultdata)]|false|none|The detailed test results|

<h2 id="tocS_RBTExecutionData">RBTExecutionData</h2>
<!-- backwards compatibility -->
<a id="schemarbtexecutiondata"></a>
<a id="schema_RBTExecutionData"></a>
<a id="tocSrbtexecutiondata"></a>
<a id="tocsrbtexecutiondata"></a>

```json
{
  "execConfigNames": "SIL",
  "generateModelCoverageReport": false,
  "forceExecute": false
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|execConfigNames|[string]|true|none|List of execution kinds (example: SIL, TL MIL, SL MIL, etc.). Not case-sensitive.|
|generateModelCoverageReport|boolean|false|none|Specify (optional) if the model coverage report should be generated. Default value is false.|
|forceExecute|boolean|false|none|Specify (optional) if the test execution should be forced (all previous results will be discarded). Default value is false.|

<h2 id="tocS_RBTExecutionDataExtended">RBTExecutionDataExtended</h2>
<!-- backwards compatibility -->
<a id="schemarbtexecutiondataextended"></a>
<a id="schema_RBTExecutionDataExtended"></a>
<a id="tocSrbtexecutiondataextended"></a>
<a id="tocsrbtexecutiondataextended"></a>

```json
{
  "UIDs": "2UPb",
  "data": {
    "execConfigNames": "SIL",
    "generateModelCoverageReport": false,
    "forceExecute": false
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UIDs|[string]|true|none|List with unique identifiers of the objects.|
|data|[RBTExecutionData](#schemarbtexecutiondata)|false|none|none|

<h2 id="tocS_RBTExecutionDataNoReport">RBTExecutionDataNoReport</h2>
<!-- backwards compatibility -->
<a id="schemarbtexecutiondatanoreport"></a>
<a id="schema_RBTExecutionDataNoReport"></a>
<a id="tocSrbtexecutiondatanoreport"></a>
<a id="tocsrbtexecutiondatanoreport"></a>

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|execConfigNames|[string]|true|none|List of execution kinds (example: SIL, TL MIL, SL MIL, etc.).|
|forceExecute|boolean|false|none|Specify (optional) if the test execution should be forced (all previous results will be discarded). Default value is false.|

<h2 id="tocS_RBTExecutionDataExtendedNoReport">RBTExecutionDataExtendedNoReport</h2>
<!-- backwards compatibility -->
<a id="schemarbtexecutiondataextendednoreport"></a>
<a id="schema_RBTExecutionDataExtendedNoReport"></a>
<a id="tocSrbtexecutiondataextendednoreport"></a>
<a id="tocsrbtexecutiondataextendednoreport"></a>

```json
{
  "UIDs": "2UPb",
  "data": {
    "execConfigNames": "SIL",
    "forceExecute": false
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UIDs|[string]|true|none|List with unique identifiers of the objects.|
|data|[RBTExecutionDataNoReport](#schemarbtexecutiondatanoreport)|false|none|none|

<h2 id="tocS_RestRBTestCaseExportInfo">RestRBTestCaseExportInfo</h2>
<!-- backwards compatibility -->
<a id="schemarestrbtestcaseexportinfo"></a>
<a id="schema_RestRBTestCaseExportInfo"></a>
<a id="tocSrestrbtestcaseexportinfo"></a>
<a id="tocsrestrbtestcaseexportinfo"></a>

```json
{
  "UIDs": "2UPb",
  "exportDirectory": "C:/RestProfiles/VectorExport",
  "exportFormat": "EXCEL",
  "additionalOptions": {
    "csvDelimiter": "SEMICOLON",
    "singleFile": true,
    "architectureUid": "2Ai7"
  },
  "overwritePolicy": "OVERWRITE"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UIDs|[string]|true|none|List with the UIDs of the elements which will be exported|
|exportDirectory|string|true|none|Directory where to export the elements|
|exportFormat|string|false|none|The format of the exported test cases. Default value is EXCEL.|
|additionalOptions|[RestVectorExportDetails](#schemarestvectorexportdetails)|false|none|none|
|overwritePolicy|string|false|none|Overwrite policy: allowed values (not case-sensitive) are: EXTEND_NAME, in which case if the exported file exists on disk, its name will be extended and the original file on disk will be kept, OVERWRITE, in which case the original file on disk is overwritten, if it exists. Default value is EXTEND_NAME|

#### Enumerated Values

|Property|Value|
|---|---|
|exportFormat|TC|
|exportFormat|EXCEL|
|exportFormat|CSV|
|exportFormat|JSON|
|overwritePolicy|EXTEND_NAME|
|overwritePolicy|OVERWRITE|
|overwritePolicy|SKIP|

<h2 id="tocS_RequirementBasedTestCase">RequirementBasedTestCase</h2>
<!-- backwards compatibility -->
<a id="schemarequirementbasedtestcase"></a>
<a id="schema_RequirementBasedTestCase"></a>
<a id="tocSrequirementbasedtestcase"></a>
<a id="tocsrequirementbasedtestcase"></a>

```json
{
  "uid": "yak7s7",
  "name": "ExampleName",
  "description": "This is a description.",
  "kind": "TC",
  "length": 42,
  "draft": false,
  "lastModifiedDate": "01-Jan-2020 12:00:00",
  "folderUID": "12",
  "scopeUID": "24a",
  "requirementUIDs": [
    "121a"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|name|string|false|none|The name of the RBTestCase.|
|description|string|false|none|An optional description of the RBTestCase|
|kind|string|false|none|The datatype or kind of the RBTestCase. Usually "tc" or "csv".|
|length|integer(int64)|false|none|The length of the vector.|
|draft|boolean|false|none|States whether or not the RBTestCase is in Draft-Mode.|
|lastModifiedDate|string|false|none|The date of the last modification to the RBTestCase|
|folderUID|string|false|none|The unique identifier of the folder the RBTestCase belongs to.|
|scopeUID|string|false|none|The unique identifier of the scope the RBTestCase belongs to.|
|requirementUIDs|[string]|false|none|none|

<h2 id="tocS_RestRBTestCaseImportInfo">RestRBTestCaseImportInfo</h2>
<!-- backwards compatibility -->
<a id="schemarestrbtestcaseimportinfo"></a>
<a id="schema_RestRBTestCaseImportInfo"></a>
<a id="tocSrestrbtestcaseimportinfo"></a>
<a id="tocsrestrbtestcaseimportinfo"></a>

```json
{
  "paths": [
    "C:/RestProfiles/testCase.tc"
  ],
  "folderUID": "exampleUID123",
  "overwritePolicy": "SKIP",
  "draft": false,
  "csvDelimiter": "SEMICOLON",
  "importKind": "TC"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|paths|[string]|true|none|none|
|folderUID|string|false|none|The UID of the folder you want to import into. If not specified Test Cases will be imported in the default Test Cases folder.|
|overwritePolicy|string|false|none|Decides what happens in case of duplicate names. Can be "EXTEND_NAME", "OVERWRITE" or "SKIP". Default is "SKIP".|
|draft|boolean|false|none|Sets the Draft-Mode of the test cases. By default its value is false.|
|csvDelimiter|string|false|none|Relevant only for CSV export format. It can have one of the following values: "SEMICOLON", "COMMA", "COLON", "PIPE". Default value is "SEMICOLON".|
|importKind|string|false|none|The kind a file should be imported as. Possible values are: "TC" or "EXCEL". "TC" by default|

#### Enumerated Values

|Property|Value|
|---|---|
|overwritePolicy|EXTEND_NAME|
|overwritePolicy|OVERWRITE|
|overwritePolicy|SKIP|
|csvDelimiter|SEMICOLON|
|csvDelimiter|COMMA|
|csvDelimiter|COLON|
|csvDelimiter|PIPE|
|importKind|TC|
|importKind|EXCEL|

<h2 id="tocS_RBTestCaseRequirementsInfo">RBTestCaseRequirementsInfo</h2>
<!-- backwards compatibility -->
<a id="schemarbtestcaserequirementsinfo"></a>
<a id="schema_RBTestCaseRequirementsInfo"></a>
<a id="tocSrbtestcaserequirementsinfo"></a>
<a id="tocsrbtestcaserequirementsinfo"></a>

```json
{
  "requirementUIDs": [
    "284"
  ],
  "testCaseUIDs": [
    "27m"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|requirementUIDs|[string]|true|none|none|
|testCaseUIDs|[string]|true|none|none|

<h2 id="tocS_Architecture">Architecture</h2>
<!-- backwards compatibility -->
<a id="schemaarchitecture"></a>
<a id="schema_Architecture"></a>
<a id="tocSarchitecture"></a>
<a id="tocsarchitecture"></a>

```json
{
  "uid": "yak7s7",
  "architectureKind": "C-Code",
  "name": "powerwindow_window_controller [C-Code]",
  "propList": "\"architectureProperties\": {\r\n      \"Test Mode\": \"GREY_BOX\",\r\n      \"Import Date\": \"Sep 18, 2020 1:19:43 PM\",\r\n       ....}"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|architectureKind|string|false|read-only|The string representation of the concrete architecture<br>, e.g. 'Simulink', 'C-Code', 'TargetLink'.|
|name|string|false|read-only|The architecture name as specified by the model.|
|propList|object|false|read-only|The Architecture property List|
|» **additionalProperties**|string|false|read-only|The Architecture property List|

<h2 id="tocS_CCodeImportInfo">CCodeImportInfo</h2>
<!-- backwards compatibility -->
<a id="schemaccodeimportinfo"></a>
<a id="schema_CCodeImportInfo"></a>
<a id="tocSccodeimportinfo"></a>
<a id="tocsccodeimportinfo"></a>

```json
{
  "modelFile": "C:/Models/PowerWindow/CodeModel.xml",
  "mappingFile": "C:/Models/PowerWindow/mappingFile.xml"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|modelFile|string|true|none|File name of the C-Code XML file|
|mappingFile|string|false|none|File name of the mapping XML file. The file must be provided if architectures are already available in the profile. The file is used to map the first imported architecture to the new imported C-Code architecture.|

<h2 id="tocS_ECWrapperResultInfo">ECWrapperResultInfo</h2>
<!-- backwards compatibility -->
<a id="schemaecwrapperresultinfo"></a>
<a id="schema_ECWrapperResultInfo"></a>
<a id="tocSecwrapperresultinfo"></a>
<a id="tocsecwrapperresultinfo"></a>

```json
{
  "uid": "yak7s7",
  "ecModelFile": "C:/Model/powerwindow_ec.mdl",
  "ecInitScript": "C:/Model/start.m"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|ecModelFile|string|false|read-only|The absolute path to the created Embedded Coder Wrapper model|
|ecInitScript|string|false|read-only|The absolute path to the created init script for the Embedded Coder Wrapper model. Can be empty.|

<h2 id="tocS_ECWrapperImportInfo">ECWrapperImportInfo</h2>
<!-- backwards compatibility -->
<a id="schemaecwrapperimportinfo"></a>
<a id="schema_ECWrapperImportInfo"></a>
<a id="tocSecwrapperimportinfo"></a>
<a id="tocsecwrapperimportinfo"></a>

```json
{
  "ecModelFile": "C:/Model/powerwindow_ec.mdl",
  "ecInitScript": "C:/Model/start.m"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ecModelFile|string|true|none|The absolute or relative path to the Embedded Coder model.|
|ecInitScript|string|false|none|The absolute or relative path to the init script of the Embedded Coder model.|

<h2 id="tocS_ECImportInfo">ECImportInfo</h2>
<!-- backwards compatibility -->
<a id="schemaecimportinfo"></a>
<a id="schema_ECImportInfo"></a>
<a id="tocSecimportinfo"></a>
<a id="tocsecimportinfo"></a>

```json
{
  "ecModelFile": "C:/Model/powerwindow_ec.mdl",
  "ecInitScript": "C:/Model/start.m",
  "parameterHandling": "OFF",
  "testMode": "BLACK_BOX",
  "fixedStepSolver": false,
  "inDepthCcodeAnalysis": false,
  "subsystemMatcher": "Model/SubsystemA.*|Model/SubsystemB",
  "parameterMatcher": "ParameterA|ParameterB|ParameterC"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ecModelFile|string|true|none|The absolute or relative path to the EmbeddedCoder model.<br>This file is mandatory and may not be undefined.|
|ecInitScript|string|false|none|The absolute or relative path to the init script of the EmbeddedCoder model.<br>This attribute may be undefined.<br>If the specified file path is invalid, an error is reported.|
|parameterHandling|string|false|none|Specifies how parameter variables are handled. Can be 'OFF' or 'EXPLICIT_PARAMETER'.<br>'OFF': Only regular inputs in the interface of subsystems are observed.<br>'EXPLICIT_PARAMETER': Parameter variables are regarded as additional<br>inputs to subsystems.<br>Default is 'EXPLICIT_PARAMETER'.<br>If not specified (undefined or invalid), the default value is used.|
|testMode|string|false|none|Specifies the test mode. Can be 'BLACK_BOX' or 'GREY_BOX'.<br>If set to 'GreyBox', local variables are regarded as additional outputs of subsystems.<br>For BlackBox-Testing only the regularoutputs in the interfaces of subsystems are observed.<br>Default is 'GreyBox'.<br>If not specified (undefined or invalid), the default value is used.|
|fixedStepSolver|boolean|false|none|Handling when a non-fixed-step solver is ecountered: If 'true', the solver is automatically set to fixed-step.<br>Otherwise an error is issued.Default is 'false'.|
|inDepthCcodeAnalysis|boolean|false|none|true: Simulink model and C-Code model are imported.<br>false: indicates that a SL SIL simulation is supported.<br>C-Code and mapping are omitted.<br>Default is 'true'|
|subsystemMatcher|string|false|none|A whitelist of all subsystems you would like to import.<br>Uses the regular expression standard.<br>Each subsystem is identified by its virtual path inside the model.<br>If no value is defined, all subsystems are imported.<br>If the specified regular expression does not produce any match, an error is reported.|
|parameterMatcher|string|false|none|A whitelist of all parameters you would like to import.<br>Uses the regular expression standard.<br>Each parameter is identified by its name.<br>If no value is defined, all calibrations are imported.<br>If the specified regular expression does not produce any match, no calibration is imported.<br>The list cannot be applied, if parameterHandling is set to 'OFF'.<br>Please note, that model workspace parameters have their name extended by the model they <br>are located in and need to be adressed accordingly in the following way: 'modelname:paramname'|

#### Enumerated Values

|Property|Value|
|---|---|
|parameterHandling|OFF|
|parameterHandling|EXPLICIT_PARAMETER|
|testMode|BLACK_BOX|
|testMode|GREY_BOX|

<h2 id="tocS_UpdateModelPath">UpdateModelPath</h2>
<!-- backwards compatibility -->
<a id="schemaupdatemodelpath"></a>
<a id="schema_UpdateModelPath"></a>
<a id="tocSupdatemodelpath"></a>
<a id="tocsupdatemodelpath"></a>

```json
{
  "slModelFile": "C:/Models/PowerWindow/ml2017b_tl50/powerwindow_sl_v01.mdl",
  "slInitScript": "C:/Models/PowerWindow/ml2017b_tl50/start.m",
  "addModelInfo": "C:/Models/PowerWindow/ml2017b_tl50/ModelInfoSl.xml",
  "tlModelFile": "C:/Models/PowerWindow/ml2017b_tl50/powerwindow_tl_v01.mdl",
  "tlInitScript": "C:/Models/PowerWindow/ml2017b_tl50/start.m",
  "environment": "C:/Models/PowerWindow/ml2017b_tl50/env.xml"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|slModelFile|string|false|none|The path to the Simulink model(.mdl|.slx).|
|slInitScript|string|false|none|The path to the init script of the Simulink model.|
|addModelInfo|string|false|none|The path to additional model information.|
|tlModelFile|string|false|none|The path to the TargetLink model file (.mdl|.slx).|
|tlInitScript|string|false|none|The path to the init script of the TargetLink model.|
|environment|string|false|none|The path to XML file including information about<br>    environmental files like additional code.|

<h2 id="tocS_SampleTime">SampleTime</h2>
<!-- backwards compatibility -->
<a id="schemasampletime"></a>
<a id="schema_SampleTime"></a>
<a id="tocSsampletime"></a>
<a id="tocssampletime"></a>

```json
{
  "uid": "s567k",
  "seconds": "0.01"
}

```

The sample time of the scope.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|none|The unique identifier (UID) of this object.|
|seconds|string|false|none|The sample time as a value given in seconds.|

<h2 id="tocS_Scope">Scope</h2>
<!-- backwards compatibility -->
<a id="schemascope"></a>
<a id="schema_Scope"></a>
<a id="tocSscope"></a>
<a id="tocsscope"></a>

```json
{
  "uid": "k25pq",
  "name": "string",
  "topLevel": true,
  "kind": "SUT",
  "path": "string",
  "architecture": "string",
  "sampleTime": {
    "uid": "s567k",
    "seconds": "0.01"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|none|The unique identifier (UID) of this object.|
|name|string|false|none|The scope name.|
|topLevel|boolean|false|none|True if scope is a toplevel scope.|
|kind|string|false|none|Scope kind.|
|path|string|false|none|Scope path.|
|architecture|string|false|none|The corresponding architecture of the scope.|
|sampleTime|[SampleTime](#schemasampletime)|false|none|The sample time of the scope.|

#### Enumerated Values

|Property|Value|
|---|---|
|kind|SUT|
|kind|DUMMY|
|kind|ENVIRONMENT|
|kind|HIDDEN_INTERNAL|
|kind|VIRTUAL|

<h2 id="tocS_RestSignal">RestSignal</h2>
<!-- backwards compatibility -->
<a id="schemarestsignal"></a>
<a id="schema_RestSignal"></a>
<a id="tocSrestsignal"></a>
<a id="tocsrestsignal"></a>

```json
{
  "uid": "yak7s7",
  "identifier": "INPUT:driver_up:var"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|identifier|string|false|read-only|The signal identifier.|

<h2 id="tocS_SLImportInfo">SLImportInfo</h2>
<!-- backwards compatibility -->
<a id="schemaslimportinfo"></a>
<a id="schema_SLImportInfo"></a>
<a id="tocSslimportinfo"></a>
<a id="tocsslimportinfo"></a>

```json
{
  "slModelFile": "C:/Models/PowerWindow/PowerWindow_SL.mdl",
  "slInitScriptFile": "C:/Models/PowerWindow/start.m",
  "parameterHandling": "EXPLICIT_PARAMETER",
  "testMode": "BLACK_BOX",
  "fixedStepSolver": true,
  "mappingFile": "C:/Models/PowerWindow/Mapping.xml",
  "subsystemMatcher": "Model|Model/SubsystemA.*|Model/SubsystemB/SubsystemBA",
  "parameterMatcher": "ParameterA|ParameterB|ParameterC"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|slModelFile|string|true|none|The absolute or relative path to the Simulink model.<br>This file is mandatory and may not be undefined!|
|slInitScriptFile|string|false|none|The absolute or relative path to the init script of the Simulink model.<br>This attribute may be undefined.<br>If the specified file path is invalid, an error is reported.|
|parameterHandling|string|false|none|Specifies how parameter variables are handled. Can be 'OFF' or 'EXPLICIT_PARAMETER'.<br>'OFF': Only regular inputs in the interface of subsystems are observed.<br>'EXPLICIT_PARAMETER': Parameter variables are regarded as additional inputs to subsystems.<br>Default is 'EXPLICIT_PARAMETER'.<br>If not specified (undefined or invalid), the default value is used.|
|testMode|string|false|none|Specifies the test mode. Can be 'BLACK_BOX' or 'GREY_BOX'.<br>If set to 'GREY_BOX', local variables are regarded as additional outputs of subsystems.<br>For Black Box-Testing only the regular outputs in the interfaces of subsystems are observed.<br>Default is 'GREY_BOX'.<br>If not specified (undefined or invalid), the default value is used.|
|fixedStepSolver|boolean|false|none|Defines, if the fixed step solver will be set or not. Can be true or false.<br>true: The analyzed Simulink model will be set to the fixed-step solver type automatically.<br> The usage of the EmbeddedPlatform requires a fixed-step solver. If the model is open and<br>the fixed-step solver is not already set, this might lead to a modified model.<br>false: The analyzed Simulink model will not be set to the fixed-step solver automatically.<br>If the fixed-step solver is not already set in the model, the method return with state of<br>a non fixed-step solver. In order to proceed the user has to set the fixed-step solver<br>manually in the Simulink simulation settings.<br>Default is 'false'.<br>Note: The option is ignored if the model is currently not in an open/loaded state. In this case it has no visible side-effect.|
|mappingFile|string|false|none|File name of the mapping XML file. The file must be provided if architectures are already available in the profile. The file is used to map the first imported architecture to the new imported Simulink architecture.<br>This attribute may be undefined.<br>If the specified file path is invalid, an error is reported.|
|subsystemMatcher|string|false|none|A whitelist of all subsystems you would like to import.<br>Uses the regular expression standard.<br>Each subsystem is identified by its virtual path inside the model.<br>If no value is defined, all subsystems are imported.<br>If the specified regular expression does not produce any match, an error is reported.<br>Keep in mind that having multiple Toplevel-Subsystem will result in an error.|
|parameterMatcher|string|false|none|A whitelist of all parameters you would like to import.<br>Uses the regular expression standard.<br>Each parameter is identified by its name.<br>If no value is defined, all parameters are imported.<br>If the specified regular expression does not produce any match, no parameter is imported.<br>The list cannot be applied, if parameterHandling is set to 'OFF'.<br>Please note, that model workspace parameters have their name extended by the model they <br>are located in and need to be adressed accordingly in the following way: 'modelname:paramname'|

#### Enumerated Values

|Property|Value|
|---|---|
|parameterHandling|OFF|
|parameterHandling|EXPLICIT_PARAMETER|
|testMode|BLACK_BOX|
|testMode|GREY_BOX|

<h2 id="tocS_TLImportInfo">TLImportInfo</h2>
<!-- backwards compatibility -->
<a id="schematlimportinfo"></a>
<a id="schema_TLImportInfo"></a>
<a id="tocStlimportinfo"></a>
<a id="tocstlimportinfo"></a>

```json
{
  "tlModelFile": "C:/Model/PowerWindow_TL.mdl",
  "tlInitScript": "C:/Model/start.m",
  "slModelFile": "C:/Model/PowerWindow_SL.mdl",
  "slInitScript": "C:/Model/start.m",
  "environment": "C:/Model/environment.xml",
  "useExistingCode": true,
  "activateModelLinking": false,
  "closedLoopModel": false,
  "fixedStepSolver": false,
  "tlSubsystem": "PowerWindow",
  "calibrationHandling": "LIMITED_BLOCKSET",
  "testMode": "BLACK_BOX",
  "mappingFileForTLArch": "C:/Model/tlmapping.xml",
  "mappingFileForCCodeArch": "C:/Model/ccodemapping.xml",
  "mappingFileForSLArch": "C:/Model/slmapping.xml",
  "subsystemMatcher": "Model/RootSubsystem/Subsystem/RootSubsystem/SubsystemA.*|Model/RootSubsystem/Subsystem/RootSubsystem/SubsystemB",
  "calibrationMatcher": "CalibrationA|CalibrationB|CalibrationC",
  "cfileMatcher": "FilenameA\\.c|FilenameB\\.c"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tlModelFile|string|true|none|The absolute or relative path to the TargetLink model file (.mdl|.slx).|
|tlInitScript|string|false|none|The absolute or relative path to the script defining all parameters needed for initializing the TL-model.<br>If not provided, the TL-model is assumed to be selfcontained.|
|slModelFile|string|false|none|The absolute or relative path to the Simulink model file (.mdl|.slx).<br> Note: If a TargetLink model is given, the SL-model is assumed to be equivalent to the TL-model.|
|slInitScript|string|false|none|The absolute or relative path to the script defining all parameters needed for initializing the SL-model. <br> If not provided, the SL-model is assumed to be selfcontained.|
|environment|string|false|none|The absolute or relative path to XML file including information about environmental files like additional code. (see specifications in CodeGeneration.dtd).|
|useExistingCode|boolean|false|none|Determine if code generation needs to be done.<br>'true': Code generation is not explicitly performed.<br>Instead it is assumed that the required code files are already generated and<br>that the corresponding DataDictionary of the model includes information about the code generation.<br> 'false': Code generation is explicitly performed during the analysis.<br>The resulting code is used for further steps.<br><br>Default is 'false'.|
|activateModelLinking|boolean|false|none|Determine if the source code needs to be linked to the TargetLink model.<br>'true': A link between the source code and the TargetLink model will be established.<br>This setting may lead to a modified TargetLink model.<br>To accomplish this link relation, the TargetLink option 'ExtendedBlockComments' needs to be enabled <br>with a subsequent TargetLink code generation.<br>'false': The source code model linking is not explictitly set by EmbeddedPlatform.<br>Default is 'false'.|
|closedLoopModel|boolean|false|none|Determine if the SUT envoronment is analyzed during extraction<br>'true': The environment of the SUT is also analyzed during the model extraction.<br>Important for analyzing closed-loop models. <br>'false': Only the SUT is considered during the model extraction. <br>Default is 'false'.|
|fixedStepSolver|boolean|false|none|Defines, if the fixed step solver will be set or not.<br>'true': The analyzed models (TargetLink model and Simulink model) will be set to the fixed-step solver type automatically.<br>The usage of the EmbeddedPlatform requires a fixed-step solver. <br>If the model is open and the fixed-step solver is not already set, <br>this might lead to a modified model.<br>'false': The analyzed models (TargetLink model and Simulink model) will not be set to the fixed-step solver automatically.<br>If the fixed-step solver is not already set in the model, an exception is thrown.<br>In order to proceed the user has to set the fixed-step solver manually in the simulation settings.<br>Note: The option is ignored if the model is currently not in an open/loaded state.<br>In this case it has no visible side-effect. <br>Default is 'false'.|
|tlSubsystem|string|false|none|Name of the Subsystem representing the TL toplevel subsystem for the analysis.<br>Note: Argument is obligatory if there is more than one toplevel system in the model.|
|calibrationHandling|string|false|none|Determine how calibration variables are being handled.<br>'OFF': Only regular inputs in the interface of subsystems are observed.<br>'EXPLICIT_PARAMETER': Calibration variables are regarded as additional inputs to subsystems.<br>Their value is set once during the initial phase of the simulation and is held constant thereafter.<br>'LIMITED_BLOCKSET': Calibration variables are regarded as additional inputs to subsystems.<br>Their value is set once during the initial phase of the simulation and is held constant thereafter.<br>Enable support for calibration within block properties, not using workspace calibrations.<br>Note: The supported Set of calibratable TL-Blocks is different from 'EXPLICIT_PARAMETER'.Default is 'EXPLICIT_PARAMETER'.<br>|
|testMode|string|false|none|Specifies the test mode. Can be 'BLACK_BOX' or 'GREY_BOX'.<br>If set to 'GREY_BOX', local variables are regarded as additional outputs of subsystems.<br>For Black Box-Testing only the regular outputs in the interfaces of subsystems are observed.<br>Default is 'GREY_BOX'.<br>If not specified (undefined or invalid), the default value is used.|
|mappingFileForTLArch|string|false|none|The absolute or relative path to the mapping file for TargetLink architecture mapping.<br>At least one mapping file must be provided if architectures are already available in the profile. The file is used to map the first imported architecture to the new imported TargetLink architecture. <br>If this file is not provided, the mapping to the first imported architecture is derived from the auto-generated <br> mapping between TargetLink, C-Code, and Simulink (if available). For the derivation to work, at least one of <br> these architectures must be mapped to the first imported architecture via a specified mapping file|
|mappingFileForCCodeArch|string|false|none|The absolute or relative path to the mapping file for C-Code architecture mapping.<br>At least one mapping must be provided if architectures are already available in the profile. The file is used to map the first imported architecture to the new imported C-Code architecture. <br>If this file is not provided, the mapping to the first imported architecture is derived from the auto-generated <br> mapping between TargetLink, C-Code, and Simulink (if available). For the derivation to work, at least one of <br> these architectures must be mapped to the first imported architecture via a specified mapping file|
|mappingFileForSLArch|string|false|none|The absolute or relative path to the mapping file for Simulink architecture mapping.<br>At least one mapping must be provided if a Simulink architecture is additionally imported and<vr> architectures are already available in the profile.<br>The file is used to map the first imported architecture to the new imported Simulink architecture.<br>If this file is not provided, the mapping to the first imported architecture is derived from the auto-generated <br> mapping between TargetLink, C-Code, and Simulink (if available). For the derivation to work, at least one of <br> these architectures must be mapped to the first imported architecture via a specified mapping file|
|subsystemMatcher|string|false|none|A whitelist of all subsystems you would like to import.<br>Uses the regular expression standard.<br>Each subsystem is identified by its virtual path inside the model.<br>If no value is defined, all subsystems are imported.<br>If the specified regular expression does not produce any match, only the toplevel subsystem is imported. <br>The root subsystem is always imported.<br>Please note that the subsystem-path has to include the Targetlink wrapper.|
|calibrationMatcher|string|false|none|A whitelist of all calibrations you would like to import.<br>Uses the regular expression standard.<br>Each calibration is identified by its name.<br>If no value is defined, all calibrations are imported.<br>If the specified regular expression does not produce any match, no calibration is imported.<br>The list cannot be applied, if calibrationHandling is set to 'OFF'.|
|cfileMatcher|string|false|none|A whitelist of all c-code files you would like to import.<br>Uses the regular expression standard.<br>Each file is identified by its name.<br>If no value is defined, all files are imported.<br>If the specified regular expression does not produce any match, no file is imported.|

#### Enumerated Values

|Property|Value|
|---|---|
|calibrationHandling|OFF|
|calibrationHandling|EXPLICIT_PARAMETER|
|calibrationHandling|LIMITED_BLOCKSET|
|testMode|BLACK_BOX|
|testMode|GREY_BOX|

<h2 id="tocS_Assumption">Assumption</h2>
<!-- backwards compatibility -->
<a id="schemaassumption"></a>
<a id="schema_Assumption"></a>
<a id="tocSassumption"></a>
<a id="tocsassumption"></a>

```json
{
  "id": "uisc23"
}

```

The environmental assumptions to use for this run.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|The Assumption UID.|

<h2 id="tocS_Config">Config</h2>
<!-- backwards compatibility -->
<a id="schemaconfig"></a>
<a id="schema_Config"></a>
<a id="tocSconfig"></a>
<a id="tocsconfig"></a>

```json
{
  "isSubscopesGoalsConsidered": false,
  "targetDefinitions": [
    {
      "label": "Statement"
    }
  ],
  "folderName": "myFolder",
  "checkUnreachableProperties": false,
  "pllString": "STM;D;CDC",
  "engineSettings": {
    "timeoutSeconds": 500,
    "handlingRateThreshold": 50,
    "analyseSubScopesHierarchically": true,
    "engineAtg": {
      "name": "ATG",
      "searchDepthSteps": 10,
      "executionMode": "TOP_DOWN",
      "mutateExistingVectors": false,
      "timeoutSecondsPerSubsystem": 500
    },
    "engineCv": {
      "name": "CV",
      "searchDepthSteps": 10,
      "timeoutSecondsPerSubsystem": 500,
      "timeoutSecondsPerProperty": 500,
      "memoryLimitMb": 500,
      "loopUnroll": 50,
      "coreEngines": [
        {
          "name": "SMIBMC"
        }
      ],
      "assumptionCheckEnabled": true,
      "searchFocus": "BALANCED",
      "parallelExecutionMode": "BALANCED",
      "maximumNumberOfThreads": 1
    },
    "allowDenormalizedFloats": true
  },
  "scopeUid": "string",
  "assumptions": [
    {
      "id": "uisc23"
    }
  ],
  "drivers": [
    {
      "id": "uisc23"
    }
  ],
  "initializationVectorUID": "exampleUID123"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|isSubscopesGoalsConsidered|boolean|false|none|Whether or not goals from sub scopes should be considered. <br>Default is 'true'|
|targetDefinitions|[[TargetDefinition](#schematargetdefinition)]|false|none|[The target definitions to use for this run. <br>If no target definitions are provided, and no PLL is given, the default target definitions are used]|
|folderName|string|false|none|Name of the folder to store Stimuli Vectors in. If the specified folder doesn't exists, it will be created with the given name. <br>If no folder is specified the default folder 'Default Stimuli Vectors' will be used.|
|checkUnreachableProperties|boolean|false|none|Whether or not unreachable properties should be (re-)checked. <br>Default is 'false'|
|pllString|string|false|none|PLL String for specifc goals to be reached. Default is '::' which matches all goals. Use e.g. 'STM;D;CDC' to find stimuli vectors for statement, decision, and condition/decision coverage. Individual PLLs can be addressed by their specific label (e.g. 'D:4:1'). Multiple PLLs can be concatenated using semicolon, e.g. 'D:4:1;C:2'. See the user guide for more information about the property location labels. <br>If this is null or empty, only the selected target definitions will be used. If in that case, the target definitions are be empty, the default target definitions are used.|
|engineSettings|[EngineSettings](#schemaenginesettings)|false|none|The engine settings to use for this run.|
|scopeUid|string|true|none|The UID of the entry scope to use for this run.|
|assumptions|[[Assumption](#schemaassumption)]|false|none|[The environmental assumptions to use for this run.]|
|drivers|[[Driver](#schemadriver)]|false|none|[The drivers to use for this run.]|
|initializationVectorUID|string|false|none|The UID of the RequirementBasedTestCase or B2BStimuliVector which shall be used to initialize the engine|

<h2 id="tocS_CoreEngine">CoreEngine</h2>
<!-- backwards compatibility -->
<a id="schemacoreengine"></a>
<a id="schema_CoreEngine"></a>
<a id="tocScoreengine"></a>
<a id="tocscoreengine"></a>

```json
{
  "name": "SMIBMC"
}

```

The core engines to use <br>Note: If no core engine is provided, all core engines are used by default!

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|The name of the core engine.If no core engine is provided, all core engines are used by default!|

#### Enumerated Values

|Property|Value|
|---|---|
|name|SMIBMC|
|name|VIS|
|name|AUTOFXP|
|name|CBMC|
|name|ISAT|

<h2 id="tocS_Driver">Driver</h2>
<!-- backwards compatibility -->
<a id="schemadriver"></a>
<a id="schema_Driver"></a>
<a id="tocSdriver"></a>
<a id="tocsdriver"></a>

```json
{
  "id": "uisc23"
}

```

The drivers to use for this run.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|The Driver source UID.|

<h2 id="tocS_EngineAtg">EngineAtg</h2>
<!-- backwards compatibility -->
<a id="schemaengineatg"></a>
<a id="schema_EngineAtg"></a>
<a id="tocSengineatg"></a>
<a id="tocsengineatg"></a>

```json
{
  "name": "ATG",
  "searchDepthSteps": 10,
  "executionMode": "TOP_DOWN",
  "mutateExistingVectors": false,
  "timeoutSecondsPerSubsystem": 500
}

```

The ATG engine. <br>Note: If neither ATG, nor CV engine is provided, both, ATG and CV are used together, using their default settings!

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|The name of the engine (heuristic). Currently, only 'ATG' is allowed. <br>Default is 'ATG'|
|searchDepthSteps|integer(int32)|false|none|The search depth (number of SUT iterations) <br>Default is '20'|
|executionMode|string|false|none|The search direction, bottom up or top down <br>Default is 'TOP_DOWN'|
|mutateExistingVectors|boolean|false|none|Defines whether or not the Mutation Based ATG engine shall be used. <br>MATG requires existing vectors to produce new results. <br>Default is 'false'|
|timeoutSecondsPerSubsystem|integer(int32)|false|none|Timeout (seconds) per scope <br>Default is '300'|

#### Enumerated Values

|Property|Value|
|---|---|
|executionMode|TOP_DOWN|
|executionMode|BOTTOM_UP|

<h2 id="tocS_EngineCv">EngineCv</h2>
<!-- backwards compatibility -->
<a id="schemaenginecv"></a>
<a id="schema_EngineCv"></a>
<a id="tocSenginecv"></a>
<a id="tocsenginecv"></a>

```json
{
  "name": "CV",
  "searchDepthSteps": 10,
  "timeoutSecondsPerSubsystem": 500,
  "timeoutSecondsPerProperty": 500,
  "memoryLimitMb": 500,
  "loopUnroll": 50,
  "coreEngines": [
    {
      "name": "SMIBMC"
    }
  ],
  "assumptionCheckEnabled": true,
  "searchFocus": "BALANCED",
  "parallelExecutionMode": "BALANCED",
  "maximumNumberOfThreads": 1
}

```

The CV engine. <br>Note: If neither ATG, nor CV engine is provided, both, ATG and CV are used together, using their default settings!

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|The name of the engine (heuristic). Currently, only 'CV' is allowed. <br>Default is 'CV'|
|searchDepthSteps|integer(int32)|false|none|The search depth (number of SUT iterations) <br>Default is '10'|
|timeoutSecondsPerSubsystem|integer(int32)|false|none|Timeout (seconds) per scope <br>Default is '-1' (unlimited)|
|timeoutSecondsPerProperty|integer(int32)|false|none|Timeout (seconds) per coverage property <br>Default is '60'|
|memoryLimitMb|integer(int32)|false|none|The maximum amount of system memory to use (MB) <br>Default is '-1' (unlimited)|
|loopUnroll|integer(int32)|false|none|The number of internal loop unwindings for potentially unbounded loops within each SUT iteration. <br>Default is '50'|
|coreEngines|[[CoreEngine](#schemacoreengine)]|false|none|[The core engines to use <br>Note: If no core engine is provided, all core engines are used by default!]|
|assumptionCheckEnabled|boolean|false|none|Whether or not core engines are allowed to explicitly checkthe satisfiability of the selected assumptions. <br>Default is 'true'|
|searchFocus|string|false|none|The search focus of the core engines. <br>Default is 'BALANCED'|
|parallelExecutionMode|string|false|none|The mode used for the parallel engine execution.If maximum number of threads used is 1, the value of this parameter is not used (instead the default value BALANCED will be used).|
|maximumNumberOfThreads|integer(int32)|false|none|The maximum number of threads available for parallel engine execution for core engines. Valid values are between 1 and available number of cores. It is possible to set this parameter to a value of -1, which will compute the number of threads automatically as half of the available number of cores. <br>Default is '1'|

#### Enumerated Values

|Property|Value|
|---|---|
|searchFocus|BALANCED|
|searchFocus|REACHABLE|
|searchFocus|UNREACHABLE|
|parallelExecutionMode|BALANCED|
|parallelExecutionMode|ENGINES|
|parallelExecutionMode|GOALS|

<h2 id="tocS_EngineSettings">EngineSettings</h2>
<!-- backwards compatibility -->
<a id="schemaenginesettings"></a>
<a id="schema_EngineSettings"></a>
<a id="tocSenginesettings"></a>
<a id="tocsenginesettings"></a>

```json
{
  "timeoutSeconds": 500,
  "handlingRateThreshold": 50,
  "analyseSubScopesHierarchically": true,
  "engineAtg": {
    "name": "ATG",
    "searchDepthSteps": 10,
    "executionMode": "TOP_DOWN",
    "mutateExistingVectors": false,
    "timeoutSecondsPerSubsystem": 500
  },
  "engineCv": {
    "name": "CV",
    "searchDepthSteps": 10,
    "timeoutSecondsPerSubsystem": 500,
    "timeoutSecondsPerProperty": 500,
    "memoryLimitMb": 500,
    "loopUnroll": 50,
    "coreEngines": [
      {
        "name": "SMIBMC"
      }
    ],
    "assumptionCheckEnabled": true,
    "searchFocus": "BALANCED",
    "parallelExecutionMode": "BALANCED",
    "maximumNumberOfThreads": 1
  },
  "allowDenormalizedFloats": true
}

```

The engine settings to use for this run.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|timeoutSeconds|integer(int32)|false|none|Global timeout (seconds) for the execution <br>Default is '-1' (unlimited)|
|handlingRateThreshold|integer(int32)|false|none|After each scope is analyzed, the 'handled rate' of the entry scope (potentially including goals from subscopes) is checked against this threshold and the stimuli vector generation is stopped when it is reached. Allowed range are integers from [1, 100] (percent of handled goals). <br>Default: 100|
|analyseSubScopesHierarchically|boolean|false|none|Enables / disables recursive analysis of subscopes. <br>Default is 'true'|
|engineAtg|[EngineAtg](#schemaengineatg)|false|none|The ATG engine. <br>Note: If neither ATG, nor CV engine is provided, both, ATG and CV are used together, using their default settings!|
|engineCv|[EngineCv](#schemaenginecv)|false|none|The CV engine. <br>Note: If neither ATG, nor CV engine is provided, both, ATG and CV are used together, using their default settings!|
|allowDenormalizedFloats|boolean|false|none|Whether or not the engine may produce denormalized floats. <br>Default is 'true'|

<h2 id="tocS_TargetDefinition">TargetDefinition</h2>
<!-- backwards compatibility -->
<a id="schematargetdefinition"></a>
<a id="schema_TargetDefinition"></a>
<a id="tocStargetdefinition"></a>
<a id="tocstargetdefinition"></a>

```json
{
  "label": "Statement"
}

```

The target definitions to use for this run. <br>If no target definitions are provided, and no PLL is given, the default target definitions are used

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|label|string|true|none|The label of the target definition.|

<h2 id="tocS_ReportCreationInfo">ReportCreationInfo</h2>
<!-- backwards compatibility -->
<a id="schemareportcreationinfo"></a>
<a id="schema_ReportCreationInfo"></a>
<a id="tocSreportcreationinfo"></a>
<a id="tocsreportcreationinfo"></a>

```json
{
  "UIDs": [
    "2UPb",
    "3rH8"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UIDs|[string]|true|none|List with unique identifiers of the objects.|

<h2 id="tocS_CodeCoverageGoal">CodeCoverageGoal</h2>
<!-- backwards compatibility -->
<a id="schemacodecoveragegoal"></a>
<a id="schema_CodeCoverageGoal"></a>
<a id="tocScodecoveragegoal"></a>
<a id="tocscodecoveragegoal"></a>

```json
{
  "pll": "STM:1",
  "type": "Statement",
  "line": 390,
  "file": "power_widow_control.c",
  "properties": [
    {
      "pll": "STM:76:0",
      "status": "Unknown",
      "coveringVectors": [
        "testCase"
      ]
    }
  ],
  "expression": "(obstacle_position!=0)",
  "blocks": [
    "string"
  ],
  "comment": "Comment",
  "justified": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pll|string|false|none|PLL string of the coverage goal.|
|type|string|false|none|Goal type of the coverage goal.|
|line|integer(int32)|false|none|The line number of the location where the coverage goal is located in the file.|
|file|string|false|none|The file name where the coverage property can be located.|
|properties|[[CodeCoverageProperty](#schemacodecoverageproperty)]|false|none|[A list with coverage goal properties.]|
|expression|string|false|none|Expression of the coverage goal.|
|blocks|[string]|false|none|none|
|comment|string|false|none|The comment.|
|justified|boolean|false|none|If this goal is justified|

<h2 id="tocS_CodeCoverageProperty">CodeCoverageProperty</h2>
<!-- backwards compatibility -->
<a id="schemacodecoverageproperty"></a>
<a id="schema_CodeCoverageProperty"></a>
<a id="tocScodecoverageproperty"></a>
<a id="tocscodecoverageproperty"></a>

```json
{
  "pll": "STM:76:0",
  "status": "Unknown",
  "coveringVectors": [
    "testCase"
  ]
}

```

A list with coverage goal properties.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pll|string|false|none|PLL string of the coverage property.|
|status|string|false|none|Status of the coverage property.|
|coveringVectors|[string]|false|none|none|

<h2 id="tocS_CodeCoverageGoalSummary">CodeCoverageGoalSummary</h2>
<!-- backwards compatibility -->
<a id="schemacodecoveragegoalsummary"></a>
<a id="schema_CodeCoverageGoalSummary"></a>
<a id="tocScodecoveragegoalsummary"></a>
<a id="tocscodecoveragegoalsummary"></a>

```json
{
  "coverageGoal": "<Goal Type>",
  "coveredCompletelyCount": 27,
  "coveredCompletelyPercentage": 9.3426,
  "coveredPartiallyCount": 0,
  "coveredPartiallyPercentage": 0,
  "handledCompletelyCount": 27,
  "handledCompletelyPercentage": 9.3426,
  "handledPartiallyCount": 0,
  "handledPartiallyPercentage": 0,
  "unhandledCount": 262,
  "unhandledPercentage": 90.6574,
  "uncoveredCount": 262,
  "uncoveredPercentage": 90.6574,
  "justifiedCompletelyCount": 22,
  "justifiedCompletelyPercentage": 2.6574,
  "justifiedPartiallyCount": 1,
  "justifiedPartiallyPercentage": 0.6574,
  "totalCount": 289
}

```

DownCast goal coverage information.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|coverageGoal|string|false|none|Name of the goal|
|coveredCompletelyCount|integer(int64)|false|none|Coverage complete count|
|coveredCompletelyPercentage|number|false|none|Coverage complete percentage|
|coveredPartiallyCount|integer(int64)|false|none|Coverage partial count|
|coveredPartiallyPercentage|number|false|none|Coverage partial percentage|
|handledCompletelyCount|integer(int64)|false|none|Handled complete count|
|handledCompletelyPercentage|number|false|none|Handled complete percentage|
|handledPartiallyCount|integer(int64)|false|none|Handled partial count|
|handledPartiallyPercentage|number|false|none|Handled partial percentage|
|unhandledCount|integer(int64)|false|none|Unhandled count|
|unhandledPercentage|number|false|none|Unhandled percentage|
|uncoveredCount|integer(int64)|false|none|Uncovered count|
|uncoveredPercentage|number|false|none|Uncovered percentage|
|justifiedCompletelyCount|integer(int64)|false|none|Covered completely (justified) count|
|justifiedCompletelyPercentage|number|false|none|Covered completely (justified) percentage|
|justifiedPartiallyCount|integer(int64)|false|none|Covered partially (justified) count|
|justifiedPartiallyPercentage|number|false|none|Covered partially (justified) percentage|
|totalCount|integer(int64)|false|none|Total count|

<h2 id="tocS_CodeCoveragePropertySummary">CodeCoveragePropertySummary</h2>
<!-- backwards compatibility -->
<a id="schemacodecoveragepropertysummary"></a>
<a id="schema_CodeCoveragePropertySummary"></a>
<a id="tocScodecoveragepropertysummary"></a>
<a id="tocscodecoveragepropertysummary"></a>

```json
{
  "coverageGoal": "<Goal Type>",
  "coveredCount": 27,
  "coveredPercentage": 9.3426,
  "unreachableInfiniteCount": 0,
  "unreachableInfinitePercentage": 0,
  "unreachableNCount": 0,
  "unreachableNPercentage": 0,
  "unreachableInfiniteJustifiedCount": 1,
  "unreachableInfiniteJustifiedPercentage": 0.559,
  "unreachableNJustifiedCount": 1,
  "unreachableNJustifiedPercentage": 0.559,
  "unknownJustifiedCount": 262,
  "unknownJustifiedPercentage": 0.6574,
  "unknownCount": 262,
  "unknownPercentage": 90.6574,
  "handledCount": 27,
  "handledPercentage": 9.3426,
  "inconsistentCount": 0,
  "inconsistentPercentage": 0,
  "unreachableCount": 0,
  "unreachablePercentage": 0,
  "totalCount": 289,
  "comment": "My comment."
}

```

DownCast property coverage information.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|coverageGoal|string|false|none|Name of the goal|
|coveredCount|integer(int64)|false|none|Covered count|
|coveredPercentage|number|false|none|Covered percentage|
|unreachableInfiniteCount|integer(int64)|false|none|Unreachable Infinite count|
|unreachableInfinitePercentage|number|false|none|Unreachable Infinite percentage|
|unreachableNCount|integer(int64)|false|none|Unreachable N count|
|unreachableNPercentage|number|false|none|Unreachable N percentage|
|unreachableInfiniteJustifiedCount|integer(int64)|false|none|Unreachable Infinite (justified) count|
|unreachableInfiniteJustifiedPercentage|number|false|none|Unreachable Infinite (justified) percentage|
|unreachableNJustifiedCount|integer(int64)|false|none|Unreachable N (justified) count|
|unreachableNJustifiedPercentage|number|false|none|Unreachable N (justified) percentage|
|unknownJustifiedCount|integer(int64)|false|none|Unknown (justified) count|
|unknownJustifiedPercentage|number|false|none|Unknown (justified) percentage|
|unknownCount|integer(int64)|false|none|Unknown count|
|unknownPercentage|number|false|none|Unknown percentage|
|handledCount|integer(int64)|false|none|Handled count|
|handledPercentage|number|false|none|Handled percentage|
|inconsistentCount|integer(int64)|false|none|Inconsistent count|
|inconsistentPercentage|number|false|none|Inconsistent percentage|
|unreachableCount|integer(int64)|false|none|Unreachable count|
|unreachablePercentage|number|false|none|Unreachable percentage|
|totalCount|integer(int64)|false|none|Total count|
|comment|string|false|none|The comment|

<h2 id="tocS_CodeCoverageResult">CodeCoverageResult</h2>
<!-- backwards compatibility -->
<a id="schemacodecoverageresult"></a>
<a id="schema_CodeCoverageResult"></a>
<a id="tocScodecoverageresult"></a>
<a id="tocscodecoverageresult"></a>

```json
{
  "CDCCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "CDCPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "ConditionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "ConditionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DecisionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DecisionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "FunctionCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "FunctionPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "FunctionCallCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "FunctionCallPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "MCDCCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "MCDCPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "RelationalOperatorCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "RelationalOperatorPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "StatementCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "StatementPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "SwitchCaseCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "SwitchCasePropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DivisionByZeroCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DivisionByZeroPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "DownCastCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCompletelyCount": 27,
    "coveredCompletelyPercentage": 9.3426,
    "coveredPartiallyCount": 0,
    "coveredPartiallyPercentage": 0,
    "handledCompletelyCount": 27,
    "handledCompletelyPercentage": 9.3426,
    "handledPartiallyCount": 0,
    "handledPartiallyPercentage": 0,
    "unhandledCount": 262,
    "unhandledPercentage": 90.6574,
    "uncoveredCount": 262,
    "uncoveredPercentage": 90.6574,
    "justifiedCompletelyCount": 22,
    "justifiedCompletelyPercentage": 2.6574,
    "justifiedPartiallyCount": 1,
    "justifiedPartiallyPercentage": 0.6574,
    "totalCount": 289
  },
  "DownCastPropertyCoverage": {
    "coverageGoal": "<Goal Type>",
    "coveredCount": 27,
    "coveredPercentage": 9.3426,
    "unreachableInfiniteCount": 0,
    "unreachableInfinitePercentage": 0,
    "unreachableNCount": 0,
    "unreachableNPercentage": 0,
    "unreachableInfiniteJustifiedCount": 1,
    "unreachableInfiniteJustifiedPercentage": 0.559,
    "unreachableNJustifiedCount": 1,
    "unreachableNJustifiedPercentage": 0.559,
    "unknownJustifiedCount": 262,
    "unknownJustifiedPercentage": 0.6574,
    "unknownCount": 262,
    "unknownPercentage": 90.6574,
    "handledCount": 27,
    "handledPercentage": 9.3426,
    "inconsistentCount": 0,
    "inconsistentPercentage": 0,
    "unreachableCount": 0,
    "unreachablePercentage": 0,
    "totalCount": 289,
    "comment": "My comment."
  },
  "codeCoverageComment": "My code coverage overview comment.",
  "robustnessCoverageComment": "My robustness checks overview comment."
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|CDCCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|CDC goal coverage information.|
|CDCPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|CDC property coverage information.|
|ConditionCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|Condition goal coverage information.|
|ConditionPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|Condition property coverage information.|
|DecisionCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|Decision goal coverage information.|
|DecisionPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|Decision property coverage information.|
|FunctionCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|Function goal coverage information.|
|FunctionPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|Function property coverage information.|
|FunctionCallCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|Function call goal coverage information.|
|FunctionCallPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|Function call property coverage information.|
|MCDCCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|MCDC goal coverage information.|
|MCDCPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|MCDC property coverage information.|
|RelationalOperatorCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|Relational operation goal coverage information.|
|RelationalOperatorPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|Relational operation property coverage information.|
|StatementCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|Statement goal coverage information.|
|StatementPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|Statement property coverage information.|
|SwitchCaseCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|Switch Case goal coverage information.|
|SwitchCasePropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|Switch Case property coverage information.|
|DivisionByZeroCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|Division By Zero goal coverage information.|
|DivisionByZeroPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|Division By Zero property coverage information.|
|DownCastCoverage|[CodeCoverageGoalSummary](#schemacodecoveragegoalsummary)|false|none|DownCast goal coverage information.|
|DownCastPropertyCoverage|[CodeCoveragePropertySummary](#schemacodecoveragepropertysummary)|false|none|DownCast property coverage information.|
|codeCoverageComment|string|false|none|The code coverage overview comment.|
|robustnessCoverageComment|string|false|none|The robustness coverage overview comment.|

<h2 id="tocS_GoalComment">GoalComment</h2>
<!-- backwards compatibility -->
<a id="schemagoalcomment"></a>
<a id="schema_GoalComment"></a>
<a id="tocSgoalcomment"></a>
<a id="tocsgoalcomment"></a>

```json
{
  "pll": "F:0",
  "comment": "MyComment"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pll|string|true|none|The PLL of the code coverage or robustness goal for which to set the comment.|
|comment|string|true|none|The comment to set on the goal with the given PLL.|

<h2 id="tocS_CodeCoverageJustify">CodeCoverageJustify</h2>
<!-- backwards compatibility -->
<a id="schemacodecoveragejustify"></a>
<a id="schema_CodeCoverageJustify"></a>
<a id="tocScodecoveragejustify"></a>
<a id="tocscodecoveragejustify"></a>

```json
{
  "justified": true,
  "plls": [
    "2fa"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|justified|boolean|false|none|The desired state of justify for the supplied goals.|
|plls|[string]|false|none|none|

<h2 id="tocS_OverviewComment">OverviewComment</h2>
<!-- backwards compatibility -->
<a id="schemaoverviewcomment"></a>
<a id="schema_OverviewComment"></a>
<a id="tocSoverviewcomment"></a>
<a id="tocsoverviewcomment"></a>

```json
{
  "type": "CC_STAT",
  "comment": "myComment"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|true|none|The type of overview for which to set the comment. Possible values for code coverage goals: CC_STAT(Code Coverage Statistics), STM(Statement), D(Decision/Branch), C(Condition), MCDC(C/DC and MC/DC), F(Function), FC(Function Call). SC(Switch-Case), RO(Relational Operator), Possible values for robustness check goals are: RC_STAT(Robustness Check Statistics) ,DZ(Division by Zero), CA(Downcast). Can also specify multiple options.|
|comment|string|true|none|The comment to set for the overview type.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|CC_STAT|
|type|STM|
|type|D|
|type|C|
|type|MCDC|
|type|F|
|type|FC|
|type|SC|
|type|RO|
|type|RC_STAT|
|type|DZ|
|type|CA|

<h2 id="tocS_MessageMarker">MessageMarker</h2>
<!-- backwards compatibility -->
<a id="schemamessagemarker"></a>
<a id="schema_MessageMarker"></a>
<a id="tocSmessagemarker"></a>
<a id="tocsmessagemarker"></a>

```json
{
  "date": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date|string|false|read-only|The date when the marker was set.|

<h2 id="tocS_Message">Message</h2>
<!-- backwards compatibility -->
<a id="schemamessage"></a>
<a id="schema_Message"></a>
<a id="tocSmessage"></a>
<a id="tocsmessage"></a>

```json
{
  "uid": "yak7s7",
  "date": "01-Jan-2020 12:00:00",
  "message": "This is a message. ",
  "hint": "This is a hint.",
  "severity": "INFO"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|date|string|false|read-only|The creation-date of the message.|
|message|string|true|none|The message itself.|
|hint|string|false|none|An additional hint.|
|severity|string|true|none|The severity of the message.|

#### Enumerated Values

|Property|Value|
|---|---|
|severity|INFO|
|severity|WARNING|
|severity|ERROR|
|severity|CRITICAL|

<h2 id="tocS_Preference">Preference</h2>
<!-- backwards compatibility -->
<a id="schemapreference"></a>
<a id="schema_Preference"></a>
<a id="tocSpreference"></a>
<a id="tocspreference"></a>

```json
{
  "preferenceName": "ARCHITECTURE_DEFAULT_VIEW",
  "preferenceValue": "C-Code"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|preferenceName|string|true|none|The name of the preference.|
|preferenceValue|string|true|none|The value of the preference.|

<h2 id="tocS_PreferenceImportResult">PreferenceImportResult</h2>
<!-- backwards compatibility -->
<a id="schemapreferenceimportresult"></a>
<a id="schema_PreferenceImportResult"></a>
<a id="tocSpreferenceimportresult"></a>
<a id="tocspreferenceimportresult"></a>

```json
{
  "messages": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|messages|[string]|false|none|none|

<h2 id="tocS_Profile">Profile</h2>
<!-- backwards compatibility -->
<a id="schemaprofile"></a>
<a id="schema_Profile"></a>
<a id="tocSprofile"></a>
<a id="tocsprofile"></a>

```json
{
  "uid": "yak7s7",
  "metadata": {
    "Profile Creator": "developer",
    "Profile Creation Date": "14-Sep-2020 14:01:43",
    "Profile Modifier": "",
    "Profile Modification Date": "",
    "Profile Creation Tool Version": "2.8p0"
  },
  "profilePath": {
    "path": "C:/RestProfiles/test.epp"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|metadata|object|true|none|The metadata containing all relevant info about the profile.|
|» **additionalProperties**|string|false|none|The metadata containing all relevant info about the profile.|
|profilePath|[ProfilePath](#schemaprofilepath)|false|none|none|

<h2 id="tocS_ProfilePath">ProfilePath</h2>
<!-- backwards compatibility -->
<a id="schemaprofilepath"></a>
<a id="schema_ProfilePath"></a>
<a id="tocSprofilepath"></a>
<a id="tocsprofilepath"></a>

```json
{
  "path": "C:/RestProfiles/test.epp"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|path|string|false|none|The location where the profile is stored.|

<h2 id="tocS_LongRunningResponse">LongRunningResponse</h2>
<!-- backwards compatibility -->
<a id="schemalongrunningresponse"></a>
<a id="schema_LongRunningResponse"></a>
<a id="tocSlongrunningresponse"></a>
<a id="tocslongrunningresponse"></a>

```json
{
  "message": "string",
  "progress": 0,
  "result": {}
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|false|none|none|
|progress|integer(int32)|false|none|none|
|result|object|false|none|none|

<h2 id="tocS_ReportExportInfo">ReportExportInfo</h2>
<!-- backwards compatibility -->
<a id="schemareportexportinfo"></a>
<a id="schema_ReportExportInfo"></a>
<a id="tocSreportexportinfo"></a>
<a id="tocsreportexportinfo"></a>

```json
{
  "exportPath": "C:/Program Files/BTC/reports",
  "newName": "New Report"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|exportPath|string|true|none|Path to export report|
|newName|string|false|none|(Optional) New report name.|

<h2 id="tocS_MatlabScriptOutput">MatlabScriptOutput</h2>
<!-- backwards compatibility -->
<a id="schemamatlabscriptoutput"></a>
<a id="schema_MatlabScriptOutput"></a>
<a id="tocSmatlabscriptoutput"></a>
<a id="tocsmatlabscriptoutput"></a>

```json
{
  "outArgs": [
    true,
    1,
    1.2,
    "myString",
    [
      false,
      2
    ],
    {
      "field1": 3,
      "field2": [
        4,
        "myString"
      ],
      "field3": {
        "childField": 5
      }
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|outArgs|[object]|false|none|Output objects of the MATLAB script. The objects returned from the script must be primitive types, cell arrays or structures.|

<h2 id="tocS_MatlabScriptInput">MatlabScriptInput</h2>
<!-- backwards compatibility -->
<a id="schemamatlabscriptinput"></a>
<a id="schema_MatlabScriptInput"></a>
<a id="tocSmatlabscriptinput"></a>
<a id="tocsmatlabscriptinput"></a>

```json
{
  "scriptName": "my_script",
  "outArgs": 3,
  "inArgs": [
    true,
    1,
    1.2,
    "myString",
    [
      false,
      2
    ],
    {
      "field1": 3,
      "field2": [
        4,
        "myString"
      ],
      "field3": {
        "childField": 5
      }
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scriptName|string|true|none|MATLAB script name.|
|outArgs|integer(int32)|true|none|Number of output arguments to return. Exception will be thrown if the given m-script returns less arguments.|
|inArgs|[object]|true|none|Parameters of the MATLAB script. The order in the list can be important, dependent of the executed m-script. The parameters will be received in the MATLAB script as follows: primitive types will be converted into their MATLAB equivalents, JSON arrays will be converted into cell arrays, JSON objects will be converted into MATLAB structures.|

<h2 id="tocS_ModelCoverageReportInfo">ModelCoverageReportInfo</h2>
<!-- backwards compatibility -->
<a id="schemamodelcoveragereportinfo"></a>
<a id="schema_ModelCoverageReportInfo"></a>
<a id="tocSmodelcoveragereportinfo"></a>
<a id="tocsmodelcoveragereportinfo"></a>

```json
{
  "type": "B2B",
  "simulationKind": "SL MIL",
  "useShortCircuitLogic": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|true|none|Specifies the testing use-case for which the model coverage report should be created.<br>Must be 'B2B' or 'RBT' for Back-to-back testing or Requirement based test, respectively.|
|simulationKind|string|true|none|Specifies the simulation mode: 'SL MIL' or 'TL MIL'|
|useShortCircuitLogic|boolean|false|none|Specifies if short circuit logic should be used for Simulink blocks. <br>The paramter is optional. If not provided, the current setting from EP is used.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|RBT|
|type|B2B|

<h2 id="tocS_ModelCoverageReportOnFoldersInfo">ModelCoverageReportOnFoldersInfo</h2>
<!-- backwards compatibility -->
<a id="schemamodelcoveragereportonfoldersinfo"></a>
<a id="schema_ModelCoverageReportOnFoldersInfo"></a>
<a id="tocSmodelcoveragereportonfoldersinfo"></a>
<a id="tocsmodelcoveragereportonfoldersinfo"></a>

```json
{
  "type": "B2B",
  "simulationKind": "SL MIL",
  "folderUIDs": "21L",
  "useShortCircuitLogic": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|true|none|Specifies the testing use-case for which the model coverage report should be created.<br>Must be 'B2B' or 'RBT' for Back-to-back testing or Requirement based test, respectively.|
|simulationKind|string|true|none|Specifies the simulation mode: 'SL MIL' or 'TL MIL'|
|folderUIDs|[string]|true|none|The comma separated list of folder UIDs for which the model coverage report shall be created.|
|useShortCircuitLogic|boolean|false|none|Specifies if short circuit logic should be used for Simulink blocks. <br>The paramter is optional. If not provided, the current setting from EP is used.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|RBT|
|type|B2B|

<h2 id="tocS_EnvironmentalAssumption">EnvironmentalAssumption</h2>
<!-- backwards compatibility -->
<a id="schemaenvironmentalassumption"></a>
<a id="schema_EnvironmentalAssumption"></a>
<a id="tocSenvironmentalassumption"></a>
<a id="tocsenvironmentalassumption"></a>

```json
{
  "uid": "yak7s7",
  "name": "EA_FR1",
  "description": "Environmental assumption description",
  "scopeUID": "u378",
  "draft": "false",
  "errors": "There is an empty place in the Universal Pattern."
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|name|string|true|none|The name of the environmental assumption.|
|description|string|true|none|The description of the environmental assumption.|
|scopeUID|string|true|none|The unique identifier (UID) of the scope this object belongs to.|
|draft|string|false|none|States whether or not the FormalRequirement is in Draft-Mode.|
|errors|[string]|false|none|List of errors|

<h2 id="tocS_FormalSpecification">FormalSpecification</h2>
<!-- backwards compatibility -->
<a id="schemaformalspecification"></a>
<a id="schema_FormalSpecification"></a>
<a id="tocSformalspecification"></a>
<a id="tocsformalspecification"></a>

```json
{
  "uid": "yak7s7",
  "name": "FR_1",
  "description": "Formal requirement description",
  "scopeUID": "u378",
  "draft": "false",
  "errors": "There is an empty place in the Universal Pattern."
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|name|string|true|none|The name of the formal requirement.|
|description|string|true|none|The description of the formal requirement.|
|scopeUID|string|true|none|The unique identifier (UID) of the scope this object belongs to.|
|draft|string|false|none|States whether or not the FormalRequirement is in Draft-Mode.|
|errors|[string]|false|none|List of errors|

<h2 id="tocS_SpecExport">SpecExport</h2>
<!-- backwards compatibility -->
<a id="schemaspecexport"></a>
<a id="schema_SpecExport"></a>
<a id="tocSspecexport"></a>
<a id="tocsspecexport"></a>

```json
{
  "specFile": "C:/Desktop/mySpecFile.spec",
  "archUid": "A1b",
  "formalSpecificationUids": "2yy"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specFile|string|true|none|The file name of the target SPEC file. Should have .spec extension.|
|archUid|string|false|none|The architecture UID to define the interface names. If specified, the SPEC file will use the interface and expression names based on the interfaces and signals defined in the given architecture.If not specified, the first imported architecture is used for the name space.|
|formalSpecificationUids|[string]|true|none|A list of uids of formal requirements or environmental assumptions to export. Note: The formal requirements / environmental assumptions must reside on the same scope!|

<h2 id="tocS_SpecImport">SpecImport</h2>
<!-- backwards compatibility -->
<a id="schemaspecimport"></a>
<a id="schema_SpecImport"></a>
<a id="tocSspecimport"></a>
<a id="tocsspecimport"></a>

```json
{
  "specPath": "C:/Desktop/mySpecFile.spec",
  "scopeId": "27Y",
  "isDraft": false,
  "optionParam": "EXTEND_NAME"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|specPath|string|true|none|The path of the given SPEC file. Should have .spec extension.|
|scopeId|string|false|none|The scopeId to use, when scope definition in SPEC file is invalid. This can happed for two reasons, the first is that in the SPEC file, the component(scope) name is invalid and can not be found in the opened profile, or when the given component(scope) name in the SPEC file is not unique within current profile.e.g. a TL architecture scope name is unique to the one in the generated CCode.|
|isDraft|boolean|false|none|The draft status setting for the formal requirements that will be imported. By default its value is false.|
|optionParam|string|false|none|The options of importing a SPEC file, when the artifacts already exists. If no value is provided, 'EXTEND_NAME' is used.|

#### Enumerated Values

|Property|Value|
|---|---|
|optionParam|EXTEND_NAME|
|optionParam|OVERWRITE|
|optionParam|SKIP|

<h2 id="tocS_InputRestrictionsFolderObject">InputRestrictionsFolderObject</h2>
<!-- backwards compatibility -->
<a id="schemainputrestrictionsfolderobject"></a>
<a id="schema_InputRestrictionsFolderObject"></a>
<a id="tocSinputrestrictionsfolderobject"></a>
<a id="tocsinputrestrictionsfolderobject"></a>

```json
{
  "filePath": "C:/path/to/file.xml"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|filePath|string|true|none|The file containing input restrictions.|

<h2 id="tocS_RequirementSetting">RequirementSetting</h2>
<!-- backwards compatibility -->
<a id="schemarequirementsetting"></a>
<a id="schema_RequirementSetting"></a>
<a id="tocSrequirementsetting"></a>
<a id="tocsrequirementsetting"></a>

```json
{
  "key": "projectName_attr",
  "value": "InformalRequirements"
}

```

A list with requirement settings.For EXCEL requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, excel_file_path, projectName_attr (or excel_sheet_name), excel_id_attr, excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, projectName_attr, doors_module_qualifier, doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|key|string|true|none|For EXCEL requirement kind, the following keys are mandatory: excel_file_path, projectName_attr, excel_id_attr. The optional setting keys are: excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys are mandatory: projectName_attr, doors_module_qualifier. The optional setting keys are: doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.|
|value|string|true|none|Setting value|

<h2 id="tocS_RequirementSource">RequirementSource</h2>
<!-- backwards compatibility -->
<a id="schemarequirementsource"></a>
<a id="schema_RequirementSource"></a>
<a id="tocSrequirementsource"></a>
<a id="tocsrequirementsource"></a>

```json
"Object containing info about RequirementSource"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|kind|string|true|none|The kind of this requirement source. The kind identifies this source to be from a specific requirement management tool.|
|settings|[[RequirementSetting](#schemarequirementsetting)]|true|none|[A list with requirement settings.For EXCEL requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, excel_file_path, projectName_attr (or excel_sheet_name), excel_id_attr, excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, projectName_attr, doors_module_qualifier, doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.]|
|definedAdditionalAttributes|[string]|false|none|none|
|externalUUID|string|true|none|The unique ID identifying the external requirement source.|
|name|string|true|none|The requirement source name.|
|uid|string|true|none|The universally unique identifier of this requirement source.|

<h2 id="tocS_RequirementImportRestConfig">RequirementImportRestConfig</h2>
<!-- backwards compatibility -->
<a id="schemarequirementimportrestconfig"></a>
<a id="schema_RequirementImportRestConfig"></a>
<a id="tocSrequirementimportrestconfig"></a>
<a id="tocsrequirementimportrestconfig"></a>

```json
{
  "kind": "One of EXCEL or DOORS",
  "nameAttribute": "REQ_ID",
  "descriptionAttribute": "Description",
  "additionalAttributes": [
    "string"
  ],
  "settings": [
    {
      "key": "projectName_attr",
      "value": "InformalRequirements"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|kind|string|true|none|The kind of imported requirements. Allowed types: EXCEL or DOORS.|
|nameAttribute|string|false|none|The name of imported requirements. Required for DOORS and EXCEL import.|
|descriptionAttribute|string|false|none|The description of imported requirements. Required for DOORS and EXCEL import.|
|additionalAttributes|[string]|false|none|none|
|settings|[[RequirementSetting](#schemarequirementsetting)]|true|none|[A list with requirement settings.For EXCEL requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, excel_file_path, projectName_attr (or excel_sheet_name), excel_id_attr, excel_start_row, excel_parent_id.For DOORS requirement kind, the following keys can be: name_attr_value, desc_attr_value, additional_attr, modification_date, projectName_attr, doors_module_qualifier, doors_baseline_major, doors_baseline_minor, doors_baseline_suffix.]|

#### Enumerated Values

|Property|Value|
|---|---|
|kind|EXCEL|
|kind|DOORS|

<h2 id="tocS_Requirement">Requirement</h2>
<!-- backwards compatibility -->
<a id="schemarequirement"></a>
<a id="schema_Requirement"></a>
<a id="tocSrequirement"></a>
<a id="tocsrequirement"></a>

```json
{
  "uid": "27T",
  "identifier": "1",
  "isRemoved": true,
  "additionalAttributes": {
    "property1": "string",
    "property2": "string"
  },
  "scopeId": "27T",
  "description": "Requirement description.",
  "name": "REQ_PW_1_1",
  "dateOfLastUpdate": "01-Jan-2020 12:00:00",
  "requirementSource": "Object containing info about RequirementSource"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|true|none|The universally unique identifier.|
|identifier|string|true|none|The requirement identifier (e.g. a chapter number within DOORS).|
|isRemoved|boolean|false|none|Value meaning whether this requirement has been removed within the requirement management tool.|
|additionalAttributes|object|false|none|Map containing all additional attributes.|
|» **additionalProperties**|string|false|none|Map containing all additional attributes.|
|scopeId|string|true|none|The scope id this requirement is directly linked to.|
|description|string|true|none|The requirement description.|
|name|string|true|none|The requirement name.|
|dateOfLastUpdate|string|true|none|The requirement last update date.|
|requirementSource|[RequirementSource](#schemarequirementsource)|true|none|none|

<h2 id="tocS_ExecutionConfigs">ExecutionConfigs</h2>
<!-- backwards compatibility -->
<a id="schemaexecutionconfigs"></a>
<a id="schema_ExecutionConfigs"></a>
<a id="tocSexecutionconfigs"></a>
<a id="tocsexecutionconfigs"></a>

```json
{
  "execConfigNames": "SIL"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|execConfigNames|[string]|false|none|List of the available execution kinds|

<h2 id="tocS_RestExecutionRecordExportInfo">RestExecutionRecordExportInfo</h2>
<!-- backwards compatibility -->
<a id="schemarestexecutionrecordexportinfo"></a>
<a id="schema_RestExecutionRecordExportInfo"></a>
<a id="tocSrestexecutionrecordexportinfo"></a>
<a id="tocsrestexecutionrecordexportinfo"></a>

```json
{
  "UIDs": "2UPb",
  "exportDirectory": "C:/RestProfiles/VectorExport",
  "exportFormat": "MDF"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UIDs|[string]|true|none|List with the UIDs of the elements which will be exported|
|exportDirectory|string|true|none|Directory where to export the elements|
|exportFormat|string|false|none|The format of the exported execution records. (Default value: "MDF").|

#### Enumerated Values

|Property|Value|
|---|---|
|exportFormat|MDF|
|exportFormat|EXCEL|

<h2 id="tocS_ExecutionRecord">ExecutionRecord</h2>
<!-- backwards compatibility -->
<a id="schemaexecutionrecord"></a>
<a id="schema_ExecutionRecord"></a>
<a id="tocSexecutionrecord"></a>
<a id="tocsexecutionrecord"></a>

```json
{
  "uid": "yak7s7",
  "executionConfig": "SIL",
  "name": "SIL_TestCase",
  "status": "OK",
  "folderName": "SIL simulations",
  "length": 2,
  "scopeName": "power_window_controller",
  "sourceName": "TestCase"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|executionConfig|string|true|none|The execution config name|
|name|string|true|none|The execution record name|
|status|string|false|none|The status of execution record.Possible options: OK, WARNING, or ERROR.|
|folderName|string|true|none|The folder name on which this execution record can be found.|
|length|integer(int64)|true|none|The length of execution record source|
|scopeName|string|true|none|The scope name of execution record|
|sourceName|string|true|none|The name of execution record source|

#### Enumerated Values

|Property|Value|
|---|---|
|status|OK|
|status|WARNING|
|status|ERROR|

<h2 id="tocS_RestExecutionRecordImportInfo">RestExecutionRecordImportInfo</h2>
<!-- backwards compatibility -->
<a id="schemarestexecutionrecordimportinfo"></a>
<a id="schema_RestExecutionRecordImportInfo"></a>
<a id="tocSrestexecutionrecordimportinfo"></a>
<a id="tocsrestexecutionrecordimportinfo"></a>

```json
{
  "paths": [
    "C:/RestProfiles/VectorExport/executionRecord.mdf"
  ],
  "kind": "SIL",
  "folderName": "New Records",
  "folderUID": "X34",
  "referenceExternalFile": true,
  "csvDelimiter": "SEMICOLON"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|paths|[string]|true|none|none|
|kind|string|true|none|The simulation kind that was used for creating the execution records from the given files. Possible values: TL MIL, SL MIL, SIL, PIL or any external simulation kind. If the user defined folder option is not specified, the simulation kind will define the default folder where the execution records will be imported.|
|folderName|string|false|none|User defined execution records folder name. <b color="red">If used, folderUID can not be used at the same time. </b>|
|folderUID|string|false|none|Existing user defined folder uid to import records. <b color="red">If used, folderName can not be used at the same time. </b>|
|referenceExternalFile|boolean|false|none|Relevant only for MF4 and CSV import format. Whether to only reference the external file rather than importing the execution record in the profile. This would be recommended for very big execution records.Default is 'false'.|
|csvDelimiter|string|false|none|Relevant only for CSV import format. It can have one of the following values: "SEMICOLON", "COMMA", "COLON", "PIPE". Default value is "SEMICOLON".|

#### Enumerated Values

|Property|Value|
|---|---|
|csvDelimiter|SEMICOLON|
|csvDelimiter|COMMA|
|csvDelimiter|COLON|
|csvDelimiter|PIPE|

<h2 id="tocS_ExecutionRecordsMoveData">ExecutionRecordsMoveData</h2>
<!-- backwards compatibility -->
<a id="schemaexecutionrecordsmovedata"></a>
<a id="schema_ExecutionRecordsMoveData"></a>
<a id="tocSexecutionrecordsmovedata"></a>
<a id="tocsexecutionrecordsmovedata"></a>

```json
{
  "UIDs": "2UPb"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UIDs|[string]|true|none|UIDs of execution records to be moved.|

<h2 id="tocS_TestCaseSimulationResult">TestCaseSimulationResult</h2>
<!-- backwards compatibility -->
<a id="schematestcasesimulationresult"></a>
<a id="schema_TestCaseSimulationResult"></a>
<a id="tocStestcasesimulationresult"></a>
<a id="tocstestcasesimulationresult"></a>

```json
"..."

```

The detailed test results mapped by execution kind

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|execRecordUIDs|[string]|false|none|The execution records UIDs.|
|execConfig|string|false|none|The execution configuration.|

<h2 id="tocS_TestCaseSimulationResultMap">TestCaseSimulationResultMap</h2>
<!-- backwards compatibility -->
<a id="schematestcasesimulationresultmap"></a>
<a id="schema_TestCaseSimulationResultMap"></a>
<a id="tocStestcasesimulationresultmap"></a>
<a id="tocstestcasesimulationresultmap"></a>

```json
{
  "testResults": "..."
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|testResults|object|false|none|The detailed test results mapped by execution kind|
|» **additionalProperties**|[TestCaseSimulationResult](#schematestcasesimulationresult)|false|none|The detailed test results mapped by execution kind|

<h2 id="tocS_TestCaseSimulationParams">TestCaseSimulationParams</h2>
<!-- backwards compatibility -->
<a id="schematestcasesimulationparams"></a>
<a id="schema_TestCaseSimulationParams"></a>
<a id="tocStestcasesimulationparams"></a>
<a id="tocstestcasesimulationparams"></a>

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|execConfigNames|[string]|true|none|List of execution kinds (example: SIL, TL MIL, SL MIL, etc.) for which to simulate. Not case-sensitive.|
|forceExecute|boolean|false|none|Specify (optional) if the simulation should be forced (all previous results will be discarded). Default is 'false'.|

<h2 id="tocS_TestCaseSimulationOnListParams">TestCaseSimulationOnListParams</h2>
<!-- backwards compatibility -->
<a id="schematestcasesimulationonlistparams"></a>
<a id="schema_TestCaseSimulationOnListParams"></a>
<a id="tocStestcasesimulationonlistparams"></a>
<a id="tocstestcasesimulationonlistparams"></a>

```json
{
  "execConfigNames": "SIL",
  "forceExecute": false,
  "UIDs": "2UPb"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|execConfigNames|[string]|true|none|List of execution kinds (example: SIL, TL MIL, SL MIL, etc.) for which to simulate. Not case-sensitive.|
|forceExecute|boolean|false|none|Specify (optional) if the simulation should be forced (all previous results will be discarded). Default is 'false'.|
|UIDs|[string]|true|none|List with unique identifiers of the objects.|

<h2 id="tocS_DomainChecksRangesInput">DomainChecksRangesInput</h2>
<!-- backwards compatibility -->
<a id="schemadomainchecksrangesinput"></a>
<a id="schema_DomainChecksRangesInput"></a>
<a id="tocSdomainchecksrangesinput"></a>
<a id="tocsdomainchecksrangesinput"></a>

```json
{
  "scopeUid": "27c",
  "signalUids": [
    "222"
  ],
  "applyBoundaryChecks": false,
  "applyInvalidRangesChecks": false,
  "percentage": 25
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scopeUid|string|true|none|The scope for which to create the domain checks ranges.|
|signalUids|[string]|false|none|none|
|applyBoundaryChecks|boolean|false|none|Used for applying the boundary checks when creating the range.Can only be used for applying boundary checks on a defined range, so it must be used only together with one of the other options (either apply invalid ranges checks or partition ranges). <br>Default is 'false'|
|applyInvalidRangesChecks|boolean|false|none|Used for applying the invalid ranges checks when creating the range. <br>Default is 'false'|
|percentage|integer(int32)|false|none|Percentage used for partioning the range interval when creating the range. <br>If no value is provided the domain check ranges will not be partitioned.|

<h2 id="tocS_DomainChecksIOInfo">DomainChecksIOInfo</h2>
<!-- backwards compatibility -->
<a id="schemadomainchecksioinfo"></a>
<a id="schema_DomainChecksIOInfo"></a>
<a id="tocSdomainchecksioinfo"></a>
<a id="tocsdomainchecksioinfo"></a>

```json
{
  "scopeUid": "26u",
  "filePath": "C:/DomainChecks/goals.xml"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scopeUid|string|true|none|The scopeUid for which to export/import domain check ranges.|
|filePath|string|true|none|The file path used for exporting/importing domain check ranges. The directory path specified in the filePath must already exist.|

<h2 id="tocS_DomainCheckGoal">DomainCheckGoal</h2>
<!-- backwards compatibility -->
<a id="schemadomaincheckgoal"></a>
<a id="schema_DomainCheckGoal"></a>
<a id="tocSdomaincheckgoal"></a>
<a id="tocsdomaincheckgoal"></a>

```json
{
  "name": "Sa1_driver_down",
  "kind": "INPUT",
  "pll": "IDCG:1:0",
  "range": "[0 42]",
  "goalType": "VALID",
  "goalStatus": "UNREACHABLE",
  "comment": "The goal is unreachable because of... ",
  "coveringVectors": [
    "testCase"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|read-only|The name of the signal for which domain check goals where created.|
|kind|string|false|read-only|The kind of the signal for which domain check goals where created.|
|pll|string|false|none|PLL string of the domain check goal.|
|range|string|false|none|The range of the domain check goal.|
|goalType|string|false|none|The type of the domain check goal.|
|goalStatus|string|false|none|The status of the domain check goal.|
|comment|string|false|none|The comment of the domain check goal.|
|coveringVectors|[string]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|kind|INPUT|
|kind|OUTPUT|
|kind|LOCAL|
|kind|PARAMETER|
|goalType|VALID|
|goalType|INVALID|
|goalStatus|COVERED|
|goalStatus|UNREACHABLE|
|goalStatus|UNKNOWN|
|goalStatus|ERROR|
|goalStatus|NOT_DEFINED|

<h2 id="tocS_DomainChecksResults">DomainChecksResults</h2>
<!-- backwards compatibility -->
<a id="schemadomainchecksresults"></a>
<a id="schema_DomainChecksResults"></a>
<a id="tocSdomainchecksresults"></a>
<a id="tocsdomainchecksresults"></a>

```json
{
  "totalCountValid": "100",
  "coveredCountValid": "100",
  "unreachableCountValid": "0",
  "errorCountValid": "0",
  "handledCountValid": "100",
  "unhandledCountValid": "0",
  "coveredPercValid": "100",
  "unreachablePercValid": "0",
  "errorPercValid": "0",
  "handledPercValid": "100",
  "unhandledPercValid": "0",
  "totalCountInvalid": "100",
  "coveredCountInvalid": "0",
  "unreachableCountInvalid": "100",
  "errorCountInvalid": "0",
  "handledCountInvalid": "100",
  "unhandledCountInvalid": "0",
  "coveredPercInvalid": "0",
  "unreachablePercInvalid": "100",
  "errorPercInvalid": "0",
  "handledPercInvalid": "100",
  "unhandledPercInvalid": "0"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|totalCountValid|string|false|read-only|The total number of valid range goals.|
|coveredCountValid|string|false|read-only|The number of covered valid range goals.|
|unreachableCountValid|string|false|read-only|The number of unreachable valid range goals.|
|errorCountValid|string|false|read-only|The number of errorneous valid range goals.|
|handledCountValid|string|false|read-only|The number of handled valid range goals.|
|unhandledCountValid|string|false|read-only|The number of unhandled  valid range goals.|
|coveredPercValid|string|false|read-only|The covered percentage for valid range goals.|
|unreachablePercValid|string|false|read-only|The unreachable percentage for valid range goals.|
|errorPercValid|string|false|read-only|The error percentage for valid range goals.|
|handledPercValid|string|false|read-only|The handled percentage for valid range goals.|
|unhandledPercValid|string|false|read-only|The unhandled percentage for valid range goals.|
|totalCountInvalid|string|false|read-only|The total number of invalid range goals.|
|coveredCountInvalid|string|false|read-only|The number of covered invalid range goals.|
|unreachableCountInvalid|string|false|read-only|The number of unreachable invalid range goals.|
|errorCountInvalid|string|false|read-only|The number of errorneous invalid range goals.|
|handledCountInvalid|string|false|read-only|The number of handled invalid range goals.|
|unhandledCountInvalid|string|false|read-only|The number of unhandled invalid range goals.|
|coveredPercInvalid|string|false|read-only|The covered percentage for invalid range goals.|
|unreachablePercInvalid|string|false|read-only|The unreachable percentage for invalid range goals.|
|errorPercInvalid|string|false|read-only|The error percentage for invalid range goals.|
|handledPercInvalid|string|false|read-only|The handled percentage for invalid range goals.|
|unhandledPercInvalid|string|false|read-only|The unhandled percentage for invalid range goals.|

<h2 id="tocS_DomainCheckGoalComment">DomainCheckGoalComment</h2>
<!-- backwards compatibility -->
<a id="schemadomaincheckgoalcomment"></a>
<a id="schema_DomainCheckGoalComment"></a>
<a id="tocSdomaincheckgoalcomment"></a>
<a id="tocsdomaincheckgoalcomment"></a>

```json
{
  "pll": "VDCG:2:0",
  "comment": "MyComment"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pll|string|true|none|The PLL of the domain check goal for which to set the comment.|
|comment|string|true|none|The comment to set on the domain check goal with the given PLL.|

<h2 id="tocS_Folder">Folder</h2>
<!-- backwards compatibility -->
<a id="schemafolder"></a>
<a id="schema_Folder"></a>
<a id="tocSfolder"></a>
<a id="tocsfolder"></a>

```json
{
  "uid": "yak7s7",
  "name": "Test Cases",
  "kind": "RB_TEST_CASE",
  "isDefault": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|uid|string|false|read-only|The unique identifier (UID) of this object.|
|name|string|true|none|The name of the folder.|
|kind|string|true|none|The folder kind.|
|isDefault|boolean|true|none|Set to 'true' if it is a default folder.|

<h2 id="tocS_FolderTransmisionObject">FolderTransmisionObject</h2>
<!-- backwards compatibility -->
<a id="schemafoldertransmisionobject"></a>
<a id="schema_FolderTransmisionObject"></a>
<a id="tocSfoldertransmisionobject"></a>
<a id="tocsfoldertransmisionobject"></a>

```json
{
  "folderKind": "RB_TEST_CASE",
  "folderName": "My folder"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|folderKind|string|true|none|The folder kind. Possible: "RB_TEST_CASE", "EXECUTION_RECORD", "STIMULI_VECTOR"|
|folderName|string|false|none|The folder name. This parameter is optional|

