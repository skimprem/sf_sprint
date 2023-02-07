# API Schema
Guide for the REST API

## Version: 

### /submitData/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

### /submitData/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this pereval. | Yes | string |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

#### PUT
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this pereval. | Yes | string |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this pereval. | Yes | string |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this pereval. | Yes | string |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |
