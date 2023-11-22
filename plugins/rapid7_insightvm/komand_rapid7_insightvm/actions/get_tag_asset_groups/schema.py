# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get asset groups associated with a tag"


class Input:
    ID = "id"


class Output:
    ASSET_GROUP_IDS = "asset_group_ids"


class GetTagAssetGroupsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "Tag ID for which to retrieve asset group associations",
      "order": 1
    }
  },
  "required": [
    "id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetTagAssetGroupsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_group_ids": {
      "type": "array",
      "title": "Asset Group IDs",
      "description": "Asset group IDs associated with the tag",
      "items": {
        "type": "integer"
      },
      "order": 1
    }
  },
  "required": [
    "asset_group_ids"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
