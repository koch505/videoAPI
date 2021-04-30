# apivideo.PlayerThemesApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](PlayerThemesApi.md#delete) | **DELETE** /players/{playerId} | Delete a player
[**delete_logo**](PlayerThemesApi.md#delete_logo) | **DELETE** /players/{playerId}/logo | Delete logo
[**list**](PlayerThemesApi.md#list) | **GET** /players | List all players
[**get**](PlayerThemesApi.md#get) | **GET** /players/{playerId} | Show a player
[**update**](PlayerThemesApi.md#update) | **PATCH** /players/{playerId} | Update a player
[**create**](PlayerThemesApi.md#create) | **POST** /players | Create a player
[**upload_logo**](PlayerThemesApi.md#upload_logo) | **POST** /players/{playerId}/logo | Upload a logo


# **delete**
> delete(player_id)

Delete a player

Delete a player if you no longer need it. You can delete any player that you have the player ID for.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl45d5vFFGrfdsdsd156dGhh" # str | The unique identifier for the player you want to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a player
        api_instance.delete(player_id)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player you want to delete. |

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

# **delete_logo**
> delete_logo(player_id)

Delete logo

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl14Db6oMJRH6SRVoOwORacK" # str | The unique identifier for the player.

    # example passing only required values which don't have defaults set
    try:
        # Delete logo
        api_instance.delete_logo(player_id)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->delete_logo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player. |

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
> PlayersListResponse list()

List all players

Retrieve a list of all the players you created, as well as details about each one.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.players_list_response import PlayersListResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    sort_by = "createdAt" # str | createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ISO-8601 format. (optional)
    sort_order = "asc" # str | Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all players
        api_response = api_instance.list(sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ISO-8601 format. | [optional]
 **sort_order** | **str**| Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**PlayersListResponse**](PlayersListResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Player get(player_id)

Show a player

Use a player ID to retrieve details about the player and display it for viewers.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.not_found import NotFound
from apivideo.model.player import Player
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl45d5vFFGrfdsdsd156dGhh" # str | The unique identifier for the player you want to retrieve. 

    # example passing only required values which don't have defaults set
    try:
        # Show a player
        api_response = api_instance.get(player_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player you want to retrieve.  |

### Return type

[**Player**](Player.md)

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
> Player update(player_id, player_update_payload)

Update a player

Use a player ID to update specific details for a player. NOTE: It may take up to 10 min before the new player configuration is available from our CDN.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.player_update_payload import PlayerUpdatePayload
from apivideo.model.not_found import NotFound
from apivideo.model.player import Player
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl45d5vFFGrfdsdsd156dGhh" # str | The unique identifier for the player.
    player_update_payload = PlayerUpdatePayload(
        text="text_example",
        link="link_example",
        link_hover="link_hover_example",
        track_played="track_played_example",
        track_unplayed="track_unplayed_example",
        track_background="track_background_example",
        background_top="background_top_example",
        background_bottom="background_bottom_example",
        background_text="background_text_example",
        enable_api=True,
        enable_controls=True,
        force_autoplay=True,
        hide_title=True,
        force_loop=True,
    ) # PlayerUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update a player
        api_response = api_instance.update(player_id, player_update_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player. |
 **player_update_payload** | [**PlayerUpdatePayload**](PlayerUpdatePayload.md)|  |

### Return type

[**Player**](Player.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Player create(player_creation_payload)

Create a player

Create a player for your video, and customise it.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.player import Player
from apivideo.model.player_creation_payload import PlayerCreationPayload
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_creation_payload = PlayerCreationPayload(
        text="text_example",
        link="link_example",
        link_hover="link_hover_example",
        track_played="track_played_example",
        track_unplayed="track_unplayed_example",
        track_background="track_background_example",
        background_top="background_top_example",
        background_bottom="background_bottom_example",
        background_text="background_text_example",
        enable_api=True,
        enable_controls=True,
        force_autoplay=False,
        hide_title=False,
        force_loop=False,
    ) # PlayerCreationPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Create a player
        api_response = api_instance.create(player_creation_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_creation_payload** | [**PlayerCreationPayload**](PlayerCreationPayload.md)|  |

### Return type

[**Player**](Player.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_logo**
> Player upload_logo(player_id, file, link)

Upload a logo

The uploaded image maximum size should be 200x100 and its weight should be 200KB.  It will be scaled down to 30px height and converted to PNG to be displayed in the player.

### Example

```python
import apivideo
from apivideo.api import player_themes_api
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.player import Player
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = player_themes_api.PlayerThemesApi(api_client)
    player_id = "pl14Db6oMJRH6SRVoOwORacK" # str | The unique identifier for the player.
    file = open('/path/to/file', 'rb') # file_type | The name of the file you want to use for your logo.
    link = "path/to/my/logo/mylogo.jpg" # str | The path to the file you want to upload and use as a logo.

    # example passing only required values which don't have defaults set
    try:
        # Upload a logo
        api_response = api_instance.upload_logo(player_id, file, link)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling PlayerThemesApi->upload_logo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The unique identifier for the player. |
 **file** | **file_type**| The name of the file you want to use for your logo. |
 **link** | **str**| The path to the file you want to upload and use as a logo. |

### Return type

[**Player**](Player.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

