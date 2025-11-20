from typing import List, Optional

from app.schemas.device import Device


_devices: list[Device] = []
_next_id: int = 1


def list_devices() -> List[Device]:
    return list(_devices)


def create_device(name: str, type: str) -> Device:
    global _next_id
    device = Device(
        id=_next_id,
        name=name,
        type=type,
        is_muted=False,
    )
    _next_id += 1
    _devices.append(device)
    return device


def get_device(device_id: int) -> Optional[Device]:
    for device in _devices:
        if device.id == device_id:
            return device
    return None


def set_muted(device_id: int, is_muted: bool) -> Optional[Device]:
    device = get_device(device_id)
    if device is None:
        return None
    device.is_muted = is_muted
    return device
