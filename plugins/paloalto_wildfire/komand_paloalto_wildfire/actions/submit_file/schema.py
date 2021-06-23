# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Submit a file for analysis"


class Input:
    FILE = "file"
    FILENAME = "filename"
    

class Output:
    SUBMISSION = "submission"
    

class SubmitFileInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "File to submit. Supported types are Email-link, Flash, APK, PDF, JAR, PE, MS-Office",
      "format": "bytes",
      "order": 1
    },
    "filename": {
      "type": "string",
      "title": "Filename",
      "description": "Optional file name",
      "order": 2
    }
  },
  "required": [
    "file"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubmitFileOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "submission": {
      "$ref": "#/definitions/filedata",
      "title": "Submission",
      "description": "Submission",
      "order": 1
    }
  },
  "required": [
    "submission"
  ],
  "definitions": {
    "filedata": {
      "type": "object",
      "title": "filedata",
      "properties": {
        "filename": {
          "type": "string",
          "title": "Filename",
          "order": 3
        },
        "filetype": {
          "type": "string",
          "title": "File Type",
          "order": 2
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "MD5 hash of file",
          "order": 5
        },
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "SHA256 hash of file",
          "order": 4
        },
        "size": {
          "type": "string",
          "title": "Size",
          "description": "File size",
          "order": 6
        },
        "supported_file_type": {
          "type": "boolean",
          "title": "Supported File",
          "description": "Boolean indicating whether the filetype of the sample is supported",
          "order": 7
        },
        "url": {
          "type": "string",
          "title": "URL",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)