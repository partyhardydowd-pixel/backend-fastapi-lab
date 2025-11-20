from typing import List

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.schemas.device import Device
from app.services.device_service import (
    list_devices,
    create_device,
    get_device,
    set_muted,
)

router = APIRouter(prefix="/devices", tags=["devices"])


class DeviceCreate(BaseModel):
    name: str
    type: str  # e.g. "tv", "receiver"


@router.get("", response_model=List[Device])
def list_devices_endpoint():
    return list_devices()


@router.post("", response_model=Device, status_code=status.HTTP_201_CREATED)
def create_device_endpoint(payload: DeviceCreate):
    return create_device(name=payload.name, type=payload.type)


@router.post("/{device_id}/mute", response_model=Device)
def mute_device_endpoint(device_id: int):
    device = set_muted(device_id, True)
    if device is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Device not found",
        )
    return device


@router.post("/{device_id}/unmute", response_model=Device)
def unmute_device_endpoint(device_id: int):
    device = set_muted(device_id, False)
    if device is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Device not found",
        )
    return device
