from scapy.all import *

from CDPModel import CDPModel
from TlvsModels.DeviceIdTlvModel import DeviceIdTlvModel
from LlcModel import LlcModel
from TlvsModels.CapabilitiesTlvModel import CapabilitiesTlvModel
from TlvsModels.PlatformTlvModel import PlatformTlvModel
from TlvsModels.SoftwareTlvModel import SoftwareTlvModel
from EthFrameModel import EthFrameModel
IFACES.show()



interface = IFACES.dev_from_index(1)
sock = conf.L2socket(iface=interface)

cdp = CDPModel()
cdp.add_tlv(DeviceIdTlvModel("Moje PC"))
cdp.add_tlv(PlatformTlvModel("python3"))
cdp.add_tlv(SoftwareTlvModel("Windows 10 x64 22H2"))
cdp.add_tlv(CapabilitiesTlvModel(True,True,True,True))

llc = LlcModel()
llc.add_payload(cdp)
eth_frame = EthFrameModel("01:02:03:04:05:06")
eth_frame.add_payload(llc)

sock.send(eth_frame.to_bytes())
