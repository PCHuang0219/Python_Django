{"@odata.context": "/redfish/v1/$metadata#MessageRegistry",
  "@odata.id": "/redfish/v1/MessageRegistry",
  "@odata.type": "#MessageRegistry.1.0.0.MessageRegistry",
  "Language": "en_US",
  "RegistryPrefix": "RMM",
  "RegistryVersion": "1.0.0",
  "OwningEntity": "Intel",
  "Messages":
    {"MSGStatusChange":
        {"Description": "Resource Status Change",
         "Message": "Resource status change.\\n",
         "Severity": "N/A",
         "NumberOfArgs": 0,
         "ParamTypes": []
        },
     "MSGResourceUpdated":
        {"Description": "Resource Update",
         "Message": "Resource updated.\\n",
         "Severity": "N/A",
         "NumberOfArgs": 0,
         "ParamTypes": []
        },
     "MSGResourceAdded":
        {"Description": "Resource Add",
          "Message": "Resource add\\n",
          "Severity": "OK",
          "NumberOfArgs": 0,
          "ParamTypes": []
        },
     "MSGResourceRemoved":
        {"Description": "Resource Remove",
         "Message": "Resource removed.\\n",
         "Severity": "OK",
         "NumberOfArgs": 0,
         "ParamTypes": []
        },
     "MSGAlert":
        {"Description": "Resource Alert",
         "Message": "Resource alert.\\n",
         "Severity": "OK",
         "NumberOfArgs": 0,
         "ParamTypes": []
        },
     "MSGDrawerResourceAdded":
        {"Description": "Drawer Add",
         "Message": "Drawer [%string] add\\n",
         "Severity": "OK",
         "NumberOfArgs": 1,
         "ParamTypes": ["string"]
        },
     "MSGDrawerResourceRemoved":
        {"Description": "Drawer Remove",
         "Message": "Drawer [%string] Remove.\\n",
         "Severity": "OK",
         "NumberOfArgs": 1,
         "ParamTypes": ["string"]
         }
     }
 }