import comtypes
comtypes.CoInitialize()

import wmi
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Функция для изменения громкости
def set_volume(volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_,0, None)
    volume_object = interface.QueryInterface(IAudioEndpointVolume)
    volume_object.SetMasterVolumeLevelScalar(volume, None)


def set_brightness(brightness):
    wmi_namespace = "root\\WMI"
    wmi_class = "WmiMonitorBrightnessMethods"

    # Инициализация WMI
    wmi_service = wmi.WMI(namespace=wmi_namespace)
    methods = wmi_service.Win32_MonitorBrightnessMethods()[0]

    # Изменение яркости
    methods.WmiSetBrightness(None, brightness)


comtypes.CoUninitialize()