from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualer_api_models_measurements_to_update_measurement_form_response_model import (
    MeasurementsToUpdateMeasurementFormResponseModel,
)
from ...types import Response


def _get_kwargs(
    work_item_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/service/workitems/{work_item_id}/form",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]]:
    if response.status_code == 200:
        response_200 = MeasurementsToUpdateMeasurementFormResponseModel.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]]:
    """Get Measurement Form.

    Args:
        work_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]]:
    """Get Measurement Form.

    Args:
        work_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]
    """

    return sync_detailed(
        work_item_id=work_item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]]:
    """Get Measurement Form.

    Args:
        work_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]]
    """

    kwargs = _get_kwargs(
        work_item_id=work_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    work_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]]:
    """Get Measurement Form.

    Args:
        work_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MeasurementsToUpdateMeasurementFormResponseModel]
    """

    return (
        await asyncio_detailed(
            work_item_id=work_item_id,
            client=client,
        )
    ).parsed
