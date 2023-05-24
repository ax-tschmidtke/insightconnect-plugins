# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a new case observable"


class Input:
    DATA = "data"
    DATATYPE = "datatype"
    ID = "id"
    IGNORESIMILARITY = "ignoreSimilarity"
    IOC = "ioc"
    JSONDATA = "jsonData"
    MESSAGE = "message"
    PAP = "pap"
    SIGHTED = "sighted"
    STARTDATE = "startDate"
    TAGS = "tags"
    TLP = "tlp"
    

class Output:
    CASE = "case"
    

class CreateCaseObservableInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "string",
      "title": "Data",
      "description": "Observable's data",
      "order": 10
    },
    "datatype": {
      "type": "string",
      "title": "Data Type",
      "description": "Observables Data Type",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "Case ID",
      "description": "ID for the case",
      "order": 1
    },
    "ignoreSimilarity": {
      "type": "boolean",
      "title": "Ignore Similarity",
      "description": "Observable's similarity ignore flag. True to ignore the observable during similarity computing",
      "default": false,
      "order": 8
    },
    "ioc": {
      "type": "boolean",
      "title": "Indicator of Compromise",
      "description": "Observable's IOC, True to mark an observable as IOC",
      "default": false,
      "order": 6
    },
    "jsonData": {
      "type": "object",
      "title": "JSON Data",
      "description": "All fields included in one JSON object. If using this, all other fields will be ignored",
      "order": 12
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Observable's description. If tags is empty, this is required",
      "order": 3
    },
    "pap": {
      "type": "integer",
      "title": "Password Authentication Protocol",
      "description": "Case's PAP",
      "default": 2,
      "enum": [
        0,
        1,
        2,
        3
      ],
      "order": 5
    },
    "sighted": {
      "type": "boolean",
      "title": "Sighted",
      "description": "Observable's sighted flag, True to mark the observable as sighted",
      "default": false,
      "order": 7
    },
    "startDate": {
      "type": "integer",
      "title": "Start Date",
      "description": "Observable start date (datetime in ms) (will default to now if left blank)",
      "order": 11
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "List of observable tags, required if message is None",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "tlp": {
      "type": "integer",
      "title": "Traffic Light Protocol",
      "description": "Case's TLP",
      "default": 2,
      "enum": [
        0,
        1,
        2,
        3
      ],
      "order": 4
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateCaseObservableOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "case": {
      "$ref": "#/definitions/observable",
      "title": "Case",
      "description": "Create case observable output",
      "order": 1
    }
  },
  "definitions": {
    "observable": {
      "type": "object",
      "title": "observable",
      "properties": {
        "_id": {
          "type": "string",
          "title": "ID",
          "description": "Observable _ID",
          "order": 12
        },
        "_type": {
          "type": "string",
          "title": "Type",
          "description": "Observable type",
          "order": 3
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "Time the observable was created at in milliseconds or epoch",
          "order": 15
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "Observable created by",
          "order": 10
        },
        "data": {
          "type": "string",
          "title": "Data",
          "description": "Observable data",
          "order": 13
        },
        "dataType": {
          "type": "string",
          "title": "Data Type",
          "description": "Observable data type",
          "order": 6
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Observable ID",
          "order": 14
        },
        "ioc": {
          "type": "boolean",
          "title": "IOC",
          "description": "Indicators of Compromise",
          "order": 7
        },
        "message": {
          "type": "string",
          "title": "Message",
          "description": "Observable message",
          "order": 11
        },
        "reports": {
          "type": "object",
          "title": "Reports",
          "description": "Observable reports",
          "order": 8
        },
        "startDate": {
          "type": "integer",
          "title": "Start Date",
          "description": "Observable start date",
          "order": 2
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Observable status",
          "order": 1
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Observable tags",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "tlp": {
          "type": "integer",
          "title": "TLP",
          "description": "Traffic Light Protocol level",
          "order": 4
        },
        "user": {
          "type": "string",
          "title": "User",
          "description": "Observable user",
          "order": 9
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
