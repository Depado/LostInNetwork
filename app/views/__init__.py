# -*- coding: utf-8 -*-

from .main import index, login, logout
from .devices import devices, configurations_device, delete_device, inspect_device
from .tasks import tasks
from .settings import settings
from .ajax import ajax_system
from .async import async_cve_update, async_cve_update_status
from .async import scan_all_devices_async_status, start_scan_all_devices_async
from .configurations import configurations, delete_configuration, inspect_configuration
from .analysis import analysis
