# Based on:
#       BCD WMI Provider Reference
#       http://msdn.microsoft.com/en-us/library/aa362677%28v=VS.85%29.aspx
#
#       Boot Configuration Data in Windows Vista
#       http://msdn.microsoft.com/en-us/windows/hardware/gg463059

name_to_id = {
  "BcdBootMgrObjectList_DisplayOrder"        : 0x24000001,
  "BcdBootMgrObjectList_BootSequence"        : 0x24000002,
  "BcdBootMgrObject_DefaultObject"           : 0x23000003,
  "BcdBootMgrInteger_Timeout"                : 0x25000004,
  "BcdBootMgrBoolean_AttemptResume"          : 0x26000005,
  "BcdBootMgrObject_ResumeObject"            : 0x23000006,
  "BcdBootMgrObjectList_ToolsDisplayOrder"   : 0x24000010,
  "BcdBootMgrDevice_BcdDevice"               : 0x21000022,
  "BcdBootMgrString_BcdFilePath"             : 0x22000023,

  "BcdDeviceInteger_RamdiskImageOffset"   : 0x35000001,
  "BcdDeviceInteger_TftpClientPort"       : 0x35000002,
  "BcdDeviceInteger_SdiDevice"            : 0x31000003,
  "BcdDeviceInteger_SdiPath"              : 0x32000004,
  "BcdDeviceInteger_RamdiskImageLength"   : 0x35000005,

  "BcdLibraryDevice_ApplicationDevice"                   : 0x11000001,
  "BcdLibraryString_ApplicationPath"                     : 0x12000002,
  "BcdLibraryString_Description"                         : 0x12000004,
  "BcdLibraryString_PreferredLocale"                     : 0x12000005,
  "BcdLibraryObjectList_InheritedObjects"                : 0x14000006,
  "BcdLibraryInteger_TruncatePhysicalMemory"             : 0x15000007,
  "BcdLibraryObjectList_RecoverySequence"                : 0x14000008,
  "BcdLibraryBoolean_AutoRecoveryEnabled"                : 0x16000009,
  "BcdLibraryIntegerList_BadMemoryList"                  : 0x1700000a,
  "BcdLibraryBoolean_AllowBadMemoryAccess"               : 0x1600000b,
  "BcdLibraryInteger_FirstMegabytePolicy"                : 0x1500000c,
  "BcdLibraryBoolean_DebuggerEnabled"                    : 0x16000010,
  "BcdLibraryInteger_DebuggerType"                       : 0x15000011,
  "BcdLibraryInteger_SerialDebuggerPortAddress"          : 0x15000012,
  "BcdLibraryInteger_SerialDebuggerPort"                 : 0x15000013,
  "BcdLibraryInteger_SerialDebuggerBaudRate"             : 0x15000014,
  "BcdLibraryInteger_1394DebuggerChannel"                : 0x15000015,
  "BcdLibraryString_UsbDebuggerTargetName"               : 0x12000016,
  "BcdLibraryBoolean_DebuggerIgnoreUsermodeExceptions"   : 0x16000017,
  "BcdLibraryInteger_DebuggerStartPolicy"                : 0x15000018,
  "BcdLibraryBoolean_EmsEnabled"                         : 0x16000020,
  "BcdLibraryInteger_EmsPort"                            : 0x15000022,
  "BcdLibraryInteger_EmsBaudRate"                        : 0x15000023,
  "BcdLibraryString_LoadOptionsString"                   : 0x12000030,
  "BcdLibraryBoolean_DisplayAdvancedOptions"             : 0x16000040,
  "BcdLibraryBoolean_DisplayOptionsEdit"                 : 0x16000041,
  "BcdLibraryBoolean_GraphicsModeDisabled"               : 0x16000046,
  "BcdLibraryInteger_ConfigAccessPolicy"                 : 0x15000047,
  "BcdLibraryBoolean_AllowPrereleaseSignatures"          : 0x16000049,

  "BcdMemDiagInteger_PassCount"      : 0x25000001,
  "BcdMemDiagInteger_FailureCount"   : 0x25000003,

  "BcdOSLoaderDevice_OSDevice"                      : 0x21000001,
  "BcdOSLoaderString_SystemRoot"                    : 0x22000002,
  #"BcdOSLoaderObject_AssociatedResumeObject"        : 0x23000003,
  "BcdOSLoaderBoolean_DetectKernelAndHal"           : 0x26000010,
  "BcdOSLoaderString_KernelPath"                    : 0x22000011,
  "BcdOSLoaderString_HalPath"                       : 0x22000012,
  "BcdOSLoaderString_DbgTransportPath"              : 0x22000013,
  "BcdOSLoaderInteger_NxPolicy"                     : 0x25000020,
  "BcdOSLoaderInteger_PAEPolicy"                    : 0x25000021,
  "BcdOSLoaderBoolean_WinPEMode"                    : 0x26000022,
  "BcdOSLoaderBoolean_DisableCrashAutoReboot"       : 0x26000024,
  "BcdOSLoaderBoolean_UseLastGoodSettings"          : 0x26000025,
  "BcdOSLoaderBoolean_AllowPrereleaseSignatures"    : 0x26000027,
  "BcdOSLoaderBoolean_NoLowMemory"                  : 0x26000030,
  "BcdOSLoaderInteger_RemoveMemory"                 : 0x25000031,
  "BcdOSLoaderInteger_IncreaseUserVa"               : 0x25000032,
  "BcdOSLoaderBoolean_UseVgaDriver"                 : 0x26000040,
  "BcdOSLoaderBoolean_DisableBootDisplay"           : 0x26000041,
  "BcdOSLoaderBoolean_DisableVesaBios"              : 0x26000042,
  "BcdOSLoaderInteger_ClusterModeAddressing"        : 0x25000050,
  "BcdOSLoaderBoolean_UsePhysicalDestination"       : 0x26000051,
  "BcdOSLoaderInteger_RestrictApicCluster"          : 0x25000052,
  "BcdOSLoaderBoolean_UseBootProcessorOnly"         : 0x26000060,
  "BcdOSLoaderInteger_NumberOfProcessors"           : 0x25000061,
  "BcdOSLoaderBoolean_ForceMaximumProcessors"       : 0x26000062,
  "BcdOSLoaderBoolean_ProcessorConfigurationFlags"  : 0x25000063,
  "BcdOSLoaderInteger_UseFirmwarePciSettings"       : 0x26000070,
  "BcdOSLoaderInteger_MsiPolicy"                    : 0x26000071,
  "BcdOSLoaderInteger_SafeBoot"                     : 0x25000080,
  "BcdOSLoaderBoolean_SafeBootAlternateShell"       : 0x26000081,
  "BcdOSLoaderBoolean_BootLogInitialization"        : 0x26000090,
  "BcdOSLoaderBoolean_VerboseObjectLoadMode"        : 0x26000091,
  "BcdOSLoaderBoolean_KernelDebuggerEnabled"        : 0x260000a0,
  "BcdOSLoaderBoolean_DebuggerHalBreakpoint"        : 0x260000a1,
  "BcdOSLoaderBoolean_EmsEnabled"                   : 0x260000b0,
  "BcdOSLoaderInteger_DriverLoadFailurePolicy"      : 0x250000c1,
  "BcdOSLoaderInteger_BootStatusPolicy"             : 0x250000E0,
}


id_to_name = dict(((name_to_id[name], name) for name in name_to_id))

id_to_format = {
    0x0 : "UnknownFormat",
    0x1 : "Device",
    0x2 : "String",
    0x3 : "Object",
    0x4 : "ObjectList",
    0x5 : "Integer",
    0x6 : "Boolean",
    0x7 : "IntegerList",
}

id_to_class = {
    0x0 : "UnknownClass",
    0x1 : "Device",
    0x2 : "Application",
    0x3 : "Device",
    0x5 : "OEM",
}

id_to_imagetype = {
    0x1 : "Firmware",
    0x2 : "Boot",
    0x3 : "Legacy Loader",
    0x4 : "Real Mode",
}

id_to_apptype = {
    0x1 : "Firmware boot manager",
    0x2 : "Windows boot manager",
    0x3 : "Windows boot loader",
    0x4 : "Windows resume application",
    0x5 : "Memory tester",
    0x6 : "Legacy NtLdr",
    0x7 : "Legacy SetupLdr",
    0x8 : "Boot sector",
    0x9 : "Startup module",
    0xa : "Generic application",
}

guid_to_name = {
    "9dea862c-5cdd-4e70-acc1-f32b344d4795" : "{bootmgr} Windows Boot Manager",
    "a5a30fa2-3d06-4e9f-b5f4-a01df9d1fcba" : "{fwbootmgr} Firmware Boot Manager",
    "b2721d73-1db4-4c62-bf78-c548a880142d" : "{memdiag} Windows Memory Tester",
    "147aa509-0358-4473-b83b-d950dda00615" : "Windows Resume Application",
    "466f5a88-0af2-4f76-9038-095b170dc21c" : "{ntldr} Legacy Windows Loader",
    "fa926493-6f1c-4193-a414-58f0b2456d1e" : "{current} Current boot entry",

    "5189b25c-5558-4bf2-bca4-289b11bd29e2" : "{badmemory}",
    "6efb52bf-1766-41db-a6b3-0ee5eff72bd7" : "{bootloadersettings}",
    "4636856e-540f-4170-a130-a84776f4c654" : "{dbgsettings}",
    "0ce4991b-e6b3-4b16-b23c-5e0d9250e5d9" : "{emssettings}",
    "7ea2e1ac-2e61-4728-aaa3-896d9d0a9f0e" : "{globalsettings}",
    "1afa9c49-16ab-4a5c-901b-212802da9460" : "{resumeloadersettings}",
}
