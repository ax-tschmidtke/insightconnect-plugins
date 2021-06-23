# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Process bytes of base64 encoded string"


class Input:
    BYTES = "bytes"
    EXPRESSION = "expression"
    OPTIONS = "options"
    

class Output:
    OUTPUT = "output"
    

class ProcessBytesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "bytes": {
      "type": "string",
      "title": "Bytes",
      "displayType": "bytes",
      "description": "File/bytes to Process",
      "format": "bytes",
      "order": 1
    },
    "expression": {
      "type": "array",
      "title": "Expression",
      "description": "Sed Expression",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "options": {
      "type": "string",
      "title": "Options",
      "description": "Sed Options",
      "order": 3
    }
  },
  "required": [
    "bytes",
    "expression"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ProcessBytesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "output": {
      "type": "string",
      "title": "Output",
      "description": "Processed String",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)