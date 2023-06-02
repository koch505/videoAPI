# apivideo.CaptionsApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](CaptionsApi.md#upload) | **POST** /videos/{videoId}/captions/{language} | Upload a caption
[**get**](CaptionsApi.md#get) | **GET** /videos/{videoId}/captions/{language} | Retrieve a caption
[**update**](CaptionsApi.md#update) | **PATCH** /videos/{videoId}/captions/{language} | Update a caption
[**delete**](CaptionsApi.md#delete) | **DELETE** /videos/{videoId}/captions/{language} | Delete a caption
[**list**](CaptionsApi.md#list) | **GET** /videos/{videoId}/captions | List video captions


# **upload**
> Caption upload(video_id, language, file)

Upload a caption

Upload a VTT file to add captions to your video. More information can be found [here](https://docs.api.video/reference/captions)

### Example
```python
# First install the api client with "pip install api.video"

import apivideo
from apivideo.api import captions_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.caption import Caption
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = captions_api.CaptionsApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Prklg" # str | The unique identifier for the video you want to add a caption to.
    language = "en" # str | A valid BCP 47 language representation.
    file = open('/path/to/file', 'rb') # file_type | The video text track (VTT) you want to upload.

    # example passing only required values which don't have defaults set
    try:
        # Upload a caption
        api_response = api_instance.upload(video_id, language, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling CaptionsApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want to add a caption to. |
 **language** | **str**| A valid BCP 47 language representation. |
 **file** | **file_type**| The video text track (VTT) you want to upload. |

### Return type

[**Caption**](Caption.md)


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Caption get(video_id, language)

Retrieve a caption

Retrieve a caption for a video in a specific language. If the language is available, the caption is returned. Otherwise, you will get a error indicating the caption was not found.

Tutorials that use the [captions endpoint](https://api.video/blog/endpoints/captions).

### Example
```python
# First install the api client with "pip install api.video"

import apivideo
from apivideo.api import captions_api
from apivideo.model.not_found import NotFound
from apivideo.model.caption import Caption
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = captions_api.CaptionsApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Prklg" # str | The unique identifier for the video you want captions for.
    language = "en" # str | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation

    # example passing only required values which don't have defaults set
    try:
        # Show a caption
        api_response = api_instance.get(video_id, language)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling CaptionsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want captions for. |
 **language** | **str**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation |

### Return type

[**Caption**](Caption.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Caption update(video_id, language, captions_update_payload)

Update a caption

To have the captions on automatically, use this method to set default: true.

### Example
```python
# First install the api client with "pip install api.video"

import apivideo
from apivideo.api import captions_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.captions_update_payload import CaptionsUpdatePayload
from apivideo.model.not_found import NotFound
from apivideo.model.caption import Caption
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = captions_api.CaptionsApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Prklg" # str | The unique identifier for the video you want to have automatic captions for.
    language = "en" # str | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    captions_update_payload = CaptionsUpdatePayload(
        default=True,
    ) # CaptionsUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update caption
        api_response = api_instance.update(video_id, language, captions_update_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling CaptionsApi->update: %s\
" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want to have automatic captions for. |
 **language** | **str**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. |
 **captions_update_payload** | [**CaptionsUpdatePayload**](CaptionsUpdatePayload.md)|  |

### Return type

[**Caption**](Caption.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(video_id, language)

Delete a caption

Delete a caption in a specific language by by video id.

### Example
```python
# First install the api client with "pip install api.video"

import apivideo
from apivideo.api import captions_api
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = captions_api.CaptionsApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Prklgc" # str | The unique identifier for the video you want to delete a caption from.
    language = "en" # str | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.

    # example passing only required values which don't have defaults set
    try:
        # Delete a caption
        api_instance.delete(video_id, language)
    except apivideo.ApiException as e:
        print("Exception when calling CaptionsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want to delete a caption from. |
 **language** | **str**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. |

### Return type

void (empty response body)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> CaptionsListResponse list(video_id)

List video captions

Retrieve a list of available captions by video id.

### Example
```python
# First install the api client with "pip install api.video"

import apivideo
from apivideo.api import captions_api
from apivideo.model.not_found import NotFound
from apivideo.model.caption import Caption
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = captions_api.CaptionsApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Prklg" # str | The unique identifier for the video you want captions for.
    language = "en" # str | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation

    # example passing only required values which don't have defaults set
    try:
        # Show a caption
        api_response = api_instance.get(video_id, language)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling CaptionsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want to retrieve a list of captions for. |
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**CaptionsListResponse**](CaptionsListResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

