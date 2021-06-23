# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Mark a suspicious threat as a threat"


class Input:
    TARGET_SCOPE = "target_scope"
    THREAT_ID = "threat_id"
    WHITENING_OPTION = "whitening_option"
    

class Output:
    AFFECTED = "affected"
    

class MarkAsThreatInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "target_scope": {
      "type": "string",
      "title": "Target Scope",
      "description": "Scope to be used for exclusions",
      "enum": [
        "group",
        "site",
        "tenant"
      ],
      "order": 2
    },
    "threat_id": {
      "type": "string",
      "title": "Threat ID",
      "description": "ID of a threat",
      "order": 1
    },
    "whitening_option": {
      "type": "string",
      "title": "Whitening Option",
      "description": "Selected whitening option",
      "enum": [
        "",
        "browser-type",
        "certificate",
        "file-type",
        "file_hash",
        "path"
      ],
      "order": 3
    }
  },
  "required": [
    "target_scope",
    "threat_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MarkAsThreatOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)